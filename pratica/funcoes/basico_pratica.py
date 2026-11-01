# Importa a biblioteca math para usar a raiz quadrada
import math


# Calcula o valor de delta para a equação de segundo grau
def calcular_delta(a, b, c):
    return pow(b, 2) - 4 * a * c


# Resolve utilizando a fórmula de bhaskara
def resolve_equação(a, b, delta):
    # Se delta for negativo a equação não possui raízes reais
    if delta < 0:
        return "A equação não possui raízes reais"
    # Faz o calculo das duas raízes
    x1 = (-b) + math.sqrt(delta) / (2 * a)
    x2 = (-b) - math.sqrt(delta) / (2 * a)
    # Retorna as duas raízes
    return x1, x2


equacao_um = resolve_equação(1, -5, calcular_delta(1, -5, 6))
print(f"Raízes da equação: {equacao_um}")
