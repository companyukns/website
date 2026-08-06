import glob
import time

hub_css = """
/* Hub Pages (Firmenkunden & Privatkunden Übersichten) */
.hub-hero {
  background: linear-gradient(135deg, #020617 0%, #0f172a 100%);
  padding: 4rem 1.5rem;
  text-align: center;
  color: white;
}
.hub-hero h1 {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
}
.hub-hero p {
  font-size: 1.25rem;
  color: #94a3b8;
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
}
.hub-container {
  max-width: 80rem;
  margin-left: auto;
  margin-right: auto;
  padding: 4rem 1.5rem;
}
.hub-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}
@media (min-width: 640px) {
  .hub-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1024px) {
  .hub-grid { grid-template-columns: repeat(3, 1fr); }
}
.hub-card {
  display: flex;
  flex-direction: column;
  background-color: #0f172a;
  border: 1px solid rgba(51,65,85,0.5);
  border-radius: 1rem;
  padding: 1.5rem;
  text-decoration: none;
  transition: all 0.2s ease-in-out;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}
.hub-card:hover {
  transform: translateY(-4px);
  border-color: #f59e0b;
  box-shadow: 0 20px 25px -5px rgba(245, 158, 11, 0.15);
}
.hub-card img {
  width: 100%;
  height: 160px;
  object-fit: cover;
  border-radius: 0.75rem;
  margin-bottom: 1rem;
}
.hub-card span {
  font-size: 0.75rem;
  font-weight: 700;
  color: #f59e0b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.5rem;
}
.hub-card strong {
  font-size: 1.125rem;
  color: #ffffff;
  margin-bottom: 0.5rem;
  line-height: 1.4;
}
.hub-card small {
  font-size: 0.875rem;
  color: #94a3b8;
  line-height: 1.5;
}
"""

css_path = 'c:/Users/Admin/Downloads/uknseu/css/style.optimized.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.hub-container' not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + hub_css)
    print("Appended missing Hub CSS classes.")

# Update cache buster across all HTML files
timestamp = int(time.time())
import re

files = glob.glob('c:/Users/Admin/Downloads/uknseu/**/*.html', recursive=True)
count = 0
for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
    
    new_text = re.sub(r'href="(/css/style\.optimized\.css\?v=)\d+"', rf'href="\g<1>{timestamp}"', text)
    
    if new_text != text:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(new_text)
        count += 1

print(f"Updated cache buster in {count} HTML files.")
