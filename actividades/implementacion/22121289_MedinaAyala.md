
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

## C4

## D1

## D2

## D3

## D4

## D5

## E1

## E2

## E3

## F1
a) ...
b) ...
c) ...
