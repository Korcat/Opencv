import requests
import json

url = "https://fanyi.baidu.com/sug"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 '
                  'Safari/537.36 Edg/114.0.1823.82 '
}
data = {
    'kw': 'sun'
}
response = requests.post(url=url, data=data, headers=headers)  # 请求参数是data
response.encoding = 'utf-8'
content = response.text  # 返回的是json数据,需要在json中编码
content_json = json.loads(content)  # 自动变为utf-8
print(content_json)
