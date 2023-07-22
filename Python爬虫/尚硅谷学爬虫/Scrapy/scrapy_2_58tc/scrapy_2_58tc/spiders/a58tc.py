import scrapy


class A58tcSpider(scrapy.Spider):
    name = "58tc"
    allowed_domains = ["cq.58.com"]
    start_urls = ["https://cq.58.com/?utm_source=market"]

    def parse(self, response):
        print("-----------------------------")

        # 页面源码字符串
        content = response.text
        # 页面源码二进制流
        # content_byte=response.body
        # print(content_byte)
        text = response.xpath('/html/body/div[2]/div/div[2]/div/a[1]/img') # 返回的是selector对象
        print(text)
        print("---------------------------")
        print(text.extract_first()) # 提取selector对象的第一个
        print(text.extract()) # 提取selector对象（如果是列表，则会提取所有的）
        print("---------------------------")
        # print(content.xpath('/html/body/div[2]/div/div[2]/div/a[1]/img[1]')) # 这样是错误的
        # print(response.extract()) # False
