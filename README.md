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

Link al video explicativo: https://drive.google.com/file/d/1GcTWInS-2dWCQBCxQppY_-5iO0bLm2wu/view?usp=sharing

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

## Uso de la aplicación

Nuestra aplicación de tienda de mascotas ofrece varias funcionalidades para gestionar diferentes aspectos del negocio.  se describen las principales funciones y los archivos asociados:

1. Menú Principal (index.py):
La función `menu_principal()` en el archivo `index.py` muestra el menú principal de la aplicación y permite gestionar las diferentes entidades, como productos, sucursales, ventas, proveedores, detalle de ventas y categorías de productos.

2. Gestión de Productos (productos.py):
La función `gestionar_productos()` en el archivo `productos.py` permite añadir, modificar, eliminar y visualizar información sobre los productos disponibles en la tienda.

3. Gestión de Sucursales (sucursales.py):
 La función `gestionar_sucursales()` en el archivo `sucursales.py` facilita la administración de las sucursales de la tienda, incluyendo la gestión de su información y ubicación.

4. Gestión de Ventas (ventas.py):
La función `gestionar_ventas()` en el archivo `ventas.py` permite registrar nuevas ventas, así como gestionar y visualizar el historial de ventas realizadas en la tienda.

5. Gestión de Proveedores (proveedores.py):
La función `gestionar_proveedores()` en el archivo `proveedores.py` ofrece herramientas para gestionar los proveedores de la tienda, incluyendo la adición, edición y eliminación de información de contacto y productos suministrados.

6. Gestión del Detalle de Ventas (detalle_ventas.py):
La función `gestionar_detalle_ventas()` en el archivo `detalle_ventas.py` permite administrar el detalle de las ventas registradas, incluyendo la visualización de los productos vendidos y la cantidad asociada a cada venta.

7. Gestión de Categorías de Productos (categorias_productos.py):
 La función `gestionar_categorias()` en el archivo `categorias_productos.py` proporciona herramientas para gestionar las categorías de los productos vendidos en la tienda, incluyendo la creación, modificación y eliminación de categorías.

        
# Sistema de Control de Stock

Este es un sistema modularizado para gestionar sucursales, productos, ventas, proveedores, detalle de ventas y categorías de productos.

## Archivos

### index.py

Este archivo contiene el menú principal de la aplicación y las funcionalidades para gestionar las diferentes entidades.
Es el punto de entrada principal para el sistema de control de stock. Su objetivo es proporcionar un menú interactivo que permite al usuario seleccionar diferentes opciones para gestionar sucursales, productos, ventas, proveedores, detalles de ventas y categorías de productos.

**menu_principal()**: Función para mostrar el menú principal y gestionar las diferentes entidades.
La función menu_principal() presenta un menú interactivo al usuario, donde se muestran varias opciones, y luego ejecuta la función correspondiente según la opción seleccionada por el usuario. Si el usuario elige la opción "7", el programa se cierra con un mensaje de despedida. Dirige las acciones del usuario a las funciones adecuadas para llevar a cabo la gestión.

### productos.py

Este archivo contiene las funciones para gestionar los productos.

**`gestionar_productos()`**: Esta función es el punto de entrada para gestionar los productos. Muestra un menú de opciones que incluye mostrar productos, añadir un producto, eliminar un producto y volver al menú principal.

**`mostrar_productos()`**: Esta función ejecuta una consulta SQL para seleccionar todos los productos de la tabla `Productos` en la base de datos. Luego imprime los detalles de cada producto en la consola.

**`añadir_producto()`**: Esta función permite al usuario ingresar los detalles de un nuevo producto, como el código de barras, nombre, precio unitario, etc. Luego ejecuta una consulta SQL para insertar estos detalles en la tabla `Productos`.

**`eliminar_producto()`**: Esta función solicita al usuario el código de barras del producto que desea eliminar. Luego ejecuta una consulta SQL para eliminar el producto correspondiente de la tabla `Productos`.

**`if __name__ == "__main__":`**: Esta línea garantiza que el script se ejecute únicamente si es ejecutado directamente y no si es importado como un módulo en otro script. En este caso, llama a la función `gestionar_productos()` para comenzar la gestión de productos.

