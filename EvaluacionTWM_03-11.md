           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
             EXAMEN — MICROSERVICIOS, GATEWAY Y EL MONOLITO
                                CON API
              Tópicos Selectos de Tecnologías Web y Móvil

                            Eduardo Alcaraz
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Nombre: José Antonio Medina Ayala              Calificación: _________


Indicaciones
════════════

  Explicar cada respuesta con palabras propias y justificar el porqué.

  Puntaje: 100 puntos (10 × 10).


1 — La frase del compañero (10 puntos)
══════════════════════════════════════

  En el pizarrón quedó:

        La API separa clientes del servidor; los microservicios
        separan servidores entre sí.

  Un compañero dice: «Entonces, si mi monolito Django expone una API y
  además lo meto en Docker, ya cumplí las dos mitades de la frase.»

  a) Desarmen su argumento. ¿Qué parte de la frase cree cumplir con la
  API? ¿Qué parte cree cumplir con Docker? ¿En qué se equivoca en cada
  una?

  Respuesta:
  Cree que la API separa al cliente del servidor y que Docker separa
  el servidor en microservicios.

  La API sí permite que el cliente se comunique con el servidor mediante
  un contrato: rutas, datos de entrada y respuestas. Pero no elimina
  todas las dependencias: el cliente todavía necesita respetar ese
  contrato. Tampoco divide por dentro la aplicación.

  Docker permite ejecutar la aplicación en un entorno aislado, pero
  meter todo el sistema en un contenedor no separa sus responsabilidades.
  Sigue siendo una sola aplicación que se actualiza y despliega junta.

  b) Den un contraejemplo mínimo: mismo código Django, con API y con
  Docker, que sigamos pudiendo llamar monolito. ¿Qué tendría que
  añadir (o partir) para que deje de serlo?

  Respuesta:
  Un proyecto Django contiene usuarios, pedidos y recomendaciones.
  Expone esas funciones mediante una API y todo corre en un contenedor.
  Sigue siendo monolito porque las tres funciones forman una sola
  aplicación y se despliegan juntas.

  Para empezar a dividirlo, podría extraer Recomendaciones a otro
  servicio, con su propio proceso y despliegue. Pedidos lo consultaría
  por una API. Así podría actualizar Recomendaciones sin tener que
  volver a desplegar Pedidos.

  c) ¿La frase del pizarrón habla de tecnologías (Docker, REST) o de
  límites de proceso / despliegue? Defiendan su lectura con lo que
  vieron en clase.

  Respuesta:
  Habla principalmente de límites y responsabilidades, no de usar una
  tecnología específica.

  La API define cómo se comunican cliente y servidor. Los microservicios
  separan partes del sistema que pueden ejecutarse y desplegarse de
  manera independiente.

  Docker y REST ayudan a construir ese diseño, pero usarlos no convierte
  automáticamente una aplicación en microservicios.


