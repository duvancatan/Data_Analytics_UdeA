--0. Consultas de ensayo en clase
--SELECT OrderID, 
--       OrderDate, 
--       ShippedDate, 
--       CustomerID, 
--       Freight
--FROM Orders
--WHERE OrderDate >= '1997-01-01' AND OrderDate < '1998-01-01'
--ORDER BY Freight DESC
--;

SELECT MIN(OrderDate) AS MinOrderDate, 
       MAX(OrderDate) AS MaxOrderDate
       FROM Orders
;