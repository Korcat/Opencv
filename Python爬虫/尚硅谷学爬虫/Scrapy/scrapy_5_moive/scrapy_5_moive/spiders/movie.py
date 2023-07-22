import scrapy
from scrapy_5_moive.items import Scrapy5MoiveItem


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.dy2018.com"]
    start_urls = ["https://www.dy2018.com/html/bikan/"]

    def parse(self, response):
        print("==========parse===========")
        li_list = response.xpath('//div[@class="co_content8"]/ul//b/a[2]')
        for li in li_list:
            name = li.xpath('./text()').extract_first()
            src_href = li.xpath('./@href').extract_first()
            # print(name, src_href)
            # 图片的跳转地址
            src_url = "https://www.dy2018.com" + src_href
            # print(src_url)
            yield scrapy.Request(url=src_url, callback=self.parse_src, meta={'name': name})  # 注意加self

    def parse_src(self, response):
        print("=========parse_src===========")
        src = response.xpath('//div[@id="Zoom"]/img[1]/@src').extract_first()
        # print(src)
        name = response.meta['name']
        print(name)

        movie = Scrapy5MoiveItem(name=name, src=src)

        yield movie


