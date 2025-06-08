
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard de Indicadores")

df = pd.DataFrame({
    "Fecha": pd.date_range("2024-01-01", periods=6, freq="M"),
    "Valor": [100, 120, 90, 110, 130, 125],
    "Indicador": ["Ventas"] * 6
})

fig = px.line(df, x="Fecha", y="Valor", color="Indicador")
st.plotly_chart(fig, use_container_width=True)
