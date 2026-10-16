import pytest
from datetime import date
from src.validators import validasi_pendaftaran

TODAY = date(2026, 10, 14)
VALID = {
    'nama': 'Siti Aminah',
    'email': 'siti@mail.com',
    'hp': '081234567890',
    'tgl_lahir': '2000-05-17',
    'password': 'P@ssw0rd1',
    'konfirmasi': 'P@ssw0rd1',
}

KASUS = [
    ('TC-02', 'nama', '', False),
    ('TC-03', 'nama', 'Al', False),
    ('TC-04', 'nama', 'Ani', True),
    ('TC-05', 'nama', 'Budi', True),
    ('TC-06', 'nama', 'A' * 99, True),
    ('TC-07', 'nama', 'A' * 100, True),
    ('TC-08', 'nama', 'A' * 101, False),
    ('TC-09', 'email', 'sitimail.com', False),
    ('TC-10', 'email', 'siti@', False),
    ('TC-11', 'email', '', False),
    ('TC-12', 'hp', '081234567', False),
    ('TC-13', 'hp', '0812345678', True),
    ('TC-14', 'hp', '0812345678901', True),
    ('TC-15', 'hp', '08123456789012', False),
    ('TC-16', 'hp', '0712345678', False),
    ('TC-17', 'hp', '08123abc789', False),
    ('TC-18', 'tgl_lahir', '2009-10-14', True),   # tepat 17 tahun
    ('TC-19', 'tgl_lahir', '2009-10-15', False),  # 16 tahun 364 hari
    ('TC-20', 'tgl_lahir', '2009-10-13', True),   # 17 tahun 1 hari
    ('TC-21', 'tgl_lahir', '14-10-2000', False),
    ('TC-22', 'tgl_lahir', '2000-02-30', False),
    ('TC-23', 'tgl_lahir', '2030-01-01', False),
    ('TC-24', 'password', 'P@ssw0r', False),
    ('TC-25', 'password', 'P@ssw0rd', True),
    ('TC-26', 'password', 'p@ssw0rd1', False),
    ('TC-27', 'password', 'P@SSW0RD1', False),
    ('TC-28', 'password', 'P@sswordA', False),
    ('TC-29', 'password', 'Passw0rd1', False),
    ('TC-30', 'konfirmasi', 'P@ssw0rd2', False),
    ('TC-31', 'konfirmasi', '', False),
]


def test_tc01_semua_valid():
    assert validasi_pendaftaran(VALID, TODAY) == []


@pytest.mark.parametrize('tc, field, nilai, valid', KASUS,
                         ids=[k[0] for k in KASUS])
def test_pendaftaran(tc, field, nilai, valid):
    data = {**VALID, field: nilai}
    if field == 'password':
        data['konfirmasi'] = nilai   # samakan agar hanya password yang diuji
    galat = validasi_pendaftaran(data, TODAY)
    assert galat == ([] if valid else [field])
