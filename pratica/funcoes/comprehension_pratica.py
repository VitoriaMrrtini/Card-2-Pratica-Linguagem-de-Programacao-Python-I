remedios = [12.50, 8.00, 15.00, 9.50, 5.00]

# Aplica o desconto de 20% e filtra < 10.00 na mesma linha:
remedios_com_desconto = [preco * 0.8 for preco in remedios if (preco * 0.8) <= 9.99]

print(remedios_com_desconto)