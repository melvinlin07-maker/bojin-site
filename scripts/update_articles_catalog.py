# -*- coding: utf-8 -*-

with open('articles.html', 'r', encoding='utf-8') as f:
    ac = f.read()

# Update count 99 -> 101
ac = ac.replace('<b>99</b><span>gentle guides</span>', '<b>101</b><span>gentle guides</span>')

row1 = '''      <a class="lib-row" data-cat="jaw" href="blog-when-your-shoulders-wont-drop.html">
        <div class="lib-row__media"><img loading="lazy" decoding="async" src="assets/shoulders-face-card-01-anatomy-draft.png" alt="When Your Shoulders Won’t Drop"></div>
        <div class="lib-row__body">
          <span class="lib-row__cat">Jaw &amp; Neck</span>
          <h2 class="lib-row__q">When your shoulders won’t drop, your face can feel tired too</h2>
          <p class="lib-row__why">How shoulder, neck, and jaw tension connect as a daily holding pattern, and a one-minute pause.</p>
          <span class="lib-row__meta">4 min read &middot; body awareness <span class="arw">&rarr;</span></span>
        </div>
      </a>
'''

row2 = '''      <a class="lib-row" data-cat="eyes" href="blog-after-you-cry-puffy-eyes-pause.html">
        <div class="lib-row__media"><img loading="lazy" decoding="async" src="assets/after-cry-card-01-draft.png" alt="After You Cry, Your Face May Need a Pause"></div>
        <div class="lib-row__body">
          <span class="lib-row__cat">Eyes</span>
          <h2 class="lib-row__q">After you cry, your face may need a pause</h2>
          <p class="lib-row__why">Why puffy, flushed skin after crying needs comfort first before reaching for any tool.</p>
          <span class="lib-row__meta">4 min read &middot; gentle eye care <span class="arw">&rarr;</span></span>
        </div>
      </a>
'''

if 'blog-when-your-shoulders-wont-drop.html' not in ac:
    ac = ac.replace('<div class="lib-list" id="lib">', '<div class="lib-list" id="lib">\n' + row1 + '\n' + row2)
    with open('articles.html', 'w', encoding='utf-8') as f:
        f.write(ac)
    print('[OK] Added 2 new articles to articles.html and updated count to 101!')
