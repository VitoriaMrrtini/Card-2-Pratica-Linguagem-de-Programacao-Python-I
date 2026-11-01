from functools import reduce


# Função criada para configurar uma taxa por item
def aplicar_taxa_embalagem(valor_taxa):
    def calcular_preco_final(preco_marmita):
        return preco_marmita + valor_taxa

    return calcular_preco_final


# Cria uma lista com o pedido
marmita = [32.0, 18.0, 24.0]

# Aplica a taxa para cada marmita
marmita_com_embalagem = map(aplicar_taxa_embalagem(2.5), marmita)

# Cria uma lista já com o preço bruto mais a embalagem
marmitas_ajustadas = list(marmita_com_embalagem)
# Imprime os preços
print(
    f"Preço das marmitas com embalagem: {marmitas_ajustadas}"
)  # Preço das marmitas com embalagem: [34.5, 20.5, 26.5]


# Faz a soma total
def somar(acumulador, preco):
    return acumulador + preco

# Faz o total do pedido do cliente
total_pedido = reduce(somar, marmitas_ajustadas)
print(f"Total do Pedido: {total_pedido} reais")
