# -*- coding: utf-8 -*-
import glob
import subprocess

files_to_add = [
    'styles.css',
    'nav.js',
    'sitemap.xml',
    'llms.txt',
    'llms-full.txt',
    'eye-method-course-preview.html',
    'brow-guide.html',
    'quiz.html',
    'results.html',
    'map.html',
    'guide.html',
    'landing.html',
    'about.html',
    'index.html',
    'start.html',
    'what-is-bojin.html',
]

# Add all blog-*.html
files_to_add.extend(glob.glob('blog-*.html'))

# Add outputs and scripts
files_to_add.extend(glob.glob('outputs/*.md'))
files_to_add.append('DIMENSIONAL_STRIKE_US_MASTER_BLUEPRINT_20261026.md')
files_to_add.extend(glob.glob('scripts/*.py'))

print(f'Staging {len(files_to_add)} specific files...')
for f in files_to_add:
    res = subprocess.run(['git', 'add', f], capture_output=True, text=True)
    if res.returncode != 0:
        print(f'Error adding {f}: {res.stderr}')

print('[OK] Staging complete. Running git diff --cached --stat:')
subprocess.run(['git', 'diff', '--cached', '--stat'])
