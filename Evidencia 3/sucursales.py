sucursales = []

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
