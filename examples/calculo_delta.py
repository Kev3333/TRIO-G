"""
Calculadora de Coerência TRIO-G
================================

Este script calcula o índice de coerência (δ) em bits a partir de:
- Mudanças na barreira de ativação (ΔΔG‡)
- Razão entre constantes de reação (K_var/K_ref)

Uso:
    python calculo_delta.py

Autor: Kevin Khristopher Kuznier
Teoria: TRIO-G (Teoria da Relatividade Informacional Ontológica Geral)
"""

import math


def calcular_delta_de_energia(delta_delta_G, temperatura=300):
    """
    Calcula bits de coerência a partir de mudança na energia de ativação.
    
    Parâmetros:
        delta_delta_G (float): Mudança em ΔG‡ em J/mol
        temperatura (float): Temperatura em Kelvin (padrão: 300 K)
    
    Retorna:
        tuple: (delta em bits, fator de aceleração)
    
    Exemplo:
        >>> bits, fator = calcular_delta_de_energia(5000, 300)
        >>> print(f"Coerência: {bits:.2f} bits")
        Coerência: 2.89 bits
        >>> print(f"Aceleração: {fator:.1f}x")
        Aceleração: 7.4x
    """
    R = 8.314  # Constante dos gases em J/(mol·K)
    R_star = R * temperatura * math.log(2)
    
    delta = delta_delta_G / R_star
    fator_aceleracao = 2 ** delta
    
    return delta, fator_aceleracao


def calcular_delta_de_razao(K_var, K_ref):
    """
    Calcula bits de coerência a partir da razão de constantes de reação.
    
    Parâmetros:
        K_var (float): Constante de reação com variação
        K_ref (float): Constante de reação de referência
    
    Retorna:
        float: delta em bits
    
    Exemplo:
        >>> delta = calcular_delta_de_razao(7.4, 1.0)
        >>> print(f"Coerência: {delta:.2f} bits")
        Coerência: 2.89 bits
    """
    razao = K_var / K_ref
    delta = math.log2(razao)
    
    return delta


def calcular_energia_de_coerencia(delta, temperatura=300):
    """
    Calcula a energia efetiva de coerência (∅) a partir de δ.
    
    Parâmetros:
        delta (float): Índice de coerência em bits
        temperatura (float): Temperatura em Kelvin (padrão: 300 K)
    
    Retorna:
        tuple: (energia em J/mol, energia em kJ/mol)
    
    Exemplo:
        >>> energia_J, energia_kJ = calcular_energia_de_coerencia(2.89, 300)
        >>> print(f"Energia de coerência: {energia_kJ:.2f} kJ/mol")
        Energia de coerência: 5.00 kJ/mol
    """
    R = 8.314  # Constante dos gases em J/(mol·K)
    R_star = R * temperatura * math.log(2)
    
    energia_J = delta * R_star
    energia_kJ = energia_J / 1000
    
    return energia_J, energia_kJ


def calcular_indicador_F(delta, delta_Q, capacidade):
    """
    Calcula o indicador de fechamento F.
    
    F > 0: Reação favorecida (pré-organização suficiente)
    F = 0: Limiar crítico
    F < 0: Reação não favorecida (meio desorganizado)
    
    Parâmetros:
        delta (float): Índice de coerência em bits
        delta_Q (float): Demanda de reorganização
        capacidade (float): Capacidade do microambiente
    
    Retorna:
        tuple: (F, interpretação)
    """
    F = delta - (delta_Q / capacidade)
    
    if F > 0:
        interpretacao = "Reação FAVORECIDA (ambiente bem organizado)"
    elif F == 0:
        interpretacao = "LIMIAR CRÍTICO"
    else:
        interpretacao = "Reação NÃO FAVORECIDA (ambiente desorganizado)"
    
    return F, interpretacao


