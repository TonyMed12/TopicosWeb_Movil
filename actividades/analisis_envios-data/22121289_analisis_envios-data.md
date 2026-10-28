# Análisis de envios-data

- **Nombre:** José Antonio Medina Ayala
- **Número de control:** 22121289
- **Equipo:**

# Análisis por archivo

La distribución de los medios cambia entre los seis archivos. Eso ayuda a anticipar en cuáles puede funcionar mejor el modelo y en cuáles hay que revisar con más cuidado los resultados.

| Archivo | Moto | Camioneta | Bicicleta | Dron | Eskuter |
| ------- | ---- | --------- | --------- | ---- | ------- |
| envios1 | 25.0% | 25.0% | 25.0% | 25.0% | — |
| envios2 | 34.7% | 14.4% | 26.2% | 8.6% | 16.2% |
| envios3 | 73.7% | 15.8% | 7.7% | 2.8% | — |
| envios4 | 57.2% | 16.9% | 18.8% | 7.1% | — |
| envios5 | 45.8% | 16.8% | 28.0% | 9.5% | — |
| envios6 | 63.1% | 31.9% | 4.2% | 0.7% | — |

- **envios1:** está balanceado. Cada uno de los cuatro medios tiene 2,500 envíos, así que ninguno domina el archivo.
- **envios2:** incluye `eskuter`, una categoría que el modelo no conoce y que representa el 16.2% de los envíos.
- **envios3:** la moto concentra el 73.7% de los casos. En cambio, el dron solo aparece en el 2.8%.
- **envios4 y envios5:** la moto sigue siendo la más frecuente, pero el reparto es menos desigual. En `envios5` la bicicleta alcanza el 28.0%.
- **envios6:** casi el 95% corresponde a moto y camioneta. Solo hay 73 envíos de dron y 424 de bicicleta.

# Predicción:

1. `envios1` podría tener buena exactitud porque contiene suficientes casos de cada medio para evaluarlos. Aun así, estar balanceado no garantiza que el modelo acierte más.
2. El modelo no podrá responder `eskuter`, porque esa categoría no formó parte de su entrenamiento.
3. `envios2` probablemente tendrá la exactitud más baja. De entrada, más de 1,600 envíos pertenecen a una categoría que el modelo no puede reconocer.
4. Los casos de `eskuter` podrían terminar clasificados como moto o bicicleta, si sus características se parecen a las de esos medios.
5. El dron podría presentar más dificultades. Su resultado debe revisarse por separado, porque en varios archivos tiene poca presencia.
6. En `envios6`, los 73 casos de dron son pocos para sacar una conclusión estable. Unos cuantos errores pueden cambiar bastante sus métricas.
7. En archivos como `envios3` y `envios6`, una exactitud alta podría esconder errores en los medios menos frecuentes, porque acertar la moto ya aporta una parte grande del resultado total.

# Resultados de la prueba con el árbol de decisión

## Resumen

Estos son los resultados reportados en la prueba. La columna “Siempre la mayoritaria” sirve como referencia: muestra cuánto se acertaría si se respondiera siempre con el medio más común de cada archivo.

| Archivo | Exactitud | Siempre la mayoritaria | Error más notable |
| ------- | --------- | ---------------------- | ----------------- |
| envios1 | 95.4% | 25.0% | 453 drones clasificados como bicicleta |
| envios2 | 77.7% | 34.7% | 1,616 eskuters fallados: 1,405 como moto y 177 como bicicleta |
| envios3 | 94.5% | 73.7% | 204 camionetas clasificadas como moto |
| envios4 | 92.7% | 57.2% | 188 camionetas y 134 bicicletas clasificadas como moto |
| envios5 | 92.5% | 45.8% | 171 motos clasificadas como bicicleta |
| envios6 | 96.2% | 63.1% | Precisión del dron cercana al 58%, con 43 motos clasificadas como dron |

