from flask import Flask
from bookshelf.app.controllers import main

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')