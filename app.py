

import streamlit as st
from impacto_concessoes import calcular_impacto_concessoes

# Paleta Viridis
VIRIDIS = [
    "#440154", "#482878", "#3E4A89", "#31688E", "#26828E", "#1F9E89", "#35B779", "#6CCE59", "#B4DE2C", "#FDE725"
]

# Customização do título e métricas com Viridis, fundo branco
st.markdown(
    f"""
    <style>
        .stApp {{
            background: #fff;
        }}
        h1 {{
            color: {VIRIDIS[7]};
        }}
        .stMetric label, .stMetric span {{
            color: {VIRIDIS[5]};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Simulador de Concessões Florestais", layout="centered")
st.title("🌳 Simulador de Potencial de Concessões Florestais")
st.write("""
Compare o cenário atual com o cenário selecionado para concessões florestais.
""")

col1, col2 = st.columns(2)

with col1:
    area_atual = st.number_input("Área do cenário atual (hectares)", min_value=0.0, value=100000.0, step=1000.0, format="%0.0f")
with col2:
    area_novo = st.number_input("Área do cenário selecionado (hectares)", min_value=0.0, value=500000.0, step=1000.0, format="%0.0f")


if st.button("Comparar Cenários"):
    resultados_atual = calcular_impacto_concessoes(area_atual)
    resultados_novo = calcular_impacto_concessoes(area_novo)

    st.subheader("Comparação dos Cenários")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### Cenário Atual\nÁrea: {area_atual:,.0f} ha")
        st.metric("Carbono (Ton/Ano)", f"{resultados_atual['Carbono (Ton/Ano)']:,.2f}")
        st.metric("Empregos Gerados", f"{resultados_atual['Empregos Gerados']:,.0f}")
        st.metric("Potencial Financeiro (R$)", f"{resultados_atual['Potencial Financeiro (R$)']:,.2f}")
        st.metric("Investimento Necessário (R$)", f"{resultados_atual['Investimento Necessário (R$)']:,.2f}")
    with col2:
        st.markdown(f"### Cenário Selecionado\nÁrea: {area_novo:,.0f} ha")
        st.metric("Carbono (Ton/Ano)", f"{resultados_novo['Carbono (Ton/Ano)']:,.2f}")
        st.metric("Empregos Gerados", f"{resultados_novo['Empregos Gerados']:,.0f}")
        st.metric("Potencial Financeiro (R$)", f"{resultados_novo['Potencial Financeiro (R$)']:,.2f}")
        st.metric("Investimento Necessário (R$)", f"{resultados_novo['Investimento Necessário (R$)']:,.2f}")

    # Gráficos comparativos
    import pandas as pd
    dados = {
        "Indicador": ["Carbono (Ton/Ano)", "Empregos Gerados", "Potencial Financeiro (R$)", "Investimento Necessário (R$)"],
        "Cenário Atual": [
            resultados_atual["Carbono (Ton/Ano)"],
            resultados_atual["Empregos Gerados"],
            resultados_atual["Potencial Financeiro (R$)"],
            resultados_atual["Investimento Necessário (R$)"]
        ],
        "Cenário Selecionado": [
            resultados_novo["Carbono (Ton/Ano)"],
            resultados_novo["Empregos Gerados"],
            resultados_novo["Potencial Financeiro (R$)"],
            resultados_novo["Investimento Necessário (R$)"]
        ]
    }
    df = pd.DataFrame(dados)
    df.set_index("Indicador", inplace=True)
    st.markdown("### Gráfico Comparativo")
    st.bar_chart(df)
