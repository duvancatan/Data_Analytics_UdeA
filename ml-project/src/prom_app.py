# Librerías #
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

# Organizar las rutas de acceso a los datos #
mainpath= "/Users/duvancatano/Documents/Data_Analytics_UdeA/ml-project/data/promotions" #Cuando aparece "\" coloco r adelante
filename= "promos.csv"
fullpath= os.path.join(mainpath,filename)

# Cargar los datos #
data = pd.read_csv(fullpath, sep=";")      # El separador es ";" porque en el archivo .csv los valores están separados por punto y coma

# Homogenizar la variable educación basic.4y, basic.6y, basic.9y, university.degree = Basic # 
data["education"] = np.where(data["education"]=="basic.4y", "Basic", data["education"])
data["education"] = np.where(data["education"]=="basic.6y", "Basic", data["education"])
data["education"] = np.where(data["education"]=="basic.9y", "Basic", data["education"])

# Poner letra inicial en mayuscula high.school=High School, professional.course=Professional Course, university.degree=University Degree
data["education"] = np.where(data["education"]=="high.school", "High School", data["education"])
data["education"] = np.where(data["education"]=="professional.course", "Professional Course", data["education"])
data["education"] = np.where(data["education"]=="university.degree", "University Degree", data["education"])

# Poner letra inicial en mayuscula illiterate=Illiterate, unknown=Unknown
data["education"] = np.where(data["education"]=="illiterate", "Illiterate", data["education"])
data["education"] = np.where(data["education"]=="unknown", "Unknown", data["education"])

# Renombrar Data Frame #
df = data

# Título #
st.title("📊 Dashboard de Promociones")
st.markdown("Análisis Interactivo de Campañas de Marketing")

# Filtros #
st.sidebar.header("🔎 Filtros")

job = st.sidebar.multiselect("Trabajo", sorted(df["job"].dropna().unique()))
marital = st.sidebar.multiselect("Estado civil", sorted(df["marital"].dropna().unique()))
education = st.sidebar.multiselect("Educación", sorted(df["education"].dropna().unique()))

age_range = st.sidebar.slider(
    "Edad",
    int(df["age"].min()),
    int(df["age"].max()),
    (int(df["age"].min()), int(df["age"].max()))
)

# Filtrado #
df_filtered = df.copy()

if job:
    df_filtered = df_filtered[df_filtered["job"].isin(job)]

if marital:
    df_filtered = df_filtered[df_filtered["marital"].isin(marital)]

if education:
    df_filtered = df_filtered[df_filtered["education"].isin(education)]

df_filtered = df_filtered[
    (df_filtered["age"] >= age_range[0]) &
    (df_filtered["age"] <= age_range[1])
]

# KPIs #
col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Total registros", len(df_filtered))
col2.metric("📊 Edad promedio", round(df_filtered["age"].mean(), 2))
col3.metric("⏱️ Duración promedio", round(df_filtered["duration"].mean(), 2))
col4.metric("💰 Tasa conversión", round((df_filtered["y"] == "yes").mean(), 3))

# TABS #
tab1, tab2, tab3 = st.tabs(["📊 Exploración", "📈 Análisis", "🤖 Modelo"])

# TAB 1: Exploración #
with tab1:

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(df_filtered, x="age", nbins=30, title="Distribución de Edad")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(df_filtered, x="y", title="Distribución de la variable objetivo")
        st.plotly_chart(fig, use_container_width=True)

    fig = px.histogram(df_filtered, x="job", color="y", title="Conversión por trabajo")
    st.plotly_chart(fig, use_container_width=True)

# TAB 2: Análsis Avanzado #
with tab2:

    col1, col2 = st.columns(2)

    with col1:
        fig = px.scatter(
            df_filtered,
            x="age",
            y="duration",
            color="y",
            title="Edad vs Duración"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.box(
            df_filtered,
            x="job",
            y="duration",
            color="y",
            title="Duración por trabajo"
        )
        st.plotly_chart(fig, use_container_width=True)

# Heatmap #
    num_cols = df_filtered.select_dtypes(include=np.number).columns
    corr = df_filtered[num_cols].corr()

    fig = go.Figure(
        data=go.Heatmap(
            z=corr.values,
            x=corr.columns,
            y=corr.columns
        )
    )

    fig.update_layout(title="Mapa de Correlación")
    st.plotly_chart(fig, use_container_width=True)

# TAB 3: Medelo #
with tab3:

    st.subheader("Predicción Simulada")

    age_input = st.number_input("Edad", 18, 100, 30)
    duration_input = st.number_input("Duración", 0, 5000, 200)

    if st.button("Predecir"):
        # Simulación simple
        pred = "yes" if duration_input > 200 else "no"
        st.success(f"Predicción: {pred}")

# Datos Finales #
st.subheader("Datos filtrados")
st.dataframe(df_filtered)

# ============================= #
#  Ejecución desde la Terminal  #
# streamlit run src/prom_app.py #         
# ============================= #