Algoritmo tiendaMascotas
	
	Definir respuesta, respuesta2 Como Entero
	
Escribir "Bienvenido al Sistema de control de Stock! Qu� desea hacer hoy?"
Escribir "OPCION 1: GESTI�N DE SUCURSALES" 
Escribir "OPCI�N 2: GESTI�N DE PRODUCTOS" 
Escribir "OPCI�N 3: VENTAS"
Escribir "OPCI�N 4 GESTI�N DE PROVEEDORES" 
Escribir "OPCI�N 5: SALIR"
Leer respuesta


Si respuesta = 1
	Escribir "Usted se encuentra en: GESTI�N DE SUCURSALES."
	Escribir "Que acci�n desea tomar? 1) AGREGAR UNA SUCURSAL | 2) ELIMINAR UNA SUCURSAL | 3) MOSTRAR SUCURSAL"
	Leer respuesta2
	Si respuesta2 =1 Entonces
		Escribir "A continuaci�n, usted podr� agregar una sucursal."
	FinSi
	Si respuesta2 =2 Entonces
		Escribir "A continuaci�n, usted podr� eliminar una sucursal."
	FinSi
	Si respuesta2 =3 Entonces
		Escribir "A continuaci�n, usted podr� visualizar la sucursal seleccionada."
	FinSi
FinSi

Si respuesta = 2
	Escribir "Usted se encuentra en: GESTI�N DE PRODUCTOS."
	Escribir "Que acci�n desea tomar? 1) AGREGAR UN PRODUCTO | 2) ELIMINAR UN PRODUCTO | 3) MOSTRAR PRODUCTO"
	Leer respuesta2
	Si respuesta2 =1 Entonces
		Escribir "A continuaci�n, usted podr� agregar un producto."
	FinSi
	Si respuesta2 =2 Entonces
		Escribir "A continuaci�n, usted podr� eliminar un producto."
	FinSi
	Si respuesta2 =3 Entonces
		Escribir "A continuaci�n, usted podr� leer informaci�n sobre el producto seleccionado."
	FinSi
FinSi

Si respuesta = 3	
	Escribir "Usted se encuentra en: VENTAS."
	Escribir "Que acci�n desea tomar? 1) CONSULTAR HISTORIAL | 2) CONSULTAR CANTIDAD VENDIDA"
	Leer respuesta2
	Si respuesta2 =1 Entonces
		Escribir "A continuaci�n, usted podr� leer el historial de ventas."
	FinSi
	Si respuesta2 =2 Entonces
		Escribir "A continuaci�n, usted podr� consultar la cantidad vendida del producto a seleccionar."
	FinSi
FinSi

Si respuesta = 4	
	Escribir "Usted se encuentra en GESTI�N DE PROVEEDORES"
	Escribir "Que acci�n desea tomar? 1) AGREGAR PROVEEDOR | 2) ELIMINAR PROVEEDOR | 3) MOSTRAR INFORMACION DE PROVEEDOR"
	Leer respuesta2
	Si respuesta2 =1 Entonces
		Escribir "A continuaci�n, usted podr� agregar un proveedor."
	FinSi
	Si respuesta2 =2 Entonces
		Escribir "A continuaci�n, usted podr� eliminar un proveedor."
	FinSi
	Si respuesta2 =3 Entonces
		Escribir "A continuaci�n, usted podr� leer informaci�n sobre el proveedor seleccionado."
	FinSi
FinSi

Si respuesta = 5	
    Escribir "Hasta luego!"
FinSi
	
FinAlgoritmo
