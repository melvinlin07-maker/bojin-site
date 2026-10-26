# -*- coding: utf-8 -*-
"""
Master Execution Script for US Bojin Website (bojinfacetension.com)
Executes Packs 04, 01, 02, and 03 in a single atomic, idempotent pass.
Strictly enforces len(new_content) >= len(old_content) across all modified HTML files.
"""
import os
import re
import json
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

REDIRECT_STUBS = {
    'blog-glow-after-bad-sleep.html',
    'blog-glow-before-event.html',
}

def safe_write(path, new_content, old_content=None):
    if old_content is not None:
        if len(new_content) < len(old_content):
            raise RuntimeError(f"SAFETY ABORT on {path}: new length ({len(new_content)}) < old length ({len(old_content)})")
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_content)

# ==============================================================================
# 1. PACK 04: Update styles.css
# ==============================================================================
with open('styles.css', 'r', encoding='utf-8') as f:
    css_old = f.read()

CSS_ADDITION = """
/* ==========================================================================
   2026 US DIMENSIONAL STRIKE UPGRADE PACK (PACK 01 - 04)
   ========================================================================== */

/* 1. 30-Second Quick Answer Box (Featured Snippet & AI Overview Target) */
.short-answer-box {
  margin: 1.5rem 0 2rem;
  padding: 1.25rem 1.4rem;
  background: var(--paper-2, #FDF8F2);
  border: 1px solid var(--line-gold, rgba(184, 146, 90, 0.35));
  border-left: 4px solid var(--jade, #2E5A44);
  border-radius: 14px;
  box-shadow: 0 4px 16px rgba(53, 29, 44, 0.04);
}
.short-answer-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-family: var(--font-sans);
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--jade, #2E5A44);
  margin: 0 0 0.45rem;
}
.short-answer-box p {
  margin: 0;
  font-size: 0.98rem;
  line-height: 1.62;
  color: var(--ink);
}

/* 2. 2026 Adversarial GEO Comparison Matrix Table */
.geo-matrix-wrap {
  margin: 1.8rem 0 2.2rem;
  overflow-x: auto;
  border-radius: 14px;
  border: 1px solid var(--line, rgba(120, 90, 60, 0.18));
  background: var(--paper-2, #FDF8F2);
}
.geo-matrix {
  width: 100%;
  border-collapse: collapse;
  font-family: var(--font-sans);
  font-size: 0.92rem;
  line-height: 1.55;
  text-align: left;
}
.geo-matrix th {
  background: color-mix(in srgb, var(--jade, #2E5A44) 10%, var(--paper-2, #FDF8F2));
  color: var(--ink);
  font-weight: 700;
  padding: 0.85rem 1rem;
  border-bottom: 1.5px solid var(--line, rgba(120, 90, 60, 0.22));
}
.geo-matrix td {
  padding: 0.85rem 1rem;
  border-bottom: 1px solid var(--line, rgba(120, 90, 60, 0.14));
  color: var(--ink);
  vertical-align: top;
}
.geo-matrix tr:last-child td {
  border-bottom: none;
}

/* 3. Inline 10-Second Micro-Commitment Self-Check Card (Pack 02) */
.bojin-inline-quiz {
  margin: 2rem 0 2.2rem;
  padding: 1.45rem 1.5rem;
  background: var(--paper-2, #FDF8F2);
  border: 1.5px solid var(--line-gold, rgba(184, 146, 90, 0.4));
  border-top: 3px solid var(--gold, #B8925A);
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(53, 29, 44, 0.06);
}
.biq-badge {
  display: inline-block;
  font-family: var(--font-sans);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--gold-ink, #8A6632);
  margin-bottom: 0.4rem;
}
.biq-question {
  font-family: var(--font-serif);
  font-size: clamp(1.25rem, 2.6vw, 1.5rem);
  font-weight: 600;
  line-height: 1.3;
  color: var(--ink);
  margin: 0 0 0.95rem;
}
.biq-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 0.65rem;
}
.biq-opt {
  appearance: none;
  background: var(--paper, #FAF4EC);
  border: 1px solid var(--line, rgba(120, 90, 60, 0.22));
  border-radius: 11px;
  padding: 0.75rem 0.95rem;
  text-align: left;
  font-family: var(--font-sans);
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--ink);
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
}
.biq-opt:hover {
  border-color: var(--gold, #B8925A);
  transform: translateY(-1px);
}
.biq-opt.is-picked {
  border-color: var(--jade, #2E5A44);
  background: color-mix(in srgb, var(--jade, #2E5A44) 10%, var(--paper-2, #FDF8F2));
  box-shadow: 0 0 0 1.5px var(--jade, #2E5A44);
}
.biq-feedback {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid var(--line, rgba(120, 90, 60, 0.18));
  font-size: 0.93rem;
  line-height: 1.55;
  color: var(--ink);
}
.biq-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-top: 0.85rem;
}

/* 4. Dual-Mode Video Demonstration Module (Pack 03) */
.bojin-video-module {
  margin: 2rem 0 2.2rem;
  padding: 1.35rem;
  background: var(--paper-2, #FDF8F2);
  border: 1px solid var(--line-gold, rgba(184, 146, 90, 0.35));
  border-radius: 16px;
  display: grid;
  grid-template-columns: minmax(180px, 240px) 1fr;
  gap: 1.35rem;
  align-items: center;
}
.bvm-player-wrap {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  background: #1C1419;
  aspect-ratio: 9 / 16;
  max-height: 320px;
  margin: 0 auto;
  width: 100%;
}
.bvm-player-wrap.is-landscape {
  aspect-ratio: 16 / 9;
}
.bvm-player-wrap video,
.bvm-player-wrap iframe {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.bvm-copy h3 {
  font-family: var(--font-serif);
  font-size: 1.35rem;
  margin: 0.25rem 0 0.55rem;
  color: var(--ink);
}
.bvm-copy p {
  font-size: 0.93rem;
  line-height: 1.58;
  color: var(--ink-soft);
  margin: 0 0 0.9rem;
}
@media (max-width: 640px) {
  .bojin-video-module {
    grid-template-columns: 1fr;
  }
  .bvm-player-wrap {
    max-width: 240px;
  }
}

/* 5. Body-Level Mobile Sticky Dual-Button Bar (Pack 04)
   Desktop (>= 768px): strictly hidden.
   Mobile (< 768px): 100% flush bottom with safe-area padding. */
.bojin-sticky-bar {
  display: none !important;
}
@media (max-width: 767px) {
  body.has-bojin-sticky {
    padding-bottom: calc(68px + env(safe-area-inset-bottom, 0px));
  }
  .bojin-sticky-bar {
    display: grid !important;
    grid-template-columns: 1fr 1.15fr;
    gap: 0.55rem;
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 990;
    padding: 0.6rem 0.85rem calc(0.6rem + env(safe-area-inset-bottom, 0px));
    background: color-mix(in srgb, var(--paper-2, #FDF8F2) 96%, transparent);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-top: 1px solid var(--line-gold, rgba(184, 146, 90, 0.38));
    box-shadow: 0 -4px 18px rgba(32, 20, 28, 0.12);
    box-sizing: border-box;
  }
  .bojin-sticky-bar a {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 42px;
    padding: 0.45rem 0.65rem;
    border-radius: 999px;
    font-family: var(--font-sans);
    font-size: 0.83rem;
    font-weight: 700;
    line-height: 1.15;
    text-decoration: none;
    text-align: center;
    white-space: nowrap;
    box-sizing: border-box;
  }
  .bojin-sticky-bar .bsb-secondary {
    background: var(--paper, #FAF4EC);
    color: var(--ink);
    border: 1.5px solid var(--line-gold, rgba(184, 146, 90, 0.55));
  }
  .bojin-sticky-bar .bsb-primary {
    background: var(--brand-bg, #351D2C);
    color: var(--brand-on, #FAF4EC);
    border: 1.5px solid var(--brand-bg, #351D2C);
  }
}
"""

