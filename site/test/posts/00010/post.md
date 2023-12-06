---
title: Code blocks must be indented by 4 whitespaces.
date: 2022-04-01
update: 2023-06-20
categories:
project_url: https://github.com/gohugoio/hugo
tags: [Development, Go, fast, Blogging]
---
Code blocks must be indented by 4 whitespaces.
Python-Markdown has a auto-guess function which works
pretty well:

    print("Hello, World")
    # some comment
    for letter in "this is a test":
        print(letter)

In cases where Python-Markdown has problems figuring out which
programming language we use, we can also add the language-tag
explicitly. One way to do this would be:


    :::python
    print("Hello, World")

or we can highlight certain lines to
draw the reader's attention:

Highlighting specific lines¶
Specific lines can be highlighted by passing the line numbers to the hl_lines argument placed right after the language identifier. Line counts start at 1.

Example:


``` python hl_lines="3 4"
""" Bubble sort """
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

https://hub.docker.com/r/squidfunk/mkdocs-material/

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