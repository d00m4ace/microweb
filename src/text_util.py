from asyncio import constants
import os
import fnmatch
import yaml
import markdown
from urllib.parse import quote
from transliterate import translit
import re
from collections import Counter
from collections import defaultdict

from bs4 import BeautifulSoup

months_rod = ["", "января", "февраля", "марта", "апреля", "мая",
              "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
months_camel = ["", "Январь", "Февраль", "Март", "Апрель", "Май",
                "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
months_small = ["", "январь", "февраль", "март", "апрель", "май",
                "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

days_of_week = ['', 'Понедельник', 'Вторник', 'Среда',
                'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
days_of_week_small = ['', 'понедельник', 'вторник',
                      'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']


def gen_date_ru(dt):
    return f"{days_of_week_small[dt.weekday()+1]}, {dt.day} {months_rod[dt.month]} {dt.year} г."


def gen_markdown(content):

    content = content.replace(
        '>>youtube>>', '<div class="video-container"><iframe src="https://www.youtube.com/embed/')
    content = content.replace(
        '<<youtube<<', '"frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>')

    html = markdown.markdown(content, extensions=[
        'fenced_code', 'codehilite', 'tables'], output_format='html')

    soup = BeautifulSoup(html, "html.parser")

    for pre in soup.find_all('pre'):
        # Обернем блок кода и кнопку в общий div
        wrap = soup.new_tag('div')
        wrap['class'] = 'code-block'
        # Добавляем кнопку "Copy Code"
        copy_button = soup.new_tag("button")
        copy_button.string = "Copy Code"
        copy_button['class'] = 'copy-code-button'
        pre.wrap(wrap)
        pre.insert_before(copy_button)

    html = str(soup)

    return html


def translit_rus(rus_str):
# Convert rus_str to string if it's not
    if not isinstance(rus_str, str):
        rus_str = str(rus_str)    

    rus_str = rus_str.replace("+", "plus")
    #rus_str = rus_str.replace("#", "sharp")
    rus_str = rus_str.replace("#", "")
    rus_str = rus_str.replace(".", "dot")
    rus_str = rus_str.replace("!", "exclamation")
    rus_str = rus_str.replace("/", "slash")

    # Transliterate the Russian string to English
    english_str = translit(rus_str, 'ru', reversed=True)

    # Replace spaces with hyphens
    english_str = re.sub('[^a-zA-Z0-9 -]', '', english_str).lower()
    english_str = english_str.replace(" ", "-")
    # Convert the English string to a URL-encoded format
    url_str = quote(english_str)
    return url_str


def path_join(path1, path2):
    return os.path.join(path1, path2)


def read_config(content):
    config_text = ""
    config_lines_count = 0

    for i in range(len(content)):
        config_text += content[i]
        config_lines_count += 1
        if content[i].startswith('---'):
            if config_lines_count != 1:
                break

    config_text = config_text.split('---\n')

    if len(config_text) != 3:
        return None

    del content[:config_lines_count]

    # Parse the YAML config header
    config = yaml.safe_load(config_text[1])

    return config


def count_words(text):
    words = text.split()
    num_words = len(words)

    last_digit = num_words % 10
    last_two_digits = num_words % 100

    if last_digit == 1 and last_two_digits != 11:
        word_end = "слово"
    elif last_digit in [2, 3, 4] and last_two_digits not in [12, 13, 14]:
        word_end = "слова"
    else:
        word_end = "слов"

    return (f"{num_words} {word_end}")


def reading_time(text):
    words = text.split()
    num_words = len(words)

    words_per_minute = 100  # средняя скорость чтения

    reading_time_minutes = round(num_words / words_per_minute)

    if reading_time_minutes < 2:
        reading_time_minutes = 2
    else:
        reading_time_minutes += 1

    return (f'{reading_time_minutes} минут(ы)')


def text_repleace(txt, replace_list, replace_txt):
    for i in range(len(replace_list)):
        txt = txt.replace(replace_list[i], replace_txt)
    return txt


def get_part(text, length):
    # Ensure the length doesn't exceed the string's length
    length = min(len(text), length)

    # Slice the string to the maximum length
    part = text[:length]

    # Find the last occurrence of '\n' in the sliced string
    last_newline = part.rfind('\n')

    # If a newline was found, slice the string again to end at this newline
    if last_newline != -1:
        part = part[:last_newline]

    return part