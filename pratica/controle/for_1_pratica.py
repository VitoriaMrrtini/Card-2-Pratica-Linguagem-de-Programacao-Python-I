# Importa a biblioteca random para escolher um filho aleatório
import random


# Lista com nome de Filhos
filho = ["Vitoria", "Vinicius", "Roberto", "Maycon"]
# Lista de tarefas
tarefa = ["Limpar a casa", "Lavar a Louça", "Lavar o banheiro"]

# Embaralha a lista de forma aleatória
random.shuffle(filho)

# Associa a cada tarefa um filho diferente
for f, t in zip(filho, tarefa):
    print(f"{f} vai {t}!")
