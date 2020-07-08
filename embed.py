from bs4 import BeautifulSoup

max_len = 60


def get_author(soup):
    ogrp_author = soup.select_one('meta[property="og:article:author" i]')
    ogsite_name = soup.select_one('meta[property="og:site_name" i]')
    twtr_author = soup.select_one('meta[name="twitter:creator" i]')
    meta_author = soup.select_one('meta[name="author" i]')

    return (ogrp_author and ogrp_author.get('content') or
            ogsite_name and ogsite_name.get('content') or
            meta_author and meta_author.get('content') or
            twtr_author and twtr_author.get('content'))


def get_image(soup):
    ogrp_image = soup.select_one('meta[property="og:image" i]')
    twtr_image = soup.select_one('meta[name="twitter:image" i]')
    meta_image = soup.select_one('link[rel="image_src" i]')

    return (ogrp_image and ogrp_image.get('content') or
            twtr_image and twtr_image.get('content') or
            meta_image and meta_image.get('href'))


def get_icon(soup):
    touch_icon = soup.select_one('link[rel="apple-touch-icon" i]')
    shortcut = soup.select_one('link[rel="shortcut icon" i]')
    icon = soup.select_one('link[rel="icon" i]')

    return (touch_icon and touch_icon.get('href') or
            shortcut and shortcut.get('href') or
            icon and icon.get('href'))


def get_description(soup):
    ogrp_desc = soup.select_one('meta[property="og:description" i]')
    twtr_desc = soup.select_one('meta[property="twitter:description" i]')
    meta_desc = soup.select_one('meta[name="description" i]')

    description = (ogrp_desc and ogrp_desc.get('content') or
                   twtr_desc and twtr_desc.get('content') or
                   meta_desc and meta_desc.get('content'))

    if len(description) > max_len:
        return '{}...'.format(description[0:max_len-1])
    else:
        return description


def parse(text):
    soup = BeautifulSoup(text, 'html5lib')

    author = get_author(soup)
    image = get_image(soup)
    icon = get_icon(soup)
    description = get_description(soup)

    return {'author': author,
            'image': image,
            'icon': icon,
            'description': description}


if __name__ == "__main__":
    import json

    with open("html/covid-health-transmit-scientists-idJPKBN24705X.html") as f:
        text = f.read()
        result = parse(text)

    with open("result-idJPKBN24705X.json", "w") as f:
        f.write(json.dumps(result, ensure_ascii=False, indent=4))

    with open("html/000981.html") as f:
        text = f.read()
        result = parse(text)

    with open("result-000981.json", "w") as f:
        f.write(json.dumps(result, ensure_ascii=False, indent=4))
