# ===================================================================== #
# Librerías necesarias para la extracción, transformación y carga (ETL) #
# ===================================================================== #

import pandas as pd
import sqlite3
from pathlib import Path

# =============================================================================================== #
# Definir rutas de archivos y base de datos usando pathlib para mayor flexibilidad y portabilidad #
# =============================================================================================== #

BASE_DIR = Path(__file__).resolve().parents[1]

csv_path = BASE_DIR / "data/promos_crudos.csv"
db_path = BASE_DIR / "database/promos.db"

# ======================================================================================= #
# Cargar datos en la base de datos SQLite y Leer CSV donde es importante el separador ";" #
# ======================================================================================= #

df = pd.read_csv(csv_path, sep=";")

conn = sqlite3.connect(db_path)

# =========================================================================================================== #
# Cargar el DataFrame en la tabla "promos_raw" de la base de datos SQLite, reemplazando la tabla si ya existe #
# =========================================================================================================== #

df.to_sql("promos_raw", conn, if_exists="replace", index=False)

conn.close()

print("Tabla promos_raw creada correctamente.")