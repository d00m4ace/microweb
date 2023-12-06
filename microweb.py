import time

import src.posts_builder as posts_build
import src.search_builder as search_builder
import src.sitemap as sitemap

sitemap_urls = []

posts_config_file_path = 'site/test/posts.cfg'
pages_config_file_path = 'site/test/pages.cfg'

start_time = time.time()

posts = posts_build.build(sitemap_urls,posts_config_file_path)
pages = posts_build.build(sitemap_urls,pages_config_file_path)

sitemap.build(sitemap_urls)

def root_filter(root):
    if root == '.':
        return False
    if root == '.\posts':
        return False
    if root.startswith('.\\posts\\page'):
        return False
    if root.startswith('.\\posts\\tags'):
        return False
    return True


search_builder.build('output', root_filter)

print("DONE!")

end_time = time.time()

elapsed_time = end_time - start_time
formatted_time = "{:.2f}".format(elapsed_time)
print("Elapsed time: ", formatted_time, "seconds")
