# ⚡ Unidad 2 Práctica 1: Ejemplos de Librerías de Python

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-00E5FF?style=for-the-badge&logo=python&logoColor=0A0B10)
![Theme](https://img.shields.io/badge/Design-Dark%20%26%20Neon%20Blue-00E5FF?style=for-the-badge&logo=visualstudiocode&logoColor=0A0B10)
![Course](https://img.shields.io/badge/Materia-T%C3%B3picos%20Avanzados-FFFFFF?style=for-the-badge&logo=google-classroom&logoColor=0A0B10)
![Status](https://img.shields.io/badge/Build-12%20%2F%2012%20Passing-00E5FF?style=for-the-badge&logo=githubactions&logoColor=0A0B10)

<p align="center">
  <b>Suite Integral de Demostración Técnica y Científica de Bibliotecas en Python</b><br>
  <i>Estructura modularizada, documentación exhaustiva, estética de alto contraste y código 100% funcional.</i>
</p>

</div>

---

## 🎨 Paleta Conceptual: Dark Mode & Neon Blue

El diseño visual, la documentación, los documentos PDF autogenerados, las gráficas científicas y la interfaz web en Flask están estrictamente construidos bajo una **estética de alto contraste**:

| Elemento Visual | Código Hex | Código RGB | Muestra Visual | Rol en el Sistema |
| :--- | :---: | :---: | :---: | :--- |
| **Fondo Base (Dark)** | `#0A0B10` | `rgb(10, 11, 16)` | `⬛` | Lienzo principal oscuro, descanso visual y elegancia técnica. |
| **Fondo Tarjetas / Cards** | `#0F172A` | `rgb(15, 23, 42)` | `🟦` | Contenedores modulares, tablas y fondos de ejes en gráficas. |
| **Azul Neón Principal** | `#00E5FF` | `rgb(0, 229, 255)` | `🌐` | Acentos, bordes luminosos, encabezados y curvas de datos. |
| **Azul Neón Secundario** | `#38BDF8` | `rgb(56, 189, 248)` | `💎` | Subtítulos, elementos hover y métricas complementarias. |
| **Texto Principal** | `#FFFFFF` | `rgb(255, 255, 255)`| `⬜` | Tipografía principal de máxima legibilidad y nitidez. |
| **Texto Atenuado** | `#94A3B8` | `rgb(148, 163, 184)`| `🌫️` | Etiquetas secundarias, notas técnicas y metadatos. |

---

## 📂 Arquitectura del Proyecto

El repositorio implementa una separación de responsabilidades desacoplada en 5 dominios tecnológicos:

```text
unidad2_practica1_librerias/
│
├── .gitignore                          # Exclusión de bytecode, temporales y caché
├── requirements.txt                    # Dependencias externas con versiones fijadas
├── README.md                           # Documentación técnica completa
├── run_all.py                          # Lanzador maestro con menú interactivo neón
│
├── standard_library/                   # MÓDULOS DE LA BIBLIOTECA ESTÁNDAR
│   ├── __init__.py
│   ├── 01_math_demo.py                 # Trigonometría, factoriales, potencias, logaritmos
│   ├── 02_random_demo.py               # Aleatoriedad, elecciones, barajado, semillas
│   ├── 03_datetime_demo.py             # Aritmética temporal, formatos, husos horarios
│   └── 04_csv_demo.py                  # Lectura/escritura CSV estándar y orientada a dicts
│
├── pdf_generation/                     # GENERACIÓN DE DOCUMENTOS PDF
│   ├── __init__.py
│   ├── 05_fpdf_demo.py                 # FPDF2: Reportes con páginas, tablas y estilos
│   └── 06_reportlab_demo.py            # ReportLab: Platypus, gráficos vectoriales y tablas
│
├── data_science/                       # COMPUTACIÓN CIENTÍFICA Y VISUALIZACIÓN
│   ├── __init__.py
│   ├── 07_numpy_demo.py                # Arrays N-D, broadcasting, álgebra lineal
│   ├── 08_pandas_demo.py               # DataFrames, filtrado booleano, agrupaciones groupby
│   └── 09_matplotlib_demo.py           # Gráficas de alta resolución estilo Dark/Neon (300 DPI)
│
├── web_and_apis/                       # CLIENTES HTTP Y MICROSERVICIOS BACKEND
│   ├── __init__.py
│   ├── 10_requests_demo.py             # Consumo REST API (PokeAPI, JSONPlaceholder, error 404)
│   └── 11_flask_demo.py                # Dashboard HTML5 Neón y endpoints JSON interactivos
│
├── machine_learning/                   # MODELADO PREDICTIVO E INTELIGENCIA ARTIFICIAL
│   ├── __init__.py
│   └── 12_sklearn_demo.py              # Regresión Lineal y Clasificación Logística con métricas
│
└── output/                             # ARTEFACTOS GENERADOS DURANTE LA EJECUCIÓN
    ├── alumnos_calificaciones.csv      # CSV básico generado por csv.writer
    ├── inventario_tecnologico.csv      # CSV estructurado generado por csv.DictWriter
    ├── resumen_ventas_pandas.csv       # Resumen analítico generado por pandas.DataFrame.to_csv
    ├── reporte_fpdf_neon.pdf           # Documento PDF generado con FPDF2
    ├── reporte_reportlab_neon.pdf      # Documento PDF empresarial generado con ReportLab
    └── grafico_rendimiento_neon.png    # Gráfico científico 300 DPI generado por Matplotlib
```

---

## 🛠️ Instalación y Requisitos

### Requisitos del Sistema
- **Python:** 3.10 o superior (compatible con Python 3.10, 3.11, 3.12, 3.13 y 3.14).
- **Sistema Operativo:** Windows 10/11, Linux o macOS.
- **Acceso a Internet:** Únicamente requerido para la instalación inicial de paquetes y para la demostración de `requests` (PokeAPI / JSONPlaceholder).

### 1. Clonar o Descargar el Proyecto
```bash
git clone https://github.com/keego124-design/unidad2_practica1_librerias.git
cd unidad2_practica1_librerias
```

### 2. (Opcional pero Recomendado) Crear Entorno Virtual
```bash
# En Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# En Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias Externas
```bash
pip install -r requirements.txt
```

---

## 🚀 Guía de Ejecución

### Opción A: Lanzador Maestro Interactivo (Recomendado)
El proyecto incluye `run_all.py`, una interfaz de línea de comandos enriquecida con códigos de escape ANSI y paleta neón:

```bash
python run_all.py
```

*Permite seleccionar individualmente cualquiera de los 12 módulos, lanzar el servidor web de Flask o ejecutar toda la suite de pruebas.*

Para ejecutar **todos los scripts en secuencia automática**:
```bash
python run_all.py --all
```

---

### Opción B: Ejecución Modular Individual

A continuación se detalla el comando directo para ejecutar cada una de las 12 librerías:

```bash
# 1. Biblioteca Estándar
python standard_library/01_math_demo.py
python standard_library/02_random_demo.py
python standard_library/03_datetime_demo.py
python standard_library/04_csv_demo.py

# 2. Generación de PDFs
python pdf_generation/05_fpdf_demo.py
python pdf_generation/06_reportlab_demo.py

# 3. Ciencia de Datos y Visualización
python data_science/07_numpy_demo.py
python data_science/08_pandas_demo.py
python data_science/09_matplotlib_demo.py

# 4. Servicios Web y APIs
python web_and_apis/10_requests_demo.py
python web_and_apis/11_flask_demo.py              # Modo Test Client (verificación rápida)
python web_and_apis/11_flask_demo.py --serve      # Modo Servidor Web en vivo (http://127.0.0.1:5000)

# 5. Aprendizaje Automático
python machine_learning/12_sklearn_demo.py
```

---

## 📖 Detalle Técnico de los 12 Módulos

### 1. `math` (Biblioteca Estándar)
* **Archivo:** [`standard_library/01_math_demo.py`](standard_library/01_math_demo.py)
* **Conceptos clave:**
  - Constantes matemáticas de alta precisión: `math.pi`, `math.e`, `math.tau`, `math.inf`.
  - Trigonometría: Conversión angular con `math.radians()`, funciones `sin()`, `cos()`, `tan()` y cálculo de hipotenusa euclidiana con `math.hypot()`.
  - Aritmética avanzada: Factoriales con `math.factorial()`, combinatoria con `math.comb(n, r)`, cálculo de MCD (`math.gcd`) y MCM (`math.lcm`).
  - Funciones exponenciales y logaritmos en bases 2, 10 y natural (`math.log`).

### 2. `random` (Biblioteca Estándar)
* **Archivo:** [`standard_library/02_random_demo.py`](standard_library/02_random_demo.py)
* **Conceptos clave:**
  - Números pseudoaleatorios: `random.random()`, enteros inclusivos con `randint()`, flotantes continuos en rangos con `uniform()` y secuencias con paso con `randrange()`.
  - Selección ponderada: `random.choice()` y `random.choices(weights=...)` para modelar probabilidades discretas.
  - Barajado y muestreo: Permutación con `random.shuffle()` y muestreo sin reemplazo con `random.sample()`.
  - Determinismo: Fijación de semilla reproducible mediante `random.seed(42)`.

### 3. `datetime` (Biblioteca Estándar)
* **Archivo:** [`standard_library/03_datetime_demo.py`](standard_library/03_datetime_demo.py)
* **Conceptos clave:**
  - Instancias de tiempo: `date.today()`, `time()` y `datetime.now()`.
  - Aritmética cronológica: Operaciones de suma y resta temporal mediante `timedelta` (cálculo de plazos y cuentas regresivas).
  - Formateo y parseo: `strftime()` para representación ISO y amigable, y `strptime()` para conversión inversa desde texto.
  - Husos horarios conscientes: Manejo de `timezone.utc` y zonas locales con desplazamientos fijos (`timezone(timedelta(hours=-6))`).

### 4. `csv` (Biblioteca Estándar)
* **Archivo:** [`standard_library/04_csv_demo.py`](standard_library/04_csv_demo.py)
* **Conceptos clave:**
  - Procesamiento secuencial: `csv.writer()` y `csv.reader()` para listas homogéneas.
  - Procesamiento clave-valor: `csv.DictWriter()` con escritura de cabecera (`writeheader()`) y `csv.DictReader()` para manipulación mediante diccionarios.
  - Artefactos producidos en `output/`: `alumnos_calificaciones.csv` e `inventario_tecnologico.csv`.

### 5. `fpdf` / `fpdf2` (Biblioteca Externa)
* **Archivo:** [`pdf_generation/05_fpdf_demo.py`](pdf_generation/05_fpdf_demo.py)
* **Conceptos clave:**
  - Clase personalizada derivada de `FPDF` con sobreescritura de `header()` y `footer()`.
  - Paginado automático con `{nb}` y cálculo de número de página dinámico.
  - Tablas estilizadas con bordes en azul neón (`#00E5FF`), fondo oscuro (`#0A0B10`) y celdas alternadas.
  - Artefacto producido: [`output/reporte_fpdf_neon.pdf`](output/reporte_fpdf_neon.pdf).

### 6. `reportlab` (Biblioteca Externa)
* **Archivo:** [`pdf_generation/06_reportlab_demo.py`](pdf_generation/06_reportlab_demo.py)
* **Conceptos clave:**
  - Arquitectura Platypus mediante `SimpleDocTemplate` y flujo de objetos `Flowables`.
  - Estilos tipográficos avanzados con `ParagraphStyle` y `getSampleStyleSheet()`.
  - Construcción de tablas complejas con `Table` y `TableStyle` (fondos degradados, rejillas neón).
  - Dibujo de gráficos vectoriales nativos con `Drawing`, `Rect` y `String`.
  - Artefacto producido: [`output/reporte_reportlab_neon.pdf`](output/reporte_reportlab_neon.pdf).

### 7. `numpy` (Biblioteca Externa)
* **Archivo:** [`data_science/07_numpy_demo.py`](data_science/07_numpy_demo.py)
* **Conceptos clave:**
  - Estructura `ndarray`: Atributos `shape`, `dtype`, `ndim` y `size`.
  - Generación de vectores y matrices: `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`.
  - Transformaciones y slicing: Redimensionamiento con `.reshape()`, transpuesta con `.T` y submatrices.
  - Operaciones vectorizadas y broadcasting sin necesidad de bucles tradicionales.
  - Álgebra matricial con el operador `@` y estadística descriptiva acelerada en C (`mean`, `std`, `var`).

### 8. `pandas` (Biblioteca Externa)
* **Archivo:** [`data_science/08_pandas_demo.py`](data_science/08_pandas_demo.py)
* **Conceptos clave:**
  - Creación de `DataFrame` a partir de diccionarios con múltiples tipos de datos.
  - Manipulación columnar: Adición de columnas derivadas vectorizadas y aplicación de lógica con `.apply()`.
  - Filtrado condicional booleano de alto rendimiento.
  - Agregación relacional: `.groupby('region').agg(...)` calculando sumatorias, conteos y promedios.
  - Artefacto producido: [`output/resumen_ventas_pandas.csv`](output/resumen_ventas_pandas.csv).

### 9. `matplotlib` (Biblioteca Externa)
* **Archivo:** [`data_science/09_matplotlib_demo.py`](data_science/09_matplotlib_demo.py)
* **Conceptos clave:**
  - Configuración estricta del tema Dark / Neon Blue mediante `plt.rcParams`.
  - Curvas matemáticas continuas con efecto de resplandor (`fill_between` con alpha).
  - Gráfico de barras comparativo con anotación automática de valores numéricos en cada columna.
  - Renderizado sin pantalla con backend `Agg` y exportación a 300 DPI de calidad editorial.
  - Artefacto producido: [`output/grafico_rendimiento_neon.png`](output/grafico_rendimiento_neon.png).

### 10. `requests` (Biblioteca Externa)
* **Archivo:** [`web_and_apis/10_requests_demo.py`](web_and_apis/10_requests_demo.py)
* **Conceptos clave:**
  - Solicitudes HTTP seguras con cabeceras `User-Agent` y control de `timeout`.
  - Consumo de **PokeAPI** (`https://pokeapi.co/api/v2/pokemon/pikachu`) extrayendo tipos, peso y habilidades.
  - Consumo de **JSONPlaceholder** (`https://jsonplaceholder.typicode.com/posts/1`).
  - Validación de estado con `.raise_for_status()`.
  - Manejo granular de excepciones: `HTTPError`, `ConnectionError`, `Timeout` y solicitudes 404 simuladas.

### 11. `flask` (Biblioteca Externa)
* **Archivo:** [`web_and_apis/11_flask_demo.py`](web_and_apis/11_flask_demo.py)
* **Conceptos clave:**
  - Microservicio backend con servidor WSGI.
  - **Ruta `/`**: Renderiza un panel web moderno en HTML5/CSS3 con estética negro profundo (`#0A0B10`), tarjetas con sombreado azul neón (`#00E5FF`) y enlaces interactivos.
  - **Ruta `/api/info`**: Endpoint REST que expone metadatos del servicio en JSON.
  - **Ruta `/api/librerias`**: Endpoint REST con el catálogo estructurado de los 12 módulos.
  - Modo verificación con `app.test_client()` o servidor interactivo con bandera `--serve`.

### 12. `scikit-learn` (Biblioteca Externa)
* **Archivo:** [`machine_learning/12_sklearn_demo.py`](machine_learning/12_sklearn_demo.py)
* **Conceptos clave:**
  - Síntesis de datos: `make_regression` y `make_classification`.
  - Preprocesamiento: Particionado `train_test_split` (80% train / 20% test) y estandarización Z-score con `StandardScaler`.
  - **Regresión Lineal**: Ajuste de pendiente e intercepto, predicción continua, evaluación con Error Cuadrático Medio (MSE) y $R^2$ Score.
  - **Clasificación Logística**: Predicción probabilística binaria, cálculo de Exactitud (Accuracy), matriz de confusión ($TN, FP, FN, TP$) y reporte detallado de métricas (Precision, Recall, F1-Score).

---

## 📊 Artefactos Producidos en la Carpeta `output/`

Al ejecutar la práctica completa o mediante `python run_all.py --all`, se generan automáticamente los siguientes archivos de salida en [`output/`](output/):

| Archivo | Generador | Descripción del Contenido |
| :--- | :--- | :--- |
| `alumnos_calificaciones.csv` | `04_csv_demo.py` | Tabla plana generada con `csv.writer`. |
| `inventario_tecnologico.csv` | `04_csv_demo.py` | Registros basados en diccionarios con `csv.DictWriter`. |
| `resumen_ventas_pandas.csv` | `08_pandas_demo.py` | Agregación por región exportada con `DataFrame.to_csv()`. |
| `reporte_fpdf_neon.pdf` | `05_fpdf_demo.py` | Documento PDF en modo oscuro neón con tablas de servicios. |
| `reporte_reportlab_neon.pdf` | `06_reportlab_demo.py` | Documento PDF con diagramas vectoriales y tablas Platypus. |
| `grafico_rendimiento_neon.png` | `09_matplotlib_demo.py` | Gráfico científico de alta definición (300 DPI) con estética neón. |

---

## 👨‍💻 Créditos y Autoría

- **Materia:** Tópicos Avanzados de Programación
- **Unidad:** Unidad 2 — Práctica 1: Ejemplos de Librerías de Python
- **Autor / Repositorio:** [@keego124-design](https://github.com/keego124-design)
- **Licencia:** MIT License
