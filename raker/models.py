# coding: utf-8
from raker import mongo

class Profile(mongo.Document):
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

