def mostrar(func):
    def inner():
        print('O usuario atual é : ', end='')
        func()
    return inner

@mostrar
def quem():
    print('Alice')

@mostrar
def envia_email_do_sistema(texto):
    # envio do email
    print('Envio de email')
    
# if __name__ == '__main__':
quem()