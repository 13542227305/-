# -*- coding: utf-8 -*-
# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html

SPIDER_MODULES = ['woaidu.spiders']
NEWSPIDER_MODULE = 'woaidu.spiders'

# 替换成自己的UA
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 ' \
             'Safari/537.36 '
# 设置重复过滤器的模块
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 设置调度器，scrapy_resis中的调度器具备与数据库交互的功能
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 设置爬虫结束的时候是否保存redis数据库的去重集合与任务队列
SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# 这里如果用不需要的可以注释掉
ITEM_PIPELINES = {
    # 'scrapy_redis.pipelines.RedisPipeline': 400,
    'woaidu.pipelines.WoaiduPipeline': 300,
}

# 设置redis数据库
REDIS_URL = "redis://127.0.0.1:6379"

# LOG_LEVEL = 'DEBUG'  # 可以注释掉

DOWNLOAD_DELAY = 1  # 这个是每个爬虫间隔的时间

# 配置MongoDB
MONGODB_HOST = '127.0.0.1'
# 端口号，默认27017
MONGODB_PORT = 27017
# 设置数据库名称
MONGODB_DBNAME = 'woaidu'
# 存放本数据的表名称
MONGODB_DOCNAME = 'woaidubook'





















# # Scrapy settings for woaidu project
# #
# # For simplicity, this file contains only settings considered important or
# # commonly used. You can find more settings consulting the documentation:
# #
# #     https://docs.scrapy.org/en/latest/topics/settings.html
# #     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# #     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#
# BOT_NAME = 'woaidu'
#
# SPIDER_MODULES = ['woaidu.spiders']
# NEWSPIDER_MODULE = 'woaidu.spiders'
#
#
# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# #USER_AGENT = 'woaidu (+http://www.yourdomain.com)'
#
# # Obey robots.txt rules
# ROBOTSTXT_OBEY = True
#
# # Configure maximum concurrent requests performed by Scrapy (default: 16)
# #CONCURRENT_REQUESTS = 32
#
# # Configure a delay for requests for the same website (default: 0)
# # See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# # See also autothrottle settings and docs
# #DOWNLOAD_DELAY = 3
# # The download delay setting will honor only one of:
# #CONCURRENT_REQUESTS_PER_DOMAIN = 16
# #CONCURRENT_REQUESTS_PER_IP = 16
#
# # Disable cookies (enabled by default)
# #COOKIES_ENABLED = False
#
# # Disable Telnet Console (enabled by default)
# #TELNETCONSOLE_ENABLED = False
#
# # Override the default request headers:
# #DEFAULT_REQUEST_HEADERS = {
# #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #   'Accept-Language': 'en',
# #}
#
# # Enable or disable spider middlewares
# # See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# #SPIDER_MIDDLEWARES = {
# #    'woaidu.middlewares.WoaiduSpiderMiddleware': 543,
# #}
#
# # Enable or disable downloader middlewares
# # See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# #DOWNLOADER_MIDDLEWARES = {
# #    'woaidu.middlewares.WoaiduDownloaderMiddleware': 543,
# #}
#
# # Enable or disable extensions
# # See https://docs.scrapy.org/en/latest/topics/extensions.html
# #EXTENSIONS = {
# #    'scrapy.extensions.telnet.TelnetConsole': None,
# #}
#
# # Configure item pipelines
# # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# #ITEM_PIPELINES = {
# #    'woaidu.pipelines.WoaiduPipeline': 300,
# #}
#
# # Enable and configure the AutoThrottle extension (disabled by default)
# # See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# #AUTOTHROTTLE_ENABLED = True
# # The initial download delay
# #AUTOTHROTTLE_START_DELAY = 5
# # The maximum download delay to be set in case of high latencies
# #AUTOTHROTTLE_MAX_DELAY = 60
# # The average number of requests Scrapy should be sending in parallel to
# # each remote server
# #AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# # Enable showing throttling stats for every response received:
# #AUTOTHROTTLE_DEBUG = False
#
# # Enable and configure HTTP caching (disabled by default)
# # See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# #HTTPCACHE_ENABLED = True
# #HTTPCACHE_EXPIRATION_SECS = 0
# #HTTPCACHE_DIR = 'httpcache'
# #HTTPCACHE_IGNORE_HTTP_CODES = []
# #HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
