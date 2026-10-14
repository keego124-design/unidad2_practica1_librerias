"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 09_matplotlib_demo.py
LIBRERÍA: matplotlib (Biblioteca Externa)
DESCRIPCIÓN: Visualización gráfica de datos con estética Dark Mode y Azul Neón:
             - Configuración completa de estilos (fondo negro, acentos neón, texto blanco).
             - Gráficas de líneas múltiples con sombreado de área (glow effect).
             - Gráfica de barras comparativa con anotación de valores numéricos.
             - Exportación automatizada a imagen PNG de alta resolución (300 DPI).
=============================================================================
"""

import sys
from pathlib import Path
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Usar backend 'Agg' para generar gráficos sin requerir ventana interactiva X11/GUI
matplotlib.use("Agg")

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
IMG_OUTPUT_PATH = OUTPUT_DIR / "grafico_rendimiento_neon.png"

# Paleta Estricta: Fondo Negro, Detalles en Azul Neón, Textos en Blanco
COLOR_BG_FIGURA = "#0A0B10"     # Negro azulado profundo
COLOR_BG_AXES = "#0F172A"       # Azul noche / pizarra
COLOR_NEON_AZUL = "#00E5FF"     # Azul Neón principal (Cyan eléctrico)
COLOR_NEON_SKY = "#38BDF8"      # Azul Neón secundario
COLOR_NEON_INDIGO = "#818CF8"   # Acento violeta-neón
COLOR_GRID = "#1E293B"          # Cuadrícula sutil
COLOR_BLANCO = "#FFFFFF"        # Blanco puro
COLOR_MUTED = "#94A3B8"         # Gris azulado legible


def banner(titulo: str):
    """Imprime un separador visual para la consola."""
    print("\n" + "=" * 65)
    print(f" >>> [MATPLOTLIB DEMO] - {titulo}")
    print("=" * 65)


def generar_grafico_neon():
    banner("Generación de Gráfico Científico en Modo Oscuro Neón")
    print("[*] Configurando parámetros visuales de Matplotlib...")

    # Configuración global de estilos
    plt.rcParams.update({
        "figure.facecolor": COLOR_BG_FIGURA,
        "axes.facecolor": COLOR_BG_AXES,
        "axes.edgecolor": COLOR_NEON_AZUL,
        "axes.linewidth": 1.2,
        "axes.labelcolor": COLOR_BLANCO,
        "xtick.color": COLOR_MUTED,
        "ytick.color": COLOR_MUTED,
        "grid.color": COLOR_GRID,
        "grid.linestyle": "--",
        "grid.alpha": 0.7,
        "text.color": COLOR_BLANCO,
        "font.family": "sans-serif",
    })

    # Crear figura con 2 subgráficos (1 fila, 2 columnas)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)

    # -------------------------------------------------------------
    # SUBGRÁFICO 1: Curvas de Rendimiento (Líneas + Área Glow)
    # -------------------------------------------------------------
    x = np.linspace(0, 10, 200)
    y_eficiencia = 100 * (1 - np.exp(-0.4 * x)) + 2.5 * np.sin(2 * x)
    y_consumo = 20 + 7 * x + 4 * np.cos(1.5 * x)

    # Curva 1: Eficiencia de Cómputo (Azul Neón Eléctrico)
    ax1.plot(x, y_eficiencia, color=COLOR_NEON_AZUL, linewidth=2.5, label="Eficiencia del Algoritmo (%)")
    ax1.fill_between(x, y_eficiencia, alpha=0.18, color=COLOR_NEON_AZUL)  # Efecto de resplandor

    # Curva 2: Rendimiento Secundario (Azul Cielo Neón)
    ax1.plot(x, y_consumo, color=COLOR_NEON_SKY, linewidth=2.0, linestyle="--", label="Carga de Procesamiento (%)")

    ax1.set_title("Curva de Rendimiento Temporal", fontsize=12, fontweight="bold", color=COLOR_BLANCO, pad=12)
    ax1.set_xlabel("Iteraciones de Optimización (x100)", fontsize=10, fontweight="bold")
    ax1.set_ylabel("Métrica de Ejecución (%)", fontsize=10, fontweight="bold")
    ax1.grid(True)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 110)

    # Leyenda estilizada
    leg1 = ax1.legend(facecolor=COLOR_BG_FIGURA, edgecolor=COLOR_NEON_AZUL, fontsize=9, loc="lower right")
    for text in leg1.get_texts():
        text.set_color(COLOR_BLANCO)

    # -------------------------------------------------------------
    # SUBGRÁFICO 2: Comparativa de Módulos (Barras Neón)
    # -------------------------------------------------------------
    modulos = ["math", "numpy", "pandas", "sklearn", "requests"]
    rendimiento_score = [98.5, 94.2, 86.0, 78.4, 91.0]
    colores_barras = [COLOR_NEON_AZUL, COLOR_NEON_SKY, "#0284C7", COLOR_NEON_INDIGO, "#06B6D4"]

    barras = ax2.bar(modulos, rendimiento_score, color=colores_barras, edgecolor=COLOR_BLANCO, linewidth=0.8, width=0.55)

    ax2.set_title("Rendimiento Benchmark por Biblioteca", fontsize=12, fontweight="bold", color=COLOR_BLANCO, pad=12)
    ax2.set_xlabel("Biblioteca Evaluada", fontsize=10, fontweight="bold")
    ax2.set_ylabel("Score de Eficiencia (0 - 100)", fontsize=10, fontweight="bold")
    ax2.set_ylim(0, 115)
    ax2.grid(True, axis="y")

    # Anotar valores sobre cada barra
    for barra in barras:
        altura = barra.get_height()
        ax2.annotate(
            f"{altura:.1f}",
            xy=(barra.get_x() + barra.get_width() / 2, altura),
            xytext=(0, 5),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
            color=COLOR_NEON_AZUL
        )

    # Título General Superpuesto
    fig.suptitle(
        "DASHBOARD CIENTÍFICO — UNIDAD 2 PRÁCTICA 1\nEstética Dark Mode / Neon Blue",
        fontsize=14,
        fontweight="bold",
        color=COLOR_BLANCO,
        y=0.98
    )

    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    # Guardar en disco
    print(f"[*] Guardando imagen de alta resolución en: {IMG_OUTPUT_PATH.name}...")
    plt.savefig(IMG_OUTPUT_PATH, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()

    print(f"[OK] Gráfico generado exitosamente en: {IMG_OUTPUT_PATH.resolve()}")


def main():
    print("\n" + "#" * 65)
    print(" EJECUCIÓN DEL MÓDULO: matplotlib")
    print(" Creación y exportación de gráficos visuales en alta definición")
    print("#" * 65)

    generar_grafico_neon()
    print("\n[OK] Demostración de matplotlib finalizada con éxito.\n")


if __name__ == "__main__":
    main()
