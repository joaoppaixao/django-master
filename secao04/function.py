# funcao de soma
def somar(a, b):
    resultado = a + b
    return resultado

print(somar(2, 5))


# funcao de cadastro
def cadastrar():
    nome = input("Digite seu nome: ")
    sexo = input("Digite seu sexo (M ou F): ")

    if (sexo == 'M' or sexo == 'm'):
        print("Seja bem-vindo, " + nome.title() + "!")
    elif (sexo == 'F' or sexo == 'f'):
        print("Seja bem-vinda, " + nome.title() + "!")

print(cadastrar())