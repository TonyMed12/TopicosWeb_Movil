# Día 3 — Medio de entrega, proveedor externo y creación

**Integrantes:**
- José Antonio Medina Ayala
- Cesar Enrique Díaz Maldonado
- Paulo Cesar Pérez Martínez
- Enrique Martínez
- Adrian Martínez Ortíz


## Decisiones ligadas al caso

| Patrón | Inconveniente concreto | Qué no es |
|---|---|---|
| Strategy | Cuatro medios de entrega deben planear un pedido con el mismo contrato `planear(pedido, contexto) → plan`; cada medio puede cambiar su cálculo sin tocar la vista. | El adaptador no calcula la entrega: solo traduce datos ajenos. |
| Adapter | Un proveedor simulado entrega JSON con `route_hint` y `score`, y otro XML con `vehicle`. `AdaptadorJSON` y `AdaptadorXML` entregan al servicio una `Sugerencia(medio, motivo)`. | No selecciona ni construye la estrategia. |
| Fábrica simple | Cuando la sugerencia ya contiene el nombre del medio, `crear_medio(nombre)` crea la clase correspondiente en un solo lugar. | No es Factory Method: no tenemos familias de trámites que redefinan un método de creación. |

## Recorrido implementado

`POST /pedidos/` → `views.crear_pedido` → `services.registrar_pedido` → proveedor falso → adaptador → `Sugerencia` → `crear_medio` → `planear` → guardar `Pedido` → redirigir al seguimiento.

El proveedor JSON fijo recomienda motocicleta; el XML fijo recomienda bicicleta. Son datos simulados para demostrar los dos formatos, no una decisión basada en el destino. `medios.py` contiene contrato, estrategias y fábrica; `sugerencias.py` contiene los adaptadores y proveedores falsos. `services.py` orquesta. `views.py` desconoce las clases concretas y las claves `route_hint` y `vehicle` no aparecen en las estrategias.

Se guardan medio, detalle y horas estimadas para que el seguimiento muestre el plan del pedido. Los pedidos anteriores conservan un ETA de dos horas y no tienen medio asignado por la migración; no se les inventa una decisión que pueda aprender.

Si mañana llega un medio de transporte diferente, agregamos una estrategia en `medios.py` y su entrada en `crear_medio`; el proveedor de prueba podría empezar a recomendarlo. No habría que modificar la vista, el adaptador ni el servicio mientras el formato del proveedor siga siendo el mismo.

## Verificación

`python manage.py migrate` y `python manage.py test`. Hay pruebas de ambos adaptadores, los cuatro planes, la persistencia y la respuesta ante un medio desconocido, además de las cinco pruebas del día 2.
