from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def get_post():
    return render_template('index.html')