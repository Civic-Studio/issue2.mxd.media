from flask import Blueprint
import os

main = Blueprint('main', __name__)


@main.route('/')
def index():
	current_path = os.getcwd()
	home_page = json.load(open('./json/home.json'))
	return render_template('index.html', home_page=home_page)