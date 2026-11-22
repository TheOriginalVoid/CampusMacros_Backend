import json

from db import db
from flask import Flask, request
from db import Food, Foodlist, db
from seed import seed_database

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campusmacros.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

#Generalized response formats
def success_response(data, code=200):
    return json.dumps(data), code

def failure_response(message,code = 404):
    return json.dumps({"error": message}), code