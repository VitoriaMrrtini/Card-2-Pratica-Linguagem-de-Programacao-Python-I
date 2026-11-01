# Estabelece a velocidade máxima da via
VELOCIDADE_MAX = 60

# Pergunta para o usuário a cor do sinal e a sua velocidade
sinal_semaforo = input("Digite a cor do sinal: (vermelho/amarelo/verde) ")
velocidade = int(input("Digite a velocidade do carro: "))
# Salva o valor das multas e pontos na carteira
pontos_carteira = 0
multa = 0

# Faz uma comparação entre a velocidade máxima e a velocidade do morista
if velocidade > VELOCIDADE_MAX and velocidade <= VELOCIDADE_MAX * (1 - 0.2):
    # Velocidade entre 61km/h até 72km/h
    multa += 130.16
    pontos_carteira += 4
elif velocidade > VELOCIDADE_MAX * (1 - 0.2) and velocidade >= VELOCIDADE_MAX * (
    1 - 0.5
):
    # Velocidade entre 73km/h até 90km/h
    multa += 195.23
    pontos_carteira += 5
elif velocidade > VELOCIDADE_MAX * (1 - 0.5):
    # Velocidade acima de 90km/h
    multa += 880.41
    pontos_carteira += 7
else:
    # Se nenhum dos casos forem verdadeiros
    pass

# Verifica se o semáfaro estava vermelho
if sinal_semaforo == "vermelho":
    multa += 293.47
    pontos_carteira += 7

# Imprime o resultado
print(f"Sua multa é de {multa:.2f}")
print(f"Possui {pontos_carteira} pontos na carteira")
