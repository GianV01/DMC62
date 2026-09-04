import streamlit as st
st.title ("Especialización Pyhton for Analitycs")
st.sidebar.title("Parametros de Ingreso")
st.write("Elaborado por: Giancarlo Valdivia")

modulos = st.sidebar.selectbox ("Seleccione el módulo",["Listas","Arreglos","Funciones","POO"])
