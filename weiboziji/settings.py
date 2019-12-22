# -*- coding: utf-8 -*-

# Scrapy settings for weiboziji project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weiboziji'

SPIDER_MODULES = ['weiboziji.spiders']
NEWSPIDER_MODULE = 'weiboziji.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weiboziji (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3928.4 Safari/537.36',



}
# 修改编码为utf-8 防止中文写入乱码
FEED_EXPORT_ENCODING = 'utf-8-sig'


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'weiboziji.middlewares.WeibozijiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'weiboziji.middlewares.WeibozijiDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
      # 'weiboziji.pipelines.MySQL2TopicPipeline': 300,
      'weiboziji.pipelines.MySQL3TopicPipeline': 100,
}
# SPIDER_MIDDLEWARES = {
#    'scrapy_deltafetch.DeltaFetch': 50,
#    'scrapy_magicfields.MagicFieldsMiddleware': 51,
# }
# DELTAFETCH_ENABLED = True
# MAGICFIELDS_ENABLED = True
# MAGIC_FIELDS = {
#     "timestamp": "$time",
#     "spider": "$spider:name",
#     "url": "scraped from $response:url",
#     "domain": "$response:url,r'https?://([\w\.]+)/']",
# }
#时间
DOWNLOAD_DELAY = 4
#默认False;为True表示启用AUTOTHROTTLE扩展
AUTOTHROTTLE_ENABLED = True
#默认5秒;初始下载延迟时间
AUTOTHROTTLE_START_DELAY = 1
#默认60秒；在高延迟情况下最大的下载延迟
AUTOTHROTTLE_MAX_DELAY = 3

# TEM_PIPELINES = {
#    'tutorial.pipelines.TutorialPipeline': 300,
# }
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'user'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'
MYSQL_PORT = 3306


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
