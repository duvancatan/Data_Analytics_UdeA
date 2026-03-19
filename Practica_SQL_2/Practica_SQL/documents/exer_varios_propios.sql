--Consultar todos los campos de la tabla "employees" del esquema "public"--
select *
from public.employees
;

--Consultar los valores del campo "city" de la tabla "employees" del esquema "public"--
select city
from public.employees
;

--Consultar los distintos valores del campo "city" de la tabla "employees" del esquema "public"--
select distinct city
from public.employees}
;

-- Verificar si hay repetidos en el campo "product_name" de la tabla "public.products"
select product_name, count(*)
from public.products
group by 1
having count(*)>1
;

-- Hacer un conteo por países, en el campo "country" y ordenarlos descendente
select country, count(*)
from public.suppliers
group by country
order by 2
;

-- Seleccionar los registros cuyo país es Mexico y/o Alemania
select * from public.customers
where country = 'Mexico' or country = 'Germany'
--where country = 'Mexico' and country = 'Germany'
;

-- Seleccionar los registros con condiciones en unit_price y quantity
select order_id, count(*)
from public.order_details
where unit_price >= 10 and quantity <=20
group by 1
;

-- Seleccionar los registros con condiciones en unit_price
select * from public.order_details
where unit_price between 10 and 20
;

-- Seleccionar los registros donde se omite Argentina
select * from public.customers
where not country = 'Argentina'
;



---------------------------------------
---- USO DE JOINs EN LAS CONSULTAS ----
---------------------------------------

-- Cruce de proveedores y productos con llave "id"
select t1.*, t2.*
from public.suppliers as t1
join public.products as t2
on t1.supplier_id = t2.product_id
;

--Cruce izquierdo de "order_details" con "orders"
select t1.*, t2.order_date, t2.freight, t2.ship_city, t2.ship_region
from public.order_details as t1
left join public.orders as t2
on t1.order_id = t2.order_id
where substring(t2.order_date)=1996