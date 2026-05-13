import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# CONFIGURACIÓN
# =========================

st.set_page_config(
    page_title="Credit Risk Dashboard",
    layout="wide",
    page_icon="📊"
)

st.title("📊 Credit Risk Dashboard")
st.markdown("Análisis exploratorio interactivo del riesgo crediticio")

# =========================
# CARGA DE DATOS
# =========================

@st.cache_data
def load_data():
    return pd.read_csv("/Users/duvancatano/Documents/Data_Analytics_UdeA/ml-project/data/credit/credito_datos.csv")

data_imp = load_data()

# =========================
# SIDEBAR FILTROS
# =========================

st.sidebar.header("🔎 Filtros")

genero = st.sidebar.multiselect(
    "Género",
    data_imp["Genero"].unique(),
    default=data_imp["Genero"].unique()
)

edad = st.sidebar.slider(
    "Edad",
    int(data_imp["Edad"].min()),
    int(data_imp["Edad"].max()),
    (20, 60)
)

df = data_imp[
    (data_imp["Genero"].isin(genero)) &
    (data_imp["Edad"].between(edad[0], edad[1]))
]

# =========================
# KPIs
# =========================

st.subheader("📌 Indicadores clave")

col1, col2, col3 = st.columns(3)

col1.metric("Total clientes", len(df))
col2.metric("Riesgosos (%)", f"{df['Objetivo'].mean()*100:.2f}%")
col3.metric("Ingreso promedio", f"{df['Ingresos_totales'].mean():,.0f}")

# =========================
# TABS
# =========================

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Distribución",
    "👥 Segmentación",
    "📈 Relaciones",
    "📞 Contacto"
])

# =========================
# TAB 1: DISTRIBUCIÓN
# =========================

with tab1:
    st.subheader("Distribución del riesgo")

    conteo = df["Objetivo"].value_counts()

    fig, ax = plt.subplots()
    ax.bar(["No riesgoso", "Riesgoso"], conteo.values)
    ax.set_title("Distribución de la variable objetivo")

    for i, v in enumerate(conteo.values):
        ax.text(i, v, f"{v}", ha='center')

    st.pyplot(fig)

# =========================
# TAB 2: SEGMENTACIÓN
# =========================

with tab2:
    st.subheader("Riesgo por segmento")

    variable = st.selectbox(
        "Selecciona variable",
        [
            "Tipo_ingresos",
            "Nivel_educativo",
            "Estado_civil",
            "Tipo_vivienda",
            "Tipo_ocupacion",
            "Perfil_activos"
        ]
    )

    tabla = pd.crosstab(
        df[variable],
        df["Objetivo"],
        normalize="index"
    )

    tabla.columns = ["No riesgoso", "Riesgoso"]
    tabla = tabla.sort_values(by="Riesgoso", ascending=False)

    fig, ax = plt.subplots(figsize=(10,5))
    tabla.plot(kind="bar", ax=ax)

    ax.set_title(f"Riesgo según {variable}")
    ax.set_ylabel("Proporción")

    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f")

    st.pyplot(fig)

# =========================
# TAB 3: RELACIONES
# =========================

with tab3:
    st.subheader("Edad vs riesgo")

    edad_riesgo = df.groupby("Edad")["Objetivo"].mean()

    fig, ax = plt.subplots()
    ax.plot(edad_riesgo.index, edad_riesgo.values)
    ax.set_title("Probabilidad de riesgo por edad")

    st.pyplot(fig)

    st.subheader("Ingresos vs riesgo")

    fig, ax = plt.subplots()
    ax.scatter(df["Ingresos_totales"], df["Objetivo"], alpha=0.3)
    ax.set_title("Ingresos vs Riesgo")

    st.pyplot(fig)

# =========================
# TAB 4: CONTACTO
# =========================

with tab4:
    st.subheader("Nivel de contacto")

    contacto = pd.crosstab(
        df["Contacto_score"],
        df["Objetivo"],
        normalize="index"
    )

    contacto.columns = ["No riesgoso", "Riesgoso"]

    fig, ax = plt.subplots()
    contacto.plot(kind="bar", ax=ax)

    ax.set_title("Riesgo según nivel de contacto")

    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f")

    st.pyplot(fig)

# =========================
# FOOTER
# =========================

st.markdown("---")
st.markdown("Dashboard desarrollado para análisis de riesgo crediticio")