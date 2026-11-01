# Define se o funcionário está vestindo o capacete
possui_capacete = True
# Define se o funcionário está vestindo o colete reflexivo
possui_colete = False
# Avalia se o Equipamento de Proteção Individual (EPI) está completo
EPI_completo = possui_capacete and possui_colete

# Imprime individualmente cada equipamento
print(f"O funcionário possui capacete: {possui_capacete}")
print(f"O funcionário possui colete: {possui_colete}")
# Validação final
print(f"O funcionário possui o EPI necessário: {EPI_completo}")
