ALTURA_MAX = 1.90
ALTURA_MINIMA = 1.65
IDADE_MINIMA = 18

idade = 18
altura = 1.60

# Verifica se a idade da pessoa condiz com a condição
possui_idade = idade >= IDADE_MINIMA
print(f"A pessoa possui a idade miníma para entrar no brinquedo? {possui_idade}")
# Verifica se a altura da pessoa condiz com a condição
possui_altura = altura >= ALTURA_MINIMA and altura <= ALTURA_MAX
print(f"A pessoa possui altura para entrar no brinquedo? \n{possui_altura}")
