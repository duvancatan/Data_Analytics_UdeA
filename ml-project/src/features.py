# ============================================================= #
# Librerías necesarias para la creación de la vista de features #
# ============================================================= #
import sqlite3
from pathlib import Path

# ================================== #
# Definir la ruta a la base de datos #
# ================================== #
BASE_DIR = Path(__file__).resolve().parents[1]
db_path = BASE_DIR / "database/promos.db"

conn = sqlite3.connect(db_path)

# ========================================================================================= #
# La vista se llama "promos_features" y selecciona las columnas relevantes para el análisis #
# ========================================================================================= #
conn.execute("""
CREATE VIEW IF NOT EXISTS promos_features AS
SELECT
    age,
    duration,
    campaign,
    emp_var_rate,
    cons_price_idx,
    cons_conf_idx,
    nr_employed,
    CASE WHEN y = 'yes' THEN 1 ELSE 0 END AS target
FROM promos_raw
WHERE age IS NOT NULL
""")

conn.commit()
conn.close()

print("Vista promos_features creada correctamente")

