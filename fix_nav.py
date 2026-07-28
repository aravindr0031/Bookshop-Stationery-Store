import glob

old_active = """              <button class="text-xs uppercase tracking-[0.15em] font-medium text-accent hover:text-accent transition-colors flex items-center relative py-2">
                <span>Home</span>
                <i class="fas fa-chevron-down text-[10px] ms-2 transition-transform duration-300 group-hover:rotate-180"></i>
                <span class="absolute bottom-0 start-0 w-full h-[2px] bg-accent transition-all duration-300 group-hover:w-full"></span>
              </button>"""

new_active = """              <button class="text-xs uppercase tracking-[0.15em] font-medium text-accent hover:text-accent transition-colors flex items-center">
                <span class="relative py-2">
                  Home
                  <span class="absolute bottom-0 start-0 w-full h-[2px] bg-accent transition-all duration-300 group-hover:w-full"></span>
                </span>
                <i class="fas fa-chevron-down text-[10px] ms-2 transition-transform duration-300 group-hover:rotate-180 py-2"></i>
              </button>"""

old_inactive = """              <button class="text-xs uppercase tracking-[0.15em] font-medium text-gray-900 dark:text-gray-100 hover:text-accent transition-colors flex items-center relative py-2">
                <span>Home</span>
                <i class="fas fa-chevron-down text-[10px] ms-2 transition-transform duration-300 group-hover:rotate-180"></i>
                <span class="absolute bottom-0 start-0 w-0 h-[2px] bg-accent transition-all duration-300 group-hover:w-full"></span>
              </button>"""

new_inactive = """              <button class="text-xs uppercase tracking-[0.15em] font-medium text-gray-900 dark:text-gray-100 hover:text-accent transition-colors flex items-center">
                <span class="relative py-2">
                  Home
                  <span class="absolute bottom-0 start-0 w-0 h-[2px] bg-accent transition-all duration-300 group-hover:w-full"></span>
                </span>
                <i class="fas fa-chevron-down text-[10px] ms-2 transition-transform duration-300 group-hover:rotate-180 py-2"></i>
              </button>"""

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_active in content or old_inactive in content:
        content = content.replace(old_active, new_active)
        content = content.replace(old_inactive, new_inactive)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', filename)