def exemplo_mutacao_enzimatica():
    """Exemplo prático: mutação que melhora atividade enzimática"""
    
    print("=" * 60)
    print("EXEMPLO: Mutação Enzimática")
    print("=" * 60)
    
    # Dados experimentais
    reducao_barreira = 5000  # J/mol (5 kJ/mol)
    temperatura = 300  # K (27°C)
    
    print(f"\n📊 Dados experimentais:")
    print(f"   Redução na barreira: {reducao_barreira/1000:.1f} kJ/mol")
    print(f"   Temperatura: {temperatura} K ({temperatura-273:.0f}°C)")
    
    # Cálculos
    delta, fator = calcular_delta_de_energia(reducao_barreira, temperatura)
    energia_J, energia_kJ = calcular_energia_de_coerencia(delta, temperatura)
    
    print(f"\n🧮 Resultados:")
    print(f"   Índice de coerência (δ): {delta:.3f} bits")
    print(f"   Fator de aceleração: {fator:.2f}x")
    print(f"   Energia de coerência (∅): {energia_kJ:.2f} kJ/mol")
    
    print(f"\n💡 Interpretação:")
    print(f"   A mutação adicionou {delta:.2f} bits de organização ao sítio ativo,")
    print(f"   tornando a reação {fator:.1f} vezes mais rápida!")
    print("=" * 60)


def exemplo_comparacao_solventes():
    """Exemplo: comparar eficiência catalítica em diferentes solventes"""
    
    print("\n" + "=" * 60)
    print("EXEMPLO: Comparação de Solventes")
    print("=" * 60)
    
    # Constantes de reação medidas
    K_agua = 1.0      # Referência (água)
    K_etanol = 3.2    # Em etanol
    K_dmso = 8.0      # Em DMSO
    
    print(f"\n📊 Constantes de reação medidas:")
    print(f"   Água (referência): K = {K_agua}")
    print(f"   Etanol: K = {K_etanol}")
    print(f"   DMSO: K = {K_dmso}")
    
    # Cálculos
    delta_etanol = calcular_delta_de_razao(K_etanol, K_agua)
    delta_dmso = calcular_delta_de_razao(K_dmso, K_agua)
    
    print(f"\n🧮 Coerência em cada solvente:")
    print(f"   Etanol: {delta_etanol:.2f} bits")
    print(f"   DMSO: {delta_dmso:.2f} bits")
    
    diferenca = delta_dmso - delta_etanol
    print(f"\n💡 Análise:")
    print(f"   DMSO fornece {diferenca:.2f} bits adicionais de organização")
    print(f"   em relação ao etanol.")
    print("=" * 60)


def exemplo_indicador_favorabilidade():
    """Exemplo: verificar se uma reação é favorecida"""
    
    print("\n" + "=" * 60)
    print("EXEMPLO: Indicador de Favorabilidade (F)")
    print("=" * 60)
    
    # Cenário 1: Enzima bem estruturada
    print("\n📌 Cenário 1: Enzima bem estruturada")
    delta1 = 5.0  # 5 bits de coerência
    delta_Q1 = 3.0
    capacidade1 = 1.0
    
    F1, interp1 = calcular_indicador_F(delta1, delta_Q1, capacidade1)
    print(f"   δ = {delta1} bits")
    print(f"   ΔQ/c = {delta_Q1/capacidade1}")
    print(f"   F = {F1:.1f} → {interp1}")
    
    # Cenário 2: Ambiente desorganizado
    print("\n📌 Cenário 2: Ambiente desorganizado")
    delta2 = 2.0
    delta_Q2 = 5.0
    capacidade2 = 1.0
    
    F2, interp2 = calcular_indicador_F(delta2, delta_Q2, capacidade2)
    print(f"   δ = {delta2} bits")
    print(f"   ΔQ/c = {delta_Q2/capacidade2}")
    print(f"   F = {F2:.1f} → {interp2}")
    
    print("=" * 60)


if __name__ == "__main__":
    print("\n🔬 CALCULADORA DE COERÊNCIA - TEORIA TRIO-G")
    print("Autor: Kevin Khristopher Kuznier\n")
    
    # Executar exemplos
    exemplo_mutacao_enzimatica()
    exemplo_comparacao_solventes()
    exemplo_indicador_favorabilidade()
    
    print("\n✅ Cálculos concluídos!")
    print("\nPara usar em seus próprios dados:")
    print("  from calculo_delta import calcular_delta_de_energia")
    print("  bits, fator = calcular_delta_de_energia(sua_energia, temperatura)")
