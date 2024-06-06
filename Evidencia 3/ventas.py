ventas = []

def gestionar_ventas():
    while True:
        print("Gestionando Ventas")
        print("1. Mostrar Ventas")
        print("2. Añadir Venta")
        print("3. Eliminar Venta")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            añadir_venta()
        elif opcion == "3":
            eliminar_venta()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_ventas():
    print("Ventas:")
    for venta in ventas:
        print(venta)

def añadir_venta():
    id_producto = input("Ingrese el ID del producto: ")
    id_sucursal = input("Ingrese el ID de la sucursal: ")
    cantidad = int(input("Ingrese la cantidad vendida: "))
    fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
    monto = float(input("Ingrese el monto de la venta: "))
    nueva_venta = {"id_producto": id_producto, "id_sucursal": id_sucursal, "cantidad": cantidad, "fecha": fecha, "monto": monto}
    ventas.append(nueva_venta)
    print("Venta añadida correctamente.")

def eliminar_venta():
    id_venta = input("Ingrese el ID de la venta a eliminar: ")
    for venta in ventas:
        if venta.get("id_venta") == id_venta:
            ventas.remove(venta)
            print("Venta eliminada correctamente.")
            break
    else:
        print("No se encontró la venta.")
