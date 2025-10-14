import streamlit as st
import random
import math

st.set_page_config(
    page_title="Simulación de Eventos Discretos",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 25%, #2a3f5f 50%, #1a2a44 75%, #0f1929 100%);
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
    }
    
    .main > div {
        padding-top: 1.5rem;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }
    
    h1 {
        background: linear-gradient(135deg, #ffffff 0%, #60a5fa 50%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.8rem !important;
        text-align: center;
        margin-bottom: 0.3rem !important;
        filter: drop-shadow(0 4px 12px rgba(59, 130, 246, 0.5));
        animation: titleGlow 3s ease-in-out infinite;
    }
    
    @keyframes titleGlow {
        0%, 100% { filter: drop-shadow(0 4px 12px rgba(59, 130, 246, 0.4)); }
        50% { filter: drop-shadow(0 4px 20px rgba(59, 130, 246, 0.7)); }
    }
    
    h3 {
        color: #f0f9ff !important;
        font-size: 2rem !important;
        text-shadow: 0 2px 8px rgba(96, 165, 250, 0.3);
    }
    
    .gradient-line {
        height: 5px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            #3b82f6 15%, 
            #60a5fa 30%,
            #93c5fd 50%,
            #60a5fa 70%,
            #3b82f6 85%,
            transparent 100%);
        border-radius: 3px;
        margin: 1.5rem auto;
        width: 70%;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.6), 0 0 40px rgba(59, 130, 246, 0.3);
        animation: lineGlow 2s ease-in-out infinite;
    }
    
    @keyframes lineGlow {
        0%, 100% { box-shadow: 0 0 20px rgba(59, 130, 246, 0.5), 0 0 40px rgba(59, 130, 246, 0.2); }
        50% { box-shadow: 0 0 30px rgba(59, 130, 246, 0.8), 0 0 60px rgba(59, 130, 246, 0.4); }
    }
    
    .stSelectbox label {
        color: #f0f9ff !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .stSelectbox > div > div {
        background: linear-gradient(135deg, rgba(30, 58, 95, 0.8) 0%, rgba(42, 74, 111, 0.7) 100%) !important;
        backdrop-filter: blur(15px);
        border: 2px solid rgba(96, 165, 250, 0.4) !important;
        border-radius: 15px !important;
        color: white !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: rgba(96, 165, 250, 0.7) !important;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2);
    }
    
    .stNumberInput label {
        color: #e0f2fe !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    .stNumberInput > div > div > input {
        background: linear-gradient(135deg, rgba(30, 58, 95, 0.6) 0%, rgba(42, 74, 111, 0.5) 100%) !important;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(96, 165, 250, 0.3) !important;
        border-radius: 10px !important;
        color: #f0f9ff !important;
        font-weight: 600 !important;
        box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: rgba(96, 165, 250, 0.6) !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2), inset 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 50%, #1e40af 100%);
        color: white;
        font-weight: 700;
        font-size: 1.15rem;
        border-radius: 14px;
        padding: 0.9rem 2.5rem;
        border: none;
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.2);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e3a8a 50%, #1e40af 100%);
        box-shadow: 0 8px 30px rgba(37, 99, 235, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.3);
        transform: translateY(-3px) scale(1.02);
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(0.98);
    }
    
    .stDataFrame {
        background: linear-gradient(135deg, rgba(30, 58, 95, 0.5) 0%, rgba(42, 74, 111, 0.4) 100%) !important;
        backdrop-filter: blur(15px);
        border-radius: 16px !important;
        border: 2px solid rgba(96, 165, 250, 0.2) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        overflow: hidden;
    }
    
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(30, 58, 95, 0.7) 0%, rgba(42, 74, 111, 0.6) 100%);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(96, 165, 250, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(59, 130, 246, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.15);
        border-color: rgba(96, 165, 250, 0.5);
    }
    
    [data-testid="metric-container"] label {
        color: #bae6fd !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        text-shadow: 0 2px 8px rgba(59, 130, 246, 0.4);
    }
    
    .stAlert {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(37, 99, 235, 0.15) 100%) !important;
        backdrop-filter: blur(10px);
        border-left: 5px solid #3b82f6 !important;
        border-radius: 12px !important;
        color: #f0f9ff !important;
        box-shadow: 0 4px 16px rgba(59, 130, 246, 0.3);
    }
    
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(96, 165, 250, 0.6), transparent);
        margin: 2.5rem 0;
        box-shadow: 0 1px 8px rgba(96, 165, 250, 0.3);
    }
    
    .subtitle-box {
        background: linear-gradient(135deg, rgba(30, 58, 95, 0.6) 0%, rgba(42, 74, 111, 0.5) 100%);
        backdrop-filter: blur(20px);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        border: 2px solid rgba(96, 165, 250, 0.3);
        margin-bottom: 2.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        animation: boxFloat 4s ease-in-out infinite;
    }
    
    @keyframes boxFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
    }
    
    .info-box {
        background: linear-gradient(135deg, rgba(30, 58, 95, 0.5) 0%, rgba(42, 74, 111, 0.4) 100%);
        backdrop-filter: blur(15px);
        border-radius: 16px;
        padding: 2rem;
        border: 2px solid rgba(96, 165, 250, 0.25);
        margin-top: 2.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.08);
    }
    
    .result-title {
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800 !important;
        margin-bottom: 1.5rem !important;
    }
    
    [data-testid="stMarkdownContainer"] p {
        color: #e0f2fe;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.2) 0%, rgba(22, 163, 74, 0.15) 100%) !important;
        backdrop-filter: blur(10px);
        border-left: 5px solid #22c55e !important;
        border-radius: 12px !important;
        color: #f0fdf4 !important;
        box-shadow: 0 4px 16px rgba(34, 197, 94, 0.3);
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2) 0%, rgba(220, 38, 38, 0.15) 100%) !important;
        backdrop-filter: blur(10px);
        border-left: 5px solid #ef4444 !important;
        border-radius: 12px !important;
        color: #fef2f2 !important;
        box-shadow: 0 4px 16px rgba(239, 68, 68, 0.3);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>✨ SIMULACIÓN DE EVENTOS DISCRETOS ✨</h1>", unsafe_allow_html=True)
