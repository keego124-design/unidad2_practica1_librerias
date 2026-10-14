"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 07_numpy_demo.py
LIBRERÍA: numpy (Biblioteca Externa)
DESCRIPCIÓN: Cómputo numérico de alto rendimiento con arreglos N-dimensionales:
             - Inicialización de ndarrays (zeros, ones, arange, linspace).
             - Manipulación de formas (reshape, transpose, aplanado).
             - Operaciones vectorizadas element-wise y broadcasting.
             - Álgebra lineal básica (producto punto, multiplicación matricial).
             - Cálculo estadístico acelerado (media, desviación, varianza).
=============================================================================
"""

import sys
import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def banner(titulo: str):
    """Imprime un separador visual para la consola."""
    print("\n" + "=" * 65)
    print(f" >>> [NUMPY DEMO] - {titulo}")
    print("=" * 65)


def demo_creacion_y_atributos():
    """Creación básica e inspección de memoria/dimensiones de ndarrays."""
    banner("1. Creación e Inspección de ndarrays")

    # Vector 1D
    v1 = np.array([10, 20, 30, 40, 50], dtype=np.int32)
    print(f"[*] Arreglo 1D (v1)               : {v1}")
    print(f"    - Forma (shape): {v1.shape} | Tipo: {v1.dtype} | Dimensión: {v1.ndim}D")

    # Matriz 2D
    m2 = np.array([[1.5, 2.8, 3.2], [4.1, 5.0, 6.7]], dtype=np.float64)
    print(f"[*] Matriz 2D (m2):\n{m2}")
    print(f"    - Filas y columnas: {m2.shape} | Total elementos: {m2.size}")

    # Generadores automáticos
    ceros = np.zeros((2, 3), dtype=int)
    unos = np.ones((2, 3), dtype=float)
    espaciado_lineal = np.linspace(0.0, 1.0, 5)  # 5 valores equidistantes entre 0 y 1

    print(f"[*] np.zeros((2, 3)):\n{ceros}")
    print(f"[*] np.linspace(0.0, 1.0, 5): {espaciado_lineal}")


def demo_reshaping_y_slicing():
    """Redimensionamiento e indexación avanzada."""
    banner("2. Reshaping, Slicing y Segmentación")

    secuencia = np.arange(1, 13)  # Arreglo de 1 al 12
    print(f"[*] Arreglo 1D original (np.arange(1, 13)):\n    {secuencia}")

    # Redimensionar a 3 filas y 4 columnas
    matriz_3x4 = secuencia.reshape((3, 4))
    print(f"[*] Transformado con .reshape(3, 4):\n{matriz_3x4}")

    # Slicing: Submatriz (filas 0 y 1, columnas 1 y 2)
    submatriz = matriz_3x4[0:2, 1:3]
    print(f"[*] Submatriz [0:2, 1:3]:\n{submatriz}")

    # Transpuesta de la matriz
    print(f"[*] Matriz Transpuesta (.T):\n{matriz_3x4.T}")


def demo_broadcasting_y_operaciones():
    """Aritmética vectorizada y reglas de broadcasting."""
    banner("3. Operaciones Vectorizadas y Broadcasting")

    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])

    print(f"[*] Vector A                     : {a}")
    print(f"[*] Vector B                     : {b}")
    print(f"[*] Suma elemento a elemento (A+B): {a + b}")
    print(f"[*] Multiplicación (A * B)       : {a * b}")
    print(f"[*] Potenciación (A ** 2)        : {a ** 2}")

    # Broadcasting: Escalar sobre matriz
    matriz = np.ones((2, 2)) * 5
    print(f"[*] Matriz base:\n{matriz}")
    print(f"[*] Broadcasting escalar (+10):\n{matriz + 10}")


def demo_algebra_lineal_y_estadistica():
    """Cálculo matricial y agregaciones estadísticas."""
    banner("4. Álgebra Lineal y Estadísticas")

    # Producto punto y multiplicación de matrices
    m_a = np.array([[1, 2], [3, 4]])
    m_b = np.array([[5, 6], [7, 8]])

    producto_matricial = m_a @ m_b  # Operador @ para producto matricial
    print(f"[*] Multiplicación Matricial (m_a @ m_b):\n{producto_matricial}")

    # Muestras aleatorias con distribución normal
    np.random.seed(123)
    datos_simulados = np.random.normal(loc=100.0, scale=15.0, size=1000)

    print(f"[*] Métricas Estadísticas sobre muestra (N=1000):")
    print(f"    - Media aritmética   : {np.mean(datos_simulados):.2f}")
    print(f"    - Desviación estándar: {np.std(datos_simulados):.2f}")
    print(f"    - Varianza           : {np.var(datos_simulados):.2f}")
    print(f"    - Valor Mínimo       : {np.min(datos_simulados):.2f}")
    print(f"    - Valor Máximo       : {np.max(datos_simulados):.2f}")
    print(f"    - Percentil 50 (Med) : {np.percentile(datos_simulados, 50):.2f}")


def main():
    print("\n" + "#" * 65)
    print(" EJECUCIÓN DEL MÓDULO: numpy")
    print(" Biblioteca fundamental para cómputo científico y arrays N-D")
    print("#" * 65)

    demo_creacion_y_atributos()
    demo_reshaping_y_slicing()
    demo_broadcasting_y_operaciones()
    demo_algebra_lineal_y_estadistica()

    print("\n[OK] Demostración de numpy finalizada con éxito.\n")


if __name__ == "__main__":
    main()
