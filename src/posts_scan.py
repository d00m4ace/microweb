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

# An instance method


def posts_scan(posts):
    # replace 'your_directory_path' with the path to the directory you want to scan
    posts.posts_files_list = file_util.scan_dir_subdirs(
        posts.posts_config['posts_dir_path'], "*.md")

    for i in range(len(posts.posts_files_list)):

        posts.posts_content.append(
            file_util.read_file_strs(posts.posts_files_list[i]))

        post_config = text_util.read_config(posts.posts_content[i])
        
        post_config['title'] = post_config['title'].replace('№', "#")

        if post_config is None:
            print("ERROR: Invalid config blok, not found 2 lines at start with '---' in " +
                  posts.posts_files_list[i])
            os.abort()

        if post_config['title'] is None:
            print("ERROR: title not set in " + posts.posts_files_list[i])
            os.abort()

        posts.posts_content_cfg.append(post_config)

        if 'page_name' not in posts.posts_content_cfg[i] or posts.posts_content_cfg[i]['page_name'] == None:
            posts.posts_content_dir_name.append(
                text_util.translit_rus(posts.posts_content_cfg[i]['title']))
        else:
            if posts.posts_content_cfg[i]['page_name'] == '/':
                posts.posts_content_dir_name.append('')
            else:
                posts.posts_content_dir_name.append(
                    text_util.translit_rus(posts.posts_content_cfg[i]['page_name']))

        posts.posts_content_text.append(''.join(posts.posts_content[i]))

        posts.posts_content_cfg[i]['tags_url'] = []

        if 'tags' in posts.posts_content_cfg[i] and posts.posts_content_cfg[i]['tags'] is not None:
            for tag in posts.posts_content_cfg[i]['tags']:

                tag_url = text_util.translit_rus(tag)

                posts.posts_content_cfg[i]['tags_url'].append(tag_url)

                if tag_url not in posts.posts_content_tags_url:
                    posts.posts_content_tags_url.append(tag_url)
                    posts.posts_content_tags_text.append(tag)

    dups = list_util.find_duplicates_with_id(posts.posts_content_dir_name)

    for item, indices in dups:
        indx = []
        for i in indices:
            #indx.append(i+1)
            indx.append(posts.posts_files_list[i])
        print(f"Duplicate post name: {item} {indx}")

    if len(dups) > 0:
        print("ERROR: Duplicate posts found!")
        os.abort()
