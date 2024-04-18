from flask import Flask


app = Flask(__name__)

app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

from app import controller, model, utils, forms, repository
