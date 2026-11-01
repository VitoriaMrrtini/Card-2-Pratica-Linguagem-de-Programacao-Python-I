# Dados do aluno
nome = "Vitoria MArtins Alves"
idade = "19"
nota = "7.5"
presenca = "0.9"
aprovado = True

print(
    f" O aluno(a) {nome} tem {idade} anos,\nEstá com {float(presenca) * 100}% de presença e com ststus de aprovado como {aprovado}"
)

# Verificando o tipo das variáveis
print(type(idade))
print(type(nota))
print(type(presenca))

# Convertendo para o formato desejado
print(int(idade))
print(float(nota))
print(float(presenca))
