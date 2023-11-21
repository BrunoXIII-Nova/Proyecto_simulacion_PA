import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Diccionario de archivos de Excel y sus respectivos nombres de columnas
archivos_excel = {
    "Libro1.xlsx": ['Frecuencia con la que lees', 'de 1 a 7'],
    "Libro2.xlsx": ['¿Sabes leer y escribir en castellano?', 'de 1 a 2'],
    "Libro3.xlsx": ['¿Con qué frecuencia Realizaron la actividad de: Contar relatos, cuentos, historias?', 'de 1 a 3'],
    "Libro4.xlsx": ['Número de computadoras/laptops en el hogar', 'de 1 a 10']
}

# Crear un cuadro combinado para seleccionar el archivo de Excel
archivo_seleccionado = st.selectbox("Selecciona un archivo de Excel", list(archivos_excel.keys()))

# Leer el archivo de Excel seleccionado
df = pd.read_excel(f"{archivo_seleccionado}", names=archivos_excel[archivo_seleccionado],index_col=list(archivos_excel.keys()[0])

# Mostrar el DataFrame completo en Streamlit
st.dataframe(df)

df.plot(kind='bar')
st.pyplot(plt)
