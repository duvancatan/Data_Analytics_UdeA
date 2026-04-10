import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# =========================
# RUTAS
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "model_linear_regression.joblib"
FEATURES_PATH = BASE_DIR / "models" / "features_linear_regression.joblib"

# =========================
# CARGAR MODELO
# =========================
model = joblib.load(MODEL_PATH)
features = joblib.load(FEATURES_PATH)

# =========================
# CONFIG APP
# =========================
st.set_page_config(
    page_title="Predicción de Viviendas",
    layout="wide"
)

st.title("🏠 Predicción del Valor de Viviendas")
st.markdown("Ingrese las características para obtener una predicción")

# =========================
# INPUTS DINÁMICOS
# =========================
input_data = {}

st.sidebar.header("📊 Variables de entrada")

for col in features:
    
    # Detectar tipo básico (puedes mejorar esto luego)
    if "age" in col or "duration" in col or "campaign" in col:
        input_data[col] = st.sidebar.number_input(col, value=0)
    
    else:
        input_data[col] = st.sidebar.text_input(col, value="")

# =========================
# BOTÓN PREDICCIÓN
# =========================
if st.sidebar.button("🔮 Predecir"):
    
    df = pd.DataFrame([input_data])
    
    try:
        pred = model.predict(df)
        
        st.success(f"💰 Predicción: {pred[0]:,.2f}")
    
    except Exception as e:
        st.error(f"Error en la predicción: {e}")

# =========================
# MOSTRAR INPUT
# =========================
st.subheader("📄 Datos ingresados")
st.write(pd.DataFrame([input_data]))


# =========================== #
# streamlit run src/stream.py #
# =========================== #