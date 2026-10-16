import pytest
from src.validators import valid_nilai_ujian, valid_ipk, valid_semester

NILAI = [(-1, False), (0, True), (1, True), (99, True), (100, True), (101, False)]
IPK = [(-0.1, False), (0.0, True), (0.1, True), (3.9, True), (4.0, True), (4.1, False)]
SEMESTER = [(0, False), (1, True), (2, True), (13, True), (14, True), (15, False)]


@pytest.mark.parametrize('nilai, expected', NILAI)
def test_nilai_ujian(nilai, expected):
    assert valid_nilai_ujian(nilai) is expected


@pytest.mark.parametrize('nilai, expected', IPK)
def test_ipk(nilai, expected):
    assert valid_ipk(nilai) is expected


@pytest.mark.parametrize('nilai, expected', SEMESTER)
def test_semester(nilai, expected):
    assert valid_semester(nilai) is expected
