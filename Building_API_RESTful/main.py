from flask import Flask, jsonify, render_template, request
from cafe import app

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def get_random_cafe():
    pass

@app.route("/random")
def get_random_cafe():
    pass

# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
