## Actividades de análisis con el dataset

### Actividad 1.
 **Predigan.** 
- Cuando llueve, ¿qué medio creen que domina? 
	- Debería de dominar la camioneta, ya que es la forma de proteger el recurso que se está entregando y de igual forma la integridad del medio de transporte y quien lo utiliza, necesitaremos ver si en los resultados pesa más el costo beneficio o la protección del medio.
- ¿Y para el centro de la ciudad? 
	- Se utilizaría bicicleta o moto de acuerdo al tráfico, sería lo más util para evitar congestionamientos y altas faltas de estacionamiento a lo largo del trayecto, pondría en primer lugar motocicleta por la facilidad de uso y movimiento sin desgaste para quien maneja.
- ¿Cuál será la distancia más larga que recorre una bicicleta en los datos?
	- No he conseguido ver aún las distancias, pero debería de ser una distancia corta a media dentro de una ciudad, donde la posibilidad para transitar de forma segura en bicicleta exista, permitiendo mantener, como se mencionó anteriormente la integridad del recurso a entregar, así como de quien usa la bicicleta.
- ¿Habrá envíos con una etiqueta que rompa las reglas del negocio? 
	- Me inclinaría porque si, podría haber etiquetas que incumplan alguna regla, al no decidir de forma obvia ante situaciones inesperadas, posiblemente influyan de forma muy específica algunos factores como lluvia, tráfico, distancia, y situaciones que no están facilmente en manos de la predicción y puedan alterar el rumbo de lo que de forma lógica se esperaría que hiciera, de acuerdo a las actividades previas, existian situaciones en el 1.2% de los casos donde se proponía algo imposible físicamente para ser ejecutado, por lo que una vez trabajando con el CSV, probablemente exista algo parecido.

**Preguntas.**

1.  ¿En qué zonas y con qué climas el dron nunca aparece? ¿Qué regla del paso 12 lo explica en cada caso?
> -   **Centro:**  0 % de drones. Dentro de las reglas se prohíbe utilizarlos en esa zona por restricción del espacio aéreo. 
> -   **Lluvia y viento fuerte:**  0 % de drones. Solo se permiten con clima despejado.
> -   **Rural:**  0 % de drones. No existe una prohibición por ser rural pero los 1000 envíos rurales superan el límite de 15 km, fuera del límite.
La ausencia puede explicarse por otra característica, como la distancia, y no necesariamente por una regla sobre la zona.

**Tabla 1. Porcentaje de cada medio según el clima.**

| Clima | Bicicleta | Camioneta | Dron | Moto |
|---|---:|---:|---:|---:|
| Despejado | 32.84 % | 16.57 % | 13.52 % | 37.07 % |
| Lluvia | 8.49 % | 16.68 % | 0.00 % | 74.83 % |
| Viento fuerte | 31.69 % | 18.41 % | 0.00 % | 49.90 % |

**Tabla 2. Porcentaje de cada medio según la zona.**

| Zona de destino | Bicicleta | Camioneta | Dron | Moto |
|---|---:|---:|---:|---:|
| Centro | 58.45 % | 13.52 % | 0.00 % | 28.03 % |
| Periferia | 0.88 % | 13.98 % | 12.61 % | 72.53 % |
| Residencial | 26.20 % | 14.62 % | 17.30 % | 41.89 % |
| Rural | 0.00 % | 40.80 % | 0.00 % | 59.20 % |


2.  La bicicleta casi no va a la periferia, aunque ninguna regla se lo prohíbe. ¿Qué otra columna lo explica? Demuéstrenlo con un número.
> Por la distancia: el **97.75 %** de los envíos a periferia supera los 7 km permitidos para bicicleta.
Solo el 2.25 % cumple el límite de distancia, pero todavía debe cumplir las demás restricciones y resultar conveniente. Por eso únicamente **0.88 %** de los envíos a periferia están etiquetados como bicicleta.

**Tabla 3. Distancias de los envios a perferia y zonas rurales.**
| Zona de destino | Distancia mínima (km) | Mediana (km) | Distancia máxima (km) |
|---|---:|---:|---:|
| Periferia | 5.23 | 15.75 | 29.39 |
| Rural | 15.93 | 34.20 | 59.12 |

El **97.75 %** de los envíos a periferia supera los 7 km, límite permitido para bicicleta.

