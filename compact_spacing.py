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
    
    # 1. Force CSS cache bust so the user sees the dark dropdown
    new_text = re.sub(r'href="(/css/style\.optimized\.css)[^"]*"', rf'href="\1?v={timestamp}"', new_text)
    
    # 2. Reduce massive paddings and margins for sections and elements
    # py-24 (96px) -> py-12 (48px)
    new_text = re.sub(r'\bpy-24\b', 'py-12', new_text)
    # py-20 (80px) -> py-10 (40px)
    new_text = re.sub(r'\bpy-20\b', 'py-10', new_text)
    # py-16 (64px) -> py-8 (32px)
    new_text = re.sub(r'\bpy-16\b', 'py-8', new_text)
    
    # Reduce massive gaps
    # gap-16 (64px) -> gap-8
    new_text = re.sub(r'\bgap-16\b', 'gap-8', new_text)
    # gap-12 (48px) -> gap-6
    new_text = re.sub(r'\bgap-12\b', 'gap-6', new_text)
    
    # Reduce massive margins
    # mb-16 (64px) -> mb-8
    new_text = re.sub(r'\bmb-16\b', 'mb-8', new_text)
    # mb-12 (48px) -> mb-6
    new_text = re.sub(r'\bmb-12\b', 'mb-6', new_text)
    
    # Just in case there is a pt-24 or mt-24 specifically
    new_text = re.sub(r'\bpt-24\b', 'pt-12', new_text)
    new_text = re.sub(r'\bmt-24\b', 'mt-12', new_text)
    new_text = re.sub(r'\bpt-20\b', 'pt-10', new_text)
    new_text = re.sub(r'\bmt-20\b', 'mt-10', new_text)
    
    # 3. Ensure dropdowns have !bg-slate-900 via Tailwind (in case CSS is slow)
    new_text = new_text.replace('class="sub-menu absolute', 'class="sub-menu absolute !bg-slate-900')

    if new_text != text:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(new_text)
        count += 1

print(f"Reduced spacing and forced CSS cache refresh in {count} HTML files.")
