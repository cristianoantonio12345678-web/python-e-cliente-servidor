# Algoritmo para calcular a média de três notas de um aluno

# Entrada de dados
nome_aluno = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota_1 + nota_2 + nota_3) / 3

# Determinação da situação (aprovado/reprovado)
if media >= 7.0:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

# Saída dos resultados
print("\n" + "="*50)
print(f"Aluno: {nome_aluno}")
print(f"Nota 1: {nota_1}")
print(f"Nota 2: {nota_2}")
print(f"Nota 3: {nota_3}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
print("="*50)
