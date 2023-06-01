import pytest

from wallet import Wallet

@pytest.fixture
def carteira():
    return Wallet(10)