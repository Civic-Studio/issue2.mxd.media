# Bookshelf Flask Combo
from flask import Flask, url_for, request
from bookshelf.app.controllers import main

# CSP and Enforce HTTPS
from flask_talisman import Talisman
csp = {
    'default-src': [
        '\'self\'',
        '*.mxd.media'
    ],
    'img-src': '*.mxd.media',
    'style-src': [
    	'\'self\'',
    	'https://fonts.googleapis.com',
    	'\'unsafe-inline\''
    ],
    'font-src': [
    	'\'self\'',
    	'https://fonts.gstatic.com'
    ],
    'script-src': [
        'https://cdn.jsdelivr.net/npm/vue',
        '\'self\'',
        '\'unsafe-inline\'',
        '\'unsafe-eval\''
    ]
}


app = Flask(__name__, static_folder=None)
app.register_blueprint(main, url_prefix='')

Talisman(app, content_security_policy=csp)