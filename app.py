import pandas as pd
import streamlit as st

from impacto_concessoes import calcular_impacto_concessoes

st.set_page_config(
    page_title="Simulador de Concessoes Florestais",
    page_icon="🌿",
    layout="wide",
)

METRIC_META = {
    "Carbono (Ton/Ano)": ("Carbono retido por ano", False, "Carbono retido por ano"),
    "Empregos Gerados": ("Empregos diretos estimados", False, "Empregos diretos estimados"),
    "Potencial Financeiro (R$)": ("Receita potencial anual", True, "Potencial financeiro"),
    "Investimento Necessario (R$)": ("Investimento necessario anual", True, "Investimento necessario"),
    "Investimento Necessário (R$)": ("Investimento necessario anual", True, "Investimento necessario"),
    "Investimento NecessÃ¡rio (R$)": ("Investimento necessario anual", True, "Investimento necessario"),
}

st.markdown(
    """
    <style>
    :root {
        --bg-top: #f6faf5;
        --bg-mid: #eef4ee;
        --panel: #ffffff;
        --primary: #1e5a3d;
        --text: #1f2d24;
        --muted: #5a6d62;
        --border: #d7e3da;
        --shadow: 0 14px 28px rgba(20, 60, 42, 0.08);
        --radius: 16px;
    }

    .stApp {
        background: radial-gradient(circle at 10% 0%, var(--bg-top) 0%, var(--bg-mid) 40%, #f9fbf9 100%);
        color: var(--text);
    }

    .block-container {
        max-width: 1160px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        background: linear-gradient(130deg, #11402f 0%, #1f5d43 48%, #2f7a58 100%);
        color: #f5fff8;
        border-radius: 18px;
        padding: 1.6rem 1.8rem;
        margin-bottom: 1.1rem;
        box-shadow: 0 18px 30px rgba(16, 52, 38, 0.24);
    }

    .hero h1 {
        margin: 0;
        font-size: 2rem;
        font-weight: 700;
        letter-spacing: -0.02rem;
    }

    .hero p {
        margin: 0.4rem 0 0;
        opacity: 0.92;
        font-size: 1rem;
    }

    .surface {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        padding: 1.1rem 1.1rem 0.4rem;
        margin-bottom: 1rem;
    }

    .kpi-title {
        margin: 0;
        font-size: 1rem;
        font-weight: 650;
        color: var(--text);
    }

    .kpi-sub {
        margin-top: 0.12rem;
        margin-bottom: 0.8rem;
        color: var(--muted);
        font-size: 0.9rem;
    }

    .stButton > button {
        background: linear-gradient(130deg, #1c5b3e 0%, #2f7a58 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.62rem 1.1rem;
        font-weight: 600;
    }

    .stButton > button:hover {
        filter: brightness(1.03);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def format_number(value: float, is_currency: bool = False) -> str:
    number = f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if is_currency:
        return f"R$ {number}"
    return number


st.markdown(
    """
    <div class="hero">
        <h1>Simulador de Potencial de Concessoes Florestais</h1>
        <p>Compare o cenario atual com um cenario projetado e visualize impactos ambientais, sociais e financeiros.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="surface">', unsafe_allow_html=True)
st.markdown("### Parametros da simulacao")

with st.form("simulacao_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        area_atual = st.number_input(
            "Area do cenario atual (hectares)",
            min_value=0.0,
            value=100000.0,
            step=1000.0,
            format="%0.0f",
        )
    with col_b:
        area_novo = st.number_input(
            "Area do cenario projetado (hectares)",
            min_value=0.0,
            value=500000.0,
            step=1000.0,
            format="%0.0f",
        )

    submitted = st.form_submit_button("Comparar cenarios")

st.markdown("</div>", unsafe_allow_html=True)

if submitted:
    resultados_atual = calcular_impacto_concessoes(area_atual)
    resultados_novo = calcular_impacto_concessoes(area_novo)
    metric_keys = list(resultados_atual.keys())

    resumo = pd.DataFrame(
        [
            {
                "Indicador": METRIC_META.get(key, ("Indicador calculado", False, key))[2],
                "Atual": resultados_atual[key],
                "Projetado": resultados_novo[key],
                "Delta": resultados_novo[key] - resultados_atual[key],
            }
            for key in metric_keys
        ]
    )
    resumo["Variacao (%)"] = (
        (resumo["Projetado"] - resumo["Atual"]) / resumo["Atual"].replace(0, pd.NA) * 100
    )

    st.markdown("### Comparacao dos indicadores")
    grid_left, grid_right = st.columns(2)

    for index, key in enumerate(metric_keys):
        subtitle, is_currency, display_title = METRIC_META.get(key, ("Indicador calculado", False, key))
        target_col = grid_left if index % 2 == 0 else grid_right

        with target_col:
            st.markdown('<div class="surface">', unsafe_allow_html=True)
            st.markdown(f'<p class="kpi-title">{display_title}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="kpi-sub">{subtitle}</p>', unsafe_allow_html=True)

            chart_df = pd.DataFrame(
                {
                    "Cenario": ["Atual", "Projetado"],
                    "Valor": [resultados_atual[key], resultados_novo[key]],
                }
            ).set_index("Cenario")
            st.bar_chart(chart_df, color=["#4f7c62"])

            metric_col_1, metric_col_2 = st.columns(2)
            delta = resultados_novo[key] - resultados_atual[key]

            with metric_col_1:
                st.metric("Atual", format_number(resultados_atual[key], is_currency))
            with metric_col_2:
                st.metric(
                    "Projetado",
                    format_number(resultados_novo[key], is_currency),
                    delta=format_number(delta, is_currency),
                )
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="surface">', unsafe_allow_html=True)
    st.markdown("### Resumo executivo")
    st.dataframe(
        resumo.assign(
            Atual=resumo["Atual"].map(lambda x: format_number(x)),
            Projetado=resumo["Projetado"].map(lambda x: format_number(x)),
            Delta=resumo["Delta"].map(lambda x: format_number(x)),
            **{
                "Variacao (%)": resumo["Variacao (%)"].map(
                    lambda x: "-" if pd.isna(x) else f"{x:,.2f}%".replace(",", "X").replace(".", ",").replace("X", ".")
                )
            },
        ),
        use_container_width=True,
        hide_index=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
