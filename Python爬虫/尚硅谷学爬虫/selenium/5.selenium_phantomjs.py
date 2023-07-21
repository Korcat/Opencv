"""
会报错
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.baidu.com"
browser = webdriver.PhantomJS('phantomjs.exe')  # 4.3.0版本的selenium已经不支持phantomjs了
browser.get(url)

browser.save_screenshot('baidu.jpg')
