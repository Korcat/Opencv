from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.baidu.com"
browser = webdriver.Chrome()
browser.get(url)
# 在搜索栏中输入关键字
browser.find_element(By.NAME,"wd").send_keys("周杰伦")
# 停顿两秒
time.sleep(2)
# 点击“百度一下”按钮
browser.find_element(By.ID,"su").click()
# 停顿两秒
time.sleep(2)
# 滑到页面底部
js_bottom='document.documentElement.scrollTop=100000'
# execute='window.scrollBy(0,10000)'
browser.execute_script(js_bottom)
# 停顿两秒
time.sleep(2)
# 点击下一页
browser.find_element(By.CLASS_NAME,'n').click() # 这里class="n"的标签只有一个
# 停顿两秒
time.sleep(2)
# 滑到页面底部
browser.execute_script(js_bottom)
# 停顿两秒
time.sleep(2)
# 返回上一步
browser.back()
# 停顿两秒
time.sleep(2)
# 前进一步
browser.forward()
# 停顿两秒
time.sleep(2)

browser.quit()
