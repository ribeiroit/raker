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
	
	yum install mongodb-server rabbitmq-server supervisor nginx
	chkconfig mongodb-server on
	chkconfig rabbitmq-server on
	chkconfig supervisord on
	chkconfig nginx on
	useradd raker

	cd /opt/
	git clone https://github.com/ribeiroit/raker.git
	chown raker: raker -R
	cd raker
	mkdir env logs
	virtualenv env
	./env/bin/pip install -r requirements.txt
	cp raker/config.sample.py raker/config.py
	(Edit config.py and put your accesses informations)

nginx and supervisord
---------------------

You can use a process control system to launch your application, so take a look at utils folders.

**API**

	cat /opt/raker/utils/api_supervisord.conf >> /etc/supervisord.conf
	cp /opt/raker/utils/raker.nginx.conf /etc/nginx/conf.d/
	sed -i bak -e /YOUR_DOMAIN/<put_your_domain_here>/g /etc/nginx/conf.d/raker.nginx.conf
	service supervisord restart
	service nginx restart

**Worker**

Your can run N workers in distributed servers, so if it'll be isolated remember to install supervisord and run:

	cat /opt/raker/utils/celery_supervisord.conf >> /etc/supervisord.conf
	service supervisord restart

running
-------

If you don't want run the above step, just open a terminal and run the processess.

To start the RESTful API:

	/opt/raker/run.py

To start scraper:

	/opt/raker/env/bin/celery -A raker.tasks worker --loglevel=info --concurrency=10 -n worker1.%h

usage
-----

To scrap a facebook profile:

	curl -i -H 'Content-type: application/json' -X POST -d '{"profile":"ribeiro.it","p_type":"f"}' http://localhost:8080/profile

To scrap a twitter profile:
	
	curl -i -H 'Content-type: application/json' -X POST -d '{"profile":"ribeiroit","p_type":"t"}' http://localhost:8080/profile

To read a profile already scraped:

	curl http://localhost:8080/profile/f/ribeiro.it

To read all profiles ordering by popularity:

	curl http://localhost:8080/profile/popularity

tests
------

	/opt/raker/env/bin/python -m unittest discover
