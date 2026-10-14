"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 04_csv_demo.py
LIBRERÍA: csv (Biblioteca Estándar de Python)
DESCRIPCIÓN: Procesamiento eficiente de archivos delimitados por comas (CSV):
             - Escritura y lectura secuencial con csv.writer y csv.reader.
             - Escritura y lectura estructurada basada en diccionarios (DictWriter, DictReader).
             - Manejo de delimitadores personalizados y caracteres de escape.
             - Generación automática de archivos en la carpeta de salida (output/).
=============================================================================
"""

import sys
import csv
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Directorio de salida
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CSV_BASICO_PATH = OUTPUT_DIR / "alumnos_calificaciones.csv"
CSV_DICT_PATH = OUTPUT_DIR / "inventario_tecnologico.csv"


def banner(titulo: str):
    """Imprime un separador visual para la consola."""
    print("\n" + "=" * 65)
    print(f" >>> [CSV DEMO] - {titulo}")
    print("=" * 65)


def demo_escritura_y_lectura_basica():
    """Uso de csv.writer y csv.reader basado en listas y tuplas."""
    banner("1. Escritura y Lectura Básica (csv.writer / csv.reader)")

    datos_alumnos = [
        ["Matricula", "Nombre", "Materia", "Calificacion", "Estado"],
        ["A001", "Carlos Mendoza", "Tópicos Avanzados", 95, "Aprobado"],
        ["A002", "Valeria Soto", "Bases de Datos", 88, "Aprobado"],
        ["A003", "Jorge Ramirez", "Redes de Computadoras", 70, "Aprobado"],
        ["A004", "Mariana Rios", "Inteligencia Artificial", 98, "Aprobado"],
        ["A005", "Diego Lopez", "Sistemas Operativos", 55, "Reprobado"]
    ]

    print(f"[*] Escribiendo archivo CSV en: {CSV_BASICO_PATH.name}...")
    with open(CSV_BASICO_PATH, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f, delimiter=",")
        escritor.writerows(datos_alumnos)
    print("    [OK] Archivo escrito satisfactoriamente.")

    print("\n[*] Leyendo y tabulando contenido con csv.reader:")
    with open(CSV_BASICO_PATH, mode="r", encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=",")
        for i, fila in enumerate(lector):
            if i == 0:
                print(f"    ENCABEZADOS -> {' | '.join(f'{col:<15}' for col in fila)}")
                print("    " + "-" * 70)
            else:
                print(f"    Fila #{i:02d}    -> {' | '.join(f'{col:<15}' for col in fila)}")


def demo_diccionarios_csv():
    """Uso de DictWriter y DictReader para trabajar con diccionarios clave-valor."""
    banner("2. CSV Orientado a Diccionarios (DictWriter / DictReader)")

    campos = ["id_producto", "nombre", "categoria", "precio_usd", "stock"]

    productos = [
        {"id_producto": 101, "nombre": "Teclado Mecánico RGB", "categoria": "Periféricos", "precio_usd": 85.50, "stock": 42},
        {"id_producto": 102, "nombre": "Monitor Gamer 144Hz", "categoria": "Monitores", "precio_usd": 240.00, "stock": 15},
        {"id_producto": 103, "nombre": "Mouse Inalámbrico Pro", "categoria": "Periféricos", "precio_usd": 65.00, "stock": 80},
        {"id_producto": 104, "nombre": "Auriculares Cancelación Ruido", "categoria": "Audio", "precio_usd": 110.00, "stock": 25},
    ]

    print(f"[*] Escribiendo inventario con csv.DictWriter en: {CSV_DICT_PATH.name}...")
    with open(CSV_DICT_PATH, mode="w", newline="", encoding="utf-8") as f:
        dict_writer = csv.DictWriter(f, fieldnames=campos)
        dict_writer.writeheader()
        dict_writer.writerows(productos)
    print("    [OK] Encabezados y registros escritos con éxito.")

    print("\n[*] Leyendo y calculando valor total de inventario con csv.DictReader:")
    valor_total_inventario = 0.0
    total_unidades = 0

    with open(CSV_DICT_PATH, mode="r", encoding="utf-8") as f:
        dict_reader = csv.DictReader(f)
        for fila in dict_reader:
            subtotal = float(fila["precio_usd"]) * int(fila["stock"])
            valor_total_inventario += subtotal
            total_unidades += int(fila["stock"])
            print(f"    - [{fila['categoria']}] {fila['nombre']:<30} | {fila['stock']:>3} un. x ${float(fila['precio_usd']):.2f} = ${subtotal:,.2f}")

    print("    " + "-" * 65)
    print(f"    TOTAL INVENTARIO: {total_unidades} unidades | Valor Monetario: ${valor_total_inventario:,.2f} USD")


def main():
    print("\n" + "#" * 65)
    print(" EJECUCIÓN DEL MÓDULO: csv")
    print(" Manejo de archivos planos tabulares estructurados (Standard Library)")
    print("#" * 65)

    demo_escritura_y_lectura_basica()
    demo_diccionarios_csv()

    print("\n[OK] Demostración de csv finalizada con éxito.")
    print(f"[*] Archivos generados guardados en: {OUTPUT_DIR}\n")


if __name__ == "__main__":
    main()
