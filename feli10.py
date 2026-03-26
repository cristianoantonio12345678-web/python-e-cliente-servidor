# Algoritmo para calcular o volume de um cilindro regular
# VOLUME = ÁREA DA BASE * ALTURA
# ÁREA DA BASE = π * R²
# Onde π = 3,14

# Constante
PI = 3.14

# Entrada de dados
raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

# Cálculo da área da base
area_base = PI * (raio ** 2)

# Cálculo do volume
volume = area_base * altura

# Saída dos resultados
print("\n" + "="*50)
print(f"Raio do cilindro: {raio}")
print(f"Altura do cilindro: {altura}")
print(f"Área da base: {area_base:.2f}")
print(f"Volume do cilindro: {volume:.2f}")
print("="*50)
