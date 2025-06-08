
import streamlit as st
from utils.db import guardar_usuario

st.title("📝 Registro de Usuarios")
nombre = st.text_input("Nombre")
email = st.text_input("Correo electrónico")
rol = st.selectbox("Rol", ["Usuario", "Administrador"])

if st.button("Registrar"):
    guardar_usuario(nombre, email, rol)
    st.success("Usuario registrado correctamente.")
