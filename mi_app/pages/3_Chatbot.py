
import streamlit as st
from utils.chatbot import responder

st.title("🤖 Chatbot Asistente")
mensaje = st.text_input("Escribe tu pregunta...")

if mensaje:
    respuesta = responder(mensaje)
    st.write(f"🧠 Chatbot: {respuesta}")
