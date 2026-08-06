import time
import glob
import re

css_code = """
/* Missing Article Styles */
.article-hero {
  padding: 4rem 0;
  background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
  color: #fff;
}
.article-container {
  max-width: 72rem;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}
.article-hero-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 3rem;
  align-items: center;
}
@media (min-width: 960px) {
  .article-hero-grid {
    grid-template-columns: 1fr 1fr;
  }
}
.article-kicker {
  color: #F5A623;
  font-weight: 800;
  text-transform: uppercase;
  font-size: 0.875rem;
  margin-bottom: 1rem;
}
.article-hero h1 {
  font-size: 2.5rem;
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 1.5rem;
}
.article-lead {
  font-size: 1.25rem;
  color: #CBD5E1;
  margin-bottom: 2rem;
  line-height: 1.6;
}
.article-main {
  padding: 4rem 0;
  background-color: #F8FAFC;
}
.article-intro {
  font-size: 1.25rem;
  font-weight: 500;
  color: #334155;
  margin-bottom: 3rem;
  line-height: 1.7;
}
.content-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}
@media (min-width: 768px) {
  .content-grid {
    grid-template-columns: 1fr 1fr;
  }
}
.content-card {
  background: white;
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
  border: 1px solid #E2E8F0;
}
.content-card h2 {
  font-size: 1.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
  color: #0F172A;
}
.content-card p {
  color: #475569;
  margin-bottom: 1rem;
  line-height: 1.6;
}
.content-card ul {
  list-style-type: disc;
  padding-left: 1.5rem;
  color: #475569;
}
.content-card ul li {
  margin-bottom: 0.5rem;
}
.article-button-row {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}
.article-primary {
  background-color: #F5A623;
  color: #0F172A;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 700;
  transition: all 0.2s;
}
.article-primary:hover {
  background-color: #D97706;
}
.article-secondary {
  background-color: transparent;
  color: #F8FAFC;
  border: 1px solid #CBD5E1;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 700;
  transition: all 0.2s;
}
.article-secondary:hover {
  background-color: rgba(255, 255, 255, 0.1);
}
.article-hero-image {
  border-radius: 1rem;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}
"""

css_path = 'c:/Users/Admin/Downloads/uknseu/css/style.optimized.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Only append if not already there
if '.article-container' not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + css_code)
    print("Appended missing article CSS classes.")

# Update cache buster
timestamp = int(time.time())
html_files = glob.glob('c:/Users/Admin/Downloads/uknseu/**/*.html', recursive=True)
count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
    
    new_text = re.sub(r'href="(/css/style\.optimized\.css\?v=)\d+"', rf'href="\g<1>{timestamp}"', text)
    
    if new_text != text:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(new_text)
        count += 1

print(f"Updated cache buster in {count} HTML files.")