st.markdown("<div class='gradient-line'></div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-box'><h4 style='color: #bae6fd; margin: 0; font-weight: 700; font-size: 1.3rem;'>Selecciona una simulación para comenzar</h4></div>", unsafe_allow_html=True)

simulacion = st.selectbox(
    "Elige una simulación:",
    ["-- Seleccionar --", "🎲 Dados", "🛒 Tienda", "🥚 Huevos", "🧂 Azúcar", "💰 Interés Simple", "📈 Interés Variable"],
    disabled=False,
    label_visibility="visible"
)
st.markdown("<br>", unsafe_allow_html=True)

if simulacion == "💰 Interés Simple":
    st.markdown("<h3>💰 Simulación de Interés Compuesto (Tasa Fija)</h3>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        capital_inicial = st.number_input("Capital inicial (Bs):", min_value=0.0, value=1000.0, step=100.0, key="k_simple")
    with col2:
        tasa = st.number_input("Tasa de interés:", min_value=0.0, max_value=1.0, value=0.035, step=0.001, key="i_simple")
    with col3:
        periodos = st.number_input("Número de periodos:", min_value=1, value=10, step=1, key="t_simple")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        btn_simular_simple = st.button("▶ SIMULAR", key="btn_simple", use_container_width=True)
    with col_btn2:
        btn_limpiar_simple = st.button("LIMPIAR", key="btn_limpiar_simple", use_container_width=True)
    
    if btn_limpiar_simple:
        st.rerun()
    
    if btn_simular_simple:
        resultados = []
        k = capital_inicial
        C = 1
        while C <= periodos:
            I = k * tasa
            k = k + I
            resultados.append({
                "Periodo": C,
                "Capital": f"{k:.2f}"
            })
            C += 1
        
        st.markdown("<h3 class='result-title'>Resultados</h3>", unsafe_allow_html=True)
        st.dataframe(resultados, use_container_width=True, height=400)
        st.success(f"Capital final después de {periodos} periodos: **{k:.2f} Bs**")

elif simulacion == "📈 Interés Variable":
    st.markdown("<h3>📈 Simulación de Interés Compuesto (Tasa Variable por Monto)</h3>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        capital_inicial = st.number_input("Capital inicial (Bs):", min_value=0.0, value=5000.0, step=100.0, key="k_variable")
    with col2:
        periodos = st.number_input("Número de periodos:", min_value=1, value=10, step=1, key="t_variable")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        btn_simular_variable = st.button("▶ SIMULAR", key="btn_variable", use_container_width=True)
    with col_btn2:
        btn_limpiar_variable = st.button("LIMPIAR", key="btn_limpiar_variable", use_container_width=True)
    
    if btn_limpiar_variable:
        st.rerun()
    
    if btn_simular_variable:
        resultados = []
        k = capital_inicial
        C = 1
        while C <= periodos:
            if k <= 10000:
                i = 0.035
            elif k <= 100000:
                i = 0.037
            else:
                i = 0.04
            
            I = k * i
            k = k + I
            resultados.append({
                "Periodo": C,
                "Tasa Aplicada": f"{i*100:.2f}%",
                "Capital": f"{k:.2f}"
            })
            C += 1
        
        st.markdown("<h3 class='result-title'>Resultados</h3>", unsafe_allow_html=True)
        st.dataframe(resultados, use_container_width=True, height=400)
        st.success(f"Capital final después de {periodos} periodos: **{k:.2f} Bs**")

elif simulacion == "🎲 Dados":
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
        btn_limpiar_dados = st.button("LIMPIAR", key="btn_limpiar_dados", use_container_width=True)
    
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
        
        st.markdown("<h3 class='result-title'>Resultados</h3>", unsafe_allow_html=True)
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
    
    st.markdown("<h4 style='color: #bae6fd; font-weight: 700;'>Distribución de Artículos Comprados</h4>", unsafe_allow_html=True)
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
        btn_limpiar_tienda = st.button("LIMPIAR", key="btn_limpiar_tienda", use_container_width=True)
    
    if btn_limpiar_tienda:
        st.rerun()
    
    if btn_simular_tienda:
        probs = [prob_0, prob_1, prob_2, prob_3]
        
        if abs(sum(probs) - 1.0) > 0.001:
            st.error("❌ Las probabilidades deben sumar 1.0")
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
            
            st.markdown("<h3 class='result-title'>Resultados</h3>", unsafe_allow_html=True)
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
    
    st.markdown("<h4 style='color: #bae6fd; font-weight: 700;'>Probabilidades del Sistema</h4>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<p style='color: #f0f9ff; font-weight: 600; font-size: 1.05rem;'>Finalidad del Huevo</p>", unsafe_allow_html=True)
        prob_roto = st.number_input("P(Roto):", min_value=0.0, max_value=1.0, value=0.2, step=0.1, key="pr_huevos")
        prob_pollo = st.number_input("P(Pollo):", min_value=0.0, max_value=1.0, value=0.3, step=0.1, key="ppo_huevos")
        prob_huevo = st.number_input("P(Permanece Huevo):", min_value=0.0, max_value=1.0, value=0.5, step=0.1, key="phu_huevos")
    
    with col2:
        st.markdown("<p style='color: #f0f9ff; font-weight: 600; font-size: 1.05rem;'>Destino del Pollo</p>", unsafe_allow_html=True)
        prob_muere = st.number_input("P(Muere):", min_value=0.0, max_value=1.0, value=0.2, step=0.1, key="pm_huevos")
        prob_sobrevive = st.number_input("P(Sobrevive):", min_value=0.0, max_value=1.0, value=0.8, step=0.1, key="ps_huevos")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        btn_simular_huevos = st.button("▶ SIMULAR", key="btn_huevos", use_container_width=True)
    with col_btn2:
        btn_limpiar_huevos = st.button("LIMPIAR", key="btn_limpiar_huevos", use_container_width=True)
    
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
        
        st.markdown("<h3 class='result-title'>Resultados</h3>", unsafe_allow_html=True)
        st.dataframe(resultados, use_container_width=True, height=400)
        
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
    
    st.markdown("<h4 style='color: #bae6fd; font-weight: 700;'>Parámetros del Sistema</h4>", unsafe_allow_html=True)
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
        btn_limpiar_azucar = st.button("LIMPIAR", key="btn_limpiar_azucar", use_container_width=True)
    
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
        
        st.markdown("<h3 class='result-title'>Resultados</h3>", unsafe_allow_html=True)
        st.dataframe(resultados, use_container_width=True, height=400)
        
        ganancia_neta = ingresos - costo_total
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Costo Total", f"{costo_total:.2f} Bs")
        col2.metric("Demanda Insatisfecha", f"{demanda_insatisfecha:.2f} Kg")
        col3.metric("Ingresos Totales", f"{ingresos:.2f} Bs")
        col4.metric("Ganancia Neta", f"{ganancia_neta:.2f} Bs")

else:
    st.markdown("<div class='info-box'><p style='color: #bae6fd; text-align: center; margin: 0; font-size: 1.2rem; font-weight: 600;'>Por favor, selecciona una simulación del menú desplegable</p></div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)