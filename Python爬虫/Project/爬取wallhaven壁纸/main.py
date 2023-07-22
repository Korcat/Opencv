from bs4 import BeautifulSoup
import urllib
import threading
import requests
import os

base_url = "https://wallhaven.cc/toplist?page="
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 '
                  'Safari/537.36 Edg/114.0.1823.82 '
}
proxies = {
    'http': '60.167.22.29:1133'
}


def crawl(page):
    file_name = f"page{page}"
    if not os.path.exists(file_name):
        os.mkdir(file_name)  # 由于存在两级目录都没创建的情况，这里要用“makedirs”
    # data = {
    #     'page': page
    # }
    url = base_url + str(page)
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    li_list = soup.find("div", id="thumbs").find("ul").find_all("li")

    for i, li in enumerate(li_list):
        pic_url = li.find("figure").find("a")["href"]
        pic_response = requests.get(url=pic_url, headers=headers)
        pic_soup = BeautifulSoup(pic_response.text, 'lxml')
        pic_link = pic_soup.find("main").find("section").find_all("div")[0].find("img")["src"]
        pic_byte = requests.get(url=pic_link, headers=headers).content
        with open(file_name + '/' + f"{i + 1}.jpg", 'wb') as f:
            f.write(pic_byte)


def crawl_pages(start_page, end_page):
    for i in range(start_page, end_page + 1):
        crawl(i)


# urllib.request.urlretrieve(url="https://w.wallhaven.cc/full/p9/wallhaven-p9yl39.jpg", filename='test.jpg')
if __name__ == '__main__':
    # pic_response = requests.get(url="https://w.wallhaven.cc/full/p9/wallhaven-p9yl39.jpg", headers=headers)
    thread_num = 5
    for i in range(thread_num):
        threading.Thread(name=f'thread{i + 1}', target=crawl_pages, args=(i * 20 + 1, i * 20 + 20))
