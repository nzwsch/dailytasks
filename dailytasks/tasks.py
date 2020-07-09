from __future__ import absolute_import, unicode_literals

from dailytasks.celery import app

import requests
import json
import random

from dailytasks import embed
from dailytasks import parser
from dailytasks import webhook

category_list = [{'color': '#ff0094', 'name': 'ネタ（メモ・その他いろいろ）'},
                 {'color': '#002aff', 'name': 'ライフスタイル（人生・生活・健康）'},
                 {'color': '#ffa200', 'name': 'IT・ガジェット（ネット・ソフト・ハード・モバイル）'},
                 {'color': '#aa00ff', 'name': 'サイエンス（科学・学問・テクノロジー）'}]


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
    return "PONG: {}".format(datearg)
