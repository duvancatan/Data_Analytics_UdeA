-- 6. Cree un informe que muestre los nombres y apellidos de todos los empleados 
-- que tienen una región especificada.
SELECT E.FirstName, 
       E.LastName
FROM Employees AS E
       JOIN Regions AS R
ON E.EmployeeID = R.RegionID  
WHERE R.RegionID IS NOT NULL
;