from flask import Flask
from flask_migrate import Migrate
from models import db,User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///task.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# iniatialize the db
db.init_app(app)

migration = Migrate(app,db)