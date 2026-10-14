import pandas as pd

datos = pd.read_csv("envios_medios.csv")

#print(datos.head())
#print("Cantidad de envíos:", len(datos))

tabla_clima = pd.crosstab(
    datos["clima"],
    datos["medio_recomendado"],
    normalize="index"
)

print("\nPorcentaje de cada medio según el clima:")
print((tabla_clima * 100).round(2))

columnas = ["distancia_km", "peso_kg", "volumen_l"]

resumen = datos.groupby("medio_recomendado")[columnas].agg(
    ["min", "median", "max"]
)

print(resumen)

from usar_modelo import es_posible

def revisar_etiqueta(fila):
    return es_posible(fila["medio_recomendado"], fila)

datos["etiqueta_valida"] = datos.apply(
    revisar_etiqueta,
    axis=1
)
print(datos["etiqueta_valida"].value_counts())

tabla_zona = pd.crosstab(
    datos["zona_destino"],
    datos["medio_recomendado"],
    normalize="index"
)

print("\nPorcentaje de cada medio según la zona:")
print((tabla_zona * 100).round(2))

periferia = datos[datos["zona_destino"] == "periferia"]

print("\nDistancias de los envíos a periferia:")
print(periferia["distancia_km"].agg(["min", "median", "max"]))

porcentaje_supera_7 = (
    periferia["distancia_km"] > 7
).mean() * 100

print(
    f"Envíos a periferia que superan 7 km: "
    f"{porcentaje_supera_7:.2f}%"
)

rural = datos[datos["zona_destino"] == "rural"]

print("\nDistancias de los envíos rurales:")
print(rural["distancia_km"].agg(["min", "median", "max"]))

print(
    "Envíos rurales que superan 15 km:",
    (rural["distancia_km"] > 15).sum()
)

print("Total de envíos rurales:", len(rural))

camionetas_cortas = datos[
    (datos["medio_recomendado"] == "camioneta")
    & (datos["distancia_km"] < 2)
].copy()

def necesita_camioneta(fila):
    otros_medios = ["bicicleta", "moto", "dron"]

    return not any(
        es_posible(medio, fila)
        for medio in otros_medios
    )

camionetas_cortas["obligatoria"] = camionetas_cortas.apply(
    necesita_camioneta,
    axis=1
)

print("\nCamionetas en viajes menores de 2 km:")
print("Total:", len(camionetas_cortas))
print("Sin otro medio permitido:", camionetas_cortas["obligatoria"].sum())
print("Con otro medio permitido:", (~camionetas_cortas["obligatoria"]).sum())