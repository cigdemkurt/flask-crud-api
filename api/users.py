from flask import Flask, jsonify,Blueprint,request
from ecommerce.models import db,User

apiUser= Blueprint('apiUser', __name__, url_prefix='/api/users')

@apiUser.route('/add',methods=["POST"])

def add_user():
    data = request.form

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True, "message": "Kullanıcı eklendi!"})

# READ
@apiUser.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    user_list = [{"id": user.id, "username": user.username, "email": user.email, "password": user.password} for user in users]
    return jsonify({"success": True, "data": user_list})

# UPDATE
@apiUser.route("/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"success": False, "message": "Kullanıcı bulunamadı"})

    data = request.form
    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    user.password = int(data.get("password", user.password))

    db.session.commit()
    return jsonify({"success": True, "message": "Kullanıcı güncellendi"})


# DELETE
@apiUser.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"success": False, "message": "Kullanıcı bulunamadı"})

    db.session.delete(user)
    db.session.commit()
    return jsonify({"success": True, "message": "Kullanıcı silindi"})
    


    return jsonify({"success":True, "data":"User Added"})
