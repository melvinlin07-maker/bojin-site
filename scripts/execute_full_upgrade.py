# -*- coding: utf-8 -*-
import os
import re
import glob

ROOT = r'c:\Users\user888\Documents\撥筋美國網站'

# ==============================================================================
# 1. TEMPLATES FOR INLINE SELF-CHECK CARDS (100% COMPLIANT, NO MEDICAL/DIAGNOSTIC TERMS)
# ==============================================================================
QUIZ_TEMPLATES = {
    'brows-forehead': """<aside class="bojin-inline-quiz" id="inline-quiz-card" data-biq-zone="brows-forehead" aria-label="10-second brow observation">
  <span class="biq-badge">🖐️ 10-Second Brow Observation · Step 1 of 2</span>
  <h3 class="biq-question">Rest your thumb pad lightly against the inner corner of your eyebrow. What do you notice?</h3>
  <div class="biq-options" role="group" aria-label="Choose what you notice">
    <button type="button" class="biq-opt" data-biq-choice="knot" data-biq-msg="That subtle firm ridge is where the corrugator muscle anchors. Instead of pressing harder, tiny calm circles with your other hand steadying the skin feel far more supportive."><span>1. A small firm ridge or knot</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="heavy" data-biq-msg="When screen fatigue sets in, the brow often feels heavy over the eye. Focusing on the upper orbital bone route helps the area feel lighter without pulling the lid."><span>2. Heavy, downward pull</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="smooth" data-biq-msg="If the brow feels calm, your forehead holding pattern may sit higher near the hairline. Checking the scalp and temple route is your best next step."><span>3. Relatively smooth</span><span aria-hidden="true">→</span></button>
  </div>
  <div class="biq-feedback" hidden aria-live="polite">
    <p class="biq-feedback-text" style="margin:0;font-weight:500"></p>
    <div class="biq-actions">
      <a class="btn" href="eye-start-quiz.html">Take 20-Second Visual Brow Quiz &rarr;</a>
      <a class="btn btn--ghost" href="brow-guide.html">See 6-Part Movement Guide</a>
    </div>
  </div>
</aside>""",

    'eyes': """<aside class="bojin-inline-quiz" id="inline-quiz-card" data-biq-zone="eyes" aria-label="10-second eye area observation">
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
</aside>""",

    'cheeks-nasolabial': """<aside class="bojin-inline-quiz" id="inline-quiz-card" data-biq-zone="cheeks-nasolabial" aria-label="10-second cheek observation">
  <span class="biq-badge">🖐️ 10-Second Midface Observation · Step 1 of 2</span>
  <h3 class="biq-question">Rest your fingers gently just beneath your cheekbone near the nose. What do you notice?</h3>
  <div class="biq-options" role="group" aria-label="Choose what you notice">
    <button type="button" class="biq-opt" data-biq-choice="one-side" data-biq-msg="Most women favor one chewing or sleeping side! Comparing your left and right cheek tension is the fastest way to personalize your daily routine."><span>1. One side feels tighter</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="heavy-cheek" data-biq-msg="When the tissue under the cheekbone feels full, gliding along the bone contour with your supporting hand steadying the skin is far more helpful than rubbing the fold."><span>2. Fullness above smile line</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="mouth-corner" data-biq-msg="Tension around mouth corners connects downward toward the jaw. Easing the jawline first gives your cheek passes a calmer foundation."><span>3. Tightness near mouth corners</span><span aria-hidden="true">→</span></button>
  </div>
  <div class="biq-feedback" hidden aria-live="polite">
    <p class="biq-feedback-text" style="margin:0;font-weight:500"></p>
    <div class="biq-actions">
      <a class="btn" href="map.html?zone=cheeks">Open 60-Second Interactive Face Map &rarr;</a>
      <a class="btn btn--ghost" href="results.html">See One-Side 5-Min Test</a>
    </div>
  </div>
</aside>""",

    'jaw-neck': """<aside class="bojin-inline-quiz" id="inline-quiz-card" data-biq-zone="jaw-neck" aria-label="10-second jaw and neck observation">
  <span class="biq-badge">🖐️ 10-Second Lower Face Observation · Step 1 of 2</span>
  <h3 class="biq-question">Pause for a moment: are your back teeth touching right now, or is your jaw resting loose?</h3>
  <div class="biq-options" role="group" aria-label="Choose what you notice">
    <button type="button" class="biq-opt" data-biq-choice="clenched" data-biq-msg="Noticing daytime clenching is a major breakthrough. Let your teeth part slightly and tongue rest—then use light, supported glides from jaw angle down the neck."><span>1. Teeth touching or braced</span><span aria-hidden="true">→</span></button>
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
</aside>""",

    'method': """<aside class="bojin-inline-quiz" id="inline-quiz-card" data-biq-zone="method" aria-label="10-second technique observation">
  <span class="biq-badge">✨ 10-Second Technique Observation · Step 1 of 2</span>
  <h3 class="biq-question">When practicing facial self-care at home, what has been your main hesitation?</h3>
  <div class="biq-options" role="group" aria-label="Choose what you notice">
    <button type="button" class="biq-opt" data-biq-choice="pulling" data-biq-msg="If the skin feels like it is dragging, the missing piece is almost always the Supporting Hand—anchoring behind the stroke so the tool glides without stretching skin."><span>1. Worried about pulling skin</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="guesswork" data-biq-msg="Random strokes across the face rarely feel satisfying. The Bojin Method focuses on anatomical bony landmarks, bone angle, and an intentional sequence."><span>2. Unsure of exact spot &amp; angle</span><span aria-hidden="true">→</span></button>
    <button type="button" class="biq-opt" data-biq-choice="fades" data-biq-msg="Instead of doing the whole face at once, try our One-Side 5-Minute Test first so you can observe the real difference in comfort in your own mirror."><span>3. Hard to tell if it works</span><span aria-hidden="true">→</span></button>
  </div>
  <div class="biq-feedback" hidden aria-live="polite">
    <p class="biq-feedback-text" style="margin:0;font-weight:500"></p>
    <div class="biq-actions">
      <a class="btn" href="facial-tension-journey.html">Try Free Interactive Video Lesson &rarr;</a>
      <a class="btn btn--ghost" href="results.html">See One-Side 5-Min Test</a>
    </div>
  </div>
</aside>"""
}