3.  Comparen los máximos de distancia, peso y volumen de cada medio con la tabla `LIMITES`. ¿Qué límites se pueden adivinar solo mirando los datos? ¿Cuál no y por qué?

| Medio | Distancia máxima observada / límite (km) | Peso máximo observado / límite (kg) | Volumen máximo observado / límite (L) |
|---|---:|---:|---:|
| Bicicleta | 7.00 / 7 | 7.99 / 8 | 39.70 / 40 |
| Moto | 39.90 / 40 | 24.93 / 25 | 89.99 / 90 |
| Dron | 14.99 / 15 | 2.50 / 2.5 | 11.98 / 12 |
| Camioneta | 59.12 / 1000 | 80.00 / 1000 | 400.57 / 3000 |

Los máximos observados permiten aproximar los límites de bicicleta, moto y dron, porque están muy cerca de ellos. Pero no demuestran por sí solos que sean restricciones obligatorias.

Los límites de camioneta no se pueden deducir de estos datos: sus máximos observados están muy por debajo de los límites definidos en `LIMITES`.

4.  Hay más de cien camionetas para viajes de menos de 2 km, lo que suena a desperdicio. ¿Cuántas tienen una razón clara para ir en camioneta? Para las que no, propongan una explicación.

| Camionetas en viajes menores de 2 km | Cantidad | Porcentaje |
|---|---:|---:|
| Sin otro medio permitido | 95 | 88.79 % |
| Con otro medio permitido | 12 | 11.21 % |
| **Total** | **107** | **100.00 %** |


De 107 envíos:

-   **95 (88.79 %)** requieren camioneta: ninguno de los otros medios está permitido.
-   **12 (11.21 %)** tienen al menos otro medio permitido.

Para esos 12, podemos proponer que la camioneta haya resultado conveniente por las temas de fragilidad o valor, o que la etiqueta se deba al ruido del generador.



### Actividad 2.
**Predigan.** 
- ¿Cuántos drones creen que salen a las 3:00? 
	- Considerando 24 horas del día, sabemos que dentro de los límites de uso de dron, está habilitado después de las 6 am, añadiendo estas restricciones, saldrían 0 drones, considerando que todas las etiquetas cumplen las reglas.
- ¿Qué porcentaje de los envíos creen que sale de noche (antes de las 6 o desde las 21)?
	- Creo que el dataset podría ser uniforme, por lo que este horario nocturno de acuerdo a que los drones y bicicleta se encuentran limitados, podría decir que alrededor de 30% si se opera de manera uniforme tanto de día como de noche unicamente utilziando estas restricciones.


**Cantidad de envíos por hora y medio:**

| hora_salida | bicicleta | camioneta | dron | moto |
|---|---:|---:|---:|---:|
| 0 | 2 | 12 | 0 | 63 |
| 1 | 6 | 11 | 0 | 49 |
| 2 | 5 | 19 | 0 | 59 |
| 3 | 4 | 13 | 0 | 60 |
| 4 | 2 | 10 | 0 | 47 |
| 5 | 8 | 25 | 0 | 116 |
| 6 | 94 | 50 | 33 | 136 |
| 7 | 204 | 92 | 68 | 233 |
| 8 | 205 | 118 | 57 | 252 |
| 9 | 187 | 97 | 65 | 279 |
| 10 | 192 | 123 | 68 | 273 |
| 11 | 178 | 107 | 72 | 283 |
| 12 | 217 | 111 | 82 | 297 |
| 13 | 211 | 112 | 70 | 284 |
| 14 | 204 | 103 | 72 | 274 |
| 15 | 199 | 122 | 81 | 303 |
| 16 | 213 | 108 | 59 | 260 |
| 17 | 192 | 97 | 69 | 292 |
| 18 | 162 | 97 | 72 | 248 |
| 19 | 166 | 78 | 45 | 199 |
| 20 | 115 | 72 | 35 | 160 |
| 21 | 20 | 58 | 0 | 240 |
| 22 | 5 | 28 | 0 | 116 |
| 23 | 5 | 15 | 0 | 55 |

----
| Horario | Cantidad de envíos | Porcentaje |
|---|---:|---:|
| Noche | 1053 | 10.53 % |
| Día | 8947 | 89.47 % |
| Total | 10000 | 100.00 % |



