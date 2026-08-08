import sys

file_path = r'c:\Users\Admin\Downloads\uknseu\css\style.optimized.css'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_css = """/* Lead Magnet Section (Robust Custom CSS) */
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
}"""

new_css = """/* Lead Magnet Section (Robust Custom CSS with High Contrast) */
.it-lm-section {
  background: #0f172a !important; /* Solid Dark Navy */
  padding: 4rem 1.5rem !important;
  color: #ffffff !important;
  border-top: 1px solid #334155 !important;
  border-bottom: 1px solid #334155 !important;
}
.it-lm-container {
  max-width: 80rem;
  margin-left: auto;
  margin-right: auto;
}
.it-lm-header {
  text-align: center;
  margin-bottom: 3.5rem;
}
.it-lm-badge {
  display: inline-block !important;
  background-color: rgba(245, 158, 11, 0.15) !important;
  color: #f59e0b !important;
  border: 1px solid rgba(245, 158, 11, 0.4) !important;
  font-weight: 800 !important;
  padding: 0.35rem 1.125rem !important;
  border-radius: 9999px !important;
  font-size: 0.75rem !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
  margin-bottom: 1.25rem !important;
}
.it-lm-header h2 {
  font-size: 2.25rem !important;
  font-weight: 800 !important;
  color: #ffffff !important;
  margin-bottom: 1rem !important;
  line-height: 1.2 !important;
}
.it-lm-header p {
  font-size: 1.125rem !important;
  color: #cbd5e1 !important;
  max-width: 48rem !important;
  margin-left: auto !important;
  margin-right: auto !important;
  line-height: 1.6 !important;
}
.it-lm-grid {
  display: grid !important;
  grid-template-columns: 1fr !important;
  gap: 2rem !important;
}
@media (min-width: 768px) {
  .it-lm-grid { grid-template-columns: repeat(3, 1fr) !important; gap: 2rem !important; }
}
@media (min-width: 1024px) {
  .it-lm-grid { gap: 2.5rem !important; }
}
.it-lm-card {
  background-color: #1e293b !important; /* Solid Slate Navy for guaranteed contrast */
  border-radius: 1.25rem !important;
  padding: 2rem !important;
  border: 1px solid #334155 !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 15px 35px -5px rgba(0,0,0,0.4) !important;
}
.it-lm-card:hover {
  transform: translateY(-5px) !important;
  border-color: #f59e0b !important;
  box-shadow: 0 20px 40px -10px rgba(245,158,11,0.2) !important;
}
.it-lm-card-header {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 0.75rem !important;
  flex-wrap: wrap !important; /* Prevents overlap */
  margin-bottom: 1.25rem !important;
  width: 100% !important;
}
.it-lm-card-badge {
  background-color: #f59e0b !important;
  color: #0f172a !important;
  font-weight: 800 !important;
  padding: 0.3rem 0.75rem !important;
  border-radius: 0.5rem !important;
  font-size: 0.7rem !important;
  text-transform: uppercase !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
  display: inline-flex !important;
  align-items: center !important;
}
.it-lm-card-time {
  color: #f59e0b !important;
  background: rgba(245, 158, 11, 0.15) !important;
  border: 1px solid rgba(245, 158, 11, 0.4) !important;
  font-weight: 800 !important;
  font-size: 0.7rem !important;
  padding: 0.25rem 0.625rem !important;
  border-radius: 0.5rem !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
  display: inline-flex !important;
  align-items: center !important;
  margin-left: auto !important;
}
.it-lm-card-title {
  font-size: 1.3rem !important;
  font-weight: 800 !important;
  color: #ffffff !important;
  margin-bottom: 0.875rem !important;
  line-height: 1.35 !important;
}
.it-lm-card-desc {
  color: #cbd5e1 !important; /* High contrast on #1e293b */
  font-size: 0.9375rem !important;
  margin-bottom: 1.25rem !important;
  line-height: 1.6 !important;
}
.it-lm-card-list {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 0 1.75rem 0 !important;
}
.it-lm-card-list li {
  display: flex !important;
  align-items: flex-start !important;
  color: #f8fafc !important; /* Pure white text for checkmarks */
  font-size: 0.9rem !important;
  font-weight: 600 !important;
  margin-bottom: 0.75rem !important;
}
.it-lm-card-list li i {
  color: #f59e0b !important;
  margin-right: 0.625rem !important;
  margin-top: 0.2rem !important;
  font-size: 1rem !important;
  flex-shrink: 0 !important;
}
.it-lm-btn {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 0.5rem !important;
  width: 100% !important;
  text-align: center !important;
  background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%) !important;
  color: #0f172a !important;
  font-weight: 900 !important;
  padding: 0.875rem 1.25rem !important;
  border-radius: 0.875rem !important;
  text-decoration: none !important;
  font-size: 0.95rem !important;
  transition: all 0.2s ease-in-out !important;
  box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4) !important;
}
.it-lm-btn:hover {
  background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 25px rgba(245, 158, 11, 0.6) !important;
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced CSS successfully.")
else:
    print("Error: Old CSS block not found.")
