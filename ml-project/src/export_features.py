# ===========================================================#
# Script para exportar la vista de features a un archivo CSV #
# ========================================================== #

# ==================================================== #
# Librerías necesarias para la exportación de features #
# ==================================================== #
import pandas as pd
import sqlite3
from pathlib import Path

# ================================== #
# Definir la ruta a la base de datos #
# ================================== #
BASE_DIR = Path(__file__).resolve().parents[1]
db_path = BASE_DIR / "database/promos.db"
conn = sqlite3.connect(db_path)

# ========================================================= #
# Leer la vista de features y exportarla a un archivo CSV #
# ========================================================= #
df_ml = pd.read_sql_query("SELECT age, duration,campaign, target FROM promos_features WHERE age < 30", conn)

conn.close()

output_path = BASE_DIR / "data/promos_ml.csv"
df_ml.to_csv(output_path, index=False)

print("Dataset ML exportado correctamente")