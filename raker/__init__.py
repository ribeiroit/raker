# coding: utf-8
#
# Copyright (c) 2014 Tirith
#
# Licensed under the Apache License, Version 2.0 (the "License")
#
# Author: Thiago Ribeiro
# Email ribeiro dot it at gmail dot com
# Created: Jun 29, 2014, 9:00 AM
#
from flask import Flask, jsonify, request, abort, json
from flask.ext.mongoengine import MongoEngine
 
# creates new app
app = Flask(__name__)
# load config file
app.config.from_pyfile('config.py')
# set database config
mongo = MongoEngine(app)
# import mongo models
from .models import Profile
# import celery task
from .tasks import scrap_profile

# usage doc
_usage =	{
	'/profile': {
		'POST': [
			'params: profile, p_type (f - facebook, t - twitter)',
			'desc: Adds a new profile name to be scraped'
		],
		'GET': [
			'params: name',
			'desc: Reads profile name scraped information'
		],
	},
	'/profile/popularity': {
		'GET': [
			'desc: Get profiles by popularity'
		]
	}
}

# defines errors messages
@app.errorhandler(400)
def not_found_error(error):
	return jsonify({'error': 400, 'message': 'bad request'}), 400

@app.errorhandler(404)
def not_found_error(error):
	return jsonify({'error': 404, 'message': 'not found'}), 404

@app.errorhandler(500)
def internal_error(error):
	return jsonify({'error': 500, 'message': 'internal server error'}), 500

@app.errorhandler(405)
def not_allowed_error(error):
	return jsonify({'error': 405, 'message': 'method not allowed', 'usage': _usage}), 405

@app.route('/')
def usage():
	return jsonify({'usage': _usage}), 200

@app.route('/profile', methods = ['POST'])
def raker_create():
	if (
		not request.json
		or not 'profile' in request.json
		or not 'p_type' in request.json
		):
		abort(400)

	profile = request.json['profile']
	p_type = request.json['p_type']

	if p_type not in ['f', 't']:
		return jsonify({'error': 400, 'message': 'Invalid p_type value'}), 400

	if Profile.objects(pr=profile,fr=p_type).count() == 0:
		scrap_profile.delay(p_type, profile)
		return jsonify({'message': 'Profile added to be scraped'}), 201
	else:
		return jsonify({'message': 'Profile already scraped, try get /profile/<profile>'}), 201
	

@app.route('/profile/<string:ptype>/<string:profile>')
def raker_read(ptype, profile):
	profile = Profile.objects.get(fr=ptype, pr=profile)
	
	if profile:
		return profile.to_json(), 200

	return jsonify({'error': 400, 'message': 'Profile doesn\'t exist'}), 400

@app.route('/profile/popularity')
def raker_read_popularity():
	profiles = [x for x in Profile.objects.all()]
	
	if profiles:
		return profiles.to_json(), 200

	return jsonify({'message': 'There is no profile available yet.'}), 200