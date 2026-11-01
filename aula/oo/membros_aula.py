#!python3

# Classe com atributo classe, método de classe e método estático
class Contador:
    # Atributo de classe que compartilha entre as instâncias
    contador = 0  # Atributos de classe

    """ Exemplo de método de instância que recebe "self"
    e muda o contador associado à instância"""

    def inc_maluco(self):
        self.contador += 1
        return self.contador

    """incremento foi simplificado para inc e
    decremento foi simplificado para dec"""

    # O @classmethod faz o método receber a própria classe como "cls"
    @classmethod
    def inc(cls):
        # Faz a incrementação do atributo de classe
        cls.contador += 1
        return cls.contador

    # Decremento
    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador

    # @staticmethod não recebe automaticamente self nem cls
    @staticmethod
    def mais_um(n):
        return n + 1


# Cria uma instância de contador
c1 = Contador()

# Imprime o método de classe diretamente pela classe várias vezes
print(c1.inc_maluco())

print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
print(Contador.mais_um(99))

# Imprime o método de instância várias vezes
print(c1.inc())
print(c1.inc())
print(c1.inc())
print(c1.dec())
print(c1.dec())
print(c1.dec())
