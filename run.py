#!./env/bin/python
# coding: utf-8
from raker import app

if __name__ == '__main__':
	app.run(host=app.config['SERVER_HOST'], port=app.config['SERVER_PORT'],
		debug=app.config['DEBUG'])