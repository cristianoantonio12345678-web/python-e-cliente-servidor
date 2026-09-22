# Algoritmo para calcular a média ponderada
# MÉDIA = (A * 7 + B * 3 + C * 4 + D * 2) / 16

# Entrada de dados
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

# Cálculo da média ponderada
media = (A * 7 + B * 3 + C * 4 + D * 2) / 16

# Saída dos resultados
print("\n" + "="*50)
print(f"Valor de A: {A}")
print(f"Valor de B: {B}")
print(f"Valor de C: {C}")
print(f"Valor de D: {D}")
print(f"Média ponderada: {media:.2f}")
print("="*50)