2 — Tres rutas, una trampa (10 puntos)
══════════════════════════════════════

  El equipo muestra este urls.py de un solo proyecto Django:

      path("usuarios/", ...),
      path("pedidos/", ...),
      path("recomendar/", ...),

  y este docker-compose.yml:

      services:
        api:
          build: .
          ports: ["8000:8000"]
          deploy:
            replicas: 3

  Afirman: «Tres rutas + tres réplicas = microservicios con alta
  disponibilidad.»

  a) Separen las dos ideas que mezclaron (rutas vs réplicas). ¿Qué
  problema resuelve cada una y cuál no resuelve?

  Respuesta:
  Las rutas permiten acceder a distintas funciones de una aplicación.
  Tener tres rutas no significa tener tres servicios independientes.

  Las réplicas son copias de la misma aplicación. Pueden repartir carga
  y ayudar a mantener el servicio si una copia falla, pero no separan
  las responsabilidades del sistema.

  Además, poner tres réplicas no garantiza alta disponibilidad: hace
  falta repartir las solicitudes entre copias sanas y evitar que una
  sola falla, como la del equipo o la base de datos, tire todo.

  b) Si una de las tres réplicas se cae a mitad de un POST /pedidos,
  ¿el sistema dejó de ser monolito? ¿Por qué sí o por qué no?

  Respuesta:
  No. Sigue siendo un monolito porque cada réplica contiene la misma
  aplicación completa. Una caída cambia su disponibilidad, no su
  arquitectura.

  La solicitud en curso puede quedar sin respuesta. Incluso podría
  haberse guardado el pedido antes de la caída, así que reenviarla sin
  controles podría crear un duplicado.

  c) Rediseñen solo con palabras el compose para que sí ilustre
  microservicios. ¿Cuántas imágenes distintas mínimo y por qué?

  Respuesta:
  Para separar las tres responsabilidades mostradas pondría:

  • usuarios: administra usuarios y sus datos.
  • pedidos: registra pedidos y consulta a Recomendaciones.
  • recomendar: ejecuta el modelo y sugiere el medio de transporte.

  Cada servicio tendría su propio proceso y podría desplegarse por
  separado. Podría añadirse un gateway como entrada pública.

  Para ilustrarlo claramente usaría tres imágenes de aplicación, una
  por responsabilidad; cuatro si también contamos el gateway.

  Aun así, no existe un mínimo universal de imágenes para que haya
  microservicios: una misma imagen puede ejecutar servicios distintos
  con diferentes comandos. Lo decisivo es la separación real de
  responsabilidades y despliegues, no contar imágenes.


3 — El gateway que «hace de más» (10 puntos)
════════════════════════════════════════════

  Les proponen este diseño «para no complicar»:

        Un solo contenedor nginx+Python que: valida el JWT, elige
        el medio con el .joblib, guarda el pedido en SQLite,
        manda el correo y devuelve el HTML.

  Lo llaman «API Gateway».

  a) ¿Es un gateway? Si no, ¿qué es? Usen la analogía del recepcionista
  (o otra) y digan qué oficios mezclaron.

  Respuesta:
  Tiene funciones de gateway, pero el conjunto es una aplicación
  concentrada en un solo despliegue, parecida a un monolito.

  Un recepcionista recibe personas, revisa su acceso y las dirige al
  lugar correcto. Aquí también le encargaron elegir el transporte,
  registrar pedidos y enviar correos.

  Validar el JWT y dirigir solicitudes sí encajan en el gateway.
  Decidir la logística y guardar pedidos son tareas del negocio.

  b) Mencionen tres consecuencias malas de ese diseño cuando el modelo
  pesado se reentrena cada semana y el correo empieza a fallar.

  Respuesta:
  1. Actualizar el modelo puede obligar a desplegar toda la aplicación,
     poniendo en riesgo también la entrada y el registro de pedidos.

  2. El modelo pesado puede consumir memoria y procesador que necesitan
     las demás funciones, haciendo lento todo el sistema.

  3. Si el envío de correo se espera dentro de la solicitud, sus fallas
     pueden retrasar o hacer parecer fallido un pedido que ya se guardó.
     El cliente podría reenviarlo y provocar duplicados.

  c) Partan ese contenedor en piezas. Para cada pieza digan: ¿queda en
  el borde (gateway) o detrás? No inventen diez servicios.

  Respuesta:
  • Gateway, en el borde: recibe solicitudes, valida el acceso, aplica
    límites y las dirige. También puede servir el HTML.

  • Pedidos, detrás: valida y guarda el pedido, crea el folio y coordina
    la consulta del medio de transporte.

  • Recomendar, detrás: carga el .joblib y recomienda el transporte.

  • Avisos, detrás: si se necesita aislar las fallas del correo, procesa
    avisos pendientes y reintenta enviarlos sin bloquear los pedidos.

  El entrenamiento del modelo iría en un proceso aparte que publique
  una versión validada; no dentro de la petición del cliente.


