# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
from settings import CnblogsFilename


class JsonWithEncodingCnblogsPipeline(object):
	def __init__(self):
		self.file = codecs.open(CnblogsFilename, 'a', encoding='utf8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + '\n'
		self.file.write(line)
		return item

	def spider_closed(self):
		self.file.close()


class MySQLStoreCnblogsPipeline(object):
	pass


class CnblogsPipeline(object):
	def process_item(self, item, spider):
		return item
