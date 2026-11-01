# Define se o funcionário está vestindo o capacete
possui_capacete = True
# Define se o funcionário está vestindo o colete reflexivo
possui_colete = True
# Avalia se o Equipamento de Proteção Individual (EPI) está completo
EPI_completo = (
    "Sim, tem EPI completo"
    if possui_capacete and possui_colete
    else "Não possui EPI suficiente"
)

# Validação final
print(f"O funcionário possui o EPI necessário: \n{EPI_completo}")
