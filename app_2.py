import streamlit as st

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo",["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3","Ejercicio 4"])

if secciones == "Home":
  st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT")
 
col1, col2, col3 = st.columns(3)

with col1:
  st.image("DMC.png")

with col2:
    
    st.image("")

with col3:
  st.image("python_logo.png")
