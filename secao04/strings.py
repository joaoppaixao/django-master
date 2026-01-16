# 015- Strings e seus métodos

texto = 'AULA PYCODEBR'

# retorna tudo a frente do caracter 4

print(texto[:4])

# mostra a quantidade de vezes que o caracter 'A' aparece

print(texto.count('A'))

# transforma tudo em minúscula

print(texto.lower())

# transforma as iniciais de cada palavra para maiúsculas

print(texto.title())

# separa as palavras por espaço, retornando uma lista das palavras

print(texto.split())

# o join serve para juntar as palavras

lista_de_palavras = texto.split() 
print(' '.join(lista_de_palavras))