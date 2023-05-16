class Fibonacci:
    
    def __init__(self, maximo):
        self.elemento_atual = 0
        self.prox_elemento = 1
        self.maximo = maximo

    def __iter__(self):
        return self

    def __next__(self):
        if self.elemento_atual > self.maximo:
            raise StopIteration

        valor_retorno = self.elemento_atual
        self.elemento_atual = self.prox_elemento
        self.prox_elemento = valor_retorno + self.prox_elemento

        return valor_retorno

    #def __str__(self):
    #    return f'Fibonacci de {self.maximo} atual -> {self.elemento_atual} proximo -> {self.prox_elemento}'

# obj_fibonacci = Fibonacci(10)
# print(obj_fibonacci)
# for numero in obj_fibonacci:
#     print(numero)

# print('Final da iteração')

def fibonacci(maximo):
    elemento_atual = 0
    prox_elemento = 1

    while elemento_atual < maximo:
        yield elemento_atual

        elemento_atual, prox_elemento = prox_elemento, elemento_atual + prox_elemento
        # prox_elemento = elemento_atual + prox_elemento

for i in fibonacci(10):
    print(i)


# [0 1 1 2 3 5 8 13]
# maximo = 10
# atual = 0
# proximo = 1
# for numero in range(maximo):
#     auxiliar = atual
#     print(auxiliar)
#     if proximo > maximo:
#         break
#     atual = proximo
#     proxmo = auxiliar + proximo
#     numero = proximo


# print('Fora do for')