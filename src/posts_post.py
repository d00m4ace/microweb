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

import src.posts_tags as posts_tags


# html_template = posts.posts_config['html_templates_content']['post_header']
# html_template = posts.posts_config['html_templates_content']['post_header_list']
# post_link = posts.posts_config['posts_url'] + '/' + posts.posts_content_dir_name[i] + '/'
def posts_html_header(html_template, post_link, posts, i):
    html = html_template

    html = html.replace(
        "{{title}}", posts.posts_content_cfg[i]['title'])

    post_date_ru = text_util.gen_date_ru(posts.posts_content_cfg[i]['date'])

    html = html.replace(
        "{{post_link}}", post_link)

    html = html.replace(
        "{{post_date}}", post_date_ru)

    if 'update' in posts.posts_content_cfg[i]:
        html = text_util.text_repleace(
            html, ["<!--post_update", "post_update-->"], "")
        html = html.replace(
            "{{post_update}}", text_util.gen_date_ru(posts.posts_content_cfg[i]['update']))

    html = html.replace(
        "{{words_count}}", text_util.count_words(posts.posts_content_text[i]))

    html = html.replace(
        "{{reading_time}}", text_util.reading_time(posts.posts_content_text[i]))

    html = html.replace(
        "{{post_id}}", str(i+1))

    return html


def posts_html_list(posts, html_base, output_html_list_path, posts_id, html_in):
    if not os.path.exists(output_html_list_path):
        os.makedirs(output_html_list_path)

    html_base = html_base.replace(
        "{{title}}", posts.posts_config['posts_cloud_title'])

    html_list = html_in

    for i in posts_id:
        post_html_path_dir = text_util.path_join(
            posts.posts_config['posts_url'], posts.posts_content_dir_name[i])

        post_html_template = posts.posts_config['html_templates_content']['post_header_list']
        post_link = posts.posts_config['posts_url'] + \
            '/' + posts.posts_content_dir_name[i] + '/'
        html_content = posts_html_header(
            post_html_template, post_link, posts, i)

        html_tags = posts.posts_config['html_templates_content']['post_tags_block']

        html_tags_list = posts_tags.tags_html_block(
            posts,
            posts.posts_content_cfg[i]['tags'],
            posts.posts_content_cfg[i]['tags_url'], '')

        if html_tags_list == "":
            html_tags = ""

        if posts.posts_config['posts_tags_build'] == False:
            html_tags = ""

        html_tags = html_tags.replace('{{tags}}', html_tags_list)

        html_content += html_tags

        html_content += posts.posts_content_short_html[i]

        html_content += posts.posts_config['html_read_more'].replace(
        "{{post_link}}", post_link)

        html_list += html_content

    html_base = html_base.replace(
        "{{content}}", html_list)

    file_util.write_file(text_util.path_join(
        output_html_list_path, 'index.html'), html_base)


def posts_html_list_with_paginate(posts, html_base, html_base_title, output_html_path, pages_url, posts_id, html_in):
    items_per_page = int(posts.posts_config['paginate_items_per_page'])

    pages = list_util.paginate_list(posts_id, items_per_page)

    for p in range(len(pages)):
        # print(pages[p])
        html_pages = ""

        output_html_path_page_p = output_html_path + ''
        if p > 0:
            output_html_path_page_p += '/page' + str(p+1)

        for c in range(len(pages)):
            output_html_path_page = output_html_path + ''
            page_url = pages_url + ''
            if c > 0:
                output_html_path_page += '/page' + str(c+1)
                page_url += '/page' + str(c+1)

            pages_link_html = ""

            if p == c:
                pages_link_html = posts.posts_config['html_templates_content']['page_link_mark'].replace(
                    '{{page_link}}', page_url)
            else:
                pages_link_html = posts.posts_config['html_templates_content']['page_link'].replace(
                    '{{page_link}}', page_url)

            pages_link_html = pages_link_html.replace('{{page}}', str(c+1))
            html_pages += pages_link_html

        html_pages = posts.posts_config['html_templates_content']['pages_block'].replace(
            '{{pages}}', html_pages)

        html = html_base.replace(
            "{{title}}", html_base_title + ' - ' + str(p+1))

        if len(pages) > 1:
            html = html.replace(
                "{{bottom}}", html_pages)
        else:
            html = html.replace(
                "{{bottom}}", '')

        html = html.replace(
            "{{top}}", '')

        posts_html_list(posts,
                        html,
                        output_html_path_page_p,
                        pages[p], html_in)
