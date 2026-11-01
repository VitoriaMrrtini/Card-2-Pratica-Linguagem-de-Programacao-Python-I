# Lista com nomes
pessoas = ["Gui", "Rebeca"]
# Lista de adjetivos
adjs = ["Sapeca", "Inteligente"]

# Para cada pessoa é combinada um nome e um adjetivo, isso é um laço aninhado
for p in pessoas:
    for a in adjs:
        print(f"{p} é {a}!")

# O "pass" não vai ser executado (Pode ser usado temporariamente)
for i in [1, 2, 3]:
    pass

# Vai percorrer um número de 1 a 9
for i in range(1, 10):
    # Caso for impar, passa para a próxima repetição e imprime os valores par
    if i % 2:
        continue
    print(i)

# Percorre de 1 a 10
for i in range(1, 11):
    # Acaba com o laço de repetição quando chegar em 5
    if i == 5:
        break
    print(i)

# Sinaliza que o programa acabou
print("Fim!")
