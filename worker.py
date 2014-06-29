#!./env/bin/python
# coding: utf-8
import pika
import time

from raker.rabbitmq import RabbitMQ
from raker.scraper import Facebook, Twitter
from raker import mongo

rabbit = RabbitMQ()

def callback(ch, method, properties, body):
	p_type, profile = str(body).split('|')
	
	# facebook
	if p_type == 'f':
		scrap = Facebook()
	elif p_type == 't':
		scrap = Twitter()

	scrap.grab_user(profile)

	if scrap.profile['nm']:
		print ' [*] Message processed'

	ch.basic_ack(delivery_tag = method.delivery_tag)

print ' [*] Waiting for messages. To exit press CTRL+C'
rabbit.channel.basic_qos(prefetch_count=1)
rabbit.channel.basic_consume(callback, queue=rabbit.queue)

rabbit.channel.start_consuming()