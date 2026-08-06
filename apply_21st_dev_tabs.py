import glob
import re

html_files = glob.glob('c:/Users/Admin/Downloads/uknseu/**/*.html', recursive=True)

count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
    
    new_text = text
    
    # We want to transform the main navigation items into 21st.dev luxury tabs.
    # Current typical class: "menu-item text-slate-100 hover:text-amber-400 font-bold transition px-2 py-2 inline-flex items-center"
    # Target 21st.dev style class: "menu-item text-slate-200 hover:text-white font-semibold transition-all duration-300 px-4 py-2 inline-flex items-center rounded-full hover:bg-white/10 hover:shadow-[inset_0_1px_0_rgba(255,255,255,0.2)]"
    
    # We'll use regex to replace the class attribute of anything containing 'menu-item'
    # but ONLY in the main desktop navigation. The mobile nav has different classes.
    
    def upgrade_tab(match):
        classes = match.group(1)
        if 'menu-item' in classes:
            # Replace the generic hover and padding with 21st.dev pill/tab styling
            new_classes = re.sub(r'text-slate-100', 'text-slate-300', classes)
            new_classes = re.sub(r'hover:text-amber-400', 'hover:text-white', new_classes)
            new_classes = re.sub(r'font-bold', 'font-semibold', new_classes)
            new_classes = re.sub(r'px-2', 'px-3 lg:px-4', new_classes)
            # Add 21st.dev glass pill effect
            if 'rounded-full' not in new_classes:
                new_classes += ' rounded-full hover:bg-white/10 hover:shadow-[inset_0_1px_0_rgba(255,255,255,0.15)] ring-1 ring-transparent hover:ring-white/20 hover:backdrop-blur-md'
            return f'class="{new_classes}"'
        return match.group(0)

    # Let's target the exact string to be safe and avoid blowing up unrelated elements.
    # We can just replace the specific classes known to be on the menu items:
    target_class_1 = 'menu-item text-slate-100 hover:text-amber-400 font-bold transition px-2 py-2 inline-flex items-center cursor-pointer'
    replacement_1 = 'menu-item text-slate-300 hover:text-white font-semibold transition-all duration-300 px-4 py-2 inline-flex items-center cursor-pointer rounded-full hover:bg-white/10 hover:shadow-[inset_0_1px_0_rgba(255,255,255,0.15)] ring-1 ring-transparent hover:ring-white/20 hover:backdrop-blur-md'
    
    target_class_2 = 'menu-item text-slate-100 hover:text-amber-400 font-bold transition px-2 py-2 inline-flex items-center'
    replacement_2 = 'menu-item text-slate-300 hover:text-white font-semibold transition-all duration-300 px-4 py-2 inline-flex items-center rounded-full hover:bg-white/10 hover:shadow-[inset_0_1px_0_rgba(255,255,255,0.15)] ring-1 ring-transparent hover:ring-white/20 hover:backdrop-blur-md'

    new_text = new_text.replace(target_class_1, replacement_1)
    new_text = new_text.replace(target_class_2, replacement_2)
    
    # Also wrap the main nav container in a subtle 21st.dev pill if it's not already
    # <div class="flex items-center justify-between h-16">
    # Let's find the nav links container which is `<div class="hidden md:flex items-center space-x-1">`
    # We will add a subtle background and border to the container of the tabs to make it a real "Tab Bar"
    target_container = 'class="hidden md:flex items-center space-x-1"'
    replacement_container = 'class="hidden md:flex items-center space-x-1 bg-slate-900/50 p-1.5 rounded-full border border-slate-700/50 shadow-inner backdrop-blur-xl"'
    new_text = new_text.replace(target_container, replacement_container)
    
    if new_text != text:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(new_text)
        count += 1

print(f"Added 21st.dev Tab (Registerkarten) elements to {count} HTML files.")
