import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lfp
import librería_clases_proyecto1 as lcp

# 1. Configuración inicial
st.set_page_config(page_title="Proyecto 1 - Aplicación", page_icon="🚀", layout="wide")

# 2. Paleta de colores racionalizada para legibilidad
COLOR_CHARCOAL = "#2F3133"  # Fondo principal (Oscuro)
COLOR_BLUE_GREY = "#4A5A6A" # Barra lateral (Intermedio)
COLOR_BEIGE = "#E6D8C6"     # Textos principales (Claro - Alto contraste)
COLOR_BRONZE = "#A07B5C"    # Títulos y acentos
COLOR_OLIVE = "#7B8A74"     # Botones y elementos activos

# 3. Función auxiliar para centralizar textos
def texto_centrado(texto, etiqueta="h1", color=COLOR_BEIGE, size=None):
    size_style = f"font-size: {size};" if size else ""
    html = f"""
        <div style='text-align: center; width: 100%; margin-bottom: 1rem;'>
            <{etiqueta} style='color: {color}; {size_style} text-shadow: 1px 1px 2px rgba(0,0,0,0.5); font-family: "Segoe UI", sans-serif;'>
                {texto}
            </{etiqueta}>
        </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# 4. Inyección de CSS Vanguardista y Menú de Bloques
def inyectar_estilos():
    css = f"""
    <style>
    /* Fondo principal y color de texto por defecto */
    .stApp {{
        background-color: {COLOR_CHARCOAL};
        color: {COLOR_BEIGE};
    }}
    
    /* Barra lateral */
    [data-testid="stSidebar"] {{
        background-color: {COLOR_BLUE_GREY} !important;
        border-right: 2px solid {COLOR_BRONZE};
    }}
    
    /* === INNOVACIÓN DEL MENÚ LATERAL (Radio a Botones en Bloque) === */
    div[role="radiogroup"] > label > div:first-child {{
        display: none !important; /* Oculta el círculo del radio button */
    }}
    div[role="radiogroup"] > label {{
        background-color: {COLOR_CHARCOAL} !important;
        color: {COLOR_BEIGE} !important;
        padding: 12px 20px !important;
        border-radius: 8px !important;
        margin-bottom: 10px !important;
        border: 1px solid {COLOR_OLIVE} !important;
        transition: all 0.3s ease !important;
        cursor: pointer;
        display: flex;
        justify-content: center;
        text-align: center;
    }}
    div[role="radiogroup"] > label:hover {{
        background-color: {COLOR_BRONZE} !important;
        color: {COLOR_CHARCOAL} !important;
        transform: translateX(5px);
    }}
    div[role="radiogroup"] > label[data-checked="true"] {{
        background-color: {COLOR_OLIVE} !important;
        color: {COLOR_CHARCOAL} !important;
        font-weight: bold !important;
        border-color: {COLOR_BEIGE} !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }}
    /* =============================================================== */

    /* Estilos de inputs (Interactividad visual) */
    div[data-baseweb="select"] > div, 
    input[type="text"], 
    input[type="number"],
    div[data-baseweb="base-input"] {{
        background-color: rgba(74, 90, 106, 0.4) !important;
        color: {COLOR_BEIGE} !important;
        border: 1px solid {COLOR_BRONZE} !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }}

    /* Efectos Hover y Focus en inputs */
    div[data-baseweb="select"] > div:hover, 
    input[type="text"]:hover, 
    input[type="number"]:hover {{
        border-color: {COLOR_OLIVE} !important;
        box-shadow: 0 0 10px rgba(123, 138, 116, 0.4) !important;
    }}
    
    div[data-baseweb="select"] > div:focus-within, 
    input[type="text"]:focus, 
    input[type="number"]:focus {{
        border-color: {COLOR_BEIGE} !important;
        background-color: rgba(74, 90, 106, 0.8) !important;
    }}

    /* Botones dinámicos */
    .stButton > button, button[kind="secondaryFormSubmit"] {{
        background-color: {COLOR_OLIVE} !important;
        color: {COLOR_CHARCOAL} !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 2rem !important;
        transition: all 0.3s ease !important;
    }}

    .stButton > button:hover, button[kind="secondaryFormSubmit"]:hover {{
        background-color: {COLOR_BRONZE} !important;
        color: {COLOR_BEIGE} !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.4) !important;
    }}

    /* Contenedores y Tarjetas */
    [data-testid="stVerticalBlockBorderWrapper"] {{
        border-radius: 12px !important;
        border: 1px solid {COLOR_BLUE_GREY} !important;
        background-color: rgba(47, 49, 51, 0.7) !important;
        transition: transform 0.3s ease !important;
    }}
    
    [data-testid="stVerticalBlockBorderWrapper"]:hover {{
        transform: translateY(-3px);
        border: 1px solid {COLOR_OLIVE} !important;
    }}

    /* Separadores y Métricas */
    hr {{ border-color: {COLOR_BRONZE} !important; opacity: 0.4; }}
    [data-testid="stMetricValue"] {{ color: {COLOR_OLIVE} !important; }}
    [data-testid="stMetricLabel"] {{ color: {COLOR_BEIGE} !important; }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

inyectar_estilos()

# 5. Nuevo menú de navegación lateral (Innovación visual)
st.sidebar.write("### 🧭 Navegación")
secciones = st.sidebar.radio(
    "Seleccione el módulo:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"],
    label_visibility="collapsed"
)

