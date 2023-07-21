import requests

url = "http://www.baidu.com/s?"  # 不加“？”也可以
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 '
                  'Safari/537.36 Edg/114.0.1823.82 '
}
# data不需要urlencode编码
data = {
    'wd': '北京'
}
response = requests.get(url=url, params=data, headers=headers)  # data和headers都不需要分装到request对象里（请求定制）
response.encoding = 'utf-8'
content = response.text
print(content)
