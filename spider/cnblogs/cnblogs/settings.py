# -*- coding: utf-8 -*-

# Scrapy settings for cnblogs project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'cnblogs'

SPIDER_MODULES = ['cnblogs.spiders']
NEWSPIDER_MODULE = 'cnblogs.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'cnblogs (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'cnblogs.middlewares.CnblogsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
	# 'cnblogs.middlewares.MyCustomDownloaderMiddleware': 543,
	'cnblogs.middlewares.RandomUserAgent': 1,
	'cnblogs.middlewares.ProxyMiddleware': 100,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
	'cnblogs.pipelines.JsonWithEncodingCnblogsPipeline': 300,
}
LOG_LEVEL = 'INFO'
LOG_FILE = 'cnblogs.log'
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# add by mazcheng @20170809
CnblogsFilename = '/home/mazhicheng/project/spider/ScrapySpider/sp1/cnblogs/cnblogs.json'
USER_AGENTS = [
	'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
	'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
	'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
	'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
	'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
	'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Maxthon 2.0)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; TencentTraveler 4.0)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; The World)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; 360SE)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Avant Browser)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
	'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; Maxthon 2.0)',
	'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; TencentTraveler 4.0)',
	'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; The World)',
	'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 360SE)',
	'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; Avant Browser)',
	'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0)',
	'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
	'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
	'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
	'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
	'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
	'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0)',
	'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Maxthon 2.0)',
	'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; TencentTraveler 4.0)',
	'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; The World)',
	'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; 360SE)',
	'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Avant Browser)',
	'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Maxthon 2.0)',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; TencentTraveler 4.0)',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; The World)',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; 360SE)',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Avant Browser)',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0)',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0 Safari/535.11',
	'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
	'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
	'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
	'Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0 Safari/537.36',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
	'Mozilla/5.0 (MSIE 9.0; Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko QQBrowser/8.1.3886.400',
	'Mozilla/5.0 (MSIE 9.0; Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko QQBrowser/8.2.3638.400',
	'Mozilla/5.0 (MSIE 9.0; Windows NT 6.0; Trident/7.0; rv:11.0) like Gecko QQBrowser/8.3.4765.400',
	'Mozilla/5.0 (MSIE 9.0; Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko QQBrowser/9.1.3471.400',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; 2345Explorer 3.4.0.12519)',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; 2345Explorer 3.5.0.12758)',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; 2345Explorer 4.0.0.13120)',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; 2345Explorer 4.2.0.13550)',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; 2345Explorer 5.0.0.14004)',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; 2345Explorer/6.1.0.8158)',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; 2345Explorer/6.2.0.9202)',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; UBrowser/5.0.1369.26)',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; UBrowser/5.2.2603.1)',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; UBrowser/5.4.4237.43)',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:34.0) Gecko/20100101 Firefox/34.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:36.0) Gecko/20100101 Firefox/36.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:37.0) Gecko/20100101 Firefox/37.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:39.0) Gecko/20100101 Firefox/39.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:41.0) Gecko/20100101 Firefox/41.0',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/2.1.7.6 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.11 YYE/3.6 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.46 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2478.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2498.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36',
	'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
	'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
	'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
	'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
	'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
	'Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62',
	'Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62',
	'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
	'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52',
	'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51',
	'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00',
	'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00',
	'Opera/12.0 (Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00',
	'Opera/12.0 (Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00',
	'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
	'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
	'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1',
	'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
	'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
	'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
	'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
	'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3',
	'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
]

PROXIES = [
	'https://45.76.48.211:3128',
	'https://195.211.189.143:3128',
	'http://177.5.219.112:8080',
	'https://203.189.88.200:8080',
	'http://119.9.89.61:8088',
	'https://165.138.124.4:8080',
	'https://45.76.48.192:3128',
	'https://128.199.85.45:8080',
	'https://179.189.192.36:8080',
	'https://149.56.44.146:1080',
	'https://200.29.191.151:3128',
	'http://36.67.16.209:53281',
	'http://43.245.216.32:53281',
	'http://63.85.203.40:8080',
	'http://41.205.36.88:80',
	'http://179.189.236.130:53281',
	'http://61.130.97.212:8099',
	'http://95.143.192.191:80',
	'http://95.47.137.32:3128',
	'http://149.202.94.120:3128',
	'http://47.52.108.18:80',
	'http://177.67.83.145:8080',
	'http://24.249.80.22:3128',
	'http://138.59.176.246:8080',
	'http://183.89.36.113:8080',
	'http://183.222.102.100:8080',
	'http://149.56.44.146:9201',
	'http://191.252.113.223:8080',
	'http://139.129.94.241:3128',
	'http://36.67.128.145:8080',
	'http://202.152.63.5:53281',
	'http://125.46.69.18:3128',
	'http://144.217.242.194:1080',
	'http://124.172.191.20:80',
	'http://125.24.156.53:8080',
	'http://108.61.146.90:3128',
	'http://221.7.36.78:80',
	'http://103.220.28.220:53281',
	'http://154.73.157.20:80',
	'http://124.167.149.46:80',
	'http://120.25.211.80:9999',
	'http://45.76.48.211:3128',
	'http://139.196.106.82:8118',
	'http://217.15.85.202:8080',
	'http://47.52.24.117:80',
	'http://123.7.82.20:3128',
	'http://78.63.141.133:3128',
	'http://47.89.20.133:3128',
	'http://89.186.229.43:8080',
	'http://120.52.21.132:8082',
	'http://105.22.33.122:8888',
	'http://221.133.44.142:8080',
	'http://45.77.35.149:3128',
	'http://181.112.62.26:53281',
	'http://180.254.209.197:80',
	'http://117.14.241.7:81',
	'http://125.43.164.173:8888',
	'http://42.51.26.79:3128',
	'http://92.126.153.114:8080',
	'http://221.7.36.78:9999',
	'http://45.32.103.86:3128',
	'http://111.13.7.119:80',
	'http://177.113.241.12:8080',
	'http://182.126.176.146:8118',
	'http://197.232.51.228:53281',
	'http://212.192.120.42:8080',
	'http://103.67.197.138:53281',
	'http://91.202.133.104:8080',
	'http://111.13.7.122:80',
	'http://186.231.100.117:8080',
	'http://185.171.60.25:8080',
	'http://137.59.44.47:80',
	'http://36.67.50.242:8080',
	'http://46.44.52.61:8081',
	'http://123.207.30.187:3128',
	'http://185.148.220.11:8081',
	'http://61.6.6.248:53281',
	'http://212.237.6.245:3128',
	'http://101.53.101.172:9999',
	'http://115.182.231.52:80',
	'http://197.232.17.83:8080',
	'http://61.7.191.81:8080',
	'http://201.184.226.98:53281',
	'http://123.103.93.38:80',
	'http://14.211.26.50:8080',
	'http://81.211.43.102:8081',
	'http://178.222.163.147:8080',
	'http://111.9.116.225:8080',
	'http://188.166.217.2:8888',
	'http://187.110.213.74:53281',
	'http://93.91.112.185:80',
	'http://182.253.154.99:8080',
	'http://131.221.120.178:53281',
	'http://138.197.211.31:3128',
	'http://68.196.97.60:8080',
	'https://158.69.198.191:3128',
	'http://183.222.102.105:8080',
	'http://169.239.49.140:8080',
	'http://182.253.197.60:80',
	'http://80.237.54.157:8080',
]