**Preguntas.**
1.  ¿En qué horas no hay ni un solo dron? ¿Coincide exactamente con la regla?
	
   No hay drones a las 0, 1, 2, 3, 4, 5, 21, 22 y 23 horas. Coincide exactamente con la regla: el dron solo está permitido desde las 6:00 hasta antes de las 21:00. Además, aparece en todas las horas permitidas.


2.  ¿Cuántos envíos de noche hay, comparados con los de día? ¿Qué consecuencia tiene eso para lo que el modelo puede aprender sobre la noche?


 Hay 1053 envíos nocturnos (10.53 %) y 8947 diurnos (89.47 %): aproximadamente 8.5 envíos de día por cada envío de noche.

   El modelo dispone de muchos menos ejemplos nocturnos para aprender. Esto puede dificultar que identifique los patrones de ese horario, especialmente en combinaciones poco frecuentes de clima, zona o características del paquete. No demuestra por sí solo que falle de noche.


3.  Entre las 20:00 y las 21:00 las bicicletas casi desaparecen y las motos aumentan. Busquen en el `README.md` qué lo explica.


Las bicicletas pasan de 115 envíos a las 20:00 a 20 a las 21:00, mientras que las motos aumentan de 160 a 240.

   El README.md explica que la bicicleta recibe una penalización por circular de noche. A partir de las 21:00, esa penalización puede hacer que la moto resulte más conveniente. La bicicleta sigue permitida, pero pierde competitividad. Además, desde las 21:00 el dron queda descartado por su restricción de horario.


4.  Un árbol solo pregunta «¿la hora es menor o igual que X?». ¿Por qué le cuesta representar «de noche»? ¿Cuántas preguntas sobre la hora necesitaría como mínimo?

 La noche comprende dos intervalos separados: horas menores que 6 y horas mayores o iguales que 21. Una sola comparación del tipo «hora ≤ X» divide las horas en dos grupos y no puede separar ambos extremos del intervalo diurno.

   Necesita como mínimo dos preguntas:

   - ¿La hora es menor o igual que 5.5? Si sí, es noche.
   - Si no, ¿la hora es menor o igual que 20.5? Si sí, es día; si no, es noche.


### Actividad 3.
**Predigan.**

- ¿Qué confusión creen que será la más frecuente?
    - Esperaría que la confusión más frecuente fuera entre moto y bicicleta, porque ambos medios pueden transportar paquetes pequeños y compartir algunas condiciones de uso. La elección puede depender de factores como distancia, prioridad y clima.

- ¿El modelo confundirá alguna vez una bicicleta con una camioneta?
    - Esperaría que no, o que fuera poco frecuente, pero posible, porque la camioneta también puede transportar paquetes pequeños. Aunque sus capacidades son muy distintas, algunos envíos podrían tener características similares.

**Resultados de la evaluación:**

| Resultado | Cantidad de envíos | Porcentaje |
|---|---:|---:|
| Predicciones correctas | 1842 | 92.10 % |
| Predicciones incorrectas | 158 | 7.90 % |
| Total de envíos de prueba | 2000 | 100.00 % |

**Confusiones: real a predicho**

| real | predicho | Cantidad |
|---|---|---:|
| moto | bicicleta | 46 |
| camioneta | moto | 32 |
| moto | dron | 29 |
| bicicleta | moto | 20 |
| dron | bicicleta | 18 |
| camioneta | bicicleta | 9 |
| camioneta | dron | 4 |

**Las tres confusiones más frecuentes:**

| real | predicho | Cantidad |
|---|---|---:|
| moto | bicicleta | 46 |
| camioneta | moto | 32 |
| moto | dron | 29 |

**Comparación con las predicciones.**

La confusión más frecuente fue moto con bicicleta, con 46 casos.
Esto es compatible con la hipótesis de que ambos medios pueden
compartir características de los envíos.

No hubo casos de bicicleta con camioneta. Sí hubo 9 casos en el
sentido contrario, camioneta a bicicleta. Por tanto, es importante
distinguir la dirección de cada confusión.

**Herramientas.**

- ¿Qué pasaría con el análisis si usáramos otro `random_state`?

    El modelo guardado fue entrenado con una separación realizada
    usando `random_state=42`. Si cambiamos ese valor al reconstruir
    la prueba, seleccionaríamos otros envíos y algunos podrían
    haber sido utilizados durante el entrenamiento del modelo.

    El análisis dejaría de evaluar exclusivamente envíos que el
    modelo nunca vio y podría dar una impresión demasiado favorable
    de su capacidad para generalizar.

