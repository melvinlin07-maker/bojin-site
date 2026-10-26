# -*- coding: utf-8 -*-
import os
import re

ROOT = r'c:\Users\user888\Documents\撥筋美國網站'

header_html = """  <header class="site-header">
    <nav class="nav" aria-label="Primary">
      <a class="brand" href="index.html"><svg class="mark" viewBox="0 0 120 70" aria-hidden="true" style="width:26px;height:16px;color:var(--jade)"><path d="M12 50 C 40 26, 82 20, 110 30 C 100 36, 58 38, 20 52 C 16 53, 12 52, 12 50 Z" fill="currentColor"/></svg><span>The Bojin Method</span></a>
      <div class="nav-links">
        <a href="index.html">Home</a>
        <a href="start.html">Begin here</a>
        <a href="about.html">About</a>
        <a href="what-is-bojin.html">What is Bojin?</a>
        <a href="results.html">Results</a>
        <a href="landing.html">Eye Reset</a>
        <a class="active" href="blog.html">Journal</a>
      </div>
      <button class="nav-toggle" data-nav-toggle type="button" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="1.8" fill="none" aria-hidden="true"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg></button>
      <div class="nav-cta">
        <button class="theme-toggle" data-theme-toggle aria-label="Toggle light or dark theme">◑</button>
        <a class="btn" href="landing.html#get">Free video</a>
      </div>
    </nav>
  </header>
"""

footer_html = """  <footer class="site-footer">
    <div class="wrap foot-inner">
      <a class="brand" href="index.html" style="color:var(--ink)"><svg class="mark" viewBox="0 0 120 70" aria-hidden="true" style="width:26px;height:16px;color:var(--jade)"><path d="M12 50 C 40 26, 82 20, 110 30 C 100 36, 58 38, 20 52 C 16 53, 12 52, 12 50 Z" fill="currentColor"/></svg><span>The Bojin Method</span></a>
      <p class="foot-note">A gentle, method-led face and neck release you can learn at home.</p>
      <nav class="foot-social" aria-label="Follow The Bojin Method">
        <a href="https://www.facebook.com/BojinFacialMethod" target="_blank" rel="noopener me" aria-label="The Bojin Method on Facebook"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.6h2.6l.4-3H13.5V8.4c0-.9.25-1.5 1.55-1.5h1.65V4.2C16.4 4.1 15.4 4 14.2 4c-2.5 0-4.2 1.5-4.2 4.3v2.1H7.4v3h2.6V21Z"/></svg></a>
        <a href="https://www.instagram.com/bojinfacialmethod" target="_blank" rel="noopener me" aria-label="The Bojin Method on Instagram"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><circle cx="12" cy="12" r="3.6"/><circle cx="17.2" cy="6.8" r="1" fill="currentColor" stroke="none"/></svg></a>
      </nav>
      <p class="foot-copy">© 2026 The Bojin Method · Yu-Ting Lan · Gentle self-care, not medical treatment.</p>
      <nav class="foot-legal" aria-label="Legal">
        <a href="privacy.html">Privacy Policy</a>
        <a href="terms.html">Terms of Service</a>
      </nav>
    </div>
  </footer>
  <script src="nav.js?v=20261026"></script>
</body>
</html>
"""

# 1. Transform shoulders-face-preview.html -> blog-when-your-shoulders-wont-drop.html
with open(os.path.join(ROOT, 'shoulders-face-preview.html'), 'r', encoding='utf-8') as f:
    s_raw = f.read()

s_art = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="canonical" href="https://bojinfacetension.com/blog-when-your-shoulders-wont-drop.html">
  <title>When Your Shoulders Won’t Drop, Your Face Can Feel Tired Too | The Bojin Method</title>
  <meta name="description" content="A quiet look at how a long day can leave your shoulders, neck, and jaw feeling held—and one gentle way to notice the pattern.">
  <link rel="stylesheet" href="styles.css?v=10">
