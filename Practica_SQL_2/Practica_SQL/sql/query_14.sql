-- 14. Encuentre la cantidad de representantes de ventas en cada ciudad que 
-- contiene al menos 2 ventas representantivas. Ordenar por número de empleados.
SELECT City, 
       COUNT(*) AS SalesRepCount
FROM Employees
WHERE Title = 'Sales Representative'
    GROUP BY City
    HAVING COUNT(*) >= 2
    ORDER BY SalesRepCount DESC
;