from pathlib import Path
import os
import urllib.parse

from dailytasks.tasks import get_result_json, get_blacklist


def test_get_result_json_returns_expected_path():
    expected_path = Path(__file__).parent.parent.joinpath('json',
                                                          'result-20200710.json')
    assert get_result_json('20200710') == expected_path


def test_get_result_json_returns_readable_and_writable_dir():
    expected_dir = Path(__file__).parent.parent.joinpath('json')
    assert os.access(expected_dir, os.R_OK | os.W_OK)


def test_blacklisted_url():
    blacklist = get_blacklist()
    input_text = """
        https://www.asahi.com/articles/ASN7K40XDN78ULFA02H.html
        https://www.asahi.com/articles/ASN7N35C5N7JUTIL04N.html
        https://www.nikkei.com/article/DGXMZO61695680Y0A710C2EA1000/
        https://www3.nhk.or.jp/news/html/20200719/k10012522851000.html
        https://comemo.nikkei.com/n/n1c9103c81c79
    """
    input_list = [l.strip() for l in input_text.strip().splitlines() if l]
    clean_list = [l for l in input_list if
                  not urllib.parse.urlparse(l).netloc in blacklist]
    assert clean_list == []
