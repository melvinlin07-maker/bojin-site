# -*- coding: utf-8 -*-
import os
import subprocess

ROOT = r'c:\Users\user888\Documents\撥筋美國網站'
bg_path = os.path.join(ROOT, 'brow-guide.html')

with open(bg_path, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Inject Top Audio Bar inside render()
target_render_top = '<p class="v3-intro" style="border-bottom:1px solid var(--line);padding-bottom:24px;margin-bottom:12px">${t(\'這是眼周三大部位的第一篇。本頁將 6 個核心章節連貫呈現：日常表情 → 五肌解剖地圖 → 定點小圓 vs 左右晃動作對比 → 動手前滑度準備 → 5 個細節問答 → 完整眼部五步驟總覽。利用頂端小目錄可隨時跳轉。\', \'Region 01 of our eye series: Brows & Inner Brow. Scroll through 6 structured parts: Expression → 5-Muscle Map → Movement Comparison → Glide Preparation → 5 Detail Q&As → Full Sequence Orientation. Use the sticky navigator above to jump between parts at any time.\')}</p>'

audio_bar_inside_render = """
        <div class="bojin-audio-bar" id="audio-guide-bar" data-audio-src="" style="margin: 1.2rem 0 2rem;">
          <div class="bab-left">
            <button type="button" class="bab-play-btn" data-audio-guide-btn>🎧 ${t('收聽 3 分鐘語音導讀', 'Listen to 3-Min Audio Guide')}</button>
            <div class="bab-meta">
              <span class="bab-title">${t('看螢幕眼睛酸？閉上眼收聽這篇眉眼教學重點', 'Brows feeling heavy from screens? Listen to the movement walk-through')}</span>
              <span class="bab-sub">${t('美式英文真人語音導讀 · 6 大重點步驟導覽', 'Spoken English guide · Small circles vs swaying comparison')}</span>
            </div>
          </div>
        </div>"""

if target_render_top in c and 'id="audio-guide-bar"' not in c.split('function render()')[1]:
    c = c.replace(target_render_top, target_render_top + '\n' + audio_bar_inside_render, 1)

# 2. Inject Part 03 Audio Button inside render()
target_render_p3 = """            <button class="v5-tab-btn" data-mode="sidebyside" aria-pressed="false">
              ${t('⚖️ 上下同框對照（慢動作直觀比對）', '⚖️ Simultaneous Dual View')}
            </button>
          </div>"""

p3_btn_inside_render = """            <button class="v5-tab-btn" data-mode="sidebyside" aria-pressed="false">
              ${t('⚖️ 上下同框對照（慢動作直觀比對）', '⚖️ Simultaneous Dual View')}
            </button>
            <button class="v5-tab-btn" id="part03-audio-btn" type="button" style="background:var(--paper-3);border-color:var(--cta-border);color:var(--ink);font-weight:700">
              🎧 ${t('聽聽看：為什麼一定要畫小圓圈 (1分鐘語音)', 'Listen: Why Small Circles Matter (1-Min Audio)')}
            </button>
          </div>"""

if target_render_p3 in c:
    c = c.replace(target_render_p3, p3_btn_inside_render, 1)

with open(bg_path, 'w', encoding='utf-8') as f:
    f.write(c)

print('[OK] Injected Top Audio Bar and Part 03 Audio Button inside render()!')

# 3. Capture fresh screenshots of Part 03 and Top
art_dir = r'C:\Users\user888\.gemini\antigravity\brain\2ef321a4-4efb-44fa-808a-4f31b0f2703e'
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
shot_part03 = os.path.join(art_dir, 'brow-guide-part03-audio.png')
shot_top = os.path.join(art_dir, 'brow-guide-top-audio.png')

# Note: capture top first
subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1280,950', f'--screenshot={shot_top}', 'http://127.0.0.1:8900/brow-guide.html'], check=True)

# Capture Part 03 comparison
subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1280,950', f'--screenshot={shot_part03}', 'http://127.0.0.1:8900/brow-guide.html?lang=en#compare'], check=True)

print('[OK] Both screenshots re-captured!')
