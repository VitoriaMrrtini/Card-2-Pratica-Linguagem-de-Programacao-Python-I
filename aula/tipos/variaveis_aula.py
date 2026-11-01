#!python3

# Variável Inteira
a = 3
# Variável Decimal
b = 4.4

# Impriminto a soma das váriaveis a e b
print(a + b)  # 7.4

# Uma variável String com um texto
texto = "Sua idade é..."

# Uma variável chamada idade contendo um inteiro armazenado
idade = 23

""" Causa um erro do tipo TypeError, não é possível concatenar diretamente uma
 string com um inteiro"""
# print(texto + idade) # TypeError

# Uma possibilidade é converter o inteiro para uma string
# print(texto + str(idade))  # Sua idade é... 23

"""Ou utiliza o "f" antes das aspas para fazer uma f-string, concatenando as
duas variáveis por meio das chaves, como por exemplo: {variável}"""
print(f"{texto} {idade}")  # Sua idade é... 23

# O operador "*" de multiplicação repete uma string n vezes
saudacao = "bom dia"
print(3 * saudacao)  # bom diabom diabom dia

# A linguagem Python não possui constantes obrigatórias
# Variáveis em maiúsculo indicam valores que não podem ser alterados
PI = 3.14
PI = 3.1415
# Solicita o raio a circunferência e converte para o tipo decimal
raio = float(input("Informe o raio da circ? "))  # raio = 2.0
""" Armazena a variável "area" o calculo
da constante de PI multiplicado pelo raio ao quadrado"""
area = PI * pow(raio, 2)

# Imprime no terminal utilizando a f-string a área da circunfêrencia
print(f"A área da circ é {area} m2")  # A área da circ é 12.566 m2
