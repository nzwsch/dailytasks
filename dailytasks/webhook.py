from os import environ
import requests
import time
import urllib.parse

per_seconds = 2  # per two seconds
webhook_url = environ.get('WEBHOOK_URL')


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


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
        # TODO: use logging
        print(r.status_code, r.text)

    return r.status_code


def post_all(og_title, embeds):
    status_codes = []
    iterate = 1
    embeded_partition = list(chunks(embeds, 10))

    for embeded_part in embeded_partition:
        title = '{} ({}/{})'.format(og_title, iterate, len(embeded_partition))
        status_code = post_link(title, embeded_part)
        time.sleep(per_seconds)
        iterate += 1
        status_codes.append(status_code)

    return status_codes
