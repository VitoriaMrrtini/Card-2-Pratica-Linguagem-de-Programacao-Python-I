# Lista de pesos por kg
pesos_bagagens = [12.5, 18.0, 35.0]
# Estabelece o peso maximo
limite_peso = 23.0

for peso in pesos_bagagens:
    # Caso a mala esteja no peso permitido, passa para a proxima
    if peso <= limite_peso:
        print("Mala está dentro do limite!")
        continue
    print(
        f"A mala excede o peso limite por {peso - limite_peso}kg, remova o excesso de peso"
    )
    break  # Para a verificação de todas as malas
