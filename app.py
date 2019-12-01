from flask import Flask, url_for, render_template
import os
import json

env = os.environ['FLASK_ENV']

app = Flask(__name__)

if env == "development":
	app.config.update(
		TESTING=True,
		FLASK_DEBUG=True
	)

with app.app_context():

	@app.route('/')
	def r_home():
		home_page = json.load(open('./json/home.json'))
		return render_template('index.html', home_page=home_page)

	@app.route('/artists')
	def r_artists():
	    return render_template('artists.html')

	@app.route('/project')
	def r_project():
	    return render_template('project.html')

	# ESSAYS
	#
	# Pump Station Operators - Individuals
	# Pump Station Operators - Teamwork & Coordination
	# What Does a Pump Station Do?
	# Keeping the Pumps Running
	# Watch: Day After A Storm
	# Watch: Evening at Station D
	# Challenges
	# Water Creature by Carole Alden

	@app.route('/essay/<title>')
	def r_behind_the_scenes(title=None):
		return render_template('essay.html', title=title)

	# GALLERIES
	#
	# Behind the Scenes
	# Water Series by Anne Nelson

	@app.route('/gallery/<series>')
	def r_render_gallery(series=None):
		return render_template('gallery.html', series=series)

if __name__ == '__main__':
    app.run()