# Día 2 — Primer corte: proyecto Django y una petición

**Integrantes:**
- José Antonio Medina Ayala
- Cesar Enrique Díaz Maldonado
- Paulo Cesar Pérez Martínez
- Enrique Martínez
- Adrian Martínez Ortíz

## Qué se hizo, en pocas palabras

Ya existe el proyecto Django (`plataforma`) con una sola app (`entregas`). Con `POST /pedidos/` se da de alta un pedido y el servidor redirige a `GET /pedidos/<id>/`, donde se ve el seguimiento (folio, estado y un ETA de mentira). Todavía no hay medios de entrega ni IA.

La vista se mantiene delgada: solo llama a `registrar_pedido(...)`, que es donde vive el trámite. La plantilla no consulta nada; recibe el contexto ya listo.


## Archivos

| Archivo | Qué hace |
|---|---|
| `entregas/models.py` | Modelo `Pedido` (folio, destino, estado, fecha de creación). |
| `entregas/services.py` | `registrar_pedido(destino)` genera el folio y guarda el pedido; `obtener_seguimiento(pedido_id)` arma el contexto (folio, estado, ETA). |
| `entregas/views.py` | `crear_pedido` (POST) y `detalle_pedido` (GET). Cada una llama a una función del servicio y nada más. |
| `entregas/urls.py` y `plataforma/urls.py` | Las rutas. |
| `entregas/templates/entregas/seguimiento.html` | Solo pinta `folio`, `estado` y `eta`. |


## El camino de `POST /pedidos/` con nombres de Django

| # | Paso | Qué es en Django | ¿Lo escribimos nosotros? |
|---|---|---|---|
| 1 | Llega la petición | El manejador WSGI de Django: el único punto de entrada para toda petición y la puerta de entrada del Front Controller (que completan el middleware y el URLconf). | No. Ya lo trae el marco. |
| 2 | Middleware | La lista `MIDDLEWARE` de `settings.py`. Para este POST importa `CsrfViewMiddleware`, que rechaza (403) si falta el token. | No. Solo está declarado en la lista. |
| 3 | Rutas | `urls.py` decide a qué vista mandar la petición (`plataforma/urls.py` incluye `entregas/urls.py`). Es la parte del Front Controller que despacha. | Las rutas sí; el mecanismo, no. |
| 4 | Vista `crear_pedido` | Page Controller: toma `destino` del POST y llama al servicio. | Sí. Es delgada a propósito. |
| 5 | Servicio `registrar_pedido` | Genera el folio y guarda el pedido con el ORM. El ORM (`Pedido.objects`) ya hace de Repository, así que no escribimos otro. | Sí, el trámite. |
| 6 | Redirección | `redirect(...)` responde 302 hacia el GET del pedido. Es el patrón PRG: recargar la página no vuelve a mandar el POST. | Sí (una línea). |
| 7 | Vista `detalle_pedido` | Llama a `obtener_seguimiento` y le pasa el resultado a la plantilla. | Sí. |
| 8 | Plantilla | El motor de plantillas de Django pinta las variables. No consulta la base de datos. | La plantilla sí; el motor, no. |

**Lo que no es GoF nuestro porque el marco ya lo instancia:** el Front Controller, la cadena de middleware, el motor de plantillas y el Repository (el ORM).


## Pruebas hechas

Hay 5 pruebas en `entregas/tests.py`. Se corren con `python manage.py test` y pasan (`Ran 5 tests ... OK`). Comprueban que:

- `POST /pedidos/` crea el pedido y redirige (302) a `/pedidos/<id>/`.
- `GET /pedidos/<id>/` responde 200 con folio y estado "Registrado".
- Repetir el GET (como un F5) no crea otro pedido: la tabla sigue con un solo registro.
- Un GET a `/pedidos/` no crea nada (405) y un pedido inexistente da 404.

(Agregar aquí, solo si lo hacen: la prueba manual en el navegador del GET de un pedido creado desde la consola de Django.)


## Pendiente para los siguientes días

- Medios de entrega y la IA (todavía no existen).
- Validar `destino`, que hoy se guarda tal como llega.
- Un formulario para crear pedidos desde el navegador.


## Dudas del equipo

(Completar con lo que costó trabajo o no quedó claro este día.)