## ¿Se cumplieron las expectativas?

1. **Buena exactitud en `envios1`: sí, aunque no fue la más alta.** Llegó al 95.4%. `envios6` obtuvo el mejor resultado con 96.2%, a pesar de tener una distribución mucho menos balanceada.
2. **El modelo no reconoce `eskuter`: sí se cumplió.** Su precisión y recall fueron de 0. Todos los casos terminaron asignados a otra categoría.
3. **`envios2` sería el más difícil: sí se cumplió.** Su exactitud fue de 77.7%, mientras que los demás archivos quedaron entre 92.5% y 96.2%.
4. **Los eskuters se confundirían con moto o bicicleta: sí se cumplió en la mayoría de los casos.** De los 1,616 envíos, 1,405 se clasificaron como moto, cerca del 87%, y 177 como bicicleta, cerca del 11%. Los 34 restantes se clasificaron como dron.
5. **El dron tendría dificultades: los resultados respaldan esa expectativa.** El análisis reporta que tuvo el menor F1 de los cuatro medios conocidos en cinco de los seis archivos. En `envios2`, si se consideran todas las categorías, el peor resultado fue el de `eskuter`.
6. **El resultado del dron en `envios6` sería poco estable: sí se cumplió.** Se acertaron 61 de 73 casos, un recall cercano al 84%. Sin embargo, su precisión fue de alrededor del 58%, porque también se etiquetaron como dron envíos que realmente eran de moto.
7. **La exactitud podría ocultar errores en las minorías: se cumplió en parte.** `envios3` tuvo 94.5% de exactitud, pero la precisión del dron fue de 62.8%. De todos modos, el árbol supera la referencia de responder siempre moto, así que sí está aprendiendo más que la categoría más frecuente.

## Patrones que se repiten

- **Muchos errores terminan en moto.** Una parte importante de las camionetas mal clasificadas y la mayoría de los eskuters se predicen como moto. Esto podría estar relacionado con características compartidas, aunque haría falta revisar los datos para confirmarlo.
- **Los drones se confunden con bicicletas.** Pasa en todos los archivos y destaca en `envios1`, con 453 casos. Una posible explicación es que ambos medios aparezcan en envíos ligeros y de corta distancia.
- **Moto y bicicleta se confunden en ambos sentidos.** En los archivos de `envios2` a `envios6` se reportan entre 42 y 171 errores por dirección.
- **Las motos clasificadas como dron afectan su precisión.** Cuando hay pocos drones reales, esos falsos positivos pesan mucho. La precisión del dron baja a 62.8% en `envios3` y a 58.1% en `envios6`.
- **La camioneta tiene una precisión alta.** Alcanza el 99% o más en todos los archivos. Su recall queda entre 85% y 93%, porque algunas camionetas reales se clasifican como moto.

## Conclusiones

- En los cinco archivos que solo contienen los cuatro medios conocidos, el árbol alcanza entre 92.5% y 96.2% de exactitud. En todos supera la referencia de elegir siempre el medio mayoritario.
- El problema más claro aparece con `eskuter`. Como el modelo no tiene esa categoría entre sus posibles respuestas, falla todos sus casos y la exactitud de `envios2` baja a 77.7%. Para incorporarla, habría que incluir ejemplos de esa clase y volver a entrenar y evaluar el modelo.
- Revisar solo la exactitud no alcanza. También se necesitan precisión, recall y F1 por medio para identificar los errores que quedan escondidos en el promedio.
- Cuando un medio tiene pocos casos de evaluación, como el dron en `envios6`, sus métricas son más sensibles a unos cuantos errores. Eso no permite concluir por sí solo cuántos ejemplos de ese medio hubo durante el entrenamiento.
- Acertar las etiquetas del CSV significa coincidir con los datos usados para evaluar. Para saber si la recomendación es adecuada en la práctica, también hay que revisar las reglas y condiciones reales del envío.
