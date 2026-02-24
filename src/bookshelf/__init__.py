# Bookshelf Flask Combo
from flask import Flask, url_for, request
from bookshelf.app.controllers import main
import os

# Compress
from flask_compress import Compress

# CSP and Enforce HTTPS
from flask_talisman import Talisman
csp = {
    'default-src': [
        '\'self\'',
        'https://*.mxd.media'
    ],
    'img-src': [
        '*.mxd.media',
        'data:',
        'https://www.google-analytics.com'
    ],
    'style-src': [
    	'\'self\'',
    	'https://fonts.googleapis.com',
    	'\'unsafe-inline\''
    ],
    'font-src': [
    	'\'self\'',
    	'https://fonts.gstatic.com',
    ],
    'script-src': [
        '\'self\'',
        '\'unsafe-eval\'',
        '\'unsafe-inline\'',
        'https://*.mxd.media',
        'https://www.googletagmanager.com',
        'https://www.google-analytics.com'
    ]
}


app = Flask(__name__, static_folder=None)
app.register_blueprint(main, url_prefix='')

app.config['CDN_URL'] = 'https://cdn.mxd.media/'
app.config['CDN_HASH'] = '-12192019'

# Only apply Talisman and Compress when not freezing the site
# Talisman forces HTTPS redirects which breaks Frozen-Flask,
# and Compress can interfere with the static file output.
if not os.environ.get('FLASK_FREEZE'):
    Talisman(app, content_security_policy=csp)
    Compress(app)
