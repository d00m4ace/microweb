import shutil
from asyncio import constants
import os
from pickle import TRUE
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
import src.posts_scan as posts_scan
import src.posts_gen as posts_gen
import src.posts_post as posts_post
import src.posts_tags as posts_tags


def posts_sort_by_date(posts, posts_id):
    id_date_dict = dict()

    for i in range(len(posts_id)):
        post_date = posts.posts_content_cfg[posts_id[i]]['date']

        if 'update' in posts.posts_content_cfg[posts_id[i]]:
            post_date = posts.posts_content_cfg[posts_id[i]]['update']

        id_date_dict[posts_id[i]] = post_date

    sorted_id_list = sorted(posts_id, key=id_date_dict.get, reverse=True)

    return sorted_id_list


def posts_list_build(posts):
    posts_id = []
    for i in range(len(posts.posts_files_list)):
        posts_id.append(i)
    posts_id.sort(reverse=True)

    sorted_id_list = posts_sort_by_date(posts, posts_id)

    posts_post.posts_html_list_with_paginate(posts,
                                             posts.posts_config['html_templates_content']['base_html'],
                                             posts.posts_config['posts_list_title'],
                                             posts.posts_config['output_html_path'],
                                             posts.posts_config['posts_url'],
                                             sorted_id_list, '')


def posts_tags_build(posts):
    for i in range(len(posts.posts_content_tags_url)):
        tag_url = posts.posts_content_tags_url[i]
        tag_text = posts.posts_content_tags_text[i]

        posts_id = posts.find_posts_id_by_tag_url(tag_url)
        posts_id.sort(reverse=True)

        sorted_id_list = posts_sort_by_date(posts, posts_id)

        html_tags = posts.posts_config['html_templates_content']['posts_tags_cloud']

        html_tags = html_tags.replace('{{title}}', 'Тег: '+tag_text)

        html_tags_list = posts_tags.tags_html_block(
            posts,
            posts.posts_content_tags_text,
            posts.posts_content_tags_url, tag_url)

        if html_tags_list == "":
            html_tags = ""

        if posts.posts_config['posts_tags_build'] == False:
            html_tags = ""

        html_tags = html_tags.replace('{{tags}}', html_tags_list)


        posts_post.posts_html_list_with_paginate(posts,
                                                 posts.posts_config['html_templates_content']['base_html'],
                                                 'Тег: '+tag_text,
                                                 posts.posts_config['output_html_path'] +
                                                 '/tags/' + tag_url,
                                                 posts.posts_config['posts_url'] +
                                                 '/tags/' + tag_url,
                                                 sorted_id_list, html_tags)


def posts_tags_cloud_build(posts):
    html_tags = posts.posts_config['html_templates_content']['posts_tags_cloud']
    
    html_tags = html_tags.replace(
        '{{title}}', posts.posts_config['posts_cloud_title'])

    html_tags_list = posts_tags.tags_html_block(
            posts,
            posts.posts_content_tags_text,
            posts.posts_content_tags_url, '')

    if html_tags_list == "":
        html_tags = ""

    html_tags = html_tags.replace('{{tags}}', html_tags_list)

    html = posts.posts_config['html_templates_content']['base_html']

    html = html.replace(
        "{{title}}", posts.posts_config['posts_cloud_title'])

    html = html.replace(
        "{{content}}", html_tags)

    html = html.replace(
        "{{bottom}}", '')

    html = html.replace(
        "{{top}}", '')

    dir_path = posts.posts_config['output_html_path'] + '/tags/'

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_util.write_file(
        dir_path + 'index.html', html)


def posts_build(config_file_path):
    config = file_util.load_cfg(config_file_path)

    file_util.load_html_templates(config)

    posts = posts_class.posts_class(config)

    posts_scan.posts_scan(posts)

    posts_gen.gen_markdown(posts)

    posts_gen.gen_html(posts)

    if 'file_copy' in posts.posts_config:
        # Loop over the pairs and copy each file
        # print(os.getcwd())
        for src in posts.posts_config['file_copy']:
            print(f"Copying {src} to {posts.posts_config['file_copy'][src]}")
            shutil.copyfile(src, posts.posts_config['file_copy'][src])

    return posts


def sitemap_build(sitemap_urls,posts):
    post_loc_base = posts.posts_config['site_full_url']
    
    if posts.posts_config['posts_url'] != "/":
     post_loc_base += posts.posts_config['posts_url'] + '/'
    else:
     post_loc_base += '/'    
        
    for i in range(len(posts.posts_content_cfg)):
     post_date = posts.posts_content_cfg[i]['date'].strftime("%Y-%m-%d")
     post_update = post_date
     if 'update' in posts.posts_content_cfg[i]:
            post_update = posts.posts_content_cfg[i]['update'].strftime("%Y-%m-%d")
     post_dir_name = posts.posts_content_dir_name[i]       
     
     post_loc = post_loc_base + post_dir_name
     
     if post_loc == posts.posts_config['site_full_url'] + '/':
         post_update = datetime.now().strftime("%Y-%m-%d")  
     
     sitemap_urls.insert(0,{"loc": post_loc, "lastmod": post_update})

     #print(f"{i} - {post_date} - {post_update} - {post_loc}")

def build(sitemap_urls,config_file_path):

    posts = posts_build(config_file_path)

    if posts.posts_config['posts_list_build']:
        posts_list_build(posts)

    if posts.posts_config['posts_tags_build']:
        posts_tags_build(posts)

    if posts.posts_config['posts_tags_cloud_build']:
        posts_tags_cloud_build(posts)
        
    sitemap_build(sitemap_urls,posts)     

    return posts
