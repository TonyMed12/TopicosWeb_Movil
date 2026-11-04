
# Actividad individual — Lo que hay detrás de la implementación

Nombre: José Antonio Medina Ayala
Matrícula: 22121289
Equipo:

## A1
El entorno virtual es suficiente para la programación y creación del proyecto, sin embargo, una vez que sea puesto en producción no es una buena práctica repetir terminales del entorno virtual, ya que esto no funcionaria para hacer que corra en producción cuando está pensado para que corra localmente, aunque aísla el proyecto y sus dependencias, no está pensado para escalarse.
El contenedor Docker aísla procesos, dependencias y el entorno de ejecución, incluyendo bibliotecas del sistema y una versión de Python y no quiere decir que el contenedor solito esté funcionando o corriendo para producción.
Como vimos en parte de las clases, llegará un momento donde requiramos algo más avanzado que el desarrollo local al que podemos llegar mediante un entorno virtual, y que se requiera de un balanceador de carga y un servidor adecuado.

## A2
a) No se perdió, simplemente se apagó el entorno virtual en el que se estaba ejecutando su parte de desarrollo, esto cada vez que accedemos o salimos pasa y no quiere decir que se encuentre perdido, solo que comenzará a correr con las instancias de Python que se encuentran directamente dentro de la computadora y no del entorno virtual, los archivos se crearán dentro de la carpeta del proyecto.

b) Necesita volver a ejecutarlo en un entorno donde tenga Python, instalar las dependencias y reiniciar el entorno virtual. 
Requirements nos indica que es lo que necesita nuestro proyecto para funcionar, sin cambiamos de ubicación donde lo estamos corriendo, éste requerirá de nuevo sus paquetes para poder funcionar correctamente, este archivo los indica seguido de la versión de los mismos y podrá ser llamado para su instalación.

c) Activarla unicamente corre en la terminal en la que ha sido activada, este proceso requiere repetirse en cada terminal nueva, pero esto no instala Python.

## A3
a) Existe dentro del sistema de archivos de la imagen de Docker que nosotros hemos cargado, no existe localmente en nuestra computadora.
Workdir establece el directorio de trabajo o si no la crea, mientras que Copy le indica que archivos tiene que copiar a la carpeta que hemos establecido, en este caso /app

b) Evita que con cada commit que nosotros hagamos, al Git detectar las diferencias de archivos sobre el repositorio base contra el que estamos trabajando, el entorno virtual y sus variables se suban, añadiendo datos sensibles además de una carga no necesaria a nuestro proyecto, mientras que .db excluye la base de datos local, con la misma finalidad.

## B1
a) Van a requerir de diferentes entregas de datos, ya que estos se duplicarán si usamos la misma lógica y manejamos cada aplicacion por separado.

b) Se puede cambiar si la lógica de negocio de nuestra aplicacion no depende de lo que tenemos en frontend, cambiando la forma en la que se muestran los datos y los mismos que se entregan. como vimos en clase, pueden ser diferentes JSON para cada uno que sería el entregable a cada frontend mediante una API.


## B2
La aplicación movil podría dejar de mostrar algunos campos en específico, mientras el contrato vuelve a ser creado, ya que este le indica a la aplicación como se van a comunicar frontend y backend, por lo que tendrá que establecerse nuevamente para funcionar con una nueva versión para que ambos sean compatibles y continue mostrando los datos.

## B3
No estoy de acuerdo, considero que deberían existir ambos tipos de validaciones para fomentar la seguridad de nuestra aplicación, no se requiere unicamente una validación si se puede saltar un dato y terminar insertando texto o codigo que pueda hacer que nuestra aplicación funcione mal.
La validación en frontend es auxiliar a la del backend y la más importante para el usuario.

## C1
a) Escalar horizontalmente significa crear nuevas instancias con la capacidad de cómputo que ya tenemos, en este caso será para poder usarse mediante un balanceador de carga, mientras que un escalado vertical, significa que a una o varias de las instancias, se les incrementará la capacidad de cómputo que tenemos de la misma.
b) El escalado vertical está limitado por la capacidad máxima del equipo o del proveedor y por su costo.
c) Cuando hay tres copias de Django, se supone que nginx actúa como balanceador y distribuye las peticiones entre ellas, normalmente la atiende una de las copias para que no se ejecute en las tres a la vez.

