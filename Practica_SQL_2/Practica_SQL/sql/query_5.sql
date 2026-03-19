-- 5. Cree un informe que muestre el título, el nombre y apellido 
-- de todos los Representantes de Ventas.
SELECT Title, 
       FirstName, 
       LastName
FROM Employees
--WHERE Title = 'Sales Representative'
WHERE Title LIKE '%Sales%'
ORDER BY LastName
;