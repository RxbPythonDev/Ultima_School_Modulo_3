class Carro:
    def __init__(self, placa, cor, modelo):
        self.placa = placa
        self.cor = cor
        self.modelo = modelo

    def __str__(self):
        return f'Carro({self.placa},{self.cor},{self.modelo})'
        
#var_carro = Carro('abc-1234', 'vermelho', 'Fusca')
#print(var_carro)