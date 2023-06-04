import pytest
from Exercicio_2 import soma_valores_do_pedido

def test_1_produto():
    assert soma_valores_do_pedido([100], 0) == 9

def test_soma_2_produtos():
    assert soma_valores_do_pedido([103, 201], 0) == 16

def test_soma_3_produtos():
    assert soma_valores_do_pedido([102, 105, 200], 0) == 34

def test_soma_4_produtos():
    assert soma_valores_do_pedido([100, 201, 105, 200], 0) == 35