### sucursales.py

Este archivo contiene las funciones para gestionar las sucursales.

**`gestionar_sucursales()`**: Esta función presenta un menú de opciones para gestionar las sucursales. Las opciones incluyen ver sucursales, agregar una nueva sucursal, actualizar una sucursal existente, eliminar una sucursal y volver al menú principal.

**`ver_sucursales()`**: Esta función ejecuta una consulta SQL para seleccionar todas las sucursales de la tabla `Sucursales` en la base de datos. Luego imprime los detalles de cada sucursal en la consola.

**`agregar_sucursal()`**: Permite al usuario ingresar los detalles de una nueva sucursal, como el ID, ciudad, dirección, teléfono y correo electrónico. Luego ejecuta una consulta SQL para insertar estos detalles en la tabla `Sucursales`.

**`actualizar_sucursal()`**: Esta función permite al usuario actualizar los detalles de una sucursal existente. Solicita el ID de la sucursal que se desea actualizar, así como los nuevos valores para ciudad, dirección, teléfono y correo electrónico. Luego ejecuta una consulta SQL para actualizar los detalles de la sucursal en la tabla `Sucursales`.

**`eliminar_sucursal()`**: Solicita al usuario el ID de la sucursal que se desea eliminar y ejecuta una consulta SQL para eliminar esa sucursal de la tabla `Sucursales`.

### ventas.py

Este archivo contiene las funciones para gestionar las ventas.

**`gestionar_ventas()`**: Esta función presenta un menú de opciones para gestionar las ventas. Las opciones incluyen mostrar ventas, añadir una nueva venta, eliminar una venta y volver al menú principal.

**`mostrar_ventas()`**: Esta función imprime en consola todas las ventas almacenadas en la lista `ventas`.

**`añadir_venta()`**: Permite al usuario ingresar los detalles de una nueva venta, como el ID del producto, ID de la sucursal, cantidad vendida, fecha y monto de la venta. Luego agrega estos detalles como un diccionario a la lista `ventas`.

**`eliminar_venta()`**: Solicita al usuario el ID de la venta que desea eliminar. Luego busca esa venta en la lista `ventas` y la elimina si la encuentra.

### proveedores.py

Este archivo contiene las funciones para gestionar los proveedores.

**`gestionar_proveedores()`**: Esta función presenta un menú de opciones para gestionar proveedores que incluye mostrar proveedores, añadir un proveedor, eliminar un proveedor y volver al menú principal.

**`mostrar_proveedores()`**: Esta función ejecuta una consulta SQL para seleccionar los proveedores de la tabla `Proveedores` en la base de datos. Luego imprime los detalles de cada proveedor en la consola.

**`añadir_proveedor()`**: Esta función permite al usuario ingresar los detalles de un nuevo proveedor, como el CUIT, nombre, apellido y teléfono. Luego ejecuta una consulta SQL para insertar estos detalles en la tabla `Proveedores`. Se incluye un manejo de excepciones para capturar errores de MySQL.

**`eliminar_proveedor()`**: Esta función solicita al usuario el CUIT del proveedor que desea eliminar. Primero verifica si el proveedor existe en la base de datos. Si existe, ejecuta una consulta SQL para eliminar el proveedor correspondiente de la tabla `Proveedores`. También se incluye un manejo de excepciones para capturar errores de MySQL.

### detalle_ventas.py

Este archivo contiene las funciones para gestionar el detalle de las ventas.

**`gestionar_detalle_ventas()`**: Esta función presenta un menú interactivo para gestionar el detalle de ventas. Permite al usuario elegir entre mostrar los detalles de ventas existentes, añadir un nuevo detalle de venta, eliminar un detalle de venta o volver al menú principal.

**`mostrar_detalle_ventas()`**: Esta función imprime todos los detalles de ventas almacenados en la lista `detalle_ventas`.

**`añadir_detalle_venta()`**: Esta función solicita al usuario ingresar información sobre un nuevo detalle de venta, como el ID de la venta, la cantidad de unidades, el precio unitario, el descuento, el total y el código de barras del producto. Luego, crea un diccionario con esta información y lo añade a la lista `detalle_ventas`.

