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


celular = Celular()

print(celular.marca)
print(celular.modelo)
print(celular.cor)
print(celular.tem_camera)
print(celular.bateria)

celular.fazer_ligacoes()
celular.jogar_cobrinha()
celular.despertador()
print(celular.calcular(12, 14))