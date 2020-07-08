import requests
import urllib.parse
from os import environ

webhook_url = environ.get('WEBHOOK_URL')


def to_embed(title=None, url=None, category=None, color=None, author=None, image=None, description=None):
    embed = {"type": "link"}

    if title:
        embed['title'] = title
    if url:
        embed['url'] = url
    if category:
        embed['footer'] = {"text": category}
    if color:
        embed['color'] = int(color.replace('#', '0x'), 16)
    if author:
        embed['author'] = {"name": author}
    if image:
        embed['thumbnail'] = {"url": urllib.parse.urljoin(url, image)}
    if description:
        embed['description'] = description

    return embed


def post_link(title, embeds):
    r = requests.post("{}?wait=true".format(webhook_url), json={
        "content": title,
        "embeds": embeds
    })
    if r.status_code >= 300:
        print(r.status_code, r.text)
    else:
        print(r.status_code)


if __name__ == "__main__":
    embed_list = [
        {
            "type": "link",
            "title": "「ハーゲンダッツ『ジャポネ きなこのティラミス』」2020年7月14日｜ハーゲンダッツ ジャパン",
            "url": "https://www.haagen-dazs.co.jp/company/newsrelease/2020/_0706_2.html",
            "footer": {
                "icon_url": "https://gigazine.net/apple-touch-icon.png",
                "text": "新商品（衣・食・住）"
            },
            "color": "#28d001",
            "thumbnail": {
                "url": "https://www.haagen-dazs.co.jp/common/img/og_top_news.jpg"
            },
            "description": "ハーゲンダッツ（Häagen-Dazs）の「ハーゲンダッツ『ジャポネ きなこのティラミス』」が発売になります！是非、アイスクリームのラインナップをチェックして、ハーゲンダッツの世界をお楽しみください。"
        }
    ]
    post_link("2020年7月6日のヘッドラインニュース", json.loads(embed_list))
