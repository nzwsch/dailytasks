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
    category_color = '2674689'

    isyokuju = cats.get(category)
    print(len(isyokuju))

    embeds = []

    for item in isyokuju:
        text = item['text']
        href = item['href']

        res = requests.get(href)
        print(res.status_code, href)

        result = embed.parse(res.text)

        embeded = webhook.to_embed(title=text,
                                   url=href,
                                   category=category,
                                   color=category_color,
                                   author=result.get('author'),
                                   image=result.get('image'),
                                   icon=result.get('icon'),
                                   description=result.get('description'))

        embeds.append(embeded)

    with open("result-isyokuju.json", "w") as f:
        f.write(json.dumps(embeds, ensure_ascii=False, indent=4))

    webhook.post_link('2020年7月6日のヘッドラインニュース', embeds)
