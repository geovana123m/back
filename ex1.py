class Celular:
    def __init__(self, marca, ano, modelo, bateria):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.bateria = bateria

    def ligar(self):
        return 'ligando celular'

    def carregar(self):
        if self.marca == 'samsung':
            return '60 minutos'
        else: 
            return '90 minutos'

    def despertar(self):
        return 'padrão'

Celular1 = Celular('sansung', 2020, 'a60', 0)
print(Celular1.carregar())