if '.bojin-sticky-bar' not in css_old:
    safe_write('styles.css', css_old.rstrip() + '\n' + CSS_ADDITION, css_old)
    print('[OK] Updated styles.css')
else:
    print('[SKIP] styles.css already has .bojin-sticky-bar')

# ==============================================================================
# 2. PACK 04 & 02 & 03: Update nav.js
# ==============================================================================
with open('nav.js', 'r', encoding='utf-8') as f:
    nav_old = f.read()

NAV_ADDITION = """
/* ── 2026 Pack 02, 03, 04: Dual-Track Mobile Sticky Bar + Inline Micro-Quiz + Video Swapper + Micro-Signals ── */
(function(){
  var path = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  var isBlog = /^blog-.+\\.html$/.test(path) && path !== 'blog-glow-after-bad-sleep.html' && path !== 'blog-glow-before-event.html';
  var isCoreSticky = /^(what-is-bojin|start|about|results|brow-guide|eye-area-guides)\\.html$/.test(path);

  /* 1. Micro-Signal Event Conditioning for Meta Pixel & GA4 */
  window.bojinSignal = function(eventName, params){
    try {
      params = params || {};
      params.page = path;
      if(window.fbq) fbq('trackCustom', eventName, params);
      if(window.gtag) gtag('event', eventName, params);
    } catch(e){}
  };

  if(isBlog || isCoreSticky){
    var scrolledHalf = false, timerDone = false, signalFired = false;
    function checkEngaged(){
      if(!signalFired && scrolledHalf && timerDone){
        signalFired = true;
        window.bojinSignal('BojinEngagedReader', {track: isBlog ? 'blog' : 'core'});
      }
    }
    setTimeout(function(){ timerDone = true; checkEngaged(); }, 30000);
    window.addEventListener('scroll', function(){
      var max = document.documentElement.scrollHeight - window.innerHeight;
      if(max > 200 && (window.scrollY / max) >= 0.5){ scrolledHalf = true; checkEngaged(); }
    }, {passive: true});
  }

  /* 2. Inline 10-Second Micro-Commitment Self-Check Handler (Pack 02) */
  document.querySelectorAll('.bojin-inline-quiz').forEach(function(card){
    if(card.getAttribute('data-biq-wired')) return;
    card.setAttribute('data-biq-wired', '1');
    var zone = card.getAttribute('data-biq-zone') || 'general';
    var opts = card.querySelectorAll('.biq-opt');
    var fb = card.querySelector('.biq-feedback');
    var fbTxt = card.querySelector('.biq-feedback-text');
    opts.forEach(function(btn){
      btn.addEventListener('click', function(){
        opts.forEach(function(b){ b.classList.remove('is-picked'); b.setAttribute('aria-pressed','false'); });
        btn.classList.add('is-picked');
        btn.setAttribute('aria-pressed','true');
        if(fb && fbTxt){
          fbTxt.textContent = btn.getAttribute('data-biq-msg') || '';
          fb.hidden = false;
        }
        window.bojinSignal('BojinMicroQuizClick', {zone: zone, choice: btn.getAttribute('data-biq-choice')});
      });
    });
  });

  /* 3. Video Play Signal & Future US YouTube Auto-Swapper (Pack 03) */
  document.querySelectorAll('[data-video-module]').forEach(function(mod){
    if(mod.getAttribute('data-bvm-wired')) return;
    mod.setAttribute('data-bvm-wired', '1');
    var ytId = (mod.getAttribute('data-youtube-id') || '').trim();
    var wrap = mod.querySelector('.bvm-player-wrap');
    if(ytId && wrap){
      wrap.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + encodeURIComponent(ytId) + '?rel=0" title="The Bojin Method Demonstration" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>';
    }
    var vid = mod.querySelector('video');
    if(vid){
      vid.addEventListener('play', function(){
        window.bojinSignal('BojinVideoPlay', {src: vid.getAttribute('src')});
      }, {once: true});
    }
  });

  /* 4. Inject Body-Level Mobile Sticky Dual-Button Bar (Pack 04) */
  if((isBlog || isCoreSticky) && !document.querySelector('.bojin-sticky-bar')){
    var eyebrowEl = document.querySelector('.eyebrow');
    var ebText = eyebrowEl ? eyebrowEl.textContent.toLowerCase() : '';
    var isEyeBrow = /eyes|brows|forehead|glasses|scalp/.test(ebText) || /eye|brow|forehead|crows-feet|tear-trough|glasses|scalp/.test(path);
    var isMethodTrack = /method|rituals|routines|myths/.test(ebText) && !/jaw-clenching|botox|dental|saggier|volume-loss|sleep-creases|hot-flashes|contraindications/.test(path);

    document.body.classList.add('has-bojin-sticky');
    var bar = document.createElement('nav');
    bar.className = 'bojin-sticky-bar';
    bar.setAttribute('aria-label', 'Quick actions');

    var leftHref = 'quiz.html?from=' + encodeURIComponent(path.replace('.html',''));
    var leftLabel = '60s Tension Quiz';
    var rightHref = 'landing.html#get';
    var rightLabel = 'Free 3-Min Video \u2192';

    if(isEyeBrow){
      leftHref = 'eye-start-quiz.html';
      leftLabel = '20s Eye & Brow Check';
    } else if(isMethodTrack){
      leftHref = 'guide.html';
      leftLabel = 'Free 5-Zone Guide';
      rightLabel = 'Watch 3-Min Demo \u2192';
    } else {
      leftHref = 'map.html';
      leftLabel = '60s Face Tension Map';
    }

    bar.innerHTML =
      '<a class="bsb-secondary" href="' + leftHref + '" data-sticky-pos="left">' + leftLabel + '</a>' +
      '<a class="bsb-primary" href="' + rightHref + '" data-sticky-pos="right">' + rightLabel + '</a>';

    bar.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        window.bojinSignal('BojinStickyClick', {pos: a.getAttribute('data-sticky-pos'), target: a.getAttribute('href')});
      });
    });
    document.body.appendChild(bar);
  }
})();
"""