**Preguntas.**

1. ¿Cuántos errores hay y cuáles son las tres confusiones más frecuentes? ¿Son entre medios parecidos o muy distintos? ¿Qué les dice eso?

    Hay 158 errores entre 2000 envíos de prueba, equivalentes
    al 7.90 %. La exactitud del modelo es 92.10 %.

    Las tres confusiones más frecuentes son moto → bicicleta
    (46 casos), camioneta → moto (32 casos) y moto → dron
    (29 casos).

    Los medios tienen capacidades diferentes, pero pueden compartir
    envíos para los que están permitidos. Moto y bicicleta pueden
    coincidir en paquetes pequeños y trayectos cortos; moto y dron,
    en paquetes ligeros; camioneta y moto, en paquetes que ambos
    pueden transportar.

    Esto sugiere dificultades para distinguir la opción conveniente
    en situaciones con características similares. Sin embargo,
    necesitamos revisar los casos para saber cuáles también
    incumplen restricciones del negocio.

2. Revisen los envíos que eran moto y el modelo mandó a dron. ¿Cuántos son de noche? ¿Cuáles corregirían las reglas del negocio y cuáles no? ¿Qué tienen en común los que no?

    Se identificaron 29 casos de moto → dron.

    Falta comprobar cuántos ocurrieron de noche y cuántos incumplen
    alguna restricción del dron mediante `es_posible`.

    Las reglas descartarían las sugerencias de dron que no estén
    permitidas. En cambio, no descartarían un dron permitido aunque
    la etiqueta del CSV fuera moto. Después revisaremos qué
    características comparten esos casos.

3. Revisen los que eran moto y el modelo mandó a bicicleta. ¿Están cerca del límite de 7 km? Si no es la distancia, busquen qué columnas los distinguen de las bicicletas que el modelo sí acertó.

    Se identificaron 46 casos de moto → bicicleta.

    Falta revisar sus distancias y comparar sus características
    con los envíos de bicicleta correctamente clasificados.
    Analizaremos, entre otras columnas, hora, clima, prioridad,
    peso, volumen, fragilidad y valor declarado.

**Para pensar.**

Como recomendación provisional, priorizaría los errores
moto → bicicleta porque son los más frecuentes: 46 casos,
equivalentes al 29.11 % de los 158 errores.

Mantendría las reglas del negocio para impedir recomendaciones
imposibles. La decisión final también debe considerar el costo
de cada error: el más frecuente no necesariamente es el más grave.


### Actividad 4.
**¿Qué columnas usa de verdad el modelo?**

**Predigan.**

Antes de revisar los resultados, propondría el siguiente orden de importancia para elegir el medio de transporte:

1. `distancia_km`.
2. `peso_kg`.
3. `volumen_l`.
4. `refrigerado`.
5. `clima`.
6. `hora_salida`.
7. `zona_destino`.
8. `prioridad`.
9. `fragil`.
10. `trafico`.
11. `valor_declarado_mxn`.
12. `largo_cm`.
13. `ancho_cm`.
14. `alto_cm`.

Esperaría que el modelo no utilizara las tres dimensiones de la caja, porque ya cuenta con el volumen calculado. Sin embargo, esto es una predicción y debe comprobarse con el árbol.

**Resultados de la importancia de las columnas:**

| Columna | Importancia |
|---|---:|
| distancia_km | 32.1999 % |
| volumen_l | 19.2928 % |
| clima | 14.3802 % |
| refrigerado | 13.1274 % |
| peso_kg | 12.6274 % |
| hora_salida | 5.8716 % |
| fragil | 1.9851 % |
| prioridad | 0.3087 % |
| valor_declarado_mxn | 0.0723 % |
| ancho_cm | 0.0655 % |
| largo_cm | 0.0274 % |
| alto_cm | 0.0254 % |
| trafico | 0.0165 % |
| zona_destino | 0.0000 % |

Las importancias se obtuvieron con `feature_importances_`. En las columnas categóricas se sumaron las importancias de sus categorías para presentar un resultado por columna original.

Por ejemplo, se sumaron las importancias de las columnas generadas para los distintos valores de `clima`.

Los valores sin redondear suman 1, equivalente al 100 %. Estos porcentajes representan la importancia dentro del árbol, no el porcentaje de aciertos atribuible a cada columna.

