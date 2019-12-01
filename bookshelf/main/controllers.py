from flask import Blueprint, render_template
import os, json

main = Blueprint('main', __name__, template_folder='../../templates')

print(os.getcwd())

@main.route('/')
def index():
	current_path = os.getcwd()
	home_page = json.load(open(current_path + '/json/home.json'))
	return render_template('index.html', home_page=home_page)