import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字
    name = "baidu"
    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]
    #  start_urls = "https://" + allowed_domains
    start_urls = ["https://www.baidu.com"]

    # response = urllib.request.urlopen()
    # response = requests.get()
    def parse(self, response):
        print("今天的重庆是晴天！")

