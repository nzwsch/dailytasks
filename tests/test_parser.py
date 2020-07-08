from pathlib import Path
from dailytasks.parser import get_categories


def open_headline(filename):
    filepath = Path(__file__).parent.parent.absolute()
    with open(filepath.joinpath('html', filename)) as f:
        text = f.read()
    return text


def test_get_categories_has_eight_keys():
    text = open_headline('20200706-headline.html')
    assert len(get_categories(text).keys()) == 8
