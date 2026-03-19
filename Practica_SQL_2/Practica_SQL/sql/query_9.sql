-- 9. Cree un informe que muestre el nombre y apellido de todos los 
-- representantes de ventas que son de Seattle o Redmond.
SELECT FirstName, 
       LastName
FROM Employees
WHERE City IN ('Seattle', 'Redmond')
;