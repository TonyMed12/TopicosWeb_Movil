"""Actividad 5: comparación de estrategias de balanceo.

Ejecutar:
    python actividad_5.py

La prueba correcta siempre conserva los mismos 2000 envíos.
La sección de trampa es deliberadamente incorrecta.
"""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

from entrenar_arbol import NUMERICAS, CATEGORICAS, OBJETIVO
from usar_modelo import es_posible


BASE = Path(__file__).resolve().parent
COLUMNAS = NUMERICAS + CATEGORICAS


def imprimir_tabla(encabezados, filas):
    """Imprime una tabla en formato Markdown."""
    print("| " + " | ".join(encabezados) + " |")
    print("|" + "|".join(["---"] + ["---:"] * (len(encabezados) - 1)) + "|")

    for fila in filas:
        print("| " + " | ".join(map(str, fila)) + " |")

    print()


def balancear(x, y, modo):
    """Iguala las clases mediante submuestreo o sobremuestreo."""
    tabla = x.copy()
    tabla[OBJETIVO] = np.asarray(y)

    grupos = [
        grupo
        for _, grupo in tabla.groupby(OBJETIVO)
    ]

    if modo == "submuestreo":
        cantidad = min(len(grupo) for grupo in grupos)
    elif modo == "sobremuestreo":
        cantidad = max(len(grupo) for grupo in grupos)
    else:
        raise ValueError("Modo de balanceo desconocido.")

    grupos_balanceados = []

    for grupo in grupos:
        grupo_balanceado = resample(
            grupo,
            replace=len(grupo) < cantidad,
            n_samples=cantidad,
            random_state=42,
        )

        grupos_balanceados.append(grupo_balanceado)

    resultado = pd.concat(
        grupos_balanceados,
        ignore_index=True,
    )

    return resultado[COLUMNAS], resultado[OBJETIVO]


