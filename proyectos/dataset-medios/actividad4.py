"""Actividad 4: importancia de columnas y evaluación al eliminarlas.

Ejecutar:
    python actividad_4.py
"""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import export_text

from entrenar_arbol import NUMERICAS, CATEGORICAS, OBJETIVO


BASE = Path(__file__).resolve().parent


def imprimir_tabla(encabezados, filas):
    """Imprime una tabla en formato Markdown."""
    print("| " + " | ".join(encabezados) + " |")
    print("|" + "|".join(["---"] + ["---:"] * (len(encabezados) - 1)) + "|")

    for fila in filas:
        print("| " + " | ".join(map(str, fila)) + " |")

    print()


def main():
    datos = pd.read_csv(BASE / "envios_medios.csv")

    columnas = NUMERICAS + CATEGORICAS
    x = datos[columnas]
    y = datos[OBJETIVO]

    x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
        x,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42,
    )

    # clone conserva la configuración, pero elimina el entrenamiento.
    modelo_guardado = joblib.load(BASE / "modelo_medios.joblib")
    modelo = clone(modelo_guardado)
    modelo.fit(x_entreno, y_entreno)

    predicciones = modelo.predict(x_prueba)
    exactitud_base = accuracy_score(y_prueba, predicciones)

    print(f"Exactitud original: {exactitud_base:.2%}")
    print(f"Entrenamiento: {len(x_entreno)}")
    print(f"Prueba: {len(x_prueba)}\n")

    # ------------------------------------------------------------
    # 1. Importancia de cada columna original.
    # ------------------------------------------------------------
    preparacion = modelo.named_steps["preparacion"]
    arbol = modelo.named_steps["arbol"]

    nombres = preparacion.get_feature_names_out()
    importancias = arbol.feature_importances_

    importancia_por_columna = dict.fromkeys(columnas, 0.0)

    for nombre, importancia in zip(nombres, importancias):
        # Ejemplos:
        # numericas__peso_kg -> peso_kg
        # categoricas__clima_lluvia -> clima_lluvia
        nombre_sin_prefijo = nombre.split("__", 1)[1]

        columna_original = next(
            columna
            for columna in columnas
            if nombre_sin_prefijo == columna
            or nombre_sin_prefijo.startswith(columna + "_")
        )

        importancia_por_columna[columna_original] += float(importancia)

    ordenadas = sorted(
        importancia_por_columna.items(),
        key=lambda elemento: elemento[1],
        reverse=True,
    )

    print("**Resultados de la importancia de las columnas:**\n")

    imprimir_tabla(
        ["Columna", "Importancia"],
        [
            [columna, f"{importancia * 100:.4f} %"]
            for columna, importancia in ordenadas
        ],
    )

    # ------------------------------------------------------------
    # 2. Eliminar una columna y volver a entrenar.
    # ------------------------------------------------------------
    resultados = []

    for columna in columnas:
        modelo_sin_columna = clone(modelo_guardado)

        numericas_restantes = [
            nombre for nombre in NUMERICAS if nombre != columna
        ]
        categoricas_restantes = [
            nombre for nombre in CATEGORICAS if nombre != columna
        ]

        codificador = clone(
            modelo_guardado.named_steps["preparacion"].transformers[1][1]
        )

        modelo_sin_columna.named_steps["preparacion"].transformers = [
            ("numericas", "passthrough", numericas_restantes),
            ("categoricas", codificador, categoricas_restantes),
        ]

        modelo_sin_columna.fit(
            x_entreno.drop(columns=columna),
            y_entreno,
        )

        predicciones_sin_columna = modelo_sin_columna.predict(
            x_prueba.drop(columns=columna)
        )

        exactitud = accuracy_score(
            y_prueba,
            predicciones_sin_columna,
        )

        cambio = (exactitud - exactitud_base) * 100

        if abs(cambio) < 1e-9:
            texto_cambio = "0.00 puntos"
        elif cambio < 0:
            texto_cambio = f"−{abs(cambio):.2f} puntos"
        else:
            texto_cambio = f"+{cambio:.2f} puntos"

        resultados.append([
            columna,
            f"{exactitud * 100:.2f} %",
            texto_cambio,
        ])

    print("**Exactitud al quitar una columna y volver a entrenar:**\n")

    imprimir_tabla(
        [
            "Columna eliminada",
            "Exactitud",
            f"Cambio respecto a {exactitud_base * 100:.2f} %",
        ],
        resultados,
    )

    # ------------------------------------------------------------
    # 3. Primeras preguntas del árbol.
    # ------------------------------------------------------------
    print("Primeros niveles del árbol:\n")

    print(
        export_text(
            arbol,
            feature_names=list(nombres),
            max_depth=3,
        )
    )


if __name__ == "__main__":
    main()