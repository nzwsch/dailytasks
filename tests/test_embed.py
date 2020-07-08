from bs4 import BeautifulSoup
from dailytasks.embed import get_author


def make_soup(text):
    return BeautifulSoup(text, "html5lib")


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