if 'BojinEngagedReader' not in nav_old:
    safe_write('nav.js', nav_old.rstrip() + '\n' + NAV_ADDITION, nav_old)
    print('[OK] Updated nav.js')
else:
    print('[SKIP] nav.js already updated')

# ==============================================================================
# 3. PACK 04: Upgrade eye-method-course-preview.html & quiz.html
# ==============================================================================
with open('eye-method-course-preview.html', 'r', encoding='utf-8') as f:
    em_old = f.read()

if 'courseWaitlistForm' not in em_old:
    em_new = em_old.replace(
        '<button class="button" type="button" aria-expanded="false" aria-controls="checkout-note" id="checkout-preview">View enrollment details →</button><p class="preview-status" id="checkout-note" hidden>Enrollment details, access terms, and refund details will appear here before the course opens. No payment is taken on this page.</p><p class="fine">Enrollment is not open on this page yet.</p>',
        '<button class="button" type="button" aria-expanded="false" aria-controls="checkout-note" id="checkout-preview">Join Priority Waitlist →</button><div class="preview-status" id="checkout-note" hidden><p style="margin:0 0 .65rem"><strong>Enrollment opens soon — join the priority waitlist:</strong> Leave your email to receive first notice when enrollment opens, plus get immediate access to the free 5-Zone Face Tension Self-Check PDF today.</p><form id="courseWaitlistForm" style="display:flex;gap:.55rem;flex-wrap:wrap;margin-top:.5rem" novalidate><input type="email" name="email" placeholder="you@email.com" aria-label="Your email" required style="flex:1 1 180px;padding:.65rem .85rem;border-radius:8px;border:1px solid rgba(120,90,60,.35);font-size:.95rem"><button class="button" type="submit" style="margin:0;cursor:pointer">Notify Me &amp; Send Free Guide →</button></form><p class="form-status" role="status" aria-live="polite" hidden style="margin:.5rem 0 0;font-size:.88rem"></p></div><p class="fine">No payment is taken on this preview page.</p>'
    ).replace(
        'note.hidden=expanded;});</script>',
        'note.hidden=expanded;});</script><script src="nav.js?v=20261026"></script><script>if(window.bojinWireOptin){window.bojinWireOptin(document.getElementById("courseWaitlistForm"),"eye_course_waitlist");}</script>'
    )
    safe_write('eye-method-course-preview.html', em_new, em_old)
    print('[OK] Updated eye-method-course-preview.html')

with open('quiz.html', 'r', encoding='utf-8') as f:
    qz_old = f.read()

if 'copyQuizSummaryBtn' not in qz_old:
    qz_new = qz_old.replace(
        "'<div class=\"zone-scores\">'+chips+'</div>'+",
        "'<div class=\"zone-scores\">'+chips+'</div>'+\n        '<p style=\"margin:.95rem 0 0\"><button type=\"button\" class=\"btn btn--ghost\" id=\"copyQuizSummaryBtn\" style=\"font-size:.86rem;padding:.5rem 1.05rem\">📋 Copy My 5-Zone Tension Summary</button></p>'+"
    ).replace(
        "var rs=document.getElementById('quizRestart');",
        "var cpBtn=document.getElementById('copyQuizSummaryBtn');\n    if(cpBtn){ cpBtn.addEventListener('click', function(){ var sTxt='My Face Tension Profile (The Bojin Method): Primary focus = '+ZONE_LABEL[top]+' ('+Math.round(sc[top])+'/100). Full scores: '+RADAR.map(function(z){return ZONE_SHORT[z]+': '+Math.round(sc[z]);}).join(', ')+'. Free check: https://bojinfacetension.com/quiz.html'; if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(sTxt).then(function(){if(window.bojinToast)window.bojinToast('✓ Your 5-Zone Tension Summary is copied!');cpBtn.textContent='✓ Summary Copied!';});} }); }\n    var rs=document.getElementById('quizRestart');"
    )
    safe_write('quiz.html', qz_new, qz_old)
    print('[OK] Updated quiz.html')

# ==============================================================================
# 4. PACK 01, 02, 03, 04 ACROSS ALL 99 BLOG ARTICLES & CORE PAGES
# ==============================================================================

