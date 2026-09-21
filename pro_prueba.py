import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lfp
import librería_clases_proyecto1 as lcp

# 1. st.set_page_config DEBE ser el primer comando de Streamlit
st.set_page_config(page_title="Proyecto 1 - Aplicación", page_icon="🚀", layout="wide")

# 2. Inyección de CSS (HTML + CSS) para diseño vanguardista
def aplicar_estilos_vanguardistas():
    estilo_css = """
    <style>
    /* Tema general y Fondo */
    .stApp {
        background-color: #0f172a;
        background-image: radial-gradient(circle at top right, #1e293b 0%, #0f172a 70%);
        color: #e2e8f0;
    }
    
    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }

    /* Títulos con efecto Neon */
    h1, h2, h3 {
        color: #38bdf8 !important;
        text-shadow: 0px 0px 8px rgba(56, 189, 248, 0.5);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Campos de entrada e interactividad (Hover y Focus) */
    div[data-baseweb="select"] > div, 
    input[type="text"], 
    input[type="number"],
    div[data-baseweb="base-input"] {
        background-color: #1e293b !important;
        color: #f8fafc !important;
        border: 1px solid #475569 !important;
        border-radius: 8px !important;
        transition: all 0.3s ease-in-out !important;
    }

    /* Efecto al pasar el cursor (Interactivo) */
    div[data-baseweb="select"] > div:hover, 
    input[type="text"]:hover, 
    input[type="number"]:hover {
        border-color: #38bdf8 !important;
        box-shadow: 0px 0px 10px rgba(56, 189, 248, 0.4) !important;
        transform: scale(1.01);
    }
    
    /* Efecto al seleccionar/escribir (Interactivo) */
    div[data-baseweb="select"] > div:focus-within, 
    input[type="text"]:focus, 
    input[type="number"]:focus {
        border-color: #818cf8 !important;
        box-shadow: 0px 0px 15px rgba(129, 140, 248, 0.6) !important;
        transform: scale(1.03);
    }

    /* Botones Vanguardistas */
    .stButton > button, button[kind="secondaryFormSubmit"] {
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%) !important;
        color: #0f172a !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.2rem !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover, button[kind="secondaryFormSubmit"]:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0px 8px 20px rgba(129, 140, 248, 0.5) !important;
        color: #ffffff !important;
    }

    /* Contenedores y Tarjetas */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 12px !important;
        border: 1px solid #334155 !important;
        background-color: #1e293b !important;
        transition: transform 0.3s, box-shadow 0.3s !important;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 20px rgba(56, 189, 248, 0.15) !important;
    }

    /* Separadores */
    hr {
        border-color: #334155 !important;
    }
    </style>
    """
    st.markdown(estilo_css, unsafe_allow_html=True)

# Aplicar los estilos
aplicar_estilos_vanguardistas()

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if secciones == "Home":
    st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT", anchor=False)
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
                        
    st.subheader(" Módulo 1 – Python Fundamentals ", anchor=False)
    st.divider()

    st.markdown("Se va a desarrollar una aplicación interactiva haciendo uso de las plataformas GitHub y Streamlit, integrando los contenidos revisados en el módulo.")
    st.divider()

    st.subheader(" Tecnologías Utilizadas ", anchor=False)

    col3, col4, col5, col6 = st.columns(4)

    with col3:
        with st.container(border=True):
            st.markdown("<h4 style='text-align: center; color: white;'>Python</h4>", unsafe_allow_html=True)

    with col4:
        with st.container(border=True):
            st.markdown("<h4 style='text-align: center; color: white;'>GitHub</h4>", unsafe_allow_html=True)

    with col5:
        with st.container(border=True):
            st.markdown("<h4 style='text-align: center; color: white;'>Streamlit</h4>", unsafe_allow_html=True)

    with col6:
        with st.container(border=True):
            st.markdown("<h4 style='text-align: center; color: white;'>Librerias</h4>", unsafe_allow_html=True)

    st.divider()

    st.subheader("Giancarlo Esteban Valdivia Asencio", anchor=False)
    st.divider()

    st.markdown("Bachiller en la carrera de Ingenieria de Sistemas e Informatica, egresado de la universidad Tecnologica del Perú en el año 2025 cuento con 4 años de experiencia laboral entre practicas pre-profesionales,practicas profesionales y puestos laborales directos, actualmente me encuentro laborando en la empresa Molitalia, y mi interesa seguir formandome en la administracion de data.")
    st.divider()

    st.subheader(" 2026 ", anchor=False)

