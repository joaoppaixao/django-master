# repetição - for 
def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

clientes = ['Bruna', 'João', 'Matheus', 'Alana']

for cliente in clientes:
    envia_email(cliente)

# repetição - while 
numero = 0

while numero <= 5:
    print(numero)
    numero += 1