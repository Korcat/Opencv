from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.baidu.com"

browser = webdriver.Chrome()
browser.get(url)
# browser = webdriver.Firefox()

# 1.根据id属性获取标签
button_id = browser.find_element(By.ID, "su")  # id="su"
print(button_id)
# 2.通过name属性选择文本框元素，并设置内容
# browser.find_element(By.NAME, 'wd').send_keys("selenium")
button_name = browser.find_element(By.NAME, 'wd')
print(button_name)
# 3.通过xpath
button_xpath = browser.find_element(By.XPATH, '//input[@id="su"]')
print(button_xpath)
# 4.通过tag标签
button_tag = browser.find_element(By.TAG_NAME, "input")
print(button_tag)
# 5.通过class属性
button_class = browser.find_element(By.CLASS_NAME, "s_ipt")  # 目前不清楚的这里的class属性怎么来的
print(button_class)
# 6.通过css
button_css = browser.find_element(By.CSS_SELECTOR, "#su")
print(button_css)
# 7.通过链接文本定位链接
button_link = browser.find_element(By.LINK_TEXT, '新闻')
print(button_link)
browser.quit()
