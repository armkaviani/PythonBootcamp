from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, order_by
from base import Base
from book import Book

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"


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


@app.route('/')
def home():
    search_result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = search_result.scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(
            title= request.form["title"],
            author= request.form["author"],
            rating= request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

