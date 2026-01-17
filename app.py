import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header("ANALISIS DE VENTA DE AUTOS USADOS")


hist_button = st.button('Construir histograma')  # crear un botón



if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches'
    )

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un diagrama de dispersión')

if build_scatter:
     
     st.write("Creando gráfico de dispersión")
     fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
     st.plotly_chart(fig, use_container_width=True)   
    