
# Investigación de Lenguajes de Programación y Frameworks

**José Antonio Medina Ayala**

----------

## ¿Qué es un paradigma de programación?

> Un paradigma de programación es una forma general de organizar y desarrollar un programa. Define cómo se plantean los problemas y cómo se construyen sus soluciones.

## ¿Qué es un patrón de diseño?

> Un patrón de diseño es una solución conocida y reutilizable para resolver un problema que aparece frecuentemente durante el desarrollo de software.

Es importante mencionar que los lenguajes de programación no tienen un único patrón de diseño oficial. Sin embargo, algunos patrones son más comunes o más fáciles de implementar en determinados lenguajes debido a sus características.

----------

## Lenguajes de Programación

### 1. Python

-   **Paradigma principal:** Es un lenguaje multiparadigma, ya que permite trabajar con programación orientada a objetos, imperativa y funcional.
    
-   **Patrón de diseño común:** **Decorador**. Permite agregar o modificar el comportamiento de una función o clase sin cambiar directamente su código original. Python facilita su uso mediante el símbolo `@`.
    

### 2. JavaScript

-   **Paradigma principal:** Es multiparadigma, pues permite utilizar programación basada en prototipos, funcional e imperativa.
    
-   **Patrón de diseño común:** **Observer (Observador)**. Permite que diferentes elementos reaccionen cuando ocurre un evento o cambio. Un ejemplo de su uso son los métodos para escuchar eventos, como `addEventListener`.
    

### 3. Java

-   **Paradigma principal:** Está principalmente orientado a objetos y utiliza clases para organizar la información y el comportamiento de los programas.
    
-   **Patrón de diseño común:** **Factory Method (Método Fábrica)**. Se utiliza para crear objetos sin tener que especificar directamente todos los detalles de su creación.
    

### 4. C#

-   **Paradigma principal:** Es multiparadigma, con soporte para programación orientada a objetos, funcional y basada en componentes.
    
-   **Patrón de diseño común:** **Observer (Observador)**. C# facilita su implementación mediante eventos y delegados, permitiendo que diferentes componentes reciban avisos cuando sucede algo importante.
    

### 5. Rust

-   **Paradigma principal:** Es multiparadigma, con características de programación funcional, imperativa y concurrente.
    
-   **Patrón característico:** **RAII**. Este patrón permite administrar automáticamente recursos como la memoria. Cuando una variable deja de utilizarse o sale de su área de ejecución, los recursos que ocupaba se liberan.
    

### 6. TypeScript

-   **Paradigma principal:** Es multiparadigma y se basa en JavaScript, pero agrega tipos y herramientas que ayudan a organizar proyectos grandes.
    
-   **Patrón de diseño común:** **Facade (Fachada)**. Consiste en proporcionar una forma sencilla de acceder a un sistema complejo, ocultando detalles que el usuario o programador no necesita conocer.
    

### 7. Go (Golang)

-   **Paradigma principal:** Es principalmente imperativo y concurrente. Utiliza estructuras sencillas y composición en lugar de herencia tradicional.
    
-   **Patrón común de concurrencia:** **Worker Pool**. Permite repartir varias tareas entre un grupo de trabajadores que las procesan de manera simultánea. Go facilita este tipo de funcionamiento mediante las `goroutines`.
    

### 8. C++

-   **Paradigma principal:** Es multiparadigma, ya que permite programación orientada a objetos, genérica e imperativa.
    
-   **Patrón característico:** **RAII**. Relaciona el uso de un recurso con la vida de un objeto. Cuando el objeto deja de existir, el recurso se libera automáticamente.
    

### 9. PHP

-   **Paradigma principal:** Es multiparadigma, con soporte para programación orientada a objetos, funcional e imperativa. Se utiliza principalmente en el desarrollo web.
    
-   **Práctica común:** **Dependency Injection (Inyección de Dependencias)**. Consiste en proporcionar a una clase los elementos que necesita desde el exterior, evitando que tenga que crearlos por sí misma. Esto facilita la organización y modificación de los programas.
    

### 10. Kotlin

-   **Paradigma principal:** Es multiparadigma y combina programación orientada a objetos con programación funcional.
    
-   **Patrón de diseño común:** **Singleton**. Se utiliza cuando se necesita que exista una sola instancia de una clase en todo el programa. Kotlin facilita su implementación mediante la palabra reservada `object`.
    

