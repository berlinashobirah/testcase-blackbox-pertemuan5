import pytest
from src.validators import valid_nominal_transfer, bisa_transfer


@pytest.mark.parametrize('nominal, expected', [
    (9_999, False),
    (10_000, True),
    (10_001, True),
    (99_999_999, True),
    (100_000_000, True),
    (100_000_001, False),
])
def test_nominal_transfer(nominal, expected):
    assert valid_nominal_transfer(nominal) is expected


# batas saldo minimal: sisa = saldo - nominal - 2.500 harus >= 50.000
@pytest.mark.parametrize('saldo, nominal, expected', [
    (62_499, 10_000, False),   # sisa 49.999
    (62_500, 10_000, True),    # sisa 50.000
    (62_501, 10_000, True),    # sisa 50.001
])
def test_saldo_minimal(saldo, nominal, expected):
    assert bisa_transfer(saldo, nominal) is expected
