#!/usr/bin/env python3
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, urljoin

ROOT = Path('docs')

href_re = re.compile(r'href\s*=\s*["\']([^"']+)["\']', re.I)

errors = []

html_files = list(ROOT.glob('**/*.html'))
if not html_files:
    print('No HTML files found in docs/')
    sys.exit(1)

for html in html_files:
    text = html.read_text(encoding='utf-8', errors='ignore')
    for m in href_re.finditer(text):
        href = m.group(1).strip()
        if not href or href.startswith(('http://','https://','mailto:','tel:','#','javascript:')):
            continue
        # remove query and fragment
        parsed = urlparse(href)
        path = parsed.path
        # resolve relative to the HTML file
        target = (html.parent / path).resolve()
        # allow directories (index.html)
        if target.is_dir():
            index_file = target / 'index.html'
            if not index_file.exists():
                errors.append((html.as_posix(), href, 'target dir missing index.html'))
        else:
            # try with .html appended if no extension
            if target.exists():
                continue
            if not Path(str(target) + '.html').exists():
                errors.append((html.as_posix(), href, 'target missing'))

if errors:
    print('Broken internal links found:')
    for src, href, reason in errors:
        print(f'- {src} -> {href} [{reason}]')
    sys.exit(2)
else:
    print('No broken internal links found in docs/.')
    sys.exit(0)
