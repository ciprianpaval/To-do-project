from flask import Flask, jsonify, request
from flask_restful import Api
import secrets
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# set connection to database
conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.db_user, secrets.db_pass, secrets.db_host, secrets.db_name)

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

api = Api(app, prefix="/api/db")
app.config['PROPAGATE_EXCEPTIONS'] = True
