import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lfp
import librería_clases_proyecto1 as lcp

# 1. Configuración inicial (DEBE ir primero)
st.set_page_config(page_title="Proyecto 1 - Aplicación", page_icon="🚀", layout="wide")

# 2. Paleta de colores extraída de la imagen
COLOR_PEACH = "#F8B195"
COLOR_WATERMELON = "#F67280"
COLOR_MAUVE = "#C06C84"
COLOR_PURPLE = "#6C5B7B"
COLOR_BLUE = "#355C7D"

# 3. Función auxiliar para centralizar textos estrictamente con HTML
def texto_centrado(texto, etiqueta="h1", color=COLOR_PEACH, size=None):
    size_style = f"font-size: {size};" if size else ""
    html = f"""
        <div style='text-align: center; width: 100%; margin-bottom: 1rem;'>
            <{etiqueta} style='color: {color}; {size_style} text-shadow: 2px 2px 4px rgba(0,0,0,0.3); font-family: "Segoe UI", sans-serif;'>
                {texto}
            </{etiqueta}>
        </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# 4. Inyección de CSS Vanguardista basado en tu paleta
def inyectar_estilos():
    css = f"""
    <style>
    /* Fondo principal con gradiente de la paleta */
    .stApp {{
        background: linear-gradient(135deg, {COLOR_BLUE} 0%, {COLOR_PURPLE} 100%);
        color: #FFFFFF;
    }}
    
    /* Barra lateral */
    [data-testid="stSidebar"] {{
        background-color: {COLOR_BLUE} !important;
        border-right: 2px solid {COLOR_MAUVE};
    }}
    
    /* Estilos de inputs y selectores (Interactividad visual) */
    div[data-baseweb="select"] > div, 
    input[type="text"], 
    input[type="number"],
    div[data-baseweb="base-input"] {{
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #FFFFFF !important;
        border: 2px solid {COLOR_PURPLE} !important;
        border-radius: 10px !important;
        transition: all 0.4s ease !important;
    }}

    /* Efectos Hover y Focus en inputs */
    div[data-baseweb="select"] > div:hover, 
    input[type="text"]:hover, 
    input[type="number"]:hover {{
        border-color: {COLOR_WATERMELON} !important;
        box-shadow: 0 0 15px rgba(246, 114, 128, 0.5) !important;
        transform: translateY(-2px);
    }}
    
    div[data-baseweb="select"] > div:focus-within, 
    input[type="text"]:focus, 
    input[type="number"]:focus {{
        border-color: {COLOR_PEACH} !important;
        box-shadow: 0 0 20px rgba(248, 177, 149, 0.8) !important;
        background-color: rgba(255, 255, 255, 0.2) !important;
    }}

    /* Botones dinámicos */
    .stButton > button, button[kind="secondaryFormSubmit"] {{
        background: linear-gradient(90deg, {COLOR_WATERMELON} 0%, {COLOR_MAUVE} 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.6rem 2rem !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2) !important;
    }}

    .stButton > button:hover, button[kind="secondaryFormSubmit"]:hover {{
        transform: scale(1.05) translateY(-3px) !important;
        box-shadow: 0 10px 20px rgba(248, 177, 149, 0.4) !important;
        background: linear-gradient(90deg, {COLOR_PEACH} 0%, {COLOR_WATERMELON} 100%) !important;
    }}

    /* Contenedores y Tarjetas */
    [data-testid="stVerticalBlockBorderWrapper"] {{
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        background: rgba(108, 91, 123, 0.3) !important;
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }}
    
    [data-testid="stVerticalBlockBorderWrapper"]:hover {{
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.3) !important;
        border: 1px solid {COLOR_WATERMELON} !important;
    }}

    /* Separadores */
    hr {{ border-color: {COLOR_MAUVE} !important; opacity: 0.5; }}
    
    /* Métricas */
    [data-testid="stMetricValue"] {{ color: {COLOR_PEACH} !important; }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

inyectar_estilos()

st.sidebar.title("Secciones")
secciones = st.sidebar.selectbox("Selecione el módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if secciones == "Home":
    texto_centrado("PROYECTO 1 – APLICACIÓN EN STREAMLIT", "h1", COLOR_PEACH, "3rem")
    st.divider()
    
    # 5. INYECCIÓN DE JAVASCRIPT Y HTML INTERACTIVO (Banner de partículas)
    banner_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            canvas {{ display: block; width: 100%; height: 150px; background: transparent; border-radius: 15px; }}
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
            
            // Colores de tu paleta
            const colors = ['{COLOR_PEACH}', '{COLOR_WATERMELON}', '{COLOR_MAUVE}'];

            function resize() {{
                width = canvas.width = window.innerWidth;
                height = canvas.height = 150;
            }}
            window.addEventListener('resize', resize);
            resize();

            class Particle {{
                constructor() {{
                    this.x = Math.random() * width;
                    this.y = Math.random() * height;
                    this.vx = (Math.random() - 0.5) * 2;
                    this.vy = (Math.random() - 0.5) * 2;
                    this.radius = Math.random() * 4 + 1;
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

            for(let i=0; i<50; i++) particles.push(new Particle());

            // Interactividad con el mouse
            let mouse = {{ x: null, y: null }};
            canvas.addEventListener('mousemove', (e) => {{
                mouse.x = e.clientX;
                mouse.y = e.clientY;
            }});

            function animate() {{
                ctx.clearRect(0, 0, width, height);
                particles.forEach(p => {{
                    p.update();
                    // Interacción repulsiva con el mouse
                    if (mouse.x) {{
                        let dx = mouse.x - p.x;
                        let dy = mouse.y - p.y;
                        let distance = Math.sqrt(dx*dx + dy*dy);
                        if (distance < 50) {{
                            p.x -= dx * 0.05;
                            p.y -= dy * 0.05;
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
    components.html(banner_html, height=155)
 
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
    texto_centrado("Módulo 1 – Python Fundamentals", "h3", COLOR_WATERMELON)
    st.divider()

    texto_centrado("Se va a desarrollar una aplicación interactiva haciendo uso de las plataformas GitHub y Streamlit, integrando los contenidos revisados en el módulo.", "p", "white")
    st.divider()

    texto_centrado("Tecnologías Utilizadas", "h3", COLOR_WATERMELON)

    col3, col4, col5, col6 = st.columns(4)
    with col3:
        with st.container(border=True):
            texto_centrado("Python", "h4", COLOR_PEACH)
    with col4:
        with st.container(border=True):
            texto_centrado("GitHub", "h4", COLOR_PEACH)
    with col5:
        with st.container(border=True):
            texto_centrado("Streamlit", "h4", COLOR_PEACH)
    with col6:
        with st.container(border=True):
            texto_centrado("Librerías", "h4", COLOR_PEACH)

    st.divider()
    texto_centrado("Giancarlo Esteban Valdivia Asencio", "h3", COLOR_MAUVE)
    st.divider()

    texto_centrado("Bachiller en la carrera de Ingenieria de Sistemas e Informatica, egresado de la universidad Tecnologica del Perú en el año 2025 cuento con 4 años de experiencia laboral entre practicas pre-profesionales,practicas profesionales y puestos laborales directos, actualmente me encuentro laborando en la empresa Molitalia, y mi interesa seguir formandome en la administracion de data.", "p", "white")
    st.divider()

    texto_centrado("2026", "h3", COLOR_WATERMELON)

elif secciones == "Ejercicio 1":
    texto_centrado("💰 Ejercicio 1 - Movimientos Diarios", "h1", COLOR_PEACH)
    st.divider()
    texto_centrado("En este ejercicio se desarrollara una app para el ingreso de movimientos categorizados por ingreso o gasto, esto con el fin de ayudar al usuario a tener un mejor control de sus movimientos financieros diarios o mensuales. Al finalizar se mostrará el detalle de sus movimientos en un listado y su saldo final, indicando si aun tiene un salgo a favor o negativo.", "p", "white")
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
    texto_centrado("No ahorres lo que queda después de gastar, gasta lo que queda después de ahorrar", "h4", COLOR_PEACH)

elif secciones == "Ejercicio 2":
    texto_centrado("🧾 Ejercicio 2 - Módulo de Ventas", "h1", COLOR_PEACH)
    st.divider()
    texto_centrado("En este ejercicio se desarrollará un modulo de ventas de productos en la que se solicitará al operario el ingreso de nombre, categoria, precio, cantidad y total, esto con el fin de tener un calculo exacto de la venta a realizar. Al finalizar se mostrará el detalle de la compra y el monto total a pagar por parte del cliente.", "p", "white")
    st.divider()

    def ejercicio_2():
        if "array_productos" not in st.session_state:
            st.session_state.array_productos = np.array([], dtype=object)
            st.session_state.array_categorias = np.array([], dtype=object)
            st.session_state.array_precios = np.array([], dtype=float)
            st.session_state.array_cantidades = np.array([], dtype=int)
            st.session_state.array_totales = np.array([], dtype=float)
        
        with st.form("form_registro_producto", clear_on_submit=True):
            texto_centrado("Ingrese el Producto", "h3", COLOR_WATERMELON)
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
            texto_centrado("Productos Registrados", "h3", COLOR_WATERMELON)
            df_registros = pd.DataFrame({
                "Producto": st.session_state.array_productos,
                "Categoría": st.session_state.array_categorias,
                "Precio Unitario": st.session_state.array_precios,
                "Cantidad": st.session_state.array_cantidades,
                "Total": st.session_state.array_totales
            })
            st.dataframe(df_registros, use_container_width=True)
            
            texto_centrado("Resumen de Compra", "h3", COLOR_MAUVE)
            col_m1, col_m2 = st.columns(2)
            col_m1.metric("Total de Productos", len(df_registros))
            col_m2.metric("Monto Total", f"S/{df_registros['Total'].sum():,.2f}")
        else:
            st.info("Aún no se han agregado registros. Completa el formulario arriba para empezar.")
            
    ejercicio_2()
    st.divider()
    texto_centrado("Lo que no se mide, no se controla; lo que no se controla, no mejora.", "h4", COLOR_PEACH)

elif secciones == "Ejercicio 3":
    texto_centrado("🖥️ Ejercicio 3 - Cálculo de Almacenamiento", "h1", COLOR_PEACH)
    st.divider()
    texto_centrado("Esta herramienta permite calcular el almacenamiento estimado necesario para respaldos en función de la cantidad de usuarios, y la cantidad de archivos a respaldar.", "p", "white")
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
        texto_centrado("Histórico de Resultados:", "h3", COLOR_WATERMELON)
        df_resultados = pd.DataFrame(st.session_state.historial_calculos)
        st.dataframe(df_resultados, use_container_width=True)

    st.divider()
    texto_centrado("Simplifica tus procesos, potencia tus resultados.", "h4", COLOR_PEACH)
    
else:
    texto_centrado("⚙️ Ejercicio 4 - Operatividad de Servidor", "h1", COLOR_PEACH)
    st.divider()
    texto_centrado("Este módulo define la entidad del servidor mediante sus atributos clave como: identificador, tiempos operativos y capacidades de disco. A partir de estas variables, el código calcula dinámicamente el porcentaje de disponibilidad restando el tiempo de caída al total, evalúa la ocupación del espacio y genera un diagnóstico del estado general del sistema.", "p", "white")
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
    texto_centrado("Simplifica tus procesos, potencia tus resultados.", "h4", COLOR_PEACH)
