from bs4 import BeautifulSoup


def download_c19():
    """
    Not yet implemented.
    """
    # import requests
    # from os import path
    # import time
    # from urllib.parse import urlparse
    # headline_link_selector = '.content > section > div > h2 > a'
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


def get_categories(text):
    soup = BeautifulSoup(text, 'html5lib')
    prefaces = soup.select('#article p.preface')

    categories = {}
    category = None

    # print(len(prefaces))
    for preface in prefaces:
        big = preface.find('big')

        if big is not None:
            category = big.text.replace("◆", "")
            categories.setdefault(category, [])

        if category is not None:
            links = preface.find_all('a', href=True)
            for link in links:
                if link.parent.name == 'b':
                    categories[category].append({'text': link.text,
                                                 'href': link['href']})

    return categories


if __name__ == "__main__":
    import json
    from pprint import pprint

    text = ""
    with open("html/20200706-headline.html") as f:
        text = f.read()
    cats = get_categories(text)
    pprint(cats)

    with open("json/result.json", "w") as f:
        f.write(json.dumps(cats, ensure_ascii=False, indent=4))
