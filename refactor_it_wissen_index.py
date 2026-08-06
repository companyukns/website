import re
import os

path = 'c:/Users/Admin/Downloads/uknseu/it-wissen/index.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Hero Section
hero_start = html.find('<!-- Hero Section -->')
hero_end = html.find('<!-- Articles Grid Section -->')

if hero_start != -1 and hero_end != -1:
    old_hero = html[hero_start:hero_end]
    new_hero = """<!-- Hero Section -->
  <section class="hub-hero">
    <h1>UKNS IT-Wissen &amp; Ratgeber</h1>
    <p>Ihr Experten-Hub für IT-Sicherheit, Cloud-Migration, Managed Services und Computerhilfe in Leipzig – 100% verständlich erklärt ohne Fachchinesisch.</p>
  </section>
  """
    html = html.replace(old_hero, new_hero)

# Replace Grid Section Start
grid_start = html.find('<!-- Articles Grid Section -->')
grid_end = html.find('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">')

if grid_start != -1 and grid_end != -1:
    old_grid_head = html[grid_start:grid_end + len('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">')]
    new_grid_head = """<!-- Articles Grid Section -->
  <section class="hub-container">
    <div class="hub-grid">"""
    html = html.replace(old_grid_head, new_grid_head)

# Replace grid closing
html = html.replace('      </div>\n    </div>\n  </section>', '    </div>\n  </section>')
html = html.replace('      </div>\r\n    </div>\r\n  </section>', '    </div>\n  </section>')

# Now parse the cards and convert them to hub-card
# Current card format:
# <a href="..." class="...">
#   <div class="block flex-grow">
#     <div class="p-7">
#       <span class="...">Tag</span>
#       <h3 class="...">Title</h3>
#       <p class="...">Description</p>
#     </div>
#   </div>
#   <div class="...">
#     ...
#   </div>
# </a>

def replace_card(match):
    href = match.group(1)
    tag = match.group(2)
    title = match.group(3)
    desc = match.group(4)
    
    # Clean up title (remove <h3> tags or text inside them, wait I just captured the inner HTML of span, h3, p)
    tag_clean = re.sub(r'<[^>]+>', '', tag).strip()
    title_clean = re.sub(r'<[^>]+>', '', title).strip()
    desc_clean = re.sub(r'<[^>]+>', '', desc).strip()
    
    return f"""<a href="{href}" class="hub-card">
          <span>{tag_clean}</span>
          <strong>{title_clean}</strong>
          <small>{desc_clean}</small>
        </a>"""

card_pattern = r'<a href="([^"]+)" class="bg-white rounded-2xl[^>]+>\s*<div class="block flex-grow">\s*<div class="p-7">\s*<span[^>]+>(.*?)</span>\s*<h3[^>]+>(.*?)</h3>\s*<p[^>]+>(.*?)</p>\s*</div>\s*</div>.*?</a>'
html = re.sub(card_pattern, replace_card, html, flags=re.DOTALL)


with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Refactored it-wissen/index.html to hub layout.")
