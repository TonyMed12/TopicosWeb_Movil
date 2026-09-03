## Problema de patrones de software

#### El problema
Una universidad pública mantiene el alta de materias, el pago de inscripción, las constancias y las becas en  **decenas de páginas sueltas**  (PHP, ASP clásico y un par de servicios nuevos). Se requiere un  **portal web único**  para el siguiente ciclo.

El estado actual, documentado por control escolar y por caja, es el siguiente.

1.  Cada trámite es un archivo distinto. En todos se copia el mismo bloque de «¿hay sesión?», el mismo registro en bitácora y el mismo encabezado HTML. Cuando cambia la regla de caducidad de la sesión, hay que tocar cuarenta archivos; siempre se olvida uno.
2.  El pago de inscripción admite  **tarjeta, transferencia SPEI y referencia de ventanilla**. El script de  `pagar.php`  es un  `switch`  de doscientas líneas. Cada banco nuevo obliga a editar ese archivo. El protocolo de un banco habla de «créditos» y códigos  `00/01`; el reglamento interno habla de «pago de inscripción» y estados  `pendiente / acreditado / rechazado`.
3.  La plantilla del kardex ejecuta consultas SQL para armar la tabla de calificaciones. Los reportes de constancias duplican esas consultas con otro formato.
4.  Cuando el pago se acredita, el mismo script llama a control escolar (alta de materias), dispara un correo al estudiante y avisa a caja. Si el correo falla, a veces no se registra el alta. Si el estudiante pulsa dos veces «pagar» porque la página tarda, se han cobrado  **dos**  cargos.
5.  La  **aplicación móvil**  de la universidad y el  **kiosco**  de la biblioteca deben mostrar el mismo trámite. La app pide un JSON mínimo (folio, saldo, plazo). El kiosco pide una página HTML con el escudo y la tabla de vencimientos. Hoy el equipo de la app hace  **doce peticiones**  para pintar la pantalla de inicio.
6.  El servicio de un banco y el de un validador de CURP externo  **se caen**  con frecuencia. Mientras no responden, el estudiante ve la rueda de espera y no puede ni consultar el kardex, que no depende de esos colaboradores.
7.  Un proveedor propone, para la descarga de una constancia en PDF, Event Sourcing, CQRS, una malla de microservicios y un almacén global Redux en el navegador. El trámite de la constancia es: autenticar, consultar un registro ya existente y generar un archivo.

El portal nuevo puede construirse en Spring, en Laravel o en Express: el análisis de patrones  **no**  espera un marco concreto. Sí espera que se use lo que el marco ya instancia (enrutador, middleware, transacción del ORM) y que no se copie un diagrama UML al lado.**

---
### Misión 1 — El portal no es un patrón

| Problema identificado | Capa | Patrón o patrones | ¿Por qué ese y no el vecino? | ¿Cuándo no aplicaría? |
|---|---|---|---|---|
| La comprobación de sesión y la bitácora están copiadas en decenas de archivos, por lo que cualquier cambio debe repetirse manualmente. | Políticas transversales | Front Controller + Middleware / Chain of Responsibility | Front Controller concentra la entrada de las peticiones y el middleware aplica sesión y bitácora en una cadena común. No es Strategy, porque no se están intercambiando algoritmos para realizar una misma operación. | No se debe programar un Front Controller o una cadena GoF desde cero si Spring, Laravel o Express ya proporcionan enrutador, filtros o middleware. Tampoco hace falta en una aplicación mínima con una sola ruta. |
| El pago se resuelve mediante un `switch` de 200 líneas para tarjeta, SPEI y referencia de ventanilla. | Aplicación / dominio | Strategy + Factory | Strategy encapsula cada forma de pago bajo un mismo contrato, mientras Factory selecciona la estrategia adecuada. No es State, porque el pago no cambia automáticamente su comportamiento según su estado; el usuario o la petición eligen el medio. | No conviene crear varias estrategias y una fábrica si solo existe un método de pago estable y no se espera que cambie. |
| El banco utiliza conceptos como “créditos” y códigos `00/01`, distintos de “pago de inscripción” y `pendiente/acreditado/rechazado`. | Integración | Adapter, posiblemente como Anti-Corruption Layer | Adapter traduce la interfaz y el vocabulario externo al modelo que entiende la universidad. No es Facade: Facade simplifica un subsistema, mientras Adapter convierte un contrato ajeno en el contrato esperado. | No hace falta si la universidad controla ambos contratos y puede hacer que utilicen directamente los mismos nombres, tipos y estados. |
| La plantilla del kardex ejecuta SQL y las constancias duplican las mismas consultas para presentar los datos con otro formato. | Presentación + datos | Repository + Template View o Transform View | Repository concentra las consultas requeridas por el dominio; las vistas reciben datos ya preparados y solamente generan HTML o PDF. No basta con MVC como etiqueta general, porque el problema concreto es que la vista conoce la persistencia. | No conviene crear un Repository enorme con decenas de métodos CRUD sin una necesidad real. Tampoco se necesita una plantilla compleja si solo se devuelve una respuesta mínima sin formato. |
| La acreditación del pago, el alta de materias y el registro deben quedar consistentes, mientras que el correo y el aviso a caja son reacciones posteriores que no deberían impedir el alta. | Datos + aplicación/dominio | Unit of Work + Observer; Transactional Outbox si los avisos son externos | Unit of Work confirma o revierte juntas las escrituras indispensables, como pago y alta. Observer desacopla las reacciones posteriores, como correo y aviso a caja. Observer no sustituye a Unit of Work: publicar un evento no garantiza por sí mismo que las escrituras queden atómicas. | Unit of Work no hace falta para una única escritura independiente. Observer no conviene cuando solo existe un receptor o cuando todas las operaciones deben completarse atómicamente en la misma transacción. |
| La aplicación móvil y el kiosco necesitan representaciones diferentes, y actualmente la app realiza doce peticiones para construir una pantalla. | Presentación / integración de API | BFF (Backend for Frontend) | Un BFF ofrece una respuesta adaptada y agregada para cada tipo de cliente: JSON mínimo para la app y HTML completo para el kiosco. No es Adapter, porque el problema no es traducir el protocolo de un proveedor ajeno; tampoco es Factory, porque no se están creando objetos. | No aplicaría si solo existe un cliente o si una misma API ya entrega a todos una representación adecuada sin múltiples peticiones. |


