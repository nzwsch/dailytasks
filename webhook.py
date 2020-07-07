import requests
from os import environ

webhook_url = environ.get('WEBHOOK_URL')


def post_link(title, embeds):
    r = requests.post(webhook_url, json={
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
            "author": {
                "name": "サイエンス（科学・学問・テクノロジー）"
            },
            "title": "コロナは空気感染もと科学者数百人、ＷＨＯに対策求める＝ＮＹＴ紙 - ロイター",
            "type": "link",
            "url": "https://jp.reuters.com/article/covid-health-transmit-scientists-idJPKBN24705X",
            "thumbnail": {
                "url": "https://s3.reutersmedia.net/resources/r/?m=02&d=20200706&t=2&i=1524718785&w=1200&r=LYNXMPEG65026",
            },
            "description": "世界保健機関（ＷＨＯ）に対し、科学者数百人が、新型コロナウイルスの空気感染の可能性を示す科学的根拠があると指摘し、対応策の推奨を改定するよう求めていることが分かった。米紙ニューヨーク・タイムズ（ＮＹＴ）が４日に報じた。"
        }
    ]
    post_link("2020年7月6日のヘッドラインニュース", embed_list)
