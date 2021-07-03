from package import app
from flask import render_template
from package.models import Customer
@app.route('/')
@app.route('/home')
def home_Page():
    return render_template('home.html')

@app.route('/CustomersPage')
def Customers_Page():
    customers = Customer.query.all()
    return render_template('CustomersPage.html', customers=customers )