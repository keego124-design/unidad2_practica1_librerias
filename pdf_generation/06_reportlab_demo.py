"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 06_reportlab_demo.py
LIBRERÍA: reportlab (Biblioteca Externa)
DESCRIPCIÓN: Creación de PDFs empresariales avanzados con Platypus y ReportLab:
             - Plantillas de documentos mediante SimpleDocTemplate y Flowables.
             - Estilos CSS-like con ParagraphStyle (fondo negro, acentos azul neón).
             - Tablas estilizadas mediante Table y TableStyle con cuadrícula neón.
             - Gráficos vectoriales nativos con Drawing, Rect y String.
=============================================================================
"""

import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.graphics.shapes import Drawing, Rect, String, Line

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
PDF_OUTPUT_PATH = OUTPUT_DIR / "reporte_reportlab_neon.pdf"

# Definición de la Paleta Neon / Dark
COLOR_FONDO = colors.HexColor("#0A0B10")
COLOR_NEON_AZUL = colors.HexColor("#00E5FF")
COLOR_NEON_CYAN = colors.HexColor("#38BDF8")
COLOR_BLANCO = colors.HexColor("#FFFFFF")
COLOR_GRIS_TEXTO = colors.HexColor("#94A3B8")
COLOR_CARD = colors.HexColor("#0F172A")


def dibujar_fondo_neon(canvas, doc):
    """Callback ejecutado por ReportLab para pintar el fondo y encabezado en cada página."""
    canvas.saveState()
    # 1. Lienzo de fondo oscuro total
    canvas.setFillColor(COLOR_FONDO)
    canvas.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=True, stroke=False)

    # 2. Barra decorativa superior en Azul Neón
    canvas.setFillColor(COLOR_NEON_AZUL)
    canvas.rect(36, doc.pagesize[1] - 30, doc.pagesize[0] - 72, 3, fill=True, stroke=False)

    # 3. Pie de página decorativo
    canvas.setStrokeColor(COLOR_NEON_AZUL)
    canvas.setLineWidth(0.5)
    canvas.line(36, 40, doc.pagesize[0] - 36, 40)

    canvas.setFont("Helvetica-Oblique", 8)
    canvas.setFillColor(COLOR_GRIS_TEXTO)
    canvas.drawString(36, 26, "Reporte Generado con ReportLab Platypus Engine | Modo Oscuro Neón")
    canvas.drawRightString(doc.pagesize[0] - 36, 26, f"Página {canvas.getPageNumber()}")
    canvas.restoreState()


def crear_grafico_vectorial_barras():
    """Genera un gráfico vectorial nativo de barras neón usando Drawing."""
    d = Drawing(400, 110)
    # Fondo del gráfico
    d.add(Rect(0, 0, 480, 105, fillColor=COLOR_CARD, strokeColor=COLOR_NEON_AZUL, strokeWidth=0.5))

    d.add(String(15, 85, "RENDIMIENTO POR LIBRERIA (OPERACIONES / MS)", fontName="Helvetica-Bold", fontSize=8, fillColor=COLOR_NEON_AZUL))

    metricas = [
        ("math", 95, colors.HexColor("#00E5FF")),
        ("numpy", 90, colors.HexColor("#38BDF8")),
        ("pandas", 75, colors.HexColor("#0284C7")),
        ("sklearn", 65, colors.HexColor("#60A5FA")),
        ("reportlab", 80, colors.HexColor("#22D3EE")),
    ]

    x_inicio = 20
    ancho_barra = 70
    espacio = 20

    for i, (nombre, valor, col) in enumerate(metricas):
        x = x_inicio + i * (ancho_barra + espacio)
        altura = valor * 0.5
        y = 25
        # Barra neón
        d.add(Rect(x, y, ancho_barra, altura, fillColor=col, strokeColor=colors.white, strokeWidth=0.2))
        # Etiqueta valor
        d.add(String(x + 22, y + altura + 4, f"{valor}%", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.white))
        # Etiqueta nombre
        d.add(String(x + 10, y - 10, nombre, fontName="Helvetica", fontSize=8, fillColor=COLOR_GRIS_TEXTO))

    return d


def generar_pdf_reportlab():
    print(f"[*] Construyendo documento ReportLab Platypus en: {PDF_OUTPUT_PATH.name}...")

    doc = SimpleDocTemplate(
        str(PDF_OUTPUT_PATH),
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=54,
        bottomMargin=54
    )

    estilos = getSampleStyleSheet()

    # Creación de estilos personalizados de alto contraste
    estilo_titulo = ParagraphStyle(
        "NeonTitulo",
        parent=estilos["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=COLOR_BLANCO,
        alignment=0,
        spaceAfter=4
    )

    estilo_subtitulo = ParagraphStyle(
        "NeonSubtitulo",
        parent=estilos["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=COLOR_NEON_AZUL,
        spaceAfter=15
    )

    estilo_cuerpo = ParagraphStyle(
        "NeonCuerpo",
        parent=estilos["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#E2E8F0"),
        spaceAfter=12
    )

    estilo_encabezado_sec = ParagraphStyle(
        "NeonSeccion",
        parent=estilos["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=COLOR_NEON_AZUL,
        spaceBefore=10,
        spaceAfter=8
    )

    historia = []

    # 1. Títulos
    historia.append(Paragraph("DASHBOARD ANALITICO DE LIBRERIAS", estilo_titulo))
    historia.append(Paragraph("Tópicos Avanzados de Programación — Unidad 2 Práctica 1", estilo_subtitulo))

    # 2. Descripción
    p_intro = (
        "El motor <b>ReportLab Platypus</b> (Page Layout and Typography Using Scripts) "
        "permite estructurar documentos técnicos mediante el patrón Flowables, facilitando la integración "
        "de tablas dinámicas con estilos automáticos, cálculo de flujo de página y gráficos vectoriales "
        "definidos en código Python puro sin requerir herramientas externas."
    )
    historia.append(Paragraph(p_intro, estilo_cuerpo))
    historia.append(Spacer(1, 10))

    # 3. Gráfico Vectorial Incrustado
    historia.append(Paragraph("1. Evaluación de Eficiencia Relativa", estilo_encabezado_sec))
    historia.append(crear_grafico_vectorial_barras())
    historia.append(Spacer(1, 15))

    # 4. Tabla de Datos Estilizada
    historia.append(Paragraph("2. Tabla Comparativa de Capacidades Técnicas", estilo_encabezado_sec))

    encabezados = ["Librería", "Propósito Principal", "Velocidad", "Dependencias", "Complejidad"]
    filas = [
        encabezados,
        ["math", "Cálculo matemático elemental y trigonometría", "Ultra Alta", "Estándar (0)", "Baja"],
        ["numpy", "Álgebra matricial y vectores N-dimensionales", "Extrema (C/BLAS)", "Externa", "Media"],
        ["pandas", "Procesamiento de DataFrames y series de tiempo", "Alta", "Externa", "Media-Alta"],
        ["reportlab", "Generación empresarial de documentos PDF", "Alta", "Externa", "Media"],
        ["scikit-learn", "Modelos de Machine Learning predictivos", "Alta", "Externa", "Avanzada"],
    ]

    tabla = Table(filas, colWidths=[75, 175, 90, 85, 95])
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLOR_CARD),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLOR_NEON_AZUL),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8.5),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        # Filas de datos
        ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#111827")),
        ("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#0B0F19")),
        ("BACKGROUND", (0, 3), (-1, 3), colors.HexColor("#111827")),
        ("BACKGROUND", (0, 4), (-1, 4), colors.HexColor("#0B0F19")),
        ("BACKGROUND", (0, 5), (-1, 5), colors.HexColor("#111827")),
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.white),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8),
        # Bordes Neón
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#00E5FF")),
    ]))

    historia.append(tabla)

    # Construir documento
    doc.build(historia, onFirstPage=dibujar_fondo_neon, onLaterPages=dibujar_fondo_neon)
    print(f"    [OK] Documento ReportLab compilado exitosamente: {PDF_OUTPUT_PATH.resolve()}")


def main():
    print("\n" + "=" * 65)
    print(" >>> EJECUCION DEL MODULO: REPORTLAB")
    print(" Compilacion de documentos PDF con tablas y graficos vectoriales")
    print("=" * 65)

    generar_pdf_reportlab()
    print("\n[OK] Demostracion de ReportLab finalizada con exito.\n")


if __name__ == "__main__":
    main()
