# ======== #
# LIBRERÍAS #
# ======== #

import streamlit as st
import pandas as pd
import plotly.express as px

# ============= #
# CONFIGURACIÓN #
# ============= #

st.set_page_config(
    page_title="Fraud EDA Dashboard",
    layout="wide",
    page_icon="📊"
)

st.title("🥷🏾 Dashboard Analítico de Detección de Fraude Financiero")
st.markdown("Análisis exploratorio interactivo del fraude")

# ===== #
# DATOS #
# ===== #

@st.cache_data
def load_data():
    return pd.read_csv(
        "/Users/duvancatano/Documents/Data_Analytics_UdeA/ml-project/data/fraud/fraude_full.csv"
    )

df = load_data()

# ============================== #
# CREAR VARIABLE PERIODO DEL DÍA #
# ============================== #

def periodo_dia(hora):

    if 0 <= hora <= 5:
        return "Madrugada"

    elif 6 <= hora <= 11:
        return "Mañana"

    elif 12 <= hora <= 17:
        return "Tarde"

    else:
        return "Noche"

df["PERIODO_DIA"] = df["HORA_AUX"].apply(periodo_dia)

# ======= #
# SIDEBAR #
# ======= #

st.sidebar.header("🔎 Filtros")

sexo = st.sidebar.multiselect(
    "Sexo",
    df["SEXO"].dropna().unique(),
    default=df["SEXO"].dropna().unique()
)

segmento = st.sidebar.multiselect(
    "Segmento",
    df["SEGMENTO"].dropna().unique(),
    default=df["SEGMENTO"].dropna().unique()
)

edad = st.sidebar.slider(
    "Edad",
    int(df["EDAD"].min()),
    int(df["EDAD"].max()),
    (25, 65)
)

df = df[
    (df["SEXO"].isin(sexo)) &
    (df["SEGMENTO"].isin(segmento)) &
    (df["EDAD"].between(*edad))
]

# ==== #
# KPIs #
# ==== #

col1, col2, col3, col4 = st.columns(4)

col1.metric("Transacciones", len(df))
col2.metric("Fraude %", f"{df['FRAUDE'].mean()*100:.2f}")
col3.metric("Valor medio", f"{df['VALOR'].mean():,.0f}")
col4.metric("Edad media", f"{df['EDAD'].mean():.1f}")

# ============== #
# GRID PRINCIPAL #
# ============== #

c1, c2 = st.columns(2)

# =================== #
# DISTRIBUCIÓN FRAUDE #
# =================== #

with c1:

    fig = px.pie(
        df,
        names="FRAUDE",
        title="Distribución Fraude",
        hole=0.5
    )

    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    st.plotly_chart(fig, use_container_width=True)

# =============== #
# SUBGRID DERECHA #
# =============== #

sub1, sub2 = c2.columns(2)

# =============== #
# FRAUDE POR HORA #
# =============== #

with sub1:

    temp = df.groupby("HORA_AUX")["FRAUDE"].mean().reset_index()

    fig = px.line(
        temp,
        x="HORA_AUX",
        y="FRAUDE",
        title="Fraude por hora"
    )

    fig.update_layout(
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)

# ========================== #
# FRAUDE POR PERIODO DEL DÍA #
# ========================== #

with sub2:

    orden_periodos = [
        "Madrugada",
        "Mañana",
        "Tarde",
        "Noche"
    ]

    df["PERIODO_DIA"] = pd.Categorical(
        df["PERIODO_DIA"],
        categories=orden_periodos,
        ordered=True
    )

    tabla = pd.crosstab(
        df["PERIODO_DIA"],
        df["FRAUDE"],
        normalize="index"
    )

    tabla.columns = ["No fraude", "Fraude"]

    tabla = tabla.reset_index()

    fig = px.bar(
        tabla,
        x="PERIODO_DIA",
        y="Fraude",
        color="Fraude",
        color_continuous_scale="Reds",
        text_auto=".2f",
        title="Fraude por periodo"
    )

    fig.update_layout(
        height=300,
        template="plotly_dark",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

# ============ #
# SEGUNDA FILA #
# ============ #

c4, c5, c6 = st.columns(3)

# ============== #
# FRAUDE POR DÍA #
# ============== #

with c4:

    orden_dias = [
        "Domingo",
        "Lunes",
        "Martes",
        "Miercoles",
        "Jueves",
        "Viernes",
        "Sabado"
    ]

    df["DIASEM"] = pd.Categorical(
        df["DIASEM"],
        categories=orden_dias,
        ordered=True
    )

    temp = df.groupby("DIASEM")["FRAUDE"].mean().reset_index()

    fig = px.bar(
        temp,
        x="DIASEM",
        y="FRAUDE",
        title="Fraude por día"
    )

    fig.update_layout(
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)

# =================== #
# FRAUDE POR QUINCENA #
# =================== #

with c5:

    temp = df.groupby("QUINCENA")["FRAUDE"].mean().reset_index()

    fig = px.bar(
        temp,
        x="QUINCENA",
        y="FRAUDE",
        color="FRAUDE",
        color_continuous_scale="Reds",
        title="Fraude por quincena",
        text_auto=".2f"
    )

    fig.update_layout(
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)

# ================ #
# FRAUDE POR CANAL #
# ================ #

with c6:

    temp = df.groupby("CANAL")["FRAUDE"].mean().reset_index()

    fig = px.bar(
        temp,
        x="CANAL",
        y="FRAUDE",
        title="Fraude por canal"
    )

    fig.update_layout(
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)

# ============ #
# TERCERA FILA #
# ============ #

c7, c8 = st.columns(2)

# ============== #
# EDAD VS FRAUDE #
# ============== #

with c7:

    fig = px.histogram(
        df,
        x="EDAD",
        color="FRAUDE",
        nbins=30,
        title="Edad vs fraude",
        barmode="overlay"
    )

    fig.update_layout(
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)

# =================== #
# INGRESOS VS EGRESOS #
# =================== #

with c8:

    fig = px.scatter(
        df,
        x="INGRESOS",
        y="EGRESOS",
        color="FRAUDE",
        title="Ingresos vs Egresos",
        opacity=0.6
    )

    fig.update_xaxes(type="log")
    fig.update_yaxes(type="log")

    fig.update_layout(
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)

# ========= #
# MOVILIDAD #
# ========= #

st.subheader("🌍 Movilidad")

fig = px.scatter(
    df,
    x="Dist_Sum_INTER",
    y="NROPAISES",
    color="FRAUDE",
    opacity=0.5,
    title="Movilidad internacional"
)

fig.update_layout(
    height=350
)

st.plotly_chart(fig, use_container_width=True)

# ====== #
# FOOTER #
# ====== #

st.markdown("---")
st.caption("EDA interactivo para detección de fraude - UdeA")

# ======================================== #
#        Ejecución desde la Terminal       #
#       streamlit run src/fraud_eda.py     #
# ======================================== #