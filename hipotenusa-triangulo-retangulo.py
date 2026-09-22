# Algoritmo para calcular a hipotenusa de um triângulo retângulo
# Teorema de Pitágoras: hipotenusa² = cateto1² + cateto2²

import math

# Entrada de dados
cateto_1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto_2 = float(input("Digite o comprimento do segundo cateto: "))

# Cálculo da hipotenusa usando o Teorema de Pitágoras
hipotenusa = math.sqrt((cateto_1 ** 2) + (cateto_2 ** 2))

# Saída dos resultados
print("\n" + "="*50)
print(f"Cateto 1: {cateto_1}")
print(f"Cateto 2: {cateto_2}")
print(f"Hipotenusa: {hipotenusa:.2f}")
print("="*50)
