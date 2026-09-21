import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lfp
import librería_clases_proyecto1 as lcp

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
        if "movimientos" not in st.session_state:
            st.session_state.movimientos = []

        concepto = st.text_input("Concepto:")
        tipo = st.selectbox("Tipo de Movimiento:", ["Ingreso", "Gasto"])
        valor = st.number_input("Valor:", min_value=0.0, format="%.2f")

        if st.button("Agregar Movimiento"):
            if concepto.strip() != "" and valor > 0:
                st.session_state.movimientos.append({
                    "concepto": concepto,
                    "tipo": tipo,
                    "valor": valor
                })

        if st.session_state.movimientos:
            st.dataframe(st.session_state.movimientos)

            total_ingresos = sum(
                m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Ingreso"
            )
            total_gastos = sum(
                m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Gasto"
            )
            saldo_final = total_ingresos - total_gastos

            st.metric("Total Ingresos", f"S/{total_ingresos:,.2f}")
            st.metric("Total Gastos", f"S/{total_gastos:,.2f}")
            st.metric("Saldo Final", f"S/{saldo_final:,.2f}")

            if saldo_final > 0:
                st.success("Tu saldo está a favor.")
            elif saldo_final < 0:
                st.error("Tu saldo está en contra.")
            else:
                st.success("Tu saldo está en equilibrio.")

    
    ejercicio_1()
    st.divider()
    st.markdown("**No ahorres lo que queda después de gastar, gasta lo que queda después de ahorrar**",text_alignment="center")

elif secciones == "Ejercicio 2":
    st.title("Ejercicio 2 - Modulo de Ventas",text_alignment="center")
    st.divider()
    st.markdown("En este ejercicio se desarrollará un modulo de ventas de productos en la que se solicitará al operario el ingreso de  "
                "nombre, categoria, precio, cantidad y total, esto con el fin de tener un calculo exacto de la venta a realizar  "
                "Al finalizar se mostrará el detalle de la compra y el monto total a pagar por parte del cliente.",text_alignment="justify")
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
            categoria = st.selectbox(
                "Categoría", 
                ["Electrónica", "Abarrotes", "Ropa", "Hogar", "Otros"]
            )
        
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
        
        if __name__ == "__main__":
            ejercicio_2()


    st.divider()
    st.markdown("**Lo que no se mide, no se controla; lo que no se controla, no mejora.**",text_alignment="center")

elif secciones == "Ejercicio 3":
    st.title(" Ejercicio 3 - Cálculo de Almacenamiento de Respaldo", text_alignment="center")
    st.divider()
    st.markdown("Esta herramienta permite calcular el **almacenamiento estimado necesario para respaldos**"  
                " en función de la cantidad de usuarios, y la cantidad de archivos a respaldar.")
    st.divider()

    if "historial_calculos" not in st.session_state:
        st.session_state.historial_calculos = []

    col1, col2 = st.columns(2)
    with col1:
        numero_usuarios = st.number_input("Número de Usuarios",min_value=1,value=1,step=1)
        archivos_por_usuario = st.number_input("Archivos por Usuario",min_value=1,value=10,step=5)
        
    with col2:
        tamano_promedio_mb = st.number_input("Tamaño Promedio por Archivo (MB)", min_value=0.1,value=5.0,step=0.5)
        factor_respaldo = st.number_input("Factor de Respaldo",min_value=1.0,value=1.5,step=0.1)
        
    btn_ejecutar = st.button("Ejecutar")

    calculo_alm = lfp.calcular_almacenamiento_respaldo(numero_usuarios,archivos_por_usuario,tamano_promedio_mb,factor_respaldo)
    st.write("**El calculo de almacenamiento de respaldo es el siguiente:**", calculo_alm)

    if btn_ejecutar:
        calculo_alm = lfp.calcular_almacenamiento_respaldo(numero_usuarios,archivos_por_usuario,tamano_promedio_mb,factor_respaldo)
        st.session_state.historial_calculos.append(calculo_alm)

    if st.session_state.historial_calculos:
        st.write("### Historico de Resultados:")
        df_resultados = pd.DataFrame(st.session_state.historial_calculos)
        st.dataframe(df_resultados, use_container_width=True)


    st.divider()
    st.markdown("**Simplifica tus procesos, potencia tus resultados.**",text_alignment="center")

