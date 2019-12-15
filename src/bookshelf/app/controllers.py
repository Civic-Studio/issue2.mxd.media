from flask import Blueprint, render_template
import os, json

main = Blueprint('main', __name__, template_folder='../../templates', static_folder='../../static')

@main.route('/')
def show_index():
	current_path = os.getcwd()
	home_page_essays = json.load(open(current_path + '/json/essays.json'))
	home_page_galleries = json.load(open(current_path + '/json/galleries.json'))
	return render_template('index.html', home_page_essays=home_page_essays, home_page_galleries=home_page_galleries)

@main.route('/essay/<title>')
def show_essays(title=None):
	return render_template('essay.html', title=title)

@main.route('/gallery/<series>')
def show_galleries(series=None):
	return render_template('galleries.html', series=series)

@main.route('/about')
def show_about():
    return render_template('about.html')

@main.route('/artists')
def show_artists():
    return render_template('artists.html')

@main.route('/projects')
def show_projects():
	return render_template('project.html')