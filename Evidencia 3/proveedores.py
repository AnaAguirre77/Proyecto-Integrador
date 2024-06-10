from db import execute_query, fetch_query

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
    query = "SELECT CUIT_Proveedor, Nombre, Apellido, Telefono FROM Proveedores"
    proveedores = fetch_query(query)
    print("Proveedores:")
    for proveedor in proveedores:
        print(f"CUIT: {proveedor[0]}, Nombre: {proveedor[1]}, Apellido: {proveedor[2]}, Teléfono: {proveedor[3]}")

def añadir_proveedor():
    cuit_proveedor = input("Ingrese el CUIT del proveedor: ")
    nombre = input("Ingrese el nombre del proveedor: ")
    apellido = input("Ingrese el apellido del proveedor: ")
    telefono = input("Ingrese el teléfono del proveedor: ")
    
    query = """
    INSERT INTO Proveedores (CUIT_Proveedor, Nombre, Apellido, Telefono)
    VALUES (%s, %s, %s, %s)
    """
    params = (cuit_proveedor, nombre, apellido, telefono)
    
    try:
        execute_query(query, params)
        print("Proveedor añadido correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al añadir proveedor: {err}")

def eliminar_proveedor():
    cuit_proveedor = input("Ingrese el CUIT del proveedor a eliminar: ")
    
    # Verificar si el proveedor existe
    query_check = "SELECT COUNT(*) FROM Proveedores WHERE CUIT_Proveedor = %s"
    params_check = (cuit_proveedor,)
    proveedor_existe = fetch_query(query_check, params_check)[0][0]

    if proveedor_existe == 0:
        print("Error: El proveedor con el CUIT especificado no existe.")
        return
    
    query = "DELETE FROM Proveedores WHERE CUIT_Proveedor = %s"
    params = (cuit_proveedor,)
    
    try:
        execute_query(query, params)
        print("Proveedor eliminado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar proveedor: {err}")
