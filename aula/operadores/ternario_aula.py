# Define se está em lockdown ou não
lockdown = False
# Define quando reais possui
grana = 30

"""Escolhe quais string vai armazenar dependendo da condição,
"Em casa" só será escolhido se a consição de lockdown for True e a variável
grana for menor ou igual a 100 """
status = "Em casa" if lockdown or grana <= 100 else "Uhuuuu"

# Imprime o resultado de status
print(f"O status é {status}")  # O status é Em casa
