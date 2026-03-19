-- 7. Cree un informe que muestre el precio unitario promedio redondeado 
-- al siguiente número entero, el precio total de las unidades en stock y 
-- el número máximo de pedidos de la tabla de productos. Todos estos datos 
-- se guardan como PrecioPromedio, StockTotal y PedidoMáximo, respectivamente.
SELECT AVG(UnitPrice) AS PrecioMedio,
       CEILING(AVG(UnitPrice)) AS PrecioPromedio, 
       SUM(UnitsInStock) AS StockTotal, 
       MAX(UnitsOnOrder) AS PedidoMáximo
FROM Products
;   