## C2
a) Cada copia que hagamos tendrá su propia memoria, no va a compartir el mismo valor del diccionario ya que por cada una este cambiará.
b) Porque son diferentes procesos, y cada una puede llegar a un proceso diferente donde no esté registrado.
c) No fue culpa de Docker, si no del almacenamiento donde se mantenía, al quedar unicamente dependiendo de la memoria, si esta cambia, no quedará una persistencia entre los datos, requiere de una base de datos como PostgreSQL o alguna por el estilo.

## C3

La variable global solo guarda el destino dentro de la memoria del proceso que atendió la primera petición. Si la siguiente petición llega a otro worker o a otra copia de Django, ese valor no estará disponible, ya que los procesos no comparten su memoria. Además, una variable global no separa los datos de cada usuario y podría terminar mezclando sus destinos.

Con request.session se relacionan los datos con la sesión de cada usuario. En la configuración del proyecto, el navegador conserva una cookie con el identificador de sesión y los datos se guardan en la base de datos compartida. Así, cualquier copia de Django puede recuperar el destino, aunque no sea la misma que atendió la primera petición.

## C4

a) Si cada una de las cinco copias ejecuta la tarea de enviar el aviso, el cliente podría recibir cinco notificaciones del mismo evento. Esta tarea debe ejecutarse mediante un proceso separado o un mecanismo que coordine su ejecución. También conviene registrar que el aviso ya fue enviado para evitar duplicarlo si hay reintentos.

b) Las migraciones modifican la estructura de la misma base de datos que utilizan todas las copias. Si cada una intenta ejecutarlas al mismo tiempo, pueden generarse conflictos. Por eso se ejecutan como un paso separado del despliegue y las aplicaciones esperan a que termine correctamente.

c) En el escenario planteado se utilizan 80 conexiones. Si PostgreSQL permite 100, quedan 20 disponibles, y también hay que considerar las conexiones de administración y de otros procesos. Por eso no podemos agregar copias sin revisar la capacidad de la base de datos.

Si cada contenedor utiliza un archivo SQLite propio, cada copia terminará guardando información diferente. PostgreSQL permite que todas consulten y modifiquen una misma base de datos compartida.

## D1

a) Obtener una exactitud alta con los mismos datos del entrenamiento no demuestra que el modelo vaya a funcionar igual con datos nuevos. El árbol ya utilizó esos ejemplos para construir sus decisiones y podría haber aprendido detalles específicos de ellos.

b) Separar un 20% permite evaluar el modelo con datos que no utilizó durante el entrenamiento. El 80% restante se usa para entrenarlo y después se comparan sus predicciones contra las respuestas del conjunto de prueba.

c) La estratificación mantiene aproximadamente la misma proporción de cada medio en los dos conjuntos. Esto es importante porque el dron solo tiene 948 de los 10,000 envíos y queremos que también esté representado en la prueba.

## D2

Si representamos despejado como 0, lluvia como 1 y viento fuerte como 2, estamos introduciendo un orden numérico que no necesariamente corresponde al significado del clima. El árbol puede hacer cortes sobre esos números y agrupar categorías según ese orden artificial.

One-hot crea una columna para cada categoría e indica con 0 o 1 cuál corresponde al envío. Así se representa el clima sin asignarle una posición numérica frente a los demás.

La preparación se guarda junto con el modelo para que los datos nuevos reciban la misma transformación que los del entrenamiento. De otra forma podríamos cambiar el orden de las columnas o la representación de las categorías y obtener resultados incorrectos.

## D3

a) El árbol sin límite tiene 346 hojas y puede ajustarse demasiado a los detalles de los datos de entrenamiento. Si obtiene un resultado muy alto al entrenar, pero baja al evaluar datos nuevos, está presentando sobreajuste. Tener más hojas no significa que vaya a generalizar mejor.

b) Elegiría el árbol con profundidad de 8 porque la mejora del de profundidad 10 es pequeña y su tamaño es casi el doble. El de 8 mantiene un resultado parecido con una estructura más sencilla, que también es más fácil de revisar y explicar.

## D4

a) Una precisión de 0.839 significa que, de todos los envíos que el modelo clasificó como dron, el 83.9% realmente tenía esa etiqueta. Un recall de 0.905 significa que logró identificar el 90.5% de todos los envíos que estaban etiquetados como dron.

b) En este caso sería más grave recomendar un dron para un envío que no debería utilizarlo, porque podría incumplir restricciones y poner en riesgo la entrega. Por eso conviene cuidar la precisión del dron. No detectar uno que sí podía utilizarlo puede hacer que se elija otro transporte, pero no representa necesariamente el mismo riesgo.