4 — localhost, la trampa favorita (10 puntos)
═══════════════════════════════════════════════

  Pedidos corre en un contenedor. Recomendar en otro, misma Compose.
  Alguien «arregla» la conexión así:

      RECOMENDAR_URL=http://127.0.0.1:8002

  En su laptop, sin Docker, ese curl a 127.0.0.1:8002 sí funcionaba.

  a) Expliquen por qué en Compose ese arreglo suele fallar aunque
  Recomendar esté sano. ¿A qué proceso apunta 127.0.0.1 desde dentro
  de Pedidos?

  Respuesta:
  127.0.0.1 significa «este mismo entorno de red».

  Dentro del contenedor de Pedidos apunta al propio contenedor de
  Pedidos, no al de Recomendar ni a la laptop anfitriona.

  La dirección no identifica por sí sola un proceso: el puerto 8002
  busca un proceso que esté escuchando ahí dentro de Pedidos. Si no
  existe, la conexión falla.

  b) ¿Por qué http://recomendar:8002 sí tiene chance de funcionar?
  ¿Quién «inventa» el nombre recomendar?

  Respuesta:
  Porque Docker ofrece resolución de nombres dentro de la red compartida.
  El nombre del servicio definido en Compose, recomendar, permite
  encontrar su contenedor.

  Funciona si ambos servicios comparten esa red y Recomendar escucha
  en el puerto interno 8002, en una interfaz accesible como 0.0.0.0.

  c) Ahora Recomendar se muda a la laptop de otro alumno
  (192.168.0.57). Escriban la URL y dos condiciones necesarias.

  Respuesta:
      RECOMENDAR_URL=http://192.168.0.57:8002

  Deben cumplirse estas dos condiciones:

  1. Recomendar debe aceptar conexiones externas: escuchar en 0.0.0.0
     y, si usa Docker, publicar el puerto 8002 en la laptop.

  2. La red debe permitir la comunicación entre equipos y el firewall
     debe permitir la entrada al puerto 8002.

  Cambiar solo la URL no arregla un puerto cerrado, un servicio que
  escucha únicamente en localhost o una WiFi que aísla los equipos.


5 — Fallo parcial con números (10 puntos)
═════════════════════════════════════════

  Escenario:

  • 1000 POST /pedidos por hora en promedio.
  • Recomendar tarda 200 ms cuando está bien.
  • El 5 % del tiempo Recomendar no responde: timeout de 3 s.
  • Pedidos, si hay timeout, usa plan B: moto y responde en 50 ms.
  • El gateway añade 5 ms.

  a) En la hora «normal», ¿el cliente espera ~200 ms o ~3 s?
  ¿Quién pone el tiempo dominante?

  Respuesta:
  Espera aproximadamente 205 ms, sin contar otros tiempos que no se
  especifican: 200 ms de Recomendar y 5 ms del gateway.

  Recomendar pone el tiempo dominante. Los 3 segundos son el límite
  de espera cuando no responde, no una espera obligatoria.

  b) En el 5 % malo, con plan B: ¿el cliente ve error o pedido creado?
  ¿Qué «mentira útil» están aceptando?

  Respuesta:
  Si Pedidos logra guardarlo, el cliente ve el pedido creado con
  respuesta 200 y transporte en moto.

  Pero primero se espera a que venza el timeout:

      3000 ms + 50 ms + 5 ms = 3055 ms, unos 3.06 segundos.

  La «mentira útil» es continuar con una opción predeterminada aunque
  quizá no sea la óptima. No se debe fingir que el modelo la calculó.
  El plan B debe ser una opción válida para ese pedido.

  Si las solicitudes se distribuyen de forma uniforme, serían unas
  50 por hora usando el plan B.

  c) ¿Qué pasa si Pedidos reintenta 10 veces y Recomendar está caído
  10 minutos? ¿Plan B siempre es peor que reintentar?

  Respuesta:
  Cada solicitud podría acumular unos 30 segundos adicionales si hace
  diez reintentos de 3 segundos, además del intento inicial.

  Las solicitudes permanecen abiertas, ocupan recursos y pueden formar
  una cola. El gateway puede agotar su tiempo de espera y devolver un
  error antes de que Pedidos termine.

  También se aumenta el tráfico contra un servicio que ya está fallando.

  El plan B puede ser mejor si permite completar el pedido de manera
  válida y rápida. Reintentar sirve para fallas breves, pero debe hacerse
  pocas veces, con pausas y un límite total de espera.


