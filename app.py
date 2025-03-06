import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title('Análisis de anuncios de coches')

# Cargar el conjunto de datos
df = pd.read_csv('vehicles_us.csv')

# Mostrar el dataframe
st.write('Datos de anuncios de coches:')
st.write(df)

# Crear un gráfico interactivo
st.write('Gráfico de dispersión: Precio vs. Año del modelo')
fig = px.scatter(df, x='model_year', y='price')
st.plotly_chart(fig)