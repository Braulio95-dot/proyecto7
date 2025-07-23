import streamlit as st
import pandas as pd
import plotly.express as px


st.title('Análisis de Vehículos Usados')


st.header('Exploración de datos de autos en venta')


df = pd.read_csv('vehicles_us.csv')


st.subheader('Vista previa de los datos')
st.write(df.head())


build_histogram = st.checkbox('Mostrar histograma del odómetro')
if build_histogram:
    st.write('Creación de un histograma de odómetro de los vehículos en venta')

    fig = px.histogram(df, x='odometer', nbins=30,
                       labels={'odometer': 'Kilometraje'},
                       title='Distribución del kilometraje (odometer)')

    st.plotly_chart(fig, use_container_width=True)


build_scatter = st.checkbox(
    'Mostrar gráfico de dispersión precio vs kilometraje')
if build_scatter:
    st.write('Creación de un gráfico de dispersión entre precio y kilometraje')

    fig_scatter = px.scatter(df, x='odometer', y='price',
                             labels={'odometer': 'Kilometraje',
                                     'price': 'Precio'},
                             title='Relación entre precio y kilometraje')

    st.plotly_chart(fig_scatter, use_container_width=True)
