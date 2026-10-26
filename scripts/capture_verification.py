# -*- coding: utf-8 -*-
import os
import subprocess

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
art_dir = r'C:\Users\user888\.gemini\antigravity\brain\2ef321a4-4efb-44fa-808a-4f31b0f2703e'

p1 = os.path.join(art_dir, 'us-pack-desktop-1440.png')
p2 = os.path.join(art_dir, 'us-pack-mobile-375.png')

subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1440,1850', f'--screenshot={p1}', 'http://127.0.0.1:8900/blog-jaw-clenching-grinding-and-bojin.html'], check=True)
subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=500,1550', f'--screenshot={p2}', 'http://127.0.0.1:8900/blog-heavy-low-brows-lift.html'], check=True)
print('[OK] Captured full responsive screenshots without Windows 500px frame crop')