## Misión 2 — Una petición, varios patrones

### Caso de uso: pagar la inscripción

Cuando el estudiante pulsa el botón "Pagar", la petición atraviesa distintas estructuras. Cada una resuelve una responsabilidad específica; por lo tanto, el portal no utiliza un solo patrón, sino una composición de patrones.

| Orden | Estructura o mecanismo | Patrón | Responsabilidad |
|---:|---|---|---|
| 1 | Borde de entrada, si existen varios servicios | API Gateway | Recibe `POST /pagos`, aplica políticas del borde y dirige la petición a la aplicación. Puede omitirse si el portal es un monolito pequeño. |
| 2 | Enrutador de Spring, Laravel o Express | Front Controller | Recibe las peticiones y determina qué ruta o controlador debe atenderlas. Se utiliza el mecanismo incluido en el framework, sin programar otro Front Controller. |
| 3 | Middleware de autenticación | Chain of Responsibility | Comprueba que el estudiante tenga una sesión válida. Si no está autenticado, detiene la cadena antes de ejecutar el pago. |
| 4 | Middleware de bitácora | Chain of Responsibility / Decorator | Registra el usuario, la fecha, la ruta y el resultado sin copiar el mismo código en cada trámite. |
| 5 | Controlador de pagos | Controller | Recibe y valida los datos básicos, como folio, importe y medio de pago. Después delega el caso de uso y no ejecuta directamente el reglamento ni consultas SQL. |
| 6 | Servicio `registrarPago` | Service Layer / Facade | Coordina el caso de uso: comprobar la inscripción, ejecutar el cobro, registrar el resultado y ordenar el alta de materias. |
| 7 | Selector del medio de pago | Factory | Selecciona la implementación correspondiente a tarjeta, SPEI o referencia de ventanilla sin colocar un `switch` extenso en el controlador. |
| 8 | Implementación del medio de pago | Strategy | Encapsula las distintas formas de pagar bajo un mismo contrato. Permite agregar otro medio sin modificar el servicio principal. |
| 9 | Traductor del servicio bancario | Adapter | Convierte términos como “créditos” y códigos `00/01` a “pago de inscripción” y estados `pendiente`, `acreditado` o `rechazado`. |
| 10 | Control de solicitudes repetidas | Idempotencia | Utiliza una clave única para impedir que dos pulsaciones del botón produzcan dos cargos. La segunda petición recupera el resultado de la primera. |
| 11 | Repositorios de pagos e inscripciones | Repository | Permiten consultar y guardar pagos, inscripciones y materias sin colocar SQL en el controlador, el servicio o las vistas. |
| 12 | Transacción del ORM o framework | Unit of Work | Confirma juntos el pago acreditado y el alta de materias, o revierte ambos. Evita dejar un cargo registrado sin el alta correspondiente. |
| 13 | Evento `PagoAcreditado` | Observer / Publicación-suscripción | Informa a varios interesados después de confirmar el pago. El correo al estudiante y el aviso a caja reaccionan al evento sin estar acoplados al servicio de pago. |
| 14 | Bandeja de salida transaccional | Transactional Outbox | Registra el evento junto con la transacción principal para enviarlo posteriormente. Así, una falla del correo no cancela ni pierde el alta de materias. |
| 15 | Generador de la respuesta | Transform View / Serialización | Construye la respuesta final, por ejemplo un JSON con folio y estado, utilizando datos ya preparados y sin ejecutar SQL desde la vista. |

### Recorrido de la petición

1. El estudiante envía `POST /pagos`.
2. El **API Gateway**, si es necesario, recibe y dirige la petición.
3. El **Front Controller** del framework identifica la ruta.
4. El middleware comprueba la sesión.
5. El middleware registra la petición en la bitácora.
6. El controlador valida los datos recibidos.
7. El **Service Layer** ejecuta el caso de uso `registrarPago`.
8. La **Factory** selecciona el medio de pago.
9. La **Strategy** correspondiente realiza la operación.
10. El **Adapter** traduce el protocolo del banco.
11. La clave de **idempotencia** evita un cargo repetido.
12. Los **Repositories** consultan y guardan la información.
13. La **Unit of Work** confirma conjuntamente el pago y el alta de materias.
14. Se genera el evento `PagoAcreditado`.
15. Los observadores envían el correo y notifican a caja.
16. Finalmente, se genera la respuesta HTTP.

### Esquema

~~~text
POST /pagos
    ↓
API Gateway, si es necesario
    ↓
Front Controller del framework
    ↓
Middleware de sesión
    ↓
Middleware de bitácora
    ↓
Controlador de pagos
    ↓
Service Layer: registrarPago
    ↓
Factory selecciona el medio
    ↓
Strategy ejecuta la forma de pago
    ↓
Adapter traduce el protocolo bancario
    ↓
Control de idempotencia
    ↓
Repository + Unit of Work
    ↓
Pago e inscripción confirmados
    ↓
Evento PagoAcreditado
    ↓
Observer + Transactional Outbox
    ↓
Correo al estudiante y aviso a caja
    ↓
Respuesta HTTP
~~~

