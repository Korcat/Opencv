"""
require:
1.安装selenium
2.将相应的驱动.exe文件放在对应环境的python目录下（这里是conda环境）
Firefox浏览器不能作为selenium浏览器驱动
"""
from selenium import webdriver

# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options


# browser = webdriver.Firefox()
# browser = webdriver.Edge()
browser = webdriver.Chrome()

url = "https://www.jd.com/"
browser.get(url)
content = browser.page_source
print(content)
