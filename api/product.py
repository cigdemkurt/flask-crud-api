from flask import Blueprint, jsonify, request
from ecommerce.models import db, Product

apiProduct = Blueprint('apiProduct', __name__, url_prefix='/api/products')

# Index
@apiProduct.route('/')
def index():
    return jsonify({"success": True, "message": "Hello Product"})

# CREATE
@apiProduct.route('/add', methods=["POST"])
def add_product():
    data = request.form

    name = data.get("name")
    price = data.get("price")
    oldPrice = data.get("oldPrice")
    description = data.get("description")
    category_id = data.get("category_id")

    new_product = Product(
        name=name,
        price=float(price),
        oldPrice=float(oldPrice) if oldPrice else 0,
        description=description,
        category_id=int(category_id)
    )
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"success": True, "message": "Ürün eklendi!"})

# READ
@apiProduct.route("/", methods=["GET"])
def get_products():
    products = Product.query.all()
    product_list = [{
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "oldPrice": p.oldPrice,
        "description": p.description,
        "category_id": p.category_id
    } for p in products]

    return jsonify({"success": True, "data": product_list})

# UPDATE
@apiProduct.route("/<int:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({"success": False, "message": "Ürün bulunamadı!"})

    data = request.form
    product.name = data.get("name", product.name)
    product.price = float(data.get("price", product.price))
    product.oldPrice = float(data.get("oldPrice", product.oldPrice))
    product.description = data.get("description", product.description)
    product.category_id = int(data.get("category_id", product.category_id))

    db.session.commit()

    return jsonify({"success": True, "message": "Ürün güncellendi!"})

# DELETE
@apiProduct.route("/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({"success": False, "message": "Ürün bulunamadı!"})

    db.session.delete(product)
    db.session.commit()

    return jsonify({"success": True, "message": "Ürün silindi!"})
