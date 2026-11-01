# Solicita para o usuário informar a nota do aluno e converte para decimal
nota = float(input("Informe nota do aluno: "))
# Verifica de o usuário respondeu com "y", caso sim a variável recebe True,
# caso contrário recebe False
comportado = True if input("Comportado? (s/n)") == "y" else False

# Verifica a condição da nota ao mesmo tempo do comportamento
# Se a nota for maior ou igual que 9 e o comportamento for True 
if nota >= 9 and comportado:
    print("Duas palavras: para bens! :P")
    print("Quadro de honra")
# Se a nota for maior ou igual que 7
elif nota >= 7:
    print("Aprovado")
# Se a nota for maior ou igual que 5.5
elif nota >= 5.5:
    print("Recuperação")
# Se a nota for maior ou igual que 3.5
elif nota >= 3.5:
    print("Recuperação + Trabalho")
# Se não nenhuma das condições acima
else:
    print("Reprovado")
# Imprime a nota
print(nota)
