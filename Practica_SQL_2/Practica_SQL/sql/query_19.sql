-- 19. Cree un informe que muestre el ID del Proveedor, el Nombre de la Empresa, 
-- el Nombre de la Categoría, el Nombre del Producto y el Precio Unitario de las
-- tablas de productos, proveedores y categorías.
SELECT p.ProductID, 
       s.CompanyName AS SupplierCompanyName, 
       c.CategoryName, 
       p.ProductName, 
       p.UnitPrice
FROM Products p
JOIN Suppliers s ON p.SupplierID = s.SupplierID
JOIN Categories c ON p.CategoryID = c.CategoryID
ORDER BY p.ProductID
;