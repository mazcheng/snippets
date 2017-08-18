# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnnvdVulnItem(scrapy.Item):
	vuln_id = scrapy.Field()
	name = scrapy.Field()
	harm_level = scrapy.Field()
	cve_id = scrapy.Field()
	vuln_type = scrapy.Field()
	report_time = scrapy.Field()
	threat_type = scrapy.Field()
	update_time = scrapy.Field()
	company = scrapy.Field()
	vuln_source = scrapy.Field()
	vuln_abstract = scrapy.Field()
	vuln_notice = scrapy.Field()
	refer_site = scrapy.Field()
	affect_entry = scrapy.Field()
	patch = scrapy.Field()


class CnnvdPatchItem(scrapy.Item):
	patch_id = scrapy.Field()
	name = scrapy.Field()
	size = scrapy.Field()
	important_level = scrapy.Field()
	report_time = scrapy.Field()
	company = scrapy.Field()
	company_homepage = scrapy.Field()
	md5_val = scrapy.Field()
	refer_site = scrapy.Field()
	vuln = scrapy.Field()


class CnnvdItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	pass
