"""
=============================================================================
PROYECTO: Unidad 2 Práctica 1 - Ejemplos de Librerías de Python
ARCHIVO: 12_sklearn_demo.py
LIBRERÍA: scikit-learn (Biblioteca Externa)
DESCRIPCIÓN: Implementación de algoritmos fundamentales de Aprendizaje Automático:
             - Generación de conjuntos de datos sintéticos controlados.
             - Particionado de datos en entrenamiento y prueba (train_test_split).
             - Normalización de características (StandardScaler).
             - Modelo 1: Regresión Lineal (predicción continua, MSE, R^2 Score).
             - Modelo 2: Clasificación Logística (predicción binaria, Accuracy, Matriz de Confusión).
=============================================================================
"""

import sys
import numpy as np
from sklearn.datasets import make_regression, make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def banner(titulo: str):
    """Imprime un separador visual para la consola."""
    print("\n" + "=" * 65)
    print(f" >>> [SCIKIT-LEARN DEMO] - {titulo}")
    print("=" * 65)


def demo_regresion_lineal():
    """Entrenamiento y evaluación de un modelo de Regresión Lineal."""
    banner("1. Regresión Lineal (Predicción Continua)")

    # 1. Generar dataset sintético (500 muestras, 1 característica con ruido)
    print("[*] Generando dataset sintético de regresión (N=500, noise=15.0)...")
    X, y = make_regression(n_samples=500, n_features=1, noise=15.0, random_state=42)

    # 2. Dividir en Entrenamiento (80%) y Prueba (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    print(f"    - Muestras de entrenamiento : {X_train.shape[0]}")
    print(f"    - Muestras de prueba (test) : {X_test.shape[0]}")

    # 3. Instanciar y entrenar el modelo
    modelo_reg = LinearRegression()
    modelo_reg.fit(X_train, y_train)

    print(f"\n[*] Parámetros aprendidos por el modelo:")
    print(f"    - Pendiente (Coeficiente W) : {modelo_reg.coef_[0]:.4f}")
    print(f"    - Intercepto (Sesgo b)      : {modelo_reg.intercept_:.4f}")

    # 4. Evaluación en conjunto de prueba
    y_pred = modelo_reg.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"\n[*] Métricas de Desempeño en Test:")
    print(f"    - Error Cuadrático Medio (MSE) : {mse:.2f}")
    print(f"    - Coeficiente de Determinación (R^2): {r2:.4f} (Excelente ajuste)")

    # 5. Inferencia con nuevos datos
    nuevas_muestras = np.array([[-2.5], [0.0], [2.5]])
    predicciones = modelo_reg.predict(nuevas_muestras)
    print(f"\n[*] Predicciones sobre nuevos valores sintéticos:")
    for val_x, val_y in zip(nuevas_muestras.flatten(), predicciones):
        print(f"    - Entrada X = {val_x:>4.1f}  ==>  Predicción Y = {val_y:.2f}")


def demo_clasificacion_binaria():
    """Entrenamiento y métricas de un Clasificador Logístico."""
    banner("2. Clasificación Binaria (Regresión Logística)")

    # 1. Generar dataset sintético para clasificación (400 muestras, 4 variables)
    print("[*] Generando dataset sintético de clasificación binaria (N=400, features=4)...")
    X, y = make_classification(
        n_samples=400,
        n_features=4,
        n_informative=3,
        n_redundant=1,
        random_state=123
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=123)

    # 2. Escalamiento de características (Feature Scaling con StandardScaler)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 3. Entrenar Clasificador
    clf = LogisticRegression(random_state=123)
    clf.fit(X_train_scaled, y_train)

    # 4. Predicción y Métricas
    y_pred_clf = clf.predict(X_test_scaled)
    exactitud = accuracy_score(y_test, y_pred_clf)

    print(f"\n[*] Métricas de Evaluación de Clasificación:")
    print(f"    - Exactitud (Accuracy Score): {exactitud * 100:.2f}%")

    # Matriz de Confusión
    matriz_conf = confusion_matrix(y_test, y_pred_clf)
    print("\n[*] Matriz de Confusión [Verdaderos Positivos / Falsos]:")
    print(f"    TN={matriz_conf[0,0]:<3} | FP={matriz_conf[0,1]:<3}")
    print(f"    FN={matriz_conf[1,0]:<3} | TP={matriz_conf[1,1]:<3}")

    print("\n[*] Reporte de Clasificación Detallado (Precision / Recall / F1-Score):")
    print(classification_report(y_test, y_pred_clf, target_names=["Clase 0 (Neg)", "Clase 1 (Pos)"]))


def main():
    print("\n" + "#" * 65)
    print(" EJECUCIÓN DEL MÓDULO: scikit-learn")
    print(" Algoritmos de Machine Learning supervisado para regresión y clasificación")
    print("#" * 65)

    demo_regresion_lineal()
    demo_clasificacion_binaria()

    print("\n[OK] Demostración de scikit-learn finalizada con éxito.\n")


if __name__ == "__main__":
    main()
