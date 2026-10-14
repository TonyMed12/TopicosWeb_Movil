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