</head>
<body>
{header_html}
  <main id="top">
    <article class="section">
      <div class="wrap wrap--narrow article reveal">
        <a class="backlink" href="blog.html">← All articles</a>
        <p class="eyebrow">Body Awareness · Face &amp; Neck</p>
        <h1>When Your Shoulders Won’t Drop, Your Face Can Feel Tired Too</h1>
        <p class="post-meta">By <b>Yu-Ting Lan</b>, from Taiwan · 4 min read</p>
        <p class="lead">You close the laptop, but your shoulders are still up near your ears. Your jaw feels set. Your face seems to be carrying a day you thought was over.</p>

        <div class="bojin-audio-bar" id="audio-guide-bar" data-audio-src="">
          <div class="bab-left">
            <button type="button" class="bab-play-btn" data-audio-guide-btn>🎧 Listen to 3-Min Audio Guide</button>
            <div class="bab-meta">
              <span class="bab-title">Shoulders tight from work? Listen while you rest your eyes</span>
              <span class="bab-sub">Spoken English overview · Gentle self-care walk-through</span>
            </div>
          </div>
        </div>

        <div class="short-answer-box" id="quick-summary">
          <span class="short-answer-eyebrow">⚡ 30-Second Key Takeaway</span>
          <p><strong>Shoulder, neck, and jaw tension work together as an interconnected chain.</strong> Start by noticing where your body is bracing and simply exhaling—you do not have to forcefully massage your face to begin easing the pattern.</p>
        </div>

        <figure class="bojin-figure" style="margin:2rem 0">
          <img src="assets/shoulders-face-card-01-anatomy-draft.png" alt="A woman at her desk with a subtle illustrated muscle overlay at one raised shoulder and the side of her neck" loading="lazy" width="1122" height="1402">
          <figcaption>The familiar end-of-day feeling: work stops, but the shoulders and jaw are still holding on.</figcaption>
        </figure>

        <p>Maybe it happens after hours at your desk, while driving, or trying to finish one last task before bed. At some point you notice your shoulders have crept upward. You lower them, and a minute later they are right back.</p>
        <p>Then you catch another detail: your teeth are touching, your jaw feels busy, or your brow is drawn together. It is easy to look in the mirror and decide your face simply looks older today. But before making that judgment, it may help to ask a smaller question: <em>What am I still holding?</em></p>

        <aside class="bojin-inline-quiz" id="inline-quiz-card" data-biq-zone="jaw-neck" aria-label="10-second posture and lower face observation">
          <span class="biq-badge">🖐️ 10-Second Lower Face Observation · Step 1 of 2</span>
          <h3 class="biq-question">Pause for a moment: are your back teeth touching right now, or is your jaw resting loose?</h3>
          <div class="biq-options" role="group" aria-label="Choose what you notice">
            <button type="button" class="biq-opt" data-biq-choice="clenched" data-biq-msg="Catching daytime clenching is a major breakthrough. Let your teeth part slightly and tongue rest—then use light, supported glides from jaw angle down the neck."><span>1. Teeth touching or braced</span><span aria-hidden="true">→</span></button>
            <button type="button" class="biq-opt" data-biq-choice="jaw-knot" data-biq-msg="When the muscle at the corner of the jaw feels thick or tired, pressing hard makes it brace more. Slow, comfortable passes with a supporting hand invite it to soften."><span>2. Firm knot at jaw corner</span><span aria-hidden="true">→</span></button>
            <button type="button" class="biq-opt" data-biq-choice="neck-tight" data-biq-msg="Forward head screen posture shows up in how the lower face feels. Finishing every routine with light downward sweeps along the side of the neck is essential."><span>3. Tightness along neck</span><span aria-hidden="true">→</span></button>
          </div>
          <div class="biq-feedback" hidden aria-live="polite">
            <p class="biq-feedback-text" style="margin:0;font-weight:500"></p>
            <div class="biq-actions">
              <a class="btn" href="map.html?zone=jaw">See 60-Second Jaw &amp; Neck Map &rarr;</a>
              <a class="btn btn--ghost" href="landing.html#get">Watch Free 3-Min Release Video</a>
            </div>
          </div>
        </aside>

        <h2>Look beyond the mirror for a moment</h2>
        <p>Your face does not work in isolation from the rest of your day. Concentration, screen time, stress, and ordinary habits can all change how you carry yourself. The shoulder and neck area may feel braced at the same time that your jaw feels set. That is a useful pattern to notice, even when you cannot identify one single cause.</p>

        <figure class="bojin-figure" style="margin:2rem 0">
          <img src="assets/shoulders-face-card-02-anatomy-draft.png" alt="Editorial close-up with a localized, semi-transparent illustration of shoulder and side-neck muscles" loading="lazy" width="1122" height="1402">
          <figcaption>A visual guide to the shoulder and neck connection. The illustration is educational, not a medical diagnosis.</figcaption>
        </figure>

        <div class="callout"><span class="callout-label">The key idea</span><p>Your face may be where you notice the day. Your shoulders and jaw can help you notice how you carried it.</p></div>

        <h2>A one-minute check-in</h2>
        <p>Try this without a tool. It is meant to help you notice what feels comfortable, not to force your shoulders into a rigid position.</p>
        <ol class="steps" style="padding-left:1.4rem;line-height:1.75">
          <li style="margin-bottom:0.75rem"><strong>Notice.</strong> Where are your shoulders right now? Let your arms rest and simply observe.</li>
          <li style="margin-bottom:0.75rem"><strong>Exhale.</strong> Take an easy breath out. Allow your shoulders to settle if they want to; there is no need to push them down.</li>
          <li style="margin-bottom:0.75rem"><strong>Soften your jaw.</strong> Check whether your teeth are touching. Let your lips rest together with space between your teeth.</li>
        </ol>

        <figure class="bojin-figure" style="margin:2rem 0">
          <img src="assets/shoulders-face-card-03-detail-draft.png" alt="Three numbered detail callouts for shoulder, exhale, and jaw softening" loading="lazy" width="1122" height="1402">
          <figcaption>Notice your shoulder, exhale, and check your jaw. Three places to observe in one moment.</figcaption>
        </figure>

        <div class="note-safety" id="safety-note"><b>Self-care, not medical care.</b> This article offers general self-care observations. If you have persistent pain, numbness, injury, or severe symptoms, seek appropriate medical advice.</div>
      </div>
    </article>
  </main>
{footer_html}
"""

with open(os.path.join(ROOT, 'blog-when-your-shoulders-wont-drop.html'), 'w', encoding='utf-8') as f:
    f.write(s_art)
print('[OK] Created blog-when-your-shoulders-wont-drop.html')

# 2. Transform after-cry-preview.html -> blog-after-you-cry-puffy-eyes-pause.html
c_art = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="canonical" href="https://bojinfacetension.com/blog-after-you-cry-puffy-eyes-pause.html">
  <title>After You Cry, Your Face May Need a Pause | The Bojin Method</title>
  <meta name="description" content="After crying, your eyes and face may feel puffy, tender, or unfamiliar. A gentle reminder to settle first and decide later whether your face needs anything at all.">
  <link rel="stylesheet" href="styles.css?v=10">
</head>
<body>
{header_html}
  <main id="top">
    <article class="section">
      <div class="wrap wrap--narrow article reveal">
        <a class="backlink" href="blog.html">← All articles</a>
        <p class="eyebrow">Emotional Days · Gentle Eye Care</p>
        <h1>After You Cry, Your Face May Need a Pause</h1>
        <p class="post-meta">By <b>Yu-Ting Lan</b>, from Taiwan · 4 min read</p>
        <p class="lead">You have already carried the feeling. Then you look in the mirror and see swollen eyes, flushed skin, and a face that does not quite feel like yours. You do not have to fix it right away.</p>

        <div class="bojin-audio-bar" id="audio-guide-bar" data-audio-src="">
          <div class="bab-left">
            <button type="button" class="bab-play-btn" data-audio-guide-btn>🎧 Listen to 3-Min Audio Guide</button>
            <div class="bab-meta">
              <span class="bab-title">Puffy or tender eyes? Listen while you rest quietly</span>
              <span class="bab-sub">Spoken English overview · Gentle self-care walk-through</span>
            </div>
          </div>
        </div>

        <div class="short-answer-box" id="quick-summary">
          <span class="short-answer-eyebrow">⚡ 30-Second Key Takeaway</span>
          <p><strong>A face can look temporarily puffy and flushed after crying.</strong> If the eye area is watery or tender, let it settle naturally first with a cool compress before trying any facial massage or tool routine.</p>
        </div>

        <figure class="bojin-figure" style="margin:2rem 0">
          <img src="assets/after-cry-card-01-draft.png" alt="A woman looking quietly into a bathroom mirror after crying; card title reads After You Cry, Your Face May Need a Pause" loading="lazy" width="1122" height="1402">
          <figcaption>The moment after an emotional release can make your face feel unfamiliar. That does not make it a problem to solve.</figcaption>
        </figure>

        <p>Sometimes the crying is brief. Sometimes it comes after you have held everything together for everyone else. When it finally passes, the emotion may be quieter—but your face still shows that something happened.</p>
        <p>Your eyelids may look puffy. The skin around your eyes may feel warm or sensitive. Your nose and cheeks may look flushed. Seeing those changes can create a second wave of discomfort: <em>I need to make myself look normal again.</em></p>
        <p>That urge is understandable, especially when you have somewhere to be. But the kindest response may be simpler than a routine: give your face a little time before deciding what it needs.</p>

        <aside class="bojin-inline-quiz" id="inline-quiz-card" data-biq-zone="eyes" aria-label="10-second eye area observation">
          <span class="biq-badge">🖐️ 10-Second Eye Observation · Step 1 of 2</span>
          <h3 class="biq-question">Close your eyes for 3 seconds and place clean fingertips gently under your eyes. What do you feel?</h3>
          <div class="biq-options" role="group" aria-label="Choose what you notice">
            <button type="button" class="biq-opt" data-biq-choice="puffy" data-biq-msg="Morning fluid and screen tiredness settle easily in thin under-eye skin. Feather-light passes along the bone rim—never dragging inward—help the area feel refreshed."><span>1. Puffy or full sensation</span><span aria-hidden="true">→</span></button>
            <button type="button" class="biq-opt" data-biq-choice="tight-corners" data-biq-msg="Tension around the outer eye corners often links to squinting. Anchoring with your supporting hand while gliding outward prevents skin drag."><span>2. Tightness at outer corners</span><span aria-hidden="true">→</span></button>
            <button type="button" class="biq-opt" data-biq-choice="tired-all-over" data-biq-msg="When your entire eye area feels fatigued, working only under the eyes is incomplete. Connecting the brow, outer corner, and cheek gives a much calmer result."><span>3. General end-of-day fatigue</span><span aria-hidden="true">→</span></button>
          </div>
          <div class="biq-feedback" hidden aria-live="polite">
            <p class="biq-feedback-text" style="margin:0;font-weight:500"></p>
            <div class="biq-actions">
              <a class="btn" href="eye-start-quiz.html">Start 20-Second Eye Starting Point &rarr;</a>
              <a class="btn btn--ghost" href="eye-area-guides.html">See 3-Region Eye Map</a>
            </div>
          </div>
        </aside>

        <h2>Why pressing immediately can backfire</h2>
        <p>When you cry, blood flow increases to the face, tear ducts are stimulated, and the delicate skin around your eyes retains temporary fluid. The tissue is active, warm, and easily sensitized.</p>
        <p>Grabbing a firm tool or rubbing vigorously into swollen eyelids right away usually produces more redness, not less. Instead, comfort comes first: splash with cool water, drink a glass of water, and allow the acute swelling to ease naturally.</p>

        <figure class="bojin-figure" style="margin:2rem 0">
          <img src="assets/after-cry-card-02-draft.png" alt="A soothing self-care reminder: Pause, Hydrate, Let the Eyes Settle" loading="lazy" width="1122" height="1402">
          <figcaption>Give your reflection permission to rest before reaching for any tool.</figcaption>
        </figure>

        <div class="note-safety" id="safety-note"><b>Gentle care rule.</b> Never use strong pressure over inflamed, scratched, or watery eyelids. Self-care should always feel comfortable and supportive.</div>
      </div>
    </article>
  </main>
{footer_html}
"""

