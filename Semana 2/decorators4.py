def log_soma_ab(func):
    def interno(a, b):
        print(str(a) + ' + ' + str(b) + ' é ', end='')
        result = func(a, b)
        print(result)
        return result
    return interno

@log_soma_ab
def soma_ab(a, b):
    soma = a + b
    return soma

if __name__ == '__main__':
    valor = soma_ab(5, 3)
    quadrado = valor ** 2
    # outro calculo com o valor
    print(valor)
    print(quadrado)