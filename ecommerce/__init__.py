# Uygulaman PostgreSQL veritabanına bağlanıyor

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def createApp():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost:5432/ecommerce'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) #bağlantı yapmak için init_app()

    return app