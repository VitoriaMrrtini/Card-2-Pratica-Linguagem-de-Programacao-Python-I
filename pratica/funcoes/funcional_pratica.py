# Recebe o valor base e a taxa de imposto
def aplicar_imposto(valor, taxa=0.18):
    return valor * (1 + taxa)


# Recebe o peso do produto e qual estado será enviado
def calcular_frete(estado="PR"):
    # Taxa base de acordo com o estado
    taxa_regiao = 15.0 if estado == "PR" else 35.0

    # Vai acessar da função pai a "taxa_região"
    def calcular_por_peso(peso):
        return taxa_regiao + (peso * 2.5)

    return calcular_por_peso


# Calcular o produto com imposto
preco_produto = 140.0
imposto_produto = aplicar_imposto(preco_produto)
print(f"Preço com imposto: R${imposto_produto}")

# Frete para dois estados SP e PR
calcular_frete_pr = calcular_frete("PR")
calcular_frete_sp = calcular_frete("SP")

# Calculo do frete com base no peso (kg)
frete_pr = calcular_frete_pr(1.5)
frete_sp = calcular_frete_sp(5.0)

print(f"Frete para pacote do Paraná: R${frete_pr}")
print(f"Frete para pacote de São Paulo: R${frete_pr}")
