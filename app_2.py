import streamlit as st

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo",["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3","Ejercicio 4"])

if secciones == "Home":
  st.write ("Te encuentras en Home")

elif secciones == "Ejercicio 1":
  st.write ("Te encuentras en el Ejercicio 1")

elif secciones == "Ejercicio 2":
  st.write ("Te encuentras en el Ejercicio 2")

elif secciones == "Ejercicio 3":
  st.write ("Te encuentras en el Ejercicio 3")

else:

  st.write ("Te encuentras en el ejercicio 4")
  











