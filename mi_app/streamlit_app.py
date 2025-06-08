
import streamlit as st
from utils.auth import login

st.set_page_config(page_title="Mi App", layout="wide")

user = login()

if user:
    st.sidebar.title("Navegación")
    st.sidebar.page_link("pages/1_Registro.py", label="Registro de usuarios")
    st.sidebar.page_link("pages/2_Seguimiento.py", label="Seguimiento")
    st.sidebar.page_link("pages/3_Chatbot.py", label="Chatbot")
    st.sidebar.page_link("pages/4_Dashboard.py", label="Dashboard")
    st.sidebar.page_link("pages/5_Ayuda.py", label="Ayuda")
else:
    st.warning("Debes iniciar sesión para continuar.")