elif secciones == "Ejercicio 1":
    st.title(" 💰 Ejercicio 1 - Movimientos Diarios", anchor=False)
    st.divider()
    st.markdown("En este ejercicio se desarrollara una app para el ingreso de movimientos categorizados por ingreso o gasto, esto con el fin de ayudar al usuario a tener un mejor control de sus movimientos financieros diarios o mensuales. Al finalizar se mostrará el detalle de sus movimientos en un listado y su saldo final, indicando si aun tiene un salgo a favor o negativo.")
    st.divider()

    def ejercicio_1():
        if "movimientos" not in st.session_state:
            st.session_state.movimientos = []

        col1, col2 = st.columns(2)
        with col1:
            concepto = st.text_input("Concepto:")
            tipo = st.selectbox("Tipo de Movimiento:", ["Ingreso", "Gasto"])
        with col2:
            valor = st.number_input("Valor:", min_value=0.0, format="%.2f")

        if st.button("Agregar Movimiento"):
            if concepto.strip() != "" and valor > 0:
                st.session_state.movimientos.append({
                    "concepto": concepto,
                    "tipo": tipo,
                    "valor": valor
                })

        if st.session_state.movimientos:
            st.dataframe(st.session_state.movimientos, use_container_width=True)

            total_ingresos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Ingreso")
            total_gastos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Gasto")
            saldo_final = total_ingresos - total_gastos

            m1, m2, m3 = st.columns(3)
            m1.metric("Total Ingresos", f"S/{total_ingresos:,.2f}")
            m2.metric("Total Gastos", f"S/{total_gastos:,.2f}")
            m3.metric("Saldo Final", f"S/{saldo_final:,.2f}")

            if saldo_final > 0:
                st.success("Tu saldo está a favor.")
            elif saldo_final < 0:
                st.error("Tu saldo está en contra.")
            else:
                st.success("Tu saldo está en equilibrio.")
    
    ejercicio_1()
    st.divider()
    st.markdown("<p style='text-align: center; color: #818cf8;'><strong>No ahorres lo que queda después de gastar, gasta lo que queda después de ahorrar</strong></p>", unsafe_allow_html=True)

