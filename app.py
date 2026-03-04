import streamlit as st
from impacto_concessoes import calcular_impacto_concessoes

st.set_page_config(page_title="Simulador de Concessões Florestais", layout="centered")
st.title("Simulador de Potencial de Concessões Florestais")
st.write("""
Este aplicativo calcula os impactos socioambientais e os investimentos necessários com base na expansão da área concedida (hectares).
""")

area = st.number_input("Meta de área concedida (hectares)", min_value=0.0, value=500000.0, step=1000.0, format="%0.0f")

if st.button("Calcular Impactos"):
    resultados = calcular_impacto_concessoes(area)
    st.subheader(f"Resultados para {area:,.0f} hectares")
    st.metric("Carbono (Ton/Ano)", f"{resultados['Carbono (Ton/Ano)']:,.2f}")
    st.metric("Empregos Gerados", f"{resultados['Empregos Gerados']:,.0f}")
    st.metric("Potencial Financeiro (R$)", f"{resultados['Potencial Financeiro (R$)']:,.2f}")
    st.metric("Investimento Necessário (R$)", f"{resultados['Investimento Necessário (R$)']:,.2f}")
