#!/apps/ns/python/bin/python
# _*_coding:utf-8_*_

"""
@author: mazhicheng
@file: csdn_spider.py
@time: 2017/8/10 11:14
"""

import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.linkextractors import LinkExtractor
from scrapy import Request, FormRequest
from csdn.items import *


class CsdnSpider(CrawlSpider):
	name = 'CsdnSpider'

	allowed_domains = [
		'passport.csdn.net',
		'csdn.net',
		'my.csdn.net'
	]
	formdata = {
		'username': 'XXX',
		'password': 'XXX'
	}

	start_urls = [
		'http://www.csdn.net/',
		'http://passport.csdn.net/account/login',
		'http://my.csdn.net/'
	]

	followers = set()
	rules = [
		Rule(LinkExtractor(allow=('csdn\.net')),
			 follow=True),
	]

	def start_requests(self):
		return [Request('https://passport.csdn.net/account/login', callback=self.parse_login)]

	def parse_login(self, response):
		return [FormRequest.from_response(response, formdata=self.formdata, callback=self.after_login)]

	def after_login(self, response):
		return [
			Request('http://my.csdn.net/service/main/my_relation?pageno=1&pagesize=50&type=follow',
					callback=self.parse_attention),
			Request('http://my.csdn.net/service/main/my_relation?pageno=2&pagesize=50&type=follow',
					callback=self.parse_attention),
		]

	def parse_attention(self, response):
		raw_followers = response.body
		for user_info in json.loads(raw_followers)['result']['list']:
			homepage = 'http://my.csdn.net/' + user_info[u'username']
			yield Request(homepage, callback=self.parse_person)


	def parse_person(self, response):
		sel = Selector(response)
		base_url = get_base_url(response)
		person_info_con = sel.css('div.persional_property div.person_info_con')
		person_photo = person_info_con.css('dl.person-photo')
		person_info = person_info_con.css('dl.person-info')
		person_detail = sel.css('div.persion_section div#divDetail.aboutMe div.myDetails.activeContent')
		item = CsdnPeopleItem()
		item['name'] = person_info.xpath('dt/span/text()').extract_first()
		item['homepage'] = base_url
		item['avatar_url'] = person_photo.xpath('dt/a/img/@src').extract_first()
		item['focus_num'] = person_photo.xpath('dd[1]/b/text()').extract_first()
		item['fans_num'] = person_photo.xpath('dd[2]/b/text()').extract_first()
		# visited
		# http://my.csdn.net/service/main/visited?username=feng88724
		yield Request('http://my.csdn.net/service/main/getSorce?username=' + item['name'],
					  meta={'item': item}, callback=self.parse_score)

	def parse_score(self, response):
		item = response.meta['item']
		score = json.loads(response.body)['result']['score']
		item['score'] = {k: v.get('level', 'null') for k, v in score.items()}
		yield Request('http://my.csdn.net/service/main/get_knownarea_list?username=' + item['name'],
					  meta={'item': item}, callback=self.parse_field)

	def parse_field(self, response):
		item = response.meta['item']
		field = json.loads(response.body)['result']
		item['field'] = [fi.get('name', 'null') for fi in field]
		yield Request('http://my.csdn.net/service/main/uc', method='POST', meta={'item': item}, body=self.post_param(item['name'], 'getSkill'),
					  callback=self.parse_skill)

	def parse_skill(self, response):
		item = response.meta['item']
		body = json.loads(response.body)
		if str(body['err']) == '0':
			skill = body['result']
			item['skill'] = [sk.get('skillname', 'null') for sk in skill]
		else:
			item['skill'] = 'null'
		yield Request('http://my.csdn.net/service/main/uc', method='POST', meta={'item': item}, body=self.post_param(item['name'], 'getEduExp'),
					  callback=self.parse_edu)

	def parse_edu(self, response):
		item = response.meta['item']
		body = json.loads(response.body)
		if str(body['err']) == '0':
			edu = body['result']
			item['edu_experience'] = [ed.get('edustartdate', 'null') + ' ~ ' + ed.get('eduenddate', 'null')
									  + ' @' + ed.get('schoolname', 'null') + ' <' + ed.get('majorstr', 'null') + '>' for ed in edu]
		else:
			item['edu_experience'] = 'null'
		yield Request('http://my.csdn.net/service/main/uc', method='POST', meta={'item': item}, body=self.post_param(item['name'], 'getWorkExp'),
					  callback=self.parse_job)

	def parse_job(self, response):
		item = response.meta['item']
		body = json.loads(response.body)
		if str(body['err']) == '0':
			job = body['result']
			item['job_experience'] = [jb.get('workbegindate', 'null') + ' ~ ' + jb.get('workenddate', 'null')
									  + ' @' + jb.get('orgname', 'null') + ' <' + jb.get('job', 'null') + '|' + jb.get('workdesc', 'null') + '>' for jb in job]
		else:
			item['job_experience'] = 'null'
		yield Request('http://my.csdn.net/service/main/uc', method='POST', meta={'item': item}, body=self.post_param(item['name'], 'getContact'),
					  callback=self.parse_contact)

	def parse_contact(self, response):
		item = response.meta['item']
		body = json.loads(response.body)
		if str(body['err']) == '0':
			contact = body['result']
			item['email'] = contact['pubemail']
			item['phone'] = contact['submobile']
			for info in contact['contactinfo']:
				if int(info['type']) == 70:
					item['qq'] = info['value']
				elif int(info['type']) == 110:
					item['wechat'] = info['value']
				else:
					item['qq'] = 'null'
					item['wechat'] = 'null'
			else:
				item['qq'] = 'null'
				item['wechat'] = 'null'
		else:
			item['email'] = 'null'
			item['qq'] = 'null'
			item['wechat'] = 'null'
		yield item

	def post_param(self, usename, method_name):
		post_data = {'params': {'username':'%s' % str(usename),'method':'%s' % method_name}}
		return json.dumps(post_data)