**Exactitud al quitar una columna y volver a entrenar:**

| Columna eliminada | Exactitud | Cambio respecto a 92.10 % |
|---|---:|---:|
| distancia_km | 79.30 % | −12.80 puntos |
| peso_kg | 90.40 % | −1.70 puntos |
| largo_cm | 92.05 % | −0.05 puntos |
| ancho_cm | 92.05 % | −0.05 puntos |
| alto_cm | 92.05 % | −0.05 puntos |
| volumen_l | 90.60 % | −1.50 puntos |
| fragil | 91.55 % | −0.55 puntos |
| refrigerado | 87.85 % | −4.25 puntos |
| valor_declarado_mxn | 92.10 % | 0.00 puntos |
| hora_salida | 89.10 % | −3.00 puntos |
| prioridad | 92.15 % | +0.05 puntos |
| zona_destino | 92.10 % | 0.00 puntos |
| clima | 84.45 % | −7.65 puntos |
| trafico | 92.10 % | 0.00 puntos |

Los cambios están expresados en puntos porcentuales.

**Herramientas.**

Se utilizó un árbol con la misma configuración del proyecto:

- `max_depth=8`.
- `min_samples_leaf=5`.
- `random_state=42`.

Se mantuvieron los mismos 8000 envíos de entrenamiento y 2000 de prueba, separados mediante estratificación y `random_state=42`.

Para cada experimento se eliminó una columna de la preparación, se volvió a entrenar el árbol y se evaluó con los mismos envíos de prueba.

El modelo entrenado sin modificaciones produjo las mismas predicciones que el modelo guardado del proyecto.

**Preguntas.**

1. ¿Cuáles son las cuatro columnas más importantes? ¿Coinciden con las primeras preguntas del árbol del paso 8? ¿Y con su predicción?

   Las cuatro columnas más importantes fueron:

   - `distancia_km`: 32.1999 %.
   - `volumen_l`: 19.2928 %.
   - `clima`: 14.3802 %.
   - `refrigerado`: 13.1274 %.

   Sí aparecen entre las primeras preguntas del árbol. Se observan divisiones por distancia alrededor de 7.01 y 39.91 km, por volumen alrededor de 90 litros, por clima de lluvia y por refrigeración.

   El orden de importancia global no tiene que ser exactamente el mismo que el orden de las preguntas, porque la importancia considera las divisiones de todo el árbol.

   Mi predicción coincidió en distancia, volumen y refrigeración entre las cuatro primeras. Sobreestimé el peso, que quedó quinto, y subestimé el clima, que quedó tercero.

   Las dimensiones sí se utilizaron, aunque con importancias muy pequeñas. La única columna con importancia exactamente cero fue `zona_destino`.

2. ¿Qué columna, al quitarla, baja más la exactitud? ¿Cuáles no la cambian nada?

   La mayor caída ocurrió al quitar `distancia_km`: la exactitud pasó de 92.10 % a 79.30 %, una reducción de 12.80 puntos porcentuales.

   Las columnas que se pudieron quitar sin cambiar la exactitud fueron:

   - `valor_declarado_mxn`.
   - `zona_destino`.
   - `trafico`.

   En los tres casos se mantuvo en 92.10 %.

   Al quitar `prioridad`, la exactitud aumentó a 92.15 %. Esto equivale a un acierto adicional y no demuestra, por sí solo, que eliminarla mejore el modelo en general.

   La importancia de una columna y el efecto de quitarla no son lo mismo. Al volver a entrenar, el árbol puede reorganizar sus preguntas y aprovechar otras columnas.

   Además, mantener la misma exactitud no significa necesariamente acertar y fallar exactamente los mismos envíos.

3. La zona de destino tiene importancia cero, pero en la actividad 1 vieron que el dron nunca va al centro. ¿Cómo puede ser que el modelo no use la zona y, aun así, la plataforma nunca mande un dron al centro?

   La plataforma combina el modelo con reglas del negocio.

   Aunque el árbol no utilice `zona_destino` y pueda sugerir un dron para un envío al centro, la función `es_posible` rechaza esa recomendación. Después, el recomendador busca otra alternativa permitida.

   Además, el generador del dataset ya impide asignar etiquetas de dron a envíos al centro.

   Por tanto, que el dataset no tenga drones al centro no demuestra que el árbol haya aprendido esa prohibición. La regla externa es la que garantiza que la recomendación final respete esa restricción.

