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
    .main {
        background-color: #1E3A5F;
    }
    .stSelectbox {
        color: white;
    }
    h1 {
        color: #FFFFFF;
        text-align: center;
    }
    h2, h3 {
        color: #A8C5E2;
    }
    .stButton>button {
        width: 100%;
        background-color: #4A90E2;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #357ABD;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎲 SIMULACIÓN DE EVENTOS DISCRETOS</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid #4A90E2;'>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Selecciona una simulación para comenzar</h3>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

simulacion = st.selectbox(
    "Elige una simulación:",
    ["-- Seleccionar --", "🎲 Dados", "🛒 Tienda", "🥚 Huevos", "🧂 Azúcar"],
    key="sim_selector"
)

st.markdown("<br>", unsafe_allow_html=True)

if simulacion == "🎲 Dados":
    st.markdown("### 🎲 Simulación de Juego de Dados")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        n_juegos = st.number_input("Número de Juegos:", min_value=1, value=10, step=1)
        costo_juego = st.number_input("Costo del juego (Bs):", min_value=0.0, value=2.0, step=0.1)
        perdida_casa = st.number_input("Pérdida de la casa si gana jugador (Bs):", min_value=0.0, value=5.0, step=0.1)
    
    with col2:
        ganancia_inicial = st.number_input("Ganancia inicial de la casa (Bs):", min_value=0.0, value=0.0, step=0.1)
    
    if st.button("▶ SIMULAR", key="btn_dados"):
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
        
        st.markdown("### 📊 Resultados")
        st.dataframe(resultados, use_container_width=True)
        
        porcentaje_casa = (gana_casa / n_juegos) * 100
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Ganancia Neta Casa", f"{ganancia_neta:.2f} Bs")
        col2.metric("Juegos ganados por Casa", gana_casa)
        col3.metric("Juegos ganados por Jugador", gana_jugador)
        
        st.info(f"📈 Porcentaje de juegos ganados por la casa: {porcentaje_casa:.2f}%")

elif simulacion == "🛒 Tienda":
    st.markdown("### 🛒 Simulación de Llegadas de Clientes")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        horas = st.number_input("Horas a simular:", min_value=1, value=10, step=1)
    
    with col2:
        sims = st.number_input("Número de simulaciones:", min_value=1, value=5, step=1)
    
    st.markdown("#### Distribución de Artículos Comprados")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        prob_0 = st.number_input("P(0 artículos):", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
    with col2:
        prob_1 = st.number_input("P(1 artículo):", min_value=0.0, max_value=1.0, value=0.3, step=0.1)
    with col3:
        prob_2 = st.number_input("P(2 artículos):", min_value=0.0, max_value=1.0, value=0.4, step=0.1)
    with col4:
        prob_3 = st.number_input("P(3 artículos):", min_value=0.0, max_value=1.0, value=0.1, step=0.1)
    
    if st.button("▶ SIMULAR", key="btn_tienda"):
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
            
            st.markdown("### 📊 Resultados")
            st.dataframe(resultados, use_container_width=True, height=300)
            
            prom_clientes = total_clientes / sims
            prom_articulos = total_articulos / sims
            
            col1, col2 = st.columns(2)
            col1.metric("Promedio Clientes Totales", f"{prom_clientes:.2f}")
            col2.metric("Promedio Artículos Vendidos", f"{prom_articulos:.2f}")

elif simulacion == "🥚 Huevos":
    st.markdown("### 🥚 Simulación de Gallina Ponedora")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        n_sim = st.number_input("Número de Simulaciones:", min_value=1, value=5, step=1)
        n_dias = st.number_input("Número de Días:", min_value=1, value=300, step=1)
    
    with col2:
        precio_huevo = st.number_input("Precio Venta Huevo ($):", min_value=0.0, value=2.0, step=0.1)
        precio_pollo = st.number_input("Precio Venta Pollo ($):", min_value=0.0, value=30.0, step=0.1)
    
    with col3:
        media = st.number_input("Media (λ) huevos/día:", min_value=0.1, value=2.0, step=0.1)
    
    st.markdown("#### Probabilidades del Sistema")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Finalidad del Huevo**")
        prob_roto = st.number_input("P(Roto):", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
        prob_pollo = st.number_input("P(Pollo):", min_value=0.0, max_value=1.0, value=0.3, step=0.1)
        prob_huevo = st.number_input("P(Permanece Huevo):", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    
    with col2:
        st.markdown("**Destino del Pollo**")
        prob_muere = st.number_input("P(Muere):", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
        prob_sobrevive = st.number_input("P(Sobrevive):", min_value=0.0, max_value=1.0, value=0.8, step=0.1)
    
    if st.button("▶ SIMULAR", key="btn_huevos"):
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
        
        st.markdown("### 📊 Resultados")
        st.dataframe(resultados, use_container_width=True)
        
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
    st.markdown("### 🧂 Simulación de Inventario de Azúcar")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        dias_sim = st.number_input("Número de días a simular:", min_value=1, value=60, step=1)
    
    st.markdown("#### Parámetros del Sistema")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        capacidad_bodega = st.number_input("Capacidad de Bodega (Kg):", min_value=0.0, value=700.0, step=10.0)
        costo_orden = st.number_input("Costo de Orden (Bs/orden):", min_value=0.0, value=100.0, step=10.0)
    
    with col2:
        costo_inventario = st.number_input("Costo de Inventario (Bs/kg):", min_value=0.0, value=0.1, step=0.01)
        costo_adquisicion = st.number_input("Costo de Adquisición (Bs/kg):", min_value=0.0, value=3.5, step=0.1)
    
    with col3:
        precio_venta = st.number_input("Precio de Venta (Bs/kg):", min_value=0.0, value=5.0, step=0.1)
        media_demanda = st.number_input("Demanda Media (Kg/día):", min_value=0.1, value=100.0, step=1.0)
    
    if st.button("▶ SIMULAR", key="btn_azucar"):
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
        
        st.markdown("### 📊 Resultados")
        st.dataframe(resultados, use_container_width=True, height=300)
        
        ganancia_neta = ingresos - costo_total
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Costo Total", f"{costo_total:.2f} Bs")
        col2.metric("Demanda Insatisfecha", f"{demanda_insatisfecha:.2f} Kg")
        col3.metric("Ingresos Totales", f"{ingresos:.2f} Bs")
        col4.metric("Ganancia Neta", f"{ganancia_neta:.2f} Bs")

else:
    st.info("👆 Por favor, selecciona una simulación del menú desplegable")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7B98B8;'>Desarrollado con Python & Streamlit</p>", unsafe_allow_html=True)