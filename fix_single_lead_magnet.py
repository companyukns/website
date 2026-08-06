import glob
import time
import re

single_css = """
/* Lockerer Lead Magnet (Single Column) */
.it-lm-single {
  margin-top: 3rem;
  margin-bottom: 3rem;
  background: linear-gradient(to right, #0f172a, #1e293b, #0f172a);
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);
  color: white;
  border: 2px solid rgba(245, 158, 11, 0.4);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
@media (min-width: 768px) {
  .it-lm-single {
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }
}
.it-lm-single-bg {
  position: absolute;
  right: -2.5rem;
  bottom: -2.5rem;
  opacity: 0.1;
  pointer-events: none;
  font-size: 8rem;
  color: white;
}
.it-lm-single-content {
  position: relative;
  z-index: 10;
  max-width: 42rem;
}
.it-lm-single-badge {
  display: inline-flex;
  align-items: center;
  background-color: #f59e0b;
  color: #0f172a;
  font-weight: 700;
  font-size: 0.75rem;
  text-transform: uppercase;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  margin-bottom: 0.75rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}
.it-lm-single-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: white;
  margin-bottom: 0.75rem;
  line-height: 1.3;
}
@media (min-width: 768px) { .it-lm-single-title { font-size: 1.875rem; } }
.it-lm-single-text {
  color: #f3f4f6;
  font-size: 1rem;
  line-height: 1.625;
  margin-bottom: 1rem;
}
.it-lm-single-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
  color: #f59e0b;
}
.it-lm-single-list span {
  display: flex;
  align-items: center;
}
.it-lm-single-list span i { color: white; margin-right: 0.375rem; }
.it-lm-single-actions {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  flex-shrink: 0;
  position: relative;
  z-index: 10;
  width: 100%;
}
@media (min-width: 640px) {
  .it-lm-single-actions { flex-direction: row; width: auto; }
}
@media (min-width: 768px) {
  .it-lm-single-actions { flex-direction: column; }
}
.it-lm-single-btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: #f59e0b;
  color: #0f172a;
  font-weight: 700;
  padding: 0.875rem 1.5rem;
  border-radius: 0.75rem;
  transition: all 0.2s;
  text-decoration: none;
  font-size: 1rem;
  text-align: center;
}
.it-lm-single-btn-primary:hover {
  background-color: #fbbf24;
  box-shadow: 0 0 15px rgba(245, 158, 11, 0.4);
}
.it-lm-single-btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(255,255,255,0.1);
  color: white;
  font-weight: 600;
  padding: 0.75rem 1.5rem;
  border-radius: 0.75rem;
  border: 1px solid rgba(255,255,255,0.3);
  transition: all 0.2s;
  text-decoration: none;
  font-size: 0.875rem;
  text-align: center;
}
.it-lm-single-btn-secondary:hover { background-color: rgba(255,255,255,0.2); }
"""

css_path = 'c:/Users/Admin/Downloads/uknseu/css/style.optimized.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.it-lm-single' not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + single_css)
    print("Appended missing Lead Magnet Single CSS classes.")

new_html = """<!-- ## LOCKERER 15-MINUTEN GRATIS-BERATUNG LEAD MAGNET ## -->
<div class="it-lm-single">
  <div class="it-lm-single-bg">
    <i class="fas fa-headset"></i>
  </div>
  <div class="it-lm-single-content">
    <div class="it-lm-single-badge">
      <i class="fas fa-coffee mr-1.5"></i>100% Unverbindlich &amp; Entspannt
    </div>
    <h3 class="it-lm-single-title">Lass uns einfach 15 Minuten quatschen! ☕</h3>
    <p class="it-lm-single-text">
      Du hast Fragen zu deiner IT, suchst nach einer Lösung oder möchtest wissen, ob es einfacher &amp; günstiger geht? Wir beraten dich super locker, voll auf Augenhöhe und komplett ohne Fachchinesisch oder Verkaufsdruck!
    </p>
    <div class="it-lm-single-list">
      <span><i class="fas fa-check-circle"></i> 15 Min. Gratis-Gespräch</span>
      <span><i class="fas fa-check-circle"></i> 100% Ehrlicher Experten-Rat</span>
      <span><i class="fas fa-check-circle"></i> Direkt anwendbare Tipps</span>
    </div>
  </div>
  <div class="it-lm-single-actions">
    <a href="/kontakt/?anfrage=15-Minuten-Gratis-Beratung" class="it-lm-single-btn-primary">
      <i class="fas fa-calendar-alt mr-2"></i>Jetzt 15 Min. Gratis-Beratung sichern
    </a>
    <a href="mailto:support@ukns.eu?subject=15-Minuten%20Gratis-Beratung%20Anfrage" class="it-lm-single-btn-secondary">
      <i class="fas fa-envelope mr-2"></i>E-Mail schreiben
    </a>
  </div>
</div>
<!-- ## END LOCKERER LEAD MAGNET ## -->"""