# ==============================================================================
# 2. UPGRADE REMAINING 64 BLOG ARTICLES WITH INLINE SELF-CHECK CARDS
# ==============================================================================
blog_paths = glob.glob(os.path.join(ROOT, 'blog-*.html'))
updated_blogs = 0

for bp in blog_paths:
    with open(bp, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'http-equiv="refresh"' in c or 'class="bojin-inline-quiz"' in c:
        continue
    
    fname = os.path.basename(bp).lower()
    
    # Determine zone
    if any(k in fname for k in ['eye', 'crows-feet', 'tear-trough', 'puffy', 'dark-circle', 'hooded', 'under-eye']):
        zone = 'eyes'
    elif any(k in fname for k in ['brow', 'forehead', 'frown', 'botox', 'scalp', 'temple']):
        zone = 'brows-forehead'
    elif any(k in fname for k in ['cheek', 'smile', 'nasolabial', 'marionette', 'asymmetry', 'lip']):
        zone = 'cheeks-nasolabial'
    elif any(k in fname for k in ['jaw', 'neck', 'chin', 'clench', 'grind', 'jowl', 'shoulder', 'posture']):
        zone = 'jaw-neck'
    else:
        zone = 'method'
        
    tpl = QUIZ_TEMPLATES[zone]
    
    # Insert right before the 2nd <h2>
    h2_matches = list(re.finditer(r'<h2[^>]*>', c))
    if len(h2_matches) >= 2:
        pos = h2_matches[1].start()
        c = c[:pos] + tpl + '\n\n' + c[pos:]
        with open(bp, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_blogs += 1

print(f'[OK] Deployed 10-Second Self-Check cards to {updated_blogs} remaining blog articles!')

# ==============================================================================
# 3. EMBED UNUSED HIGH-RES ANATOMY IMAGES FROM ASSETS/
# ==============================================================================
image_embeds = [
    ('blog-forehead-lines-deepening.html', 'assets/bojin-forehead-portrait-compare.webp', 'Comparing tense brow contracted vs gentle release along bone contour'),
    ('blog-forehead-frown-lines.html', 'assets/bojin-forehead-portrait-steps.webp', 'Two-step observation: finding the corrugator landmark then releasing outward'),
    ('blog-jaw-end-of-day-release.html', 'assets/bojin-jaw-step-find-muscle.webp', 'Locating masseter landmark below cheekbone before gentle glide'),
    ('blog-scalp-and-hairline-tension.html', 'assets/bojin-hairline-scalp-closeup-technique.jpg', 'Yu-Ting Lan demonstrating gentle hairline and scalp release technique'),
    ('blog-the-point-behind-your-ear.html', 'assets/bojin-ear-side-face-hands-on.jpg', 'Two-hand supported placement along the ear-contour release route'),
]

for fname, img_rel, alt_text in image_embeds:
    fpath = os.path.join(ROOT, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        fc = f.read()
    if img_rel not in fc:
        fig_html = f'''<figure class="bojin-figure" style="margin:2rem 0">
  <img src="{img_rel}" alt="{alt_text}" loading="lazy" width="1200" height="800">
  <figcaption>{alt_text}.</figcaption>
</figure>
'''
        # Insert before 2nd <h2> or after quick summary
        if 'id="quick-summary"' in fc:
            fc = re.sub(r'(</div>\s*<!--.*?-->|\</div>)', r'\1\n' + fig_html, fc, count=1)
        elif '<h2' in fc:
            fc = fc.replace('<h2', fig_html + '\n<h2', 1)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(fc)
        print(f'[OK] Embedded unused image {img_rel} into {fname}')

# ==============================================================================
# 4. DEPLOY AI COMPARISON TABLES (GEO-MATRIX) TO TOP 10 HIGH-IMPRESSION ARTICLES
# ==============================================================================
GEO_TABLES = {
    'blog-natural-botox-alternative-forehead.html': """<div class="geo-matrix-wrap" id="geo-table">
  <table class="geo-matrix" aria-label="Forehead Botox vs Bojin Observation">
    <thead>
      <tr>
        <th>Observation Focus</th>
        <th>Common Neuromodulator Expectation</th>
        <th>The Bojin Method Observation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Inner Brow Tension</strong></td>
        <td>Freezing the muscle movement chemically.</td>
        <td>Releasing the mechanical tissue bracing using supported small circles.</td>
      </tr>
      <tr>
        <td><strong>Everyday Screen Fatigue</strong></td>
        <td>Wears off over 3 to 4 months.</td>
        <td>An everyday 2-minute mindful habit you own and control at home.</td>
      </tr>
      <tr>
        <td><strong>Natural Movement</strong></td>
        <td>Reduces expressive movement.</td>
        <td>Preserves natural expression while easing the end-of-day heavy feeling.</td>
      </tr>
    </tbody>
  </table>
</div>
""",

    'blog-tired-puffy-eyes.html': """<div class="geo-matrix-wrap" id="geo-table">
  <table class="geo-matrix" aria-label="Eye Creams vs Bojin Eye Reset">
    <thead>
      <tr>
        <th>Under-Eye Notice</th>
        <th>Surface Topical Approach</th>
        <th>The Bojin Method Approach</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Morning Fluid Fullness</strong></td>
        <td>Layering heavy creams that may sit on surface.</td>
        <td>Feather-light glides along orbital bone rim to encourage natural drainage.</td>
      </tr>
      <tr>
        <td><strong>Outer-Corner Tightness</strong></td>
        <td>Tugging delicate skin inward with fingers.</td>
        <td>Anchoring with supporting finger; gliding outward along bone contour.</td>
      </tr>
      <tr>
        <td><strong>Brow-to-Lid Heaviness</strong></td>
        <td>Treating under-eye in complete isolation.</td>
        <td>Releasing upper brow anchor first so whole eye zone feels lighter.</td>
      </tr>
    </tbody>
  </table>
</div>
""",

    'blog-the-supporting-hand.html': """<div class="geo-matrix-wrap" id="geo-table">
  <table class="geo-matrix" aria-label="One-Handed Scraping vs Two-Handed Bojin">
    <thead>
      <tr>
        <th>Technique Element</th>
        <th>Single-Handed Facial Massage</th>
        <th>Two-Handed Bojin Method</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Skin Movement</strong></td>
        <td>Skin drags and bunches ahead of the tool.</td>
        <td>Supporting hand anchors skin behind tool; zero dragging.</td>
      </tr>
      <tr>
        <td><strong>Pressure Control</strong></td>
        <td>Easy to press too deeply into bone.</td>
        <td>Supporting hand senses tissue feedback; calibrated comfortable touch.</td>
      </tr>
      <tr>
        <td><strong>End of Routine</strong></td>
        <td>Stops abruptly on the cheek.</td>
        <td>Always sweeps downward off side of neck to finish calmly.</td>
      </tr>
    </tbody>
  </table>
</div>
"""
}

for fname, tbl_html in GEO_TABLES.items():
    fpath = os.path.join(ROOT, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        fc = f.read()
    if 'id="geo-table"' not in fc and 'id="quick-summary"' in fc:
        fc = fc.replace('<div class="short-answer-box" id="quick-summary">', '<div class="short-answer-box" id="quick-summary">', 1)
        # Place table after quick-summary div
        end_qs = fc.find('</div>', fc.find('id="quick-summary"')) + 6
        fc = fc[:end_qs] + '\n' + tbl_html + fc[end_qs:]
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(fc)
        print(f'[OK] Added AI geo-matrix comparison table to {fname}')

print('[OK] Script 1/2 complete!')
