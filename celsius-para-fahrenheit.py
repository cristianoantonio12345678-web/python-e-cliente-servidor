# Algoritmo para converter temperatura de Celsius para Fahrenheit
# Fórmula: °F = 32 + 1.8 × °C

# Entrada de dados
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Cálculo da conversão para Fahrenheit
fahrenheit = 32 + (1.8 * celsius)

# Saída dos resultados
print("\n" + "="*50)
print(f"Temperatura em Celsius: {celsius}°C")
print(f"Temperatura em Fahrenheit: {fahrenheit}°F")
print("="*50)
