-- 8. Cree un informe que muestre el título de cortesía y el nombre
-- y apellido de todos los empleados cuyo título de cortesía comienza con "M".
SELECT TitleOfCourtesy, 
       FirstName, 
       LastName
FROM Employees
WHERE TitleOfCourtesy LIKE 'M%'
;