proveedores = []

def gestionar_proveedores():
    while True:
        print("Gestionando Proveedores")
        print("1. Mostrar Proveedores")
        print("2. Añadir Proveedor")
        print("3. Eliminar Proveedor")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_proveedores()
        elif opcion == "2":
            añadir_proveedor()
        elif opcion == "3":
            eliminar_proveedor()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_proveedores():
    print("Proveedores:")
    for proveedor in proveedores:
        print(proveedor)

def añadir_proveedor():
    nombre = input("Ingrese el nombre del proveedor: ")
    contacto = input("Ingrese el contacto del proveedor: ")
    nuevo_proveedor = {"nombre": nombre, "contacto": contacto}
    proveedores.append(nuevo_proveedor)
    print("Proveedor añadido correctamente.")

def eliminar_proveedor():
    nombre = input("Ingrese el nombre del proveedor a eliminar: ")
    for proveedor in proveedores:
        if proveedor["nombre"] == nombre:
            proveedores.remove(proveedor)
            print("Proveedor eliminado correctamente.")
            break
    else:
        print("No se encontró el proveedor.")
