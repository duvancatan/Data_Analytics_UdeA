--1.Recupere todas las columnas de la tabla Región.
select * from public.region
;
select region_id, 
       region_description
from public.region
;

--2.Seleccione las columnas Nombre y Apellido de la tabla Empleados (Employees).
select first_name,
	   last_name
from public.employees
;

--3. Seleccione las columnas Nombre y Apellido de la tabla Empleados (Employees). Ordenar por Apellido.
select first_name,
	   last_name
from public.employees
order by last_name asc
;

select first_name,
	   last_name
from public.employees
order by last_name desc
;

select first_name,
	   last_name
from public.employees
order by 2 desc
;

--4. Cree un informe que muestre los pedidos (Orders) de Northwind ordenados por flete (Freight), desde el 
--más caro hasta el más barato. Muestra OrderID, OrderDate, ShippedDate, CustomerID y Freight.
select order_id,
       order_date,
	   shipped_date, 
	   freight
from public.orders
order by freight desc
;

select order_id,
       order_date,
	   shipped_date, 
	   freight
from public.orders
order by 4 desc
;

--5.Cree un informe que muestre el título y el nombre y apellido de todas las ventas representantivas.
select distinct title
from public.employees
;

select title,
       first_name,
       last_name
from public.employees
where title='Sales Representative'
;

-- Hacer un conteo por title
select title,
       count(*) as total
from public.employees
group by 1
having count(*)>1
;

--6. Cree un informe que muestre los nombres y apellidos de todos los empleados 
--   que tienen una región especificada.
select distinct region
from public.employees
;

select first_name,
       last_name
from public.employees
where region Is Not Null
;

--8. Cree un informe que muestre el título de cortesía y el nombre y apellido de todos los empleados 
--   cuyo título de cortesía comienza con "M".
select distinct title_of_courtesy
from public.employees
;

select first_name,
       last_name
from public.employees
where title_of_courtesy ilike 'M%'
;

--9.Cree un informe que muestre el nombre y apellido de todos los representantes de ventas 
--  que son de Seattle o Redmond.
select distinct city, region
from public.employees
;

select first_name,
       last_name
from public.employees
where city='Seattle' or city='Redmond'
; 

select first_name,
       last_name
from public.employees
where city in ('Seattle' , 'Redmond')
;

--10. Cree un informe que muestre el nombre de la empresa, el título del contacto, la ciudad
--    y el país de todos clientes en México o en cualquier ciudad de España excepto Madrid.
select distinct country
from public.customers
order by 1
;

select company_name,
       contact_title,
	   city,
	   country
from public.customers
where country in ('Mexico', 'Spain') and city != 'Madrid'
;

--11.Si el costo del flete (freight) es mayor o igual a $500.00, ahora tributará con el 10%. 
--   Cree un informe que muestre la identificación del pedido, el costo del flete, el costo del flete 
--   con este impuesto para todos los pedidos de $500 o más.
select *
from public.orders limit 10
;

select order_id,
       freight,
	   freight+0.10*freight as total
from public.orders
where freight>=500
;
--¿Qué pasa si quiero agregar la tasa como un campo adicional?

--12. Encuentre el número total de unidades solicitadas del Product ID 3
select product_id
from public.order_details
;

select count(t1.order_id) as cantidad
from orders as t1
inner join order_details as t2 
on t1.order_id = t2.order_id
where t2.product_id = 3
;

--13.Crucemos las tablas "Suppliers" con "Products" mediante la clave especificada y mostrar cómo 
--   se seleccionan todos los campos y unos específicos.

select distinct supplier_id 
from public.suppliers 
order by supplier_id asc
;

select distinct product_id
from public.products
order by product_id asc
;

select t1.*, t2.*
from public.suppliers as t1
inner join public.products as t2
on t1.supplier_id = t2.product_id
;


--14. Empleando la Cla
select birth_date as fecha 
from public.employees 
;

with 
fecha as (
select employee_id, birth_date 
from public.employees 
where birth_date <= '1952-02-19'
)
select t2.employee_id,
       t1.first_name, 
       t1.last_name, 
	   t1.title,
	   t2.birth_date
from fecha as t2
inner join public.employees as t1
on t1.employee_id = t2.employee_id
;



	   

