#!python3
# A classe base representando um Carro
class Carro:
    # É o método construtor escrito como __init__, inicia a velocidade como 0
    def __init__(self):
        self.__velocidade = 0

    """@property é um getter, ou seja decorador embutido que transforma
    um método de uma classe em um atributo gerenciador"""

    @property
    def velocidade(self):
        return self.__velocidade

    # Incrementa 5 na velocidade e retorna o valor
    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade

    # Decrementa 5 na velocidade e retorna o valor
    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade


# O Uno herde de Carro os mesmo comportamentos
class Uno(Carro):
    pass


# A Ferrari herde de Carro os mesmo comportamentos
class Ferrari(Carro):
    # Escreve por cima do método acelerar alterando o comportamento
    def acelerar(self):
        # O "super()" acessa a implementação da classe pai
        super().acelerar()
        # Aumenta a velocidade em 5 de novo
        return super().acelerar()


# Cria o objeto da Classe Ferrari
c1 = Ferrari()
# Executa 3 vezes a aceleração e a frenagem
print(c1.acelerar())  # 10
print(c1.acelerar())  # 20
print(c1.acelerar())  # 30
# A frenagem continua decrementando de 5 em 5
print(c1.frear())  # 25
print(c1.frear())  # 20
print(c1.frear())  # 15