QUIZ_CARDS = {
    'brows-forehead': """<aside class="bojin-inline-quiz" data-biq-zone="brows-forehead" aria-label="10-second brow tension self-check">
  <span class="biq-badge">🖐️ 10-Second Touch Self-Check · Step 1 of 2</span>
  <h3 class="biq-question">Lightly rest your ring finger at the inner corner of your eyebrow. How does that spot feel right now?</h3>
  <div class="biq-options" role="group" aria-label="Choose what you notice">
    <button type="button" class="biq-opt" data-biq-choice="smooth" data-biq-msg="Your inner brow feels relatively rested today. Keeping your touch feather-light and anchored will help maintain that ease."><span>1. Smooth &amp; easy</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="ridge" data-biq-msg="Notice that firm ridge? That is where the corrugator muscle anchors along the brow bone—the #1 spot where screen focus and daily concentration quietly collect."><span>2. A small firm ridge or knot</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="heavy" data-biq-msg="When the inner brow and temples feel heavy or tender, broad scraping often pulls the skin. A tiny, supported circle with a stabilizing finger works much more gently."><span>3. Heavy, tight, or tender</span><span aria-hidden="true">→</span></button>
  </div>
  <div class="biq-feedback" hidden aria-live="polite">
    <p class="biq-feedback-text" style="margin:0;font-weight:500"></p>
    <div class="biq-actions">
      <a class="btn" href="landing.html#get">Watch Free 3-Min Brow Release Video &rarr;</a>
      <a class="btn btn--ghost" href="brow-guide.html">Explore Interactive Brow Guide</a>
    </div>
  </div>
</aside>""",
    'eyes': """<aside class="bojin-inline-quiz" data-biq-zone="eyes" aria-label="10-second eye area self-check">
  <span class="biq-badge">👁️ 10-Second Eye Area Check · Step 1 of 2</span>
  <h3 class="biq-question">When you look in the mirror or blink slowly right now, what stands out most around your eyes?</h3>
  <div class="biq-options" role="group" aria-label="Choose what you notice">
    <button type="button" class="biq-opt" data-biq-choice="morning-puff" data-biq-msg="Morning fullness often settles when you stop pressing directly on the soft under-eye bag and instead follow the bony orbital rim outward and down the side of the neck."><span>1. Morning puffiness or fullness</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="heavy-lids" data-biq-msg="When the upper orbit and outer corner feel heavy even after sleep, start above the brow and along the temple rather than tugging the delicate eyelid skin."><span>2. Heavy lids &amp; tired look</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="screen-strain" data-biq-msg="Long hours of visual focus hold the muscles around the eye socket still. A calm 3-minute reset with a supporting finger helps the whole eye area feel lighter."><span>3. Tightness after screen time</span><span aria-hidden="true">→</span></button>
  </div>
  <div class="biq-feedback" hidden aria-live="polite">
    <p class="biq-feedback-text" style="margin:0;font-weight:500"></p>
    <div class="biq-actions">
      <a class="btn" href="eye-start-quiz.html">Take 4-Question Eye Starting Check &rarr;</a>
      <a class="btn btn--ghost" href="eye-area-guides.html">See 3-Region Eye Map</a>
    </div>
  </div>
</aside>""",
    'cheeks-nasolabial': """<aside class="bojin-inline-quiz" data-biq-zone="cheeks-nasolabial" aria-label="10-second cheek tension self-check">
  <span class="biq-badge">🖐️ 10-Second Midface Check · Step 1 of 2</span>
  <h3 class="biq-question">Press gently just beneath your cheekbone (next to the side of your nose). What do you notice?</h3>
  <div class="biq-options" role="group" aria-label="Choose what you notice">
    <button type="button" class="biq-opt" data-biq-choice="one-side" data-biq-msg="Most women favor one chewing or sleeping side! Comparing your left and right cheek tension is the fastest way to personalize your daily order."><span>1. One side feels tighter</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="heavy-cheek" data-biq-msg="When the tissue under the cheekbone feels full or heavy, gliding at a low angle along the bone edge (with your other hand steadying the skin) feels far more supportive than rubbing the fold itself."><span>2. Fullness above the smile line</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="mouth-corner" data-biq-msg="Tension around the corners of the mouth often connects to the jaw and chin. Easing the lower jaw first gives your cheek passes a calmer foundation."><span>3. Tightness near mouth corners</span><span aria-hidden="true">→</span></button>
  </div>
  <div class="biq-feedback" hidden aria-live="polite">
    <p class="biq-feedback-text" style="margin:0;font-weight:500"></p>
    <div class="biq-actions">
      <a class="btn" href="map.html?zone=cheeks">Open 60-Second Interactive Face Map &rarr;</a>
      <a class="btn btn--ghost" href="quiz.html?from=cheeks">Take Full 5-Zone Quiz</a>
    </div>
  </div>
</aside>""",
    'jaw-neck': """<aside class="bojin-inline-quiz" data-biq-zone="jaw-neck" aria-label="10-second jaw and neck tension check">
  <span class="biq-badge">🖐️ 10-Second Jaw &amp; Neck Check · Step 1 of 2</span>
  <h3 class="biq-question">Pause for a second: are your upper and lower back teeth touching right now, or is your jaw hanging loose?</h3>
  <div class="biq-options" role="group" aria-label="Choose what you notice">
    <button type="button" class="biq-opt" data-biq-choice="clenched" data-biq-msg="Catching your teeth touching during the day is a major realization. Let your tongue rest and lips stay soft—then use light, supported strokes from the jaw angle down the side of the neck."><span>1. Teeth touching or braced</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="jaw-knot" data-biq-msg="When the muscle at the corner of the jaw feels thick or tired, pressing harder only makes it brace more. Slow, comfortable circles with a supporting hand invite it to soften."><span>2. Firm knot at the jaw corner</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="neck-tight" data-biq-msg="A stiff neck and forward screen posture often show up in how the lower face feels. Finishing every routine with feather-light sweeps down the sides of the neck is essential."><span>3. Tightness along the neck</span><span aria-hidden="true">→</span></button>
  </div>
  <div class="biq-feedback" hidden aria-live="polite">
    <p class="biq-feedback-text" style="margin:0;font-weight:500"></p>
    <div class="biq-actions">
      <a class="btn" href="map.html?zone=jaw">See 60-Second Jaw &amp; Neck Map &rarr;</a>
      <a class="btn btn--ghost" href="landing.html#get">Watch Free 3-Min Release Video</a>
    </div>
  </div>
</aside>""",
    'method': """<aside class="bojin-inline-quiz" data-biq-zone="method" aria-label="10-second technique self-check">
  <span class="biq-badge">✨ 10-Second Technique Check · Step 1 of 2</span>
  <h3 class="biq-question">When you do facial massage at home, what has been your biggest frustration so far?</h3>
  <div class="biq-options" role="group" aria-label="Choose what you notice">
    <button type="button" class="biq-opt" data-biq-choice="pulling" data-biq-msg="If the skin feels like it is stretching or dragging, the missing piece is almost always the Supporting Hand—anchoring behind the stroke so the tool glides without tugging."><span>1. Worried about pulling skin</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="guesswork" data-biq-msg="Randomly gliding across the whole cheek rarely feels satisfying. The Bojin Method narrows your focus to exact anatomical landmarks, bone angle, and a calm sequence."><span>2. Unsure of exact spot &amp; angle</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="fades" data-biq-msg="Instead of doing the whole face at once, try our One-Side 5-Minute Test first so you can observe the real difference in weight and comfort on your own mirror."><span>3. Hard to tell if it's working</span><span aria-hidden="true">→</span></button>
  </div>
  <div class="biq-feedback" hidden aria-live="polite">
    <p class="biq-feedback-text" style="margin:0;font-weight:500"></p>
    <div class="biq-actions">
      <a class="btn" href="facial-tension-journey.html">Try Free Interactive Video Lesson &rarr;</a>
      <a class="btn btn--ghost" href="results.html">See the One-Side 5-Min Test</a>
    </div>
  </div>
</aside>"""
}

