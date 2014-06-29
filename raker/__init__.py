# coding: utf-8
import pika

from flask import Flask, jsonify, request, abort, json
from flask.ext.mongoengine import MongoEngine
 
# creates new app
app = Flask(__name__)
# load config file
app.config.from_pyfile('config.py')
# set database config
mongo = MongoEngine(app)

# import rabbit
from rabbitmq import RabbitMQ
# import models
from .models import Profile

# set rabbitmq connection
rabbit = RabbitMQ()

# usage doc
_usage =	{
	'url': '/raker',
	'POST': [
		'params: profile, p_type (f - facebook, t - twitter)',
		'desc: Adds a new profile name to be scraped'
	],
	'GET': [
		'params: name',
		'desc: Reads profile name scraped information'
	],
	'DELETE': [
		'params: profile, type',
		'desc: Drops a profile'
	]
}

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
		rabbit.add_message('%s|%s' % (p_type, profile))
	
	return jsonify({'message': 'Profile added to be scraped'}), 201

@app.route('/profile/<string:name>')
def raker_read(name):
	return jsonify({'name':name}), 200

@app.route('/profile/<string:name>', methods = ['DELETE'])
def raker_delete(name):
	return jsonify({'name':name}), 200