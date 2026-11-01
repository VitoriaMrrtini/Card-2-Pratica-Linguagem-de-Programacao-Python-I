# Cria um loop que vai de 0 até 9
for i in range(10):
    print(i, end=" ")  # 0 1 2 3 4 5 6 7 8 9

print("")

# Cria um loop que vai de 1 até 11, sem considerar realmente o 11
for i in range(1, 11):
    print(i, end=" ")  # 1 2 3 4 5 6 7 8 9 10

print("")

# Cria um loop que vai de 1 até 100 e pula de 7 em 7
for i in range(1, 100, 7):
    print(i, end=" ")  # 1 8 15 22 29 36 43 50 57 64 71 78 85 92 99

print("")

# Cria um loop que vai de 20 até 0 fazendo uma contagem regressiva de 3 em 3
for i in range(20, 0, -3):
    print(i, end=" ")  # 20 17 14 11 8 5 2

print("")

# O for percorre os elementos de uma lista
nums = [2, 4, 6, 8]
for n in nums:
    print(n, end=",")  # 2,4,6,8,

print("")

# String também podem percorrer caracteres por meio de um for
texto = "Python é muito massa!"

for letra in texto:
    print(letra, end=" ")  # P y t h o n   é   m u i t o   m a s s a !

print("")

# Elimina os duplicados do conjunto
for n in {1, 2, 3, 4, 4, 4}:
    print(n, end=" ")  # 1 2 3 4

print("")

# Cria um dicinário para produtos
produto = {"nome": "Caneta", "preco": 8.80, "desc": 0.5}

# Percorre as chaves do dicionário e acesso o valor por meio da chave
for atrib in produto:
    print(atrib, "==>", produto[atrib])

print("")

# items(): Retorna o par no formato chave e valor
for atrib, valor in produto.items():
    print(atrib, "==>", valor)

print("")

# values(): Retorna os valores do dicionário
for valor in produto.values():
    print(valor, end=" ")

print("")

# keys(): Retorna as chaves do dicionário
for atrib in produto.keys():
    print(atrib, end=" ")