else: 
    st.title(" Ejercicio 3 - Operatividad de Servidor", text_alignment="center")
    st.divider()
    st.markdown("Este módulo define la entidad del servidor mediante sus atributos clave como:  "  
                " identificador, tiempos operativos y capacidades de disco.A partir de estas variables,"  
                " el código calcula dinámicamente el porcentaje de disponibilidad restando el tiempo de caída al total,  "
                " evalúa la ocupación del espacio y genera un diagnóstico del estado general del sistema.",text_alignment="justify")
    st.divider()
    
    st.set_page_config(page_title="Gestión CRUD de Servidores", page_icon="🖥️", layout="wide")
    st.title("🖥️ Sistema de Gestión de Servidores (CRUD)")

if "servidores" not in st.session_state:
    # Instanciamos usando lcp.Servidor()
    s1 = lcp.Servidor("Servidor-Web-01", 720, 10, 1000, 800)
    s2 = lcp.Servidor("Servidor-BD-01", 720, 50, 500, 480)
    st.session_state.servidores = {
        s1.nombre: s1,
        s2.nombre: s2
    }

# -----------------------------------------------------------------------------
# PESTAÑAS (st.tabs) PARA ORGANIZAR LAS OPERACIONES CRUD
# -----------------------------------------------------------------------------
tab_leer, tab_crear, tab_actualizar, tab_eliminar = st.tabs([
    "📋 1. Leer / Visualizar", 
    "➕ 2. Crear Servidor", 
    "✏️ 3. Actualizar Servidor", 
    "🗑️ 4. Eliminar Servidor"
])

# =============================================================================
# C - CREATE (CREAR REGISTROS)
# =============================================================================
with tab_crear:
    st.header("➕ Crear un Nuevo Servidor")
    
    with st.form("form_crear_servidor", clear_on_submit=True):
        nombre = st.text_input("Nombre del Servidor")
        
        col1, col2 = st.columns(2)
        with col1:
            tiempo_total = st.number_input("Tiempo Total (Horas)", min_value=1.0, value=720.0, step=1.0)
            almacenamiento_total = st.number_input("Almacenamiento Total (GB)", min_value=1.0, value=1000.0, step=10.0)
        
        with col2:
            tiempo_caida = st.number_input("Tiempo de Caída (Horas)", min_value=0.0, value=0.0, step=0.5)
            almacenamiento_usado = st.number_input("Almacenamiento Usado (GB)", min_value=0.0, value=100.0, step=10.0)
        
        btn_crear = st.form_submit_button("Guardar Servidor")
        
        if btn_crear:
            if not nombre.strip():
                st.error("⚠️ Debe ingresar un nombre válido para el servidor.")
            elif nombre in st.session_state.servidores:
                st.error("⚠️ Ya existe un servidor registrado con ese nombre.")
            else:
                try:
                    # Uso del alias lcp.Servidor
                    nuevo_servidor = lcp.Servidor(
                        nombre=nombre.strip(),
                        tiempo_total_h=tiempo_total,
                        tiempo_caida_h=tiempo_caida,
                        almacenamiento_total_gb=almacenamiento_total,
                        almacenamiento_usado_gb=almacenamiento_usado
                    )
                    st.session_state.servidores[nuevo_servidor.nombre] = nuevo_servidor
                    st.success(f"✅ ¡Servidor **'{nuevo_servidor.nombre}'** creado exitosamente!")
                    st.rerun()
                except ValueError as e:
                    st.error(f"❌ Error de validación: {e}")

