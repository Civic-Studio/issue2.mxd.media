from flask import Blueprint, render_template

essays = Blueprint('essays', __name__)

#####################
#  ESSAYS AVAILABLE #
#####################
# Pump Station Operators - Individuals by Aron Chang
# Pump Station Operators - Teamwork & Coordination by Aron Chang
# What Does a Pump Station Do?
# Keeping the Pumps Running
# Watch: Day After A Storm
# Watch: Evening at Station D
# Challenges
# Water Creature by Carole Alden
#####################

@essays.route('/essay/<title>')
def index(title=None):
	return render_template('essay.html', title=title)