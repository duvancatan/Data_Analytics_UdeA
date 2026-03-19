# Documentación: Base de Datos "inmuebles_crudos.csv"

## Descripción General
Este conjunto de datos contiene información sobre transacciones de bienes inmuebles en México durante el periodo de 2016-2017. Incluye detalles sobre propiedades listadas, vendidas o alquiladas en diferentes ciudades del país.

---

## Diccionario de Variables

### 1. **Referencia**
- **Tipo de dato:** Numérico Entero (Integer)
- **Descripción:** Identificador único para cada propiedad inmobiliaria en la base de datos.
- **Rango de valores:** Números positivos (Ej: 1, 2, 3, ...)
- **Uso:** Clave primaria para identificar registros únicos.

### 2. **FechaAlta**
- **Tipo de dato:** Fecha (Date)
- **Formato:** MM/DD/YY
- **Descripción:** Fecha en la que la propiedad fue registrada o listada en el sistema inmobiliario.
- **Rango de valores:** Fechas entre enero de 2016 y marzo de 2016 (aproximadamente)
- **Ejemplo:** 1/18/16 (18 de enero de 2016)

### 3. **Tipo**
- **Tipo de dato:** Texto/Categoría (Categorical)
- **Descripción:** Clasificación del tipo de propiedad inmueble.
- **Valores posibles:**
  - **Casa:** Vivienda unifamiliar
  - **Departamento:** Apartamento o condominio
  - **Oficina:** Espacio comercial para oficinas
  - **Local:** Pequeño espacio comercial
  - **Industrial:** Propiedad de uso industrial
  - **Terreno:** Terreno sin construcción
  - **Estacionamiento:** Espacio para estacionamiento

### 4. **Operación**
- **Tipo de dato:** Texto/Categoría (Categorical)
- **Descripción:** Tipo de transacción inmobiliaria realizada.
- **Valores posibles:**
  - **Venta:** La propiedad fue vendida
  - **Alquiler:** La propiedad fue arrendada

### 5. **Ciudad**
- **Tipo de dato:** Texto/Categoría (Categorical)
- **Descripción:** Ubicación geográfica de la propiedad en México.
- **Valores posibles:**
  - **Cancún:** Ciudad en Quintana Roo
  - **Tijuana:** Ciudad en Baja California
  - **Monterrey:** Ciudad en Nuevo León
  - **Ciudad de México:** Capital del país

### 6. **Superficie**
- **Tipo de dato:** Numérico Entero (Integer)
- **Unidad de medida:** Metros cuadrados (m²)
- **Descripción:** Área total de la propiedad inmueble.
- **Rango de valores:** Números positivos (Ej: 40, 89, 103, ...)
- **Ejemplo:** 215 m²

### 7. **Precio Venta**
- **Tipo de dato:** Numérico Decimal (Numeric)
- **Unidad de medida:** Pesos Mexicanos ($)
- **Descripción:** Valor económico de la propiedad al momento de la transacción (venta o alquiler).
- **Formato en archivo:** Texto con formato de currency (Ej: " $1,154,980 ")
- **Nota:** Contiene espacios y símbolos de moneda que deben limpiarse para análisis numéricos.
- **Ejemplo:** $1,154,980

### 8. **Fecha Venta**
- **Tipo de dato:** Fecha (Date)
- **Formato:** MM/DD/YY
- **Descripción:** Fecha en la que se completó la transacción de la propiedad (venta o alquiler).
- **Rango de valores:** Fechas entre enero y febrero de 2017
- **Ejemplo:** 1/14/17 (14 de enero de 2017)

### 9. **Vendedor**
- **Tipo de dato:** Texto (String)
- **Descripción:** Nombre del agente inmobiliario o vendedor responsable de la transacción.
- **Valores observados:**
  - Joaquín
  - Jesús
  - Carmen
  - Luisa
  - Pedro
  - María
- **Uso:** Identificar qué vendedor realizó cada transacción.

### 10. **Estatus**
- **Tipo de dato:** Texto/Categoría (Categorical)
- **Descripción:** Estado actual de la transacción de la propiedad.
- **Valores posibles:**
  - **Vendida:** La transacción fue completada exitosamente (aplicable tanto para ventas como alquileres finalizados)
- **Nota:** En este dataset, todos los registros muestran "Vendida", indicando transacciones completadas.

### 11. **Días para Vender**
- **Tipo de dato:** Numérico Entero (Integer)
- **Unidad de medida:** Días
- **Descripción:** Número de días transcurridos entre la fecha en que la propiedad fue listada (FechaAlta) y la fecha en que se completó la transacción (Fecha Venta).
- **Cálculo:** Fecha Venta - FechaAlta = Días para Vender
- **Rango de valores:** Números positivos (Ej: 362, 348, 357, ...)
- **Interpretación:** Mayor número indica que tomó más tiempo vender/alquilar la propiedad.

---

## Resumen de Características del Dataset

| Característica | Descripción |
|---|---|
| **Período de datos** | Enero 2016 - Febrero 2017 |
| **Número de variables** | 11 columnas |
| **Tipo de análisis recomendado** | Análisis de precios, tiempo de venta, distribución geográfica, comparativa por tipo de propiedad |
| **Limpieza requerida** | Remover símbolos de moneda en "Precio Venta"; convertir fechas a formato estándar |
| **Variables numéricas** | Referencia, Superficie, Precio Venta, Días para Vender |
| **Variables categóricas** | Tipo, Operación, Ciudad, Vendedor, Estatus |
| **Variables de fecha** | FechaAlta, Fecha Venta |

---

## Notas Importantes para el Análisis

1. **Limpieza de datos:** El campo "Precio Venta" contiene símbolos de moneda y espacios que necesitan ser removidos para operaciones numéricas.

2. **Conversión de fechas:** Las fechas están en formato MM/DD/YY y pueden requerir conversión a un formato estándar (YYYY-MM-DD) según el sistema de análisis.

3. **Contexto:** Todas las transacciones en este dataset fueron completadas ("Vendida"), por lo que no hay registros de propiedades sin vender.

4. **Variabilidad temporal:** El tiempo para completar una transacción varía entre 319 y 365 días aproximadamente.
