import streamlit as st

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo",["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3","Ejercicio 4"])

if secciones == "Home":
  st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT")
 
col1, col3 = st.columns(2)

with col1:
  with st.container(horizontal_alignment="center"):
    st.image("DMC.png", width=150)

with col3:
  st.image("python_logo.png",width="stretch")


