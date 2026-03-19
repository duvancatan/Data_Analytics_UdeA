-- 20. Cree un informe que muestre el ID del Cliente y la suma del Flete 
-- de la tabla de pedidos, con la suma del flete mayor a $200, agrupados 
-- por ID del Cliente.

SELECT CustomerID, 
       SUM(Freight) AS TotalFreight
FROM Orders
GROUP BY CustomerID
HAVING SUM(Freight) > 200;          