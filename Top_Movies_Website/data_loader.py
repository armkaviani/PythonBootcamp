from base import app, db
from model import Movie

class DataLoader:
    def add_initial_movies():
        movie1 = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard...",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )

        movie2 = Movie(
            title="Avatar The Way of Water",
            year=2022,
            description="Set more than a decade after the events...",
            rating=7.3,
            ranking=9,
            review="I liked the water.",
            img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
        )

        with app.app_context():
            db.session.add_all([movie1, movie2])
            db.session.commit()
            print("Movies added.")