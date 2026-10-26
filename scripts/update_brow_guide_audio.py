# -*- coding: utf-8 -*-

audio_bar = """<div class="bojin-audio-bar" id="audio-guide-bar" data-audio-src="" style="margin: 1.2rem 0 2rem;">
  <div class="bab-left">
    <button type="button" class="bab-play-btn" data-audio-guide-btn>🎧 Listen to 3-Min Audio Guide</button>
    <div class="bab-meta">
      <span class="bab-title">Brows feeling heavy from screens? Listen to the movement walk-through</span>
      <span class="bab-sub">Spoken English guide · Small circles vs swaying comparison</span>
    </div>
  </div>
</div>
"""

with open('brow-guide.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remove Quiz from nav
c = c.replace('<a href="quiz.html">Quiz</a>\n', '')
c = c.replace('<a href="quiz.html">Quiz</a>', '')

# 2. Insert audio bar right under intro
target = '<p class="v3-intro" style="border-bottom:1px solid var(--line);padding-bottom:24px;margin-bottom:12px">Region 01 of our eye series: Brows &amp; Inner Brow. Scroll through 6 structured parts: Expression → 5-Muscle Map → Movement Comparison → Glide Preparation → 5 Detail Q&amp;As → Full Sequence Orientation. Use the sticky navigator above to jump between parts at any time.</p>'
if target in c and 'id="audio-guide-bar"' not in c:
    c = c.replace(target, target + '\n' + audio_bar)

with open('brow-guide.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('[OK] brow-guide.html updated with Audio Guide Bar and Quiz removed!')
