import os
import fnmatch
import json
from bs4 import BeautifulSoup
import zipfile

def build(html_dir, root_filter):
    pages_data = []
    cur_dir = os.getcwd()
    os.chdir(html_dir)

    for root, dirs, files in os.walk('.'):
        for file in fnmatch.filter(files, '*.html'):
            if root_filter(root) == False:
                continue

            filepath = os.path.join(root, file)

            with open(filepath, 'r', encoding='utf8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

            title = soup.title.string if soup.title else ''
            body = ' '.join(soup.stripped_strings)

            filepath = filepath.replace('index.html', '')
            filepath = filepath.replace('.\\', '/')

            pages_data.append({
                'title': title,
                'body': body,
                'url': filepath,
            })

    # Create a ZIP file
    with zipfile.ZipFile('search_index.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Write the JSON data to a file inside the ZIP
        zipf.writestr('search_index.json', json.dumps(pages_data, ensure_ascii=False))

    os.chdir(cur_dir)