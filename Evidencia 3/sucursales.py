from db import execute_query, fetch_query

def gestionar_sucursales():
    while True:
        print("\nGestionar Sucursales")
        print("1. Ver Sucursales")
        print("2. Agregar Sucursal")
        print("3. Actualizar Sucursal")
        print("4. Eliminar Sucursal")
        print("5. Volver al Menú Principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ver_sucursales()
        elif opcion == "2":
            agregar_sucursal()
        elif opcion == "3":
            actualizar_sucursal()
        elif opcion == "4":
            eliminar_sucursal()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def ver_sucursales():
    query = "SELECT * FROM Sucursales"
    results = fetch_query(query)
    for row in results:
        print(row)

def agregar_sucursal():
    id_sucursal = input("Ingrese el ID de la Sucursal: ")
    ciudad = input("Ingrese la Ciudad: ")
    direccion = input("Ingrese la Dirección: ")
    telefono = input("Ingrese el Teléfono: ")
    email = input("Ingrese el Email: ")

    query = """
    INSERT INTO Sucursales (ID_Sucursal, Ciudad, Direccion, Telefono, Email)
    VALUES (%s, %s, %s, %s, %s)
    """
    params = (id_sucursal, ciudad, direccion, telefono, email)
    execute_query(query, params)

def actualizar_sucursal():
    id_sucursal = input("Ingrese el ID de la Sucursal a actualizar: ")
    ciudad = input("Ingrese la nueva Ciudad: ")
    direccion = input("Ingrese la nueva Dirección: ")
    telefono = input("Ingrese el nuevo Teléfono: ")
    email = input("Ingrese el nuevo Email: ")

    query = """
    UPDATE Sucursales
    SET Ciudad = %s, Direccion = %s, Telefono = %s, Email = %s
    WHERE ID_Sucursal = %s
    """
    params = (ciudad, direccion, telefono, email, id_sucursal)
    execute_query(query, params)

def eliminar_sucursal():
    id_sucursal = input("Ingrese el ID de la Sucursal a eliminar: ")

    query = "DELETE FROM Sucursales WHERE ID_Sucursal = %s"
    params = (id_sucursal,)
    execute_query(query, params)
