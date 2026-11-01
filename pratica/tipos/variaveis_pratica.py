# Constantes
VALOR_POR_HORA = 5.0
VALOR_POR_MINUTO_EXTRA = 2.5 / 30

# Dados de Entrada
cliente = input("Digite seu nome completo: ")
horas_principais = int(input("Digite as horas estacionados: "))
minutos_extra = int(input("Digite os minutos extras estacionados: "))

# Calculos de preço
custo_horas = VALOR_POR_HORA * horas_principais
custo_extra = VALOR_POR_MINUTO_EXTRA * minutos_extra
preco_total =  custo_horas + custo_extra

# Dados de Saída
print(f"Cliente: {cliente}")
print(f"Tempo total: {horas_principais}h e {minutos_extra}min")
print(f"Valor pelas horas: R$ {custo_horas:.2f}")
print(f"Valor pelos minutos extras: R$ {custo_extra:.2f}")
print(f"Total a pagar: R$ {preco_total:.2f}")
