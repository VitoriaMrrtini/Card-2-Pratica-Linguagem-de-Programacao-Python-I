# Função que soma duas variáveis
def soma(a, b):
    return a + b


# Função que subtrai duas variáveis
def sub(a, b):
    return a - b


# Armazena na variável "somar" a função "soma" e imprime no terminal
somar = soma
print(somar(3, 4))


# Recebe uma função como argumento e retorna dentro a função "operacao_aritmetica"
def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)


# A função "operacao_aritmetica" recebe "soma" como argumento
resultado = operacao_aritmetica(soma, 13, 48)
print(resultado)

# A função "operacao_aritmetica" recebe "sub" como argumento
resultado = operacao_aritmetica(sub, 13, 48)
print(resultado)


# Cria uma função e retorna outra função
def soma_parcial(a):
    # Processamento pesado 1 - 10s
    # Processamento pesado 2 - 10s
    # Processamento pesado 3 - 40s

    # Esta função interna mantém acesso ao valor "a" da função externa
    def concluir_soma(b):
        return a + b

    # Retorna a função interna
    return concluir_soma


# Exemplos conceituais de chamadas que poderiam repetir o processamento pesado
# r1 = soma_total(1,2) => 1m10s
# r2 = soma_total(1,3) => 1m10s
# r3 = soma_total(1,4) => 1m10s


# Cria uma variável que armazena a função soma_parcial com o argumento a = 1
soma_1 = soma_parcial(1)
# Reutiliza a função com diferentes valores para b
r1 = soma_1(2)
r2 = soma_1(3)
r3 = soma_1(4)

# Cria a função e chama instantaneamente

resultado_final = soma_parcial(10)(12)
# Mesmo que a sequência abaixo
# fn = soma_parcial(10)
# resultado_final = fn(12)
print(resultado_final)

# Imprime o resultado
print(resultado_final, r1, r2, r3)
