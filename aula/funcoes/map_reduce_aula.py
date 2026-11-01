# Importa reduce para reduzir os valores para um único resultado
from functools import reduce


# Cria uma função adicionando "delta" como nota
def somar_nota(delta):
    # Função interna que recebe a nota e soma com o valor da função anterior
    def somar(nota):
        return nota + delta

    # Retorna a função interna
    return somar


# Lista de notas
notas = [6.4, 7.2, 5.8, 8.4]

# Aplica map na função "somar_nota" para cada nota
notas_finais_1 = map(somar_nota(1.5), notas)
# Aplica outro map na função "somar_nota" para cada nota, porém com outro valor
notas_finais_2 = map(somar_nota(1.6), notas)

# Imprime os objetos do map
print(notas_finais_1)  # <map object at 0x7f22ebcaa170>
print(notas_finais_2)  # <map object at 0x7f22ebcaa1d0>
print(list(notas_finais_1))  # [7.9, 8.7, 7.3, 9.9]
print(list(notas_finais_2))  # [8.0, 8.8, 7.4, 10.0]


# Um função que adiciona um meio as notas
# def mais_um_meio(nota):
#     return nota + 1.5

# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5


# Cria função somar que é usada pelo reduce, soma dois argumentos
def somar(a, b):
    return a + b


# O reduce vai acumular os valores da lista, o valor 0 define o valor do acumulador
total = reduce(somar, notas, 0)
# Equivale ao reduce acima
# total = 0
# for n in notas:
#     total += n
print(total)
