import streamlit as st

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo",["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3","Ejercicio 4"])

if secciones == "Home":
  st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT")
  st.header("PROYECTO 1 – APLICACIÓN EN STREAMLIT")