def main():
    datos = pd.read_csv(BASE / "envios_medios.csv")

    x = datos[COLUMNAS]
    y = datos[OBJETIVO]

    x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
        x,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42,
    )

    plantilla = joblib.load(BASE / "modelo_medios.joblib")

    def evaluar(
        x_entrenamiento,
        y_entrenamiento,
        class_weight=None,
        prueba=None,
        reales=None,
    ):
        """Entrena un árbol nuevo y evalúa sus predicciones."""
        if prueba is None:
            prueba = x_prueba
        if reales is None:
            reales = y_prueba

        modelo = clone(plantilla)
        modelo.set_params(arbol__class_weight=class_weight)
        modelo.fit(x_entrenamiento, y_entrenamiento)

        predicciones = modelo.predict(prueba)

        reales_dron = np.asarray(reales) == "dron"
        predicciones_dron = predicciones == "dron"

        imposibles = 0
        drones_imposibles = 0

        for medio, (_, paquete) in zip(
            predicciones,
            prueba.iterrows(),
        ):
            if not es_posible(medio, paquete):
                imposibles += 1

                if medio == "dron":
                    drones_imposibles += 1

        return {
            "entrenamiento": len(x_entrenamiento),
            "prueba": len(prueba),
            "exactitud": accuracy_score(reales, predicciones),
            "precision_dron": precision_score(
                reales_dron,
                predicciones_dron,
                zero_division=0,
            ),
            "recall_dron": recall_score(
                reales_dron,
                predicciones_dron,
                zero_division=0,
            ),
            "f1_macro": f1_score(
                reales,
                predicciones,
                average="macro",
            ),
            "predice_dron": int(predicciones_dron.sum()),
            "imposibles": imposibles,
            "drones_imposibles": drones_imposibles,
            "drones_detectados": int(
                (reales_dron & predicciones_dron).sum()
            ),
            "drones_no_detectados": int(
                (reales_dron & ~predicciones_dron).sum()
            ),
            "drones_incorrectos": int(
                (~reales_dron & predicciones_dron).sum()
            ),
        }

    # ------------------------------------------------------------
    # Parte A: referencias para interpretar la exactitud.
    # ------------------------------------------------------------
    print("Referencias de exactitud:\n")

    imprimir_tabla(
        ["Modelo hipotético", "Dataset completo", "Prueba"],
        [
            [
                "Nunca dice dron y acierta todo lo demás",
                f"{(y != 'dron').mean() * 100:.2f} %",
                f"{(y_prueba != 'dron').mean() * 100:.2f} %",
            ],
            [
                "Siempre dice moto",
                f"{(y == 'moto').mean() * 100:.2f} %",
                f"{(y_prueba == 'moto').mean() * 100:.2f} %",
            ],
        ],
    )

    # ------------------------------------------------------------
    # Parte B: estrategias correctas.
    # ------------------------------------------------------------
    resultados = {}

    resultados["Sin balancear"] = evaluar(
        x_entreno,
        y_entreno,
    )

    x_sub, y_sub = balancear(
        x_entreno,
        y_entreno,
        modo="submuestreo",
    )

    resultados["Submuestreo"] = evaluar(x_sub, y_sub)

    x_sobre, y_sobre = balancear(
        x_entreno,
        y_entreno,
        modo="sobremuestreo",
    )

    resultados["Sobremuestreo"] = evaluar(x_sobre, y_sobre)

    resultados["class_weight balanced"] = evaluar(
        x_entreno,
        y_entreno,
        class_weight="balanced",
    )

    print("**Resultados con los mismos 2000 envíos de prueba:**\n")

    imprimir_tabla(
        [
            "Estrategia",
            "Envíos de entrenamiento",
            "Exactitud",
            "Precision dron",
            "Recall dron",
            "Veces que predice dron",
            "Sugerencias imposibles",
        ],
        [
            [
                nombre,
                resultado["entrenamiento"],
                f"{resultado['exactitud'] * 100:.2f} %",
                f"{resultado['precision_dron'] * 100:.2f} %",
                f"{resultado['recall_dron'] * 100:.2f} %",
                resultado["predice_dron"],
                resultado["imposibles"],
            ]
            for nombre, resultado in resultados.items()
        ],
    )

    print(f"Drones reales en la prueba: {(y_prueba == 'dron').sum()}\n")

    print("**Detalle de los resultados del dron:**\n")

    imprimir_tabla(
        [
            "Estrategia",
            "Drones detectados",
            "Drones no detectados",
            "Predicciones dron incorrectas",
        ],
        [
            [
                nombre,
                resultado["drones_detectados"],
                resultado["drones_no_detectados"],
                resultado["drones_incorrectos"],
            ]
            for nombre, resultado in resultados.items()
        ],
    )

    # ------------------------------------------------------------
    # Trampa deliberada: balancear ANTES de separar.
    # Esta evaluación NO es válida para elegir el modelo.
    # ------------------------------------------------------------
    x_trampa, y_trampa = balancear(
        x,
        y,
        modo="sobremuestreo",
    )

    (
        x_entreno_trampa,
        x_prueba_trampa,
        y_entreno_trampa,
        y_prueba_trampa,
    ) = train_test_split(
        x_trampa,
        y_trampa,
        test_size=0.2,
        stratify=y_trampa,
        random_state=42,
    )

    resultado_trampa = evaluar(
        x_entreno_trampa,
        y_entreno_trampa,
        prueba=x_prueba_trampa,
        reales=y_prueba_trampa,
    )

    # Comprueba cuántas filas de prueba tienen las mismas
    # características que alguna fila del entrenamiento.
    filas_entrenamiento = set(
        map(tuple, x_entreno_trampa.to_numpy())
    )

    filas_compartidas = sum(
        tuple(fila) in filas_entrenamiento
        for fila in x_prueba_trampa.to_numpy()
    )

    print("**Trampa deliberada:**\n")

    imprimir_tabla(
        ["Resultado", "Valor"],
        [
            [
                "Filas de entrenamiento",
                resultado_trampa["entrenamiento"],
            ],
            [
                "Filas de prueba",
                resultado_trampa["prueba"],
            ],
            [
                "Filas de prueba con características idénticas "
                "a alguna de entrenamiento",
                filas_compartidas,
            ],
            [
                "Exactitud",
                f"{resultado_trampa['exactitud'] * 100:.2f} %",
            ],
            [
                "Precision dron",
                f"{resultado_trampa['precision_dron'] * 100:.2f} %",
            ],
            [
                "Recall dron",
                f"{resultado_trampa['recall_dron'] * 100:.2f} %",
            ],
            [
                "Veces que predice dron",
                resultado_trampa["predice_dron"],
            ],
            [
                "Sugerencias imposibles",
                resultado_trampa["imposibles"],
            ],
        ],
    )

    # ------------------------------------------------------------
    # Datos adicionales para interpretar y decidir.
    # ------------------------------------------------------------
    print("**F1 macro de las estrategias correctas:**\n")

    imprimir_tabla(
        ["Estrategia", "F1 macro"],
        [
            [
                nombre,
                f"{resultado['f1_macro'] * 100:.2f} %",
            ]
            for nombre, resultado in resultados.items()
        ],
    )

    print("**Recomendaciones de dron imposibles:**\n")

    imprimir_tabla(
        ["Estrategia", "Predicciones de dron imposibles"],
        [
            [nombre, resultado["drones_imposibles"]]
            for nombre, resultado in resultados.items()
        ],
    )

    eliminados = len(x_entreno) - len(x_sub)

    print(
        f"El submuestreo eliminó {eliminados} ejemplos "
        f"({eliminados / len(x_entreno):.2%} del entrenamiento)."
    )


if __name__ == "__main__":
    main()