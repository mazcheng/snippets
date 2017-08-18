# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	pass


class CsdnPeopleItem(scrapy.Item):
	name = scrapy.Field()
	homepage = scrapy.Field()
	avatar_url = scrapy.Field()
	focus_num = scrapy.Field()
	fans_num = scrapy.Field()
	score = scrapy.Field()
	field = scrapy.Field()
	skill = scrapy.Field()
	edu_experience = scrapy.Field()
	job_experience = scrapy.Field()
	email = scrapy.Field()
	phone = scrapy.Field()
	qq = scrapy.Field()
	wechat = scrapy.Field()


class CsdnBlogItem(scrapy.Item):
	name = scrapy.Field()
	blog_url = scrapy.Field()
	blog_cls = scrapy.Field()
	product_time = scrapy.Field()
	reader_num = scrapy.Field()
	comment_num = scrapy.Field()
	ding_num = scrapy.Field()
	cai_num = scrapy.Field()
