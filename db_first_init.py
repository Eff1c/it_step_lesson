from app import db
from server import app

with app.app_context():
    db.create_all()
