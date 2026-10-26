# -*- coding: utf-8 -*-
import glob

for p in glob.glob('blog-*.html'):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c
    if 'class="geo-matrix-wrap"' in c and 'id="geo-table"' not in c:
        c = c.replace('class="geo-matrix-wrap"', 'class="geo-matrix-wrap" id="geo-table"', 1)
    if 'class="bojin-inline-quiz"' in c and 'id="inline-quiz-card"' not in c:
        c = c.replace('class="bojin-inline-quiz"', 'class="bojin-inline-quiz" id="inline-quiz-card"', 1)
    if 'class="bojin-video-module"' in c and 'id="video-demo-card"' not in c:
        c = c.replace('class="bojin-video-module"', 'class="bojin-video-module" id="video-demo-card"', 1)
    if '<div class="callout"><span class="callout-label">30-second summary</span>' in c:
        c = c.replace('<div class="callout"><span class="callout-label">30-second summary</span>', '<div class="callout" id="old-30s-summary"><span class="callout-label">30-second summary</span>', 1)
    if '<figure class="bojin-figure" style="margin:1.6rem 0">' in c and 'id="jaw-gold-photo"' not in c:
        c = c.replace('<figure class="bojin-figure" style="margin:1.6rem 0">', '<figure class="bojin-figure" id="jaw-gold-photo" style="margin:1.6rem 0">', 1)
    if c != orig:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)

# Also add the video module to blog-jaw-clenching-grinding-and-bojin.html so all 4 demos can be seen on that page too
jaw_path = 'blog-jaw-clenching-grinding-and-bojin.html'
with open(jaw_path, 'r', encoding='utf-8') as f:
    jc = f.read()
if 'id="video-demo-card"' not in jc:
    v_html = '''<section class="bojin-video-module" id="video-demo-card" data-video-module data-youtube-id="">
  <div class="bvm-player-wrap">
    <video controls playsinline preload="metadata" poster="assets/journal/52b355b8d0.jpg">
      <source src="assets/journal/ca6d02ebb3.mp4" type="video/mp4">
    </video>
  </div>
  <div class="bvm-copy">
    <span class="biq-badge">🎥 12-Second Technique Preview</span>
    <h3>How the Supporting Hand Anchors Skin During Facial Bojin</h3>
    <p>Yu-Ting Lan demonstrates how to place your supporting hand to steady the skin before gliding the Bojin tool, preventing skin drag.</p>
    <a class="btn" href="landing.html#get">Watch Full 3-Min Guided Video &rarr;</a>
  </div>
</section>
'''
    jc = jc.replace('<h2 id="the-5-steps-for-a-tight-clenching-jaw">', v_html + '<h2 id="the-5-steps-for-a-tight-clenching-jaw">', 1)
    with open(jaw_path, 'w', encoding='utf-8') as f:
        f.write(jc)

# Make the waitlist form in eye-method-course-preview.html immediately open (not hidden behind a click)
with open('eye-method-course-preview.html', 'r', encoding='utf-8') as f:
    ec = f.read()
ec = ec.replace('aria-expanded="false" aria-controls="checkout-note" id="checkout-preview"', 'aria-expanded="true" aria-controls="checkout-note" id="checkout-preview"')
ec = ec.replace('<div class="preview-status" id="checkout-note" hidden>', '<div class="preview-status" id="checkout-note">')
with open('eye-method-course-preview.html', 'w', encoding='utf-8') as f:
    f.write(ec)

# Add scroll-margin-top to styles.css so sticky header never covers anchor targets
with open('styles.css', 'r', encoding='utf-8') as f:
    sc = f.read()
if '#quick-summary, #geo-table' not in sc:
    sc += '\n#quick-summary, #geo-table, #inline-quiz-card, #video-demo-card, #old-30s-summary, #jaw-gold-photo { scroll-margin-top: 96px; }\n'
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(sc)

print('[OK] All direct anchor links and open waitlist form ready!')
