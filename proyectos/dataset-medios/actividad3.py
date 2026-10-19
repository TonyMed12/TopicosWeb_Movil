import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from entrenar_arbol import NUMERICAS, CATEGORICAS, OBJETIVO

# Separar caracteristicas
datos = pd.read_csv("envios_medios.csv")

x = datos[NUMERICAS + CATEGORICAS]
y = datos[OBJETIVO]

x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
    x,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

## Cargar el modelo

modelo = joblib.load("modelo_medios.joblib")
predicciones = modelo.predict(x_prueba)

## Misma tabla
comparacion = x_prueba.assign(
    real=y_prueba,
    predicho=predicciones
)

# Nomas guardar los errores
errores = comparacion[
    comparacion["real"] != comparacion["predicho"]
]

# Contar confusiones
confusiones = (
    errores.groupby(["real", "predicho"])
    .size()
    .sort_values(ascending=False)
)

print("Envíos de prueba:", len(x_prueba))
print("Total de errores:", len(errores))
print(f"Porcentaje de errores: {len(errores) / len(x_prueba) * 100:.2f}%")

print("\nConfusiones: real → predicho")
print(confusiones)

print("\nLas tres confusiones más frecuentes:")
print(confusiones.head(3))