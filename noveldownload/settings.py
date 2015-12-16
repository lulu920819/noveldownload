# Scrapy settings for noveldownload project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'noveldownload'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['noveldownload.spiders']
NEWSPIDER_MODULE = 'noveldownload.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

DOWNLOAD_DELAY = 0

ITEM_PIPELINES = {
    'noveldownload.pipelines.NoveldownloadPipeline':300,
}


DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True

CONCURRENT_ITEMS = 128
CONCURRENT_REQUEST = 64
CONCURRENT_REQUEST_PER_DOMAIN = 64


LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = '../test.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False