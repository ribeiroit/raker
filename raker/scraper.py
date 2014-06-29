# coding: utf-8
#
# Scraper
#
import re
import urllib
import requests
import bs4
import tweepy

import config

class ScraperError(Exception):
	pass

class Scraper(object):
	"""
	Main scraper interface
	"""
	def __init__(self):
		self.session = ''
		self.profile = {'nm':'', 'im':'', 'dc':'', 'pi':'', 'fr':'', 'pr':''}

	def connection(self):
		raise NotImplementedError("Method not implemented: connection")

	def grab_user(self):
		raise NotImplementedError("Method not implemented: grab_users")

	def get_url(self, url, session=True):
		rc = requests.get(url, cookies = self.session.cookies)
		s = bs4.BeautifulSoup(rc.text)
		return s

class Facebook(Scraper):
	"""
	Handles facebook guys
	"""
	def __init__(self):
		super(Facebook, self).__init__()
		self.profile['fr'] = 'f'
		self.session = requests.Session()

	def connection(self):
		try:
			self.facebook_login()
		except Exception as err:
			raise ScraperError(err)

		return True

	# Starts a new facebook session
	def facebook_login(self):
		rc = requests.get('http://m.facebook.com/index.php')
		s = bs4.BeautifulSoup(rc.text)
		li = s.find_all(attrs={'name':'li'})

		postdata = {
			'lsd'	: '',
			'li'	: li[0]['value'],
			'charset_test' : urllib.unquote_plus('%E2%82%AC%2C%C2%B4%2C%E2%82%'\
				'AC%2C%C2%B4%2C%E6%B0%B4%2C%D0%94%2C%D0%84'),
			'email'	: config.FACEBOOK_LOGIN,
			'pass'	: config.FACEBOOK_PASSWORD,
			'login'	: 'Login'
		}

		r = self.session.post('https://www.facebook.com/login.php?m=m&refsrc'\
			'=http%3A%2F%2Fm.facebook.com%2Findex.php&refid=8', 
			cookies=rc.cookies, data=postdata)
		
		if not re.search('Logout', r.text):
			raise ScraperError('Invalid facebook login or password')

	# Check session to guarantee that cookie exists
	def check_session(self):
		if 'c_user' not in self.session.cookies.keys():
			raise ScraperError('Your facebook session has expired')

	def grab_user(self, profile):
		self.check_session()

		s = self.get_url('https://m.facebook.com/%s?fref=pymk&refid=7' % profile)

		self.profile['pr'] = profile

		nm = s.find('strong', attrs={'class': 'profileName'})
		if nm:
			self.profile['nm'] = nm.string
		
		dc = s.find('span', attrs={'class': 'c mfss'})
		if dc :
			self.profile['dc'] = dc.string

		im = s.find('img', attrs={'class': 'profpic img'})
		if im:
			self.profile['im'] = im['src']

		# Get friends information
		s = self.get_url('https://m.facebook.com/%s?v=friends&refid=17' % profile)
		pi = s.find('h3', attrs={'class': 'al aps'})
		
		if pi:
			total = re.search(r'(\d+)', pi.string)
			if total:
				self.profile['pi'] = int(total.group(1))
			else:
				self.profile['dc'] = u'User has no friends'
		else:
			self.profile['dc'] = u'User with profile restricted'

		return True


class Twitter(Scraper):
	"""
	Handles twitter guys
	"""
	def __init__(self):
		super(Twitter, self).__init__()
		self.profile['fr'] = 't'

	def connection(self):
		try:
			auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, 
				config.TWITTER_CONSUMER_SECRET)
			auth.set_access_token(config.TWITTER_ACCESS_TOKEN,
				config.TWITTER_ACCESS_TOKEN_SECRET)
			self.session = tweepy.API(auth)
		except Exception as err:
			raise ScraperError(err)

		return True

	def grab_user(self, profile):
		user = self.session.get_user(profile)

		if user:
			self.profile['pr'] = profile
			self.profile['nm'] = user.name
			self.profile['im'] = user.profile_image_url
			self.profile['dc'] = user.description
			self.profile['pi'] = int(user.followers_count)

			return True

		return False