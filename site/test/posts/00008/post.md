---
title: This is a text in **Markdown**!
description: 'Обзор проектов D00M4ACE: MMORPG, генераторы сайтов и настольные игры.'
date: 2022-04-01
categories:
project_url: https://github.com/gohugoio/hugo
tags: [Markdown]
---
# Hello World

This is a text in **Markdown**!

- It has lists
- It has **bold text**
- It has *italic text*
- And more...

[Link to Google](https://www.google.com)

I tried to become a vegan today. I made it to lunch time and couldn't bear the 
sight of another green leaf. Yuck!

https://yakworks.github.io/docmark/extensions/codehilite/

``` Docker
FROM ubuntu

# Install vnc, xvfb in order to create a 'fake' display and firefox
RUN apt-get update && apt-get install -y x11vnc xvfb firefox
RUN mkdir ~/.vnc

# Setup a password
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd

# Autostart firefox (might not be the best way, but it does the trick)
RUN bash -c 'echo "firefox" >> /.bashrc'

EXPOSE 5900
CMD ["x11vnc", "-forever", "-usepw", "-create"]
```

- Japan
* Tokyo
* Osaka
* Nagoya
- France
* Paris
* Marseille
* Lyon
- Germany
* Berlin
* Hamburg
* Munich

- Flour
- Cheese
- Tomatoes

Four steps to better sleep:

1. Stick to a sleep schedule
2. Create a bedtime ritual
3. Get comfortable
4. Manage stress

***