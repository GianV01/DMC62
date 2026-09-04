import streamlit as st
st.title ("Especialización Pyhton for Analitycs")
st.sidebar.title("Parametros de Ingreso")
st.write("Elaborado por: Giancarlo Valdivia")

modulos = st.sidebar.selectbox ("Seleccione el módulo",["Listas","Arreglos","Funciones","POO"])

if modulos == "Listas":
  st.write("Te encuentras en el modulo de listas")

elif modulos == "Arreglos":
  st.write("Te encuentras en el modulo arreglos")

elif modulos == "Funciones":
  st.write("Te encuentras en el modulo Funciones")

else:
  st.write("No te encuentrsa en ningun codigo")
