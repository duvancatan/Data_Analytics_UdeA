-- 4. Cree un informe que muestre los pedidos (Orders) de Northwind
-- ordenados por flete (Freight), desde el más caro hasta el más 
-- barato. Muestra OrderID, OrderDate, ShippedDate, CustomerID y Freight.
SELECT OrderID, 
       OrderDate, 
       ShippedDate, 
       CustomerID, 
       Freight
FROM Orders
ORDER BY Freight DESC
;