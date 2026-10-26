# -*- coding: utf-8 -*-
import glob
import json
import re
import os
import subprocess

blogs = [b for b in sorted(glob.glob('blog-*.html')) if b not in ('blog-glow-after-bad-sleep.html', 'blog-glow-before-event.html')]

nav_results_cnt = 0
qa_box_cnt = 0
geo_matrix_cnt = 0
inline_quiz_cnt = 0
video_mod_cnt = 0
video_schema_cnt = 0
json_errors = []

for b in blogs:
    c = open(b, encoding='utf-8').read()
    if 'href="results.html"' in c: nav_results_cnt += 1
    if 'class="short-answer-box"' in c: qa_box_cnt += 1
    if 'class="geo-matrix"' in c: geo_matrix_cnt += 1
    if 'class="bojin-inline-quiz"' in c: inline_quiz_cnt += 1
    if 'data-video-module' in c: video_mod_cnt += 1
    if '"@type": "VideoObject"' in c or '"@type":"VideoObject"' in c: video_schema_cnt += 1

    for m in re.finditer(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', c, re.S | re.I):
        try:
            json.loads(m.group(1))
        except Exception as e:
            json_errors.append((b, str(e)))

print(f"Total Real Blog Posts Checked : {len(blogs)}")
print(f"1. Top Nav 'Results' Link     : {nav_results_cnt} / {len(blogs)}")
print(f"2. 30s Quick Answer Box       : {qa_box_cnt} / {len(blogs)}")
print(f"3. 2026 GEO Comparison Matrix : {geo_matrix_cnt} flagship pages")
print(f"4. 10s Inline Micro-Quiz Card : {inline_quiz_cnt} / 35 target pages")
print(f"5. Video Demo Module Embedded : {video_mod_cnt} / 12 target pages")
print(f"6. VideoObject JSON-LD Schema : {video_schema_cnt} / 12 target pages")
print(f"7. JSON-LD Syntax Errors      : {len(json_errors)}")

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
art_dir = r'C:\Users\user888\.gemini\antigravity\brain\2ef321a4-4efb-44fa-808a-4f31b0f2703e'

if os.path.exists(chrome):
    p1 = os.path.join(art_dir, 'us-pack-desktop-1440.png')
    p2 = os.path.join(art_dir, 'us-pack-mobile-375.png')
    subprocess.run([chrome, '--headless=new', '--disable-gpu', '--window-size=1440,1050', f'--screenshot={p1}', 'http://127.0.0.1:8900/blog-heavy-low-brows-lift.html#quick-summary'], check=True)
    subprocess.run([chrome, '--headless=new', '--disable-gpu', '--window-size=375,812', f'--screenshot={p2}', 'http://127.0.0.1:8900/blog-heavy-low-brows-lift.html#quick-summary'], check=True)
    print("Screenshots saved:", p1, p2)
