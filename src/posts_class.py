from asyncio import constants
import os
import yaml
import markdown
from urllib.parse import quote
from transliterate import translit
import re
import locale
from datetime import datetime

import src.text_util as text_util
import src.list_util as list_util
import src.file_util as file_util

class posts_class:
    # Initialization method (constructor)
    def __init__(self, config):
        self.posts_config = config
        self.posts_files_list = []
        self.posts_content = []
        self.posts_content_cfg = []
        self.posts_content_text = []
        self.posts_content_html = []
        self.posts_content_short_html = []
        self.posts_content_dir_name = []
        self.posts_content_tags_url = []
        self.posts_content_tags_text = []

    def find_posts_id_by_tag_url(self, tag_url):
        posts_id = []
        for i in range(len(self.posts_files_list)):
            if tag_url in self.posts_content_cfg[i]['tags_url']:
                posts_id.append(i)
        return posts_id

 

