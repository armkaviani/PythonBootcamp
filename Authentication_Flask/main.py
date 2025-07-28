from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from base import app, db, login_manager
from model import User


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method=="POST":

        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(email=request.form.get('email'),
                        name=request.form.get('name'),
                        password=hash_and_salted_password,
                        )
        
        db.session.add(new_user)
        db.session.commit()
        return render_template("secret.html", name=request.get('name'))

    return render_template("register.html")


@app.route('/login')
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if check_password_hash(User.password, password):
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")



if __name__ == "__main__":
    app.run(debug=True)
