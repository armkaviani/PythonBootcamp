from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from base import Base
from book import Book

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"


# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

all_books = []


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(book)
        return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

