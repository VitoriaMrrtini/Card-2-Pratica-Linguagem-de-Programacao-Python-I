# *notas vai receber quantas notas o professor quiser passar.
# **opcoes recebe configurações extras
def calcular_media_notas(aluno, *notas, **opcoes):

    # Vai calcular a média total das notas
    media = sum(notas) / len(notas)

    # Extrai os valores padrão de configuração
    bonus = opcoes.get("bonus", 0.0)
    mostrar_status = opcoes.get("status", False)

    # aplica o bonus na média das notas
    media_final = media + bonus

    # Monta a frase base
    resultado = f"O aluno(a): {aluno}, possui média: {media_final:.2f}"

    # Se o status for True vai passar pelo if e mandar a situação como "Aprovado(a)"
    # Caso contrário se o status for False vai mandr a situação como "Reprovado(a)"
    if mostrar_status:
        situacao = "Aprovado(a)" if media_final >= 6.0 else "Reprovado(a)"
        resultado += f", sua situação é: {situacao}."

    return resultado


# Pode passar sem o **kwargs sem erro
# Passa bônus e status por meio de **kwargs
aluno_um = calcular_media_notas("Vitoria", 9.0, 7.5, 8.2, 8.7, bonus=0.5, status=True)
print(aluno_um)  # O aluno(a): Vitoria, possui média: 8.85, sua situação é: Aprovado(a).
