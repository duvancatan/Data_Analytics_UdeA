# ==========================================================
# Script para ejecutar una consulta SQL y exportarla a CSV
# ==========================================================

import pandas as pd
import sqlite3
from pathlib import Path

# ==========================================================
# Rutas del proyecto
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[1]

DB_PATH = BASE_DIR / "database" / "northwind.db"
SQL_DIR = BASE_DIR / "sql"
DATA_DIR = BASE_DIR / "data"


# ==========================================================
# Función para ejecutar consulta
# ==========================================================

def export_query(i):

    sql_file = SQL_DIR / f"query_{i}.sql"

    with open(sql_file, "r") as f:
        query = f.read()

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(query, conn)

    conn.close()

    output_file = DATA_DIR / f"query_{i}.csv"

    df.to_csv(output_file, index=False)

    print("\nConsulta ejecutada correctamente")
    print(f"Archivo generado: {output_file}")


# ==========================================================
# Pedir número de consulta al usuario
# ==========================================================

i = int(input("¿Qué query quieres ejecutar? "))

export_query(i)