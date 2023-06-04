import pytest
from Exercicio_3 import calcular_preco_volume, validar_medida, calcular_multiplicador_peso, calcular_multiplicador_rota, calcular_frete

def test_calcular_preco_volume_menor_que_1000():
    assert calcular_preco_volume(500) == 10

def test_calcular_preco_volume_entre_1000_e_10000():
    assert calcular_preco_volume(5000) == 20

def test_calcular_preco_volume_entre_10000_e_30000():
    assert calcular_preco_volume(20000) == 30

def test_calcular_preco_volume_entre_30000_e_100000():
    assert calcular_preco_volume(70000) == 20

def test_calcular_preco_volume_maior_que_100000():
    assert calcular_preco_volume(500000) == 0

def test_validar_medida_numerica():
    assert validar_medida('30') == 30

def test_validar_medida_nao_numerica():
    assert validar_medida('letra') == -1

def test_calcular_multiplicador_peso_menor_que_100g():
    assert calcular_multiplicador_peso(0.05) == 1

def test_calcular_multiplicador_peso_entre_100g_e_1kg():
    assert calcular_multiplicador_peso(0.5) == 1.5

def test_calcular_multiplicador_peso_entre_1kg_e_10kg():
    assert calcular_multiplicador_peso(5) == 2

def test_calcular_multiplicador_peso_entre_10kg_e_30kg():
    assert calcular_multiplicador_peso(20) == 3

def test_calcular_multiplicador_peso_maior_que_30kg():
    assert calcular_multiplicador_peso(50) == 0

def test_calcular_multiplicador_rota_rs_ou_sr():
    assert calcular_multiplicador_rota('rs') == 1
    assert calcular_multiplicador_rota('sr') == 1

def test_calcular_multiplicador_rota_bs_ou_sb():
    assert calcular_multiplicador_rota('bs') == 1.2
    assert calcular_multiplicador_rota('sb') == 1.2

def test_calcular_multiplicador_rota_br_ou_rb():
    assert calcular_multiplicador_rota('br') == 1.5
    assert calcular_multiplicador_rota('rb') == 1.5

def test_calcular_multiplicador_rota_outras_siglas():
    assert calcular_multiplicador_rota('rj') == 0

def test_calcular_frete():
    assert calcular_frete(10, 1.5, 1.5) == 22.5