# Scrapy settings for crawling project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'crawling'

SPIDER_MODULES = ['crawling.spiders']
NEWSPIDER_MODULE = 'crawling.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawling (+http://www.yourdomain.com)'
