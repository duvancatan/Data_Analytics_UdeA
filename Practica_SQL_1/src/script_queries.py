# ============================================================ #
# Libretas de Python para consultar la base de datos en SQLite #
# ============================================================ #
import pandas as pd
import sqlite3
from pathlib import Path

# ================================== #
# Conexión a la base de datos SQLite #
# ================================== #
bd = sqlite3.connect("database/inmuebles.db")


# ============================================================ #
# 1. ¿Cuántas propiedades hay registradas en la base de datos? #
# ============================================================ #
query_1 = """SELECT COUNT(*) AS total 
           FROM inmuebles_raw"""

# ================================================================================================= #           
# 2. ¿Cuál es el precio máximo y mínimo de venta registrado? Remueva los símbolos de moneda y comas #
# ================================================================================================= #
query_2 = """SELECT 
    MIN(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)) AS precio_minimo,
    MAX(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)) AS precio_maximo
FROM inmuebles_raw;"""

# ========================================= #
# 3. ¿Cuántas propiedades son de cada tipo? #
# ========================================= #
query_3 = """SELECT Tipo,
                    COUNT(*) AS cantidad
             FROM inmuebles_raw
               GROUP BY Tipo
               ORDER BY cantidad ASC;
           """


# ========================================================= #
# 4. ¿Cuál es la superficie promedio por tipo de propiedad? #
# ========================================================= #
query_4 = """SELECT Tipo,
                    ROUND(AVG(Superficie), 2) AS superficie_promedio,
                    COUNT(*) AS numero_propiedades
             FROM inmuebles_raw
                GROUP BY 1
                ORDER BY superficie_promedio DESC;"""


# ========================================================================================= #
# 5. ¿Qué vendedor ha vendido más propiedades y cuál es el precio promedio que ha manejado? #
# ========================================================================================= #
query_5 = """SELECT Vendedor,
                    COUNT(*) AS total_ventas,
                    ROUND(AVG(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)), 2) AS precio_promedio
            FROM inmuebles_raw
                GROUP BY Vendedor
                ORDER BY total_ventas DESC;"""


# ================================================================ #
# 6. ¿Cuál es el promedio de días para vender agrupado por ciudad? #
# ================================================================ #
query_6 = """SELECT Ciudad,
                    ROUND(AVG("Días para Vender"), 2) AS dias_promedio,
                    MIN("Días para Vender") AS dias_minimo,
                    MAX("Días para Vender") AS dias_maximo,
                    COUNT(*) AS total_operaciones
            FROM inmuebles_raw
                GROUP BY Ciudad
                ORDER BY dias_promedio DESC;"""


# ======================================================================================================== #
# 7. ¿Cuáles son las ciudades con mayor ingresos totales por ventas? (Considera solo operaciones de Venta) #
# ======================================================================================================== #
query_7 = """SELECT Ciudad,
                    SUM(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)) AS ingresos_totales,
                    COUNT(*) AS numero_propiedades,
                    ROUND(AVG(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)), 2) AS precio_promedio
            FROM inmuebles_raw
            WHERE Operación = 'Venta'
                GROUP BY Ciudad
                ORDER BY ingresos_totales DESC;"""


# ================================================================ #
# 8. ¿Quién es el mejor vendedor según ingresos totales generados? #
# ================================================================ #
query_8 = """WITH vendedores_ranking AS (
    SELECT Vendedor,
           COUNT(*) AS total_operaciones,
           SUM(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)) AS ingresos_totales,
           ROUND(AVG(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)), 2) AS precio_promedio,
           ROW_NUMBER() OVER (ORDER BY SUM(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)) DESC) AS ranking
    FROM inmuebles_raw
        GROUP BY Vendedor
)
SELECT *
FROM vendedores_ranking
ORDER BY ranking;"""


# ============================================================ #
# 9. ¿Cuál es el tipo de propiedad más vendido en cada ciudad? #
# ============================================================ #
query_9 = """WITH tipo_por_ciudad AS (
    SELECT Ciudad,
           Tipo,
           COUNT(*) AS cantidad,
           ROW_NUMBER() OVER (PARTITION BY Ciudad ORDER BY COUNT(*) DESC) AS ranking
    FROM inmuebles_raw
        GROUP BY Ciudad, Tipo
)
SELECT Ciudad,
       Tipo,
       cantidad
    FROM tipo_por_ciudad
    WHERE ranking = 1
       ORDER BY cantidad DESC;"""

# ===================================================================================================== #
# 10. ¿Qué vendedor tiene mejor rendimiento en términos de precio por metro cuadrado y tiempo de venta? #
# ===================================================================================================== #
query_10 = """WITH vendedor_performance AS (
    SELECT Vendedor,
           Ciudad,
           COUNT(*) AS total_operaciones,
           ROUND(AVG(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL) / Superficie), 2) AS precio_por_m2,
           ROUND(AVG("Días para Vender"), 2) AS dias_promedio,
           ROUND(AVG(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)), 2) AS precio_promedio,
           RANK() OVER (PARTITION BY Ciudad ORDER BY AVG(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL) / Superficie) DESC) AS ranking_precio_m2,
           RANK() OVER (PARTITION BY Ciudad ORDER BY AVG("Días para Vender") ASC) AS ranking_velocidad
    FROM inmuebles_raw
        GROUP BY Vendedor, Ciudad
        HAVING COUNT(*) >= 2
)
SELECT Vendedor,
       Ciudad,
       total_operaciones,
       precio_por_m2,
       dias_promedio,
       ranking_precio_m2,
       ranking_velocidad,
       ROUND((ranking_precio_m2 + ranking_velocidad) / 2.0, 2) AS score_promedio
    FROM vendedor_performance
       ORDER BY Ciudad, score_promedio ASC;"""



# ==================================================================================== #
# Ejecutar la consulta y cargar el resultado en un DataFrame de Pandas y guarda en CSV #
# ==================================================================================== #
df = pd.read_sql_query(query_4, bd)
df.to_csv("data/query_4.csv", index=False)

# =================================================== #
# Imprimir el resultado de la consulta en la terminal #
# =================================================== #
print(df.to_string(index=False))

# ============================================ #
# Cerrar la conexión a la base de datos SQLite #
# ============================================ #
bd.close()