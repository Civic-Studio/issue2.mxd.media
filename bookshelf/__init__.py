from flask import Flask
from bookshelf.artists.controllers import artists
from bookshelf.essays.controllers import essays
from bookshelf.galleries.controllers import galleries
from bookshelf.main.controllers import main

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(artists, url_prefix='/artists')
app.register_blueprint(essays, url_prefix='/essays')
app.register_blueprint(galleries, url_prefix='/galleries')