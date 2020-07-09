import requests
from os import path
import time
from urllib.parse import urlparse

headline_link_selector = '.content > section > div > h2 > a'

test_txt = """
https://gigazine.net/news/20200706-headline/
https://gigazine.net/news/20200703-headline/
https://gigazine.net/news/20200702-headline/
https://gigazine.net/news/20200701-headline/
https://gigazine.net/news/20200630-headline/
https://gigazine.net/news/20200629-headline/
https://gigazine.net/news/20200626-headline/
https://gigazine.net/news/20200625-headline/
https://gigazine.net/news/20200624-headline/
https://gigazine.net/news/20200623-headline/
https://gigazine.net/news/20200622-headline/
https://gigazine.net/news/20200619-headline/
https://gigazine.net/news/20200618-headline/
https://gigazine.net/news/20200617-headline/
https://gigazine.net/news/20200616-headline/
https://gigazine.net/news/20200615-headline/
https://gigazine.net/news/20200612-headline/
https://gigazine.net/news/20200611-headline/
https://gigazine.net/news/20200610-headline/
https://gigazine.net/news/20200609-headline/
https://gigazine.net/news/20200608-headline/
https://gigazine.net/news/20200605-headline/
https://gigazine.net/news/20200604-headline/
https://gigazine.net/news/20200603-headline/
https://gigazine.net/news/20200602-headline/
https://gigazine.net/news/20200601-headline/
https://gigazine.net/news/20200529-headline/
https://gigazine.net/news/20200528-headline/
https://gigazine.net/news/20200527-headline/
https://gigazine.net/news/20200526-headline/
https://gigazine.net/news/20200525-headline/
https://gigazine.net/news/20200522-headline/
https://gigazine.net/news/20200521-headline/
https://gigazine.net/news/20200520-headline/
https://gigazine.net/news/20200519-headline/
https://gigazine.net/news/20200518-headline/
https://gigazine.net/news/20200515-headline/
https://gigazine.net/news/20200514-headline/
https://gigazine.net/news/20200513-headline/
https://gigazine.net/news/20200512-headline/
"""

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
