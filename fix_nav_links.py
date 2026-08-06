import glob
import re
import os

html_files = glob.glob('c:/Users/Admin/Downloads/uknseu/**/*.html', recursive=True)

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
    
    # 1. Remove .prevent from desktop nav clicks so links work!
    new_text = text.replace('@click.prevent="open = !open"', '@click="open = !open"')
    
    if new_text != text:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(new_text)

print(f"Updated {len(html_files)} HTML files for clickable nav links.")
