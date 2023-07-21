from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# chrome_options = Options()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(options=chrome_options)
# url = "https://www.baidu.com"
# browser.get(url)
# browser.save_screenshot('headless.png')
def headless_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    return browser


if __name__ == '__main__':
    browser = headless_browser()
    url = "https://www.baidu.com"
    browser.get(url)
    browser.save_screenshot('headless.png')
