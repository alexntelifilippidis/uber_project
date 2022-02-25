from app.__init__ import db


class User(db.Model):
    __table_args__ = {'schema': 'uber'}
    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    role = db.Column(db.String(50))

    def __init__(self, username, role):
        self.username = username
        self.role = role







        
