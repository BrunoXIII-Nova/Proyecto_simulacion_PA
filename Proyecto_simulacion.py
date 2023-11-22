import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Diccionario de archivos de Excel y sus respectivos nombres de columnas
archivos_excel = {
    "Encuesta 1": {"file": "Libro1.xlsx", "columns": ['Frecuencia con la que lees', 'de 1 a 7']},
    "Encuesta 2": {"file": "Libro2.xlsx", "columns": ['¿Sabes leer y escribir en castellano?', 'de 1 a 2']},
    "Encuesta 3": {"file": "Libro3.xlsx", "columns": ['¿Con qué frecuencia Realizaron la actividad de: Contar relatos, cuentos, historias?', 'de 1 a 3']},
    "Encuesta 4": {"file": "Libro4.xlsx", "columns": ['Número de computadoras/laptops en el hogar', 'de 1 a 10']},
    "Encuesta 5": {"file": "Libro5.xlsx", "columns": ['Número de libros impresos en el hogar', '(0:5000)']}
}

st.title('Encuesta Nacional de Lectura')

# combobox
encuesta_seleccionada = st.selectbox("Selecciona una encuesta a continuación", list(archivos_excel.keys()))

# filas y columnas del grafico
archivo_seleccionado = archivos_excel[encuesta_seleccionada]["file"]
columnas_seleccionadas = archivos_excel[encuesta_seleccionada]["columns"]

# Se lee el archivo excel que seleccionamos
df = pd.read_excel(f"{archivo_seleccionado}", names=columnas_seleccionadas, index_col=0)

# Se muestras en la pagina
st.dataframe(df)

# Si la encuesta seleccionada es la "Encuesta 5", utilizar un histograma
if encuesta_seleccionada == "Encuesta 5":
    df.hist(bins=50)
else:
    df.plot(kind='bar')

st.pyplot(plt)
