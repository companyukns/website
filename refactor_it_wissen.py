import glob
import re
import os

files = glob.glob('c:/Users/Admin/Downloads/uknseu/it-wissen/*.html')
files.extend(glob.glob('c:/Users/Admin/Downloads/uknseu/it-notfallplan*/*.html'))
files.extend(glob.glob('c:/Users/Admin/Downloads/uknseu/it-dienstleister*/*.html'))

for fpath in files:
    if fpath.endswith('index.html') and 'it-wissen' in fpath:
        continue # skip the overview page, it's already a grid
        
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Skip if it doesn't have article-hero (maybe already refactored or different layout)
    if 'class="article-hero"' not in html:
        continue

    # Extract elements
    kicker_match = re.search(r'<p class="article-kicker">([^<]+)</p>', html)
    kicker = kicker_match.group(1) if kicker_match else "Wissen & Ratgeber"
    
    h1_match = re.search(r'<h1>(.*?)</h1>', html, re.DOTALL)
    h1 = h1_match.group(1) if h1_match else "IT-Ratgeber"
    
    lead_match = re.search(r'<p class="article-lead">(.*?)</p>', html, re.DOTALL)
    lead = lead_match.group(1) if lead_match else ""
    
    buttons_match = re.search(r'<div class="article-button-row">(.*?)</div>', html, re.DOTALL)
    buttons = buttons_match.group(1) if buttons_match else ""
    # Transform buttons to 21st.dev style
    buttons = buttons.replace('class="article-primary"', 'class="inline-block bg-amber-500 text-slate-900 font-bold px-8 py-4 rounded-xl hover:bg-amber-400 transition-all shadow-lg hover:shadow-amber-500/25"')
    buttons = buttons.replace('class="article-secondary"', 'class="inline-block bg-slate-800 text-white font-bold px-8 py-4 rounded-xl border border-slate-700 hover:bg-slate-700 transition-all"')
    
    pic_match = re.search(r'(<picture>.*?</picture>)', html, re.DOTALL)
    pic = pic_match.group(1) if pic_match else ""
    # Add rounded corners and shadow to picture img
    pic = re.sub(r'<img ', '<img class="w-full rounded-2xl shadow-2xl border border-slate-700/50" ', pic)
    
    intro_match = re.search(r'<p class="article-intro">(.*?)</p>', html, re.DOTALL)
    intro = intro_match.group(1) if intro_match else ""
    
    # Extract all content cards
    cards = re.findall(r'<section class="content-card">(.*?)</section>', html, re.DOTALL)
    
    # Build 21st.dev template
    # We use a dark, centered theme.
    new_main = f"""<main class="bg-slate-950 text-slate-300 relative overflow-hidden">
    <!-- Ambient Background Glow -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[500px] opacity-20 pointer-events-none" style="background: radial-gradient(circle, rgba(59,130,246,0.8) 0%, rgba(15,23,42,0) 70%);"></div>
    
    <article class="relative z-10 py-16 md:py-24">
        <!-- Hero Centered -->
        <header class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center mb-16">
            <span class="inline-block bg-slate-800 text-amber-400 text-xs font-bold uppercase tracking-wider py-1.5 px-4 rounded-full border border-amber-500/30 mb-6 shadow-[0_0_15px_rgba(245,166,35,0.15)]">{kicker}</span>
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white mb-8 leading-tight tracking-tight">{h1}</h1>
            <p class="text-xl md:text-2xl text-slate-300 font-medium leading-relaxed max-w-3xl mx-auto mb-10">{lead}</p>
            <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                {buttons}
            </div>
        </header>

        <!-- Centered Image in 21st.dev Glass Frame -->
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 mb-20">
            <div class="p-2 md:p-4 bg-slate-900/50 backdrop-blur-2xl rounded-3xl border border-slate-700/50 shadow-2xl">
                {pic}
            </div>
        </div>

        <!-- Centered Content -->
        <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
            <p class="text-xl text-slate-200 font-medium leading-relaxed mb-16 text-center">{intro}</p>
            
            <div class="space-y-8">
"""
    for card in cards:
        # Style inner tags of the card
        card_content = card
        card_content = re.sub(r'<h2>(.*?)</h2>', r'<h2 class="text-2xl font-bold text-white mb-4">\1</h2>', card_content)
        card_content = re.sub(r'<p>(.*?)</p>', r'<p class="text-slate-400 text-lg leading-relaxed mb-6">\1</p>', card_content)
        card_content = re.sub(r'<ul>(.*?)</ul>', r'<ul class="space-y-3 text-slate-300">\1</ul>', card_content, flags=re.DOTALL)
        card_content = re.sub(r'<li>(.*?)</li>', r'<li class="flex items-start"><i class="fas fa-check-circle text-amber-500 mt-1 mr-3"></i><span>\1</span></li>', card_content)
        
        new_main += f"""
                <div class="bg-slate-900/60 backdrop-blur-md rounded-3xl p-8 md:p-10 border border-slate-700/50 shadow-xl hover:border-slate-600 transition-colors">
                    {card_content}
                </div>
"""
    new_main += """
            </div>
        </div>
    </article>
</main>"""

    # Replace the old <main>...</main> with the new template
    new_html = re.sub(r'<main>.*?</main>', new_main, html, flags=re.DOTALL)
    
    if new_html != html:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)

print("Refactored IT-Wissen articles into centered 21st.dev layouts.")
