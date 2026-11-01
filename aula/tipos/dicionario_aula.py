# Um dicionàrio com informações de um aluno
aluno = {"nome": "Pedro Henrique", "nota": 9.2, "ativo": True}

# Imprime o tipo da variável
print(type(aluno))  # <class 'dict'>
# Acessa o valor associado a chave "nome"
print(aluno["nome"])  # Pedro Henrique
# Acessa o valor associado a chave "nota"
print(aluno["nota"])  # 9.2
# Acessa o valor associado a chave "ativo"
print(aluno["ativo"])  # True
# Imprime a quantidade de chaves presentes no dicionário
print(len(aluno))  # 3
