# Algoritmo para calcular a soma de três notas de um aluno

# Entrada de dados
nome_aluno = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

# Cálculo da soma
soma_notas = nota_1 + nota_2 + nota_3

# Cálculo da média
media_notas = soma_notas / 3

# Saída dos resultados
print("\n" + "="*40)
print(f"Aluno: {nome_aluno}")
print(f"Nota 1: {nota_1}")
print(f"Nota 2: {nota_2}")
print(f"Nota 3: {nota_3}")
print(f"Soma das notas: {soma_notas}")
print(f"Média das notas: {media_notas:.2f}")
print("="*40)
