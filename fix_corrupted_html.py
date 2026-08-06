import glob
import re

files = glob.glob('c:/Users/Admin/Downloads/uknseu/**/*.html', recursive=True)

fixed_count = 0
for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
    
    new_text = text
    # Fix corrupted tags like </a>/article> or </article>/article>
    new_text = re.sub(r'</a>/article>', '</a>', new_text)
    new_text = re.sub(r'</article>/article>', '</article>', new_text)
    
    # Fix nested <a> tags: <a href="X" class="..."><a class="..." href="X"> ... </a>
    # If an <a> tag is wrapped in another <a> tag with the same href, remove the inner <a> tag!
    def clean_nested_a(match):
        outer_open = match.group(1) # <a href="..." ...>
        inner_content = match.group(2) # <a class="..." ...> ... </a> ...
        
        # Remove inner <a ...> and </a>
        inner_content = re.sub(r'<a[^>]*>', '<div class="block flex-grow">', inner_content)
        inner_content = inner_content.replace('</a>', '</div>')
        return outer_open + inner_content + '</a>'

    # Match <a href="...">...<a ...>...</a>...</a>
    # Let's do it carefully for it-wissen/index.html cards:
    # <a href="URL" class="bg-white..."><a class="block flex-grow" href="URL">...</a>...</a>
    pattern = r'(<a\s+href="[^"]+"\s+class="bg-white[^"]*">)\s*<a\s+class="block flex-grow"[^>]*>(.*?)</div>\s*</a>'
    
    if new_text != text:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(new_text)
        fixed_count += 1

print(f"Fixed corrupted tags in {fixed_count} files.")
