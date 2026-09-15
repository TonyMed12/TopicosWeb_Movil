# Análisis de las implementaciones de entregas

> - José Antonio Medina Ayala
> - Cesar Enrique Díaz Maldonado
> - Paulo Cesar Pérez Martínez
> - Enrique Martínez
> - Adrian Martínez Ortíz
---

La **implementación 1** aplica una arquitectura orientada a objetos con los patrones Adapter, Factory Method y Strategy. Esto separa las integraciones externas, la creación de medios de entrega y las reglas de planeación.

La **implementación 2** es un ejemplo intencional de mala práctica: concentra todo el flujo en un único método, duplica reglas y depende directamente de detalles de cada proveedor.


## Flujo de la implementación 1

```text
Proveedor externo
      |
      v
Adapter -> Sugerencia -> Factory Method -> Strategy -> Plan de entrega
```

1. Un proveedor devuelve una recomendación con su formato propio (JSON o XML).
2. Un adaptador transforma ese formato a  `Sugerencia`, el contrato del dominio.
3. La logística correspondiente crea el medio de entrega adecuado.
4. El medio ejecuta su estrategia de planeación y produce un `Plan`.

## Patrones de diseño de la implementación 1

### Adapter

Los adaptadores `AdaptadorOpenAI` y `AdaptadorXml` implementan `RecomendadorIA`. Cada uno traduce la respuesta específica de su proveedor a `Sugerencia(medio, motivo)`.

- OpenAI usa campos como `route_hint`, `score` y `why`.
- El proveedor XML usa el atributo `vehicle` y una nota.
- El dominio no necesita conocer JSON, XML ni los nombres técnicos externos.

Beneficio: se puede agregar otro proveedor creando un adaptador nuevo, sin cambiar el proceso de registrar pedidos.

### Factory Method

`Logistica` declara el método fábrica `crear_medio()`. Sus subclases deciden qué objeto concreto crear:

- `LogisticaAerea` crea `EntregaDron`.
- `LogisticaCorta` crea `EntregaBicicleta`.
- `LogisticaUrbana` crea `EntregaMotocicleta`.
- `LogisticaTerrestre` crea `EntregaCamioneta`.

El método `despachar()` trabaja con la abstracción `MedioDeEntrega`, sin depender de una clase de transporte concreta.

### Strategy

`MedioDeEntrega` define la operación común `planear(pedido, contexto)`. Cada vehículo encapsula su propia estrategia:

- Bicicleta: paquetes pequeños y recorridos cortos.
- Motocicleta: paquetes medianos, tráfico y urgencia.
- Camioneta: carga amplia y costo que depende del peso.
- Dron: límites de peso y distancia; no opera con lluvia.

Beneficio: las reglas de un vehículo se modifican sin afectar las reglas de los otros.

## Características y prácticas de la implementación 1

- Está disponible en Python y Java con la misma organización.
- Define objetos de dominio: `Pedido`, `ContextoViaje`, `Sugerencia` y `Plan`.
- Separa dominio, integración externa, creación de objetos, reglas de negocio y presentación.
- Depende de abstracciones: `RegistrarPedido` recibe `RecomendadorIA`, no un proveedor concreto.
- Facilita pruebas unitarias: se pueden probar adaptadores, medios y el registro de pedidos de forma aislada.
|


## Análisis de la implementación 2

La implementación 2 no aplica un patrón de diseño formal. Centraliza el flujo completo en `registrar_pedido` (Python) o `registrarPedido` (Java):

```text
datos primitivos -> proveedor -> formato externo -> vehículo -> reglas -> impresión
```

### Prácticas problemáticas

#### Método demasiado grande (God Function)

El mismo método recibe los datos, simula al proveedor, interpreta la respuesta, elige el vehículo, calcula el plan e imprime el resultado. Esto viola el principio de responsabilidad única.

#### Código duplicado

Las reglas de dron, bicicleta, motocicleta y camioneta se repiten en los bloques de OpenAI y XML. Un cambio en tarifas o restricciones debe replicarse en más de un lugar y puede producir inconsistencias.

#### Condicionales extensos

La selección de proveedor, vehículo y cálculo se hace mediante cadenas de `if/elif/else` o `if/else if`. Agregar un proveedor o medio aumenta el tamaño y complejidad del método central.

#### Acoplamiento fuerte

La lógica de negocio conoce campos externos como `route_hint`, cadenas XML y valores específicos como `"drone"` o `"van"`. Un cambio de formato externo obliga a modificar el flujo principal.

#### Parametros primitivos

El pedido se pasa como muchos parámetros primitivos: origen, destino, peso, distancia, urgencia, tráfico, lluvia y proveedor. Además, los límites, tarifas y nombres técnicos están dispersos como números y cadenas literales.

#### Procesamiento XML frágil

La variante Java busca texto usando `contains`; la variante Python compara fragmentos de cadena. Esto puede fallar si cambia el formato del XML aunque conserve su significado.

#### Manejo de errores insuficiente

Para proveedores o medios desconocidos se imprime un mensaje y el programa continúa. Esto puede producir un plan incompleto o inválido, en lugar de detener el flujo con un error controlado.

## Patrones ausentes en la implementación 2

- No hay **Adapter**: JSON y XML entran directamente a la lógica de negocio.
- No hay **Strategy**: las reglas de cada vehículo viven en condicionales, no en objetos intercambiables.
- No hay **Factory Method**: no existe una abstracción responsable de crear medios de entrega.

La selección mediante condicionales no es, por sí misma, un patrón de diseño adecuado para este dominio si se espera que crezca.

La implementación 1 aplica correctamente Adapter, Factory Method y Strategy como solución didáctica. Reduce acoplamiento y duplicación, mejora la legibilidad y facilita evolución y pruebas.

La implementación 2 solo es razonable como prototipo pequeño o contraste académico. Para un sistema mantenible debe refactorizarse hacia contratos, objetos de dominio, adaptadores y estrategias independientes.
