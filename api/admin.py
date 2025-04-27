from flask import Blueprint, request, jsonify
from ecommerce.models import db, Admin

apiAdmin = Blueprint('apiAdmin', __name__, url_prefix='/api/admins')

# Index
@apiAdmin.route('/')
def index():
    return jsonify({"success": True, "message": "Hello Admin"})

# CREATE (Admin ekle)
@apiAdmin.route('/add', methods=["POST"])
def add_admin():
    data = request.form
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    mod = data.get("mod")

    if not username or not email or not password or mod is None:
        return jsonify({"success": False, "message": "Eksik alanlar var!"})

    new_admin = Admin(
        username=username,
        email=email,
        password=password,
        mod=int(mod)
    )
    db.session.add(new_admin)
    db.session.commit()

    return jsonify({"success": True, "message": "Admin eklendi!"})

# READ (Tüm Adminleri Listele)
@apiAdmin.route("/", methods=["GET"])
def get_admins():
    admins = Admin.query.all()
    admin_list = [{
        "id": a.id,
        "username": a.username,
        "email": a.email,
        "password": a.password,
        "mod": a.mod
    } for a in admins]

    return jsonify({"success": True, "data": admin_list})

# UPDATE (Admin Güncelle)
@apiAdmin.route("/<int:id>", methods=["PUT"])
def update_admin(id):
    admin = Admin.query.get(id)

    if not admin:
        return jsonify({"success": False, "message": "Admin bulunamadı!"})

    data = request.form
    admin.username = data.get("username", admin.username)
    admin.email = data.get("email", admin.email)
    admin.password = data.get("password", admin.password)
    admin.mod = int(data.get("mod", admin.mod))

    db.session.commit()

    return jsonify({"success": True, "message": "Admin güncellendi!"})

# DELETE (Admin Sil)
@apiAdmin.route("/<int:id>", methods=["DELETE"])
def delete_admin(id):
    admin = Admin.query.get(id)

    if not admin:
        return jsonify({"success": False, "message": "Admin bulunamadı!"})

    db.session.delete(admin)
    db.session.commit()

    return jsonify({"success": True, "message": "Admin silindi!"})
