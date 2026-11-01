# Senha correta como uma constante
SENHA = "1234"
# Número máximo de tentativas
tentativas = 3
# O laço roda enquanto houver tentativas e se a senha não for digitada corretamente
while tentativas > 0:
    senha_digitada = input("Digite a senha do cartão: ")
    # Verifica se a senha digitada está correta
    if senha_digitada == SENHA:
        print("Pode retirar o cartão.")
        break
    else:
        tentativas -= 1
    # Mostra o número de tentativas restantes, se as tentativas acabarem o laço se encerra
    if tentativas > 0:
        print(f"Senha incorreta! Você possui {tentativas} restantes antes de bloquear seu cartão")
    else:
        print("Cartão bloqueado! Para desbloquear o cartão vá para o caixa da sua agência.")