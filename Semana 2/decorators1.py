def ola(func):
    def inner():
        print('Ola')
        func()
        print('Tudo bem?')
    return inner

def nome():
    print('Alice')


print('Antes')
variavel_obj = ola(nome)
print('Depois')
variavel_obj()
print('Final')
nome()

# def maiusculo(texto):
#     return texto.upper()

# print(maiusculo('adimir'))
# variavel_aluno = maiusculo
# print(variavel_aluno('jeferson'))










# print('Antes')
# obj = ola(nome)
# print('Depois')
# obj()
# print('Final')
# nome()