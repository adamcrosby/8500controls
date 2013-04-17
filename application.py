#!/usr/bin/env python
from datetime import date

from flask import *
from database import db_session
from model import Control
from search import *


application = Flask(__name__)
app = application

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
@app.route("/")
def default():
	return redirect(url_for('allControls'))

@app.route("/controls")
def allControls():
	subjects = {}
	for subject in db_session.query(Control.subjectArea).distinct():
		subjects[subject[0]] = []

	for key in subjects.keys():
		high = Control.query.filter_by(subjectArea=key).filter_by(impactCode='High').all()
		med = Control.query.filter_by(subjectArea=key).filter_by(impactCode='Medium').all()
		low = Control.query.filter_by(subjectArea=key).filter_by(impactCode='Low').all()
		for item in high:
			subjects[key].append(item)
		for item in med:
			subjects[key].append(item)		
		for item in low:
			subjects[key].append(item)
	return render_template('8500list.html', controls = subjects)

@app.route("/about")
def about():
	return render_template('about.html')

@app.route('/control/<number>')
def getControlDetail(number):

	c = Control.query.filter_by(number = number.upper()).first()
	if c:
		return render_template('8500detail.html', control=c)
	else:
		return "No such control"

@app.route("/search")
def search():
        query = request.args.get('q')

        if query == "" or query == None:
                return render_template('nosearchresults.html', query=False)

        searchResults = getSearchResults(query)
        if searchResults == False:
                return render_template('nosearchresults.html', query=query)
        else:
                return render_template('searchresults.html', results = searchResults, environ=request.environ, query=query)
	
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')