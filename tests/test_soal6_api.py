import pytest
from src.api import app

HEADER_OK = {'Authorization': 'Bearer token-valid'}
BASE = {'name': 'Laptop Gaming', 'price': 5_000_000,
        'stock': 10, 'category': 'electronics'}


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def kirim(client, body, headers=HEADER_OK):
    return client.post('/api/v1/products', json=body, headers=headers)


def test_01_valid_request(client):
    r = kirim(client, BASE)
    assert r.status_code == 201
    assert r.get_json()['name'] == 'Laptop Gaming'


@pytest.mark.parametrize('ubah, field', [
    ({'name': 'ab'}, 'name'),            # No 2: name < 3
    ({'price': 999}, 'price'),           # No 3: price < 1000
    ({'stock': 1001}, 'stock'),          # No 4: stock > 1000
    ({'category': 'toys'}, 'category'),  # No 5: category invalid
])
def test_validasi_gagal_400(client, ubah, field):
    r = kirim(client, {**BASE, **ubah})
    assert r.status_code == 400
    assert field in r.get_json()['error']


def test_06_unauthorized_token_salah(client):
    r = kirim(client, BASE, headers={'Authorization': 'Bearer salah'})
    assert r.status_code == 401


def test_unauthorized_tanpa_token(client):
    assert kirim(client, BASE, headers={}).status_code == 401


@pytest.mark.parametrize('ubah, status', [
    ({'name': 'Pen'}, 201),            # name min
    ({'name': 'a' * 100}, 201),        # name max
    ({'name': 'a' * 101}, 400),        # name max+1
    ({'price': 1000}, 201),            # price min
    ({'price': 10_000_000}, 201),      # price max
    ({'price': 10_000_001}, 400),      # price max+1
    ({'stock': 0}, 201),               # stock min
    ({'stock': 1000}, 201),            # stock max
    ({'stock': -1}, 400),              # stock min-1
    ({'stock': 10.5}, 400),            # stock bukan integer
    ({'price': 'abc'}, 400),           # price bukan number
])
def test_bva_api(client, ubah, status):
    assert kirim(client, {**BASE, **ubah}).status_code == status


def test_field_name_hilang(client):
    body = {k: v for k, v in BASE.items() if k != 'name'}
    assert kirim(client, body).status_code == 400