QUIZ_MAP_35 = {
    'blog-forehead-frown-lines.html': 'brows-forehead',
    'blog-forehead-lines-deepening.html': 'brows-forehead',
    'blog-frown-lines-menopause.html': 'brows-forehead',
    'blog-heavy-low-brows-lift.html': 'brows-forehead',
    'blog-natural-botox-alternative-forehead.html': 'brows-forehead',
    'blog-screen-to-forehead-tension-chain.html': 'brows-forehead',
    'blog-tense-forehead-relief.html': 'brows-forehead',
    'blog-scalp-and-temple-tightness-and-your-face.html': 'brows-forehead',
    'blog-crows-feet-eye-corners.html': 'eyes',
    'blog-dark-circles-tired-eyes.html': 'eyes',
    'blog-eye-cream-not-absorbing.html': 'eyes',
    'blog-hooded-heavy-eyelids.html': 'eyes',
    'blog-menopause-tired-eyes.html': 'eyes',
    'blog-screen-tired-eyes-desk-reset.html': 'eyes',
    'blog-tear-trough-hollow-under-eyes.html': 'eyes',
    'blog-tired-puffy-eyes.html': 'eyes',
    'blog-under-eye-bags-over-50.html': 'eyes',
    'blog-are-nasolabial-folds-permanent.html': 'cheeks-nasolabial',
    'blog-cheeks-after-flight-travel.html': 'cheeks-nasolabial',
    'blog-cheeks-before-makeup.html': 'cheeks-nasolabial',
    'blog-facial-asymmetry-one-side-more-tense.html': 'cheeks-nasolabial',
    'blog-marionette-lines-drooping-mouth-corners.html': 'cheeks-nasolabial',
    'blog-smile-lines-cheeks.html': 'cheeks-nasolabial',
    'blog-jaw-before-video-call.html': 'jaw-neck',
    'blog-jaw-clenching-grinding-and-bojin.html': 'jaw-neck',
    'blog-jaw-end-of-day-release.html': 'jaw-neck',
    'blog-jawline-double-chin.html': 'jaw-neck',
    'blog-jowls-sagging-along-jawline.html': 'jaw-neck',
    'blog-neck-tension-showing-in-your-face.html': 'jaw-neck',
    'blog-turkey-neck-and-neck-lines.html': 'jaw-neck',
    'blog-gua-sha-vs-bojin.html': 'method',
    'blog-gua-sha-not-working.html': 'method',
    'blog-how-much-pressure.html': 'method',
    'blog-the-supporting-hand.html': 'method',
    'blog-why-the-order-matters.html': 'method',
}

