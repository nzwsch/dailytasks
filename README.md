# dailytasks

It runs a small scraping script which collect links from [Gigazine's][gigazine]
headline and post them for [Discord][discord] on every weekday.

![Preview](https://i.gyazo.com/b7a29ceea84aebfe0f5ecdaf6b16ace2.png)

## Setup

Before use this program you need to create [webhook at discord][webhook].

    git clone https://github.com/nzwsch/dailytasks && cd dailytasks
    echo WEBHOOK_URL=https://discordapp.com/api/webhooks/{webhook.id}/{webhook.token} > .env
    docker-compose up --build # BOOM

## Testing

We use [pytest](https://pypi.org/project/pytest/) for testing.

    pip install -U pytest
    pytest

## License

This project is licensed under the terms of the **MIT** license.

[gigazine]: https://gigazine.net
[discord]:  https://discord.com
[webhook]:  https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks
