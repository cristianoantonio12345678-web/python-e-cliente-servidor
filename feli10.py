# Algoritmo para calcular o volume de um cone regular
# VOLUME = (ÁREA DA BASE * ALTURA) / 3
# ÁREA DA BASE = π * R²
# Onde π = 3,14

# Constante
PI = 3.14

# Entrada de dados
raio = float(input("Digite o raio do cone: "))
altura = float(input("Digite a altura do cone: "))

# Cálculo da área da base
area_base = PI * (raio ** 2)

# Cálculo do volume
volume = (area_base * altura) / 3

# Saída dos resultados
print("\n" + "="*50)
print(f"Raio do cone: {raio}")
print(f"Altura do cone: {altura}")
print(f"Área da base: {area_base:.2f}")
print(f"Volume do cone: {volume:.2f}")
print("="*50)
