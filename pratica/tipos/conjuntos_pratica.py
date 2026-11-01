# Materias
# Cria um conjunto/set com as matérias obrigatórias na grade
materias_obrigatorias = {"Introdução a Programação", "Pré-Calculo", "Algoritmos"}
# Cria um conjunto/set com as matérias já concluidas
materias_concluidas = {"Introdução a Programação", "Pré-Calculo", "Banco de Dados"}
# Retorna adiferença entre os conjuntos
materias_a_fazer = materias_obrigatorias.difference(materias_concluidas)
# Retorna união dos conjuntos
todas_as_materias = materias_obrigatorias.union(materias_concluidas)

print(materias_a_fazer)
print(todas_as_materias)
