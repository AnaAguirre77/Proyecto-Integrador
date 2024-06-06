categorias = []

def gestionar_categorias():
    while True:
        print("Gestionando Categorías de Productos")
        print("1. Mostrar Categorías")
        print("2. Añadir Categoría")
        print("3. Eliminar Categoría")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_categorias()
        elif opcion == "2":
            añadir_categoria()
        elif opcion == "3":
            eliminar_categoria()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_categorias():
    print("Categorías:")
    for categoria in categorias:
        print(categoria)

def añadir_categoria():
    nombre = input("Ingrese el nombre de la categoría: ")
    descripcion = input("Ingrese la descripción de la categoría: ")
    productos_categoria = []
    while True:
        añadir_producto_categoria = input("¿Desea añadir un producto a esta categoría? (s/n): ")
        if añadir_producto_categoria.lower() == 's':
            nombre_producto = input("Ingrese el nombre del producto: ")
            descripcion_producto = input("Ingrese la descripción del producto: ")
            producto = {"nombre": nombre_producto, "descripcion": descripcion_producto}
            productos_categoria.append(producto)
        else:
            break
    nueva_categoria = {"nombre": nombre, "descripcion": descripcion, "productos": productos_categoria}
    categorias.append(nueva_categoria)
    print("Categoría añadida correctamente.")

def eliminar_categoria():
    nombre = input("Ingrese el nombre de la categoría a eliminar: ")
    for categoria in categorias:
        if categoria["nombre"] == nombre:
            categorias.remove(categoria)
            print("Categoría eliminada correctamente.")
            break
    else:
        print("No se encontró la categoría.")
