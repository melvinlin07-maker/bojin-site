# -*- coding: utf-8 -*-
import re
import json
import urllib.request

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    urls = re.findall(r'<loc>(https://bojinfacetension\.com/[^<]+)</loc>', f.read())

print(f'Discovered {len(urls)} canonical URLs in sitemap.xml ready for IndexNow ping.')
