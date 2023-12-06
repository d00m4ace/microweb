---
title: Highlighting specific lines
date: 2022-04-01
categories:
project_url: https://github.com/gohugoio/hugo
tags:
---
# Hello World

This is a text in **Markdown**!

- It has lists
- It has **bold text**
- It has *italic text*
- And more...

[Link to Google](https://www.google.com)

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

<<*>>

https://hub.docker.com/r/squidfunk/mkdocs-material/

``` c
extern size_t
pb_varint_scan(const uint8_t data[], size_t left) {
  assert(data && left);
  left = left > 10 ? 10 : left;

#ifdef __SSE2__

  /* Mapping: remaining bytes ==> bitmask */
  static const int mask_map[] = {
    0x0000, 0x0001, 0x0003, 0x0007,
    0x000F, 0x001F, 0x003F, 0x007F,
    0x00FF, 0x01FF, 0x03FF
  };

  /* Load buffer into 128-bit integer and create high-bit mask */
  __m128i temp = _mm_loadu_si128((const __m128i *)data);
  __m128i high = _mm_set1_epi8(0x80);

  /* Intersect and extract mask with high-bits set */
  int mask = _mm_movemask_epi8(_mm_and_si128(temp, high));
  mask = (mask & mask_map[left]) ^ mask_map[left];

  /* Count trailing zeroes */
  return mask ? __builtin_ctz(mask) + 1 : 0;

#else

  /* Linear scan */
  size_t size = 0;
  while (data[size++] & 0x80)
    if (!--left)
      return 0;
  return size;

#endif /* __SSE2__ */

}
```


Docker example here:


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