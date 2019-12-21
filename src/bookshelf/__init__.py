# Bookshelf Flask Combo
from flask import Flask, url_for, request
from bookshelf.app.controllers import main

# CSP and Enforce HTTPS
from flask_talisman import Talisman
csp = {
    'default-src': [
        '\'self\'',
        'https://*.mxd.media'
    ],
    'img-src': [
        '*.mxd.media',
        'data:'
    ],
    'style-src': [
    	'\'self\'',
    	'https://fonts.googleapis.com',
        'https://*.typekit.net',
    	'\'unsafe-inline\''
    ],
    'font-src': [
    	'\'self\'',
    	'https://fonts.gstatic.com',
        'https://*.typekit.net'
    ],
    'script-src': [
        'https://*.mxd.media',
        '\'self\'',
        '\'unsafe-inline\'',
        '\'unsafe-eval\''
    ]
}


app = Flask(__name__, static_folder=None)
app.register_blueprint(main, url_prefix='')

app.config['CDN_URL'] = 'https://cdn.mxd.media/'
app.config['CDN_HASH'] = '-12192019'

Talisman(app, content_security_policy=csp)