-- 12. Encuentre el número total de unidades solicitadas del Product ID 3.
SELECT SUM(Quantity) AS TotalUnitsOrdered
FROM [Order Details]
WHERE ProductID = 3
;