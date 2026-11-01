remedios = [
    {"nome": "Dorflex", "preco": 19.99},
    {"nome": "Dipirona Monoidratada", "preco": 5.99},
    {"nome": "Ibuprofeno", "preco": 16.99},
]
# Ordena a lista de remédios em ordem crescente
remedios_ordenados = sorted(remedios, key=lambda remedio: remedio["preco"])
print(
    remedios_ordenados
)  # [{'nome': 'Dipirona Monoidratada', 'preco': 5.99}, {'nome': 'Ibuprofeno', 'preco': 16.99}, {'nome': 'Dorflex', 'preco': 19.99}]

# Aplica desconto de 20% em cada dicionário, o map cria um novo dicionário
remedios_promocao = list(
    map(
        lambda r: {"nome": r["nome"], "preco": round(r["preco"] * 0.8, 2)},
        remedios_ordenados,
    )
)
print(remedios_promocao)
# Filtra os dicionários mantendo os remédios com preço menor que 9,99
remedios_menores = list(filter(lambda r: r["preco"] <= 9.99, remedios_promocao))
print(remedios_menores)
