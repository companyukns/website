import os
import re
import time

def bust_cache_in_all_html(directory):
    new_timestamp = str(int(time.time()))
    count = 0
    pattern = re.compile(rb'href="/css/style\.optimized\.css(\?v=\d+)?"')
    new_str = f'href="/css/style.optimized.css?v={new_timestamp}"'.encode('utf-8')
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'rb') as f:
                    content = f.read()
                
                if pattern.search(content):
                    new_content = pattern.sub(new_str, content)
                    with open(file_path, 'wb') as f:
                        f.write(new_content)
                    count += 1
                    
    print(f"Updated cache buster in {count} HTML files safely (binary mode).")

if __name__ == "__main__":
    bust_cache_in_all_html(r"c:\Users\Admin\Downloads\uknseu")
