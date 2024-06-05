# Importar las funciones de los otros archivos
from sucursales import gestionar_sucursales
from productos import gestionar_productos
from proveedores import gestionar_proveedores
from ventas import gestionar_ventas

# Función para mostrar el menú principal y gestionar las entidades
def menu_principal():
    while True:
        print("Bienvenido al Sistema de Control de Stock")
        print("1. Gestionar Sucursales")
        print("2. Gestionar Productos")
        print("3. Gestionar Ventas")
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

# Llama a la función principal del menú
menu_principal()
