import glob
import os

article_styles = '''
/* ==========================================================================
   IT-WISSEN ARTICLE MASTER STYLES (Restored & Polished)
   ========================================================================== */

.article-container {
  max-width: 52rem;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.article-hero {
  background: linear-gradient(180deg, #0F172A 0%, #080D1A 100%) !important;
  color: #FFFFFF;
  padding: 5rem 0 4rem 0;
  text-align: center;
}

.article-hero-grid {
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
  align-items: center;
}

.article-kicker {
  color: #F5A623;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
}

.article-hero h1 {
  font-size: 2.75rem;
  font-weight: 900;
  line-height: 1.2;
  margin-bottom: 1.5rem;
  color: #FFFFFF !important;
}

.article-lead {
  font-size: 1.25rem;
  color: #CBD5E1;
  margin-bottom: 2rem;
  max-width: 42rem;
  margin-left: auto;
  margin-right: auto;
}

.article-hero-image {
  border-radius: 1.5rem;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  max-width: 100%;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.article-main {
  padding: 5rem 0;
  background-color: #F8FAFC;
}

.article-intro {
  font-size: 1.25rem;
  line-height: 1.8;
  color: #334155;
  margin-bottom: 3.5rem;
}

.content-grid {
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
  margin-bottom: 4rem;
}

.content-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 1.5rem;
  padding: 3rem;
  box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.05);
}

.content-card h2 {
  font-size: 1.75rem;
  font-weight: 800;
  color: #0F172A !important;
  margin-bottom: 1.25rem;
}

.content-card p {
  color: #475569 !important;
  line-height: 1.8;
  margin-bottom: 1.25rem;
}

.content-card ul {
  list-style-type: disc;
  padding-left: 1.5rem;
  color: #475569 !important;
}

.content-card ul li {
  margin-bottom: 0.75rem;
}

.article-section {
  margin-bottom: 5rem;
}

.article-section-title {
  font-size: 2.25rem;
  font-weight: 800;
  color: #0F172A !important;
  margin-bottom: 2.5rem;
}

.steps-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.step-card {
  background: #FFFFFF;
  border-top: 4px solid #F5A623;
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}

.step-card span {
  display: inline-block;
  background: #FEF3C7;
  color: #B45309;
  font-weight: 900;
  font-size: 0.875rem;
  padding: 0.35rem 1rem;
  border-radius: 9999px;
  margin-bottom: 1.25rem;
}

.step-card h3 {
  font-weight: 800;
  font-size: 1.25rem;
  margin-bottom: 0.75rem;
  color: #0F172A !important;
}

.step-card p {
  color: #475569 !important;
}

.faq-grid {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.faq-item {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 1.25rem;
  padding: 1.75rem;
}

.faq-item summary {
  font-weight: 800;
  font-size: 1.25rem;
  color: #0F172A !important;
  cursor: pointer;
  outline: none;
}

.faq-item p {
  margin-top: 1.25rem;
  color: #475569 !important;
}

.related-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.related-card {
  display: block;
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  padding: 1.75rem;
  border-radius: 1.25rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.related-card:hover {
  border-color: #2563EB;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  transform: translateY(-3px);
}

.related-card strong {
  display: block;
  font-weight: 800;
  color: #0F172A !important;
  margin-bottom: 0.5rem;
}

.related-card small {
  color: #64748B;
}

.article-cta {
  background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
  border-radius: 1.75rem;
  padding: 3.5rem;
  color: #FFFFFF;
  text-align: center;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.article-cta h2 {
  font-size: 2rem;
  font-weight: 900;
  margin-bottom: 1.25rem;
  color: #FFFFFF !important;
}

.article-cta p {
  color: #CBD5E1 !important;
  margin-bottom: 2.5rem;
}

.article-cta .article-primary {
  display: inline-block;
  background: #F5A623;
  color: #0F172A;
  font-weight: 900;
  padding: 1.25rem 2.5rem;
  border-radius: 1rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.article-cta .article-primary:hover {
  background: #FCD34D;
  transform: translateY(-2px);
}

.article-button-row {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 2rem;
}

.article-button-row .article-primary {
  background: #F5A623;
  color: #0F172A;
  font-weight: 900;
  padding: 1rem 2rem;
  border-radius: 1rem;
  text-decoration: none;
  transition: all 0.2s;
}

.article-button-row .article-primary:hover {
  background: #FCD34D;
  transform: translateY(-2px);
}

.article-button-row .article-secondary {
  background: transparent;
  color: #FFFFFF;
  border: 2px solid rgba(255, 255, 255, 0.3);
  font-weight: 900;
  padding: 1rem 2rem;
  border-radius: 1rem;
  text-decoration: none;
  transition: all 0.2s;
}

.article-button-row .article-secondary:hover {
  border-color: #FFFFFF;
  background: rgba(255, 255, 255, 0.1);
}

.article-footer {
  background: #0F172A;
  color: #94A3B8 !important;
  padding: 4rem 0;
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.article-footer strong {
  color: #F8FAFC !important;
}

.article-footer a {
  color: #CBD5E1 !important;
}

.article-footer a:hover {
  color: #F5A623 !important;
}
'''

css_files = glob.glob('c:/Users/Admin/Downloads/uknseu/css/style.optimized.css', recursive=True)
for cfile in css_files:
    with open(cfile, 'r', encoding='utf-8', errors='ignore') as fp:
        css_text = fp.read()
    if 'IT-WISSEN ARTICLE MASTER STYLES' not in css_text:
        new_css_text = css_text + '\n' + article_styles
        with open(cfile, 'w', encoding='utf-8') as fp:
            fp.write(new_css_text)
        print(f"Added IT-Wissen article styles to {cfile}")
    else:
        print(f"Styles already exist in {cfile}")
