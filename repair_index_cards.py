import re

path = 'c:/Users/Admin/Downloads/uknseu/it-wissen/index.html'

with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Fix corrupted </a>/article>
html = html.replace('</a>/article>', '</a>')
html = html.replace('</article>/article>', '</article>')

# Remove nested <a> tags in the cards
# Replace:
# <a href="URL" class="bg-white..."><a class="block flex-grow" href="URL">
# with:
# <a href="URL" class="bg-white rounded-2xl shadow-lg border border-slate-200/90 overflow-hidden transform hover:-translate-y-1.5 transition-all duration-300 flex flex-col block group cursor-pointer">
# <div class="block flex-grow">

html = re.sub(
    r'<a href="([^"]+)" class="bg-white rounded-2xl shadow-lg border border-slate-200/90 overflow-hidden transform hover:-translate-y-1.5 transition-all duration-300 flex flex-col">\s*<a class="block flex-grow" href="[^"]+">',
    r'<a href="\1" class="bg-white rounded-2xl shadow-lg border border-slate-200/90 overflow-hidden transform hover:-translate-y-1.5 transition-all duration-300 flex flex-col block group cursor-pointer">\n            <div class="block flex-grow">',
    html
)

# Replace inner </a> before the footer of the card with </div>
html = re.sub(
    r'</div>\s*</a>\s*<div class="px-7 pb-6 pt-0 mt-auto border-t border-slate-100 flex items-center justify-between">',
    r'</div>\n          </div>\n          <div class="px-7 pb-6 pt-0 mt-auto border-t border-slate-100 flex items-center justify-between">',
    html
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Cleaned it-wissen/index.html cards HTML.")
