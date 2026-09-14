import streamlit as st

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

import streamlit as st

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if secciones == "Home":
    st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT")
    st.divider()
 
    col1, col2 = st.columns(2)

    with col1:
        st.image("DMC.png", width=150)

    with col2:
        st.image("python_logo.png", width=200)

    st.divider()
                        
    st.subheader(" Módulo 1 – Python Fundamentals ")
    st.divider()

    st.markdown("Se va a desarrollar una aplicación interactiva haciendo uso de las plataformas GitHub y Streamlit, integrando los contenidos revisados en el módulo.")
    st.divider()

    st.subheader(" Tecnologias Utilizadas ")

    col3, col4, col5, col6 = st.columns(4)

    with col3:
        with st.container(border=True):
            st.markdown(" **Python** ")

    with col4:
        with st.container(border=True):
            st.markdown(" **GitHub** ")

    with col5:
        with st.container(border=True):
            st.markdown(" **Streamlit** ")

    with col6:
        with st.container(border=True):
            st.markdown(" **Librerias** ")

    st.divider()

    st.subheader(" Elaborado por Giancarlo Esteban Valdivia Asencio")
    st.divider()

    st.markdown("Bachiller en la carrera de Ingenieria de Sistemas e Informatica, egresado de la universidad Tecnologica del Perú en el año 2025 cuento con 4 años de experiencia laboral entre practicas pre-profesionales, practicas profesionales y puestos laborales directos, actualmente me encuentro laborando en la empresa Molitalia, y mi interesa seguir formandome en la administracion de data.")
    st.divider()

    st.subheader(" 2026 ")

elif secciones == "Ejercicio 1":
    st.write("Te encuentras en el ejercicio 1")

elif secciones == "Ejercicio 1":
  st.write ("Te encuentras en home")

elif secciones == "Ejercicio 2":
  st.write ("Te encuentras en home")

elif secciones == "Ejercicio 3":
  st.write ("Te encuentras en home")

else: 
  st.write ("Te encuentras en home")


  


  











