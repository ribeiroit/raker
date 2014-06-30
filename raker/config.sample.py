# coding: utf-8
#
# Copyright (c) 2014 Tirith
#
# Licensed under the Apache License, Version 2.0 (the "License")
#
# Author: Thiago Ribeiro
# Email ribeiro dot it at gmail dot com
# Created: Jun 28, 2014, 4:32 AM
#
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
 
# Statement for enabling the development environment
DEBUG = True
DEBUG_TB_INTERCEPT_REDIRECTS = False

# App name
APP_NAME = 'YOUR APP NAME'

# App host
SERVER_HOST = '0.0.0.0'

# App port
SERVER_PORT = 8080
 
# Secret key for signing cookies
# echo '<your_passphrase>' | md5
SECRET_KEY = '<secret_key>'
 
# Database settings
MONGODB_SETTINGS = {'DB': 'raker', 'HOST': '<host>', 'PORT': 27017}
TESTING = True

# Message broker
RABBITMQ_HOST = '<host>'
RABBITMQ_QUEUE = 'raker'

# facebook
FACEBOOK_LOGIN = '<your_email>'
FACEBOOK_PASSWORD = '<your_password>'

# twitter
TWITTER_CONSUMER_KEY = '<consumer_key>'
TWITTER_CONSUMER_SECRET = '<consumer_secret>'
TWITTER_ACCESS_TOKEN = '<access_token>'
TWITTER_ACCESS_TOKEN_SECRET = '<access_token_secret>'

# JSON as UTF-8
JSON_AS_ASCII = False