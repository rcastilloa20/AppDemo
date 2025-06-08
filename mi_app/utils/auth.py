
import streamlit as st

def login():
    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if user == "admin" and password == "123":
            st.success("Bienvenido")
            return {"usuario": user}
        else:
            st.error("Credenciales inválidas")
    return None
