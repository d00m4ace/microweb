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
import src.list_util as list_util


def scan_dir_subdirs(directory, pattern='*'):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in fnmatch.filter(files, pattern):
            file_list.append(os.path.join(root, file))
    return file_list


def load_cfg(cfg_file_path):
    config = []
    with open(cfg_file_path, "r", encoding='utf8') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            os.abort()
    return config


def load_files(file_dict):
    files_content = dict()
    if type(file_dict) is dict:
        for key, value in file_dict.items():
            files_content[key] = read_file(value)
    else:
        print("ERROR: load_files need dict but recive: " + file_dict)
        os.abort()
    return files_content


def load_html_templates(config):
    cur_dir = os.getcwd()
    os.chdir(config['html_templates_dir'])
    config['html_templates_content'] = load_files(config['html_templates'])
    os.chdir(cur_dir)

def read_file_strs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return content


def write_file(file_path, txt):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(txt)


'''
if you want arbitrary prefixes/suffixes to identify your variables, you can simply use re.sub with a lambda expression:

from pathlib import Path
import re

def tpl(fn:Path, v:dict[str,str]) -> str:
	text = fn.with_suffix('.html').read_text()
	return re.sub("(<!-- (.+?) -->)", lambda m: v[m[2].lower()], text)

html = tpl(Path(__file__), {
	'title' : 't',
	'body' : 'b'
})
'''
