# Algoritmo para converter horas e minutos em apenas minutos

# Entrada de dados
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))

# Cálculo da conversão para minutos
minutos_totais = (horas * 60) + minutos

# Saída dos resultados
print("\n" + "="*45)
print(f"Tempo informado: {horas}h {minutos}min")
print(f"Total em minutos: {minutos_totais} minutos")
print("="*45)
