import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Título principal
st.title("Dashboard de Indicadores Económicos de Chile")

# Sidebar
st.sidebar.title("Configuración")

# Selector de indicador
indicador = st.sidebar.selectbox(
    "Seleccione un indicador",
    ["dolar", "euro", "uf", "bitcoin"]
)

# URL dinámica
url = f"https://mindicador.cl/api/{indicador}"

# Obtener datos
respuesta = requests.get(url)

datos = respuesta.json()

# Crear DataFrame
df = pd.DataFrame(datos["serie"])

# Mostrar información
st.subheader(f"Datos de {indicador.upper()}")

st.write(df)

# Calcular estadísticas
promedio = df["valor"].mean()

maximo = df["valor"].max()

minimo = df["valor"].min()

# Mostrar métricas
col1, col2, col3 = st.columns(3)

col1.metric("Promedio", round(promedio, 2))

col2.metric("Máximo", round(maximo, 2))

col3.metric("Mínimo", round(minimo, 2))

# Crear gráfico
fig, ax = plt.subplots()

ax.plot(df["fecha"], df["valor"])

ax.set_title(f"Evolución de {indicador}")

ax.set_xlabel("Fecha")

ax.set_ylabel("Valor")

plt.xticks(rotation=45)

# Mostrar gráfico
st.pyplot(fig)