import pytest
from src.validators import validasi_registrasi

VALID = {
    'nama': 'Budi Santoso',
    'username': 'budi123',
    'email': 'budi@mail.com',
    'password': 'Passw0rd1',
    'umur': 20,
    'telepon': '081234567890',
}

# (id test case, field yang diubah, nilai, apakah seharusnya valid)
KASUS = [
    ('TC-02', 'nama', '', False),
    ('TC-03', 'nama', 'Al', False),
    ('TC-04', 'nama', 'Ani', True),
    ('TC-05', 'nama', 'Budi', True),
    ('TC-06', 'nama', 'A' * 49, True),
    ('TC-07', 'nama', 'A' * 50, True),
    ('TC-08', 'nama', 'A' * 51, False),
    ('TC-09', 'username', '', False),
    ('TC-10', 'username', 'bud1', False),
    ('TC-11', 'username', 'budi1', True),
    ('TC-12', 'username', 'a' * 20, True),
    ('TC-13', 'username', 'a' * 21, False),
    ('TC-14', 'username', '1budi123', False),
    ('TC-15', 'username', 'budi_123', False),
    ('TC-16', 'email', 'budimail.com', False),
    ('TC-17', 'email', 'budi@', False),
    ('TC-18', 'email', '', False),
    ('TC-19', 'password', 'Passw0r', False),
    ('TC-20', 'password', 'Passw0rd', True),
    ('TC-21', 'password', 'passw0rd1', False),
    ('TC-22', 'password', 'PASSW0RD1', False),
    ('TC-23', 'password', 'Password', False),
    ('TC-24', 'umur', 16, False),
    ('TC-25', 'umur', 17, True),
    ('TC-26', 'umur', 100, True),
    ('TC-27', 'umur', 101, False),
    ('TC-28', 'umur', 'abc', False),
    ('TC-29', 'telepon', '081234567', False),
    ('TC-30', 'telepon', '0812345678901', True),
    ('TC-31', 'telepon', '08123456789012', False),
    ('TC-32', 'telepon', '0712345678', False),
    ('TC-33', 'telepon', '0812345678', True),
]


def test_tc01_semua_valid():
    assert validasi_registrasi(VALID) == []


@pytest.mark.parametrize('tc, field, nilai, valid', KASUS,
                         ids=[k[0] for k in KASUS])
def test_registrasi(tc, field, nilai, valid):
    galat = validasi_registrasi({**VALID, field: nilai})
    assert galat == ([] if valid else [field])
