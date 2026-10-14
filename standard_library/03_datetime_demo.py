"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 03_datetime_demo.py
LIBRERÍA: datetime (Biblioteca Estándar de Python)
DESCRIPCIÓN: Manejo integral de fechas, tiempos y husos horarios:
             - Creación e inspección de objetos date, time y datetime.
             - Aritmética temporal con timedelta (plazos, restas y sumas).
             - Formateo (strftime) y parseo desde texto (strptime).
             - Zonas horarias conscientes (timezone-aware) con UTC y offsets.
=============================================================================
"""

import sys
from datetime import date, time, datetime, timedelta, timezone

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def banner(titulo: str):
    """Imprime un separador visual para la consola."""
    print("\n" + "=" * 65)
    print(f" >>> [DATETIME DEMO] - {titulo}")
    print("=" * 65)


def demo_fechas_y_horas_actuales():
    """Obtención y descomposición del tiempo actual."""
    banner("1. Fechas y Horas del Sistema")
    hoy = date.today()
    ahora = datetime.now()

    print(f"[*] Fecha de hoy (date.today())             : {hoy}")
    print(f"    - Año: {hoy.year}, Mes: {hoy.month}, Día: {hoy.day}")
    print(f"    - Día de la semana (0=Lunes, 6=Domingo) : {hoy.weekday()}")

    print(f"[*] Fecha y hora exacta (datetime.now())    : {ahora}")
    print(f"    - Hora: {ahora.hour}, Minutos: {ahora.minute}, Segundos: {ahora.second}.{ahora.microsecond}")

    hora_fija = time(14, 30, 45)
    print(f"[*] Objeto time independiente (14:30:45)    : {hora_fija}")


def demo_aritmetica_con_timedelta():
    """Operaciones de suma, resta y cálculo de diferencias temporales."""
    banner("2. Aritmética Temporal con timedelta")
    ahora = datetime.now()

    plazo_entrega = timedelta(days=15, hours=4, minutes=30)
    fecha_entrega = ahora + plazo_entrega

    print(f"[*] Momento actual                          : {ahora.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[*] Intervalo agregado (+15d, 4h, 30m)      : {plazo_entrega}")
    print(f"[*] Fecha límite calculada                  : {fecha_entrega.strftime('%Y-%m-%d %H:%M:%S')}")

    # Cálculo de diferencia entre dos fechas
    anio_nuevo_2027 = datetime(2027, 1, 1, 0, 0, 0)
    diferencia = anio_nuevo_2027 - ahora
    print(f"[*] Tiempo restante para Año Nuevo 2027     : {diferencia.days} días, {diferencia.seconds // 3600} horas")


def demo_formateo_y_parseo():
    """Conversión bidireccional entre cadenas de texto y fechas."""
    banner("3. Formateo (strftime) y Parseo (strptime)")
    ahora = datetime.now()

    # Formatos legibles con strftime
    formato_iso = ahora.strftime("%Y-%m-%d")
    formato_extendido = ahora.strftime("%A, %d de %B de %Y - %I:%M %p")
    print(f"[*] Formato estándar ISO (%Y-%m-%d)         : {formato_iso}")
    print(f"[*] Formato extendido de presentación       : {formato_extendido}")

    # Parseo de una cadena de texto a datetime con strptime
    cadena_fecha = "2026-12-25 21:45:00"
    fecha_parseada = datetime.strptime(cadena_fecha, "%Y-%m-%d %H:%M:%S")
    print(f"[*] Cadena original                         : '{cadena_fecha}'")
    print(f"[*] Objeto datetime parseado (strptime)     : {type(fecha_parseada)} -> {fecha_parseada}")


def demo_zonas_horarias():
    """Manejo de fechas conscientes con husos horarios UTC y locales."""
    banner("4. Zonas Horarias (Timezone-Aware)")
    hora_utc = datetime.now(timezone.utc)
    print(f"[*] Hora mundial UTC (Coordinated Universal): {hora_utc.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

    tz_mexico = timezone(timedelta(hours=-6), name="CST")
    hora_mexico = hora_utc.astimezone(tz_mexico)
    print(f"[*] Hora en Zona Centro México (UTC-6)      : {hora_mexico.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

    tz_tokio = timezone(timedelta(hours=9), name="JST")
    hora_tokio = hora_utc.astimezone(tz_tokio)
    print(f"[*] Hora en Tokio, Japón (UTC+9)            : {hora_tokio.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")


def main():
    print("\n" + "#" * 65)
    print(" EJECUCIÓN DEL MÓDULO: datetime")
    print(" Control de tiempo cronológico, intervalos y zonas horarias")
    print("#" * 65)

    demo_fechas_y_horas_actuales()
    demo_aritmetica_con_timedelta()
    demo_formateo_y_parseo()
    demo_zonas_horarias()

    print("\n[OK] Demostración de datetime finalizada con éxito.\n")


if __name__ == "__main__":
    main()
