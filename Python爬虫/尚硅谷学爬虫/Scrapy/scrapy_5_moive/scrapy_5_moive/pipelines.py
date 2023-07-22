# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import urllib.request
import requests


class Scrapy5MoivePipeline:
    def process_item(self, item, spider):
        file_name = "电影天堂"
        if not os.path.exists(file_name):
            os.mkdir(file_name)  # 默认创建的文件夹都在spiders下
        # urllib.request.urlretrieve(url=str(item['src']), filename=file_name + '/' + str(item['name']) + '.jpg')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/114.0.0.0 '
                          'Safari/537.36 Edg/114.0.1823.82 ',

        }
        response = requests.get(url=str(item['src']), headers=headers)
        content = response.content
        with open(file_name + '/' + str(item['name']) + '.jpg', 'wb') as f:
            f.write(content)
        return item
