"""
__VIEWSTATE: MGsgwj2xq/49YgM4TF6XQbWUMM78vyekMLRkIV7DJyvO8XOQgpqS0Y4AB/Kr5v68Afhz8OQWnsk2TZamaB7Z7tMgERqLDRmSH6hyR46QYvESQo1S7ph6p4C6p+fJNFak+AhIkImYGv/HWPhIdC23jrD+eV4=
__VIEWSTATEGENERATOR: C93BE1AE
from:
email: 1220353261@qq.com
pwd: afafafa
code: iwl9
denglu: 登录
"""
import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import cv2
import os
import numpy as np
from io import BytesIO

url = "https://so.gushiwen.cn/user/login.aspx"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 '
                  'Safari/537.36 Edg/114.0.1823.82 ',
}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
content = response.text
# print(content)

# 1.获取__VIEWSTATE、__VIEWSTATEGENERATOR
soup = BeautifulSoup(content, 'lxml')
VIEWSTATE = soup.select('#__VIEWSTATE')[0].attrs['value']
VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs['value']
# print(VIEWSTATE)
# print(VIEWSTATEGENERATOR)

# 2.获取验证码
_url = soup.select('#imgCode')[0].attrs['src']
base_url = "https://so.gushiwen.cn"
code_url = base_url + _url
session = requests.session()
response_s = session.get(url=code_url)
content_s = response_s.content
print(content_s)
with open('code.gif', 'wb') as f:
    f.write(content_s)


# 3.登录
login_url = "https://so.gushiwen.cn/user/login.aspx"
code = input("请输入验证码：")
data = {
    '__VIEWSTATE': VIEWSTATE,
    '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
    'from': '',
    'email': '16674258254',
    'pwd': '20030725',
    'code': code,
    'denglu': '登录'
}
response_end = session.post(url=login_url, data=data, headers=headers)  # 注意这里为session对象
response_end.encoding = 'utf-8'
content_end = response_end.text
with open("古诗文网首页.html", 'w', encoding='utf-8') as f:
    f.write(content_end)
