from db import execute_query, fetch_query

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
    query = "SELECT * FROM Productos"
    productos = fetch_query(query)
    print("\nLista de Productos:")
    for producto in productos:
        print(f"Código de Barras: {producto[0]}, Nombre: {producto[1]}, Precio Unitario: {producto[2]}, Stock: {producto[3]}, ID Categoría: {producto[4]}, Descripción: {producto[5]}, CUIT Proveedor: {producto[6]}")
    print()

def añadir_producto():
    codigo_de_barras = input("Ingrese el código de barras del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio_unitario = input("Ingrese el precio unitario del producto: ")
    stock = input("Ingrese el stock del producto: ")
    id_categoria = input("Ingrese el ID de la categoría del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    cuit_proveedor = input("Ingrese el CUIT del proveedor del producto: ")

    query = """
    INSERT INTO Productos (Codigo_de_barras, Nombre, Precio_Unitario, Stock, ID_Categoria, Descripcion, CUIT_Proveedor)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    params = (codigo_de_barras, nombre, precio_unitario, stock, id_categoria, descripcion, cuit_proveedor)
    execute_query(query, params)
    print("Producto añadido con éxito.\n")

def eliminar_producto():
    codigo_de_barras = input("Ingrese el código de barras del producto a eliminar: ")
    query = "DELETE FROM Productos WHERE Codigo_de_barras = %s"
    params = (codigo_de_barras,)
    execute_query(query, params)
    print("Producto eliminado con éxito.\n")

if __name__ == "__main__":
    gestionar_productos()
