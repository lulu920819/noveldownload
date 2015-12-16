# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from noveldownload.items import NoveldownloadItem
from scrapy.http import Request

class NovelSpider(CrawlSpider):
    #name="doubanmoive"
    #allowed_domains=["movie.douban.com"]
    #start_urls=["http://movie.douban.com/top250"]
    name="noveldownload"
    allowed_domains=["lwxs520.com"]
    start_urls=["http://www.lwxs520.com/books/21/21156/4773876.html"]
    
#    rules=[
#        Rule(SgmlLinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
#        Rule(SgmlLinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')),callback="parse_item"),      
#    ]
    def parse(self,response):       
        prefix = 'http://www.lwxs520.com/books/21/21156/'
        item = NoveldownloadItem()
        sel = HtmlXPathSelector(response)
        title = sel.select('//*[@id="bgdiv"]/table[2]/tbody/tr[1]/td/div/h1') 
        # //*[@id="content"]/p
        content = sel.select('//*[@id="content"]/p').extract()
        #print title
        #print content
        item['title'] = title
        item['content'] = content
        #print item['title']
        #print item['content']      

        yield item

        nexturl = sel.select('//*[@id="thumb"]/a[3]/@href').extract()
        url = prefix + nexturl[0]
        print url
        yield Request(url, callback=self.parse)
        #sel = HtmlXPathSelector(response)
        #raw_urls = sel.select('//*[@class="dccss"]/a/@href').extract()
        #urls = []
        #for url in raw_urls:
            #print url
            #link = url.select('@href').extract()
            #print link[0]
        #    url = prefix +url 
         #   urls.append(url)


        #for item_url in urls:
        #    print url
        #    yield scrapy.Request(url = item_url, callback = self.parse_item)

    #def parse_item(self, response):
   #     item = NoveldownloadItem()
   #     sel = HtmlXPathSelector(response)
   #     item['title'] = sel.select('//*[@id="bgdiv"]/table[2]/tbody/tr[1]/td/div/h1') 
   #     item['content'] = sel.select('//*[@id="content"]/p')
   #     print item['title']
   #     print item['content']
   #     return item


       # //*[@id="thumb"]/a[3]

        