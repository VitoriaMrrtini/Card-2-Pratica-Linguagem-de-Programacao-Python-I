# Cria a variável e armazena o inteiro 10
x = 10

# Decrementa de x até o valor chegar a 0,
# ou seja faz um loop até a condição ser falsa
while x:
    print(x)
    x -= 1

# print("Fim!")

# Acumula a soma das notas
total = 0
# Armazena quantas notas foram informadas
qte = 0
# Armazena a última nota informada
nota = 0

# Continua até a nota informada for -1
while nota != -1:
    # Solicita a nota para o usuário e converte para float
    nota = float(input("Informe a nota ou -1 para sair: "))
    # Compara a nota a -1 para que não entre dentro do calculo total
    if nota != -1:
        # Incrementa a quantidade de notas
        qte += 1
        # Soma a nota ao total
        total += nota

# Imprime a média das notas informadas
print(f"A média da tuma é {total / qte}")