6 — Apagan el «edificio equivocado» (10 puntos)
═══════════════════════════════════════════════

  Tres contenedores: gateway, pedidos, recomendar.
  Los experimentos se realizan por separado.

  Respuesta:
  Supongo que el gateway sirve el HTML y que Pedidos tiene el plan B
  descrito en la pregunta anterior.

  1. docker compose stop gateway

     El navegador no puede cargar la página desde http://IP:8080/
     ni crear pedidos por esa entrada. Normalmente verá un error de
     conexión.

     Pedidos y Recomendar siguen vivos. Desde dentro de la red todavía
     podrían recibir solicitudes directas y trabajar entre ellos.

  2. docker compose stop pedidos

     El gateway puede seguir mostrando la página porque sirve el HTML.
     Al intentar crear un pedido, no puede comunicarse con Pedidos y
     devuelve un error, normalmente 502 o 503 según su configuración.

     Gateway y Recomendar siguen vivos. Recomendar todavía podría
     responder consultas internas, pero no puede registrar pedidos.

  3. docker compose stop recomendar

     La página sigue cargando. Al crear un pedido, Pedidos detecta que
     Recomendar no está disponible y usa moto como plan B.

     El cliente recibe el pedido creado. Puede haber demora hasta que
     se detecte el fallo; si la conexión se rechaza de inmediato, no
     necesariamente se esperan los 3 segundos completos.

     Gateway y Pedidos siguen vivos. Sin plan B, la creación podría
     fallar por depender de Recomendar.

  ¿En cuál parece más muerto hacia afuera?

  Cuando se apaga el gateway: desde la entrada pública no se puede
  acceder a nada, aunque los dos servicios internos sigan funcionando.

  Esto muestra que el borde es una pieza crítica. Si hay una sola
  instancia y falla, deja inaccesibles servicios que siguen sanos.


7 — WiFi del salón, conflicto de roles (10 puntos)
══════════════════════════════════════════════════

  • Ana: gateway + HTML.
  • Beto: pedidos.
  • Carla: recomendar.
  • Diana: otro gateway «por si Ana falla».

  El cliente configura a veces la IP de Ana y a veces la de Diana.

  a) ¿Qué problema de diseño introdujo Diana aunque todo responda 200?

  Respuesta:
  Hay dos entradas que el cliente debe conocer y elegir manualmente.
  Si sus configuraciones son distintas, podrían aplicar reglas de
  acceso diferentes o dirigir solicitudes a distintos destinos.

  Tener dos gateways no está mal por sí mismo: pueden dar redundancia.
  El problema es que no están coordinados detrás de una entrada estable
  ni existe un mecanismo definido para elegir uno sano.

  Lo adecuado sería una dirección pública común que reparta el tráfico,
  con las mismas reglas en ambos gateways.

  b) Beto configuró RECOMENDAR_URL=http://localhost:8002, pero
  Recomendar está en la laptop de Carla. ¿Cómo lo corrigen?

  Respuesta:
  localhost apunta a la propia máquina o contenedor de Beto, por lo que
  no encuentra el servicio que corre en la laptop de Carla.

  Debe configurar la dirección real de Carla, por ejemplo:

      RECOMENDAR_URL=http://192.168.0.57:8002

  Carla debe aceptar conexiones externas y permitir ese puerto. Así
  mantienen los servicios separados y se comunican por la red.

  c) La WiFi tiene AP isolation. ¿Pueden hacer la práctica tal cual?
  Propongan un plan B.

  Respuesta:
  Si el aislamiento impide las conexiones entre alumnos, no pueden
  hacerla tal cual. Un ping fallido por sí solo no demuestra que HTTP
  esté bloqueado, pero el aislamiento indicado sí impide la práctica.

  Como plan B, pueden ejecutar gateway, pedidos y recomendar en
  contenedores separados dentro de una misma laptop y una red Compose.

  Se conserva la lección porque siguen siendo procesos separados,
  comunicándose por red y pudiendo detenerse de manera independiente.