**`eliminar_detalle_venta()`**: Esta función solicita al usuario ingresar el ID del detalle de venta que desea eliminar. Luego, busca este detalle de venta en la lista `detalle_ventas` y lo elimina si se encuentra.

La lista `detalle_ventas` actúa como una especie de "base de datos temporal" donde se almacenan los detalles de ventas. Sin embargo, ten en cuenta que esta implementación no persistirá los datos entre ejecuciones del programa; es decir, los detalles de ventas se perderán cuando el programa se cierre. Si deseas que los datos se conserven entre ejecuciones, necesitarás implementar algún tipo de almacenamiento persistente, como una base de datos.

### categorias_productos.py

Este archivo contiene las funciones que gestiona las categorías de los productos. Estas funciones permiten al usuario gestionar las categorías de productos de manera interactiva a través del menú principal del sistema de control de stock.

**`gestionar_categorias()`**: Esta función presenta un menú interactivo para gestionar las categorías de productos. Permite al usuario elegir entre mostrar las categorías existentes, añadir una nueva categoría, eliminar una categoría o volver al menú principal.

**`mostrar_categorias()`**: Esta función ejecuta una consulta SQL para seleccionar todas las categorías de productos de la base de datos y luego imprime los detalles de cada categoría, incluyendo su ID, nombre y descripción.

**`añadir_categoria()`**: Esta función solicita al usuario que ingrese el nombre y la descripción de la nueva categoría y luego ejecuta una consulta SQL para insertar la nueva categoría en la base de datos.

**`eliminar_categoria()`**: Esta función solicita al usuario que ingrese el ID de la categoría que desea eliminar. Primero verifica si la categoría existe en la base de datos. Si existe, ejecuta una consulta SQL para eliminar la categoría correspondiente.

**gestionar_categorias()**: Función para gestionar las categorías de los productos.

### db.py
Este archivo proporciona funciones para conectarse a una base de datos MySQL, ejecutar consultas SQL y recuperar resultados de consultas. Estas funciones son útiles para interactuar con una base de datos MySQL en el contexto de la aplicación de control de stock, permitiendo ejecutar consultas y recuperar datos de manera fácil y segura.

**`config_bd()`**: Esta función intenta leer la configuración de la base de datos desde un archivo JSON. Si el archivo no se encuentra o está mal formateado, se muestra un mensaje de error y la función devuelve `None`. En caso contrario, devuelve el diccionario de configuración.

**`crear_conexion()`**: Esta función utiliza la configuración de la base de datos obtenida de `config_bd()` para establecer una conexión con la base de datos MySQL. Si la conexión se establece correctamente, devuelve el objeto de conexión; de lo contrario, devuelve `None`.

**`execute_query(query, params=None)`**: Esta función ejecuta una consulta SQL proporcionada como argumento `query`. También puede tomar parámetros opcionales `params` para consultas parametrizadas. Utiliza la función `create_connection()` para establecer una conexión con la base de datos y ejecuta la consulta. Si la ejecución es exitosa, confirma los cambios en la base de datos y muestra un mensaje de éxito; de lo contrario, muestra un mensaje de error.

**`fetch_query(query, params=None)`**: Esta función ejecuta una consulta SQL proporcionada como argumento `query` y devuelve todos los resultados. También puede tomar parámetros opcionales `params` para consultas parametrizadas. Utiliza la función `create_connection()` para establecer una conexión con la base de datos, ejecuta la consulta y devuelve los resultados. Si la ejecución es exitosa, devuelve los resultados; de lo contrario, devuelve `None`.


## Contenido del Repositorio

### `index.py`
Este archivo actúa como punto de entrada de la aplicación. Contiene la función `menu_principal()` que muestra el menú principal de la aplicación, permitiendo la navegación hacia la gestión de productos, sucursales, ventas, proveedores, detalles de ventas y categorías de productos.

