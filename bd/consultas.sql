USE petshop;

SELECT * FROM sucursales;

SELECT Telefono AS `Teléfono`, Email AS `Correo Electrónico`
FROM sucursales;

SELECT * FROM clientes WHERE Apellido LIKE "%e%";

SELECT * FROM productos
WHERE `Precio_Unitario` BETWEEN 5.0 AND 15.0;

SELECT * FROM productos WHERE Stock > 100 LIMIT 4;

SELECT Pr.Nombre Producto, Cat.Nombre AS `Categoría`
FROM Productos Pr
INNER JOIN Categoria Cat 
ON Pr.ID_Categoria = Cat.ID_Categoria;

SELECT Pr.Nombre Producto, Cat.Nombre AS `Categoría`
FROM Productos Pr
INNER JOIN Categoria Cat 
ON Pr.ID_Categoria = Cat.ID_Categoria
WHERE Pr.Nombre LIKE "%perros%";

