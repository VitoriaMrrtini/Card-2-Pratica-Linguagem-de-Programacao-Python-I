class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self.__titular = titular  # Atributo privado
        self.saldo = saldo  # Usa o setter para validar o valor inicial

    # Getter para o titular
    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    # Setter para saldo
    @saldo.setter
    def saldo(self, novo_saldo):
        # O saldo não pode ser definido como negativo diretamente
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print(f"Digite um valor positivo para o saldo!")

    # Property calculada
    # O saldo limite é sempre 50% do saldo
    @property
    def limite_credito(self):
        return self.saldo * 0.5


conta_um = ContaBancaria("Vinicius", 1500.0)
conta_um.saldo = 2000.0
conta_um.saldo = -10.0  # Digite um valor positivo para o saldo!

print("-" * 50)

print(
    f"Nome do Titular: {conta_um.titular} \nSaldo Atual da Conta: {conta_um.saldo} \nLimite de Saldo: {conta_um.limite_credito}"
)

print("-" * 50)
