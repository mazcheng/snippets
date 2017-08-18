#!/apps/ns/python/bin/python
# _*_coding:utf-8_*_

"""
@author: mazhicheng
@file: cnblogs_spider.py
@time: 2017/8/9 14:35
"""

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.response import get_base_url
from scrapy.linkextractors import LinkExtractor
from cnblogs.items import *


class CnblogsSpider(CrawlSpider):
	# define crawler name
	name = 'CnblogsSpider'
	# limit crawler domain list, if not here: give up crawler other domain
	allowed_domains = ['cnblogs.com']
	# define crawler entrance
	start_urls = [
		'http://www.cnblogs.com/rwxwsblog/default.html?page=1'
	]
	# define crawler URL rule and assign callback func is `parse_item`
	rules = [
		Rule(LinkExtractor(allow=('/rwxwsblog/default.html\?page=\d{1,}')),
			 follow=True,
			 callback='parse_item')
	]
	print '-----CnblogsSpider-----'

	# define callback func
	# use Xpath or CSS Selector
	def parse_item(self, response):
		items = []
		sel = Selector(response)
		base_url = get_base_url(response)
		postTitle = sel.css('div.day div.postTitle')
		postCon = sel.css('div.postCon div.c_b_p_desc')
		for index in range(len(postTitle)):
			item = CnblogsItem()
			item['title'] = postTitle[index].css('a').xpath('text()').extract()[0]
			item['link'] = postTitle[index].css('a').xpath('@href').extract()[0]
			item['list_url'] = base_url
			try:
				item['desc'] = postCon[index].xpath('text()').extract()[0]
			except Exception as e:
				item['desc'] = 'not desc'
			items.append(item)
		return items
