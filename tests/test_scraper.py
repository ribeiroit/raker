# coding: utf-8
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