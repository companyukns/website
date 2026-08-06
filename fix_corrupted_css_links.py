import glob
import re
import time

html_files = glob.glob('c:/Users/Admin/Downloads/uknseu/**/*.html', recursive=True)
timestamp = int(time.time())

count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
    
    new_text = text
    
    def fix_link_tag(match):
        tag = match.group(0)
        # Check if it's a stylesheet link and NOT google fonts
        if 'rel="stylesheet"' in tag and 'fonts.googleapis.com' not in tag:
            # Replace whatever href it has with the correct CSS path
            tag = re.sub(r'href="[^"]*"', f'href="/css/style.optimized.css?v={timestamp}"', tag)
        return tag

    # Find all <link ... > tags
    new_text = re.sub(r'<link[^>]+>', fix_link_tag, new_text)
    
    if new_text != text:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(new_text)
        count += 1

print(f"Fixed broken CSS links in {count} HTML files.")
