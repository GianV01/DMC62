import streamlit as st

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if secciones == "Home":
    st.markdown("<h1 style='text-align: center;'>PROYECTO 1 – APLICACIÓN EN STREAMLIT</h1>", unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.image("DMC.png", width=150)

    with col2:
        st.image("python_logo.png", width=200)

    st.divider()

    st.markdown("<h3 style='text-align: center;'>Módulo 1 – Python Fundamentals</h3>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<p style='text-align: center;'>Se va a desarrollar una aplicación interactiva haciendo uso de las plataformas GitHub y Streamlit, integrando los contenidos revisados en el módulo.</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<h3 style='text-align: center;'>Tecnologias Utilizadas</h3>", unsafe_allow_html=True)

    col3, col4, col5, col6 = st.columns(4)

    with col3:
        with st.container(border=True):
            st.markdown("<p style='text-align: center;'><b>Python</b></p>", unsafe_allow_html=True)

    with col4:
        with st.container(border=True):
            st.markdown("<p style='text-align: center;'><b>GitHub</b></p>", unsafe_allow_html=True)

    with col5:
        with st.container(border=True):
            st.markdown("<p style='text-align: center;'><b>Streamlit</b></p>", unsafe_allow_html=True)

    with col6:
        with st.container(border=True):
            st.markdown("<p style='text-align: center;'><b>Librerias</b></p>", unsafe_allow_html=True)

    st.divider()

    st.markdown("<h3 style='text-align: center;'>Elaborado por Giancarlo Esteban Valdivia Asencio</h3>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<p style='text-align: justify;'>Bachiller en la carrera de Ingenieria de Sistemas e Informatica, egresado de la universidad Tecnologica del Perú en el año 2025 cuento con 4 años de experiencia laboral entre practicas pre-profesionales, practicas profesionales y puestos laborales directos, actualmente me encuentro laborando en la empresa Molitalia, y mi interesa seguir formandome en la administracion de data.</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<h3 style='text-align: center;'>2026</h3>", unsafe_allow_html=True)

elif secciones == "Ejercicio 1":
    st.write("Te encuentras en el ejercicio 1")










