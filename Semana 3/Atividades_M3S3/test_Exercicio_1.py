import pytest
from Exercicio_1 import calcula_desconto

def test_calculo_quantidade_menor_que_10():
    assert calcula_desconto(1.0, 9) == (9,9)

def test_calculo_quantidade_entre_10_e_99():
    assert calcula_desconto(1.0, 98) == (93.1, 98)

def test_calculo_quantidade_entre_100_e_999():
    assert calcula_desconto(1.0, 998) == (898.2, 998)
    
def test_calculo_quantidade_maior_que_999():
    assert calcula_desconto(1.0, 1000) == (850, 1000)