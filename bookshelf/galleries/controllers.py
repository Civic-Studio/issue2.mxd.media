from flask import Blueprint, render_template

galleries = Blueprint('galleries', __name__)

@galleries.route('/galleries/<series>')
def index(series=None):
	return render_template('galleries.html', series=series)