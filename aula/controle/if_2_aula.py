# Avalia os valores de acordo com "True" ou "False"
a = "valor"  # Se uma string contém um conteúdo é considerada como True
a = 0  # Se for igual a zero é considerado False
a = -0.00001  # Qualquer número diferente de zero é considerado True
a = ""  # Se uma string não contém nenhum conteúdo é considerada como False
a = " "  # Não está vazia então é True
a = []  # Lista vazia é considerada False
a = {}  # Dicionário vazio é considerado False

# O if vai avaliar se a condição, nesse caso a variável "a" é verdadeira
if a:
    print("Existe!!!")
else:
    print("não existe ou zero ou vazio...")
