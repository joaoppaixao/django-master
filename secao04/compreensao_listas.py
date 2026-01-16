numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados) 

# realizando a mesma ação com compreensão de listas
# [ expr for item in list ]

dobro = [numero * 2 for numero in numeros]

print(dobro)

# exercicio: convertendo lista para maiúsculo e adicionando a uma nova lista
nomes = ['João', 'Bruna', 'Matheus', 'Alana', 'Milani']

# [ expr for item in list cond ]
nomes_maiusculos = [nome.upper() for nome in nomes if nome[0] == 'M']

print(nomes_maiusculos)