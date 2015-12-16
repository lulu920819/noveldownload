# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class NoveldownloadPipeline(object):
    def process_item(self, item, spider):
    	datapath = '../test.php'
    	fd = open(datapath,'a')
    	line = str(item['title']) + '#$#' +str(item['content'])+'\n'
    	fd.write(line)
    	fd.close
        return item
