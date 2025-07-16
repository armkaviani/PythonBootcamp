from flask import Flask, jsonify, render_template, request
from cafe import app, db, Cafe
from sqlalchemy import select
import random

@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    pass


def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}
                

@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all():
    result = db.session.execute(db.select(Cafe)).order_by(Cafe.name)
    all_cafes = result.scalars().all()

    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search", methods=["GET"])
def get_searched_cafe():
    respond = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location==respond))
    all_searched_location = result.scalars().all()

    if all_searched_location:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_searched_location])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

    

# HTTP POST - Create Record

app.route("/add", methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        mg_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
