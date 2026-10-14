"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 08_pandas_demo.py
LIBRERÍA: pandas (Biblioteca Externa)
DESCRIPCIÓN: Manipulación, limpieza y análisis estructurado de datos tabulares:
             - Creación e inspección de Series y DataFrames.
             - Filtrado booleano, segmentación y adición de columnas calculadas.
             - Agregaciones estadísticas y agrupación relacional (.groupby()).
             - Importación y exportación de conjuntos de datos a formato CSV.
=============================================================================
"""

import sys
from pathlib import Path
import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CSV_RESUMEN_PATH = OUTPUT_DIR / "resumen_ventas_pandas.csv"


def banner(titulo: str):
    """Imprime un separador visual para la consola."""
    print("\n" + "=" * 65)
    print(f" >>> [PANDAS DEMO] - {titulo}")
    print("=" * 65)


def demo_creacion_dataframe():
    """Construcción de DataFrames a partir de diccionarios e inspección de estructura."""
    banner("1. Creación e Inspección de DataFrames")

    datos_ventas = {
        "id_transaccion": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
        "cliente": ["TechCorp", "InnovaLab", "ByteSoft", "CloudNet", "TechCorp", "DataFlow", "InnovaLab", "ByteSoft"],
        "region": ["Norte", "Sur", "Norte", "Centro", "Norte", "Sur", "Sur", "Centro"],
        "unidades": [12, 5, 25, 8, 14, 30, 9, 18],
        "precio_unitario": [150.0, 320.0, 95.0, 450.0, 150.0, 80.0, 320.0, 110.0],
        "metodo_pago": ["Transferencia", "Tarjeta", "Transferencia", "Efectivo", "Tarjeta", "Transferencia", "Tarjeta", "Transferencia"]
    }

    df = pd.DataFrame(datos_ventas)
    print("[*] Primeros registros del DataFrame (.head()):")
    print(df.head(4).to_string(index=False))

    print("\n[*] Información general del dataset (.info()):")
    df.info()

    return df


def demo_filtrado_y_columnas_calculadas(df: pd.DataFrame):
    """Operaciones de vectorización, filtrado booleano y cálculo de métricas."""
    banner("2. Columnas Calculadas y Filtrado Booleano")

    # Columna calculada: Monto total de la venta
    df["monto_total"] = df["unidades"] * df["precio_unitario"]

    # Columna calculada con condición (descuento del 10% si unidades >= 15)
    df["aplica_descuento"] = df["unidades"] >= 15
    df["total_final"] = df.apply(
        lambda row: row["monto_total"] * 0.90 if row["aplica_descuento"] else row["monto_total"],
        axis=1
    )

    print("[*] DataFrame con columnas de 'monto_total' y 'total_final':")
    columnas_vista = ["id_transaccion", "cliente", "region", "unidades", "monto_total", "total_final"]
    print(df[columnas_vista].to_string(index=False))

    # Filtro: Transacciones con total final > $3,000 USD
    filtro_alto_valor = df[df["total_final"] > 3000.0]
    print(f"\n[*] Transacciones mayores a $3,000 USD (Total coincidentes: {len(filtro_alto_valor)}):")
    print(filtro_alto_valor[["id_transaccion", "cliente", "region", "total_final"]].to_string(index=False))

    return df


def demo_agrupacion_y_estadistica(df: pd.DataFrame):
    """Resúmenes agregados mediante groupby y exportación."""
    banner("3. Agrupación (.groupby) y Resumen Estadístico")

    print("[*] Estadísticas numéricas generales (.describe()):")
    print(df[["unidades", "precio_unitario", "total_final"]].describe().round(2))

    # Agrupación por Región
    resumen_region = df.groupby("region").agg(
        total_ventas_usd=("total_final", "sum"),
        promedio_venta_usd=("total_final", "mean"),
        unidades_vendidas=("unidades", "sum"),
        transacciones=("id_transaccion", "count")
    ).reset_index()

    print("\n[*] Rendimiento Comercial Agrupado por Región:")
    print(resumen_region.to_string(index=False))

    # Exportación a CSV
    resumen_region.to_csv(CSV_RESUMEN_PATH, index=False, encoding="utf-8")
    print(f"\n[OK] Resumen analítico exportado a CSV en: {CSV_RESUMEN_PATH.name}")


def main():
    print("\n" + "#" * 65)
    print(" EJECUCIÓN DEL MÓDULO: pandas")
    print(" Análisis y manipulación avanzada de estructuras de datos tabulares")
    print("#" * 65)

    df_base = demo_creacion_dataframe()
    df_transformado = demo_filtrado_y_columnas_calculadas(df_base)
    demo_agrupacion_y_estadistica(df_transformado)

    print("\n[OK] Demostración de pandas finalizada con éxito.\n")


if __name__ == "__main__":
    main()
