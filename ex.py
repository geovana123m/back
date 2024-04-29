class Carro:
    def __init__(self, modelo, ano, marca):
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

    def acelerar(self):
        return 'acelerando'
    def velocidadeMaxima(self):
        if self.modelo == 'uno':
            return 'infinita'
        else:
            return '200km/h'

carro1 = Carro('uno', 1999, 'fiat')

print(carro1.velocidadeMaxima())