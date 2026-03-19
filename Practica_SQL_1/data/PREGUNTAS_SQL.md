# 10 Preguntas SQL - Base de Datos Inmuebles
## De Menor a Mayor Dificultad

---

## NIVEL 1: CONSULTAS BÁSICAS

### Pregunta 1: ¿Cuántas propiedades hay registradas en la base de datos?
**Dificultad:** ⭐ Principiante

```sql
SELECT COUNT(*) AS total_propiedades
FROM inmuebles_raw;
```

**Conceptos:** `COUNT()`, agregación básica

---

### Pregunta 2: ¿Cuál es el precio máximo y mínimo de venta registrado?
**Dificultad:** ⭐ Principiante

```sql
SELECT 
    MIN(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)) AS precio_minimo,
    MAX(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)) AS precio_maximo
FROM inmuebles_raw;
```

**Conceptos:** `MIN()`, `MAX()`, `CAST()`, `REPLACE()`, limpieza de datos

---

### Pregunta 3: ¿Cuántas propiedades son de cada tipo?
**Dificultad:** ⭐ Principiante

```sql
SELECT 
    Tipo,
    COUNT(*) AS cantidad
FROM inmuebles_raw
GROUP BY Tipo
ORDER BY cantidad DESC;
```

**Conceptos:** `GROUP BY`, `ORDER BY`, agregación

---

## NIVEL 2: CONSULTAS INTERMEDIAS

### Pregunta 4: ¿Cuál es la superficie promedio por tipo de propiedad?
**Dificultad:** ⭐⭐ Intermedio

```sql
SELECT 
    Tipo,
    ROUND(AVG(Superficie), 2) AS superficie_promedio,
    COUNT(*) AS numero_propiedades
FROM inmuebles_raw
GROUP BY Tipo
ORDER BY superficie_promedio DESC;
```

**Conceptos:** `AVG()`, `ROUND()`, agregaciones múltiples, `GROUP BY`

---

### Pregunta 5: ¿Qué vendedor ha vendido más propiedades y cuál es el precio promedio que ha manejado?
**Dificultad:** ⭐⭐ Intermedio

```sql
SELECT 
    Vendedor,
    COUNT(*) AS total_ventas,
    ROUND(AVG(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)), 2) AS precio_promedio
FROM inmuebles_raw
GROUP BY Vendedor
ORDER BY total_ventas DESC;
```

**Conceptos:** `GROUP BY`, `COUNT()`, `AVG()`, limpieza de datos, múltiples agregaciones

---

### Pregunta 6: ¿Cuál es el promedio de días para vender agrupado por ciudad?
**Dificultad:** ⭐⭐ Intermedio

```sql
SELECT 
    Ciudad,
    ROUND(AVG("Días para Vender"), 2) AS dias_promedio,
    MIN("Días para Vender") AS dias_minimo,
    MAX("Días para Vender") AS dias_maximo,
    COUNT(*) AS total_operaciones
FROM inmuebles_raw
GROUP BY Ciudad
ORDER BY dias_promedio DESC;
```

**Conceptos:** `GROUP BY`, múltiples funciones de agregación, `ORDER BY`

---

## NIVEL 3: CONSULTAS AVANZADAS

### Pregunta 7: ¿Cuáles son las ciudades con mayor ingresos totales por ventas? (Considera solo operaciones de Venta)
**Dificultad:** ⭐⭐⭐ Avanzado

```sql
SELECT 
    Ciudad,
    SUM(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)) AS ingresos_totales,
    COUNT(*) AS numero_propiedades,
    ROUND(AVG(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)), 2) AS precio_promedio
FROM inmuebles_raw
WHERE Operación = 'Venta'
GROUP BY Ciudad
ORDER BY ingresos_totales DESC;
```

**Conceptos:** `SUM()`, `WHERE`, filtrado de datos, `GROUP BY`, limpieza avanzada de datos

---

### Pregunta 8: Ranking: ¿Quién es el mejor vendedor según ingresos totales generados?
**Dificultad:** ⭐⭐⭐ Avanzado

