from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from form import CafeForm
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv") as file:
            file.write(f"\n{form.cafe.data},"
                       f"\n{form.location.data},"
                       f"\n{form.open.data},"
                       f"\n{form.close.data},"
                       f"\n{form.coffee_rating.data},"
                       f"\n{form.wifi_rating.data},"
                       f"\n{form.power_rating.data},")
        return redirect(url_for('cafes'))    
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True)
