import glob
import time

lm_css = """
/* Lead Magnet Section (Robust Custom CSS) */
.it-lm-section {
  background: linear-gradient(135deg, #020617 0%, #0f172a 100%);
  padding: 4rem 1.5rem;
  color: white;
  border-top: 1px solid rgba(51,65,85,0.5);
}
.it-lm-container {
  max-width: 80rem;
  margin-left: auto;
  margin-right: auto;
}
.it-lm-header {
  text-align: center;
  margin-bottom: 3rem;
}
.it-lm-badge {
  display: inline-block;
  background-color: #f59e0b;
  color: #0f172a;
  font-weight: 800;
  padding: 0.375rem 1rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}
.it-lm-header h2 {
  font-size: 2.25rem;
  font-weight: 800;
  color: #ffffff;
  margin-bottom: 1rem;
  line-height: 1.2;
}
.it-lm-header p {
  font-size: 1.125rem;
  color: #cbd5e1;
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.6;
}
.it-lm-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}
@media (min-width: 768px) {
  .it-lm-grid { grid-template-columns: repeat(3, 1fr); }
}
.it-lm-card {
  background-color: rgba(255,255,255,0.05);
  backdrop-filter: blur(12px);
  border-radius: 1rem;
  padding: 1.5rem;
  border: 1px solid rgba(255,255,255,0.1);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.3s ease;
  box-shadow: 0 10px 25px -5px rgba(0,0,0,0.2);
}
.it-lm-card:hover {
  transform: translateY(-5px);
  border-color: #f59e0b;
}
.it-lm-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}
.it-lm-card-badge {
  background-color: #f59e0b;
  color: #0f172a;
  font-weight: 800;
  padding: 0.25rem 0.625rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  text-transform: uppercase;
}
.it-lm-card-time {
  color: #f59e0b;
  font-weight: 700;
  font-size: 0.75rem;
}
.it-lm-card-title {
  font-size: 1.25rem;
  font-weight: 800;
  color: #ffffff;
  margin-bottom: 0.75rem;
  line-height: 1.3;
}
.it-lm-card-desc {
  color: #e2e8f0;
  font-size: 0.875rem;
  margin-bottom: 1rem;
  line-height: 1.5;
}
.it-lm-card-list {
  list-style: none;
  padding: 0;
  margin: 0 0 1.5rem 0;
}
.it-lm-card-list li {
  display: flex;
  align-items: flex-start;
  color: #e2e8f0;
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
}
.it-lm-card-list li i {
  color: #f59e0b;
  margin-right: 0.5rem;
  margin-top: 0.25rem;
}
.it-lm-btn {
  display: block;
  width: 100%;
  text-align: center;
  background-color: #f59e0b;
  color: #0f172a;
  font-weight: 800;
  padding: 0.75rem 1rem;
  border-radius: 0.75rem;
  text-decoration: none;
  font-size: 0.875rem;
  transition: all 0.2s;
}
.it-lm-btn:hover {
  background-color: #fbbf24;
  box-shadow: 0 0 15px rgba(245,158,11,0.4);
}
"""

css_path = 'c:/Users/Admin/Downloads/uknseu/css/style.optimized.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.it-lm-section' not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + lm_css)
    print("Appended missing Lead Magnet CSS classes.")
else:
    print("Lead Magnet CSS already exists.")

# Now replace the HTML in all files
# We will use regex to find the section block:
import re

