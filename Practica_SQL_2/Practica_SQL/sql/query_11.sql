-- 11. Si el costo del flete (freight) es mayor o igual a $500.00, ahora tributará con el 10%. 
-- Cree un informe que muestre la identificación del pedido, el costo del flete, el costo del 
-- flete con este impuesto para todos los pedidos de $500 o más.
SELECT OrderID, 
       Freight, 
       Freight * 1.10 AS FreightWithTax
FROM Orders
WHERE Freight >= 500.00
;