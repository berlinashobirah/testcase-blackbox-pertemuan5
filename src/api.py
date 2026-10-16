from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_TOKEN = 'token-valid'
KATEGORI = {'electronics', 'clothing', 'food'}


def _angka(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


@app.post('/api/v1/products')
def buat_produk():
    # 401: cek token paling awal
    if request.headers.get('Authorization') != f'Bearer {VALID_TOKEN}':
        return jsonify(error='invalid token'), 401

    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error='invalid JSON body'), 400

    name = data.get('name')
    price = data.get('price')
    stock = data.get('stock')
    category = data.get('category')

    if not isinstance(name, str) or not 3 <= len(name) <= 100:
        return jsonify(error='name must be 3-100 characters'), 400
    if not _angka(price) or not 1000 <= price <= 10_000_000:
        return jsonify(error='price must be 1000-10000000'), 400
    if not isinstance(stock, int) or isinstance(stock, bool) or not 0 <= stock <= 1000:
        return jsonify(error='stock must be an integer 0-1000'), 400
    if not isinstance(category, str) or category not in KATEGORI:
        return jsonify(error='category must be electronics, clothing, or food'), 400

    produk = {'id': 1, 'name': name, 'price': price,
              'stock': stock, 'category': category}
    return jsonify(produk), 201
