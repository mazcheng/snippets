# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import re
import random
import base64
import logging
from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

log = logging.getLogger('scrapy.proxies')


class RandomUserAgentMiddleware(UserAgentMiddleware):

	def __init__(self, settings, user_agent='Scrapy'):
		super(RandomUserAgentMiddleware, self).__init__()
		self.user_agent = user_agent
		user_agent_list_file = settings.get('USER_AGENT_LIST')
		if not user_agent_list_file:
			self.user_agent_list = [settings.get('USER_AGENT', user_agent)]
		else:
			with open(user_agent_list_file, 'r') as ua_file:
				self.user_agent_list = [line.strip() for line in ua_file]

	@classmethod
	def from_crawler(cls, crawler):
		obj = cls(crawler.settings)
		crawler.signals.connect(obj.spider_opened, signal=signals.spider_opened)
		return obj

	def process_request(self, request, spider):
		user_agent = random.choice(self.user_agent_list)
		if user_agent:
			request.headers.setdefault('User-Agent', user_agent)

class ProxyMode:
	RANDOMIZE_PROXY_EVERY_REQUESTS = 0
	RANDOMIZE_PROXY_ONCE = 1
	SET_CUSTOM_PROXY = 2


# https://github.com/aivarsk/scrapy-proxies/blob/master/scrapy_proxies/randomproxy.py
class RandomProxyMiddleware(object):

	def __init__(self, settings):
		self.mode = settings.get('PROXY_MODE')
		self.proxy_list = settings.get('PROXY_LIST')
		self.chosen_proxy = ''
		if not self.proxy_list:
			raise KeyError('PROXY_LIST setting is missing')
		self.proxies = {}
		if self.mode in [ProxyMode.RANDOMIZE_PROXY_EVERY_REQUESTS, ProxyMode.RANDOMIZE_PROXY_ONCE]:
			with open(self.proxy_list) as proxy_file:
				for line in proxy_file:
					parts = re.match('(\w+://)(\w+:\w+@)?(.+)', line.strip())
					if not parts:
						continue
					# Cut trailing @
					if parts.group(2):
						user_pass = parts.group(2)[:-1]
					else:
						user_pass = ''
					self.proxies[parts.group(1) + parts.group(3)] = user_pass
				if self.mode == ProxyMode.RANDOMIZE_PROXY_ONCE:
					self.chosen_proxy = random.choice(tuple(self.proxies.keys()))
		elif self.mode == ProxyMode.SET_CUSTOM_PROXY:
			custom_proxy = settings.get('CUSTOM_PROXY')
			parts = re.match('(\w+://)(\w+:\w+@)?(.+)', custom_proxy.strip())
			if not parts:
				raise ValueError('CUSTOM_PROXY is not well formatted')

			if parts.group(2):
				user_pass = parts.group(2)[:-1]
			else:
				user_pass = ''

			self.proxies[parts.group(1) + parts.group(3)] = user_pass
			self.chosen_proxy = parts.group(1) + parts.group(3)
		else:
			self.chosen_proxy = None

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings)

	def process_request(self, request, spider):
		# Don't overwrite with a random one (server-side state for IP)
		if 'proxy' in request.meta:
			if not request.meta["exception"]:
				return
		request.meta["exception"] = False
		if len(self.proxies) == 0:
			raise ValueError('All proxies are unusable, cannot proceed')

		if self.mode == ProxyMode.RANDOMIZE_PROXY_EVERY_REQUESTS:
			proxy_address = random.choice(tuple(self.proxies.keys()))
		else:
			proxy_address = self.chosen_proxy

		proxy_user_pass = self.proxies[proxy_address]

		if proxy_user_pass:
			request.meta['proxy'] = proxy_address
			basic_auth = 'Basic ' + base64.b64encode(proxy_user_pass.encode()).decode()
			request.headers['Proxy-Authorization'] = basic_auth
		else:
			log.debug('Proxy user pass not found')
		log.debug('Using proxy <%s>, %d proxies left' % (
			proxy_address, len(self.proxies)))

	def process_exception(self, request, exception, spider):
		if 'proxy' not in request.meta:
			return
		if self.mode in [ProxyMode.RANDOMIZE_PROXY_EVERY_REQUESTS, ProxyMode.RANDOMIZE_PROXY_ONCE]:
			proxy = request.meta['proxy']
			try:
				del self.proxies[proxy]
			except KeyError:
				pass
			request.meta["exception"] = True
			if self.mode == ProxyMode.RANDOMIZE_PROXY_ONCE:
				self.chosen_proxy = random.choice(tuple(self.proxies.keys()))
			log.info('Removing failed proxy <%s>, %d proxies left' % (
				proxy, len(self.proxies)))


class CnnvdSpiderMiddleware(object):
	# Not all methods need to be defined. If a method is not defined,
	# scrapy acts as if the spider middleware does not modify the
	# passed objects.

	@classmethod
	def from_crawler(cls, crawler):
		# This method is used by Scrapy to create your spiders.
		s = cls()
		crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
		return s

	def process_spider_input(self, response, spider):
		# Called for each response that goes through the spider
		# middleware and into the spider.

		# Should return None or raise an exception.
		return None

	def process_spider_output(self, response, result, spider):
		# Called with the results returned from the Spider, after
		# it has processed the response.

		# Must return an iterable of Request, dict or Item objects.
		for i in result:
			yield i

	def process_spider_exception(self, response, exception, spider):
		# Called when a spider or process_spider_input() method
		# (from other spider middleware) raises an exception.

		# Should return either None or an iterable of Response, dict
		# or Item objects.
		pass

	def process_start_requests(self, start_requests, spider):
		# Called with the start requests of the spider, and works
		# similarly to the process_spider_output() method, except
		# that it doesn’t have a response associated.

		# Must return only requests (not items).
		for r in start_requests:
			yield r

	def spider_opened(self, spider):
		spider.logger.info('Spider opened: %s' % spider.name)