**Para pensar.**

No dejaría de pedir un dato únicamente porque este árbol le asigne importancia cero.

Por ejemplo, `zona_destino` sigue siendo necesaria para impedir drones al centro y bicicletas a zonas rurales. Otros datos pueden servir para calcular costos, gestionar seguros, realizar auditorías o entrenar modelos futuros.

Las dimensiones permiten calcular el volumen y también pueden ser útiles para comprobar que el paquete cabe físicamente.

Sí revisaría qué información necesita capturarse manualmente. El volumen puede calcularse a partir de las dimensiones; la hora puede obtenerse del horario programado; el clima y el tráfico podrían consultarse automáticamente.

La decisión debe considerar las necesidades de toda la plataforma, no únicamente las columnas que utiliza este modelo.

### Actividad 5.
**El dron es minoría: ¿hay que balancear el dataset?**

**Parte A — Pensar antes de tocar los datos.**

1. ¿Qué exactitud tendría un modelo que nunca dice dron y siempre acierta todo lo demás? ¿Y uno que siempre dice moto? ¿Qué les dice eso sobre usar la exactitud para juzgar un dataset desbalanceado? ¿Qué medidas del paso 7 usarían en su lugar?

   Un modelo que nunca predice dron y acierta todos los demás envíos tendría 90.52 % de exactitud en el dataset completo, porque solamente fallaría los 948 drones de los 10000 envíos.

   En los 2000 envíos de prueba tendría 90.50 %, porque hay 190 drones reales.

   Un modelo que siempre predice moto tendría 45.78 % de exactitud en el dataset completo y 45.75 % en la prueba.

   Esto muestra que una exactitud aparentemente alta puede ocultar que el modelo no reconoce una clase: el primer modelo tendría recall de dron igual a cero.

   Usaría precision, recall y F1 por clase, además de la matriz de confusión. También revisaría F1 macro, que da el mismo peso a cada clase, y el número de sugerencias imposibles.

2. ¿Por qué hay tan pocos drones? ¿Es un error de los datos o refleja cómo funciona la empresa? ¿Cambia eso la decisión de balancear?

   El dataset es sintético y representa una operación donde el dron solamente puede utilizarse bajo condiciones específicas:

   - Peso máximo de 2.5 kg.
   - Volumen máximo de 12 litros.
   - Distancia máxima de 15 km.
   - Clima despejado.
   - Horario desde las 6:00 hasta antes de las 21:00.
   - Destino fuera del centro.
   - Paquete sin refrigeración.

   Además, que el dron sea posible no significa que sea la opción más conveniente. El generador compara costos y condiciones entre los medios permitidos.

   Por eso, la minoría del dron está prevista en el diseño y no demuestra un error en los datos.

   No balancearía solamente para que todas las clases tengan la misma cantidad. Primero revisaría cómo reconoce el modelo los drones y qué costo tienen sus errores.

3. Si deciden balancear, ¿se balancea antes o después de separar los datos de entrenamiento y de prueba? ¿Se balancean también los datos de prueba?

   Primero separaría entrenamiento y prueba. Después balancearía únicamente los datos de entrenamiento.

   Si repetimos ejemplos antes de separar, podrían quedar copias del mismo envío en entrenamiento y prueba. Esto provoca fuga de información y la evaluación deja de representar correctamente el comportamiento con envíos nuevos.

   No balancearía los datos de prueba. Los mantendría con su distribución original para representar las condiciones del dataset y comparar todas las estrategias con los mismos envíos.

   Si también balanceamos la prueba, cambia el peso de cada clase en la exactitud y cambia la interpretación de la precision. Ya no estaríamos realizando la misma evaluación.

**Parte B — Probar estrategias.**

Se comparó el modelo original con tres formas de balancear:

- **Submuestreo:** reducir todas las clases a 758 ejemplos, que es la cantidad de drones en entrenamiento.
- **Sobremuestreo:** repetir ejemplos de las clases minoritarias hasta que cada clase tenga 3663 filas, que es la cantidad de motos en entrenamiento.
- **Pesos de clase:** mantener los 8000 envíos y utilizar `class_weight="balanced"` para dar mayor peso a las clases menos frecuentes durante el entrenamiento.

En todos los casos se conservaron los mismos parámetros del árbol, excepto `class_weight` en la estrategia correspondiente.

