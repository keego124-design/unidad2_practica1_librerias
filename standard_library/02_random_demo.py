"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 02_random_demo.py
LIBRERÍA: random (Biblioteca Estándar de Python)
DESCRIPCIÓN: Demostración del generador de números pseudoaleatorios:
             - Generación de números enteros y flotantes continuos.
             - Selección aleatoria simple y con pesos ponderados.
             - Muestreo sin reemplazo y permutación/mezcla de secuencias.
             - Reproducibilidad mediante semillas deterministas (seed).
=============================================================================
"""

import sys
import random

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def banner(titulo: str):
    """Imprime un separador visual para la consola."""
    print("\n" + "=" * 65)
    print(f" >>> [RANDOM DEMO] - {titulo}")
    print("=" * 65)


def demo_generacion_basica():
    """Generación de flotantes y enteros aleatorios."""
    banner("1. Generación de Valores Numéricos Aleatorios")
    flotante_cero_uno = random.random()
    print(f"[*] random.random() [0.0, 1.0)              : {flotante_cero_uno:.6f}")

    dado_6_caras = random.randint(1, 6)
    print(f"[*] random.randint(1, 6) (Tiro de dado)     : {dado_6_caras}")

    temperatura = random.uniform(18.5, 32.0)
    print(f"[*] random.uniform(18.5, 32.0) (grados C)   : {temperatura:.2f} C")

    par_aleatorio = random.randrange(10, 31, 2)
    print(f"[*] random.randrange(10, 31, paso=2)        : {par_aleatorio}")


def demo_elecciones_y_ponderacion():
    """Selección de elementos simples y selecciones ponderadas."""
    banner("2. Selecciones de Elementos (Choices)")
    lenguajes = ["Python", "JavaScript", "Rust", "Go", "C++", "Java"]
    print(f"[*] Lista de lenguajes disponibles          : {lenguajes}")

    seleccionado = random.choice(lenguajes)
    print(f"[*] random.choice(lenguajes)                : {seleccionado}")

    pesos = [50, 15, 25, 5, 3, 2]
    muestras = random.choices(lenguajes, weights=pesos, k=5)
    print(f"[*] random.choices(weights=[50,15,25,...], k=5): {muestras}")


def demo_mezclas_y_muestreo():
    """Barajado y muestreo estadístico sin reemplazo."""
    banner("3. Mezcla (Shuffle) y Muestreo sin Reemplazo (Sample)")
    mazo = ["As de Espadas", "Rey de Corazones", "Reina de Diamantes", "Joker", "7 de Treboles"]
    print(f"[*] Mazo ordenado original                  : {mazo}")

    mazo_barajado = mazo.copy()
    random.shuffle(mazo_barajado)
    print(f"[*] random.shuffle(mazo_barajado)           : {mazo_barajado}")

    mano_poker = random.sample(mazo, k=3)
    print(f"[*] random.sample(mazo, k=3) (Sin repeticion): {mano_poker}")


def demo_semilla_determinista():
    """Demostración de reproducibilidad con random.seed."""
    banner("4. Reproducibilidad Determinista con random.seed()")
    print("[*] Fijando semilla = 42...")
    random.seed(42)
    secuencia_1 = [random.randint(1, 100) for _ in range(5)]
    print(f"    Secuencia 1 con seed(42): {secuencia_1}")

    print("[*] Reiniciando la misma semilla = 42...")
    random.seed(42)
    secuencia_2 = [random.randint(1, 100) for _ in range(5)]
    print(f"    Secuencia 2 con seed(42): {secuencia_2}")

    print(f"[*] ¿Las secuencias son idénticas?: {secuencia_1 == secuencia_2} (Garantiza reproducibilidad en pruebas)")


def main():
    print("\n" + "#" * 65)
    print(" EJECUCIÓN DEL MÓDULO: random")
    print(" Generación y manejo de aleatoriedad determinista y pseudoaleatoria")
    print("#" * 65)

    demo_generacion_basica()
    demo_elecciones_y_ponderacion()
    demo_mezclas_y_muestreo()
    demo_semilla_determinista()

    print("\n[OK] Demostración de random finalizada con éxito.\n")


if __name__ == "__main__":
    main()