8 — El front que conoce demasiado (10 puntos)
═════════════════════════════════════════════

  El HTML hace esto al enviar el formulario:

      await fetch("http://192.168.1.20:8002/sugerir", { ... });
      await fetch("http://192.168.1.30:8001/pedidos", { ... });

  El autor dice: «Más rápido: me salto el gateway.»

  a) Listen tres problemas.

  Respuesta:
  1. Seguridad: los servicios internos deben quedar accesibles para el
     navegador y las llamadas pueden saltarse los controles del gateway.

  2. Dependencia de direcciones: el front conoce las IP y puertos internos.
     Si cambian, hay que modificar su configuración o código.

  3. Coordinación: el navegador controla dos pasos que pueden fallar por
     separado. Podría obtener una recomendación y nunca crear el pedido,
     o repetir el envío y crear pedidos duplicados.

  b) Rediseñen la secuencia correcta con gateway: una llamada desde el
  navegador. ¿Quién habla con Recomendar y por qué no el navegador?

  Respuesta:
  La secuencia sería:

      Navegador → Gateway → Pedidos.

  Pedidos consulta a Recomendar, recibe el resultado o aplica el plan B,
  guarda el pedido y devuelve el folio. La respuesta regresa al navegador
  pasando por el gateway.

  Pedidos habla con Recomendar porque le corresponde coordinar la
  creación del pedido. Así el navegador solo envía una solicitud y no
  necesita conocer la organización interna.

  c) El selector de modelo va en el JSON. ¿Quién debería crear el folio?
  ¿Qué invariante rompen si los dos «crean» algo?

  Respuesta:
  Pedidos debe crear el folio porque es el responsable del pedido.
  Recomendar solo devuelve una sugerencia usando el modelo solicitado.

  La regla que debe mantenerse es: un mismo pedido tiene un único folio
  oficial. Si ambos generan folios de pedido, pueden aparecer dos
  identificadores para la misma operación o registros sin relación clara.

  Recomendar puede tener un identificador de consulta, pero ese
  identificador no sustituye al folio del pedido.


9 — El LLM vendedor (10 puntos)
═══════════════════════════════

  Producto: tienda + envíos.

  • Modelo .joblib: medio de transporte.
  • LLM: texto para convencer al cliente en la ficha del producto.

  Proponen un microservicio cerebro que hace ambas cosas en una
  petición /inteligente.

  a) Critiquen el nombre y el corte. ¿Qué oficios mezclaron?
  ¿Qué falla si el LLM tarda 8 s y despacho necesita < 500 ms?

  Respuesta:
  El nombre cerebro no explica su responsabilidad. Mezcla logística
  de envíos con redacción de textos comerciales solo porque ambas
  funciones usan modelos.

  Sus necesidades son distintas: el despacho necesita rapidez y el
  texto comercial puede tardar más o generarse con anticipación.

  Si la respuesta espera a que terminen ambas tareas, los 8 segundos
  del LLM impiden responder el despacho en menos de 500 ms.

  b) Propongan dos endpoints o servicios y digan quién los usa.

  Respuesta:
  • POST /textos-producto
    Genera el texto comercial. Lo usa el front de tienda mediante el
    gateway. Puede devolver un texto previamente generado o uno básico
    si el LLM no está disponible.

  • POST /sugerir-transporte
    Recomienda el medio de transporte con el .joblib. Lo usa Pedidos
    dentro del flujo de pedido y envío.

  Pueden pertenecer a dos servicios separados para poder ajustar sus
  recursos y actualizaciones de forma independiente.

  c) El LLM vive en un servidor GPU en otra red. ¿El front apunta a
  la GPU o al gateway? ¿Qué configuración se cambia al mudar proveedor?

  Respuesta:
  El front apunta al gateway. El servicio de textos es quien se comunica
  con el proveedor del LLM.

  Si cambia el proveedor, se actualiza la configuración central de ese
  servicio, por ejemplo LLM_BASE_URL, sin cambiar el front.

  Si el nuevo proveedor usa una API diferente, también debe adaptarse
  la integración dentro del servicio de textos; cambiar la URL por sí
  solo podría no ser suficiente.


