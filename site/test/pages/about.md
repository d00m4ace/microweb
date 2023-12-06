---
title: Vegan experiment
date: 2022-04-01
update: 2023-05-31
categories:
project_url: https://github.com/gohugoio/hugo
tags: [Development, Go, fast, Blogging, nginx and python]
page_name: about
---
# about Hello World

<iframe width="560" height="315"
src="https://www.youtube.com/embed/XR5BMIYaxQ8" 
frameborder="0" 
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

This is a text in **Markdown**!

- It has lists
- It has **bold text**
- It has *italic text*
- And more...

<iframe width="640" height="480"
    src="https://www.youtube.com/embed/XR5BMIYaxQ8"
    frameborder="0"
    allow="autoplay; encrypted-media"
    allowfullscreen>
</iframe>

[Link to Google](https://www.google.com)

I tried to become a vegan today. I made it to lunch time and couldn't bear the 
sight of another green leaf. Yuck!

https://yakworks.github.io/docmark/extensions/codehilite/

<<*>>

```
# code block
print '3 backticks or'
print 'indent 4 spaces'
```

	:::python
	def hello_world():
		print("Hello, world!")

`Inline code` with backticks

	:::javascript 
	// I'm A tab
	console.log('Code Tab A');

next code:

	:::javascript
	// I'm tab B
	console.log('Code Tab B');

##This is a test

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


    :::python hl_lines="1 5"
    print("highlight me!")
    # but not me!
    for letter in "this is a test":
    print(letter)
    # I want to be highlighted, too!
	
here c++ code example
	
	:::c++
	#include <iostream>

	int main()
	{
		std::cout << "Hello, world!" << std::endl;
		return 0;
	}
	
and etc


``` python
""" Bubble sort """
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```


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