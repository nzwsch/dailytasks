import requests
from os import path
import time
from urllib.parse import urlparse

headline_link_selector = '.content > section > div > h2 > a'

if __name__ == "__main__":
    with open('test.txt') as f:
        for line in f.readlines():
            url = line.rstrip()
            urlpath = urlparse(url).path
            filename = '{}.html'.format(path.basename(path.abspath(urlpath)))
            dist = path.join('html', filename)
            page = requests.get(url)
            print(page.status_code, url)
            time.sleep(2)
            with open(dist, 'w') as fw:
                fw.write(page.text)
