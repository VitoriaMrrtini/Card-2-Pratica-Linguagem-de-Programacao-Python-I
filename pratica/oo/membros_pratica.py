class Estacionamento:
    # Atributo classe é compartilhado com todos os carros
    vagas_ocupadas = 0

    def __init__(self, placa: str):
        # Atributo instância pertence apenas a esse carro
        self.placa = placa

    # Método instância, usa "self" para acessar a placa do carro
    def estacionar(self):
        Estacionamento.vagas_ocupadas += 1
        print(f"O Carro de placa {self.placa} estacionou")

    # Método classe usa "cls" gerencia o atributo global da classe
    @classmethod
    def obter_vagas(cls):
        return f"Há um {cls.vagas_ocupadas}total de carros estacionados"

    # Método estático, não possui "self" e nem "cls"
    @staticmethod
    def validar_placa(placa: str) -> bool:
        # Valida se a placa tem 7 caracteres
        return len(placa) == 7


placa_um = "ABC1D23"
print(f"A placa {placa_um} é valida? {Estacionamento.validar_placa(placa_um)}")
carro_um = Estacionamento(placa_um)
carro_um.estacionar()
print(Estacionamento.obter_vagas())
