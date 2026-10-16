import re
from datetime import date, datetime


def _int(x):
    return isinstance(x, int) and not isinstance(x, bool)


def _angka(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


# ---------- Soal 1 ----------
def valid_username(u):
    return (isinstance(u, str) and 5 <= len(u) <= 20
            and re.fullmatch(r'[A-Za-z0-9]+', u) is not None)


def valid_password(p):
    return (isinstance(p, str) and len(p) >= 8
            and re.search(r'[A-Z]', p) is not None
            and re.search(r'[a-z]', p) is not None
            and re.search(r'[0-9]', p) is not None)


def valid_umur(umur):
    return _int(umur) and 17 <= umur <= 100


# ---------- Soal 2 ----------
def valid_jumlah_tiket(n):
    return _int(n) and 1 <= n <= 10


def valid_kode_promo(k):
    if k is None or k == '':      # opsional: kosong boleh
        return True
    return isinstance(k, str) and 5 <= len(k) <= 10


def _parse_tanggal(s):
    if not isinstance(s, str) or re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', s) is None:
        return None
    try:
        return datetime.strptime(s, '%Y-%m-%d').date()
    except ValueError:            # misal 2026-02-30
        return None


def valid_tanggal_berangkat(s, today=None):
    today = today or date.today()
    d = _parse_tanggal(s)
    return d is not None and d >= today


# ---------- Soal 3 ----------
def valid_nilai_ujian(x):
    return _angka(x) and 0 <= x <= 100


def valid_ipk(x):
    return _angka(x) and 0.0 <= x <= 4.0


def valid_semester(x):
    return _int(x) and 1 <= x <= 14


# ---------- Soal 4 ----------
BIAYA_ADMIN = 2500
SALDO_MINIMAL = 50000


def valid_nominal_transfer(n):
    return _int(n) and 10_000 <= n <= 100_000_000


def bisa_transfer(saldo, nominal):
    # sisa saldo setelah nominal + biaya admin tidak boleh < saldo minimal
    return valid_nominal_transfer(nominal) and saldo - nominal - BIAYA_ADMIN >= SALDO_MINIMAL


# ---------- Soal 5 ----------
def valid_nama(n):
    return isinstance(n, str) and 3 <= len(n) <= 50


def valid_username_reg(u):
    return valid_username(u) and not u[0].isdigit()


def valid_email(e):
    pola = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+([.][A-Za-z0-9-]+)*[.][A-Za-z]{2,}'
    return isinstance(e, str) and re.fullmatch(pola, e) is not None


def valid_telepon(t):
    # diawali 08 + 8 sampai 11 digit lagi = total 10-13 digit
    return isinstance(t, str) and re.fullmatch(r'08[0-9]{8,11}', t) is not None


def validasi_registrasi(data):
    """Mengembalikan daftar nama field yang tidak valid ([] = semua valid)."""
    aturan = {
        'nama': valid_nama,
        'username': valid_username_reg,
        'email': valid_email,
        'password': valid_password,
        'umur': valid_umur,
        'telepon': valid_telepon,
    }
    return [f for f, fn in aturan.items() if not fn(data.get(f))]


# ---------- Soal 7 ----------
def valid_nama_bonus(n):
    return isinstance(n, str) and 3 <= len(n) <= 100


def valid_password_bonus(p):
    # aturan password Soal 1 + wajib ada simbol
    return valid_password(p) and re.search(r'[^A-Za-z0-9]', p) is not None


def hitung_umur(lahir, today):
    sudah_ulang_tahun = (today.month, today.day) >= (lahir.month, lahir.day)
    return today.year - lahir.year - (0 if sudah_ulang_tahun else 1)


def valid_tanggal_lahir(s, today=None):
    today = today or date.today()
    lahir = _parse_tanggal(s)
    return lahir is not None and hitung_umur(lahir, today) >= 17


def valid_konfirmasi(password, konfirmasi):
    return isinstance(konfirmasi, str) and konfirmasi != '' and password == konfirmasi


def validasi_pendaftaran(data, today=None):
    aturan = [
        ('nama', valid_nama_bonus(data.get('nama'))),
        ('email', valid_email(data.get('email'))),
        ('hp', valid_telepon(data.get('hp'))),
        ('tgl_lahir', valid_tanggal_lahir(data.get('tgl_lahir'), today)),
        ('password', valid_password_bonus(data.get('password'))),
        ('konfirmasi', valid_konfirmasi(data.get('password'), data.get('konfirmasi'))),
    ]
    return [field for field, ok in aturan if not ok]
