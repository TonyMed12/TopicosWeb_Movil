## Selección de Lenguajes de Programación
- José Antonio Medina Ayala
- ---

### Análisis de estacionamiento por computadora
--- 
> **Utilizando las cámaras ubicadas en una torre dentro del Instituto Tecnológico de Morelia, se requiere realizar un reconocimiento de los cajones de estacionamiento disponible con la finalidad de que personal de seguridad pueda cerrar el estacionamiento cuando no quepan más vehículos y evitar cualquier tipo de accidente o evitar perder el tiempo**

En casos practicos que he tenido la posibilidad de observar proyectos de vision por computadora, siendo de los más conocidos YOLO, podemos utilizar Python.
Python, porque tiene buenas herramientas y bibliotecas ya optimizadas para inteligencia artificial y procesamiento de imágenes al utilizar visión por computadora, facilitandonos probar y poco a poco ir entrenando y mejorando el modelo de detección.
Utilizaría Observer como modelo porque el sistema depende de cambios constantes y en tiempo real, cada vez que se ocupa o libera un cajón, los demás componentes reciben la actualización sin estar consultando continuamente a la cámara

---
---

### Comunicación con LoRa
---
> **Se plantea el problema de seleccionar un lenguaje de programación adecuado para poder trabajar con LoRa, argumentando por qué debe de utilizarse en este caso.**

En este caso, hablando de un pequeño proyecto, podemos utilizar WebSockets, o eventos para recibir y emitir las señales, simulando un pequeño WhatsApp
De acuerdo con lo investigado, C++ sería una buena opción para programar la comunicación LoRa, ya que permite controlar directamente placas como ESP32 y tiene librerías compatibles con estos módulos. 
Sin embargo, debido a la complejidad de desarrollar toda la interfaz en C++, y por la curva de aprendizaje en caso de tener menor cantidad de tiempo, yo utilizaría una tecnología más conocida para mí, como Next.js, para crear la aplicación web. 
Esta podría conectarse al dispositivo mediante una API o WebSockets, permitiendo enviar y recibir mensajes en tiempo real, mientras que C++ se encargaría únicamente de la comunicación entre los módulos LoRa.

Usando un el patrón de diseño con el que no estoy familiarizado, pero que creo que sería adecuado, Observer, ya que permite notificar automáticamente a los componentes de la aplicación cuando se recibe un nuevo mensaje. 
En este caso, el ESP32 recibiría los datos mediante LoRa y los enviaría a la aplicación web usando WebSockets; después los componentes desarrollados con Next.js actualizarían la conversación en tiempo real.
