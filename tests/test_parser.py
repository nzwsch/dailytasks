from re import match
from pathlib import Path

from dailytasks.parser import get_og_title, get_headline_links, get_categories, DATEARG_PATTERN


def read_html(filename):
    filepath = Path(__file__).parent.parent.absolute()
    with open(filepath.joinpath('html', filename)) as f:
        text = f.read()
    return text


def test_DATEARG_PATTERN():
    assert match(DATEARG_PATTERN, "20200709")


def test_not_DATEARG_PATTERN():
    assert not match(DATEARG_PATTERN, "12345678")


def test_get_og_title():
    text = """
    <head>
        <meta property="og:title" content="2020年7月6日のヘッドラインニュース" />
    </head>
    """
    assert get_og_title(text) == "2020年7月6日のヘッドラインニュース"


def test_get_headline_links_includes_20200708():
    text = read_html('c19-20200709.html')
    headline_link = 'https://gigazine.net/news/20200708-headline/'
    assert headline_link in get_headline_links(text)


def test_get_headline_links_does_not_include_20200709():
    text = read_html('c19-20200709.html')
    headline_link = 'https://gigazine.net/news/20200709-headline/'
    assert not headline_link in get_headline_links(text)


def test_get_categories_has_eight_keys():
    text = read_html('20200706-headline.html')
    assert len(get_categories(text).keys()) == 8