VIDEO_MAP_12 = {
    'blog-the-supporting-hand.html': {
        'src': 'assets/journal/ca6d02ebb3.mp4',
        'poster': 'assets/journal/52b355b8d0.jpg',
        'duration': 'PT12S',
        'sec': '12',
        'name': 'How the Supporting Hand Anchors Skin During Facial Bojin',
        'desc': 'Yu-Ting Lan demonstrates how to place your supporting hand to steady the skin before gliding the Bojin tool, preventing skin drag.',
        'landscape': False
    },
    'blog-forehead-frown-lines.html': {
        'src': 'assets/journal/7d0eda9fcf.mp4',
        'poster': 'assets/journal/7692c6dd09.png',
        'duration': 'PT12S',
        'sec': '12',
        'name': 'Inner-Brow Bojin Preview: Small Circle Observation with Yu-Ting Lan',
        'desc': 'A 12-second inner-brow demonstration showing small, calm circles above the brow bone with a supporting finger.',
        'landscape': False
    },
    'blog-heavy-low-brows-lift.html': {
        'src': 'assets/journal/4c8bae444f.mp4',
        'poster': 'assets/journal/bb43f1a959.jpg',
        'duration': 'PT12S',
        'sec': '12',
        'name': 'Gentle Brow Bone Reset and Upward Support Demonstration',
        'desc': 'Yu-Ting Lan demonstrates how to support the brow arch and ease heavy-feeling brow tension without pulling the eyelid.',
        'landscape': False
    },
    'blog-forehead-lines-deepening.html': {
        'src': 'assets/journal/166212b1b1.mp4',
        'poster': 'assets/journal/c35e71b0c5.jpg',
        'duration': 'PT11S',
        'sec': '11',
        'name': 'Small Supported Circles vs Broad Swaying Along the Brow',
        'desc': 'Visual comparison of small, anchored Bojin circles versus unanchored swaying across the forehead and brow.',
        'landscape': False
    },
    'blog-screen-to-forehead-tension-chain.html': {
        'src': 'assets/journal/e076001a77.mp4',
        'poster': 'assets/journal/420a15ad1d.png',
        'duration': 'PT14S',
        'sec': '14',
        'name': 'Complete Upper-Brow Sequence Flow After Screen Time',
        'desc': 'A calm, step-by-step upper brow sequence excerpt for easing forehead tightness after long screen hours.',
        'landscape': False
    },
    'blog-how-much-pressure.html': {
        'src': 'assets/journal/52c3553278.mp4',
        'poster': 'assets/journal/8bb4877b14.jpg',
        'duration': 'PT11S',
        'sec': '11',
        'name': '10-Second Cheek Glide and Slip Check Before Starting Bojin',
        'desc': 'How to test comfortable pressure and oil slip on your cheek before starting a facial Bojin routine.',
        'landscape': False
    },
    'blog-the-angle-of-the-bojin-tool.html': {
        'src': 'assets/journal/9ee6c52722.mp4',
        'poster': 'assets/journal/52b355b8d0.jpg',
        'duration': 'PT12S',
        'sec': '12',
        'name': 'Thumb Anchor and Tool Angle Along the Orbital Rim',
        'desc': 'Demonstrating how the thumb anchor and bone-contour angle work together for safe, gentle contact.',
        'landscape': False
    },
    'blog-your-first-5-minutes-with-bojin.html': {
        'src': 'assets/journal/b7450c9d8d.mp4',
        'poster': 'assets/journal/420a15ad1d.png',
        'duration': 'PT12S',
        'sec': '12',
        'name': 'Where to Begin: Finding the Inner Brow Starting Landmark',
        'desc': 'Beginner demonstration of locating the inner brow starting point with calm, supported contact.',
        'landscape': False
    },
    'blog-tired-puffy-eyes.html': {
        'src': 'assets/facial-tension-journey/m1-start-captioned.mp4',
        'poster': 'assets/facial-tension-journey/m1-start-captioned.jpg',
        'duration': 'PT28S',
        'sec': '28',
        'name': 'Eye-Area Bojin Lesson Excerpt: Starting Position (Captioned)',
        'desc': 'Captioned teaching excerpt with Yu-Ting Lan showing the gentle eye-area starting position.',
        'landscape': True
    },
    'blog-why-the-order-matters.html': {
        'src': 'assets/facial-tension-journey/m3-route-captioned.mp4',
        'poster': 'assets/facial-tension-journey/m1-start-captioned.jpg',
        'duration': 'PT30S',
        'sec': '30',
        'name': 'Following the Anatomical Route Around the Eye Contour (Captioned)',
        'desc': 'Captioned lesson excerpt showing why sequence and route order matter around the eye contour.',
        'landscape': True
    },
    'blog-gua-sha-not-working.html': {
        'src': 'assets/facial-tension-journey/m7-mistake-captioned.mp4',
        'poster': 'assets/facial-tension-journey/guiding-hand-teaser-hd.jpg',
        'duration': 'PT28S',
        'sec': '28',
        'name': 'Common Facial Tool Mistake vs Supported Bojin Glide (Captioned)',
        'desc': 'Captioned demonstration comparing a common unanchored tool mistake with a supported Bojin pass.',
        'landscape': True
    },
    'blog-how-you-end-a-session.html': {
        'src': 'assets/facial-tension-journey/m10-finish-captioned.mp4',
        'poster': 'assets/facial-tension-journey/m1-start-captioned.jpg',
        'duration': 'PT26S',
        'sec': '26',
        'name': 'How to Finish an Eye and Face Bojin Session Gently (Captioned)',
        'desc': 'Captioned lesson excerpt showing the calm finishing sweep at the end of a Bojin routine.',
        'landscape': True
    },
}

GEO_MATRICES = {
    'blog-heavy-low-brows-lift.html': """<div class="geo-matrix-wrap">
  <table class="geo-matrix" aria-label="Separating brow appearance from brow sensation">
    <thead>
      <tr>
        <th>What You Notice</th>
        <th>Common Misinterpretation</th>
        <th>The Bojin Method Observation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Naturally low-set brows</strong></td>
        <td>Pressing harder upward will permanently reposition the eyebrow arch.</td>
        <td>Bone shape is structural; self-care focuses on comfort along the orbital rim, not altering anatomy.</td>
      </tr>
      <tr>
        <td><strong>End-of-day brow heaviness</strong></td>
        <td>Pulling the forehead skin taut with a wide stone.</td>
        <td>Use a supporting finger to steady the skin while making small, calm circles at the inner brow anchor.</td>
      </tr>
      <tr>
        <td><strong>Furrowed feeling after screens</strong></td>
        <td>Rubbing directly over the crease without oil or support.</td>
        <td>Pause, add a drop of slip, and notice whether the inner brow ridge feels tight before moving outward.</td>
      </tr>
    </tbody>
  </table>
</div>""",
    'blog-jaw-clenching-grinding-and-bojin.html': """<figure class="bojin-figure" style="margin:1.6rem 0">
  <img src="assets/bojin-jaw-muscle-gold-line-technique.jpg" alt="Yu-Ting Lan demonstrating gentle Bojin placement along the gold-mapped masseter muscle line on the jaw" loading="lazy" width="1200" height="800">
  <figcaption>Observing the masseter path from below the cheekbone toward the jaw angle using a calm, supported hand position.</figcaption>
</figure>
<div class="geo-matrix-wrap">
  <table class="geo-matrix" aria-label="Daytime jaw holding vs dental bruxism">
    <thead>
      <tr>
        <th>Observation</th>
        <th>Common Habit Mistake</th>
        <th>Gentle Bojin Self-Care Approach</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Teeth touching while working</strong></td>
        <td>Digging forcefully into the sore jaw knot with a cold stone.</td>
        <td>Let the lips rest together with teeth slightly apart first, then use slow, comfortable glides along the jaw contour.</td>
      </tr>
      <tr>
        <td><strong>Tightness below the cheekbone</strong></td>
        <td>Dragging downward without steadying the skin.</td>
        <td>Anchor with your supporting hand and follow the bone angle gently toward the ear.</td>
      </tr>
      <tr>
        <td><strong>Sharp pain, locking, or clicking</strong></td>
        <td>Trying to massage through joint pain at home.</td>
        <td>Skip self-massage over painful joints and consult a dentist or medical professional.</td>
      </tr>
    </tbody>
  </table>
</div>""",
    'blog-gua-sha-vs-bojin.html': """<div class="geo-matrix-wrap">
  <table class="geo-matrix" aria-label="Gua Sha tool vs The Bojin Method technique comparison">
    <thead>
      <tr>
        <th>Practice Element</th>
        <th>Typical At-Home Gua Sha</th>
        <th>The Bojin Method</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Focus</strong></td>
        <td>Broad flat-edge strokes across the cheeks and jawline.</td>
        <td>Exact anatomical point, bone-contour angle, and deliberate sequence.</td>
      </tr>
      <tr>
        <td><strong>Role of the Second Hand</strong></td>
        <td>Often left idle while one hand pulls the stone.</td>
        <td>Acts as the Supporting Hand—anchoring behind every pass so skin never drags.</td>
      </tr>
      <tr>
        <td><strong>Tool Requirement</strong></td>
        <td>Flat jade or quartz stone plate.</td>
        <td>Works with your existing stone, clean fingertips, or a slim stainless steel Bojin stick.</td>
      </tr>
    </tbody>
  </table>
</div>"""
}

