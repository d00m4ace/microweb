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

import src.posts_post as posts_post

def tags_html_block(posts, posts_tags, posts_tags_url, selected_tag_url):
    if posts_tags is None or len(posts_tags) == 0:
        return ""

    html_tags = ""

    for j in range(len(posts_tags)):
        tag = posts_tags[j]
        tags_url = posts_tags_url[j]
        
        if not isinstance(tag, str):
            tag = str(tag)    

        html_tag = ""

        if selected_tag_url == tags_url:
            html_tag = posts.posts_config['html_templates_content']['posts_tag_mark']
        else:
            html_tag = posts.posts_config['html_templates_content']['posts_tag']

        html_tag = html_tag.replace("{{tag_name}}", tag)
        html_tag = html_tag.replace(
            "{{tag_link}}", f"{posts.posts_config['posts_url']}/tags/{tags_url}/")
        html_tags += html_tag

    return html_tags
