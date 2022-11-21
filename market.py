from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length =30), unique=True)
    price = db.Column(db.Integer())



@app.route('/home')
@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        form = request.form
        search_value = form['search_string']
        search = "%{}%".format(search_value)
        results = Item.query.filter(Item.name.like(search)).all()
        return render_template('market.html', items=results )
    else:
        return redirect('/market')




