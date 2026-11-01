# Importa reduce para reduzir os valores para um único resultado
from functools import reduce

# Cria uma lista de dicionários, com nome do aluno e a aua nota
alunos = [
    {"nome": "Ana", "nota": 7.2},
    {"nome": "Breno", "nota": 8.1},
    {"nome": "Claudia", "nota": 8.7},
    {"nome": "Pedro", "nota": 6.4},
    {"nome": "Rafael", "nota": 6.7},
]
# Lambda é uma função anônima e curta
# Retorna "True" para o aluno que tirar uma nota ou igual a 7
aluno_aprovado = lambda aluno: aluno["nota"] >= 7
# Extrai os valores das notas de alunos
obter_nota = lambda aluno: aluno["nota"]
# Cria uma função lambda recebendo dois valores e retorna a soma deles
somar = lambda a, b: a + b

# Filter filtra elementos de uma lista, conjunto ou tupla com base em uma condição
# Filtra os alunos que obteram notas maiores ou iguais a 7
alunos_aprovados = filter(aluno_aprovado, alunos)
# A função map exttrai de cada aluno aprovado o valor da sua nota
notas_alunos_aprovados = map(obter_nota, alunos_aprovados)
# Percore as notas dos alunos aprovados e acumula (setado em 0) o valor total de todas as notas
total = reduce(somar, notas_alunos_aprovados, 0)

# Imprime a nota do terceiro aluno da lista e chama a função
print(obter_nota(alunos[2]))
# Imprime a lista completa com o dicionário de alunos
print(alunos)
"""[{'nome': 'Ana', 'nota': 7.2},
{'nome': 'Breno', 'nota': 8.1},
{'nome': 'Claudia', 'nota': 8.7},
{'nome': 'Pedro', 'nota': 6.4},
{'nome': 'Rafael',
'nota': 6.7}]"""
# Imprime a lista de alunos aprovados
print(alunos_aprovados)  # <filter object at 0x71aaa9d2e530>
# Imprime as notas de alunos aprovados
print(notas_alunos_aprovados)  # <map object at 0x71aaa9d2e500>
print(total / len(alunos_aprovados))  # TypeError
