#!./env/bin/python
# coding: utf-8
import pika

from raker import app

class RabbitMQ:
	def __init__(self):
		self.queue = app.config['RABBITMQ_QUEUE']
		self.conn = pika.BlockingConnection(
			pika.ConnectionParameters(host=app.config['RABBITMQ_HOST'])
		)
		self.channel = self.conn.channel()
		self.channel.queue_declare(queue=self.queue, durable=True)

	def add_message(self, message):
		try:
			self.channel.basic_publish(
				exchange='',
				routing_key=self.queue,
				body=message,
				properties=pika.BasicProperties(delivery_mode = 2,)
			)
		except Exception:
			return False
		return True