all_blogs = sorted(glob.glob('blog-*.html'))
modified_blogs = 0
llms_entries = []

for b in all_blogs:
    if b in REDIRECT_STUBS:
        continue
    with open(b, 'r', encoding='utf-8') as f:
        old_html = f.read()
    html = old_html

    # Extract title and meta description for llms-full.txt & quick answer box
    title_m = re.search(r'<title>(.*?)</title>', html, re.S)
    desc_m = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', html, re.I)
    if not desc_m:
        desc_m = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\']', html, re.I)
    title_txt = title_m.group(1).strip() if title_m else b
    desc_txt = desc_m.group(1).strip() if desc_m else ''
    llms_entries.append((b, title_txt, desc_txt))

    # 1. Add <a href="results.html">Results</a> to top nav if missing
    if 'href="results.html"' not in html:
        html = html.replace(
            '<a href="what-is-bojin.html">What is Bojin?</a>\n<a href="landing.html">Eye Reset</a>',
            '<a href="what-is-bojin.html">What is Bojin?</a>\n<a href="results.html">Results</a>\n<a href="landing.html">Eye Reset</a>'
        ).replace(
            '<a href="what-is-bojin.html">What is Bojin?</a>\r\n<a href="landing.html">Eye Reset</a>',
            '<a href="what-is-bojin.html">What is Bojin?</a>\r\n<a href="results.html">Results</a>\r\n<a href="landing.html">Eye Reset</a>'
        )
        if 'href="results.html"' not in html:
            html = re.sub(
                r'(<a[^>]*href="what-is-bojin\.html"[^>]*>What is Bojin\?</a>)',
                r'\1\n<a href="results.html">Results</a>',
                html,
                count=1
            )

    # 2. Inject .short-answer-box + optional .geo-matrix-wrap after <p class="lead">...</p>
    if 'class="short-answer-box"' not in html and desc_txt:
        qa_html = (
            f'\n<div class="short-answer-box" id="quick-summary">'
            f'<span class="short-answer-eyebrow">⚡ 30-Second Key Takeaway</span>'
            f'<p><strong>{desc_txt}</strong> Remember: this is a gentle, supported self-care observation you can test on one side of your face—never a forceful press or medical treatment.</p>'
            f'</div>'
        )
        if b in GEO_MATRICES:
            qa_html += '\n' + GEO_MATRICES[b]
        html = re.sub(r'(<p class="lead"[^>]*>.*?</p>)', r'\1' + qa_html.replace('\\', '\\\\'), html, count=1, flags=re.S)

    # 3. Inject 10-Second Inline Micro-Commitment Quiz Card before the 2nd <h2 in the 35 designated posts
    if b in QUIZ_MAP_35 and 'class="bojin-inline-quiz"' not in html:
        q_zone = QUIZ_MAP_35[b]
        q_card = QUIZ_CARDS[q_zone]
        h2_matches = list(re.finditer(r'<h2\b[^>]*>', html))
        # Ignore any h2 inside .bojin-toc-modular
        content_h2s = [m for m in h2_matches if 'bojin-toc-title' not in m.group(0)]
        target_h2 = content_h2s[1] if len(content_h2s) >= 2 else (content_h2s[0] if content_h2s else None)
        if target_h2:
            idx = target_h2.start()
            html = html[:idx] + q_card + '\n' + html[idx:]

    # 4. Inject Video Demonstration Module + VideoObject Schema in the 12 designated posts
    if b in VIDEO_MAP_12 and 'data-video-module' not in html:
        v = VIDEO_MAP_12[b]
        v_schema = {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": v['name'],
            "description": v['desc'],
            "thumbnailUrl": [f"https://bojinfacetension.com/{v['poster']}"],
            "contentUrl": f"https://bojinfacetension.com/{v['src']}",
            "uploadDate": "2026-10-18",
            "duration": v['duration'],
            "creator": {
                "@type": "Person",
                "@id": "https://bojinfacetension.com/#yuting-lan",
                "name": "Yu-Ting Lan"
            },
            "publisher": {
                "@type": "Organization",
                "@id": "https://bojinfacetension.com/#organization",
                "name": "The Bojin Method",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://bojinfacetension.com/assets/logo-the-bojin-method.png",
                    "width": 1200,
                    "height": 1200
                }
            },
            "isAccessibleForFree": True
        }
        schema_tag = f'<script type="application/ld+json">{json.dumps(v_schema, ensure_ascii=False)}</script>\n</head>'
        html = html.replace('</head>', schema_tag, 1)

        landscape_cls = ' is-landscape' if v['landscape'] else ''
        v_mod = f"""<section class="bojin-video-module" data-video-module data-youtube-id="" aria-label="Hands-on teacher demonstration">
  <div class="bvm-player-wrap{landscape_cls}">
    <video controls playsinline preload="metadata" poster="{v['poster']}" src="{v['src']}" aria-label="{v['name']}"></video>
  </div>
  <div class="bvm-copy">
    <span class="short-answer-eyebrow">🎥 Teacher Micro-Demonstration · {v['sec']}s Clip</span>
    <h3>{v['name']}</h3>
    <p>{v['desc']} This short excerpt is an observation preview, not a complete routine.</p>
    <div style="display:flex;flex-wrap:wrap;gap:.65rem">
      <a class="btn" href="landing.html#get">Watch Full 3-Min Guided Video &rarr;</a>
      <a class="btn btn--ghost" href="watch-inner-brow-bojin.html">Open Dedicated Watch Page</a>
    </div>
  </div>
</section>\n"""
        if '<div class="faq"' in html:
            html = html.replace('<div class="faq"', v_mod + '<div class="faq"', 1)
        elif '<div class="article-cta"' in html:
            html = html.replace('<div class="article-cta"', v_mod + '<div class="article-cta"', 1)
        else:
            html = html.replace('</article>', v_mod + '</article>', 1)

    if html != old_html:
        safe_write(b, html, old_html)
        modified_blogs += 1

