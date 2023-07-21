from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.baidu.com"
browser = webdriver.Chrome()
browser.get(url)
text1 = browser.find_element(By.ID, "su")
text2 = browser.find_element(By.LINK_TEXT, "新闻")

# 获取标签class属性值
print(text1.get_attribute('class'))
# 获取标签的名字
print(text1.tag_name)
# 获取标签的文本（<........>文本<........>）
print(text2.text)
browser.quit()
