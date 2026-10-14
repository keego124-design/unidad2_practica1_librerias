"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 05_fpdf_demo.py
LIBRERÍA: fpdf / fpdf2 (Biblioteca Externa)
DESCRIPCIÓN: Creación de documentos PDF vectoriales con diseño personalizado:
             - Configuración de márgenes, orientación y tamaños de página.
             - Fondo oscuro (#0A0B10), detalles en azul neón (#00E5FF) y texto blanco.
             - Encabezados, pies de página automatizados con numeración dinámica.
             - Tablas estructuradas con celdas alineadas y estilos modernos.
=============================================================================
"""

import sys
from pathlib import Path
from fpdf import FPDF

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
PDF_OUTPUT_PATH = OUTPUT_DIR / "reporte_fpdf_neon.pdf"


class NeonPDF(FPDF):
    """Clase personalizada derivada de FPDF para aplicar una estética Dark/Neon Blue."""

    def header(self):
        # Fondo oscuro en toda la página
        self.set_fill_color(10, 11, 16)  # #0A0B10 (Negro azulado profundo)
        self.rect(0, 0, 210, 297, "F")

        # Barra decorativa superior en Azul Neón
        self.set_fill_color(0, 229, 255)  # #00E5FF (Azul Neón)
        self.rect(10, 10, 190, 2.5, "F")

        # Título del Encabezado
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 229, 255)  # Azul Neón
        self.set_xy(10, 15)
        self.cell(190, 8, "TOPICOS AVANZADOS DE PROGRAMACION", align="L", new_x="LMARGIN", new_y="NEXT")

        self.set_font("Helvetica", "", 9)
        self.set_text_color(148, 163, 184)  # Gris azulado tenue
        self.set_x(10)
        self.cell(190, 5, "Unidad 2: Practica 1 - Demostracion de Generacion de PDFs con FPDF", align="L", new_x="LMARGIN", new_y="NEXT")
        self.ln(6)

    def footer(self):
        # Posición a 15 mm del final
        self.set_y(-15)
        # Línea divisoria en azul neón
        self.set_draw_color(0, 229, 255)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())

        self.set_font("Helvetica", "I", 8)
        self.set_text_color(148, 163, 184)
        self.cell(95, 10, "Reporte Autogenerado con Python + FPDF", align="L")
        self.cell(95, 10, f"Pagina {self.page_no()}/{{nb}}", align="R")


def generar_pdf_fpdf():
    print(f"[*] Iniciando generacion de PDF con FPDF en: {PDF_OUTPUT_PATH.name}...")
    pdf = NeonPDF(orientation="P", unit="mm", format="A4")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # 1. Título Principal
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)  # Blanco puro
    pdf.cell(190, 10, "Resumen Ejecutivo de Rendimiento", align="C", new_x="LMARGIN", new_y="NEXT")

    # Subtítulo
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(0, 229, 255)
    pdf.cell(190, 6, "Auditoria de Modulos y Servicios de Software", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    # 2. Párrafo Introductorio
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(241, 245, 249)  # Blanco suave
    descripcion = (
        "El presente documento es generado automaticamente mediante el modulo FPDF en Python. "
        "Demuestra el formateo de paginas de alto contraste estilizadas con una paleta Dark Mode "
        "y acentos en azul neon. Permite la insercion de metadatos, estructuracion de tablas con "
        "alineacion precisa y paginado dinamico de documentos tecnicos universitarios."
    )
    pdf.multi_cell(190, 6, descripcion)
    pdf.ln(6)

    # 3. Tabla Estilizada de Datos
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 229, 255)
    pdf.cell(190, 8, "Metricas de Operacion del Sistema", new_x="LMARGIN", new_y="NEXT")

    # Encabezados de Tabla
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(15, 23, 42)    # Fondo azul noche
    pdf.set_draw_color(0, 229, 255)   # Borde azul neón
    pdf.set_text_color(0, 229, 255)
    pdf.set_line_width(0.3)

    columnas = [("ID Modulo", 25), ("Nombre del Servicio", 70), ("Tiempo Respuesta", 45), ("Estado Operativo", 50)]
    for col_nombre, ancho in columnas:
        pdf.cell(ancho, 8, col_nombre, border=1, fill=True, align="C")
    pdf.ln()

    # Filas de la Tabla
    datos_servicios = [
        ("MOD-01", "Motor de Base de Datos SQLite", "1.2 ms", "OPTIMO"),
        ("MOD-02", "Controlador REST API / Endpoint", "14.5 ms", "ACTIVO"),
        ("MOD-03", "Procesador Criptografico SHA-256", "0.8 ms", "OPTIMO"),
        ("MOD-04", "Generador de Informes PDF", "48.2 ms", "ACTIVO"),
        ("MOD-05", "Pipeline de Clasificacion ML", "92.0 ms", "EN ESPERA"),
    ]

    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(255, 255, 255)

    for i, (cod, nombre, tiempo, estado) in enumerate(datos_servicios):
        # Color alterno en filas
        if i % 2 == 0:
            pdf.set_fill_color(20, 24, 38)
        else:
            pdf.set_fill_color(12, 14, 22)

        pdf.cell(25, 7, cod, border="LR", fill=True, align="C")
        pdf.cell(70, 7, f" {nombre}", border="LR", fill=True, align="L")
        pdf.cell(45, 7, tiempo, border="LR", fill=True, align="C")

        # Color condicional según estado
        if estado == "OPTIMO":
            pdf.set_text_color(0, 229, 255)
        elif estado == "ACTIVO":
            pdf.set_text_color(56, 189, 248)
        else:
            pdf.set_text_color(148, 163, 184)

        pdf.cell(50, 7, estado, border="LR", fill=True, align="C")
        pdf.set_text_color(255, 255, 255)
        pdf.ln()

    # Cierre de tabla con línea inferior
    pdf.cell(190, 0, "", border="T", new_x="LMARGIN", new_y="NEXT")

    # 4. Cuadro de Resumen (Card Informativa)
    pdf.ln(8)
    pdf.set_fill_color(15, 23, 42)
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.4)
    pdf.rect(10, pdf.get_y(), 190, 22, "DF")

    pdf.set_xy(14, pdf.get_y() + 3)
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(0, 229, 255)
    pdf.cell(182, 5, "[!] CONCLUSION DE AUDITORIA:", new_x="LMARGIN", new_y="NEXT")

    pdf.set_x(14)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(241, 245, 249)
    pdf.cell(182, 5, "Todos los componentes se encuentran en conformidad con los estandares de la Unidad 2.", new_x="LMARGIN", new_y="NEXT")

    # Guardar en disco
    pdf.output(str(PDF_OUTPUT_PATH))
    print(f"    [OK] Archivo PDF generado exitosamente: {PDF_OUTPUT_PATH.resolve()}")


def main():
    print("\n" + "=" * 65)
    print(" >>> EJECUCION DEL MODULO: FPDF")
    print(" Generacion de documentos PDF estilizados en modo oscuro y neon blue")
    print("=" * 65)

    generar_pdf_fpdf()
    print("\n[OK] Demostracion de FPDF finalizada con exito.\n")


if __name__ == "__main__":
    main()
