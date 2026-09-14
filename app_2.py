import streamlit as st

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo",["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3","Ejercicio 4"])

if secciones == "Home":
  st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT",text_alignment="center")
  st.divider()
 
col1, col3 = st.columns(2)

with col1:
  with st.container(horizontal_alignment="center"):
    st.image("DMC.png", width=150)

with col3:
  st.image("python_logo.png",width="stretch")

st.divider()
                        
st.subheader (" Módulo 1 – Python Fundamentals ", text_alignment="center")

st.divider()

texto1 = ""Se va a desarrollar una aplicación interactiva dentro haciendo uso de las plataformas GitHub y Streamlit,  
integrando los contenidos revisados en el módulo.""

st.markdown(texto1, text_alignment="justify")

st.divider()

st.subheader (" Elaborado por Giancarlo Esteban Valdivia Asencio", text_alignment="center")

st.divider()

st.markdown ("Bachiller en la carrera de Ingenieria de Sistemas e Informatica, egresado de la universidad Tecnologica del Perú en el año 2025 cuento con 4 años de experiencia laboral entre practicas pre-profesionales, practicas profesionales y puestos laborales directos,actualmente me encuentro laborando en la empresa Molitalia, y mi interesa seguir formandome en la administracion de data. ", text_alignment= "justify")

st.divider()

st.subheader (" 2026 ", text_alignment="center")

st.divider()



