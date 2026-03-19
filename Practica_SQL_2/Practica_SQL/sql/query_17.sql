-- 17. Cree un reporte que muestre el ID del pedido, el nombre 
-- de la empresa que lo realizó y el nombre y apellidos del empleado asociado. 
-- Mostrar solo los pedidos realizados después del 1 de enero de 2021 que se 
-- enviaron después de su fecha de entrega. Ordenar por nombre de la empresa.
SELECT o.OrderID, 
       c.CompanyName, 
       e.FirstName, 
       e.LastName,
       o.OrderDate
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
JOIN Employees e ON o.EmployeeID = e.EmployeeID
WHERE o.OrderDate > '2021-01-01'
  AND o.ShippedDate > o.RequiredDate
ORDER BY c.CompanyName, o.OrderDate
;
