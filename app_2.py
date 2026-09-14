import streamlit as st

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if secciones == "Home":
  st.write ("Te encuentras en home")
  st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT",text_alignment="center")
  st.divider()
 
col1, col2 = st.columns(2)

with col1:
  with st.container(horizontal_alignment="center"):
    st.image("DMC.png", width=150)

with col2:
  with st.container(horizontal_alignment="center"):
    st.image("python_logo.png",width=200)

st.divider()

elif secciones == "Ejercicio 1":
  st.write ("Te encuentras en home")

elif secciones == "Ejercicio 2":
  st.write ("Te encuentras en home")

elif secciones == "Ejercicio 3":
  st.write ("Te encuentras en home")

else: 
  st.write ("Te encuentras en home")


  


  











