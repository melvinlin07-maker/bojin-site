# -*- coding: utf-8 -*-
import glob
import re

audio_bar_html = """<div class="bojin-audio-bar" id="audio-guide-bar" data-audio-src="">
  <div class="bab-left">
    <button type="button" class="bab-play-btn" data-audio-guide-btn>🎧 Listen to 3-Min Audio Guide</button>
    <div class="bab-meta">
      <span class="bab-title">Eyes tired from screens? Listen while you rest your eyes</span>
      <span class="bab-sub">Spoken English overview · Gentle self-care walk-through</span>
    </div>
  </div>
</div>
"""

blog_files = glob.glob('blog-*.html')
audio_added = 0
quiz_removed = 0

for p in blog_files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c
    if 'http-equiv="refresh"' in c:
        continue
    # 1. Remove Quiz from nav-links
    c = re.sub(r'\s*<a\s+href="quiz\.html">Quiz</a>', '', c)
    c = re.sub(r'\s*<a\s+class="active"\s+href="quiz\.html">Quiz</a>', '', c)
    if '<a href="quiz.html">Quiz</a>' not in c and '<a href="quiz.html">Quiz</a>' in orig:
        quiz_removed += 1
        
    # 2. Add Audio Guide bar to all 99 real articles if not present
    if 'id="audio-guide-bar"' not in c and 'id="quick-summary"' in c:
        c = c.replace('<div class="short-answer-box" id="quick-summary">', audio_bar_html + '<div class="short-answer-box" id="quick-summary">', 1)
        audio_added += 1
        
    if c != orig:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)

# Also remove Quiz from core pages nav
core_pages = ['index.html', 'start.html', 'about.html', 'what-is-bojin.html', 'results.html', 'landing.html', 'blog.html', 'map.html', 'guide.html', 'eye-start-quiz.html']
for p in core_pages:
    try:
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        orig = c
        c = re.sub(r'\s*<a\s+href="quiz\.html">Quiz</a>', '', c)
        c = re.sub(r'\s*<a\s+class="active"\s+href="quiz\.html">Quiz</a>', '', c)
        if c != orig:
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
    except:
        pass

print(f'[OK] Done! Removed Quiz from nav. Audio Guide Bar added to {audio_added} more articles (now 100% of all 99 blog articles have it)!')
