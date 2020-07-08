import requests
import webhook
import embed
import gigazine
import json

if __name__ == "__main__":
    # send discord
    text = ""
    with open("html/20200706-headline.html") as f:
        text = f.read()
    cats = gigazine.parse(text)

    category = '新商品（衣・食・住）'
    category_color = '#28d001'

    isyokuju = cats.get(category)
    print(len(isyokuju))

    embeds = []

    for item in isyokuju:
        text = item['text']
        href = item['href']

        r = requests.get(href)
        print(r.status_code, href)

        result = embed.parse(r.content)

        embeded = webhook.to_embed(title=text,
                                   url=href,
                                   category='カテゴリ◆{}'.format(category),
                                   color=category_color,
                                   author=result.get('author'),
                                   image=result.get('image'),
                                   description=result.get('description'))

        embeds.append(embeded)

    with open("result-isyokuju.json", "w") as f:
        f.write(json.dumps(embeds, ensure_ascii=False, indent=4))

    webhook.post_link('2020年7月6日のヘッドラインニュース', embeds)
