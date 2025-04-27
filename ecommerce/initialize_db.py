#initialize_db database'in oluşturulduğu yer

from ecommerce.models import db
from ecommerce import createApp

def createDB(app):
    with app.app_context():
        db.create_all()

# Flask uygulama context’i içinde db.create_all() çalıştırıyor

# Bu, SQLAlchemy'de tanımladığın tüm tabloları veritabanında oluşturur
