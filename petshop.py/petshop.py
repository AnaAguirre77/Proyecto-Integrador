# Definición de las entidades como diccionarios y listas

sucursales = []
productos = []
proveedores = []
ventas = []

# Función para mostrar el menú principal y gestionar las entidades

def menu_principal():
    while True:
        print("Bienvenido al Sistema de Control de Stock")
        print("1. Gestionar Sucursales")
        print("2. Gestionar Productos")
        print("3. Gestionar ventas")
        print("4. Gestionar Proveedores")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            gestionar_sucursales()
        elif opcion == "2":
            gestionar_productos()
        elif opcion == "3":
            gestionar_ventas()
        elif opcion == "4":
            gestionar_proveedores()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Funciones para gestionar cada entidad

def gestionar_sucursales():
    while True:
        print("Gestionando Sucursales")
        print("1. Mostrar Sucursales")
        print("2. Añadir Sucursal")
        print("3. Eliminar Sucursal")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_sucursales()
        elif opcion == "2":
            añadir_sucursal()
        elif opcion == "3":
            eliminar_sucursal()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_sucursales():
    print("Sucursales:")
    for sucursal in sucursales:
        print(sucursal)

def añadir_sucursal():
    nombre = input("Ingrese el nombre de la sucursal: ")
    ubicacion = input("Ingrese la ubicación de la sucursal: ")
    nueva_sucursal = {"nombre": nombre, "ubicacion": ubicacion}
    sucursales.append(nueva_sucursal)
    print("Sucursal añadida correctamente.")

def eliminar_sucursal():
    nombre = input("Ingrese el nombre de la sucursal a eliminar: ")
    for sucursal in sucursales:
        if sucursal["nombre"] == nombre:
            sucursales.remove(sucursal)
            print("Sucursal eliminada correctamente.")
            break
    else:
        print("No se encontró la sucursal.")

def gestionar_ventas():
    print("Funcionalidad de Gestionar Ventas aún no implementada.")
    # Lógica para gestionar venta

def gestionar_productos():
    print("Funcionalidad de Gestionar Productos aún no implementada.")
    # Lógica para gestionar productos

def gestionar_proveedores():
    print("Funcionalidad de Gestionar Proveedores aún no implementada.")
    # Lógica para gestionar proveedores

# Llama a la función principal del menú
menu_principal()
