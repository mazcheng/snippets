# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
from settings import CsdnPeopleFilename


class CsdnPipeline(object):
	def process_item(self, item, spider):
		return item


class JsonWithEncodingCnblogsPipeline(object):
	def __init__(self):
		self.file = codecs.open(CsdnPeopleFilename, 'a', encoding='utf8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + '\n'
		self.file.write(line)
		return item

	def spider_closed(self):
		self.file.close()
