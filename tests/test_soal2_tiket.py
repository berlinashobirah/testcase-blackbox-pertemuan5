import pytest
from datetime import date
from src.validators import (valid_jumlah_tiket, valid_kode_promo,
                            valid_tanggal_berangkat)

TODAY = date(2026, 10, 14)


@pytest.mark.parametrize('nilai, expected', [
    (5, True), (0, False), (11, False), (2.5, False), ('abc', False),
])
def test_jumlah_tiket(nilai, expected):
    assert valid_jumlah_tiket(nilai) is expected


@pytest.mark.parametrize('nilai, expected', [
    ('', True),               # P1 kosong (opsional)
    ('PROMO2026', True),      # P2 9 karakter
    ('PRM1', False),          # P3 < 5
    ('PROMO2026ABC', False),  # P4 > 10
])
def test_kode_promo(nilai, expected):
    assert valid_kode_promo(nilai) is expected


@pytest.mark.parametrize('nilai, expected', [
    ('2026-10-21', True),    # P1 masa depan
    ('2026-10-14', True),    # batas: hari ini masih valid
    ('2026-10-13', False),   # batas: kemarin
    ('2020-01-01', False),   # P2 lampau
    ('21-10-2026', False),   # P3 format salah
    ('2026-02-30', False),   # P4 tanggal tidak ada
])
def test_tanggal(nilai, expected):
    assert valid_tanggal_berangkat(nilai, today=TODAY) is expected
