# Imprime no terminal o conjunto com três elementos
print({1, 2, 3})  # {1, 2, 3}
# Imprime o tipo do conjunto
print(type({1, 2, 3}))  # <class 'set'>
# Cria a variável "conj" e descarta os elementos duplicados
conj = {1, 2, 3, 3, 3, 3, 3}  # o mesmo que conj = {1, 2, 3}
"""Os conjuntos não possuem indexação igual as listas e tuplas, por tanto não é
possivel acessar elementos pelo indíce, dando TypeError"""
# print(conj[1])
# Imprime os elementos do conjunto
print(conj)  # {1, 2, 3}
# Imprime a quantidade de elementos dentro do conjunto
print(len(conj))
