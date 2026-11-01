# Cria uma tupla com quatro nomes
# Tuplas não podem ser modificadas após sua criação
nomes = ("Ana", "Bia", "Gui", "Leo", "Ana")

""" Compara as letra maiúsculas e minúsculas, a palavra "Bia" não é encontrada,
pois na tupla existe "Bia" """
print("bia" in nomes)  # False

# Encontra exatamente a palavra "Bia"
print("Bia" in nomes)  # True


# Acessa a tupla por meio de índices, assim como nas listas
print(nomes[0])  # Ana
# Encontra do índice 1 até antes do índice 2
print(nomes[1:2])  # ('Bia',)
# Encontra do ìndice 1 até antes do ultimo ìndice
print(nomes[1:-1])  # ('Bia', 'Gui', 'Leo')
# Encontra do índice 2 até o último índice
print(nomes[2:])  # ('Gui', 'Leo', 'Ana')
# Encontra do primeiro índice até antes do penúltimo índice
print(nomes[:-2])  # ('Ana', 'Bia', 'Gui')

# Imprime a quantidade de elemntos dentro da tupla
print(len(nomes))  # 5

# Mostra qual é o tipo da estrutura
x = ("Bia",)
print(type(x))  # <class 'tuple'>

print(type(nomes))  # <class 'tuple'>

# Imprime a tupla inteira
print(nomes)  # ('Ana', 'Bia', 'Gui', 'Leo', 'Ana')
