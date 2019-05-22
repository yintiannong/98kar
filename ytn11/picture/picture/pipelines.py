# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import uuid
class PicturePipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    def get_media_requests(self, item, info):
        return [Request(x,meta={'fold_name':item['fold_name']}) for x in item.get(self.images_urls_field, [])]
    def file_path(self, request, response=None, info=None):
        fold_name=request.mata['fold_name']
        return fold_name+'\\'+str(uuid.uuid4())+'.jpg'
