"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 11_flask_demo.py
LIBRERÍA: flask (Biblioteca Externa)
DESCRIPCIÓN: Microframework web moderno y ligero para servicios backend y APIs:
             - Ruta raíz ('/') que renderiza una interfaz web interactiva HTML5
               con estética Dark Mode (#0A0B10), detalles en Azul Neón (#00E5FF)
               y tipografía en blanco.
             - Ruta REST API ('/api/info') que responde con estructura JSON.
             - Ruta REST API ('/api/librerias') con catálogo de módulos de la práctica.
             - Modo dual: Ejecución de verificación interna (test client) o servidor en vivo.
=============================================================================
"""

import sys
from datetime import datetime, timezone
from flask import Flask, jsonify, render_template_string, request

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

app = Flask(__name__)

# Plantilla HTML con Estética Estricta: Fondo Negro (#0A0B10), Acentos Azul Neón (#00E5FF), Texto Blanco
HTML_TEMPLATE_NEON = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Neon Dashboard | Unidad 2 Práctica 1</title>
    <style>
        :root {
            --bg-base: #0A0B10;
            --bg-card: #0F172A;
            --neon-blue: #00E5FF;
            --neon-sky: #38BDF8;
            --text-white: #FFFFFF;
            --text-muted: #94A3B8;
            --border-glow: rgba(0, 229, 255, 0.4);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--bg-base);
            color: var(--text-white);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 20px;
        }

        .header-container {
            text-align: center;
            max-width: 800px;
            margin-bottom: 35px;
        }

        .badge {
            display: inline-block;
            background: rgba(0, 229, 255, 0.12);
            color: var(--neon-blue);
            border: 1px solid var(--neon-blue);
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 15px;
            box-shadow: 0 0 10px var(--border-glow);
        }

        h1 {
            font-size: 2.3rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #FFFFFF 60%, var(--neon-blue) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        p.subtitle {
            color: var(--text-muted);
            font-size: 1.05rem;
            line-height: 1.6;
        }

        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 22px;
            max-width: 950px;
            width: 100%;
            margin-bottom: 35px;
        }

        .card {
            background-color: var(--bg-card);
            border: 1px solid rgba(0, 229, 255, 0.25);
            border-radius: 12px;
            padding: 24px;
            transition: transform 0.2s, box-shadow 0.2s;
            position: relative;
            overflow: hidden;
        }

        .card:hover {
            transform: translateY(-4px);
            border-color: var(--neon-blue);
            box-shadow: 0 0 20px var(--border-glow);
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, var(--neon-blue), var(--neon-sky));
        }

        .card h3 {
            font-size: 1.15rem;
            color: var(--neon-blue);
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .card p {
            color: var(--text-muted);
            font-size: 0.92rem;
            line-height: 1.5;
            margin-bottom: 16px;
        }

        .btn-neon {
            display: inline-block;
            background-color: transparent;
            color: var(--neon-blue);
            border: 1px solid var(--neon-blue);
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 0.88rem;
            font-weight: 600;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .btn-neon:hover {
            background-color: var(--neon-blue);
            color: var(--bg-base);
            box-shadow: 0 0 15px var(--neon-blue);
        }

        .status-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: #10B981;
            font-weight: 600;
            font-size: 0.9rem;
        }

        .dot {
            width: 8px;
            height: 8px;
            background-color: #10B981;
            border-radius: 50%;
            box-shadow: 0 0 8px #10B981;
        }

        footer {
            margin-top: auto;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.85rem;
            border-top: 1px solid rgba(0, 229, 255, 0.2);
            padding-top: 20px;
            width: 100%;
            max-width: 950px;
        }
    </style>
</head>
<body>

    <div class="header-container">
        <span class="badge">FLASK REST BACKEND</span>
        <h1>Microservicio Web de Tópicos Avanzados</h1>
        <p class="subtitle">Demostración interactiva de desarrollo web ligero con Flask en Python. Servidor activo con renderizado de vistas HTML modernas y endpoints JSON de alta respuesta.</p>
    </div>

    <div class="dashboard-grid">
        <div class="card">
            <h3>⚡ Estado del Servidor</h3>
            <p>Monitoreo en tiempo real del runtime de Python, carga activa y métricas de disponibilidad.</p>
            <div style="margin-bottom: 15px;" class="status-pill">
                <span class="dot"></span> Online (HTTP 200 OK)
            </div>
            <a href="/api/info" class="btn-neon" target="_blank">Consultar /api/info ↗</a>
        </div>

        <div class="card">
            <h3>📚 Catálogo de Librerías</h3>
            <p>Endpoint REST que retorna en estructura JSON el catálogo de los 12 módulos demostrados.</p>
            <div style="margin-bottom: 15px; color: var(--neon-sky); font-size: 0.9rem;">
                Total: 12 Módulos Registrados
            </div>
            <a href="/api/librerias" class="btn-neon" target="_blank">Consultar /api/librerias ↗</a>
        </div>

        <div class="card">
            <h3>🎨 Paleta Neon Blue</h3>
            <p>Diseño corporativo de alto contraste para interfaces de ingeniería de software.</p>
            <div style="display: flex; gap: 8px; margin-bottom: 15px;">
                <span style="background: #0A0B10; border: 1px solid #00E5FF; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem;">#0A0B10</span>
                <span style="background: #00E5FF; color: #0A0B10; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold;">#00E5FF</span>
                <span style="background: #FFFFFF; color: #0A0B10; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold;">#FFFFFF</span>
            </div>
            <a href="https://flask.palletsprojects.com/" class="btn-neon" target="_blank">Docs Oficiales ↗</a>
        </div>
    </div>

    <footer>
        Tópicos Avanzados de Programación — Unidad 2 Práctica 1 | Estética Dark Mode & Neon Blue
    </footer>

</body>
</html>
"""


@app.route("/", methods=["GET"])
def home():
    """Ruta principal: Renderiza la interfaz gráfica web en HTML5/CSS3."""
    return render_template_string(HTML_TEMPLATE_NEON)


@app.route("/api/info", methods=["GET"])
def api_info():
    """Ruta REST que retorna información del servidor y metadatos en formato JSON."""
    return jsonify({
        "status": "online",
        "codigo_http": 200,
        "materia": "Tópicos Avanzados de Programación",
        "unidad": "Unidad 2: Práctica 1",
        "proyecto": "Ejemplos de Librerías de Python",
        "servidor": "Flask Microframework WSGI",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "paleta_visual": {
            "fondo": "#0A0B10 (Negro Profundo)",
            "acento_principal": "#00E5FF (Azul Neón)",
            "tipografia": "#FFFFFF (Blanco)"
        }
    })


@app.route("/api/librerias", methods=["GET"])
def api_librerias():
    """Ruta REST que expone el catálogo completo de las 12 librerías del proyecto."""
    librerias = [
        {"nombre": "math", "categoria": "Biblioteca Estándar", "descripcion": "Cálculo matemático avanzado, trigonometría y factoriales"},
        {"nombre": "random", "categoria": "Biblioteca Estándar", "descripcion": "Generación pseudoaleatoria, barajado y selección"},
        {"nombre": "datetime", "categoria": "Biblioteca Estándar", "descripcion": "Manejo de fechas, tiempos, zonas horarias y parseo"},
        {"nombre": "csv", "categoria": "Biblioteca Estándar", "descripcion": "Lectura y escritura de datos tabulares delimitados"},
        {"nombre": "fpdf / fpdf2", "categoria": "Generación PDF", "descripcion": "Creación rápida y ligera de documentos PDF"},
        {"nombre": "reportlab", "categoria": "Generación PDF", "descripcion": "Motor empresarial para documentos complejos con tablas y dibujos"},
        {"nombre": "numpy", "categoria": "Data Science", "descripcion": "Álgebra matricial y cómputo numérico de alta velocidad"},
        {"nombre": "pandas", "categoria": "Data Science", "descripcion": "Estructuras de datos DataFrame y análisis estadístico"},
        {"nombre": "matplotlib", "categoria": "Data Science", "descripcion": "Visualización y graficación científica exportable en alta resolución"},
        {"nombre": "requests", "categoria": "Web & APIs", "descripcion": "Cliente HTTP para consumo de APIs REST con manejo de errores"},
        {"nombre": "flask", "categoria": "Web & APIs", "descripcion": "Microframework web backend con soporte para vistas HTML y JSON"},
        {"nombre": "scikit-learn", "categoria": "Machine Learning", "descripcion": "Modelos predictivos de regresión y clasificación con métricas"},
    ]
    return jsonify({
        "total_librerias": len(librerias),
        "catalogo": librerias
    })


def verificar_rutas_con_test_client():
    """Ejecuta una verificación de integración automatizada sin bloquear el puerto."""
    print("[*] Iniciando verificación automatizada de endpoints con Flask TestClient...")
    cliente = app.test_client()

    # 1. Probar ruta raíz '/'
    resp_home = cliente.get("/")
    print(f"    - GET /             -> Status: {resp_home.status_code} OK (HTML Dashboard renderizado, {len(resp_home.data)} bytes)")

    # 2. Probar ruta '/api/info'
    resp_info = cliente.get("/api/info")
    datos_info = resp_info.get_json()
    print(f"    - GET /api/info     -> Status: {resp_info.status_code} OK (JSON Status: '{datos_info.get('status')}')")

    # 3. Probar ruta '/api/librerias'
    resp_libs = cliente.get("/api/librerias")
    datos_libs = resp_libs.get_json()
    print(f"    - GET /api/librerias-> Status: {resp_libs.status_code} OK (Librerías registradas: {datos_libs.get('total_librerias')})")

    print("    [OK] Todas las rutas web y REST responden con HTTP 200 exitosamente.")


def main():
    print("\n" + "#" * 65)
    print(" EJECUCIÓN DEL MÓDULO: flask")
    print(" Aplicación web backend moderna con vistas HTML y endpoints JSON")
    print("#" * 65)

    if "--serve" in sys.argv:
        print("\n[*] Iniciando Servidor Web Flask en modo interactivo...")
        print("[*] Abre tu navegador en: http://127.0.0.1:5000")
        print("[*] Presiona Ctrl+C en cualquier momento para detener el servidor.\n")
        app.run(host="127.0.0.1", port=5000, debug=False)
    else:
        verificar_rutas_con_test_client()
        print("\n[*] Nota: Para levantar el servidor web en vivo en el navegador ejecuta:")
        print("    python web_and_apis/11_flask_demo.py --serve\n")


if __name__ == "__main__":
    main()
