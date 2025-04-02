# Cargar datos
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

air_nyc = pd.read_csv('AB_NYC_2019.csv')
air_nyc['estimated_income'] = air_nyc['price'] * air_nyc['reviews_per_month'].fillna(0) * 12



st.title("Dashboard Airbnb NYC")

zona = st.selectbox("Selecciona zona:", air_nyc['neighbourhood_group'].unique())
filtrado = air_nyc[air_nyc['neighbourhood_group'] == zona]

st.subheader(f"Distribución de precios en {zona}")
st.bar_chart(filtrado['room_type'].value_counts())

st.subheader("Histograma de precios")
fig, ax = plt.subplots()
filtrado['price'].hist(ax=ax, bins=50)
st.pyplot(fig)

st.subheader("Top alojamientos más rentables")
st.dataframe(filtrado.sort_values(by='estimated_income', ascending=False).head(10))
