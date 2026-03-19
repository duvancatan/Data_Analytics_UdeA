-- 13. Recuperar el número de empleados en cada ciudad.
SELECT City, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY City
;