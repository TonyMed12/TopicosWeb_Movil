# Día 1 — Estudiar el caso web (sin código de dominio)

**Integrantes:**
- José Antonio Medina Ayala
- Cesar Enrique Díaz Maldonado
- Paulo Cesar Pérez Martínez
- Enrique Martínez
- Adrian Martínez Ortíz

## El problema

Una empresa de mensajería tiene su operación regada en varios lugares: páginas sueltas, un Excel de rutas y tres sistemas distintos para conectarse con los servicios de entrega. El objetivo del semestre es construir una sola plataforma que registre pedidos y decida cómo se entregan (camioneta, moto, bicicleta o dron), apoyándose en un sistema de inteligencia artificial que recomienda el medio más adecuado.

Lo importante no es solo que el sistema funcione, sino que esté diseñado de forma que, cuando algo cambie más adelante (un medio de entrega nuevo, otro proveedor de IA, otra forma de pago, otra pantalla), no haya que modificar medio sistema para lograrlo.


## Tabla de los siete puntos a resolver

| # | Punto a resolver | Qué ya resuelve Django | Qué falta construir | Qué no se debe copiar tal cual |
|---|---|---|---|---|
| 1 | Cada trámite repite su propia forma de revisar si hay sesión activa | El middleware de sesión y autenticación ya viene integrado por defecto | Marcar con `@login_required` las vistas que requieran sesión | Una clase propia de Front Controller o un manejo de sesión hecho a mano |
| 2 | Un switch enorme decide el medio de entrega, y cada proveedor de IA responde en un formato distinto | Nada, es lógica de dominio propia del proyecto | Strategy (una clase por medio de entrega, todas con el mismo contrato) + Adapter (traduce la respuesta de cada proveedor a un formato único) + una fábrica simple `crear("dron")` que hace el `new` fuera de la vista | Un solo `if`/`switch` mezclando la elección del medio con la traducción de cada proveedor; tampoco un Factory Method (`LogisticaAerea.crearMedio`), que solo se justifica si hay familias de trámite que redefinen el gancho |
| 3 | La plantilla de seguimiento consulta la base de datos directamente, y esa misma consulta se repite en otro reporte | El ORM (`Pedido.objects`, que ya hace de Repository) y el motor de plantillas | Un Service Layer (ej. `obtener_seguimiento`) que arme el contexto ya listo para la plantilla y para cualquier reporte | Una clase Repository propia encima del ORM (sería complejidad redundante), consultas SQL dentro de la plantilla, o duplicar la misma consulta en dos lugares |
| 4 | Cobro, alta del envío y aviso al cliente están mezclados, y un doble clic genera un cobro doble | `transaction.atomic` (que ya cumple el papel de Unit of Work) y `transaction.on_commit` (para ejecutar algo solo después de confirmar) | Envolver cobro + alta en un `transaction.atomic`; mandar el aviso con `on_commit` (Observer simple, después del commit); una clave de idempotencia para el pago; y PRG para que recargar no repita el envío | Mandar el aviso dentro de la misma transacción, confiar solo en deshabilitar el botón por JavaScript, o escribir una clase Unit of Work propia |
| 5 | La app y el panel piden la información de formas distintas, y la app hace muchas peticiones para pintar el inicio | `JsonResponse` (o Django REST Framework) | Un endpoint tipo BFF (`GET /api/pedidos/<id>`) que reutilice el mismo Service Layer del panel, pero devuelva JSON mínimo | Duplicar la consulta del pedido para la app en vez de reutilizar el Service Layer |
| 6 | Cuando el mapa o la IA se caen, hasta la información ya guardada deja de poder consultarse | Nada directo | Timeout en las llamadas externas + un flag para apagar la IA + que `GET /pedidos/<id>` de un folio ya guardado no dependa de la IA (responde con lo que ya está en la base) | Dejar la aplicación esperando una respuesta sin límite de tiempo; y por ahora no montar un Circuit Breaker completo, porque es más complejidad de la que pide este problema |
| 7 | Se propone Event Sourcing, CQRS y Redux global solo para generar un PDF sencillo | Vistas normales + autenticación | Autenticar → consultar el pedido → generar el archivo, nada más | Añadir Event Sourcing, CQRS o Redux para un trámite tan simple |

## Preguntas finales

**¿`urls.py` es Front Controller, Page Controller, o el camino hacia los dos?**
Es el camino hacia los dos. En Django, el Front Controller no es un solo archivo: lo forman en conjunto el handler (`WSGIHandler`), que recibe toda petición HTTP, la cadena de middleware por la que pasa esa petición, y el URLconf. Dentro de ese conjunto, `urls.py` es la parte que decide a qué vista mandar cada petición. Cada vista, a su vez, actúa como Page Controller del trámite específico. Por eso `urls.py` es el enlace entre el punto único de entrada y cada Page Controller.

**¿La plantilla Jinja/Django puede hacer SELECT? ¿Por qué sí o por qué no?**
Técnicamente podría, si se le pasa un queryset sin evaluar y la plantilla lo recorre. Pero no debería: rompe el patrón Template View / Service Layer, ya que la plantilla pasaría a decidir qué datos buscar en vez de solo mostrarlos. La vista o el servicio deben entregar el contexto ya resuelto.
