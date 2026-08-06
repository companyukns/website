import glob
import re
import time

css_code = """
/* 21st.dev IT-Wissen Article Layout (No-Tailwind Fallback) */
.it-article-main {
  background-color: #020617;
  color: #cbd5e1;
  position: relative;
  overflow: hidden;
}
.it-ambient-glow {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 1000px;
  height: 500px;
  opacity: 0.2;
  pointer-events: none;
  background: radial-gradient(circle, rgba(59,130,246,0.8) 0%, rgba(15,23,42,0) 70%);
}
.it-article-wrapper {
  position: relative;
  z-index: 10;
  padding-top: 4rem;
  padding-bottom: 6rem;
}
.it-container-hero {
  max-width: 56rem;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1rem;
  padding-right: 1rem;
  text-align: center;
  margin-bottom: 4rem;
}
.it-kicker {
  display: inline-block;
  background-color: #1e293b;
  color: #fbbf24;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.375rem 1rem;
  border-radius: 9999px;
  border: 1px solid rgba(245,166,35,0.3);
  margin-bottom: 1.5rem;
  box-shadow: 0 0 15px rgba(245,166,35,0.15);
}
.it-title {
  font-size: 2.25rem;
  font-weight: 800;
  color: #ffffff;
  margin-bottom: 2rem;
  line-height: 1.2;
}
@media (min-width: 768px) { .it-title { font-size: 3rem; } }
@media (min-width: 1024px) { .it-title { font-size: 3.75rem; } }
.it-lead {
  font-size: 1.25rem;
  color: #cbd5e1;
  font-weight: 500;
  line-height: 1.625;
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 2.5rem;
}
.it-buttons {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}
@media (min-width: 640px) { .it-buttons { flex-direction: row; } }
.it-btn-primary {
  display: inline-block;
  background-color: #f59e0b;
  color: #0f172a;
  font-weight: 700;
  padding: 1rem 2rem;
  border-radius: 0.75rem;
  transition: all 0.2s;
  box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
  text-decoration: none;
}
.it-btn-primary:hover {
  background-color: #fbbf24;
  box-shadow: 0 10px 25px -3px rgba(245,158,11,0.4);
}
.it-btn-secondary {
  display: inline-block;
  background-color: #1e293b;
  color: #ffffff;
  font-weight: 700;
  padding: 1rem 2rem;
  border-radius: 0.75rem;
  border: 1px solid #334155;
  transition: all 0.2s;
  text-decoration: none;
}
.it-btn-secondary:hover { background-color: #334155; }
.it-image-container {
  max-width: 64rem;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1rem;
  padding-right: 1rem;
  margin-bottom: 5rem;
}
.it-image-frame {
  padding: 0.5rem;
  background-color: rgba(15,23,42,0.5);
  backdrop-filter: blur(24px);
  border-radius: 1.5rem;
  border: 1px solid rgba(51,65,85,0.5);
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);
}
@media (min-width: 768px) { .it-image-frame { padding: 1rem; } }
.it-image {
  width: 100%;
  height: auto;
  border-radius: 1rem;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);
  border: 1px solid rgba(51,65,85,0.5);
  display: block;
}
.it-container-content {
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1rem;
  padding-right: 1rem;
}
.it-intro {
  font-size: 1.25rem;
  color: #e2e8f0;
  font-weight: 500;
  line-height: 1.625;
  margin-bottom: 4rem;
  text-align: center;
}
.it-cards-wrapper {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
.it-glass-card {
  background-color: rgba(15,23,42,0.6);
  backdrop-filter: blur(12px);
  border-radius: 1.5rem;
  padding: 2rem;
  border: 1px solid rgba(51,65,85,0.5);
  box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);
  transition: border-color 0.2s;
}
@media (min-width: 768px) { .it-glass-card { padding: 2.5rem; } }
.it-glass-card:hover { border-color: #475569; }
.it-card-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 1rem;
  line-height: 1.3;
}
.it-card-text {
  color: #94a3b8;
  font-size: 1.125rem;
  line-height: 1.625;
  margin-bottom: 1.5rem;
}
.it-card-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  color: #cbd5e1;
  padding: 0;
  margin: 0;
  list-style: none;
}
.it-card-list li {
  display: flex;
  align-items: flex-start;
}
.it-card-list i {
  color: #f59e0b;
  margin-top: 0.25rem;
  margin-right: 0.75rem;
}
"""

css_path = 'c:/Users/Admin/Downloads/uknseu/css/style.optimized.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.it-article-main' not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + css_code)
    print("Appended custom CSS for IT-Wissen.")

files = glob.glob('c:/Users/Admin/Downloads/uknseu/it-wissen/*.html')
files.extend(glob.glob('c:/Users/Admin/Downloads/uknseu/it-notfallplan*/*.html'))
files.extend(glob.glob('c:/Users/Admin/Downloads/uknseu/it-dienstleister*/*.html'))

timestamp = int(time.time())

