import random

# Cria uma tupla com os lados de um dado
DADO = (1, 2, 3, 4, 5, 6)

# Escolhe de forma aleatória um lado do dado 5 vezes
resultado = tuple(random.choice(DADO) for _ in range(5))

# Imprime o resultado e o seu tipo
print(f"Resuldado : {resultado}")
print(type(resultado))