c) El modelo puede equivocarse porque los datos contienen casos parecidos con etiquetas distintas, porque faltan características que expliquen la decisión o porque el árbol no representa perfectamente todos los patrones. Por eso su resultado no sustituye la revisión de las reglas del negocio.

## D5

La mejora del Random Forest es de aproximadamente un punto porcentual, pero también hay que considerar el tamaño y la facilidad para explicar sus decisiones. El árbol ocupa alrededor de 14 KB, mientras que el bosque ocupa cerca de 60 MB. Si cada proceso carga una copia, esa diferencia también aumenta el consumo de memoria.

El árbol permite seguir una ruta de decisiones para entender el resultado. En el Random Forest la explicación es menos directa porque combina varios árboles.

La vista de Django no tendría que cambiar si continúa utilizando la misma interfaz del recomendador. Se puede implementar otra clase que cargue el bosque y entregue una Sugerencia con el mismo formato que espera la aplicación.

## E1

a) El árbol aprende relaciones entre los datos y las etiquetas, pero eso no garantiza que respete siempre una restricción como impedir que el dron opere de noche. Puede recomendarlo si los patrones aprendidos lo llevan a esa respuesta.

b) Un modelo más grande tampoco garantiza que desaparezcan todos los errores. Las restricciones del negocio deben comprobarse de forma explícita, porque tienen que cumplirse aunque el modelo asigne una probabilidad alta a una opción incorrecta.

c) Las restricciones se mantienen en reglas.py para que se apliquen sin depender del modelo utilizado. Así, si cambiamos del árbol al Random Forest o a un servicio externo, las mismas reglas siguen revisando si el medio propuesto es válido.

## E2

No es una contradicción, porque los pedidos y el modelo tienen necesidades diferentes. Un pedido contiene información que cambia y debe estar disponible para cualquier copia de la aplicación, por eso requiere almacenamiento compartido y persistente.

El modelo cargado se utiliza para consultar y hacer predicciones, sin modificarlo durante cada petición. Por eso cada proceso puede mantener su propia copia en memoria, siempre que se controle qué versión utiliza y que haya memoria suficiente.

Además, mantenerlo cargado evita leer y reconstruir el archivo .joblib en cada petición, lo que reduciría el rendimiento.

## E3

El problema puede aparecer porque el archivo .joblib se generó con una versión de scikit-learn y la nueva imagen instaló otra. Al no fijar las versiones en requirements.txt, una reconstrucción puede crear un entorno distinto, aunque el código del proyecto siga igual.

Para evitarlo se deben fijar las versiones utilizadas para entrenar y ejecutar el modelo, incluyendo sus dependencias relevantes, y comprobar que el modelo carga correctamente antes del despliegue.

Esto se relaciona con los entornos virtuales y Docker porque ambos ayudan a controlar las dependencias. Sin embargo, el contenedor no garantiza por sí solo que dos construcciones instalen las mismas versiones si estas no quedaron especificadas.

## F1

a) Se puede crear una clase que implemente la interfaz RecomendadorIA y su método sugerir. Esta clase enviaría los datos al servicio externo y convertiría la respuesta al formato Sugerencia que ya utiliza la plataforma.

Esto corresponde al patrón Adapter, porque permite conectar una implementación externa con la interfaz que espera nuestra aplicación. Las vistas, la creación de los medios y las estrategias de entrega pueden mantenerse mientras se conserve ese contrato. También deben seguir aplicándose las reglas del negocio.

b) La petición llega a /entregas/recomendar/ y la vista valida el JSON, los campos requeridos y los valores numéricos. Después consulta al recomendador para obtener una propuesta de medio.

Las reglas revisan si la propuesta es posible para ese paquete. Si no cumple, se debe buscar una alternativa válida. Después crear_medio construye el objeto correspondiente y su estrategia calcula el tiempo y las indicaciones del plan. Finalmente, la vista devuelve la respuesta en JSON.

La IA participa en la recomendación, pero la validación, las restricciones, la creación del medio y el cálculo del plan siguen siendo responsabilidades de la aplicación.

c) La incorporación de IA no elimina la necesidad de los patrones de diseño. El Adapter permite cambiar de proveedor o de formato de respuesta sin modificar todas las partes que utilizan el recomendador.

También permite incorporar un tiempo máximo de espera y un recomendador de respaldo si el servicio externo falla. Las estrategias mantienen separado el cálculo de cada medio de transporte, mientras que las reglas siguen controlando las restricciones del negocio.

Si todo se resolviera directamente en la vista, esta terminaría mezclando las llamadas al servicio, el manejo de errores, las reglas y el cálculo del plan, haciendo más difícil mantener la aplicación.
