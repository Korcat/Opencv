# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request
import os


class Scrapy4DangdangPipeline:

    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    # item就是传递给pipline的item对象
    def process_item(self, item, spider):
        self.fp.write(str(item))
        # with open('book.json', 'a', encoding='utf-8') as f:
        #     f.write(str(item))
        return item  # 不能丢掉这个部分

    def close_spider(self, spider):
        self.fp.close()


class DangdangPicDownload:

    def process_item(self, item, spider):
        file_name = f"page{item['page']}"
        if not os.path.exists(file_name):
            os.mkdir(file_name)
        pic_url = "https:" + str(item['src'])
        pic_name = str(item['name'])
        urllib.request.urlretrieve(url=pic_url, filename=file_name + '/' + pic_name + '.jpg')
        return item
