from flask import Blueprint, request, jsonify
from ecommerce.models import db, Category

apiCategories = Blueprint('apiCategories', __name__, url_prefix='/api/categories')

# Index
@apiCategories.route('/')
def index():
    return jsonify({"success": True, "message": "Hello Categories"})

# CREATE (Kategori ekle)
@apiCategories.route('/add', methods=["POST"])
def add_category():
    data = request.form
    name = data.get("name")

    if not name:
        return jsonify({"success": False, "message": "Kategori ismi eksik!"})

    new_category = Category(name=name)
    db.session.add(new_category)
    db.session.commit()

    return jsonify({"success": True, "message": "Kategori eklendi!"})

# READ (Tüm Kategorileri Listele)
@apiCategories.route("/", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    category_list = [{"id": c.id, "name": c.name} for c in categories]

    return jsonify({"success": True, "data": category_list})

# UPDATE (Kategori Güncelle)
@apiCategories.route("/<int:id>", methods=["PUT"])
def update_category(id):
    category = Category.query.get(id)

    if not category:
        return jsonify({"success": False, "message": "Kategori bulunamadı!"})

    data = request.form
    category.name = data.get("name", category.name)

    db.session.commit()

    return jsonify({"success": True, "message": "Kategori güncellendi!"})

# DELETE (Kategori Sil)
@apiCategories.route("/<int:id>", methods=["DELETE"])
def delete_category(id):
    category = Category.query.get(id)

    if not category:
        return jsonify({"success": False, "message": "Kategori bulunamadı!"})

    db.session.delete(category)
    db.session.commit()

    return jsonify({"success": True, "message": "Kategori silindi!"})
