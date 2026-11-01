# Atribui valores booleanos as 3 variáveis
b1 = True
b2 = False
b3 = True
# O "and" retorna True quando todas as condições forem verdadeiras
print(b1 and b2 and b3)  # False
# O "or" retorna True quando qualquer uma das condições forem verdadeiras
print(b1 or b2 or b3)  # True
# O "!=" é usado como uma comparação de diferença
print(b1 != b2)  # xor
# O "not" inverte o valor do booleano
print(not b1)  # False
print(not b2)  # True
"""Combina os operadores lógicos and e
not para tornar a condição verdadeira"""
print(b1 and not b2 and b3)  # True

# Atribui valores para as variáveis x e y
x = 3
y = 4

# Faz uma comparação entre valores lógicos e relacionais
print(b1 and not b2 and x < y)  # True
