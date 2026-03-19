# ================================================================================================== #
# Este script se conecta a una base de datos SQLite, ejecuta una consulta SQL para obtener todos los #
# registros de la tabla "customers" y luego imprime los resultados utilizando pandas.                #
# ================================================================================================== #

# ================================================================================ #
# Librerías necesarias para la conexión a la base de datos y manipulación de datos #
# ================================================================================ #
import sqlite3
import pandas as pd
from pathlib import Path


# ================================================================================================== #
# Definición de la ruta a la base de datos y conexión a la misma. Luego, se ejecuta una consulta SQL #
# para obtener los datos de la tabla "customers" y se imprimen los resultados.                       #
# ================================================================================================== #
BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR.parent / "/Users/duvancatano/Documents/Ciencia_Datos/Analitica_de_Datos_Material/Clase_5_SQL/Practica_SQL/database/northwind.db"

conn = sqlite3.connect(db_path)

query = """SELECT * FROM customers LIMIT 10;"""

tables = pd.read_sql_query(query, conn)

print(tables)