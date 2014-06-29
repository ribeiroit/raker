# coding: utf-8
#
# Copyright (c) 2014 Tirith
#
# Licensed under the Apache License, Version 2.0 (the "License")
#
# Author: Thiago Ribeiro
# Email ribeiro dot it at gmail dot com
# Created: Jun 28, 2014, 13:00 PM
#
import unittest2 as unittest
from raker.scraper import Facebook, Twitter

class FacebookTest(unittest.TestCase):
	def setUp(self):
		self.scraper = Facebook()

	def test_connection(self):
		self.assertEqual(self.scraper.connection(), True)

	def test_grab_user(self):
		self.scraper.connection()
		self.assertEqual(self.scraper.grab_user(profile='ribeiro.it'), True)
		self.assertEqual(self.scraper.profile['nm'], 'Thiago Ribeiro')

class TwitterTest(unittest.TestCase):
	def setUp(self):
		self.scraper = Twitter()

	def test_connection(self):
		self.assertEqual(self.scraper.connection(), True)

	def test_grab_user(self):
		self.scraper.connection()
		self.assertEqual(self.scraper.grab_user(profile='ribeiroit'), True)
		self.assertEqual(self.scraper.profile['nm'], 'Thiago Ribeiro')

if __name__ == '__main__':
	unittest.main()