**Resultados con los mismos 2000 envíos de prueba:**

| Estrategia | Envíos de entrenamiento | Exactitud | Precision dron | Recall dron | Veces que predice dron | Sugerencias imposibles |
|---|---:|---:|---:|---:|---:|---:|
| Sin balancear | 8000 | 92.10 % | 83.90 % | 90.53 % | 205 | 31 |
| Submuestreo | 3032 | 89.75 % | 88.94 % | 93.16 % | 199 | 29 |
| Sobremuestreo | 14652 | 90.20 % | 76.61 % | 100.00 % | 248 | 35 |
| class_weight balanced | 8000 | 90.30 % | 76.61 % | 100.00 % | 248 | 35 |

La prueba contiene 190 drones reales.

Las sugerencias imposibles se contaron aplicando `es_posible` a la predicción directa de cada modelo, antes de que la plataforma la corrija. El conteo incluye sugerencias de cualquier medio de transporte.

**Detalle de los resultados del dron:**

| Estrategia | Drones detectados | Drones no detectados | Predicciones dron incorrectas |
|---|---:|---:|---:|
| Sin balancear | 172 | 18 | 33 |
| Submuestreo | 177 | 13 | 22 |
| Sobremuestreo | 190 | 0 | 58 |
| class_weight balanced | 190 | 0 | 58 |

El modelo original detectó 172 de los 190 drones reales. El submuestreo detectó 177. El sobremuestreo y los pesos de clase detectaron los 190, pero también recomendaron dron para más envíos cuya etiqueta real era otro medio.

**Trampa deliberada.**

Para realizar una evaluación incorrecta a propósito, se repitieron ejemplos hasta igualar todas las clases antes de separar entrenamiento y prueba.

Esto permitió que copias de un mismo envío quedaran en ambos conjuntos y cambió la distribución de la prueba.

| Resultado | Valor |
|---|---:|
| Filas de entrenamiento | 14649 |
| Filas de prueba | 3663 |
| Filas de prueba con características idénticas a alguna de entrenamiento | 2392 |
| Exactitud | 91.92 % |
| Precision dron | 91.03 % |
| Recall dron | 97.49 % |
| Veces que predice dron | 981 |
| Sugerencias imposibles | 46 |

Comparado con el sobremuestreo realizado correctamente, la exactitud aparente aumentó de 90.20 % a 91.92 % y la precision del dron pasó de 76.61 % a 91.03 %.

Sin embargo, el recall bajó de 100.00 % a 97.49 %. No todas las métricas mejoraron y la exactitud tampoco superó al modelo original sin balancear.

La mejora aparente no demuestra una mayor capacidad para generalizar. Hay 2392 filas de prueba cuyas características también están presentes en entrenamiento.

Además, la prueba ahora contiene aproximadamente 25 % de cada clase. Aumentar artificialmente la proporción de drones puede elevar su precision sin que eso represente una mejora ante la distribución original.

Los conteos absolutos de predicciones e imposibles tampoco deben compararse directamente con los anteriores, porque esta prueba tiene 3663 filas en lugar de 2000.

**Parte C — Interpretar.**

1. ¿Qué pasó con el recall del dron y qué pasó con su precision? ¿Por qué una sube cuando la otra baja?

   Con sobremuestreo y pesos de clase, el recall del dron aumentó de 90.53 % a 100.00 %, mientras que la precision bajó de 83.90 % a 76.61 %.

   Los modelos identificaron todos los drones reales, pero también clasificaron como dron más envíos que pertenecían a otros medios.

   Al aumentar la influencia del dron durante el entrenamiento, el árbol puede ampliar las situaciones en las que lo recomienda. Esto permite recuperar drones que antes no detectaba, pero también produce más falsos positivos.

   Sin embargo, no es obligatorio que una métrica suba cuando la otra baja. Con submuestreo mejoraron tanto la precision como el recall del dron, aunque disminuyó la exactitud global.

2. ¿Alguna estrategia dejó al modelo con muchos menos datos de entrenamiento? ¿Qué se pierde con eso?

   El submuestreo redujo el entrenamiento de 8000 a 3032 ejemplos.

   Se eliminaron 4968 ejemplos, equivalentes al 62.10 % del entrenamiento original.

   Se pierde diversidad de las clases mayoritarias y pueden desaparecer ejemplos de situaciones poco frecuentes. Esto puede dificultar que el modelo aprenda correctamente los límites entre esas clases.

   En este experimento, la exactitud global bajó de 92.10 % a 89.75 %.