with open(os.path.join(ROOT, 'blog-after-you-cry-puffy-eyes-pause.html'), 'w', encoding='utf-8') as f:
    f.write(c_art)
print('[OK] Created blog-after-you-cry-puffy-eyes-pause.html')

# 3. Add both to sitemap.xml
sm_path = os.path.join(ROOT, 'sitemap.xml')
with open(sm_path, 'r', encoding='utf-8') as f:
    sm = f.read()

new_urls = """  <url><loc>https://bojinfacetension.com/blog-when-your-shoulders-wont-drop.html</loc><lastmod>2026-10-26</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>
  <url><loc>https://bojinfacetension.com/blog-after-you-cry-puffy-eyes-pause.html</loc><lastmod>2026-10-26</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>
</urlset>"""

if 'blog-when-your-shoulders-wont-drop.html' not in sm:
    sm = sm.replace('</urlset>', new_urls)
    with open(sm_path, 'w', encoding='utf-8') as f:
        f.write(sm)
    print('[OK] Added new articles to sitemap.xml')

# 4. Remove Quiz from blog.html header
b_path = os.path.join(ROOT, 'blog.html')
with open(b_path, 'r', encoding='utf-8') as f:
    bc = f.read()
bc = bc.replace('<a href="https://bojinfacetension.com/quiz.html">Quiz</a>', '')
with open(b_path, 'w', encoding='utf-8') as f:
    f.write(bc)
print('[OK] Removed Quiz from blog.html header')
