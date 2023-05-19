def mostrar(func):
    def interno():
        print('O usuario atual é : ', end='')
        func()
    return interno

def quem():
    print('Alice')

# if __name__ == '__main__':
myobj = mostrar(quem)
myobj()