"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 01_math_demo.py
LIBRERÍA: math (Biblioteca Estándar de Python)
DESCRIPCIÓN: Demostración de funciones matemáticas avanzadas:
             - Constantes matemáticas (pi, e, tau).
             - Trigonometría y conversión angular.
             - Factoriales, combinatoria y divisibilidad (gcd, lcm).
             - Logaritmos y exponenciación.
=============================================================================
"""

import sys
import math

# Asegurar codificación UTF-8 en consolas de Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def banner(titulo: str):
    """Imprime un separador visual de alto contraste en consola."""
    print("\n" + "=" * 65)
    print(f" >>> [MATH DEMO] - {titulo}")
    print("=" * 65)


def demo_constantes():
    """Muestra el uso de constantes fundamentales provistas por math."""
    banner("1. Constantes Matemáticas Fundamentales")
    print(f"[*] Valor de Pi (pi)              : {math.pi:.10f}")
    print(f"[*] Base del logaritmo natural (e): {math.e:.10f}")
    print(f"[*] Constante Tau (2*pi)          : {math.tau:.10f}")
    print(f"[*] Infinito positivo (inf)       : {math.inf}")
    print(f"[*] ¿Es finito math.pi?           : {math.isfinite(math.pi)}")


def demo_trigonometria():
    """Ejemplos de funciones trigonométricas e hiperbólicas."""
    banner("2. Trigonometría y Conversión de Ángulos")
    angulo_grados = 45.0
    # math.sin, cos y tan esperan radianes, por lo que convertimos primero
    angulo_radianes = math.radians(angulo_grados)

    print(f"[*] Ángulo original en grados    : {angulo_grados}°")
    print(f"[*] Conversión a radianes        : {angulo_radianes:.6f} rad")
    print(f"[*] Seno(45°)                    : {math.sin(angulo_radianes):.6f}")
    print(f"[*] Coseno(45°)                  : {math.cos(angulo_radianes):.6f}")
    print(f"[*] Tangente(45°)                : {math.tan(angulo_radianes):.6f}")

    # Teorema de Pitágoras con math.hypot (hipotenusa de catetos 3 y 4)
    cateto_a, cateto_b = 3.0, 4.0
    hipotenusa = math.hypot(cateto_a, cateto_b)
    print(f"[*] Hipotenusa para catetos {cateto_a} y {cateto_b}: {hipotenusa}")


def demo_aritmetica_avanzada():
    """Demostración de factoriales, combinatoria y máximo común divisor."""
    banner("3. Factoriales, Divisibilidad y Aritmética Avanzada")
    numero = 6
    print(f"[*] Factorial de {numero} ({numero}!)       : {math.factorial(numero)}")

    # Combinaciones: nCr = n! / (r! * (n - r)!)
    n, r = 10, 3
    print(f"[*] Combinaciones de {n} elementos tomados de {r} en {r} (math.comb): {math.comb(n, r)}")

    # Máximo Común Divisor (GCD) y Mínimo Común Múltiplo (LCM)
    a, b = 48, 180
    print(f"[*] MCD (Greatest Common Divisor) de {a} y {b}: {math.gcd(a, b)}")
    print(f"[*] MCM (Least Common Multiple) de {a} y {b}  : {math.lcm(a, b)}")


def demo_logaritmos_y_potencias():
    """Manejo de potencias, raíces y funciones logarítmicas."""
    banner("4. Logaritmos y Funciones Exponenciales")
    valor = 100.0
    print(f"[*] Raíz cuadrada de {valor}               : {math.sqrt(valor)}")
    print(f"[*] Logaritmo natural (base e) de {valor} : {math.log(valor):.4f}")
    print(f"[*] Logaritmo en base 10 de {valor}       : {math.log10(valor)}")
    print(f"[*] Logaritmo en base 2 de 64            : {math.log2(64)}")
    print(f"[*] Exponencial e^2                      : {math.exp(2):.4f}")
    print(f"[*] Redondeo hacia arriba (ceil de 4.12) : {math.ceil(4.12)}")
    print(f"[*] Redondeo hacia abajo (floor de 4.89): {math.floor(4.89)}")


def main():
    print("\n" + "#" * 65)
    print(" EJECUCIÓN DEL MÓDULO: math")
    print(" Biblioteca estándar de operaciones numéricas y científicas")
    print("#" * 65)

    demo_constantes()
    demo_trigonometria()
    demo_aritmetica_avanzada()
    demo_logaritmos_y_potencias()

    print("\n[OK] Demostración de math finalizada con éxito.\n")


if __name__ == "__main__":
    main()
