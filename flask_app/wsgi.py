from app import app
from app.database_creation import db_creation

# create db
try:
    db_creation()
except:
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)
