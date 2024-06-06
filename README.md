# Grupo 9

# Datos del Grupo

- Integrante 1:
  - Nombre: Ana Luz 
  - Apellido: Aguirre
  - DNI: 43.188.563
  - Correo Electrónico: aguirreluzana5f@gmail.com
  - GitHub: https://github.com/AnaAguirre77

- Integrante 2:
  - Nombre: Alan 
  - Apellido: García Pagliardini
  - DNI: 35.917.637
  - Correo Electrónico: alan.gpagliardini@gmail.com
  - GitHub: https://github.com/pagliardini

- Integrante 3:
  - Nombre: Mauricio Leonel
  - Apellido: Molina
  - DNI: 45.699.198
  - Correo Electrónico: mauri.molina1025@gmail.com
  - GitHub: https://github.com/Mauri-Molina

- Integrante 4:
  - Nombre: Fabián 
  - Apellido: Monar
  - DNI: 95.850.539
  - Correo Electrónico: fabian.monar.u@gmail.com
  - GitHub: https://github.com/fabianmonar

- Integrante 5:
  - Nombre: Maciel 
  - Apellido: Barbero
  - DNI: 35.144.709
  - Correo Electrónico: m8barbero@gmail.com
  - GitHub: https://github.com/MacielBarbero


# Descripción de la Propuesta del Proyecto
El proyecto consiste en desarrollar un sistema de control de stock para una tienda de mascotas. Este sistema permitirá gestionar información sobre sucursales, productos, pedidos y proveedores.

Los usuarios podrán acceder al sistema para ver el inventario disponible en cada sucursal, realizar pedidos de productos, mantener actualizada la información de los proveedores y gestionar el stock de productos en las diferentes ubicaciones de la tienda.

El sistema estará diseñado para ser fácil de usar y eficiente, permitiendo una gestión efectiva del inventario y asegurando que los productos estén disponibles cuando los clientes los necesiten.

# Análisis y Diseño del Proyecto
Para diseñar el menú principal y la primera interacción del usuario con el sistema de control de stock para la tienda de mascotas, es importante tener en cuenta varios aspectos. 

1. Facilidad de uso: El menú principal debe ser intuitivo y fácil de entender para que los usuarios puedan navegar por las diferentes opciones sin dificultad.

2. Acceso rápido a las funciones principales: El menú principal debe proporcionar acceso rápido a las funciones más utilizadas, como la gestión de sucursales, productos, pedidos y proveedores.

3. Organización lógica: Las opciones del menú deben estar organizadas de manera lógica y coherente, agrupando funciones relacionadas para facilitar la navegación.

4. Información clara: Cada opción del menú debe estar acompañada de una descripción clara para que los usuarios comprendan qué hace cada función aprimera vista.
   
## Pseudocódigo General
    Mostrar "Menú Principal:"
    Mostrar "1. Gestión de Sucursales"
    Mostrar "2. Gestión de Productos"
    Mostrar "3. Ventas"
    Mostrar "4. Gestión de Proveedores"
    Mostrar "5. Salir"
    
    Leer opción
    
    Si opción es igual a 1:
        // Llamar a la función para gestionar sucursales
        gestionarSucursales()
    
    Si opción es igual a 2:
        // Llamar a la función para gestionar productos
        gestionarProductos()
    
    Si opción es igual a 3:
        // Llamar a la función para realizar un pedido
        realizarPedido()
    
    Si opción es igual a 4:
        // Llamar a la función para gestionar proveedores
        gestionarProveedores()
    
    Si opción es igual a 5:
        Salir del programa
        
# Sistema de Control de Stock

Este es un sistema modularizado para gestionar sucursales, productos, ventas y proveedores.

## Archivos

### main.py

Este archivo contiene el menú principal de la aplicación y las funciones para gestionar las diferentes entidades.

- menu_principal(): Función para mostrar el menú principal y gestionar las diferentes entidades.

### productos.py

Este archivo contiene las funciones para gestionar los productos.

- gestionar_productos(): Función para gestionar los productos.

### sucursales.py

Este archivo contiene las funciones para gestionar las sucursales.

- gestionar_sucursales(): Función para gestionar las sucursales.

### ventas.py

Este archivo contiene las funciones para gestionar las ventas.

- gestionar_ventas(): Función para gestionar las ventas.

### proveedores.py

Este archivo contiene las funciones para gestionar los proveedores.

- **gestionar_proveedores()**: Función para gestionar los proveedores.
