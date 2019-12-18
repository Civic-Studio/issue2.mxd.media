from flask import Blueprint, render_template, request
import os, json

site_name = 'Issue 2 from Mixed Media: Water Systems'
fb_admin = '12345678'

main = Blueprint('main', __name__, template_folder='../../templates', static_folder='../../static')

@main.route('/')
def show_index():
	current_path = os.getcwd()
	print(current_path)
	home_page_essays = json.load(open(current_path + '/json/essays.json'))
	home_page_galleries = json.load(open(current_path + '/json/galleries.json'))

	metadata_name = {
		'keywords': 'New Orleans artists, Mixed Media, SWBNO, Sewerage Water Board New Orleans, art, water systems',
		'description': 'This feature is a part of MIXED MEDIA, a multidisciplinary initiative by the Blue House / Civic Studio that supports civic dialog on critical issues through art, research, and storytelling.',
		'twitter:description': 'https://cdn.mxd.media/partners/mm.png',
		'twitter:img:src': 'https://cdn.mxd.media/partners/mm.png'
	}

	metadata_property = {
		'og:title': 'Mixed Media: Water Systems - New Orleans, Louisiana',
		'og:type': 'Home Page',
		'og:url': request.url,
		'og:image': 'https://cdn.mxd.media/partners/mm.png',
		'og:description': 'This feature is a part of MIXED MEDIA, a multidisciplinary initiative by the Blue House / Civic Studio that supports civic dialog on critical issues through art, research, and storytelling.',
		'og:site_name': site_name,
		'fb:admins': fb_admin
	}

	return render_template(
		'index.html',
		home_page_essays=home_page_essays,
		home_page_galleries=home_page_galleries
	)

@main.route('/essay/<title>')
def show_essays(title=None):
	return render_template('essay.html', title=title)

@main.route('/gallery/<series>')
def show_galleries(series=None):
	return render_template('galleries.html', series=series)

@main.route('/artists')
def show_artists():
	metadata_name = {
		'keywords': 'New Orleans artists, Mixed Media, CFreedom, Maggie Hermann, Ann Nelson, art and media',
		'description': 'CFreedom, Maggie Hermann, Ann Nelson, and others capture water systems in New Orleans',
		'twitter:description': 'https://cdn.mxd.media/partners/mm.png',
		'twitter:img:src': 'https://cdn.mxd.media/partners/mm.png'
	}

	metadata_property = {
		'og:title': 'The Artists of Mixed Media: Water Systems',
		'og:type': 'Artist Page',
		'og:url': request.url,
		'og:image': 'https://cdn.mxd.media/partners/mm.png',
		'og:description': 'CFreedom, Maggie Hermann, Ann Nelson, and others capture water systems in New Orleans',
		'og:site_name': site_name,
		'fb:admins': fb_admin
	}

	return render_template(
		'artists.html',
		metadata_name=metadata_name,
		metadata_property=metadata_property
	)

@main.route('/project')
def show_projects():
	metadata_name = {
		'keywords': 'New Orleans artists, Mixed Media, SWBNO, Sewerage Water Board New Orleans, water management',
		'description': 'Mixed Media\'s sophomore issue - Water Systems',
		'twitter:description': 'https://cdn.mxd.media/partners/mm.png',
		'twitter:img:src': 'https://cdn.mxd.media/partners/mm.png'
	}

	metadata_property = {
		'og:title': 'About Mixed Media: Water Systems',
		'og:type': 'About Page',
		'og:url': request.url,
		'og:image': 'https://cdn.mxd.media/partners/mm.png',
		'og:description': 'Mixed Media\'s sophomore issue - Water Systems',
		'og:site_name': site_name,
		'fb:admins': fb_admin
	}

	return render_template(
		'project.html',
		metadata_name=metadata_name,
		metadata_property=metadata_property
	)

@main.route('/purchase')
def show_purchase():
	return render_template('purchase.html')