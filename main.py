"""
Projeto: Simulador de Potencial de Concessões Florestais
Objetivo: Calcular impactos socioambientais e investimentos necessários 
com base na expansão da área concedida (Hectares).
Linguagem: Python
"""

# Coeficientes base (Exemplos hipotéticos para modelagem inicial)
CO2_POR_HECTARE = 10.5  # Toneladas de carbono retido/evitado por hectare ao ano
EMPREGOS_POR_1000_HA = 15  # Número de empregos diretos e indiretos por 1000 hectares
INVESTIMENTO_ESTADO_POR_HA = 120.0  # Custo de gestão do Serviço Florestal por hectare (R$)

# Funções para cálculos
def calcular_carbono(area_ha):
    """Calcula o total de carbono retido/evitado."""
    return area_ha * CO2_POR_HECTARE

def calcular_empregos(area_ha):
    """Calcula o total de empregos gerados."""
    return (area_ha / 1000) * EMPREGOS_POR_1000_HA

def calcular_investimento(area_ha):
    """Calcula o investimento necessário para gestão."""
    return area_ha * INVESTIMENTO_ESTADO_POR_HA

# Exemplo de uso
if __name__ == "__main__":
    area_concedida = 5000  # hectares
    carbono = calcular_carbono(area_concedida)
    empregos = calcular_empregos(area_concedida)
    investimento = calcular_investimento(area_concedida)

    print(f"Área concedida: {area_concedida} ha")
    print(f"Carbono retido/evitado: {carbono:.2f} toneladas/ano")
    print(f"Empregos gerados: {empregos:.0f}")
    print(f"Investimento necessário: R$ {investimento:.2f}")
