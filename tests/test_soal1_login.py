import pytest
from src.validators import valid_username, valid_password, valid_umur


@pytest.mark.parametrize('nilai, expected', [
    ('user123', True),                  # P1 valid
    ('ab12', False),                    # P2 < 5 karakter
    ('usernameabcdefghij123', False),   # P3 > 20 karakter (21)
    ('user_name!', False),              # P4 simbol
])
def test_username(nilai, expected):
    assert valid_username(nilai) is expected


@pytest.mark.parametrize('nilai, expected', [
    ('Password123', True),   # P1 valid
    ('Pass1ab', False),      # P2 7 karakter
    ('password123', False),  # P3 tanpa huruf besar
    ('PASSWORD123', False),  # P4 tanpa huruf kecil
    ('PasswordAbc', False),  # P5 tanpa angka
])
def test_password(nilai, expected):
    assert valid_password(nilai) is expected


@pytest.mark.parametrize('nilai, expected', [
    (25, True),     # P1 valid
    (10, False),    # P2 < 17
    (150, False),   # P3 > 100
    ('abc', False), # P4 bukan angka
])
def test_umur(nilai, expected):
    assert valid_umur(nilai) is expected
