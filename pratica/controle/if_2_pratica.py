usuario = input("Digite um nome de usuário: ")

# Envia uma mensagem para o usuário caso digite seu nome ou não
if usuario:
    print(f"Bem vindo(a), {usuario}")
else:
    print("Seu nome de usuário não pode ser vazio")
