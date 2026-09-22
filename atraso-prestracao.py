# Algoritmo para calcular o valor da prestação com atraso
# NOVA PRESTAÇÃO = PRESTAÇÃO ATUAL + (PRESTAÇÃO ATUAL * TAXA * DIAS) / 100

# Entrada de dados
prestacao_atual = float(input("Digite o valor da prestação atrasada: R$ "))
taxa_juros = float(input("Digite a taxa de juros (em %): "))
dias_atraso = int(input("Digite o número de dias de atraso: "))

# Cálculo dos juros
juros = (prestacao_atual * taxa_juros * dias_atraso) / 100

# Cálculo da nova prestação
nova_prestacao = prestacao_atual + juros

# Saída dos resultados
print("\n" + "="*50)
print(f"Prestação original: R$ {prestacao_atual:.2f}")
print(f"Taxa de juros: {taxa_juros}%")
print(f"Dias de atraso: {dias_atraso}")
print(f"Juros acumulados: R$ {juros:.2f}")
print(f"Nova prestação: R$ {nova_prestacao:.2f}")
print("="*50)
