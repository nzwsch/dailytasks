from pathlib import Path
import os

from dailytasks.tasks import get_result_json


def test_get_result_json_returns_expected_path():
    expected_path = Path(__file__).parent.parent.joinpath('json',
                                                          'result-20200710.json')
    assert get_result_json('20200710') == expected_path


def test_get_result_json_returns_writable_dir():
    writable_dir = Path(__file__).parent.parent.joinpath('json')
    assert os.access(writable_dir, os.W_OK)
