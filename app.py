from flask import Flask, jsonify
from flask_cors import CORS

from ecommerce import createApp
from ecommerce.initialize_db import createDB
from api.users import apiUser
from api.product import apiProduct
from api.admin import apiAdmin
from api.categories import apiCategories

app = createApp()
CORS(app)

# Blueprint kayıtları
app.register_blueprint(apiUser)
app.register_blueprint(apiProduct)
app.register_blueprint(apiAdmin)
app.register_blueprint(apiCategories)

# Veritabanı oluştur
try:
    createDB(app)
except Exception as e:
    print("Veritabanı zaten var:", e)


# Rotalar
@app.route("/")
def index():
    return jsonify({"success": True, "message": "Hello World"})

@app.route("/shares")
def shares():
    return jsonify({"success": True, "data": ["paylasim1", "paylasim2", "paylasim3"]})

@app.route("/profile")
def profile():
    return jsonify({
        "id": 1,
        "name": "Furkan",
        "age": 25,
        "following": 80,
        "followers": 100,
        "followList": ["ahmet", "belgin"]
    })

if __name__ == "__main__":
    app.run(debug=True)
