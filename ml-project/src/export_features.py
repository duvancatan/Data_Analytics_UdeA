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
db_path = BASE_DIR / "database/housing.db"
conn = sqlite3.connect(db_path)

# ========================================================= #
# Leer la vista de features y exportarla a un archivo CSV #
# ========================================================= #

#query = """ SELECT  
#                   municipality,
#                   COUNT(*) AS Total
#              FROM housing  
#            GROUP BY 1
#            ORDER BY Total;
#"""

query = """ SELECT municipality, 
                   AVG(house_market_value) AS promedio
            FROM housing  
            GROUP BY 1
            ORDER BY promedio;
"""

df_ml = pd.read_sql_query(query, conn)

conn.close()

output_path = BASE_DIR / "data/housing/query.csv"
df_ml.to_csv(output_path, index=False)

print("Query exportado correctamente")