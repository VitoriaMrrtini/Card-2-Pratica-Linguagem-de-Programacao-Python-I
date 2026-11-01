"""PEP (Python Enhancement Proposal) É documentos oficial que descrevem
funcionalidades, convenções ou processos para a linguagem python
"""


# O "*" permite receber uma quantidade aleatória de argumentos posicionais
def soma(*nums):
    # Cria um totalizador começando no zero
    total = 0
    # Percorre os elementos recebidos
    for n in nums:
        total += n
    # Retorna a soma dos elementos
    return total


# O "**" permite receber uma quantidade aleatória de argumentos nomeados
def resultado_final(**kwargs):
    # Verifica a variável recebida no dicionário "kwargs"
    status = (
        "aprovado(a)" if kwargs["nota"] >= 7 else "reprovado(a)"
    )  # Se a nota for maior ou igual a 7 armazena a string "aprovado(a)"
    # Retorna a mensagem com o nome e o status da nota
    return f"{kwargs['nome']} foi {status}"
