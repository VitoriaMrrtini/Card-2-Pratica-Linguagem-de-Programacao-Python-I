# Faz uma importação da função reduce do módulo functools
from functools import reduce

# Cria uma lista de dicionários, com nome do aluno e a sua nota
aluno = [
    {"nome": "Ana", "nota": 7.2},
    {"nome": "Breno", "nota": 8.1},
    {"nome": "Claudia", "nota": 8.7},
    {"nome": "Pedro", "nota": 6.4},
    {"nome": "Rafael", "nota": 6.7},
]

# Cria uma função lambda recebendo dois valores e retorna a soma deles
somar = lambda a, b: a + b

# Cria uma lista contendo o dicionário dos alunos que tiraram uma nota ou igual a 7
alunos_aprovados = [aluno["nota"] for aluno in aluno if aluno["nota"] >= 7]
# Extrai os valores das notas da lista de alunos aprovados
notas_alunos_aprovados = [aluno["nota"] for aluno in alunos_aprovados]
# Utiliza a função criada "somar" para iterar sobre as notas, e obter o valor acumulado
total = reduce(somar, notas_alunos_aprovados, 0)
# Imprime média do valor total da soma pela quantidades de alunos aprovados
print(total / len(alunos_aprovados))
