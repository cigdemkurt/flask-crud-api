#models: veri tabanı ile ilgili işlemler (tablolar/fonksiyonlar)

from dataclasses import dataclass
from ecommerce import db

@dataclass #dataclass veritabanına eklenecek olan tabloyu temsil eder.
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

@dataclass
class Admin(db.Model):
    __tablename__ = 'admin'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(120))
    email= db.Column(db.String(120))
    password=db.Column(db.String(120))
    mod=db.Column(db.Integer)
    
    def __init__(self,id,username,email,password,mod):
        self.username=username
        self.email=email
        self.password=password
        self.mod=mod

@dataclass #dataclass veritabanına eklenecek olan tabloyu temsil eder.
class Category(db.Model):
    __tablename__ = 'category'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120))  

@dataclass #dataclass veritabanına eklenecek olan tabloyu temsil eder.
class Product(db.Model):
    __tablename__ = 'product'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120))
    price= db.Column(db.Float)
    oldPrice=db.Column(db.Float)
    description=db.Column(db.String(120))
    category_id=db.Column(db.Integer,db.ForeignKey('category.id'))

