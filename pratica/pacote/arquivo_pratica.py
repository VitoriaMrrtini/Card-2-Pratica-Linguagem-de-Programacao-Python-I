def maior_de_idade(idade: int) -> bool:
    # Verifica se a pessoa tem mais de 18 anos
    return idade >= 18

if __name__ == "__main__":
    idade_pessoa = 15
    pode_beber = maior_de_idade(idade_pessoa)
    print(f"A pessoa que tem {idade_pessoa} idade, pode beber?\n{pode_beber}")