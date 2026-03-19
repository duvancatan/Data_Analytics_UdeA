-- 16. Cree un reporte que muestre los pedidos de los empleados.
SELECT o.OrderID, 
       o.OrderDate, 
       e.FirstName, 
       e.LastName
FROM Orders o
JOIN Employees e 
ON o.EmployeeID = e.EmployeeID
ORDER BY o.OrderDate
;