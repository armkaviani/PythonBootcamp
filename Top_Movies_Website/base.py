from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask import Flask
from flask_bootstrap import Bootstrap5


class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'


Bootstrap5(app)
db = SQLAlchemy(model_class=Base)
db.init_app(app)


with app.app_context():
    db.create_all()