elif secciones == "Ejercicio 2":
    st.title(" 🧾 Ejercicio 2 - Módulo de Ventas", anchor=False)
    st.divider()
    st.markdown("En este ejercicio se desarrollará un modulo de ventas de productos en la que se solicitará al operario el ingreso de nombre, categoria, precio, cantidad y total, esto con el fin de tener un calculo exacto de la venta a realizar. Al finalizar se mostrará el detalle de la compra y el monto total a pagar por parte del cliente.")
    st.divider()

    def ejercicio_2():
        if "array_productos" not in st.session_state:
            st.session_state.array_productos = np.array([], dtype=object)
            st.session_state.array_categorias = np.array([], dtype=object)
            st.session_state.array_precios = np.array([], dtype=float)
            st.session_state.array_cantidades = np.array([], dtype=int)
            st.session_state.array_totales = np.array([], dtype=float)

        st.markdown("### Ingrese el Producto")
        
        with st.form("form_registro_producto", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                producto = st.text_input("Nombre del Producto")
                categoria = st.selectbox("Categoría", ["Electrónica", "Abarrotes", "Ropa", "Hogar", "Otros"])
            with col2:
                precio = st.number_input("Precio (S/)", min_value=0.0, value=0.0, step=0.50)
                cantidad = st.number_input("Cantidad", min_value=1, value=1, step=1)
                
            btn_agregar = st.form_submit_button("Agregar Producto")

        if btn_agregar:
            if not producto.strip():
                st.error("⚠️ El **Nombre del Producto** es obligatorio.")
            elif categoria == "-- Selecciona una categoría --":
                st.error("⚠️ Debes seleccionar una **Categoría** válida.")
            elif precio <= 0:
                st.error("⚠️ El **Precio** debe ser mayor a 0.")
            elif cantidad <= 0:
                st.error("⚠️ La **Cantidad** debe ser mayor a 0.")
            else:
                total = precio * cantidad
                
                st.session_state.array_productos = np.append(st.session_state.array_productos, producto)
                st.session_state.array_categorias = np.append(st.session_state.array_categorias, categoria)
                st.session_state.array_precios = np.append(st.session_state.array_precios, precio)
                st.session_state.array_cantidades = np.append(st.session_state.array_cantidades, cantidad)
                st.session_state.array_totales = np.append(st.session_state.array_totales, total)
                
                st.success(f"Producto '{producto}' agregado correctamente.")
            
        st.markdown("### Productos Registrados")
        if len(st.session_state.array_productos) > 0:
            df_registros = pd.DataFrame({
                "Producto": st.session_state.array_productos,
                "Categoría": st.session_state.array_categorias,
                "Precio Unitario": st.session_state.array_precios,
                "Cantidad": st.session_state.array_cantidades,
                "Total": st.session_state.array_totales
            })
            
            st.dataframe(df_registros, use_container_width=True)
            
            st.markdown("### Resumen de Compra")
            col_m1, col_m2 = st.columns(2)
            col_m1.metric("Total de Productos Registrados", len(df_registros))
            col_m2.metric("Monto Total", f"S/{df_registros['Total'].sum():,.2f}")
        else:
            st.info("Aún no se han agregado registros. Completa el formulario arriba para empezar.")
            
    ejercicio_2()
    st.divider()
    st.markdown("<p style='text-align: center; color: #818cf8;'><strong>Lo que no se mide, no se controla; lo que no se controla, no mejora.</strong></p>", unsafe_allow_html=True)

elif secciones == "Ejercicio 3":
    st.title(" 🖥️ Ejercicio 3 - Cálculo de Almacenamiento", anchor=False)
    st.divider()
    st.markdown("Esta herramienta permite calcular el **almacenamiento estimado necesario para respaldos** en función de la cantidad de usuarios, y la cantidad de archivos a respaldar.")
    st.divider()

    if "historial_calculos" not in st.session_state:
        st.session_state.historial_calculos = []

    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            numero_usuarios = st.number_input("Número de Usuarios", min_value=1, value=1, step=1)
            archivos_por_usuario = st.number_input("Archivos por Usuario", min_value=1, value=10, step=5)
            
        with col2:
            tamano_promedio_mb = st.number_input("Tamaño Promedio por Archivo (MB)", min_value=0.1, value=5.0, step=0.5)
            factor_respaldo = st.number_input("Factor de Respaldo", min_value=1.0, value=1.5, step=0.1)
            
        btn_ejecutar = st.button("Ejecutar Cálculo")

    if btn_ejecutar:
        calculo_alm = lfp.calcular_almacenamiento_respaldo(numero_usuarios, archivos_por_usuario, tamano_promedio_mb, factor_respaldo)
        st.success(f"**El cálculo de almacenamiento de respaldo estimado es:** {calculo_alm}")
        st.session_state.historial_calculos.append(calculo_alm)

    if st.session_state.historial_calculos:
        st.markdown("### Histórico de Resultados:")
        df_resultados = pd.DataFrame(st.session_state.historial_calculos)
        st.dataframe(df_resultados, use_container_width=True)

    st.divider()
    st.markdown("<p style='text-align: center; color: #818cf8;'><strong>Simplifica tus procesos, potencia tus resultados.</strong></p>", unsafe_allow_html=True)
    
else:
    st.title(" ⚙️ Ejercicio 4 - Operatividad de Servidor", anchor=False)
    st.divider()
    st.markdown("Este módulo define la entidad del servidor mediante sus atributos clave como: identificador, tiempos operativos y capacidades de disco. A partir de estas variables, el código calcula dinámicamente el porcentaje de disponibilidad restando el tiempo de caída al total, evalúa la ocupación del espacio y genera un diagnóstico del estado general del sistema.")
    st.divider()
    
    if "servidores" not in st.session_state:
        st.session_state.servidores = {"Servidor-01": lcp.Servidor("Servidor-01", 720, 10, 1000, 800)}

    tab_read, tab_create, tab_update, tab_delete = st.tabs(["📋 Leer", "➕ Crear", "✏️ Actualizar", "🗑️ Eliminar"])

    with tab_read:
        if not st.session_state.servidores:
            st.info("No hay servidores registrados.")
        else:
            datos = [s.resumen() for s in st.session_state.servidores.values()]
            st.dataframe(pd.DataFrame(datos), use_container_width=True)

    with tab_create:
        with st.container(border=True):
            nombre = st.text_input("Nombre del servidor")
            c1, c2 = st.columns(2)
            with c1:
                tiempo_total = st.number_input("Tiempo Total (Horas)", min_value=1.0, value=720.0)
                tiempo_caida = st.number_input("Tiempo Caída (Horas)", min_value=0.0, value=0.0)
            with c2:
                almacenamiento_total = st.number_input("Almacenamiento Total (GB)", min_value=1.0, value=500.0)
                almacenamiento_usado = st.number_input("Almacenamiento Usado (GB)", min_value=0.0, value=100.0)

            if st.button("Guardar Servidor"):
                if not nombre.strip():
                    st.error("Ingresa un nombre válido.")
                elif nombre in st.session_state.servidores:
                    st.error("El servidor ya existe.")
                else:
                    try:
                        nuevo = lcp.Servidor(nombre.strip(), tiempo_total, tiempo_caida, almacenamiento_total, almacenamiento_usado)
                        st.session_state.servidores[nuevo.nombre] = nuevo
                        st.success(f"Servidor '{nuevo.nombre}' creado.")
                        st.rerun()
                    except ValueError as e:
                        st.error(f"Error: {e}")
    
    with tab_update:
        if not st.session_state.servidores:
            st.info("No hay servidores para actualizar.")
        else:
            with st.container(border=True):
                seleccion = st.selectbox("Selecciona servidor a modificar:", list(st.session_state.servidores.keys()), key="sb_upd")
                actual = st.session_state.servidores[seleccion]
        
                c3, c4 = st.columns(2)
                with c3:
                    tt = st.number_input("Tiempo Total (Horas)", min_value=1.0, value=float(actual.tiempo_total_h), key="u_tt")
                    tc = st.number_input("Tiempo Caída (Horas)", min_value=0.0, value=float(actual.tiempo_caida_h), key="u_tc")
                with c4:
                    at = st.number_input("Almacenamiento Total (GB)", min_value=1.0, value=float(actual.almacenamiento_total_gb), key="u_at")
                    au = st.number_input("Almacenamiento Usado (GB)", min_value=0.0, value=float(actual.almacenamiento_usado_gb), key="u_au")
        
                if st.button("Actualizar Registro"):
                    try:
                        st.session_state.servidores[seleccion] = lcp.Servidor(seleccion, tt, tc, at, au)
                        st.success(f"Servidor '{seleccion}' actualizado.")
                        st.rerun()
                    except ValueError as e:
                        st.error(f"Error: {e}")
    
    with tab_delete:
        if not st.session_state.servidores:
            st.info("No hay servidores para eliminar.")
        else:
            with st.container(border=True):
                a_borrar = st.selectbox("Selecciona servidor a eliminar:", list(st.session_state.servidores.keys()), key="sb_del")
                
                if st.button("Eliminar Servidor"):
                    del st.session_state.servidores[a_borrar]
                    st.success(f"Servidor '{a_borrar}' eliminado.")
                    st.rerun()
    
    st.divider()
    st.markdown("<p style='text-align: center; color: #818cf8;'><strong>Simplifica tus procesos, potencia tus resultados.</strong></p>", unsafe_allow_html=True)