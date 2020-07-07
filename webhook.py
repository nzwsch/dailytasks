import requests
from os import environ

webhook_url = environ.get('WEBHOOK_URL')


def post_link(title, embeds):
    r = requests.post(webhook_url, json={
        "content": title,
        "embeds": embeds
    })
    print(r.status_code)


if __name__ == "__main__":
    embed_list = [
        {
            "title": "コロナは空気感染もと科学者数百人、ＷＨＯに対策求める＝ＮＹＴ紙 - ロイター",
            "type": "link",
            "url": "https://jp.reuters.com/article/covid-health-transmit-scientists-idJPKBN24705X"
        }
    ]
    post_link("サイエンス（科学・学問・テクノロジー）", embed_list)
