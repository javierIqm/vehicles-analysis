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

# Crear un gráfico interactivo de dispersión
st.write('Gráfico de dispersión: Precio vs. Año del modelo')
fig_scatter = px.scatter(df, x='model_year', y='price', title='Precio vs. Año del modelo')
st.plotly_chart(fig_scatter)

# Checkbox para mostrar el histograma
if st.checkbox('Mostrar histograma del precio'):
    st.write('Histograma del precio de los coches')
    fig_hist = px.histogram(df, x='price', nbins=30, title='Distribución del precio de los coches')
    st.plotly_chart(fig_hist)

# Checkbox para mostrar el histograma del año del modelo
if st.checkbox('Mostrar histograma del año del modelo'):
    st.write('Histograma del año del modelo de los coches')
    fig_hist_year = px.histogram(df, x='model_year', nbins=30, title='Distribución del año del modelo de los coches')
    st.plotly_chart(fig_hist_year)