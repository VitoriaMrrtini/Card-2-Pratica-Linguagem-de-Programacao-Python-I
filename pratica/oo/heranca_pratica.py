class Funcionario:
    def __init__(self, nome, salario):
        # Os atributos são compartilhados por todos os funcionários
        self.nome = nome
        self.salario = salario

    # Retorna o salário padrão
    def retorna_salario(self):
        return self.salario

    # Retorna uma mensagem com as informações do funcionário
    def exibir_dados(self):
        return f"Nome funcionário: {self.nome}, salário R${self.salario},"


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        # O super() chama o construtor __init__ da classe pai nesse caso funcionário
        super().__init__(nome, salario)
        # Atributo específico da classe Gerente
        self.bonus = bonus

    # Calcula a soma do salario mais o bonus recebido como gerente
    def calcula_salario(self):
        return super().retorna_salario() + self.bonus

    # Retorna a mensagem com as informações de gerente, agora com o salário junto do bonus
    def exibir_dados(self):
        salario_total = self.calcula_salario()
        return f"Nome Gerente: {self.nome}, salário total R${salario_total:.2f}."


# Criando um funcionário
funcionario_um = Funcionario("Roberto", 3000.0)
print(funcionario_um.exibir_dados())

# Criando um gerente
gerente_um = Gerente("Roberto", 3000.0, 2000.0)
print(gerente_um.exibir_dados())
