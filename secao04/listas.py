clientes = ['Bruna', 'João', 'Matheus', 'Alana']

print(clientes[0])

# criando uma lista vazia
carros = ['Golf', 'Audi']

# adicionando elementos com a função append()
carros.append('Ferrari')

print(carros)

# adicionando elementos no meio de listas (sem ser no último índice)
carros.insert(1, 'BMW')

print(carros)

# removendo o último elemento da lista com pop()
carros.pop()

print(carros)

# removendo elementos da lista pelo índice com del
del carros[2]

print(carros)

# removendo elementos da lista pelo valor 
carros.remove('BMW')

print(carros)