10 — El inversionista y la semana imposible (10 puntos)
═══════════════════════════════════════════════════════

  Hoy:

  • Panel interno: monolito Django, funciona y tiene poco tráfico.
  • App clientes: gateway + pedidos + recomendar.
  • Idea: LLM de ventas, aún no implementado.
  • Equipo: 5 personas.
  • Inversionista: «Todo a microservicios en 7 días o no hay dinero».

  a) Respuesta al inversionista: máximo 8 líneas, con postura y riesgo.

  Respuesta:
  No recomiendo dividir todo el sistema en siete días.
  El panel funciona y su tráfico no justifica esa urgencia.
  Separarlo exige ajustar comunicación, datos, despliegues y pruebas.
  Con cinco personas, hacerlo a ciegas aumenta el riesgo de fallas.
  Podríamos terminar con pedidos duplicados o servicios inaccesibles.
  Esta semana propongo proteger la API y aislar el entrenamiento.
  Después dividiremos lo que las mediciones indiquen que lo necesita.

  b) Ordenen las cuatro iniciativas de más a menos urgente.

  Respuesta:
  Orden propuesto: 3 → 2 → 1 → 4.

  Primero, 3: meter autenticación y límites de solicitudes en el gateway.
  La entrada pública necesita controlar quién accede y evitar que un
  exceso de solicitudes deje sin servicio a los clientes.

  Segundo, 2: sacar el reentrenamiento a un proceso aparte.
  Permite entrenar y validar el modelo sin interrumpir Pedidos ni
  consumir sus recursos durante la atención al cliente.

  Tercero, 1: partir el panel Django en seis microservicios.
  Lo dejaría pendiente porque funciona y tiene poco tráfico. Primero
  comprobaría si existe una necesidad real de dividir alguna parte.

  Cuarto, 4: subir el LLM sin timeouts ni plan B.
  No lo aprobaría en esas condiciones: puede dejar solicitudes abiertas
  y empeorar el servicio. Antes de publicarlo necesita límites de espera
  y una respuesta alternativa.

  Este orden supone que no hay una falla activa más urgente. Si el
  entrenamiento ya estuviera tirando Pedidos, atendería primero eso.

  c) Inventen una métrica observable para decidir cuándo partir algo
  del monolito.

  Respuesta:
  Mediría cuántos despliegues exclusivos del módulo de reportes provocan
  una interrupción en el resto del panel.

  Por ejemplo: si en un mes tres actualizaciones de reportes interrumpen
  otras funciones del panel, sería una señal para evaluar su separación
  y permitir que se despliegue de manera independiente.

  Primero revisaría la causa: si basta corregir el despliegue, separar
  el módulo podría ser un trabajo innecesario.

  d) Frase propia: ¿microservicios son el objetivo o la herramienta?

  Respuesta:
  Los microservicios son una herramienta: vale la pena usarlos cuando
  separar una parte resuelve más problemas de los que agrega.