files = glob.glob('c:/Users/Admin/Downloads/uknseu/**/*.html', recursive=True)
count = 0
timestamp = str(int(time.time()))

for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
    
    if "<!-- ## LOCKERER 15-MINUTEN GRATIS-BERATUNG LEAD MAGNET ## -->" in text:
        # Some don't have the END tag, so we replace from START to </div>...
        # Let's be smart: use regex to replace from START to just before <footer or <section id="contact" or </main> 
        # Actually, the easiest is to just find the START comment and the END comment. Since we didn't add an END comment in `add_friendly_lead_magnet_everywhere.py`, it looks like this:
        # <!-- ## LOCKERER 15-MINUTEN GRATIS-BERATUNG LEAD MAGNET ## -->
        # <div class="my-12 ..."> ... </div>
        # (Next element like </main> or <section id="contact">)
        
        # Regex to find the block: start comment, any characters, up to (but not including) the next major tag.
        # But wait, earlier script inserted exactly `banner_html`.
        # Let's extract the exact banner_html we injected and replace it directly!
        
        banner_html_injected = '''<!-- ## LOCKERER 15-MINUTEN GRATIS-BERATUNG LEAD MAGNET ## -->
<div class="my-12 bg-gradient-to-r from-primary-blue via-light-blue to-primary-blue p-8 md:p-10 rounded-2xl shadow-2xl text-white border-2 border-primary-yellow/40 relative overflow-hidden" data-aos="fade-up">
  <div class="absolute -right-10 -bottom-10 opacity-10 pointer-events-none">
    <i class="fas fa-headset text-9xl"></i>
  </div>
  <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-8">
    <div class="max-w-2xl text-center md:text-left">
      <div class="inline-flex items-center bg-primary-yellow text-primary-blue font-bold text-xs uppercase px-3 py-1 rounded-full mb-3 shadow-md">
        <i class="fas fa-coffee mr-1.5 text-sm"></i>100% Unverbindlich &amp; Entspannt
      </div>
      <h3 class="text-2xl md:text-3xl font-bold text-white mb-3">Lass uns einfach 15 Minuten quatschen! ☕</h3>
      <p class="text-gray-100 text-base leading-relaxed mb-4">
        Du hast Fragen zu deiner IT, suchst nach einer Lösung oder möchtest wissen, ob es einfacher &amp; günstiger geht? Wir beraten dich super locker, voll auf Augenhöhe und komplett ohne Fachchinesisch oder Verkaufsdruck!
      </p>
      <div class="flex flex-wrap items-center justify-center md:justify-start gap-4 text-xs font-semibold text-primary-yellow">
        <span class="flex items-center"><i class="fas fa-check-circle mr-1.5 text-white"></i> 15 Min. Gratis-Gespräch</span>
        <span class="flex items-center"><i class="fas fa-check-circle mr-1.5 text-white"></i> 100% Ehrlicher Experten-Rat</span>
        <span class="flex items-center"><i class="fas fa-check-circle mr-1.5 text-white"></i> Direkt anwendbare Tipps</span>
      </div>
    </div>
    <div class="flex flex-col sm:flex-row md:flex-col gap-3 w-full md:w-auto flex-shrink-0">
      <a href="/kontakt/?anfrage=15-Minuten-Gratis-Beratung" class="inline-flex items-center justify-center bg-primary-yellow text-primary-blue font-bold px-6 py-3.5 rounded-xl hover:bg-yellow-400 transition shadow-lg glow-button yellow-glow text-base text-center">
        <i class="fas fa-calendar-alt mr-2 text-lg"></i>Jetzt 15 Min. Gratis-Beratung sichern
      </a>
      <a href="mailto:support@ukns.eu?subject=15-Minuten%20Gratis-Beratung%20Anfrage" class="inline-flex items-center justify-center bg-white/10 hover:bg-white/20 text-white font-semibold px-6 py-3 rounded-xl transition border border-white/30 text-sm text-center">
        <i class="fas fa-envelope mr-2"></i>E-Mail schreiben
      </a>
    </div>
  </div>
</div>'''
        
        # Replace the exact string
        if banner_html_injected in text:
             new_text = text.replace(banner_html_injected, new_html)
        else:
             # Fallback regex if formatting slightly differs
             pattern = r'<!-- ## LOCKERER 15-MINUTEN GRATIS-BERATUNG LEAD MAGNET ## -->.*?E-Mail schreiben\s*</a>\s*</div>\s*</div>\s*</div>'
             new_text = re.sub(pattern, new_html, text, flags=re.DOTALL)
             
        # cache buster
        new_text = re.sub(r'href="(/css/style\.optimized\.css\?v=)\d+"', rf'href="\g<1>{timestamp}"', new_text)
        
        if new_text != text:
            with open(fpath, 'w', encoding='utf-8') as fp:
                fp.write(new_text)
            count += 1

print(f"Updated Single Lead Magnet HTML in {count} HTML files.")
