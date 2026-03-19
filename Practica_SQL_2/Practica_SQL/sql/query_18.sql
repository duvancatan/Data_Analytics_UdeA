-- 18. Cree un informe que muestre la cantidad total de productos pedidos 
-- (de la tabla Order_Details). Mostrar solo los registros de productos con una 
-- cantidad inferior a 200. El informe debe mostrar las siguientes 5 filas.
SELECT ProductID, 
       SUM(Quantity) AS TotalQuantityOrdered
FROM [Order Details]
GROUP BY ProductID
HAVING SUM(Quantity) > 200000
ORDER BY TotalQuantityOrdered DESC
--LIMIT 5
;