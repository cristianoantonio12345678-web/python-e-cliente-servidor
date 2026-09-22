# Algoritmo para calcular a soma das faltas do 1º e 2º bimestre de um aluno

# Entrada de dados
nome_aluno = input("Digite o nome do aluno: ")
faltas_1_bimestre = int(input("Digite o número de faltas do 1º bimestre: "))
faltas_2_bimestre = int(input("Digite o número de faltas do 2º bimestre: "))

# Cálculo da soma
total_faltas = faltas_1_bimestre + faltas_2_bimestre

# Saída dos resultados
print("\n" + "="*40)
print(f"Aluno: {nome_aluno}")
print(f"Faltas no 1º bimestre: {faltas_1_bimestre}")
print(f"Faltas no 2º bimestre: {faltas_2_bimestre}")
print(f"Total de faltas: {total_faltas}")
print("="*40)
