# Define a função saudacao com os valores padrão para nom e idade
def saudacao(nome="Pessoa", idade=20):
    # Imprime uma mensagem com o nome e idade, utilizando a f-string
    print(f"Bom dia {nome}!\nVocê nem parece ter {idade} anos!")


# Exemplo simples da função saudacao
# def saudacao():
#     print("Boa tarde!")


# Define a função soma_e_multi
def soma_e_multi(a, b, x):
    # Retorna o calculo dos argumentos
    return a + b * x


# Verifica se o arquivo foi excutado diretamente
if __name__ == "__main__":
    # Exemplo da função saudacao
    saudacao("Ana", idade=30)
