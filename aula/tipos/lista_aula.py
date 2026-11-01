# Cria lista com três inteiros
nums = [1, 2, 3]
# Imprime o tipo da variável, no caso uma lista
print(type(nums))  # <class 'list'>

# Adicione um alemento ao final da lista
nums.append(3)  # [1, 2, 3, 3]
nums.append(4)  # [1, 2, 3, 3, 4]
nums.append(500)  # [1, 2, 3, 3, 4, 500]

# Imprime no terminal a quantidade de elemento da lista
print(len(nums))  # 6


# Confirma se o 2 está presente na lista
print(2 in nums)  # True

# Altera o elemento no índice 3 pelo valor 100
nums[3] = 100  # [1, 2, 3, 100, 4, 500]

# Adiciona o valor na primeira posicão
nums.insert(0, -200)  # [-200, 1, 2, 3, 100, 4, 500]

# Imprime o valor na posição 5
print(nums[5])  # 4
# Imprime o valor da ultima posição
print(nums[-1])  # 500
# Imprime o valor da penúltima posição
print(nums[-2])  # 4

# Imprime a lista completa
print(nums)  # [-200, 1, 2, 3, 100, 4, 500]
