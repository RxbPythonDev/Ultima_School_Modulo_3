def decorator_imprimir(func):
    def inner(capital, taxa, tempo):
        print(f'CAPITAL: {capital} TAXA: {taxa} TEMPO: {tempo}')
        resultado = func(capital, taxa, tempo)
        print(f'RESULTADO: {resultado}')
    return inner

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo