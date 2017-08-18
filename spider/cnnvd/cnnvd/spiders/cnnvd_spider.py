#!/apps/ns/python/bin/python
# _*_coding:utf-8_*_

"""
@author: mazhicheng
@file: cnnvd_spider.py
@time: 2017/8/16 18:21
"""

import re
import logging
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.response import get_base_url
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
from cnnvd.items import *
# from cnnvd.settings import LOG_CONF

# logging.config.fileConfig(LOG_CONF)

class CnnvdSpider(CrawlSpider):
	name = 'CnnvdSpider'
	allowed_domains = ['cnnvd.org.cn']
	start_urls = [
		'http://www.cnnvd.org.cn/web/vulnerability/querylist.tag?pageno=1099',
		'http://www.cnnvd.org.cn/web/cnnvdpatch/querylist.tag?pageno=1494',
	]
	rules = [
		# 漏洞列表页
		Rule(LinkExtractor(allow=(r'/web/vulnerability/querylist\.tag', ), deny=('qstartdateXq', 'relLdKey',
																				 'cvCnnvdUpdatedateXq','cpvendor')),
			 follow=True,
			 callback='parse_vuln'),
		# 补丁列表页
		Rule(LinkExtractor(allow=(r'/web/cnnvdpatch/querylist\.tag', ), ),
			 follow=True,
			 callback='parse_patch'),
		# 漏洞详情页
		Rule(LinkExtractor(allow=(r'/web/xxk/ldxqById\.tag', ), deny=('qstartdateXq', 'relLdKey',
																	  'cvCnnvdUpdatedateXq', 'cpvendor')),
			 follow=True,
			 callback='parse_vuln_item'),
		# 补丁详情页
		Rule(LinkExtractor(allow=(r'/web/xxk/bdxqById\.tag', ), ),
			 follow=True,
			 callback='parse_patch_item'),
	]

	host = 'http://www.cnnvd.org.cn'

	PAGE_NO = re.compile(r'(.*?pageno=)(\d+)')
	VULN_ID = re.compile(r'.*?=(CNNVD-\d+-\d+)')

	def parse_vuln(self, response):
		logging.critical(response.url)
		vuln_selector = Selector(response)
		vuln_href = vuln_selector.xpath("//a[@class='a_title2']/@href")
		for href in vuln_href.extract():
			abs_url = self.host + href
			yield Request(abs_url, callback=self.parse_vuln_item)
		try:
			if 'pageno' in response.url:
				comm_url, page_no = self.PAGE_NO.search(response.url).groups()
				abs_url = comm_url + str(int(page_no)+1)
			else:
				abs_url = self.host + '/web/vulnerability/querylist.tag?pageno=2'
			yield Request(abs_url, callback=self.parse_vuln)
		except Exception as e:
			logging.error('parse_vuln URL[%s] ERR[%s]' % (response.url, e))

	def parse_patch(self, response):
		logging.critical(response.url)
		patch_selector = Selector(response)
		patch_href = patch_selector.xpath("//a[@class='a_title2']/@href")
		for href in patch_href.extract():
			abs_url = self.host + href
			yield Request(abs_url, callback=self.parse_patch_item)
		try:
			if 'pageno' in response.url:
				comm_url, page_no = self.PAGE_NO.search(response.url).groups()
				abs_url = comm_url + str(int(page_no) + 1)
			else:
				abs_url = self.host + '/web/cnnvdpatch/querylist.tag?pageno=2'
			yield Request(abs_url, callback=self.parse_patch)
		except Exception as e:
			logging.error('parse_vuln URL[%s] ERR[%s]' % (response.url, e))

	def parse_vuln_item(self, response):
		logging.critical(response.url)
		vuln_item_selector = Selector(response)
		vuln_detail = vuln_item_selector.xpath("//div[contains(@class, 'detail_xq') and contains(@class, 'w770')]")
		vuln_notice_refer_entry_patch = vuln_item_selector.xpath("//div[contains(@class, 'd_ldjj') and contains(@class, 'm_t_20')]")

		vuln_item = CnnvdVulnItem()
		vuln_item['vuln_id'] = self._clean_extract_first(vuln_detail, 'ul/li[1]/span/text()')
		vuln_item['name'] = self._clean_extract_first(vuln_detail, 'h2/text()')
		vuln_item['harm_level'] = self._clean_extract_first(vuln_detail, 'ul/li[2]/a/text()')
		vuln_item['cve_id'] = self._clean_extract_first(vuln_detail, 'ul/li[3]/a/text()')
		vuln_item['vuln_type'] = self._clean_extract_first(vuln_detail, 'ul/li[4]/a/text()')
		vuln_item['report_time'] = self._clean_extract_first(vuln_detail, 'ul/li[5]/a/text()')
		vuln_item['threat_type'] = self._clean_extract_first(vuln_detail, 'ul/li[6]/a/text()')
		vuln_item['update_time'] = self._clean_extract_first(vuln_detail, 'ul/li[7]/a/text()')
		vuln_item['company'] = self._clean_extract_first(vuln_detail, 'ul/li[8]/a/text()')
		vuln_item['vuln_source'] = self._clean_extract_first(vuln_detail, 'ul/li[9]/a/text()')

		vuln_item['vuln_abstract'] = self._merge_clean_extract(vuln_item_selector, "//div[@class='d_ldjj']/p/text()")
		vuln_item['vuln_abstract'] += self._merge_clean_extract(vuln_item_selector, "//div[@class='d_ldjj']/p/a/text()")

		vuln_item['vuln_notice'] = self._merge_clean_extract(vuln_item_selector,
															 '/html/body/div[4]/div/div[1]/div[4]/p/text()')
		vuln_item['vuln_notice'] += self._merge_clean_extract(vuln_item_selector,
															  '/html/body/div[4]/div/div[1]/div[4]/p/a/text()')
		vuln_item['refer_site'] = self._merge_clean_extract(vuln_item_selector,
															'/html/body/div[4]/div/div[1]/div[5]/p/text()')
		vuln_item['refer_site'] += self._merge_clean_extract(vuln_item_selector,
															 '/html/body/div[4]/div/div[1]/div[5]/p/a/text()')
		vuln_item['affect_entry'] = self._merge_clean_extract(vuln_item_selector,
															  '/html/body/div[4]/div/div[1]/div[6]/p/text()')
		vuln_item['affect_entry'] += self._merge_clean_extract(vuln_item_selector,
															   '/html/body/div[4]/div/div[1]/div[6]/p/a/text()')
		vuln_item['patch'] = self._merge_clean_extract(vuln_item_selector,
													   '/html/body/div[4]/div/div[1]/div[7]/p/text()')
		vuln_item['patch'] += self._merge_clean_extract(vuln_item_selector,
														'/html/body/div[4]/div/div[1]/div[7]/p/a/text()')
		yield vuln_item

	def parse_patch_item(self, response):
		logging.critical(response.url)
		patch_item_selector = Selector(response)
		patch_detail = patch_item_selector.xpath("//div[contains(@class, 'detail_xq') and contains(@class, 'w770')]")

		patch_item = CnnvdPatchItem()
		patch_item['patch_id'] = self._clean_extract_first(patch_detail, 'ul/li[1]/text()')
		patch_item['name'] = self._clean_extract_first(patch_detail, 'h2/text()')
		patch_item['size'] = self._clean_extract_first(patch_detail, 'ul/li[2]/text()')
		patch_item['important_level'] = self._clean_extract_first(patch_detail, 'ul/li[3]/text()')
		patch_item['report_time'] = self._clean_extract_first(patch_detail, 'ul/li[4]/text()')
		patch_item['company'] = self._clean_extract_first(patch_detail, 'ul/li[5]/text()')
		patch_item['company_homepage'] = self._clean_extract_first(patch_detail, 'ul/li[6]/a/text()')
		patch_item['md5_val'] = self._clean_extract_first(patch_detail, 'ul/li[7]/text()')
		patch_item['refer_site'] = self._merge_clean_extract(patch_item_selector, "//div[@class='d_ldjj']/p/text()")
		patch_item['refer_site'] += self._merge_clean_extract(patch_item_selector, "//div[@class='d_ldjj']/p/a/text()")
		patch_item['vuln'] = self._merge_clean_extract(patch_item_selector, "//a[@class='a_title2']/@href", ', ')
		patch_item['vuln'] = self.VULN_ID.findall(patch_item['vuln'])

		yield patch_item

	def _clean_extract_first(self, selector, xpath_path, default_str=''):
		try:
			extract_first_result = selector.xpath(xpath_path).extract_first(default_str)
			return extract_first_result.strip()
		except Exception as e:
			return ''

	def _merge_clean_extract(self, selector, xpath_path, join_str=''):
		try:
			clean_extract_result = map(lambda x: x.strip(), selector.xpath(xpath_path).extract())
			return join_str.join(clean_extract_result)
		except Exception as e:
			return ''