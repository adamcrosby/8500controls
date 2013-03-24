#!/usr/bin/env python
from datetime import date

from flask import *
from database import db_session
from model import Control


application = Flask(__name__)
app = application

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
@app.route("/")
def default():
	return "hi"

@app.route("/controls")
def allControls():
	c = Control.query.all()
	titles = ""
	for control in c:
		titles = titles + "<br>" + control.title

	return titles

@app.route("/about")
def about():
	return render_template('about.html')
	
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')