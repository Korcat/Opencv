from bs4 import BeautifulSoup
import urllib
import threading
import requests
import os

url = "https://wallhaven.cc/toplist"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 '
                  'Safari/537.36 Edg/114.0.1823.82 '
}
proxies = {
    'http': '60.167.22.29:1133'
}


def craw(page):
    file_name = os.path.join(os.getcwd(), f"page{page}")
    if not os.path.exists(file_name):
        os.makedirs(file_name)  # 由于存在两级目录都没创建的情况，这里要用“makedirs”
    data = {
        'page': page
    }
    response = requests.get(url=url, data=data, headers=headers)
    response.encoding = 'utf-8'
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    pic_text = soup.find("div", id="thumbs").find("ul").find_all("li")
    for i, text in enumerate(pic_text):
        pic_url = text.find("figure").find("img")["data-src"]
        pic_response = requests.get(url=pic_url, headers=headers)
        with open(file_name + '/' + f"{i + 1}.jpg", 'wb') as f:
            f.write(pic_response.content)


def craw_page(page):
    data = {
        'page': page
    }
    response = requests.get(url=url, data=data, headers=headers)
    response.encoding = 'utf-8'
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    sections = soup.find_all("div", id="thumbs")
    for i, section in enumerate(sections):
        file_name = os.path.join(os.getcwd(), f"page{i + 1}")
        if not os.path.exists(file_name):
            os.makedirs(file_name)  # 由于存在两级目录都没创建的情况，这里要用“makedirs”
        pic_text = section.find("ul").find_all("li")
        for j, text in enumerate(pic_text):
            pic_url = text.find("figure").find("img")["data-src"]
            pic_response = requests.get(url=pic_url, headers=headers)
            with open(file_name + '/' + f"{j + 1}.jpg", 'wb') as f:
                f.write(pic_response.content)


# urllib.request.urlretrieve(url="https://w.wallhaven.cc/full/p9/wallhaven-p9yl39.jpg", filename='test.jpg')
# craw(1)
if __name__ == '__main__':
    # craw(2)
    # pic_response = requests.get(url="https://w.wallhaven.cc/full/p9/wallhaven-p9yl39.jpg", headers=headers)
    # with open('test.jpg', 'wb') as f:
    #     f.write(pic_response.content)
    # thread1 = threading.Thread(name="thread1", target=craw, args=(1,))
    # thread2 = threading.Thread(name="thread2", target=craw, args=(2,))
    # thread3 = threading.Thread(name="thread3", target=craw, args=(3,))
    # thread4 = threading.Thread(name="thread4", target=craw, args=(4,))
    # thread5 = threading.Thread(name="thread5", target=craw, args=(5,))
    # thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()
    # thread5.start()
    craw_page(2)
