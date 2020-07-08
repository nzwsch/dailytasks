from bs4 import BeautifulSoup


def parse(text):
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

    text = ""
    with open("html/20200706-headline.html") as f:
        text = f.read()
    cats = parse(text)
    # print(cats)

    with open("result.json", "w") as f:
        f.write(json.dumps(cats, ensure_ascii=False, indent=4))
