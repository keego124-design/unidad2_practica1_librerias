"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: run_all.py
DESCRIPCIÓN: Lanzador maestro interactivo estilo consola Neón:
             - Menú interactivo con estética de terminal de alta definición.
             - Ejecución selectiva de cualquiera de los 12 scripts modulares.
             - Ejecución secuencial completa de toda la suite con reporte de estado.
             - Lanzamiento directo del servidor web Flask interactivo.
=============================================================================
"""

import sys
import subprocess
from pathlib import Path

# Soporte UTF-8 en consolas Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent

# Códigos de escape ANSI para colores neón en terminal
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_NEON_AZUL = "\033[96m"      # Cyan / Azul Neón
C_NEON_SKY = "\033[94m"       # Azul brillante
C_WHITE = "\033[97m"          # Blanco intenso
C_MUTED = "\033[90m"          # Gris atenuado
C_GREEN = "\033[92m"          # Verde éxito
C_RED = "\033[91m"            # Rojo error

MODULOS = [
    # (Código, Nombre de Librería, Ruta Relativa, Categoría)
    ("01", "math", "standard_library/01_math_demo.py", "Biblioteca Estándar"),
    ("02", "random", "standard_library/02_random_demo.py", "Biblioteca Estándar"),
    ("03", "datetime", "standard_library/03_datetime_demo.py", "Biblioteca Estándar"),
    ("04", "csv", "standard_library/04_csv_demo.py", "Biblioteca Estándar"),
    ("05", "fpdf", "pdf_generation/05_fpdf_demo.py", "Generación PDF"),
    ("06", "reportlab", "pdf_generation/06_reportlab_demo.py", "Generación PDF"),
    ("07", "numpy", "data_science/07_numpy_demo.py", "Ciencia de Datos"),
    ("08", "pandas", "data_science/08_pandas_demo.py", "Ciencia de Datos"),
    ("09", "matplotlib", "data_science/09_matplotlib_demo.py", "Ciencia de Datos"),
    ("10", "requests", "web_and_apis/10_requests_demo.py", "Web & APIs"),
    ("11", "flask", "web_and_apis/11_flask_demo.py", "Web & APIs"),
    ("12", "scikit-learn", "machine_learning/12_sklearn_demo.py", "Machine Learning"),
]


def imprimir_banner():
    banner = f"""
{C_NEON_AZUL}=============================================================================
  ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
  ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
  ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
  ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
  ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
  ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
  >>> UNIDAD 2 PRÁCTICA 1: EJEMPLOS DE LIBRERÍAS DE PYTHON <<<
============================================================================={C_RESET}
{C_WHITE}  Estética:{C_RESET} Fondo Negro | {C_NEON_AZUL}Detalles Azul Neón{C_RESET} | {C_WHITE}Textos en Blanco{C_RESET}
{C_MUTED}  Materia :{C_RESET} Tópicos Avanzados de Programación
"""
    print(banner)


def ejecutar_script(ruta_relativa: str, argumentos: list = None) -> bool:
    """Ejecuta un script de Python mediante un subproceso aislado."""
    ruta_absoluta = BASE_DIR / ruta_relativa
    if not ruta_absoluta.exists():
        print(f"{C_RED}[!] Error: No se localizó el archivo en {ruta_absoluta}{C_RESET}")
        return False

    cmd = [sys.executable, str(ruta_absoluta)]
    if argumentos:
        cmd.extend(argumentos)

    try:
        resultado = subprocess.run(cmd)
        return resultado.returncode == 0
    except Exception as e:
        print(f"{C_RED}[!] Excepción al ejecutar {ruta_relativa}: {e}{C_RESET}")
        return False


def ejecutar_todos():
    """Ejecuta secuencialmente los 12 módulos y genera reporte de estado."""
    print(f"\n{C_NEON_AZUL}{C_BOLD}[*] INICIANDO EJECUCIÓN SECUENCIAL DE LOS 12 MÓDULOS...{C_RESET}\n")

    exitos = 0
    errores = 0
    reporte = []

    for codigo, nombre, ruta, categoria in MODULOS:
        print(f"{C_NEON_SKY}---> Ejecutando [{codigo}] {nombre} ({categoria})...{C_RESET}")
        ok = ejecutar_script(ruta)
        if ok:
            exitos += 1
            reporte.append((codigo, nombre, "EXITOSO", C_GREEN))
        else:
            errores += 1
            reporte.append((codigo, nombre, "FALLIDO", C_RED))

    # Resumen final
    print("\n" + "=" * 65)
    print(f"{C_BOLD}{C_WHITE} RESUMEN DE EJECUCIÓN DE LA PRÁCTICA{C_RESET}")
    print("=" * 65)
    for cod, nom, est, color in reporte:
        print(f"  [{cod}] {nom:<15} : {color}{est}{C_RESET}")
    print("-" * 65)
    print(f"  Total Exitosos : {C_GREEN}{exitos} / 12{C_RESET}")
    print(f"  Total Errores  : {C_RED}{errores}{C_RESET}")
    print("=" * 65)


def menu_interactivo():
    while True:
        imprimir_banner()
        print(f"{C_BOLD}{C_WHITE}SELECCIONA UNA OPCIÓN:{C_RESET}\n")

        for cod, nombre, _, cat in MODULOS:
            print(f"  {C_NEON_AZUL}[{cod}]{C_RESET} {C_WHITE}{nombre:<14}{C_RESET} {C_MUTED}({cat}){C_RESET}")

        print(f"\n  {C_GREEN}[A]{C_RESET}  {C_BOLD}Ejecutar TODOS los 12 scripts en secuencia{C_RESET}")
        print(f"  {C_NEON_SKY}[W]{C_RESET}  {C_BOLD}Lanzar Servidor Web Flask interactivo (--serve en puerto 5000){C_RESET}")
        print(f"  {C_MUTED}[0]{C_RESET}  Salir del lanzador\n")

        opcion = input(f"{C_NEON_AZUL}Ingresa tu opción >> {C_RESET}").strip().upper()

        if opcion == "0":
            print(f"\n{C_WHITE}¡Hasta pronto! Práctica 1 finalizada.{C_RESET}\n")
            break
        elif opcion == "A":
            ejecutar_todos()
            input(f"\n{C_MUTED}Presiona Enter para volver al menú principal...{C_RESET}")
        elif opcion == "W":
            print(f"\n{C_NEON_AZUL}[*] Iniciando Flask Web Server en vivo...{C_RESET}")
            ejecutar_script("web_and_apis/11_flask_demo.py", ["--serve"])
            input(f"\n{C_MUTED}Presiona Enter para volver al menú principal...{C_RESET}")
        else:
            # Buscar script individual por código o nombre
            seleccionado = next((m for m in MODULOS if m[0] == opcion or m[1].lower() == opcion.lower()), None)
            if seleccionado:
                cod, nom, ruta, cat = seleccionado
                print(f"\n{C_NEON_AZUL}[*] Ejecutando demostración de '{nom}'...{C_RESET}\n")
                ejecutar_script(ruta)
                input(f"\n{C_MUTED}Presiona Enter para continuar...{C_RESET}")
            else:
                print(f"\n{C_RED}[!] Opción no reconocida. Intenta de nuevo.{C_RESET}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        ejecutar_todos()
    else:
        menu_interactivo()


if __name__ == "__main__":
    main()
