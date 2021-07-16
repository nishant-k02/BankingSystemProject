from flask import Flask, render_template  # '5556042175c17d1b44574f30'
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.db'
#app.config['SECRET_KEY'] = '5556042175c17d1b44574f30'
db = SQLAlchemy(app)

from package import routes
