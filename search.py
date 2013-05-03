#!/usr/bin/env
#from flask import *
#from flask.ext.sqlalchemy import SQLAlchemy
import urllib
from model import Control
HARD_LIMIT = 25

def searchControlTitle(query):
	return Control.query.filter(Control.title.ilike(query)).all()

def searchControlNumber(query):
	return Control.query.filter(Control.number.ilike(query)).all()

def searchControlDescription(query):
	return Control.query.filter(Control.description.ilike(query)).all()

def searchControlThreat(query):
	return Control.query.filter(Control.threat.ilike(query)).all()

def searchControlGuidance(query):
	return Control.query.filter(Control.guidance.ilike(query)).all()

def searchControlReferences(query):
	return Control.query.filter(Control.references.ilike(query)).all()	



def getSearchResults(query):
	query = query.replace("%", "").strip()
	results = {}
	sql_query = '%%%s%%' % query # So it can be used in 'like' searchs properly

	results['controls'] = searchControlTitle(sql_query)
	results['controls'] = results['controls'] + searchControlNumber(sql_query)

	results['content'] = searchControlTitle(sql_query)
	results['content'] = results['content'] + searchControlNumber(sql_query)
	results['content'] = results['content'] + searchControlDescription(sql_query)
	results['content'] = results['content'] + searchControlThreat(sql_query)
	results['content'] = results['content'] + searchControlGuidance(sql_query)
	results['content'] = results['content'] + searchControlReferences(sql_query)

	results['controls'] = list(set(results['controls'])) # Eliminate duplicates
	results['content'] = list(set(results['content'])) # Eliminate duplicates

	# Some checks had no <description tag> - Patched for now, fix in import!
	for result in results['content']:
		if result.description == None:
			result.description = ""
	if (len(results['controls']) > 0) or (len(results['content']) > 0):
		return results
	else:
		return False


