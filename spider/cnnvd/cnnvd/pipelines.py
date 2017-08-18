# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
from settings import CnnvdVulnFile, CnnvdPatchFile
from items import CnnvdVulnItem, CnnvdPatchItem


class CnnvdPipeline(object):
	def process_item(self, item, spider):
		return item


class JsonWithEncodingCnblogsPipeline(object):
	def __init__(self):
		self.vulnfile = codecs.open(CnnvdVulnFile, 'a', encoding='utf8')
		self.patchfile = codecs.open(CnnvdPatchFile, 'a', encoding='utf8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + '\n'
		if isinstance(item, CnnvdVulnItem):
			self.vulnfile.write(line)
		elif isinstance(item, CnnvdPatchItem):
			self.patchfile.write(line)
		else:
			pass
		return item

	def spider_closed(self):
		self.vulnfile.close()
		self.patchfile.close()