if secciones == "Home":
    texto_centrado("PROYECTO 1 – APLICACIÓN EN STREAMLIT", "h1", COLOR_BEIGE, "2.8rem")
    st.divider()
    
    # Animación JS interactiva adaptada a la nueva paleta
    banner_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            canvas {{ display: block; width: 100%; height: 140px; background: transparent; border-radius: 10px; }}
            body {{ margin: 0; overflow: hidden; }}
        </style>
    </head>
    <body>
        <canvas id="canvas"></canvas>
        <script>
            const canvas = document.getElementById('canvas');
            const ctx = canvas.getContext('2d');
            let width, height;
            let particles = [];
            const colors = ['{COLOR_BLUE_GREY}', '{COLOR_BRONZE}', '{COLOR_OLIVE}'];

            function resize() {{
                width = canvas.width = window.innerWidth;
                height = canvas.height = 140;
            }}
            window.addEventListener('resize', resize);
            resize();

            class Particle {{
                constructor() {{
                    this.x = Math.random() * width;
                    this.y = Math.random() * height;
                    this.vx = (Math.random() - 0.5) * 1.5;
                    this.vy = (Math.random() - 0.5) * 1.5;
                    this.radius = Math.random() * 3 + 1;
                    this.color = colors[Math.floor(Math.random() * colors.length)];
                }}
                update() {{
                    this.x += this.vx;
                    this.y += this.vy;
                    if (this.x < 0 || this.x > width) this.vx *= -1;
                    if (this.y < 0 || this.y > height) this.vy *= -1;
                }}
                draw() {{
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                    ctx.fillStyle = this.color;
                    ctx.fill();
                }}
            }}
            for(let i=0; i<60; i++) particles.push(new Particle());
            
            let mouse = {{ x: null, y: null }};
            canvas.addEventListener('mousemove', (e) => {{
                mouse.x = e.clientX; mouse.y = e.clientY;
            }});

            function animate() {{
                ctx.clearRect(0, 0, width, height);
                particles.forEach(p => {{
                    p.update();
                    if (mouse.x) {{
                        let dx = mouse.x - p.x;
                        let dy = mouse.y - p.y;
                        if (Math.sqrt(dx*dx + dy*dy) < 60) {{
                            p.x -= dx * 0.03; p.y -= dy * 0.03;
                        }}
                    }}
                    p.draw();
                }});
                requestAnimationFrame(animate);
            }}
            animate();
        </script>
    </body>
    </html>
    """
    components.html(banner_html, height=145)
 
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
    texto_centrado("Módulo 1 – Python Fundamentals", "h3", COLOR_BRONZE)
    st.divider()

    texto_centrado("Se va a desarrollar una aplicación interactiva haciendo uso de las plataformas GitHub y Streamlit, integrando los contenidos revisados en el módulo.", "p", COLOR_BEIGE)
    st.divider()

    texto_centrado("Tecnologías Utilizadas", "h3", COLOR_BRONZE)

    col3, col4, col5, col6 = st.columns(4)
    for col, tech in zip([col3, col4, col5, col6], ["Python", "GitHub", "Streamlit", "Librerías"]):
        with col:
            with st.container(border=True):
                texto_centrado(tech, "h4", COLOR_OLIVE)

    st.divider()
    texto_centrado("Giancarlo Esteban Valdivia Asencio", "h3", COLOR_BRONZE)
    st.divider()

    texto_centrado("Bachiller en la carrera de Ingenieria de Sistemas e Informatica, egresado de la universidad Tecnologica del Perú en el año 2025 cuento con 4 años de experiencia laboral entre practicas pre-profesionales,practicas profesionales y puestos laborales directos, actualmente me encuentro laborando en la empresa Molitalia, y mi interesa seguir formandome en la administracion de data.", "p", COLOR_BEIGE)
    st.divider()

    texto_centrado("2026", "h3", COLOR_OLIVE)

elif secciones == "Ejercicio 1":
    texto_centrado("💰 Ejercicio 1 - Movimientos Diarios", "h1", COLOR_BEIGE)
    st.divider()
    texto_centrado("En este ejercicio se desarrollara una app para el ingreso de movimientos categorizados por ingreso o gasto, esto con el fin de ayudar al usuario a tener un mejor control de sus movimientos financieros diarios o mensuales. Al finalizar se mostrará el detalle de sus movimientos en un listado y su saldo final, indicando si aun tiene un salgo a favor o negativo.", "p", COLOR_BEIGE)
    st.divider()

    def ejercicio_1():
        if "movimientos" not in st.session_state:
            st.session_state.movimientos = []

        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                concepto = st.text_input("Concepto:")
                tipo = st.selectbox("Tipo de Movimiento:", ["Ingreso", "Gasto"])
            with col2:
                valor = st.number_input("Valor:", min_value=0.0, format="%.2f")

            if st.button("Agregar Movimiento"):
                if concepto.strip() != "" and valor > 0:
                    st.session_state.movimientos.append({"concepto": concepto, "tipo": tipo, "valor": valor})

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
                st.info("Tu saldo está en equilibrio.")

    ejercicio_1()
    st.divider()
    texto_centrado("No ahorres lo que queda después de gastar, gasta lo que queda después de ahorrar", "h4", COLOR_BRONZE)

elif secciones == "Ejercicio 2":
    texto_centrado("🧾 Ejercicio 2 - Módulo de Ventas", "h1", COLOR_BEIGE)
    st.divider()
    texto_centrado("En este ejercicio se desarrollará un modulo de ventas de productos en la que se solicitará al operario el ingreso de nombre, categoria, precio, cantidad y total, esto con el fin de tener un calculo exacto de la venta a realizar. Al finalizar se mostrará el detalle de la compra y el monto total a pagar por parte del cliente.", "p", COLOR_BEIGE)
    st.divider()

    def ejercicio_2():
        if "array_productos" not in st.session_state:
            st.session_state.array_productos = np.array([], dtype=object)
            st.session_state.array_categorias = np.array([], dtype=object)
            st.session_state.array_precios = np.array([], dtype=float)
            st.session_state.array_cantidades = np.array([], dtype=int)
            st.session_state.array_totales = np.array([], dtype=float)
        
        with st.form("form_registro_producto", clear_on_submit=True):
            texto_centrado("Ingrese el Producto", "h3", COLOR_BRONZE)
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
                st.error("⚠️ El Nombre del Producto es obligatorio.")
            elif categoria == "-- Selecciona una categoría --":
                st.error("⚠️ Debes seleccionar una Categoría válida.")
            elif precio <= 0:
                st.error("⚠️ El Precio debe ser mayor a 0.")
            elif cantidad <= 0:
                st.error("⚠️ La Cantidad debe ser mayor a 0.")
            else:
                total = precio * cantidad
                st.session_state.array_productos = np.append(st.session_state.array_productos, producto)
                st.session_state.array_categorias = np.append(st.session_state.array_categorias, categoria)
                st.session_state.array_precios = np.append(st.session_state.array_precios, precio)
                st.session_state.array_cantidades = np.append(st.session_state.array_cantidades, cantidad)
                st.session_state.array_totales = np.append(st.session_state.array_totales, total)
                st.success(f"Producto '{producto}' agregado correctamente.")
        
        if len(st.session_state.array_productos) > 0:
            texto_centrado("Productos Registrados", "h3", COLOR_BRONZE)
            df_registros = pd.DataFrame({
                "Producto": st.session_state.array_productos,
                "Categoría": st.session_state.array_categorias,
                "Precio Unitario": st.session_state.array_precios,
                "Cantidad": st.session_state.array_cantidades,
                "Total": st.session_state.array_totales
            })
            st.dataframe(df_registros, use_container_width=True)
            
            texto_centrado("Resumen de Compra", "h3", COLOR_OLIVE)
            col_m1, col_m2 = st.columns(2)
            col_m1.metric("Total de Productos", len(df_registros))
            col_m2.metric("Monto Total", f"S/{df_registros['Total'].sum():,.2f}")
        else:
            st.info("Aún no se han agregado registros. Completa el formulario arriba para empezar.")
            
    ejercicio_2()
    st.divider()
    texto_centrado("Lo que no se mide, no se controla; lo que no se controla, no mejora.", "h4", COLOR_BRONZE)

elif secciones == "Ejercicio 3":
    texto_centrado("🖥️ Ejercicio 3 - Cálculo de Almacenamiento", "h1", COLOR_BEIGE)
    st.divider()
    texto_centrado("Esta herramienta permite calcular el almacenamiento estimado necesario para respaldos en función de la cantidad de usuarios, y la cantidad de archivos a respaldar.", "p", COLOR_BEIGE)
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
        texto_centrado("Histórico de Resultados:", "h3", COLOR_BRONZE)
        df_resultados = pd.DataFrame(st.session_state.historial_calculos)
        st.dataframe(df_resultados, use_container_width=True)

    st.divider()
    texto_centrado("Simplifica tus procesos, potencia tus resultados.", "h4", COLOR_BRONZE)
    
else:
    texto_centrado("⚙️ Ejercicio 4 - Operatividad de Servidor", "h1", COLOR_BEIGE)
    st.divider()
    texto_centrado("Este módulo define la entidad del servidor mediante sus atributos clave como: identificador, tiempos operativos y capacidades de disco. A partir de estas variables, el código calcula dinámicamente el porcentaje de disponibilidad restando el tiempo de caída al total, evalúa la ocupación del espacio y genera un diagnóstico del estado general del sistema.", "p", COLOR_BEIGE)
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
    texto_centrado("Simplifica tus procesos, potencia tus resultados.", "h4", COLOR_BRONZE)
