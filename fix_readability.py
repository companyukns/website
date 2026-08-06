import glob
import re

# 1. Fix Impressum & Datenschutz massive spacing
for fpath in ['c:/Users/Admin/Downloads/uknseu/impressum/index.html', 'c:/Users/Admin/Downloads/uknseu/datenschutz/index.html']:
    try:
        with open(fpath, 'r', encoding='utf-8') as fp:
            text = fp.read()
        
        # Replace 'prose prose-lg' with a tighter prose configuration
        new_text = text.replace(
            'prose prose-lg', 
            'prose prose-base prose-headings:mt-4 prose-headings:mb-2 prose-p:my-2 prose-ul:my-2 prose-li:my-0'
        )
        # Also let's reduce py-6 back to py-8 or whatever is reasonable if needed, 
        # but the main issue is the prose spacing.
        
        if new_text != text:
            with open(fpath, 'w', encoding='utf-8') as fp:
                fp.write(new_text)
    except FileNotFoundError:
        pass

# 2. Fix IT-Wissen Readability & double badges
it_wissen_index = 'c:/Users/Admin/Downloads/uknseu/it-wissen/index.html'
try:
    with open(it_wissen_index, 'r', encoding='utf-8') as fp:
        text = fp.read()
    
    new_text = text
    # Remove the old small badge since we have the new 21st.dev badge
    new_text = re.sub(r'<span class="bg-amber-400 text-slate-950 font-black text-xs uppercase px-4 py-1\.5 rounded-full shadow-md inline-block mb-4">.*?</span>\s*', '', new_text)
    
    # Let's increase the py-4 slightly so it's not squished to the header
    new_text = new_text.replace('<section class="py-4 md:py-6 bg-gradient-to-br', '<section class="py-12 md:py-16 bg-gradient-to-br')
    
    # Maybe the white text on light background? No, it's a dark background.
    # What if the user meant the individual articles? Let's fix the articles too.
    
    if new_text != text:
        with open(it_wissen_index, 'w', encoding='utf-8') as fp:
            fp.write(new_text)
except FileNotFoundError:
    pass

# Let's also check all it-wissen subpages for readability (prose spacing and hero padding)
article_files = glob.glob('c:/Users/Admin/Downloads/uknseu/it-wissen/*.html')
for fpath in article_files:
    if fpath.endswith('index.html'): continue
    with open(fpath, 'r', encoding='utf-8') as fp:
        text = fp.read()
    
    new_text = text
    # Fix prose spacing for readability
    new_text = new_text.replace('prose prose-lg', 'prose prose-base prose-headings:mt-6 prose-headings:mb-3 prose-p:my-3')
    
    # Fix hero section padding if it was squished
    new_text = new_text.replace('py-4 md:py-6 bg-gradient-to-br', 'py-10 md:py-16 bg-gradient-to-br')
    new_text = new_text.replace('py-4 bg-slate-50', 'py-10 bg-slate-50')
    new_text = new_text.replace('py-6 bg-slate-50', 'py-10 bg-slate-50')
    
    if new_text != text:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(new_text)

print("Fixed Impressum spacing and IT-Wissen readability.")
