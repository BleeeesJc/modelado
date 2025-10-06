import streamlit as st
import random
import math

st.set_page_config(
    page_title="Simulación de Eventos Discretos",
    page_icon="🎲",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .main > div {
        padding-top: 2rem;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        font-weight: 700 !important;
    }
    
    h1 {
        background: linear-gradient(120deg, #ffffff 0%, #a8c5e2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
        text-align: center;
        margin-bottom: 0.5rem !important;
        text-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    h3 {
        color: #e0e7ff !important;
        font-size: 1.8rem !important;
    }
    
    .gradient-line {
        height: 4px;
        background: linear-gradient(90deg, transparent, #4a90e2, #6ec1e4, #4a90e2, transparent);
        border-radius: 2px;
        margin: 1.5rem auto;
        width: 60%;
        box-shadow: 0 2px 10px rgba(74, 144, 226, 0.5);
    }
    
    .stSelectbox label {
        color: #e0e7ff !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }
    
    .stSelectbox > div > div {
        background: rgba(42, 74, 111, 0.6) !important;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(74, 144, 226, 0.3) !important;
        border-radius: 12px !important;
        color: white !important;
    }
    
    .stNumberInput label {
        color: #d4e3f0 !important;
        font-weight: 600 !important;
    }
    
    .stNumberInput > div > div > input {
        background: rgba(42, 74, 111, 0.5) !important;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(74, 144, 226, 0.3) !important;
        border-radius: 8px !important;
        color: white !important;
        font-weight: 600 !important;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        border-radius: 12px;
        padding: 0.8rem 2rem;
        border: none;
        box-shadow: 0 4px 15px rgba(74, 144, 226, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #357abd 0%, #2a5f8f 100%);
        box-shadow: 0 6px 20px rgba(74, 144, 226, 0.6);
        transform: translateY(-2px);
    }
    
    .stDataFrame {
        background: rgba(42, 74, 111, 0.4) !important;
        backdrop-filter: blur(10px);
        border-radius: 12px !important;
        border: 2px solid rgba(74, 144, 226, 0.2) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(42, 74, 111, 0.6) 0%, rgba(53, 122, 189, 0.4) 100%);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(74, 144, 226, 0.3);
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    [data-testid="metric-container"] label {
        color: #a8c5e2 !important;
        font-weight: 600 !important;
    }
    
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }
    
    .stAlert {
        background: rgba(74, 144, 226, 0.2) !important;
        backdrop-filter: blur(10px);
        border-left: 4px solid #4a90e2 !important;
        border-radius: 8px !important;
        color: #e0e7ff !important;
    }
    
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(74, 144, 226, 0.5), transparent);
        margin: 2rem 0;
    }
    
    .subtitle-box {
        background: rgba(42, 74, 111, 0.4);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        border: 2px solid rgba(74, 144, 226, 0.2);
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .info-box {
        background: rgba(42, 74, 111, 0.3);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 1.5rem;
        border: 2px solid rgba(74, 144, 226, 0.2);
        margin-top: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>SIMULACIÓN DE EVENTOS DISCRETOS</h1>", unsafe_allow_html=True)
st.markdown("<div class='gradient-line'></div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-box'><h4 style='color: #a8c5e2; margin: 0; font-weight: 600;'>Selecciona una simulación para comenzar</h4></div>", unsafe_allow_html=True)

simulacion = st.selectbox(
    "Elige una simulación:",
    ["-- Seleccionar --", "🎲 Dados", "🛒 Tienda", "🥚 Huevos", "🧂 Azúcar"],
    disabled=False,
    label_visibility="visible"
)

st.markdown("<br>", unsafe_allow_html=True)

if simulacion == "🎲 Dados":
    st.markdown("<h3>🎲 Simulación de Juego de Dados</h3>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        n_juegos = st.number_input("Número de Juegos:", min_value=1, value=10, step=1, key="nj_dados")
        costo_juego = st.number_input("Costo del juego (Bs):", min_value=0.0, value=2.0, step=0.1, key="cj_dados")
        perdida_casa = st.number_input("Pérdida de la casa si gana jugador (Bs):", min_value=0.0, value=5.0, step=0.1, key="pc_dados")
    
    with col2:
        ganancia_inicial = st.number_input("Ganancia inicial de la casa (Bs):", min_value=0.0, value=0.0, step=0.1, key="gi_dados")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        btn_simular_dados = st.button("▶ SIMULAR", key="btn_dados", use_container_width=True)
    with col_btn2:
        btn_limpiar_dados = st.button("🔄 LIMPIAR", key="btn_limpiar_dados", use_container_width=True)
    
    if btn_limpiar_dados:
        st.rerun()
    
    if btn_simular_dados:
        ganancia_neta = ganancia_inicial
        gana_casa = 0
        gana_jugador = 0
        resultados = []
        
        for juego in range(1, n_juegos + 1):
            ganancia_neta += costo_juego
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            suma = dado1 + dado2
            
            if suma == 7:
                ganador = "Jugador"
                gana_jugador += 1
                ganancia_neta -= perdida_casa
            else:
                ganador = "Casa"
                gana_casa += 1
            
            resultados.append({
                "Juego": juego,
                "Dado 1": dado1,
                "Dado 2": dado2,
                "Suma": suma,
                "Ganador": ganador,
                "Ganancia Casa": f"{ganancia_neta:.2f}"
            })
        
        st.markdown("<h3>📊 Resultados</h3>", unsafe_allow_html=True)
        st.dataframe(resultados, use_container_width=True, height=400)
        
        porcentaje_casa = (gana_casa / n_juegos) * 100
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Ganancia Neta Casa", f"{ganancia_neta:.2f} Bs")
        col2.metric("Juegos ganados por Casa", gana_casa)
        col3.metric("Juegos ganados por Jugador", gana_jugador)
        
        st.info(f"Porcentaje de juegos ganados por la casa: {porcentaje_casa:.2f}%")

elif simulacion == "🛒 Tienda":
    st.markdown("<h3>🛒 Simulación de Llegadas de Clientes</h3>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        horas = st.number_input("Horas a simular:", min_value=1, value=10, step=1, key="h_tienda")
    
    with col2:
        sims = st.number_input("Número de simulaciones:", min_value=1, value=5, step=1, key="s_tienda")
    
    st.markdown("<h4 style='color: #a8c5e2;'>Distribución de Artículos Comprados</h4>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        prob_0 = st.number_input("P(0 artículos):", min_value=0.0, max_value=1.0, value=0.2, step=0.1, key="p0_tienda")
    with col2:
        prob_1 = st.number_input("P(1 artículo):", min_value=0.0, max_value=1.0, value=0.3, step=0.1, key="p1_tienda")
    with col3:
        prob_2 = st.number_input("P(2 artículos):", min_value=0.0, max_value=1.0, value=0.4, step=0.1, key="p2_tienda")
    with col4:
        prob_3 = st.number_input("P(3 artículos):", min_value=0.0, max_value=1.0, value=0.1, step=0.1, key="p3_tienda")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        btn_simular_tienda = st.button("▶ SIMULAR", key="btn_tienda", use_container_width=True)
    with col_btn2:
        btn_limpiar_tienda = st.button("🔄 LIMPIAR", key="btn_limpiar_tienda", use_container_width=True)
    
    if btn_limpiar_tienda:
        st.rerun()
    
    if btn_simular_tienda:
        probs = [prob_0, prob_1, prob_2, prob_3]
        
        if abs(sum(probs) - 1.0) > 0.001:
            st.error("Las probabilidades deben sumar 1.0")
        else:
            total_clientes = 0
            total_articulos = 0
            articulos = [0, 1, 2, 3]
            limites = [sum(probs[:i+1]) for i in range(len(probs))]
            resultados = []
            
            for sim in range(1, sims + 1):
                for hora in range(1, horas + 1):
                    llegadas = random.randint(0, 3)
                    total_clientes += llegadas
                    
                    articulos_hora = 0
                    for _ in range(llegadas):
                        r = random.random()
                        for i, limite in enumerate(limites):
                            if r <= limite:
                                articulos_hora += articulos[i]
                                break
                    
                    total_articulos += articulos_hora
                    resultados.append({
                        "Simulación": sim,
                        "Hora": hora,
                        "Clientes": llegadas,
                        "Artículos Vendidos": articulos_hora
                    })
            
            st.markdown("<h3>📊 Resultados</h3>", unsafe_allow_html=True)
            st.dataframe(resultados, use_container_width=True, height=400)
            
            prom_clientes = total_clientes / sims
            prom_articulos = total_articulos / sims
            
            col1, col2 = st.columns(2)
            col1.metric("Promedio Clientes Totales", f"{prom_clientes:.2f}")
            col2.metric("Promedio Artículos Vendidos", f"{prom_articulos:.2f}")

elif simulacion == "🥚 Huevos":
    st.markdown("<h3>🥚 Simulación de Gallina Ponedora</h3>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        n_sim = st.number_input("Número de Simulaciones:", min_value=1, value=5, step=1, key="ns_huevos")
        n_dias = st.number_input("Número de Días:", min_value=1, value=300, step=1, key="nd_huevos")
    
    with col2:
        precio_huevo = st.number_input("Precio Venta Huevo ($):", min_value=0.0, value=2.0, step=0.1, key="ph_huevos")
        precio_pollo = st.number_input("Precio Venta Pollo ($):", min_value=0.0, value=30.0, step=0.1, key="pp_huevos")
    
    with col3:
        media = st.number_input("Media (λ) huevos/día:", min_value=0.1, value=2.0, step=0.1, key="m_huevos")
    
    st.markdown("<h4 style='color: #a8c5e2;'>Probabilidades del Sistema</h4>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<p style='color: #e0e7ff; font-weight: 600;'>Finalidad del Huevo</p>", unsafe_allow_html=True)
        prob_roto = st.number_input("P(Roto):", min_value=0.0, max_value=1.0, value=0.2, step=0.1, key="pr_huevos")
        prob_pollo = st.number_input("P(Pollo):", min_value=0.0, max_value=1.0, value=0.3, step=0.1, key="ppo_huevos")
        prob_huevo = st.number_input("P(Permanece Huevo):", min_value=0.0, max_value=1.0, value=0.5, step=0.1, key="phu_huevos")
    
    with col2:
        st.markdown("<p style='color: #e0e7ff; font-weight: 600;'>Destino del Pollo</p>", unsafe_allow_html=True)
        prob_muere = st.number_input("P(Muere):", min_value=0.0, max_value=1.0, value=0.2, step=0.1, key="pm_huevos")
        prob_sobrevive = st.number_input("P(Sobrevive):", min_value=0.0, max_value=1.0, value=0.8, step=0.1, key="ps_huevos")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        btn_simular_huevos = st.button("▶ SIMULAR", key="btn_huevos", use_container_width=True)
    with col_btn2:
        btn_limpiar_huevos = st.button("🔄 LIMPIAR", key="btn_limpiar_huevos", use_container_width=True)
    
    if btn_limpiar_huevos:
        st.rerun()
    
    if btn_simular_huevos:
        resultados = []
        total_ingreso = 0
        total_huevos = 0
        total_pollos = 0
        total_rotos = 0
        
        for sim in range(1, n_sim + 1):
            ingreso = 0
            huevos_vendidos = 0
            pollos_vivos = 0
            huevos_rotos = 0
            
            for _ in range(n_dias):
                L = math.exp(-media)
                k = 0
                p = 1
                while p > L:
                    k += 1
                    p *= random.random()
                n_huevos = k - 1
                
                for _ in range(n_huevos):
                    r = random.random()
                    if r < prob_roto:
                        huevos_rotos += 1
                    elif r < prob_roto + prob_pollo:
                        r2 = random.random()
                        if r2 >= prob_muere:
                            pollos_vivos += 1
                            ingreso += precio_pollo
                    else:
                        huevos_vendidos += 1
                        ingreso += precio_huevo
            
            resultados.append({
                "Simulación": sim,
                "Ingreso": f"{ingreso:.2f}",
                "Huevos Rotos": huevos_rotos,
                "Huevos Vendidos": huevos_vendidos,
                "Pollos Vivos": pollos_vivos
            })
            
            total_ingreso += ingreso
            total_huevos += huevos_vendidos
            total_pollos += pollos_vivos
            total_rotos += huevos_rotos
        
        st.markdown("<h3>📊 Resultados</h3>", unsafe_allow_html=True)
        st.dataframe(resultados, use_container_width=True, height=300)
        
        ingreso_prom = total_ingreso / n_sim
        ingreso_dia = ingreso_prom / n_dias
        prom_huevos = total_huevos / n_sim
        prom_pollos = total_pollos / n_sim
        prom_rotos = total_rotos / n_sim
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Ingreso Bruto Promedio", f"${ingreso_prom:.2f}")
        col2.metric("Ingreso Promedio por Día", f"${ingreso_dia:.2f}")
        col3.metric("Promedio Huevos Rotos", f"{prom_rotos:.2f}")
        
        col4, col5 = st.columns(2)
        col4.metric("Promedio Pollos Vivos", f"{prom_pollos:.2f}")
        col5.metric("Promedio Huevos Vendidos", f"{prom_huevos:.2f}")

elif simulacion == "🧂 Azúcar":
    st.markdown("<h3>🧂 Simulación de Inventario de Azúcar</h3>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    dias_sim = st.number_input("Número de días a simular:", min_value=1, value=60, step=1, key="ds_azucar")
    
    st.markdown("<h4 style='color: #a8c5e2;'>Parámetros del Sistema</h4>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        capacidad_bodega = st.number_input("Capacidad de Bodega (Kg):", min_value=0.0, value=700.0, step=10.0, key="cb_azucar")
        costo_orden = st.number_input("Costo de Orden (Bs/orden):", min_value=0.0, value=100.0, step=10.0, key="co_azucar")
    
    with col2:
        costo_inventario = st.number_input("Costo de Inventario (Bs/kg):", min_value=0.0, value=0.1, step=0.01, key="ci_azucar")
        costo_adquisicion = st.number_input("Costo de Adquisición (Bs/kg):", min_value=0.0, value=3.5, step=0.1, key="ca_azucar")
    
    with col3:
        precio_venta = st.number_input("Precio de Venta (Bs/kg):", min_value=0.0, value=5.0, step=0.1, key="pv_azucar")
        media_demanda = st.number_input("Demanda Media (Kg/día):", min_value=0.1, value=100.0, step=1.0, key="md_azucar")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        btn_simular_azucar = st.button("▶ SIMULAR", key="btn_azucar", use_container_width=True)
    with col_btn2:
        btn_limpiar_azucar = st.button("🔄 LIMPIAR", key="btn_limpiar_azucar", use_container_width=True)
    
    if btn_limpiar_azucar:
        st.rerun()
    
    if btn_simular_azucar:
        dias_revision = 7
        inventario = capacidad_bodega
        pedido_en_curso = 0
        dias_entrega = 0
        
        costo_total = 0
        demanda_insatisfecha = 0
        ingresos = 0
        resultados = []
        
        for dia in range(1, dias_sim + 1):
            if dias_entrega > 0:
                dias_entrega -= 1
            if dias_entrega == 0 and pedido_en_curso > 0:
                inventario += pedido_en_curso
                pedido_en_curso = 0
            
            demanda = round(-media_demanda * math.log(1 - random.random()))
            
            if demanda <= inventario:
                ventas = demanda
                inventario -= demanda
                faltante = 0
            else:
                ventas = inventario
                faltante = demanda - inventario
                demanda_insatisfecha += faltante
                inventario = 0
            
            ingresos += ventas * precio_venta
            costo_total += inventario * costo_inventario
            
            pedido = 0
            if dia % dias_revision == 0 and pedido_en_curso == 0:
                pedido = capacidad_bodega - inventario
                if pedido > 0:
                    pedido_en_curso = pedido
                    dias_entrega = random.randint(1, 3)
                    costo_total += costo_orden + pedido * costo_adquisicion
            
            resultados.append({
                "Día": dia,
                "Demanda": demanda,
                "Ventas": ventas,
                "Faltante": faltante,
                "Inventario": round(inventario, 2),
                "Pedido": pedido,
                "Costo Acum": round(costo_total, 2)
            })
        
        st.markdown("<h3>📊 Resultados</h3>", unsafe_allow_html=True)
        st.dataframe(resultados, use_container_width=True, height=400)
        
        ganancia_neta = ingresos - costo_total
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Costo Total", f"{costo_total:.2f} Bs")
        col2.metric("Demanda Insatisfecha", f"{demanda_insatisfecha:.2f} Kg")
        col3.metric("Ingresos Totales", f"{ingresos:.2f} Bs")
        col4.metric("Ganancia Neta", f"{ganancia_neta:.2f} Bs")

else:
    st.markdown("<div class='info-box'><p style='color: #a8c5e2; text-align: center; margin: 0; font-size: 1.1rem;'>Por favor, selecciona una simulación del menú desplegable</p></div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7B98B8; font-size: 0.95rem;'>Desarrollado con Python & Streamlit</p>", unsafe_allow_html=True)