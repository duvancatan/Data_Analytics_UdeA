-- 10. Cree un informe que muestre el nombre de la empresa, el título del contacto, 
-- la ciudad y el país de todos clientes en México o en cualquier ciudad de España excepto Madrid.
SELECT CompanyName, 
       ContactTitle, 
       City, 
       Country
FROM Customers
WHERE Country = 'Mexico'
   OR (Country = 'Spain' AND City <> 'Madrid')    
;  
   