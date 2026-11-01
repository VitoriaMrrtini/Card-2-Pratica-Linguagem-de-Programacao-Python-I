# Define uma classe para representar um produto
class Produto:
    # Os valores de preço e desconto possuem valores por padrão
    def __init__(self, nome, preco=1.99, desc=0):
        # Construtor recebe nome, preço e desconto
        self.__nome = nome
        self.preco = preco
        self.desc = desc

    # @property permite acessar o método como se fosse um atributo
    @property
    def preco(self):
        return self.__preco  # Os "__" altera de forma interna para torna-lo privado

    # Setter da propriedade "preco"
    @preco.setter
    def preco(self, novo_preco):
        # Encontra os preços maiores que zero
        if novo_preco > 0:
            self.__preco = novo_preco

    # Calcula o preço final aplicando o desconto
    @property
    def preco_final(self):
        return (1 - self.desc) * self.preco


# Cria dois produtos diferentes com nome, preço e desconto
p1 = Produto("Caneta", 5.99, 0.1)  # Produto.__init__(p1)
p2 = Produto("Caderno", 12.99, 0.2)

# Atribui valores negativos
# p1.preco = -70
# p2.preco = -1.99
p1.preco = 17.99
p2.preco = 15.99

# Imprime as informações dos produtos e seus preços após o desconto
# O acesso direto a p1.__nome e p2.__nome fora da classe resulta no erro "AttributeError"
print(p1.__nome, p1.preco, p1.desc, p1.preco_final)
# print(p2.__Produto__nome, p2.preco, p2.desc, p2.preco_final) # Usa o name mangling para acessar diretamente o atributo privado
print(p2.__nome, p2.preco, p2.desc, p2.preco_final)
