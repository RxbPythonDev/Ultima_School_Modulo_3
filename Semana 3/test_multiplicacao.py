import pytest
from multiplicacao import multiplicacao

def test_multiplicacao():
    assert multiplicacao(10, 2) == 20

def test_multiplicacao1():
    assert multiplicacao(10, 3) == 30