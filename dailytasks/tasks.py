from __future__ import absolute_import, unicode_literals

from dailytasks.celery import app

import requests
from pathlib import Path
from re import match
import json
import os
import random
import urllib.parse

from dailytasks import embed
from dailytasks import parser
from dailytasks import webhook

category_list = [{'color': '#ff0094', 'name': 'ネタ（メモ・その他いろいろ）'},
                 {'color': '#002aff', 'name': 'ライフスタイル（人生・生活・健康）'},
                 {'color': '#ffa200', 'name': 'IT・ガジェット（ネット・ソフト・ハード・モバイル）'},
                 {'color': '#aa00ff', 'name': 'サイエンス（科学・学問・テクノロジー）'}]


def get_result_json(datearg):
    root_dir = Path(__file__).parent.parent.absolute()
    return root_dir.joinpath("json", "result-{}.json".format(datearg))


def get_embed_items(category, cateogry_items):
    # TODO: use logging
    print(len(cateogry_items), category['name'])

    embed_items = []

    for item in cateogry_items:
        text = item['text']
        href = item['href']
        category_name = 'カテゴリ◆{}'.format(category['name'])
        color = category['color']

        # GET request
        r = requests.get(href)

        # TODO: use logging
        print(r.status_code, href)

        result = embed.parse(r.content)
        embed_item = webhook.to_embed(title=text,
                                      url=href,
                                      category=category_name,
                                      color=color,
                                      author=result.get('author'),
                                      image=result.get('image'),
                                      description=result.get('description'))

        embed_items.append(embed_item)

    return embed_items


@app.task
def add(url):
    r = requests.get(url)

    og_title = parser.get_og_title(r.content)
    categories = parser.get_categories(r.content)

    embeds = []

    for key in categories.keys():
        if key in [c['name'] for c in category_list]:
            print(key)
            category = next(c for c in category_list if c['name'] == key)
            cateogry_items = categories[key]
            embed_items = get_embed_items(category, cateogry_items)
            for embed_item in embed_items:
                embeds.append(embed_item)

    # shuffle
    random.shuffle(embeds)

    # TODO: fix json path
    with open("json/result.json", "w") as f:
        f.write(json.dumps(embeds, ensure_ascii=False, indent=4))

    # webhook
    status_codes = webhook.post_all(og_title, embeds)

    return status_codes


@app.task
def ping(datearg):
    if not match(parser.valid_datearg_pattern, datearg):
        raise ValueError("datearg is not valid: {}".format(datearg))

    result_json_path = get_result_json(datearg)

    if os.path.exists(result_json_path):
        return None

    # カテゴリ: ヘッドライン
    r = requests.get("https://gigazine.net/news/C19/")

    if r.status_code >= 300:
        # TODO: use logging
        print(r.text)
        return r.status_code

    # parse links
    headline_today = 'https://gigazine.net/news/{}-headline/'.format(datearg)
    headline_links = parser.get_headline_links(r.content)

    if not headline_today in headline_links:
        # TODO: use logging
        print(json.dumps(headline_links, ensure_ascii=False, indent=4))
        return 'not found {} in headline_links'.format(headline_today)

    # save links to json
    with open(result_json_path, "w") as f:
        headline_result = {"headline_today": headline_today,
                           "headline_links": headline_links}
        f.write(json.dumps(headline_result, ensure_ascii=False, indent=4))

    return "PONG: {}".format(datearg)
