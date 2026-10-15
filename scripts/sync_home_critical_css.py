"""Refresh homepage first-paint CSS after editing styles.css. No dependencies."""
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- home-critical-css:start -->'
END = '<!-- home-critical-css:end -->'


def between(source, start, end):
    return source.split(start, 1)[1].split(end, 1)[0]


def main():
    css = (ROOT / 'styles.css').read_text(encoding='utf-8')
    # Preserve the shared stylesheet's cascade order, including its late overrides.
    sections = [
        css.split('/* ---------- grids & cards ---------- */', 1)[0],
        between(css, '/* ---------- header / nav ---------- */',
                '/* ---------- footer (centered, compact) ---------- */'),
        between(css, '/* prevent any sub-pixel horizontal scroll', '/* review wall */').split('*/', 1)[1],
        between(css, '/* reveal-on-scroll */', '/* ---------- blog / articles ---------- */'),
        between(css, '/* — gold second voice:', '/* — cards & tiles:').split('*/', 1)[1],
        between(css, '/* — bands:', '/* ============================================================\n   Editorial touches').split('*/', 1)[1],
        css[css.index('/* Mobile editorial rhythm:'):],
    ]
    critical = '\n'.join(sections)
    critical = re.sub(r'/\*.*?\*/', '', critical, flags=re.S)
    critical = '\n'.join(line.strip() for line in critical.splitlines() if line.strip())
    source_hash = hashlib.sha256(css.encode()).hexdigest()[:16]
    block = (f'{START}\n  <!-- Generated from styles.css ({source_hash}); '
             'refresh with python scripts/sync_home_critical_css.py -->\n'
             f'  <style id="home-critical-css">\n{critical}\n  </style>\n'
             '  <link rel="stylesheet" href="styles.css?v=9" media="print" '
             'onload="this.media=\'all\'">\n'
             '  <noscript><link rel="stylesheet" href="styles.css?v=9"></noscript>\n'
             f'  {END}')
    path = ROOT / 'index.html'
    html = path.read_text(encoding='utf-8')
    if START in html:
        before, rest = html.split(START, 1)
        _, after = rest.split(END, 1)
        html = before + block + after
    else:
        needle = '<link rel="stylesheet" href="styles.css?v=9">'
        if html.count(needle) != 1:
            raise SystemExit('Expected one homepage stylesheet link; no files changed.')
        html = html.replace(needle, block, 1)
    path.write_text(html, encoding='utf-8', newline='\n')
    print(f'Updated homepage critical CSS: {len(critical.encode())} bytes; source {source_hash}')


if __name__ == '__main__':
    main()