```sql
WITH vendedores_ranking AS (
    SELECT 
        Vendedor,
        COUNT(*) AS total_operaciones,
        SUM(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)) AS ingresos_totales,
        ROUND(AVG(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)), 2) AS precio_promedio,
        ROW_NUMBER() OVER (ORDER BY SUM(CAST(REPLACE(REPLACE("Precio Venta", '$', ''), ',', '') AS DECIMAL)) DESC) AS ranking
    FROM inmuebles_raw
    GROUP BY Vendedor
)
SELECT *
FROM vendedores_ranking
ORDER BY ranking;
```

**Conceptos:** `WITH` (CTE), `ROW_NUMBER()`, funciones de ventana, agregaciones complejas

---

### Pregunta 9: ¿Cuál es el tipo de propiedad más vendido en cada ciudad?
**Dificultad:** ⭐⭐⭐ Avanzado

```sql
WITH tipo_por_ciudad AS (
    SELECT 
        Ciudad,
        Tipo,
        COUNT(*) AS cantidad,
        ROW_NUMBER() OVER (PARTITION BY Ciudad ORDER BY COUNT(*) DESC) AS ranking
    FROM inmuebles_raw
    GROUP BY Ciudad, Tipo
)
SELECT 
    Ciudad,
    Tipo,
    cantidad
FROM tipo_por_ciudad
WHERE ranking = 1
ORDER BY cantidad DESC;
```

**Conceptos:** CTE, `PARTITION BY`, `ROW_NUMBER()`, ventanas, `GROUP BY` múltiple

---

## NIVEL 4: CONSULTAS EXPERTO

### Pregunta 10: Análisis comparativo: ¿Qué vendedor tiene mejor rendimiento en términos de precio por metro cuadrado y tiempo de venta?
**Dificultad:** ⭐⭐⭐⭐ Experto

```sql
WITH vendedor_performance AS (
    SELECT 
        Vendedor,
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
SELECT 
    Vendedor,
    Ciudad,
    total_operaciones,
    precio_por_m2,
    dias_promedio,
    ranking_precio_m2,
    ranking_velocidad,
    ROUND((ranking_precio_m2 + ranking_velocidad) / 2.0, 2) AS score_promedio
FROM vendedor_performance
ORDER BY Ciudad, score_promedio ASC;
```

**Conceptos:** 
- CTE avanzado
- `RANK()` con `PARTITION BY`
- Cálculos derivados complejos
- Divisiones entre columnas
- `HAVING` con agregaciones
- Múltiples funciones de ventana
- Lógica de negocio compleja

---

## Resumen de Conceptos SQL por Dificultad

| Dificultad | Preguntas | Conceptos Clave |
|---|---|---|
| ⭐ Principiante | 1-3 | COUNT, MIN, MAX, GROUP BY, ORDER BY |
| ⭐⭐ Intermedio | 4-6 | AVG, SUM, múltiples agregaciones, WHERE |
| ⭐⭐⭐ Avanzado | 7-9 | CTE, ROW_NUMBER, PARTITION BY, joins implícitos |
| ⭐⭐⭐⭐ Experto | 10 | Múltiples ventanas, RANK, cálculos derivados, HAVING avanzado |

---

## Notas de Implementación

1. **Limpieza de datos:** Las consultas incluyen `REPLACE()` para limpiar el formato de moneda en "Precio Venta"
2. **Conversión de tipos:** Se utiliza `CAST()` para convertir texto a valores numéricos
3. **Redondeo:** `ROUND()` se usa para presentar resultados con 2 decimales
4. **CTEs:** Las consultas avanzadas usan `WITH` para mejorar legibilidad
5. **Funciones de ventana:** `ROW_NUMBER()`, `RANK()` y `PARTITION BY` para análisis comparativos

---

## Orden Recomendado para Aprendizaje

1. Practica primero las Preguntas 1-3 (SELECT, COUNT, GROUP BY)
2. Luego Preguntas 4-6 (AVG, múltiples agregaciones)
3. Después Preguntas 7-9 (filtros, CTEs, funciones de ventana)
4. Finalmente Pregunta 10 (análisis complejo combinando todo)
