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

import src.text_util as text_util


def find_duplicates_with_id(lst):
    count = defaultdict(list)
    for i, item in enumerate(lst):
        count[item].append(i)
    return [(item, indices) for item, indices in count.items() if len(indices) > 1]


def find_duplicates(lst):
    count = Counter(lst)
    return [item for item in count if count[item] > 1]


def paginate_list(input_list, page_size):
    return [input_list[i:i+page_size] for i in range(0, len(input_list), page_size)]