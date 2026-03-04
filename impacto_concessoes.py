def calcular_impacto_concessoes(area_total_ha):
    # Definindo coeficientes (ajuste estes números com seus dados reais)
    CO2_POR_HA = 2.5  # ton/ano
    EMPREGOS_POR_1000_HA = 5
    RETORNO_FINANCEIRO_POR_HA = 150.00 # Reais/ano
    
    # Custos de Investimento (Equipe, Modelagem, Desenho)
    CUSTO_GESTAO_POR_HA = 12.00 

    # Cálculos
    carbono_total = area_total_ha * CO2_POR_HA
    empregos_totais = (area_total_ha / 1000) * EMPREGOS_POR_1000_HA
    financeiro_total = area_total_ha * RETORNO_FINANCEIRO_POR_HA
    investimento_necessario = area_total_ha * CUSTO_GESTAO_POR_HA

    return {
        "Carbono (Ton/Ano)": carbono_total,
        "Empregos Gerados": empregos_totais,
        "Potencial Financeiro (R$)": financeiro_total,
        "Investimento Necessário (R$)": investimento_necessario
    }

# Interface simples de teste
if __name__ == "__main__":
    area_teste = float(input("Digite a meta de área em hectares (ex: 5000000): "))
    resultados = calcular_impacto_concessoes(area_teste)
    
    print(f"\n--- Resultados para {area_teste:,.0f} hectares ---")
    for chave, valor in resultados.items():
        print(f"{chave}: {valor:,.2f}")

    input("\nPressione Enter para sair...")


