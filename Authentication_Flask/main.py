from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from base import app, db, login_manager
from model import User


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method=="POST":
        new_user = User(email=request.get('email'),
                        name=request.get('name'),
                        password=request.get('password')
                        )
        
        db.session.add(new_user)
        db.session.commit()
        return render_template("secret.html", name=request.get('name'))

    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")



if __name__ == "__main__":
    app.run(debug=True)
