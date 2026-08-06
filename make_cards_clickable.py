import glob
import re

html_files = glob.glob('c:/Users/Admin/Downloads/uknseu/**/*.html', recursive=True)

count_service_cards = 0
count_article_cards = 0

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
    
    new_text = text
    
    # 1. Fix Service Cards
    # Find <div class="service-card-item ..."> ... <a ... href="URL">...</a> </div>
    # and convert the outer div to an <a>, and the inner <a> to a <span>.
    
    def process_service_card(match):
        global count_service_cards
        card_html = match.group(0)
        
        # Find the href inside the card
        href_match = re.search(r'<a[^>]+href="([^"]+)"[^>]*>.*?</a>', card_html)
        if not href_match:
            return card_html
        
        href = href_match.group(1)
        
        # Change outer <div class="service-card-item..."> to <a href="..." class="service-card-item block cursor-pointer group...">
        card_html = re.sub(r'^<div (class="[^"]*service-card-item[^"]*")', rf'<a href="{href}" \1', card_html)
        
        # Change inner <a class="..." href="...">...</a> to <span class="...">...</span>
        def replace_inner_a(m):
            inner_a = m.group(0)
            inner_a = inner_a.replace('<a ', '<span ')
            inner_a = inner_a.replace('</a>', '</span>')
            # Remove href attribute
            inner_a = re.sub(r'\s*href="[^"]*"', '', inner_a)
            return inner_a
            
        card_html = re.sub(r'<a[^>]+href="[^"]+"[^>]*>.*?</a>', replace_inner_a, card_html)
        
        # Change closing </div> to </a>
        card_html = re.sub(r'</div>$', '</a>', card_html)
        
        count_service_cards += 1
        return card_html

    # We need a robust regex to match the whole card. Service cards usually don't have nested <div class="service-card-item">.
    # We can match <div class="service-card-item ... </div> by finding the start, and counting divs, but regex is hard for nested divs.
    # Better approach: split by '<div class="service-card-item' and process.
    
    parts = new_text.split('<div class="service-card-item')
    if len(parts) > 1:
        processed_text = parts[0]
        for part in parts[1:]:
            # part contains the rest of the file starting with ' ..."> ...'
            # We need to find the matching closing </div>
            div_count = 1
            i = 0
            while div_count > 0 and i < len(part):
                if part[i:i+4] == '<div':
                    div_count += 1
                elif part[i:i+6] == '</div>':
                    div_count -= 1
                i += 1
            
            if div_count == 0:
                card_content = '<div class="service-card-item' + part[:i]
                remainder = part[i:]
                
                href_match = re.search(r'<a[^>]+href="([^"]+)"[^>]*>', card_content)
                if href_match:
                    href = href_match.group(1)
                    # Convert outer div to a
                    card_content = card_content.replace('<div class="service-card-item', f'<a href="{href}" class="service-card-item block cursor-pointer group', 1)
                    # Convert inner a to span
                    def replace_a(m):
                        s = m.group(0).replace('<a ', '<span ').replace('</a>', '</span>')
                        return re.sub(r'\s*href="[^"]*"', '', s)
                    card_content = re.sub(r'<a[^>]+href="[^"]+"[^>]*>.*?</a>', replace_a, card_content)
                    # Convert closing div to a
                    card_content = card_content[:-6] + '</a>'
                    count_service_cards += 1
                
                processed_text += card_content + remainder
            else:
                processed_text += '<div class="service-card-item' + part
        new_text = processed_text


    # 2. Fix Article Cards (in it-wissen)
    # `<article class="bg-white rounded-2xl shadow-lg border...`
    # Same logic: split by `<article `
    parts = new_text.split('<article ')
    if len(parts) > 1:
        processed_text = parts[0]
        for part in parts[1:]:
            div_count = 1
            i = 0
            while div_count > 0 and i < len(part):
                if part[i:i+8] == '<article':
                    div_count += 1
                elif part[i:i+10] == '</article>':
                    div_count -= 1
                i += 1
            
            if div_count == 0:
                card_content = '<article ' + part[:i]
                remainder = part[i:]
                
                href_match = re.search(r'<a[^>]+href="([^"]+)"[^>]*>', card_content)
                if href_match:
                    href = href_match.group(1)
                    # Convert outer article to a
                    card_content = card_content.replace('<article ', f'<a href="{href}" ', 1)
                    # Convert inner a to span or div
                    def replace_a2(m):
                        s = m.group(0).replace('<a ', '<div ').replace('</a>', '</div>')
                        return re.sub(r'\s*href="[^"]*"', '', s)
                    card_content = re.sub(r'<a[^>]+href="[^"]+"[^>]*>.*?</a>', replace_a2, card_content)
                    # Convert closing article to a
                    card_content = card_content[:-10] + '</a>'
                    count_article_cards += 1
                
                processed_text += card_content + remainder
            else:
                processed_text += '<article ' + part
        new_text = processed_text

    if new_text != text:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(new_text)

print(f"Made {count_service_cards} service cards and {count_article_cards} article cards fully clickable globally.")
