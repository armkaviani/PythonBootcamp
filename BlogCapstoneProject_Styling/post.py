from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/3e27ef44dc8127610106").json()

app = Flask(__name__)

@app.route('/')
def get_post():
    return render_template('index.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post/<int:index>")
def show_posts(index):
    requested_post = ""
    for post in posts:
        if post["id"] == index:
            requested_post = post
    return render_template('post.html', post=requested_post)