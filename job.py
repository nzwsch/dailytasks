import requests
import webhook
import embed
import gigazine
import json
import random
import time


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == "__main__":
    # send discord
    text = ""
    with open("html/20200706-headline.html") as f:
        text = f.read()
    cats = gigazine.parse(text)

    categories = [{'name': 'ネタ（メモ・その他いろいろ）', 'color': '#ff0094'},
                  {'name': 'ライフスタイル（人生・生活・健康）', 'color': '#002aff'},
                  {'name': 'IT・ガジェット（ネット・ソフト・ハード・モバイル）', 'color': '#ffa200'},
                  {'name': 'サイエンス（科学・学問・テクノロジー）', 'color': '#aa00ff'}]

    embeds = []

    for category in categories:
        items = cats.get(category['name'])

        print(len(items), category['name'])

        for item in items:
            text = item['text']
            href = item['href']
            category_name = 'カテゴリ◆{}'.format(category['name'])
            color = category['color']

            r = requests.get(href)
            print(r.status_code, href)

            result = embed.parse(r.content)

            embeded = webhook.to_embed(title=text,
                                       url=href,
                                       category=category_name,
                                       color=color,
                                       author=result.get('author'),
                                       image=result.get('image'),
                                       description=result.get('description'))

            embeds.append(embeded)

    random.shuffle(embeds)

    with open("json/result.json", "w") as f:
        f.write(json.dumps(embeds, ensure_ascii=False, indent=4))

    iterate = 1
    embeded_partition = list(chunks(embeds, 10))
    for embed_list in embeded_partition:
        title = '2020年7月6日のヘッドラインニュース ({}/{})'.format(iterate,
                                                      len(embeded_partition))
        webhook.post_link(title, embed_list)
        time.sleep(1)
        iterate += 1
