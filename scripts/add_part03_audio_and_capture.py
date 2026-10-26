# -*- coding: utf-8 -*-
import os
import subprocess

ROOT = r'c:\Users\user888\Documents\撥筋美國網站'

# 1. Update brow-guide.html
bg_path = os.path.join(ROOT, 'brow-guide.html')
with open(bg_path, 'r', encoding='utf-8') as f:
    bg = f.read()

# Add scroll-margin-top to #audio-guide-bar inside brow-guide.html style
if '#audio-guide-bar { scroll-margin-top: 200px; }' not in bg:
    bg = bg.replace('</style>', '#audio-guide-bar { scroll-margin-top: 200px; margin: 18px 0 24px !important; }\n</style>', 1)

# Add the dedicated Part 03 Audio Button
old_tabs = """          <div class="v5-compare-tabs" role="tablist" aria-label="Select comparison mode">
            <button class="v5-tab-btn" data-mode="circle" aria-pressed="true">
              ⭕ Correct: Complete Small Circle
            </button>
            <button class="v5-tab-btn" data-mode="sway" aria-pressed="false">
              ❌ Mistake: Side-to-Side Sway
            </button>
            <button class="v5-tab-btn" data-mode="sidebyside" aria-pressed="false">
              ⚖️ Simultaneous Dual View
            </button>
          </div>"""

new_tabs = """          <div class="v5-compare-tabs" role="tablist" aria-label="Select comparison mode">
            <button class="v5-tab-btn" data-mode="circle" aria-pressed="true">
              ⭕ Correct: Complete Small Circle
            </button>
            <button class="v5-tab-btn" data-mode="sway" aria-pressed="false">
              ❌ Mistake: Side-to-Side Sway
            </button>
            <button class="v5-tab-btn" data-mode="sidebyside" aria-pressed="false">
              ⚖️ Simultaneous Dual View
            </button>
            <button class="v5-tab-btn" id="part03-audio-btn" type="button" style="background:var(--paper-3);border-color:var(--cta-border);color:var(--ink);font-weight:700">
              🎧 Listen: Why Small Circles Matter (1-Min Audio)
            </button>
          </div>"""

if old_tabs in bg:
    bg = bg.replace(old_tabs, new_tabs, 1)

with open(bg_path, 'w', encoding='utf-8') as f:
    f.write(bg)

# 2. Update nav.js with Part 03 Audio handler
nav_path = os.path.join(ROOT, 'nav.js')
with open(nav_path, 'r', encoding='utf-8') as f:
    nav = f.read()

part03_js = """
  // 3. Dedicated Part 03 Technique Explanation Audio
  document.addEventListener('click', function(e){
    var p3btn = e.target.closest('#part03-audio-btn');
    if (!p3btn) return;
    if ('speechSynthesis' in window) {
      if (window.speechSynthesis.speaking && !window.speechSynthesis.paused) {
        window.speechSynthesis.cancel();
        p3btn.innerHTML = '🎧 Listen: Why Small Circles Matter (1-Min Audio)';
        return;
      }
      var msg = "Here is why the teacher draws a complete small circle instead of swaying side-to-side. When you sway back and forth across the brow, the tool drags and stretches the delicate skin over the brow bone. But when you anchor with your supporting finger and draw small, rhythmic circles in one spot before stepping outward, you gently release the corrugator tension beneath the skin without pulling the eye area. Notice how the supporting hand keeps the skin steady behind every stroke.";
      var utter = new SpeechSynthesisUtterance(msg);
      utter.lang = 'en-US';
      utter.rate = 0.95;
      utter.onend = function(){ p3btn.innerHTML = '🎧 Listen: Why Small Circles Matter (1-Min Audio)'; };
      window.speechSynthesis.cancel();
      window.speechSynthesis.speak(utter);
      p3btn.innerHTML = '⏹ Stop Audio (Playing...)';
      if (window.bojinSignal) window.bojinSignal('BojinAudioPart03Play', { page: location.pathname });
    }
  });
"""

if 'BojinAudioPart03Play' not in nav:
    nav = nav.replace('// 2. Pinterest Save Button', part03_js + '\n  // 2. Pinterest Save Button')
    with open(nav_path, 'w', encoding='utf-8') as f:
        f.write(nav)

# 3. Capture screenshot of brow-guide.html at #compare
art_dir = r'C:\Users\user888\.gemini\antigravity\brain\2ef321a4-4efb-44fa-808a-4f31b0f2703e'
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
shot_part03 = os.path.join(art_dir, 'brow-guide-part03-audio.png')
shot_top = os.path.join(art_dir, 'brow-guide-top-audio.png')

subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1280,950', f'--screenshot={shot_part03}', 'http://127.0.0.1:8900/brow-guide.html#compare'], check=True)
subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1280,850', f'--screenshot={shot_top}', 'http://127.0.0.1:8900/brow-guide.html'], check=True)

print('[OK] Part 03 audio button installed and 2 screenshots captured!')
