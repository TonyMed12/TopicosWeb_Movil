import pandas as pd

datos = pd.read_csv("envios_medios.csv")


## Cantidades para el dron
tabla = pd.crosstab(
    datos["hora_salida"],
    datos["medio_recomendado"]
)

print("Cantidad de envíos por hora y medio:")
print(tabla)

noche = (
    (datos["hora_salida"] < 6)
    | (datos["hora_salida"] >= 21)
)

cantidad_noche = noche.sum()
cantidad_dia = (~noche).sum()

print("\nEnvíos de noche:", cantidad_noche)
print("Envíos de día:", cantidad_dia)
print(f"Porcentaje nocturno: {noche.mean() * 100:.2f}%")