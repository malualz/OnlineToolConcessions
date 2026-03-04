

import streamlit as st

import pandas as pd
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
    st.markdown(
        """
        <style>
        .indicador-box {
            background: #f5f5f5;
            border-radius: 12px;
            padding: 20px 16px 10px 16px;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            font-size: 12px !important;
        }
        .stApp {
            max-width: 1100px;
            margin-left: auto;
            margin-right: auto;
        }
        .st-emotion-cache-1wmy9hl {
            width: 500px !important;
        }
        .st-emotion-cache-13ejsyy {
            width: 500px !important;
        }
        .st-emotion-cache-1y4p8pa {
            margin-right: 30px !important;
        }
        .st-emotion-cache-1r6slb0 {
            margin-left: 30px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col_esq, col_dir = st.columns(2)

    # Indicadores da coluna esquerda
    indicadores_esq = [
        ("Carbono (Ton/Ano)", "Carbono Retido/Evitado"),
        ("Empregos Gerados", "Empregos Gerados")
    ]
    # Indicadores da coluna direita
    indicadores_dir = [
        ("Potencial Financeiro (R$)", "Potencial Financeiro (R$)"),
        ("Investimento Necessário (R$)", "Investimento Necessário (R$)")
    ]

    with col_esq:
        for chave, titulo in indicadores_esq:
            df_metric = pd.DataFrame({
                "Cenário": ["Atual", "Selecionado"],
                titulo: [resultados_atual[chave], resultados_novo[chave]]
            })
            df_metric.set_index("Cenário", inplace=True)
            st.markdown(f'<div class="indicador-box">', unsafe_allow_html=True)
            st.markdown(f"#### {titulo}")
            st.bar_chart(df_metric)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Cenário Atual**")
                st.metric(titulo, f"{resultados_atual[chave]:,.2f}")
            with col2:
                st.markdown(f"**Cenário Selecionado**")
                st.metric(titulo, f"{resultados_novo[chave]:,.2f}")
            st.markdown('</div>', unsafe_allow_html=True)

    with col_dir:
        for chave, titulo in indicadores_dir:
            df_metric = pd.DataFrame({
                "Cenário": ["Atual", "Selecionado"],
                titulo: [resultados_atual[chave], resultados_novo[chave]]
            })
            df_metric.set_index("Cenário", inplace=True)
            st.markdown(f'<div class="indicador-box">', unsafe_allow_html=True)
            st.markdown(f"#### {titulo}")
            st.bar_chart(df_metric)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Cenário Atual**")
                st.metric(titulo, f"{resultados_atual[chave]:,.2f}")
            with col2:
                st.markdown(f"**Cenário Selecionado**")
                st.metric(titulo, f"{resultados_novo[chave]:,.2f}")
            st.markdown('</div>', unsafe_allow_html=True)
