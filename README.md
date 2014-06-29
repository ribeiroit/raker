raker
=====

Social network scraper. Just a simple implementation to grab info from Facebook and Twitter.

libs and dependencies
---------------------

Python 2.7.x

MongoDB >= 2.2.x

RabbitMQ >= 3.3.4 

installation
------------

	git clone https://github.com/ribeiroit/raker.git
	cd raker
	mkdir env
	virtualenv env
	./env/bin/pip install -r requirements.txt
	cp raker/config.sample.py raker/config.py
	(Edit config.py and put your accesses informations)

running
-------

To start the RESTful API:

	./run.py

To start scraper:

	./worker.py

usage
-----

To scrap a facebook profile:

	curl -i -H 'Content-type: application/json' -X POST -d '{"profile":"ribeiro.it","p_type":"f"}' http://localhost:8080/profile

To scrap a twitter profile:
	
	curl -i -H 'Content-type: application/json' -X POST -d '{"profile":"ribeiroit","p_type":"t"}' http://localhost:8080/profile

tests
------

	./env/bin/python -m unittest discover