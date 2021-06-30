from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.db'
db = SQLAlchemy(app)

class Customer(db.Model):
    Sr_no = db.Column(db.Integer(), primary_key = True)
    Name = db.Column(db.String(length = 30), nullable = False,)
    Email_Id = db.Column(db.String(length=30), nullable=False, unique = True )
    Account_Number = db.Column(db.Integer(), nullable=False, unique = True )
    Balance = db.Column(db.Integer(), nullable=False )

    def __repr__(self):
        return f'Customer {self.Name}'

@app.route('/')
@app.route('/home')
def home_Page():
    return render_template('home.html')

@app.route('/CustomersPage')
def Customers_Page():
    customers = Customer.query.all()
    return render_template('CustomersPage.html', customers=customers )