# ===================================== #
# DASHBOARD ANALÍTICO DE SPAM DETECTION #
# ===================================== #

import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler


# CONFIGURACIÓN GENERAL
st.set_page_config(
    page_title="Spam Detection Dashboard",
    page_icon="📧",
    layout="wide"
)

# ESTILO
st.markdown(
    """
    <style>
    .main {
        background-color: #0E1117;
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    h1, h2, h3 {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# TÍTULO
st.title("📧 Dashboard Inteligente de Detección de Spam")

st.markdown(
    """
    Análisis exploratorio interactivo de correos electrónicos spam utilizando técnicas de Machine Learning y visualización avanzada.
    """
)

# CARGA DE DATOS
@st.cache_data
def load_data():

    df = pd.read_csv(
        "/Users/duvancatano/Documents/Data_Analytics_UdeA/ml-project/data/spam/spam_dataset.csv"
    )

    return df


# Dataset
df = load_data()

# VARIABLE OBJETIVO
if df['type'].dtype == 'object':
    df['type'] = np.where(df['type'] == 'spam', 1, 0)

# RENOMBRE DE CLASES
map_class = {
    0: 'No Spam',
    1: 'Spam'
}

df['Clase'] = df['type'].map(map_class)

# SIDEBAR
st.sidebar.header("⚙️ Configuración")

selected_class = st.sidebar.multiselect(
    "Clase de correo",
    options=df['Clase'].unique(),
    default=df['Clase'].unique()
)

# Variables importantes
important_vars = [
    'free',
    'money',
    'credit',
    'your',
    'charExclamation',
    'capitalTotal',
    'business',
    'remove'
]

selected_var = st.sidebar.selectbox(
    "Variable de análisis",
    important_vars
)

# Filtrado
df = df[df['Clase'].isin(selected_class)]

# KPIs
c1, c2, c3, c4 = st.columns(4)

spam_rate = df['type'].mean() * 100

c1.metric(
    "📨 Correos",
    f"{len(df):,}"
)

c2.metric(
    "🚨 Spam (%)",
    f"{spam_rate:.2f}%"
)

c3.metric(
    "🔠 Mayúsculas Promedio",
    f"{df['capitalTotal'].mean():.1f}"
)

c4.metric(
    "❗ Exclamaciones Promedio",
    f"{df['charExclamation'].mean():.2f}"
)

# PRIMERA FILA
col1, col2 = st.columns(2)

# DISTRIBUCIÓN DE CLASES
with col1:

    conteo = df['Clase'].value_counts()

    porcentaje = (
        df['Clase']
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )

    fig = px.bar(
        x=conteo.index,
        y=conteo.values,
        text=porcentaje.astype(str) + '%',
        color=conteo.index,
        title='Distribución de Correos',
        color_discrete_map={
            'No Spam': '#636EFA',
            'Spam': '#EF553B'
        }
    )

    fig.update_layout(
        template='plotly_dark',
        title_x=0.5,
        showlegend=False,
        height=420,
        xaxis_title='Clase',
        yaxis_title='Cantidad'
    )

    fig.update_traces(textposition='outside')

    st.plotly_chart(fig, use_container_width=True)

# PIE CHART
with col2:

    fig = px.pie(
        df,
        names='Clase',
        hole=0.6,
        title='Proporción Spam vs No Spam',
        color='Clase',
        color_discrete_map={
            'No Spam': '#636EFA',
            'Spam': '#EF553B'
        }
    )

    fig.update_layout(
        template='plotly_dark',
        title_x=0.5,
        height=420
    )

    st.plotly_chart(fig, use_container_width=True)

# SEGUNDA FILA
col3, col4 = st.columns(2)

# HISTOGRAMA VARIABLE
with col3:

    fig = px.histogram(
        df,
        x=selected_var,
        color='Clase',
        marginal='box',
        opacity=0.7,
        nbins=40,
        title=f'Distribución de {selected_var}',
        color_discrete_map={
            'No Spam': '#636EFA',
            'Spam': '#EF553B'
        }
    )

    fig.update_layout(
        template='plotly_dark',
        title_x=0.5,
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# BOXPLOT
with col4:

    fig = px.box(
        df,
        x='Clase',
        y=selected_var,
        color='Clase',
        points='outliers',
        title=f'Boxplot de {selected_var}',
        color_discrete_map={
            'No Spam': '#636EFA',
            'Spam': '#EF553B'
        }
    )

    fig.update_layout(
        template='plotly_dark',
        title_x=0.5,
        height=500,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

# TERCERA FILA
st.subheader("📊 Relaciones entre Variables")

scatter_pairs = {
    'Money vs Free': ('money', 'free'),
    'Credit vs Your': ('credit', 'your'),
    'CapitalTotal vs CapitalLong': ('capitalTotal', 'capitalLong'),
    'Business vs Remove': ('business', 'remove')
}

selected_pair = st.selectbox(
    'Seleccionar relación',
    list(scatter_pairs.keys())
)

x_var, y_var = scatter_pairs[selected_pair]

fig = px.scatter(
    df,
    x=x_var,
    y=y_var,
    color='Clase',
    opacity=0.7,
    title=f'{x_var} vs {y_var}',
    color_discrete_map={
        'No Spam': '#636EFA',
        'Spam': '#EF553B'
    }
)

fig.update_layout(
    template='plotly_dark',
    title_x=0.5,
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# MATRIZ DE CORRELACIÓN
st.subheader("🔥 Correlación de Variables con Spam")

corr = (
    df.select_dtypes(include=['int64', 'float64'])
    .corr(numeric_only=True)['type']
    .drop('type')
    .sort_values(ascending=False)
)

corr_df = pd.DataFrame({
    'Variable': corr.index,
    'Correlación': corr.values
})

fig = px.bar(
    corr_df.head(20),
    x='Correlación',
    y='Variable',
    orientation='h',
    color='Correlación',
    color_continuous_scale='RdBu_r',
    title='Top Variables Asociadas al Spam'
)

fig.update_layout(
    template='plotly_dark',
    title_x=0.5,
    height=700
)

st.plotly_chart(fig, use_container_width=True)

# MATRIZ DE DISPERSIÓN
st.subheader("🧠 Scatter Matrix")

matrix_vars = [
    'free',
    'money',
    'credit',
    'your',
    'charExclamation'
]

fig = px.scatter_matrix(
    df,
    dimensions=matrix_vars,
    color='Clase',
    title='Scatter Matrix de Variables Relevantes',
    color_discrete_map={
        'No Spam': '#636EFA',
        'Spam': '#EF553B'
    }
)

fig.update_layout(
    template='plotly_dark',
    title_x=0.5,
    height=900
)

st.plotly_chart(fig, use_container_width=True)

# TABLA DESCRIPTIVA
st.subheader("📑 Estadísticas Descriptivas")

st.dataframe(
    df.describe().T,
    use_container_width=True
)

# INTERPRETACIÓN AUTOMÁTICA
st.subheader("🧾 Interpretación")

most_corr = corr.abs().sort_values(ascending=False).head(5)

for var in most_corr.index:

    st.markdown(
        f"""
        - La variable **{var}** presenta una fuerte asociación con la clasificación de spam.
        """
    )

st.markdown(
    """
    Los correos spam suelen presentar:

    - mayor frecuencia de palabras promocionales,
    - más signos de exclamación,
    - uso excesivo de mayúsculas,
    - y patrones lingüísticos repetitivos.
    """
)

# FOOTER
st.markdown('---')

st.caption(
    'Dashboard Interactivo de Detección de Spam • Machine Learning • Plotly • Streamlit'
)

# ============================= #
#  Ejecución desde la Terminal  #
# streamlit run src/spam_eda.py #         
# ============================= #