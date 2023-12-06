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

import time

import json
from bs4 import BeautifulSoup

# html_dir directory containing your HTML files
def build(html_dir, root_filter):

    # List to store data for each page
    pages_data = []

    # Iterate over each file in the directory
    # for filename in os.listdir(html_dir):
    #    if not filename.endswith('.html'):
    #        continue

    cur_dir = os.getcwd()
    os.chdir(html_dir)

    for root, dirs, files in os.walk('.'):
        for file in fnmatch.filter(files, '*.html'):

            if root_filter(root) == False:
                continue

            filepath = os.path.join(root, file)

            # Parse the HTML file with Beautiful Soup
            with open(filepath, 'r', encoding='utf8') as f:
                # , from_encoding='utf8'
                soup = BeautifulSoup(f.read(), 'html.parser')

                # print(soup.prettify("utf8").encode('utf-8'))

            # Extract the title and text of the page
            title = soup.title.string if soup.title else ''
            body = ' '.join(soup.stripped_strings)

            # print(title)
            # print(body)

            filepath = filepath.replace('index.html', '')
            filepath = filepath.replace('.\\', '/')

            # Append this data to the list
            pages_data.append({
                'title': title,
                'body': body,
                'url': filepath,
            })

            # print(pages_data)

    # Write the data to a JSON file
    with open('search_index.json', 'w', encoding='utf8') as f:
        json.dump(pages_data, f, ensure_ascii=False)

    os.chdir(cur_dir)