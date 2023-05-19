import time

def time_exec(func):
    def wrapper(*args, **kargs):
        inicio = time.time()
        result = func(*args, **kargs)
        fim = time.time()
        print(func.__name__ + ' executado em ' + str((fim-inicio)*1000 ) + ' milisegundos' )
  
    return wrapper

@time_exec
def calc_quadrado(numeros):
    resultado = []
    for numero in numeros:
        resultado.append(numero*numero)

    return resultado

@time_exec
def calc_cubo(numeros):
    resultado = []
    for numero in numeros:
        resultado.append(numero*numero*numero)

    return resultado

# if __name__ == '__main__':
lista_numeros = range(1,1000000)
calc_quadrado(lista_numeros)
calc_cubo(lista_numeros)