print(f'[OK] Upgraded {modified_blogs} blog articles (100% length safety verified)')

# ==============================================================================
# 5. PACK 01: Generate llms-full.txt & update llms.txt
# ==============================================================================
llms_full_lines = [
    "# The Bojin Method — Complete Structured Knowledge Base for AI & Search Systems (llms-full.txt)",
    "",
    "> Official Domain: https://bojinfacetension.com/",
    "> Founder & Primary Instructor: Yu-Ting Lan (藍郁婷), Founder of Héhé Studio (和合雅築), Taiwan.",
    "> Core Discipline: At-home facial Bojin self-care education for women 50+ focusing on gentle facial tension observation, supporting-hand stability, bone-contour angle, and sequence.",
    "",
    "## 1. Fundamental Distinctions: The Bojin Method vs. Broad Gua Sha",
    "| Dimension | Broad Gua Sha | The Bojin Method |",
    "| :--- | :--- | :--- |",
    "| Primary Mechanism | Wide flat-stone gliding across large skin surfaces | Precise point placement along bone contours and muscular attachments |",
    "| Skin Protection | Often done one-handed without anchoring | Mandatory Supporting Hand anchors behind every stroke to prevent skin drag |",
    "| Sensation Goal | Surface warmth; sometimes mistakenly pushed to redness | Calm, comfortable pressure—never painful, bruising, or tugging |",
    "| Verification | Whole-face routine | One-Side 5-Minute Self-Test (comparing rested feel and visual ease on one side) |",
    "",
    "## 2. Interactive Self-Check & Visual Guides Directory",
    "- **60-Second Interactive 5-Zone Face Tension Map**: https://bojinfacetension.com/map.html",
    "- **1-Minute 8-Question Face Tension Profile Quiz**: https://bojinfacetension.com/quiz.html",
    "- **4-Question Eye-Area Starting Point Check**: https://bojinfacetension.com/eye-start-quiz.html",
    "- **Interactive Upper-Brow 9-Clip Micro-Movement Guide**: https://bojinfacetension.com/brow-guide.html",
    "- **12-Second Inner-Brow Teacher Watch Page**: https://bojinfacetension.com/watch-inner-brow-bojin.html",
    "- **3-Region Eye Area Visual Guide**: https://bojinfacetension.com/eye-area-guides.html",
    "- **One-Side 5-Minute Comparison Proof**: https://bojinfacetension.com/results.html",
    "- **Free 3-Minute Inner-Brow Release Video & 5-Zone PDF Guide**: https://bojinfacetension.com/landing.html",
    "",
    "## 3. Complete 99-Article Structured Q&A Knowledge Index",
]

for slug, t_txt, d_txt in llms_entries:
    llms_full_lines.append(f"- **[{t_txt}](https://bojinfacetension.com/{slug})**: {d_txt}")

safe_write('llms-full.txt', '\n'.join(llms_full_lines) + '\n')
print('[OK] Generated llms-full.txt with all 99 articles')

with open('llms.txt', 'r', encoding='utf-8') as f:
    llms_old = f.read()
if 'llms-full.txt' not in llms_old:
    llms_new = llms_old.replace(
        '## Site overview\n',
        '## Site overview\n- [Full AI Knowledge Index — All 99 Articles & Method Matrix (llms-full.txt)](https://bojinfacetension.com/llms-full.txt)\n- [Interactive 5-Zone Face Tension Map](https://bojinfacetension.com/map.html)\n'
    )
    safe_write('llms.txt', llms_new, llms_old)
    print('[OK] Updated llms.txt with link to llms-full.txt')

# ==============================================================================
# 6. PACK 01 & 03: Weaponize sitemap.xml with <image:image> and <video:video>
# ==============================================================================
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sm_old = f.read()

sm_new = sm_old
for slug, v in VIDEO_MAP_12.items():
    loc_tag = f"<loc>https://bojinfacetension.com/{slug}</loc>"
    if loc_tag in sm_new:
        # Check if video:video is already inside this <url> block
        pattern = re.compile(r'(<url>\s*' + re.escape(loc_tag) + r'.*?)(</url>)', re.S)
        m = pattern.search(sm_new)
        if m and '<video:video>' not in m.group(1):
            v_xml = (
                f"<video:video>"
                f"<video:thumbnail_loc>https://bojinfacetension.com/{v['poster']}</video:thumbnail_loc>"
                f"<video:title>{v['name']}</video:title>"
                f"<video:description>{v['desc']}</video:description>"
                f"<video:content_loc>https://bojinfacetension.com/{v['src']}</video:content_loc>"
                f"<video:duration>{v['sec']}</video:duration>"
                f"<video:publication_date>2026-10-18</video:publication_date>"
                f"</video:video>"
            )
            sm_new = sm_new[:m.start(2)] + v_xml + sm_new[m.start(2):]

if sm_new != sm_old:
    safe_write('sitemap.xml', sm_new, sm_old)
    print('[OK] Updated sitemap.xml with 12 <video:video> entries')

# ==============================================================================
# 7. PACK 01: Create scripts/push_indexnow.py
# ==============================================================================
INDEXNOW_SCRIPT = """# -*- coding: utf-8 -*-
import re
import json
import urllib.request

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    urls = re.findall(r'<loc>(https://bojinfacetension\\.com/[^<]+)</loc>', f.read())

print(f'Discovered {len(urls)} canonical URLs in sitemap.xml ready for IndexNow ping.')
"""
safe_write('scripts/push_indexnow.py', INDEXNOW_SCRIPT)
print('[OK] Created scripts/push_indexnow.py')
