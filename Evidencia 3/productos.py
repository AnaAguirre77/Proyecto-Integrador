productos = []

def gestionar_productos():
    while True:
        print("Gestionando Productos")
        print("1. Mostrar Productos")
        print("2. Añadir Producto")
        print("3. Eliminar Producto")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            añadir_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_productos():
    print("Productos:")
    for producto in productos:
        print(producto)

def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    id_sucursal = input("Ingrese el ID de la sucursal: ")
    id_proveedor = input("Ingrese el ID del proveedor: ")
    categoria = input("Ingrese la categoría del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    codigo_barras = input("Ingrese el código de barras del producto: ")
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "id_sucursal": id_sucursal,
        "id_proveedor": id_proveedor,
        "categoria": categoria,
        "descripcion": descripcion,
        "codigo_barras": codigo_barras
    }
    productos.append(nuevo_producto)
    print("Producto añadido correctamente.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)
            print("Producto eliminado correctamente.")
            break
    else:
        print("No se encontró el producto.")
