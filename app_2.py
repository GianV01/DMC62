import streamlit as st

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if secciones == "Home":
    st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT",text_alignment="center")
    st.divider()
 
    col1, col2 = st.columns(2)

    with col1:
        
        _, subcol_img1, _ = st.columns([1, 2, 1])
        with subcol_img1:
            st.image("DMC.png", width=150)

    with col2:
        _, subcol_img2, _ = st.columns([1, 2, 1])
        with subcol_img2:
            st.image("python_logo.png", width=250)

    st.divider()
                        
    st.subheader(" Módulo 1 – Python Fundamentals ",text_alignment="center")
    st.divider()

    st.markdown("Se va a desarrollar una aplicación interactiva haciendo uso de las plataformas GitHub y Streamlit, integrando los contenidos revisados en el módulo.",text_alignment="justify")
    st.divider()

    st.subheader(" Tecnologias Utilizadas ",text_alignment="center")

    col3, col4, col5, col6 = st.columns(4)

    with col3:
        with st.container(border=True):
            st.markdown(" **Python** ",text_alignment="center")

    with col4:
        with st.container(border=True):
            st.markdown(" **GitHub** ",text_alignment="center")

    with col5:
        with st.container(border=True):
            st.markdown(" **Streamlit** ",text_alignment="center")

    with col6:
        with st.container(border=True):
            st.markdown(" **Librerias** ",text_alignment="center")

    st.divider()

    st.subheader("Giancarlo Esteban Valdivia Asencio",text_alignment="center")
    st.divider()

    st.markdown("Bachiller en la carrera de Ingenieria de Sistemas e Informatica, egresado de la universidad Tecnologica del Perú en el año 2025 cuento con 4 años de experiencia laboral entre practicas pre-profesionales,practicas profesionales y puestos laborales directos, actualmente me encuentro laborando en la empresa Molitalia, y mi interesa seguir formandome en la administracion de data.",text_alignment="justify")
    st.divider()

    st.subheader(" 2026 ",text_alignment="center")
elif secciones == "Ejercicio 1":
    st.title("Ejercicio 1 - Movimientos Diaros",text_alignment="center")
    st.divider()
    st.markdown("En este ejercicio se desarrollara una app para el ingreso de movimientos categorizados por ingreso o gasto, esto con el fin de ayudar al usuario a tener un mejor control de sus movimientos financieros diarios o mensuales. Al finalizar se mostrará el detalle de sus movimientos en un listado y su saldo final, indicando si aun tiene un salgo a favor o negativo.",text_alignment="justify")
    st.divider()

    def ejercicio_1():

        if"movimientos" not in st.session_state:
            st.session_state.movimientos = []

    concepto = st.text_input("Concepto:")
    tipo = st.selectbox("Tipo de Movimiento:" , ["Ingreso","Gasto"])
    valor = st.number_input("Valor:", min_value=0.0,format="%.2f")

    if st.button("Agregar Movimiento"):
        if concepto.strip() != "" and valor > 0:
            st.session_state.movimiento.append({"concepto": concepto, "tipo": tipo, "valor": valor})
            
            if st.session_state.movimientos:
                st.dataframe(st.session_state.movimientos)
                        
        total_ingresos = sum(
            m["valor"]
            for m in st.session_state.movimientos
            if m["tipo"] == "Ingreso"
        )
        total_gastos = sum(
            m["valor"]
            for m in st.session_state.movimientos
            if m["tipo"] == "Gasto"
        )
        saldo_final = total_ingresos - total_gastos
        
        st.metric("Total Ingresos", f"${total_ingresos:,.2f}")
        st.metric("Total Gastos", f"${total_gastos:,.2f}")
        st.metric("Saldo Final", f"${saldo_final:,.2f}")

        
        if saldo_final > 0:
            st.success("El flujo de caja está a favor.")
        elif saldo_final < 0:
            st.error("El flujo de caja está en contra.")
        else:
            st.success("El flujo de caja está en equilibrio.")
            
            mostrar_ejericio_1() 

    st.subheader(" Elaborado por Giancarlo Valdivia ",text_alignment="center")

elif secciones == "Ejercicio 2":
    st.title("FORMULARIO DE REGISTRO", text_alignment="center")
    st.divider()

elif secciones == "Ejercicio 3":
    st.title(".....", text_alignment="center")
    st.divider()

else: 
    st.title(".....", text_alignment="center")
    st.divider()


  


  











