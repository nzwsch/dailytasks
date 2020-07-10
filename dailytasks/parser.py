from bs4 import BeautifulSoup

DATEARG_PATTERN = r"^(20\d{2})(0?[1-9]|1[0-2])(0[1-9]|[12]\d|30|31)$"


def get_og_title(text):
    soup = BeautifulSoup(text, 'html5lib')
    og_title = soup.select_one('meta[property="og:title"]')
    return og_title['content']


def get_headline_links(text):
    soup = BeautifulSoup(text, 'html5lib')
    links = soup.select('.content > section > div > h2 > a[href]')
    return [link['href'] for link in links]


def get_categories(text):
    soup = BeautifulSoup(text, 'html5lib')
    prefaces = soup.select('#article p.preface')

    categories = {}
    category = None

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

    text = ""
    with open("html/20200706-headline.html") as f:
        text = f.read()
    cats = get_categories(text)

    with open("json/result.json", "w") as f:
        f.write(json.dumps(cats, ensure_ascii=False, indent=4))
