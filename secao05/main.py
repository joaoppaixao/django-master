class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'

    def fazer_ligacoes(self):
        print('Fazendo ligações...')
    
    def jogar_cobrinha(self):
        print('Jogando cobrinha...')

    def despertador(self):
        print('Despertando...')

    def calcular(self, v1, v2):
        return v1 + v2

# criando uma instância da classe Celular()
celular = Celular()

# chamando as propriedades da classe 
print(celular.marca)
print(celular.modelo)
print(celular.cor)
print(celular.tem_camera)
print(celular.bateria)

# chamando as funções da classe
celular.fazer_ligacoes()
celular.jogar_cobrinha()
celular.despertador()

calculado = celular.calcular(12, 14)
print(calculado)