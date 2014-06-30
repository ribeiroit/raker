# coding: utf-8
#
# Copyright (c) 2014 Tirith
#
# Licensed under the Apache License, Version 2.0 (the "License")
#
# Author: Thiago Ribeiro
# Email ribeiro dot it at gmail dot com
# Created: Jun 29, 2014, 15:00 PM
#
from raker import mongo

class Profile(mongo.Document):
	"""
	Profile object to be saved.
	Names were simplified due it be nosql
	"""
	# name
	nm = mongo.StringField()
	# image url
	im = mongo.StringField()
	# description
	dc = mongo.StringField()
	# popularity index
	pi = mongo.IntField()
	# from: [f] facebook, [t] twitter
	fr = mongo.StringField()
	# profile
	pr = mongo.StringField()

	meta = {
		'indexes': ['-pi', 'pr']
	}