### 11. Swift

-   **Paradigma principal:** Utiliza programación orientada a protocolos, funcional y orientada a objetos.
    
-   **Patrón de diseño común:** **Delegate (Delegado)**. Permite que un objeto encargue a otro la realización de ciertas acciones o la administración de determinada información. Es muy utilizado en el desarrollo de aplicaciones para dispositivos Apple.
    

### 12. Ruby

-   **Paradigma principal:** Está principalmente orientado a objetos, ya que prácticamente todos sus elementos se manejan como objetos. También incluye características de programación funcional.
    
-   **Patrón de diseño común:** **Iterator (Iterador)**. Permite recorrer los elementos de una colección sin necesidad de conocer cómo está organizada internamente. Algunos ejemplos son `each` y `map`.
    

### 13. Scala

-   **Paradigma principal:** Es multiparadigma y combina la programación funcional con la programación orientada a objetos.
    
-   **Patrón de diseño común:** **Strategy (Estrategia)**. Permite tener diferentes formas de realizar una tarea y elegir la más adecuada según la situación, sin cambiar el resto del programa.
    

### 14. Dart

-   **Paradigma principal:** Está principalmente orientado a objetos y utiliza clases para organizar los programas. También permite el uso de mixins para reutilizar funciones.
    
-   **Patrón de diseño común:** **Builder (Constructor)**. Permite crear objetos complejos paso a paso. Es utilizado con frecuencia junto con Flutter para construir interfaces mediante diferentes elementos o widgets.
    

### 15. R

-   **Paradigma principal:** Combina principalmente la programación funcional y declarativa. Está enfocado en el análisis estadístico, las matemáticas y la ciencia de datos.
    
-   **Patrón común:** **Pipeline (Tubería)**. Consiste en realizar una serie de transformaciones en orden, donde el resultado de una operación se utiliza como entrada para la siguiente.
    

----------

## Frameworks de Desarrollo

Un framework es un conjunto de herramientas y reglas que facilita la creación de aplicaciones. A diferencia de un lenguaje de programación, un framework proporciona una estructura previamente organizada para desarrollar un proyecto.

### 16. Spring Boot (Java)

-   **Forma de trabajo:** Se basa principalmente en programación orientada a objetos y permite separar funciones importantes del programa.
    
-   **Patrón característico:** **Inversion of Control (Inversión de Control)** mediante **Dependency Injection (Inyección de Dependencias)**. Spring Boot se encarga de crear y administrar muchos de los componentes que necesita una aplicación, evitando que el programador tenga que hacerlo manualmente.
    

### 17. Angular (TypeScript)

-   **Forma de trabajo:** Utiliza componentes y programación reactiva para construir aplicaciones web.
    
-   **Patrón característico:** **Observer (Observador)**. Angular puede reaccionar a cambios en la información y actualizar los componentes necesarios. Para ello utiliza herramientas como RxJS y sus observables.
    

### 18. Django (Python)

-   **Forma de trabajo:** Utiliza principalmente programación orientada a objetos e imperativa.
    
-   **Patrón arquitectónico:** **MTV (Model-Template-View)**. Separa una aplicación en tres partes:
    
    -   **Modelo:** administra la información y la base de datos.
      -   **Plantilla:** muestra la información al usuario. 
    -   **Vista:** procesa las solicitudes y contiene la lógica de la aplicación.
        

Este modelo es una variante del patrón MVC.

### 19. React (JavaScript)

-   **Forma de trabajo:** Utiliza un enfoque declarativo y basado en componentes para crear interfaces.
    
-   **Patrón característico:** **Flujo de datos unidireccional**. La información normalmente pasa de los componentes principales a los componentes secundarios mediante propiedades llamadas `props`.
    

React también permite combinar componentes pequeños para construir interfaces más grandes y organizadas.

### 20. Laravel (PHP)

-   **Forma de trabajo:** Se basa principalmente en programación orientada a objetos.
    
-   **Patrones característicos:** **MVC** y **Active Record**. MVC divide la aplicación en modelos, vistas y controladores. Por otra parte, Active Record permite representar las tablas de una base de datos mediante clases y objetos.
    

Laravel utiliza estas características por medio de Eloquent, su herramienta para trabajar con bases de datos.

----------


