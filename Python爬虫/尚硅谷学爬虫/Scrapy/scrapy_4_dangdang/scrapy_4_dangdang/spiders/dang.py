import scrapy
from scrapy_4_dangdang.items import Scrapy4DangdangItem


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]
    base_url = "http://category.dangdang.com/pg"
    page = 1

    def parse(self, response):
        print("========================")
        # src = response.xpath('//ul[@id="component_59"]/li/a/img/@data-original')
        # alt = response.xpath('//ul[@id="component_59"]/li/a/img/@alt')
        # price = response.xpath('//ul[@id="component_59"]/li/p[3]/span[1]/text()')
        li_list = response.xpath('//ul[@id="component_59"]/li')
        # print(li_list)
        for li in li_list:
            src = li.xpath('./a/img/@data-original').extract_first()
            if not src:
                src = li.xpath('./a/img/@src').extract_first()
            name = li.xpath('./a/img/@alt').extract_first()
            price = li.xpath('./p[3]/span[1]/text()').extract_first()
            # print(src, name, price)

            # 用items类将爬取的数据集成为对象
            book = Scrapy4DangdangItem(src=src, name=name, price=price, page=self.page)
            # yield用于将items对象传递给pipeline
            yield book
        # 递归爬取每一页
        if self.page < 5:
            self.page += 1

            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'

            yield scrapy.Request(url=url, callback=self.parse)
