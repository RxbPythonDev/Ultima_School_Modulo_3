dict_cardapio = {
    100: ('Cachorro Quente', 9),
    101: ('Cachorro Quente Duplo', 11),
    102: ('X-Egg', 12),
    103: ('X-Salada', 12),
    104: ('X-Bacon', 14),
    105: ('X-Tudo', 17),
    200: ('Refrigerante Lata', 5),
    201: ('Chá Gelado', 4)
}

def soma_valores_do_pedido(pedido: list, total):
    for codigo in pedido:
        total = total + dict_cardapio[codigo][1]
    return total

if __name__ == '__main__':
    cardapio = """
    *******************Cardápio*******************
    ----------------------------------------------
    | Código |        Descrição        |  Valor  |
    |   100  |     Cachorro Quente     |   9,00  |
    |   101  |  Cachorro Quente Duplo  |  11,00  |
    |   102  |           X-Egg         |  12,00  |
    |   103  |         X-Salada        |  12,00  |
    |   104  |          X-Bacon        |  14,00  |
    |   105  |           X-Tudo        |  17,00  |
    |   200  |    Refrigerente Lata    |   5,00  |
    |   201  |         Chá Gelado      |   4,00  |
    ----------------------------------------------
    """
    print(cardapio)

    total = 0.0
    codigo = int(input('Entre com o código desejado: '))
    pedido = []
    codigos_cardapio = [100,101,102,103,104,105,200,201]
    while True:
        if codigo in codigos_cardapio:
            print(f'Você pediu um {dict_cardapio[codigo][0]} no valor de R${dict_cardapio[codigo][1]},00')
            pedido.append(codigo)
        else:
            print('Opção inválida')
            codigo = int(input('Entre com o código desejado: '))
            continue

        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('2 - Não')
        pedir_mais = int(input())

        if pedir_mais == 2:
            break

        codigo = int(input('Entre com o código desejado: '))
    total = soma_valores_do_pedido(pedido, total)
    print(f'O total a ser pago é: R${total:.2f}')