new_lm_html = """<!-- ## LEAD MAGNET SECTION: GRATIS-ANGEBOTE FÜR FIRMENKUNDEN ## -->
<section class="it-lm-section" id="gratis-angebote">
  <div class="it-lm-container">
    <div class="it-lm-header">
      <span class="it-lm-badge">Exklusiv für Firmenkunden in Leipzig</span>
      <h2>Sichern Sie sich Ihr kostenloses 15-Minuten Erstgespräch</h2>
      <p>Wählen Sie Ihr passendes Aufhänger-Angebot – 100% unverbindlich, direkt anwendbar und speziell auf Leipziger Unternehmen zugeschnitten.</p>
    </div>

    <div class="it-lm-grid">
      <!-- Angebot 1: Firmen & Mittelstand -->
      <div class="it-lm-card">
        <div>
          <div class="it-lm-card-header">
            <span class="it-lm-card-badge">Mittelstand & Gewerbe</span>
            <span class="it-lm-card-time"><i class="fas fa-clock mr-1"></i>15 Min. Gratis</span>
          </div>
          <h3 class="it-lm-card-title"><i class="fas fa-shield-alt text-primary-yellow mr-2"></i>20-Punkte IT-Sicherheitsanalyse</h3>
          <p class="it-lm-card-desc">Prüfung von Firmen-IT, Schwachstellen, Ransomware-Risiken, Cloud-Sicherheit & Backup-Strategien mit klarer Standortbestimmung.</p>
          <ul class="it-lm-card-list">
            <li><i class="fas fa-check-circle"></i>Schwachstellen- & Ransomware-Check</li>
            <li><i class="fas fa-check-circle"></i>E-Mail-, Cloud- & Passwort-Prüfung</li>
            <li><i class="fas fa-check-circle"></i>Konkreter IT-Handlungsplan</li>
          </ul>
        </div>
        <a href="/kontakt/?anfrage=20-Punkte-Sicherheitsanalyse" class="it-lm-btn">
          <i class="fas fa-calendar-check mr-1.5"></i>Sicherheitsanalyse anfragen
        </a>
      </div>

      <!-- Angebot 2: Arztpraxen & Kanzleien -->
      <div class="it-lm-card">
        <div>
          <div class="it-lm-card-header">
            <span class="it-lm-card-badge">Praxen & Kanzleien</span>
            <span class="it-lm-card-time"><i class="fas fa-clock mr-1"></i>15 Min. Gratis</span>
          </div>
          <h3 class="it-lm-card-title"><i class="fas fa-user-shield text-primary-yellow mr-2"></i>IT-Notfall- & DSGVO-Check</h3>
          <p class="it-lm-card-desc">Für sensible Daten in Kanzleien, Praxen & Immobilienfirmen: Ausfallsicherheit, Notfall-Wiederherstellung und DSGVO-Compliance.</p>
          <ul class="it-lm-card-list">
            <li><i class="fas fa-check-circle"></i>Ausfallsicherheits-Check für Praxen</li>
            <li><i class="fas fa-check-circle"></i>DSGVO-Datensicherung & Verschlüsselung</li>
            <li><i class="fas fa-check-circle"></i>Garantierte IT-Notfall-Reaktionszeit</li>
          </ul>
        </div>
        <a href="/kontakt/?anfrage=DSGVO-Notfall-Check" class="it-lm-btn">
          <i class="fas fa-user-md mr-1.5"></i>DSGVO-Notfall-Check anfragen
        </a>
      </div>

      <!-- Angebot 3: Berater & Dienstleister -->
      <div class="it-lm-card">
        <div>
          <div class="it-lm-card-header">
            <span class="it-lm-card-badge">Beratung & Dienstleister</span>
            <span class="it-lm-card-time"><i class="fas fa-clock mr-1"></i>15 Min. Gratis</span>
          </div>
          <h3 class="it-lm-card-title"><i class="fas fa-laptop-code text-primary-yellow mr-2"></i>IT-Strategie- & Effizienz-Beratung</h3>
          <p class="it-lm-card-desc">Für Unternehmensberater, Agenturen & Dienstleister: Optimierung von Microsoft 365, KI-Workflows, Cloud-Kosten & flexiblen Berater-Arbeitsplätzen.</p>
          <ul class="it-lm-card-list">
            <li><i class="fas fa-check-circle"></i>Microsoft 365 & Cloud-Potential-Analyse</li>
            <li><i class="fas fa-check-circle"></i>KI-Automatisierung für Routinen</li>
            <li><i class="fas fa-check-circle"></i>Sicheres Homeoffice & Mobiles Arbeiten</li>
          </ul>
        </div>
        <a href="/kontakt/?anfrage=IT-Strategie-Beratung" class="it-lm-btn">
          <i class="fas fa-lightbulb mr-1.5"></i>Effizienz-Beratung anfragen
        </a>
      </div>
    </div>
  </div>
</section>
<!-- ## END LEAD MAGNET SECTION ## -->"""

files = glob.glob('c:/Users/Admin/Downloads/uknseu/**/*.html', recursive=True)
count = 0
timestamp = str(int(time.time()))

for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
    
    # We need to find the block starting with "<!-- ## LEAD MAGNET SECTION: GRATIS-ANGEBOTE FÜR FIRMENKUNDEN ## -->"
    # and ending with "<!-- ## END LEAD MAGNET SECTION ## -->" or just before the <footer> if the end comment is missing.
    
    # Check if the block exists
    if "<!-- ## LEAD MAGNET SECTION: GRATIS-ANGEBOTE FÜR FIRMENKUNDEN ## -->" in text:
        # Regex to replace the whole block
        pattern = r'<!-- ## LEAD MAGNET SECTION: GRATIS-ANGEBOTE FÜR FIRMENKUNDEN ## -->.*?<!-- ## END LEAD MAGNET SECTION ## -->'
        new_text = re.sub(pattern, new_lm_html, text, flags=re.DOTALL)
        
        # If it doesn't have the end tag for some reason:
        if new_text == text:
            pattern2 = r'<!-- ## LEAD MAGNET SECTION: GRATIS-ANGEBOTE FÜR FIRMENKUNDEN ## -->.*?(?=<footer)'
            new_text = re.sub(pattern2, new_lm_html + '\n', text, flags=re.DOTALL)
            
        # Also update cache buster
        new_text = re.sub(r'href="(/css/style\.optimized\.css\?v=)\d+"', rf'href="\g<1>{timestamp}"', new_text)
        
        if new_text != text:
            with open(fpath, 'w', encoding='utf-8') as fp:
                fp.write(new_text)
            count += 1

print(f"Updated Lead Magnet HTML in {count} HTML files.")
