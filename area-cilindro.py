# Algoritmo para calcular a área de um cilindro regular
# ÁREA = 2 * ÁREA DA BASE + ÁREA LATERAL
# ÁREA DA BASE = π * R²
# ÁREA LATERAL = 2 * π * R * ALTURA
# Onde π = 3,14

# Constante
PI = 3.14

# Entrada de dados
raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

# Cálculo da área da base
area_base = PI * (raio ** 2)

# Cálculo da área lateral
area_lateral = 2 * PI * raio * altura

# Cálculo da área total
area_total = 2 * area_base + area_lateral

# Saída dos resultados
print("\n" + "="*50)
print(f"Raio do cilindro: {raio}")
print(f"Altura do cilindro: {altura}")
print(f"Área da base: {area_base:.2f}")
print(f"Área lateral: {area_lateral:.2f}")
print(f"Área total: {area_total:.2f}")
print("="*50)
