import os
import glob

# 1. Check bundle.js for scroll events
js_files = glob.glob(r'c:\Users\Admin\Downloads\uknseu\js\*.js')
print('JS Files found:', js_files)
for js in js_files:
    try:
        with open(js, 'r', encoding='utf-8') as f:
            content = f.read()
            if 'scroll' in content:
                print(f'Scroll event found in {js}')
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if 'scroll' in line:
                        print(f'Line {i}: {line}')
    except Exception as e:
        print(f"Error reading {js}: {e}")

# 2. Check for the old malformed block and clean it
malformed_block = """    <div class="flex flex-col sm:flex-row md:flex-col gap-3 w-full md:w-auto flex-shrink-0">
      <a href="/kontakt/?anfrage=15-Minuten-Gratis-Beratung" class="inline-flex items-center justify-center bg-primary-yellow text-primary-blue font-bold px-6 py-3.5 rounded-xl hover:bg-yellow-400 transition shadow-lg glow-button yellow-glow text-base text-center">
        <i class="fas fa-calendar-alt mr-2 text-lg"></i>Jetzt 15 Min. Gratis-Beratung sichern
      </a>
      <a href="mailto:support@ukns.eu?subject=15-Minuten%20Gratis-Beratung%20Anfrage" class="inline-flex items-center justify-center bg-white/10 hover:bg-white/20 text-white font-semibold px-6 py-3 rounded-xl transition border border-white/30 text-sm text-center">
        <i class="fas fa-envelope mr-2"></i>E-Mail schreiben
      </a>
    </div>
  </div>
</div>"""

malformed_block_2 = """    <div class="flex flex-col sm:flex-row md:flex-col gap-3 w-full md:w-auto flex-shrink-0">
      <a href="/kontakt/?anfrage=15-Minuten-Gratis-Beratung" class="inline-flex items-center justify-center bg-primary-yellow text-primary-blue font-bold px-6 py-3.5 rounded-xl hover:bg-yellow-400 transition shadow-lg glow-button yellow-glow text-base text-center">
        <i class="fas fa-calendar-alt mr-2 text-lg"></i>Jetzt 15 Min. Gratis-Beratung sichern
      </a>
      <a href="mailto:support@ukns.eu?subject=15-Minuten%20Gratis-Beratung%20Anfrage" class="inline-flex items-center justify-center bg-white/10 hover:bg-white/20 text-white font-semibold px-6 py-3 rounded-xl transition border border-white/30 text-sm text-center">
        <i class="fas fa-envelope mr-2"></i>E-Mail schreiben
      </a>
    </div>"""

html_files = glob.glob(r'c:\Users\Admin\Downloads\uknseu\**\*.html', recursive=True)
fixed_count = 0
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        if malformed_block in content:
            content = content.replace(malformed_block, '')
            modified = True
            
        if malformed_block_2 in content:
            content = content.replace(malformed_block_2, '')
            modified = True
            
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_count += 1
    except Exception as e:
        pass
print(f'Fixed {fixed_count} files with malformed block.')
