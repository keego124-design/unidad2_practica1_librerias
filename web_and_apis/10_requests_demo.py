"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 10_requests_demo.py
LIBRERÍA: requests (Biblioteca Externa)
DESCRIPCIÓN: Consumo robusto de servicios web y APIs REST públicas:
             - Solicitudes HTTP GET a PokeAPI y JSONPlaceholder.
             - Configuración de cabeceras (headers), parámetros y timeouts.
             - Procesamiento de respuestas en formato JSON.
             - Manejo estricto de excepciones (HTTPError, ConnectionError, Timeout).
=============================================================================
"""

import sys
import requests

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def banner(titulo: str):
    """Imprime un separador visual para la consola."""
    print("\n" + "=" * 65)
    print(f" >>> [REQUESTS DEMO] - {titulo}")
    print("=" * 65)


def demo_consumo_pokeapi():
    """Consulta de datos en PokeAPI (API REST Pública) con validación."""
    banner("1. Consulta a PokeAPI (pokemon/pikachu)")
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    headers = {"User-Agent": "TopicosAvanzadosPython/2.0 (Educativo)"}

    print(f"[*] Enviando peticion GET a: {url}...")
    try:
        respuesta = requests.get(url, headers=headers, timeout=8.0)
        # Verifica si el código de estado es 200 OK (lanza HTTPError si es 4xx o 5xx)
        respuesta.raise_for_status()

        datos = respuesta.json()
        print(f"    [OK] Codigo HTTP: {respuesta.status_code} OK")
        print(f"    - Nombre Pokemon   : {datos['name'].capitalize()}")
        print(f"    - ID Nacional      : #{datos['id']}")
        print(f"    - Altura           : {datos['height'] / 10:.1f} m")
        print(f"    - Peso             : {datos['weight'] / 10:.1f} kg")
        print(f"    - Experiencia Base : {datos['base_experience']} XP")

        tipos = [t["type"]["name"].capitalize() for t in datos["types"]]
        print(f"    - Tipos Elementales: {', '.join(tipos)}")

        habilidades = [h["ability"]["name"].capitalize() for h in datos["abilities"]]
        print(f"    - Habilidades      : {', '.join(habilidades)}")

    except requests.exceptions.Timeout:
        print("[!] Error: Se agoto el tiempo de espera (Timeout) al conectar con PokeAPI.")
    except requests.exceptions.ConnectionError:
        print("[!] Error de Red: No se pudo establecer conexion con el servidor remoto.")
    except requests.exceptions.HTTPError as http_err:
        print(f"[!] Error HTTP detectado: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"[!] Error inesperado en la solicitud: {err}")


def demo_consumo_jsonplaceholder():
    """Consulta de recursos estructurados en JSONPlaceholder (Mock API)."""
    banner("2. Consulta a JSONPlaceholder (posts y usuarios)")
    url = "https://jsonplaceholder.typicode.com/posts/1"

    print(f"[*] Consultando Post #1 en: {url}...")
    try:
        res = requests.get(url, timeout=5.0)
        res.raise_for_status()
        post = res.json()

        print(f"    [OK] Codigo HTTP: {res.status_code}")
        print(f"    - User ID  : {post['userId']}")
        print(f"    - Post ID  : {post['id']}")
        print(f"    - Titulo   : {post['title']}")
        print(f"    - Cuerpo   : {post['body'][:80]}...")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error al consumir JSONPlaceholder: {e}")


def demo_manejo_errores_404():
    """Demostración de captura controlada de errores 404 (Not Found)."""
    banner("3. Manejo Controlado de Excepciones HTTP (Simulacion 404)")
    url_inexistente = "https://jsonplaceholder.typicode.com/recurso_que_no_existe_99999"

    print(f"[*] Solicitando ruta intencionalmente invalida:\n    {url_inexistente}")
    try:
        resp = requests.get(url_inexistente, timeout=5.0)
        print(f"[*] Codigo recibido: {resp.status_code}")
        resp.raise_for_status()

    except requests.exceptions.HTTPError as e:
        print(f"    [CONTROLADO] Se capturo HTTPError exitosamente:")
        print(f"    -> Detalle: El recurso no fue encontrado (Status {resp.status_code}). El programa continua sin colapsar.")
    except Exception as e:
        print(f"    [!] Error general: {e}")


def main():
    print("\n" + "#" * 65)
    print(" EJECUCIÓN DEL MÓDULO: requests")
    print(" Cliente HTTP para comunicacion con APIs REST y microservicios")
    print("#" * 65)

    demo_consumo_pokeapi()
    demo_consumo_jsonplaceholder()
    demo_manejo_errores_404()

    print("\n[OK] Demostración de requests finalizada con éxito.\n")


if __name__ == "__main__":
    main()