# =============================================================================
# R - READ (LEER Y VISUALIZAR REGISTROS)
# =============================================================================
with tab_leer:
    st.header("📋 Registros de Servidores Activos")
    
    if not st.session_state.servidores:
        st.info("No hay servidores registrados actualmente.")
    else:
        # Método resumen() ejecutado desde la clase Servidor
        lista_resumenes = [s.resumen() for s in st.session_state.servidores.values()]
        df = pd.DataFrame(lista_resumenes)
        df.columns = ["Nombre Servidor", "Disponibilidad (%)", "Uso Almacenamiento (%)", "Estado"]
        
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.divider()
        st.subheader("Métricas de Salud Operativa")
        cols = st.columns(len(st.session_state.servidores))
        for idx, (nombre, serv) in enumerate(st.session_state.servidores.items()):
            datos = serv.resumen()
            with cols[idx]:
                st.metric(label=nombre, value=f"{datos['disponibilidad_pct']}% Uptime", delta=datos['estado'])

# =============================================================================
# U - UPDATE (ACTUALIZAR REGISTROS)
# =============================================================================
with tab_actualizar:
    st.header("✏️ Actualizar Datos de un Servidor")
    
    if not st.session_state.servidores:
        st.info("No hay servidores disponibles para editar.")
    else:
        servidor_seleccionado_nombre = st.selectbox(
            "Selecciona el servidor que deseas modificar:",
            options=list(st.session_state.servidores.keys()),
            key="sb_actualizar"
        )
        
        servidor_actual = st.session_state.servidores[servidor_seleccionado_nombre]
        
        st.write(f"Modificando atributos de: **{servidor_actual.nombre}**")
        
        col1, col2 = st.columns(2)
        with col1:
            nuevo_tiempo_total = st.number_input("Tiempo Total (Horas)", min_value=1.0, value=float(servidor_actual.tiempo_total_h), key="u_tt")
            nuevo_almacenamiento_total = st.number_input("Almacenamiento Total (GB)", min_value=1.0, value=float(servidor_actual.almacenamiento_total_gb), key="u_at")
        
        with col2:
            nuevo_tiempo_caida = st.number_input("Tiempo de Caída (Horas)", min_value=0.0, value=float(servidor_actual.tiempo_caida_h), key="u_tc")
            nuevo_almacenamiento_usado = st.number_input("Almacenamiento Usado (GB)", min_value=0.0, value=float(servidor_actual.almacenamiento_usado_gb), key="u_au")
            
        if st.button("💾 Actualizar Registro", use_container_width=True):
            try:
                # Reinstanciamos con lcp.Servidor
                servidor_actualizado = lcp.Servidor(
                    nombre=servidor_actual.nombre,
                    tiempo_total_h=nuevo_tiempo_total,
                    tiempo_caida_h=nuevo_tiempo_caida,
                    almacenamiento_total_gb=nuevo_almacenamiento_total,
                    almacenamiento_usado_gb=nuevo_almacenamiento_usado
                )
                
                st.session_state.servidores[servidor_actual.nombre] = servidor_actualizado
                st.success(f"✅ Se actualizaron los datos de **{servidor_actual.nombre}** correctamente.")
                st.rerun()
            except ValueError as e:
                st.error(f"❌ Error al actualizar: {e}")

# =============================================================================
# D - DELETE (ELIMINAR REGISTROS)
# =============================================================================
with tab_eliminar:
    st.header("🗑️ Eliminar Servidor")
    
    if not st.session_state.servidores:
        st.info("No hay servidores registrados para eliminar.")
    else:
        servidor_a_eliminar = st.selectbox(
            "Selecciona el servidor que deseas eliminar permanentemente:",
            options=list(st.session_state.servidores.keys()),
            key="sb_eliminar"
        )
        
        st.warning(f"⚠️ Estás a punto de borrar el registro del servidor **{servidor_a_eliminar}**.")
        
        if st.button("🔥 Confirmar y Eliminar", type="primary"):
            del st.session_state.servidores[servidor_a_eliminar]
            st.success(f"🗑️ Servidor **{servidor_a_eliminar}** eliminado con éxito.")
            st.rerun()
    
    
    st.divider()
    st.markdown("**Simplifica tus procesos, potencia tus resultados.**",text_alignment="center")


  


  











