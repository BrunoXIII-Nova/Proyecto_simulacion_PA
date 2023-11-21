import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Diccionario de archivos de Excel y sus respectivos nombres de columnas
archivos_excel = {
    "Libro1.xlsx": ['Frecuencia con la que lees', 'de 1 a 7'],
    "Libro2.xlsx": ['Columna1', 'Columna2'],
    "Libro3.xlsx": ['ColumnaA', 'ColumnaB'],
    "Libro4.xlsx": ['ColumnaX', 'ColumnaY']
}

# Crear un cuadro combinado para seleccionar el archivo de Excel
archivo_seleccionado = st.selectbox("Selecciona un archivo de Excel", list(archivos_excel.keys()))

# Leer el archivo de Excel seleccionado
df = pd.read_excel(f"{archivo_seleccionado}", names=archivos_excel[archivo_seleccionado])

# Mostrar el DataFrame completo en Streamlit
st.dataframe(df)

df.plot(kind='bar')
st.pyplot(plt)
