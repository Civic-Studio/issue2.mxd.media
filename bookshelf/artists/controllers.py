from flask import Blueprint, render_template

artists = Blueprint('artists', __name__)

@artists.route('/artists')
def index():
    return render_template('artists.html')