import requests

class IteradorFipe:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.modelos = requests.get(f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.marca_id}/modelos').json()['modelos']
        self.indice = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.modelos):
            modelo = self.modelos[self.indice]
            self.indice += 1
            return {'nome': modelo['nome'], 'id': modelo['codigo']}
        else:
            raise StopIteration

iterador = IteradorFipe(21) #FIAT
for modelo in iterador:
    print(modelo)