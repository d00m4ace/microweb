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

import src.posts_class as posts_class

import src.posts_post as posts_post
import src.posts_tags as posts_tags

break_token = '<<*>>'
short_content_len = 256*2

def generate_code_block(code):
    code_block = f'```\n{code}\n```'
    copy_button = '<button class="btn" data-clipboard-text="{0}">Copy</button>'.format(code)
    return f'{code_block}\n{copy_button}'

def gen_markdown(posts):
    for i in range(len(posts.posts_files_list)):

        post_txt = posts.posts_content_text[i].replace(break_token, '')
        content_short = ""

        if break_token in posts.posts_content_text[i]:
            content_short = posts.posts_content_text[i].split(break_token)[0]
        else:
            content_short = text_util.get_part(
            posts.posts_content_text[i]+ '\n\n', short_content_len)

        if len(content_short) < len(post_txt):
            content_short += '\n\n**...**'
        else:
            content_short = content_short

        post_txt += '\n\n***\n\n'

        posts.posts_content_html.append(
            text_util.gen_markdown(post_txt))

        posts.posts_content_short_html.append(
            text_util.gen_markdown(content_short))


def gen_html(posts):
    for i in range(len(posts.posts_files_list)):
        post_html_path_dir = text_util.path_join(
            posts.posts_config['output_html_path'], posts.posts_content_dir_name[i])

        if not os.path.exists(post_html_path_dir):
            os.makedirs(post_html_path_dir)

        html = posts.posts_config['html_templates_content']['base_html']
        html = html.replace(
            "{{title}}", posts.posts_content_cfg[i]['title'])

        html = html.replace(
            "{{description}}", f'<meta name="description" content="{posts.posts_content_cfg[i]["description"]}"/>')

        html_content = posts_post.posts_html_header(posts.posts_config['html_templates_content']['post_header'],
                                                    "", posts, i)

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

        html_content += posts.posts_content_html[i]

        nav_html = posts.posts_config['html_templates_content']['nav_prev_next_post']

        if i-1 >= 0:
            post_link = posts.posts_config['posts_url'] + \
                '/' + posts.posts_content_dir_name[i-1] + '/'
            nav_html = nav_html.replace('{{prev_url}}', post_link)

            nav_html = nav_html.replace(
                '{{title_prev_url}}', posts.posts_content_cfg[i-1]['title'])

            nav_html = text_util.text_repleace(
                nav_html, ["<!--prev_url", "prev_url-->"], "")

        if i+1 < len(posts.posts_files_list):
            post_link = posts.posts_config['posts_url'] + \
                '/' + posts.posts_content_dir_name[i+1] + '/'
            nav_html = nav_html.replace('{{next_url}}', post_link)

            nav_html = nav_html.replace(
                '{{title_next_url}}', posts.posts_content_cfg[i+1]['title'])

            nav_html = text_util.text_repleace(
                nav_html, ["<!--next_url", "next_url-->"], "")

        html_content += nav_html

        html = html.replace(
            "{{content}}", html_content)

        html = html.replace(
            "{{bottom}}", '')

        html = html.replace(
            "{{top}}", '')

        file_util.write_file(text_util.path_join(
            post_html_path_dir, 'index.html'), html)