# -*- coding: utf-8 -*-
import os
import re
import glob

ROOT = r'c:\Users\user888\Documents\撥筋美國網站'

# 1. Append CSS for Black Tech 4 (Audio Guide Player) & Black Tech 5 (Pinterest Save Button)
css_path = os.path.join(ROOT, 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

extra_css = """
/* 6. Black Tech 4: Audio Guide Bar (Listen to Article / NotebookLM Dual-Host Slot) */
.bojin-audio-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  margin: 1.2rem 0 1.4rem;
  padding: 0.85rem 1.2rem;
  background: color-mix(in srgb, var(--jade, #351D2C) 6%, var(--paper-2, #FFFDFC));
  border: 1px solid var(--line-gold, #DCC69B);
  border-radius: 999px;
  box-shadow: 0 3px 12px rgba(53, 29, 44, 0.05);
}
.bab-left {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.bab-play-btn {
  appearance: none;
  border: 1.5px solid var(--cta-border, #B89558);
  background: var(--brand-bg, #351D2C);
  color: var(--brand-on, #FBF6EF);
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 700;
  padding: 0.48rem 1.05rem;
  border-radius: 999px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  transition: transform 0.15s ease, opacity 0.15s ease;
}
.bab-play-btn:hover {
  transform: translateY(-1px);
  opacity: 0.92;
}
.bab-meta {
  display: flex;
  flex-direction: column;
  line-height: 1.25;
}
.bab-title {
  font-family: var(--font-sans);
  font-size: 0.86rem;
  font-weight: 700;
  color: var(--ink);
}
.bab-sub {
  font-family: var(--font-sans);
  font-size: 0.76rem;
  color: var(--ink-soft);
}

/* 7. Black Tech 5: Pinterest Visual Search Save Button on Original Anatomy Photos */
.bojin-figure, .portrait-card {
  position: relative;
}
.bojin-pin-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: rgba(189, 8, 28, 0.92);
  color: #fff !important;
  font-family: var(--font-sans);
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  padding: 6px 12px;
  border-radius: 999px;
  text-decoration: none !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
  transition: transform 0.15s ease, background 0.15s ease;
}
.bojin-pin-btn:hover {
  background: #e60023;
  transform: scale(1.04);
}
#audio-guide-bar { scroll-margin-top: 96px; }
"""

if '.bojin-audio-bar' not in css:
    css += '\n' + extra_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Update nav.js to support Audio Guide read-aloud + Pinterest Save Button injection on all figures
nav_path = os.path.join(ROOT, 'nav.js')
with open(nav_path, 'r', encoding='utf-8') as f:
    nav_js = f.read()

extra_js = """
/* === Black Tech 4 & 5: Audio Guide Spoken Overview + Pinterest Save Button === */
(function(){
  // 1. Audio Guide Bar Handler (Supports MP3 file if present, or instant natural US English Speech Synthesis)
  document.addEventListener('click', function(e){
    var btn = e.target.closest('[data-audio-guide-btn]');
    if (!btn) return;
    var bar = btn.closest('.bojin-audio-bar');
    var audioSrc = bar ? bar.getAttribute('data-audio-src') : '';
    if (audioSrc) {
      var aud = bar.querySelector('audio');
      if (!aud) {
        aud = document.createElement('audio');
        aud.src = audioSrc;
        bar.appendChild(aud);
      }
      if (aud.paused) {
        aud.play();
        btn.textContent = '⏸ Pause Audio Guide';
        if (window.bojinSignal) window.bojinSignal('BojinAudioGuidePlay', { page: location.pathname });
      } else {
        aud.pause();
        btn.textContent = '🎧 Listen to 3-Min Audio Guide';
      }
      return;
    }
    if ('speechSynthesis' in window) {
      if (window.speechSynthesis.speaking && !window.speechSynthesis.paused) {
        window.speechSynthesis.cancel();
        btn.textContent = '🎧 Listen to 3-Min Audio Guide';
        return;
      }
      var art = document.querySelector('article.section') || document.querySelector('main');
      if (!art) return;
      var h1 = art.querySelector('h1') ? art.querySelector('h1').innerText : '';
      var qs = document.getElementById('quick-summary') ? document.getElementById('quick-summary').innerText : '';
      var paras = Array.from(art.querySelectorAll('p, h2, li')).slice(0, 18).map(function(el){ return el.innerText; }).join('. ');
      var utter = new SpeechSynthesisUtterance(h1 + '. ' + qs + '. ' + paras);
      utter.lang = 'en-US';
      utter.rate = 0.96;
      utter.onend = function(){ btn.textContent = '🎧 Listen to 3-Min Audio Guide'; };
      window.speechSynthesis.cancel();
      window.speechSynthesis.speak(utter);
      btn.textContent = '⏹ Stop Audio Guide (Playing...)';
      if (window.bojinSignal) window.bojinSignal('BojinAudioGuidePlay', { page: location.pathname });
    }
  });

  // 2. Pinterest Save Button Auto-Injector on Anatomy Figures (.bojin-figure, .portrait-card)
  function initPinButtons(){
    var figs = document.querySelectorAll('.bojin-figure, .portrait-card');
    var pageUrl = encodeURIComponent('https://bojinfacetension.com/' + (location.pathname.split('/').pop() || 'index.html'));
    figs.forEach(function(fig){
      if (fig.querySelector('.bojin-pin-btn')) return;
      var img = fig.querySelector('img');
      if (!img) return;
      var rawSrc = img.getAttribute('src') || '';
      var mediaUrl = encodeURIComponent('https://bojinfacetension.com/' + rawSrc.replace(/^\\//, ''));
      var desc = encodeURIComponent((img.getAttribute('alt') || document.title) + ' — The Bojin Method by Yu-Ting Lan');
      var a = document.createElement('a');
      a.className = 'bojin-pin-btn';
      a.href = 'https://www.pinterest.com/pin/create/button/?url=' + pageUrl + '&media=' + mediaUrl + '&description=' + desc;
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
      a.setAttribute('aria-label', 'Save anatomy diagram to Pinterest');
      a.innerHTML = '📌 Save';
      a.addEventListener('click', function(){
        if (window.bojinSignal) window.bojinSignal('BojinPinterestSave', { media: rawSrc });
      });
      fig.appendChild(a);
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPinButtons);
  } else {
    initPinButtons();
  }
})();
"""

if 'BojinAudioGuidePlay' not in nav_js:
    nav_js += '\n' + extra_js
    with open(nav_path, 'w', encoding='utf-8') as f:
        f.write(nav_js)

# 3. Inject the Audio Guide Bar (#audio-guide-bar) into the Top 10 GSC Flagship Articles
TOP_10_AUDIO = [
    'blog-heavy-low-brows-lift.html',
    'blog-jaw-clenching-grinding-and-bojin.html',
    'blog-gua-sha-vs-bojin.html',
    'blog-natural-botox-alternative-forehead.html',
    'blog-forehead-frown-lines.html',
    'blog-tired-puffy-eyes.html',
    'blog-the-supporting-hand.html',
    'blog-how-much-pressure.html',
    'blog-screen-tired-eyes-desk-reset.html',
    'blog-neck-tension-showing-in-your-face.html',
]

audio_html = """<div class="bojin-audio-bar" id="audio-guide-bar" data-audio-src="">
  <div class="bab-left">
    <button type="button" class="bab-play-btn" data-audio-guide-btn>🎧 Listen to 3-Min Audio Guide</button>
    <div class="bab-meta">
      <span class="bab-title">Eyes tired from screens? Listen while you rest your eyes</span>
      <span class="bab-sub">Spoken English overview · Gentle self-care walk-through</span>
    </div>
  </div>
</div>
"""

for fname in TOP_10_AUDIO:
    fpath = os.path.join(ROOT, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'id="audio-guide-bar"' not in c and 'id="quick-summary"' in c:
        c = c.replace('<div class="short-answer-box" id="quick-summary">', audio_html + '<div class="short-answer-box" id="quick-summary">', 1)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

# 4. Upgrade sitemap.xml with <image:image> tags for all 99 blog articles (Black Tech 5)
sitemap_path = os.path.join(ROOT, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sm = f.read()

if 'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"' not in sm:
    sm = sm.replace(
        'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"'
    )

img_added = 0
for bpath in sorted(glob.glob(os.path.join(ROOT, 'blog-*.html'))):
    bname = os.path.basename(bpath)
    with open(bpath, 'r', encoding='utf-8') as f:
        bc = f.read()
    if 'http-equiv="refresh"' in bc:
        continue
    # Find all article images
    imgs = re.findall(r'<img[^>]+src="([^"]+)"[^>]*>', bc)
    title_m = re.search(r'<title>([^<]+)</title>', bc)
    page_title = title_m.group(1).strip() if title_m else 'The Bojin Method'
    loc_tag = f'<loc>https://bojinfacetension.com/{bname}</loc>'
    if loc_tag in sm:
        # Check if <image:image> already inside this <url> block
        pos = sm.find(loc_tag)
        end_url = sm.find('</url>', pos)
        block = sm[pos:end_url]
        if '<image:image>' not in block and imgs:
            img_tags = []
            seen_srcs = set()
            for src in imgs[:3]:
                if src.startswith('http') or src in seen_srcs:
                    continue
                seen_srcs.add(src)
                clean_title = page_title.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                img_tags.append(
                    f'\n    <image:image>'
                    f'\n      <image:loc>https://bojinfacetension.com/{src.lstrip("/")}</image:loc>'
                    f'\n      <image:title>{clean_title}</image:title>'
                    f'\n    </image:image>'
                )
            if img_tags:
                sm = sm[:end_url] + ''.join(img_tags) + '\n  ' + sm[end_url:]
                img_added += 1

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sm)

print(f'[OK] Black Tech 4 (Audio Guide) & Black Tech 5 (Pinterest Save + {img_added} Sitemap Image blocks) deployed!')
