# import requests
from os import path
import time
import urlparse

headline_link_selector = '.content > section > div > h2 > a'

# page = requests.get(url)

if __name__ == "__main__":
    with open('test.txt') as f:
        for line in f.readlines():
            url = line.rstrip()
            urlpath = urlparse.urlparse(url).path
            filename = '{}.html'.format(path.basename(path.abspath(urlpath)))
            dist = path.join('html', filename)
            time.sleep(2)
            with open(dist, 'w') as fw:
                fw.write("hello")
