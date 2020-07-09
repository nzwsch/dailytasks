from bs4 import BeautifulSoup
from dailytasks.embed import get_author, summarize, parse


def make_soup(text):
    return BeautifulSoup(text, "html5lib")


def test_summarize_return_none():
    assert summarize(None) == None


def test_summarize_return_short_text():
    long_text = "abcdefghij" * 6
    assert summarize("short text") == "short text"


def test_summarize_return_long_text_to_not_summarized():
    long_text = "abcdefghij" * 6
    assert summarize(long_text, 60) == long_text


def test_summarize_return_long_text_to_summarized():
    long_text = "abcdefghij" * 6
    assert summarize(long_text + "k", 60) == long_text + "..."


def test_get_author_by_opengraph_author():
    soup = make_soup("""
    <head>
        <meta property="og:article:author" content="Batman">
        <meta property="og:site_name" content="Robin">
        <meta name="Author" content="Batgirl">
        <meta name="twitter:creator" content="Joker">
    </head>
    """)
    assert get_author(soup) == "Batman"


def test_get_author_by_site_name():
    soup = make_soup("""
    <head>
        <meta property="og:site_name" content="Robin">
        <meta name="Author" content="Batgirl">
        <meta name="twitter:creator" content="Joker">
    </head>
    """)
    assert get_author(soup) == "Robin"


def test_get_author_by_twitter():
    soup = make_soup("""
    <head>
        <meta name="Author" content="Batgirl">
        <meta name="twitter:creator" content="Joker">
    </head>
    """)
    assert get_author(soup) == "Batgirl"


def test_get_author_by_meta():
    soup = make_soup("""
    <head>
        <meta name="twitter:creator" content="Joker">
    </head>
    """)
    assert get_author(soup) == "Joker"


def test_parse_with_none():
    text = """
    <head></head>
    """
    assert parse(text) == {"author": None,
                           "image": None,
                           "icon": None,
                           "description": None}
