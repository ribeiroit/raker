raker
=====

Social network scraper. Just a simple implementation to grab info from Facebook and Twitter.

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

	./run.py
	
tests
------

	./env/bin/python -m unittest discover