### `productos.py`
Gestiona la funcionalidad relacionada con los productos:
- **`gestionar_productos()`**: Muestra un menú para la gestión de productos.
- **`mostrar_productos()`**: Ejecuta una consulta SQL para mostrar todos los productos.
- **`añadir_producto()`**: Permite añadir un nuevo producto a la base de datos.
- **`eliminar_producto()`**: Permite eliminar un producto existente usando su código de barras.

### `sucursales.py`
Gestiona la funcionalidad relacionada con las sucursales:
- **`gestionar_sucursales()`**: Muestra un menú para la gestión de sucursales.
- **`ver_sucursales()`**: Ejecuta una consulta SQL para mostrar todas las sucursales.
- **`agregar_sucursal()`**: Permite añadir una nueva sucursal.
- **`actualizar_sucursal()`**: Actualiza los detalles de una sucursal existente.
- **`eliminar_sucursal()`**: Permite eliminar una sucursal usando su ID.

### `ventas.py`
Gestiona la funcionalidad relacionada con las ventas:
- **`gestionar_ventas()`**: Muestra un menú para la gestión de ventas.
- **`mostrar_ventas()`**: Muestra todas las ventas registradas en la lista.
- **`añadir_venta()`**: Permite añadir una nueva venta a la lista de ventas.
- **`eliminar_venta()`**: Permite eliminar una venta usando su ID.

### `proveedores.py`
Gestiona la funcionalidad relacionada con los proveedores:
- **`gestionar_proveedores()`**: Muestra un menú para la gestión de proveedores.
- **`mostrar_proveedores()`**: Ejecuta una consulta SQL para mostrar todos los proveedores.
- **`añadir_proveedor()`**: Permite añadir un nuevo proveedor a la base de datos.
- **`eliminar_proveedor()`**: Permite eliminar un proveedor usando su CUIT.

### `detalle_ventas.py`
Gestiona el detalle de las ventas:
- **`gestionar_detalle_ventas()`**: Muestra un menú para la gestión del detalle de ventas.
- **`mostrar_detalle_ventas()`**: Muestra todos los detalles de ventas registrados en la lista.
- **`añadir_detalle_venta()`**: Permite añadir un nuevo detalle de venta a la lista de detalles.
- **`eliminar_detalle_venta()`**: Permite eliminar un detalle de venta usando su ID.

### `categorias_productos.py`
Gestiona la funcionalidad relacionada con las categorías de productos:
- **`gestionar_categorias()`**: Muestra un menú para la gestión de categorías de productos.
- **`mostrar_categorias()`**: Ejecuta una consulta SQL para mostrar todas las categorías de productos.
- **`añadir_categoria()`**: Permite añadir una nueva categoría a la base de datos.
- **`eliminar_categoria()`**: Permite eliminar una categoría usando su ID.

### `db.py`
Proporciona funciones para la interacción con la base de datos MySQL:
- **`config_bd()`**: Lee la configuración de la base de datos desde un archivo JSON.
- **`create_connection()`**: Establece una conexión con la base de datos MySQL usando la configuración proporcionada.
- **`execute_query(query, params=None)`**: Ejecuta una consulta SQL en la base de datos.
- **`fetch_query(query, params=None)`**: Ejecuta una consulta SQL y devuelve los resultados.



## Estructura de Archivos

Evidencia 3
├── index.py
├── productos.py
├── proveedores.py
├── sucursales.py
├── ventas.py
├── detalle_ventas.py
└── categorias_productos.py

# Requisitos

Python 3.7+
pip

# Instalación

1. Clona el repositorio: [https://github.com/AnaAguirre77/Proyecto-Integrador.git]

> git clone 
> cd petshop

2. Crea y activa un entorno virtual:

> python -m venv venv
> source venv/bin/activate   # En Windows usa `venv\Scripts\activate`

3. Instala las dependencias:

> pip install -r requirements.txt

4. Configura la base de datos:

Asegurate de tener un servidor de base de datos MySQL funcionamiento, se recomienda la version 8.0.
Crea la base de datos y las tablas utilizando el script SQL proporcionado (sql_SCRIPT.sql).

5. Ejecuta el script para insertar ejemplos de datos:

> python insertar_ejemplos.py

6. Ejecuta la aplicación:

> python index.py

