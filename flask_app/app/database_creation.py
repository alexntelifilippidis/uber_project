from app import app
from app.models import *

def db_creation():
    # create tables from models.py
    db.create_all()
    db.session.commit()
