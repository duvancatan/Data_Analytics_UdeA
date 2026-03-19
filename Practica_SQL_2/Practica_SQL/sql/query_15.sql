-- 15. Encuentre las empresas (el CompanyName) que realizaron pedidos en 2020.
SELECT DISTINCT c.CompanyName
FROM Customers c
JOIN Orders o 
ON c.CustomerID = o.CustomerID    
WHERE STRFTIME('%Y', OrderDate) = CAST('2020' AS INT)
;  

--SELECT MIN(STRFTIME('%Y', OrderDate)) AS MinOrderYear, 
--       MAX(STRFTIME('%Y', OrderDate)) AS MaxOrderYear
--    FROM Orders
--;

--SELECT DATETIME('now')
--;

--SELECT DATETIME('now', 'localtime');

--SELECT * FROM Orders
--WHERE OrderDate BETWEEN '2020-01-01' AND '2020-12-31'
--ORDER BY OrderDate
--LIMIT 5
--;
