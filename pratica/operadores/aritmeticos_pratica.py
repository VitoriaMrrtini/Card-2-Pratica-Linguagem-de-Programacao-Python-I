# Valor original da compra sem o desconto
valor_da_compra = 450.0
# Valor em dinheiro entregue
valor_pago = 500.0
# Percento de desconto
desconto = 0.1

# Valor final da compra após o desconto
compra_com_desconto = valor_da_compra * (1 - desconto)
# Troco que deve ser devolvido ao cliente
troco = valor_pago - compra_com_desconto

print(f"Valor da compra com desconto: R$ {compra_com_desconto:.2f}")
print(f"Troco a devolver: R$ {troco:.2f}")