for fpath in files:
    if fpath.endswith('index.html') and 'it-wissen' in fpath:
        continue
        
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    if '<main class="bg-slate-950 text-slate-300 relative overflow-hidden">' not in html:
        continue

    # Extract elements from the previously generated tailwind HTML
    
    kicker_match = re.search(r'<span class="inline-block bg-slate-800[^>]+>([^<]+)</span>', html)
    kicker = kicker_match.group(1) if kicker_match else "Wissen & Ratgeber"
    
    h1_match = re.search(r'<h1 class="text-4xl[^>]+>(.*?)</h1>', html, re.DOTALL)
    h1 = h1_match.group(1) if h1_match else "IT-Ratgeber"
    
    lead_match = re.search(r'<p class="text-xl md:text-2xl[^>]+>(.*?)</p>', html, re.DOTALL)
    lead = lead_match.group(1) if lead_match else ""
    
    buttons_match = re.search(r'<div class="flex flex-col sm:flex-row[^>]+>(.*?)</div>\s*</header>', html, re.DOTALL)
    buttons = buttons_match.group(1) if buttons_match else ""
    buttons = buttons.replace('class="inline-block bg-amber-500 text-slate-900 font-bold px-8 py-4 rounded-xl hover:bg-amber-400 transition-all shadow-lg hover:shadow-amber-500/25"', 'class="it-btn-primary"')
    buttons = buttons.replace('class="inline-block bg-slate-800 text-white font-bold px-8 py-4 rounded-xl border border-slate-700 hover:bg-slate-700 transition-all"', 'class="it-btn-secondary"')
    
    pic_match = re.search(r'(<picture>.*?</picture>)', html, re.DOTALL)
    pic = pic_match.group(1) if pic_match else ""
    pic = re.sub(r'class="w-full[^"]*" class="article-hero-image"', 'class="it-image"', pic)
    pic = re.sub(r'class="w-full[^"]*"', 'class="it-image"', pic)
    
    intro_match = re.search(r'<p class="text-xl text-slate-200[^>]+>(.*?)</p>', html, re.DOTALL)
    intro = intro_match.group(1) if intro_match else ""
    
    cards = re.findall(r'<div class="bg-slate-900/60 backdrop-blur-md[^>]+>(.*?)</div>\s*(?:</div>|</article>|<!--|<div class="bg-slate-900)', html, re.DOTALL)
    # The regex above is tricky because of nested divs.
    # Better logic to extract cards from the tailwind layout:
    cards = []
    parts = html.split('<div class="bg-slate-900/60 backdrop-blur-md')
    for p in parts[1:]:
        end_idx = p.find('</div>\n\n                <div class="bg-slate-900/60')
        if end_idx == -1:
            end_idx = p.find('</div>\n\n            </div>\n        </div>\n    </article>')
            if end_idx == -1:
                end_idx = p.rfind('</div>')
        cards.append(p[:end_idx])

    # Rebuild using strict semantic classes
    new_main = f"""<main class="it-article-main">
    <div class="it-ambient-glow"></div>
    
    <article class="it-article-wrapper">
        <header class="it-container-hero">
            <span class="it-kicker">{kicker}</span>
            <h1 class="it-title">{h1}</h1>
            <p class="it-lead">{lead}</p>
            <div class="it-buttons">
                {buttons.strip()}
            </div>
        </header>

        <div class="it-image-container">
            <div class="it-image-frame">
                {pic.strip()}
            </div>
        </div>

        <div class="it-container-content">
            <p class="it-intro">{intro}</p>
            
            <div class="it-cards-wrapper">
"""
    for card_html in cards:
        # Extract title, text, list
        c_title_match = re.search(r'<h2[^>]+>(.*?)</h2>', card_html, re.DOTALL)
        c_title = c_title_match.group(1) if c_title_match else ""
        
        c_text_match = re.search(r'<p[^>]+>(.*?)</p>', card_html, re.DOTALL)
        c_text = c_text_match.group(1) if c_text_match else ""
        
        c_list_items = re.findall(r'<span>(.*?)</span>', card_html, re.DOTALL)
        
        li_html = ""
        for li in c_list_items:
            li_html += f'<li><i class="fas fa-check-circle"></i><span>{li}</span></li>'
        
        ul_html = f'<ul class="it-card-list">{li_html}</ul>' if li_html else ""
        
        new_main += f"""
                <div class="it-glass-card">
                    <h2 class="it-card-title">{c_title}</h2>
                    <p class="it-card-text">{c_text}</p>
                    {ul_html}
                </div>
"""
    new_main += """
            </div>
        </div>
    </article>
</main>"""

    new_html = re.sub(r'<main class="bg-slate-950.*?<\/main>', new_main, html, flags=re.DOTALL)
    
    new_html = re.sub(r'href="(/css/style\.optimized\.css\?v=)\d+"', rf'href="\g<1>{timestamp}"', new_html)
    
    if new_html != html:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)

print("Semantic CSS refactoring applied to IT-Wissen!")
