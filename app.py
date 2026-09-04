import streamlit as st
st.title ("Especialización Pyhton for Analitycs")
st.sidebar.title("Parametros de Ingreso")
st.write("Elaborado por: Giancarlo Valdivia")

modulos = st.sidebar.selectbox ("Seleccione el módulo",["Listas","Arreglos","Funciones","POO"])

if modulos == "Listas":
  st.write("Te encuentras en el modulo de listas")
  
  valor_inicial = st.number_input("Ingrese tu valor inicial del rango", value = 0)
  valor_final = st.number_input("Ingrese tu valor final del rango", value = 10)

  lista == list(range(valor_inicial,valor_final))

st.write(lista)

elif modulos == "Arreglos":
  st.write("Te encuentras en el modulo arreglos")

elif modulos == "Funciones":
  st.write("Te encuentras en el modulo funciones")

else:
  st.write("Te encuentras en el modulo POO")
