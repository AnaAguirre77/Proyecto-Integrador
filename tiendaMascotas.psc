Algoritmo tiendaMascotas
	
	Definir respuesta, respuesta2 Como Entero
	
Escribir "Bienvenido al Sistema de control de Stock! Qué desea hacer hoy?"
Escribir "OPCION 1: GESTIÓN DE SUCURSALES" 
Escribir "OPCIÓN 2: GESTIÓN DE PRODUCTOS" 
Escribir "OPCIÓN 3: VENTAS"
Escribir "OPCIÓN 4 GESTIÓN DE PROVEEDORES" 
Escribir "OPCIÓN 5: SALIR"
Leer respuesta


Si respuesta = 1
	Escribir "Usted se encuentra en: GESTIÓN DE SUCURSALES."
	Escribir "Que acción desea tomar? 1) AGREGAR UNA SUCURSAL | 2) ELIMINAR UNA SUCURSAL | 3) MOSTRAR SUCURSAL"
	Leer respuesta2
	Si respuesta2 =1 Entonces
		Escribir "A continuación, usted podrá agregar una sucursal."
	FinSi
	Si respuesta2 =2 Entonces
		Escribir "A continuación, usted podrá eliminar una sucursal."
	FinSi
	Si respuesta2 =3 Entonces
		Escribir "A continuación, usted podrá visualizar la sucursal seleccionada."
	FinSi
FinSi

Si respuesta = 2
	Escribir "Usted se encuentra en: GESTIÓN DE PRODUCTOS."
	Escribir "Que acción desea tomar? 1) AGREGAR UN PRODUCTO | 2) ELIMINAR UN PRODUCTO | 3) MOSTRAR PRODUCTO"
	Leer respuesta2
	Si respuesta2 =1 Entonces
		Escribir "A continuación, usted podrá agregar un producto."
	FinSi
	Si respuesta2 =2 Entonces
		Escribir "A continuación, usted podrá eliminar un producto."
	FinSi
	Si respuesta2 =3 Entonces
		Escribir "A continuación, usted podrá leer información sobre el producto seleccionado."
	FinSi
FinSi

Si respuesta = 3	
	Escribir "Usted se encuentra en: VENTAS."
	Escribir "Que acción desea tomar? 1) CONSULTAR HISTORIAL | 2) CONSULTAR CANTIDAD VENDIDA"
	Leer respuesta2
	Si respuesta2 =1 Entonces
		Escribir "A continuación, usted podrá leer el historial de ventas."
	FinSi
	Si respuesta2 =2 Entonces
		Escribir "A continuación, usted podrá consultar la cantidad vendida del producto a seleccionar."
	FinSi
FinSi

Si respuesta = 4	
	Escribir "Usted se encuentra en GESTIÓN DE PROVEEDORES"
	Escribir "Que acción desea tomar? 1) AGREGAR PROVEEDOR | 2) ELIMINAR PROVEEDOR | 3) MOSTRAR INFORMACION DE PROVEEDOR"
	Leer respuesta2
	Si respuesta2 =1 Entonces
		Escribir "A continuación, usted podrá agregar un proveedor."
	FinSi
	Si respuesta2 =2 Entonces
		Escribir "A continuación, usted podrá eliminar un proveedor."
	FinSi
	Si respuesta2 =3 Entonces
		Escribir "A continuación, usted podrá leer información sobre el proveedor seleccionado."
	FinSi
FinSi

Si respuesta = 5	
    Escribir "Hasta luego!"
FinSi
	
FinAlgoritmo