3. Si dos estrategias distintas les dieron números casi iguales para el dron, expliquen por qué son, en el fondo, la misma idea.

   El sobremuestreo y `class_weight="balanced"` obtuvieron la misma precision y recall del dron, y ambos lo predijeron 248 veces.

   Las dos estrategias aumentan la influencia relativa de las clases minoritarias. El sobremuestreo lo hace repitiendo ejemplos; los pesos de clase lo hacen aumentando el peso de esos ejemplos en los cálculos del árbol.

   No son exactamente equivalentes. Las repeticiones se seleccionan aleatoriamente y parámetros como `min_samples_leaf` dependen del número de filas.

   Por eso, aunque las métricas del dron coincidieron, la exactitud global fue ligeramente distinta: 90.20 % con sobremuestreo y 90.30 % con pesos de clase.

   Tener las mismas métricas tampoco demuestra que ambos modelos hayan realizado exactamente las mismas predicciones.

4. En el paso 15, el motivo de la respuesta dice «confianza 84 %». Después de balancear, ¿ese porcentaje sigue significando lo mismo?

   No debe interpretarse automáticamente como una probabilidad del 84 % de acertar en la operación real.

   En un árbol de decisión, `predict_proba` utiliza las proporciones de clases de la hoja donde termina el envío. Cuando se utilizan pesos de clase, esas proporciones se calculan con los pesos correspondientes.

   Balancear modifica la distribución de entrenamiento o la influencia de cada clase. El dron deja de representar aproximadamente el 9.5 % de los ejemplos y pasa a tener una presencia o un peso parecido al de las demás clases.

   Por eso, el porcentaje puede dejar de reflejar la frecuencia real del dron.

   Incluso antes de balancear, la confianza del árbol no garantiza una probabilidad bien calibrada. Para presentarla como tal habría que evaluarla y, si corresponde, calibrarla con datos separados que mantengan la distribución real.

**Parte D — Decidir.**

**Para pensar.**

Como recomendación provisional, mantendría el modelo sin balancear.

Obtuvo la mayor exactitud global, 92.10 %, y ya detecta 172 de los 190 drones reales. También obtuvo el mayor F1 macro:

| Estrategia | F1 macro |
|---|---:|
| Sin balancear | 91.24 % |
| Submuestreo | 89.74 % |
| Sobremuestreo | 89.57 % |
| class_weight balanced | 89.54 % |

Esto no demuestra que sea necesariamente el modelo más rentable, porque todavía no conocemos el costo económico de cada tipo de error.

Si no utilizar un dron cuando convenía fuera muy costoso, consideraría los modelos balanceados. El sobremuestreo y los pesos de clase recuperaron los 18 drones que el modelo original no detectaba, pero aumentaron de 33 a 58 las recomendaciones incorrectas de dron.

Si recomendar un dron cuando no conviene implica más costos, retrasos o uso ineficiente de recursos, esa pérdida de precision puede ser importante.

Las reglas del negocio corrigen las recomendaciones imposibles: por ejemplo, un dron de noche, con lluvia, al centro o con un paquete demasiado pesado.

Sin embargo, no corrigen necesariamente una recomendación permitida pero inconveniente. De las 58 predicciones incorrectas de dron de los modelos con sobremuestreo y pesos de clase, 21 incumplen las reglas y 37 sí están permitidas por `es_posible`.

Las reglas tampoco obligan a elegir dron cuando el modelo recomienda otro medio permitido.

Por eso, antes de cambiar el modelo de la plataforma, también evaluaría las recomendaciones finales después del filtro y el costo de cada decisión.

Si mañana la empresa compra el doble de drones, no duplicaría automáticamente sus ejemplos en el dataset. Revisaría cómo cambian la disponibilidad, los costos y la capacidad de operación.

Tener más drones puede hacer conveniente utilizarlos en más envíos, pero no elimina sus restricciones de peso, volumen, distancia, clima, horario o zona.

Actualizaría la lógica de asignación y recopilaría nuevos datos antes de decidir si conviene reentrenar o balancear.

Finalmente, estos resultados corresponden a una sola separación fija de entrenamiento y prueba. Para tomar una decisión de producción necesitaríamos validación adicional y una evaluación final independiente.
