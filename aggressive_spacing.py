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
    
    # Force CSS cache bust again
    new_text = re.sub(r'href="(/css/style\.optimized\.css\?v=)\d+"', rf'href="\1{timestamp}"', new_text)
    if '?v=' not in new_text and '/css/style.optimized.css' in new_text:
        new_text = re.sub(r'href="(/css/style\.optimized\.css)[^"]*"', rf'href="\1?v={timestamp}"', new_text)

    # Aggressive spacing reduction
    # Reduce py-12 on the main hero container down to py-4 or py-6
    new_text = re.sub(r'\bpy-12\b', 'py-6', new_text)
    new_text = re.sub(r'\bpy-10\b', 'py-6', new_text)
    new_text = re.sub(r'\bpy-8\b', 'py-4', new_text)
    
    # Reduce header height from h-20 (80px) to h-16 (64px) to bring content higher up
    new_text = re.sub(r'\bh-20\b', 'h-16', new_text)
    
    # Reduce margins
    new_text = re.sub(r'\bmb-8\b', 'mb-6', new_text)
    new_text = re.sub(r'\bmt-8\b', 'mt-4', new_text)
    
    if new_text != text:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(new_text)
        count += 1

print(f"Aggressive spacing reduction applied to {count} HTML files.")
