# Bookshelf Flask Combo
from flask import Flask, url_for, request
from bookshelf.app.controllers import main

# CSP and Enforce HTTPS
from flask_talisman import Talisman
from csp import csp

app = Flask(__name__, static_folder=None)
app.register_blueprint(main, url_prefix='')

Talisman(app, content_security_policy=csp)