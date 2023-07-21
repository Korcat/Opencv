"""
一个类型，六个属性

"""
import requests

url = "https://www.baidu.com"

response = requests.get(url=url)

# 类型：requests.models.Response
print(type(response))

# 属性
# 1.编码格式
response.encoding = 'utf-8'
# 2.网页源码
print(response.text)
# 3.网页url
print(response.url)
# 4. 网页源码的二进制数据
print(response.content)
# 5.响应的状态码
print(response.status_code)
# 6.响应头
print(response.headers)
