#!/usr/bin/env python3
import os
import glob
import json
import re
from urllib.parse import quote

import requests

OWNER = 'mariajesusnaranjo'
REPO = 'skills-integrate-mcp-with-copilot'

TOKEN = os.environ.get('GITHUB_TOKEN')
if not TOKEN:
    print('ERROR: GITHUB_TOKEN environment variable not set')
    raise SystemExit(1)

API_URL = f'https://api.github.com/repos/{OWNER}/{REPO}/issues'


def parse_frontmatter_and_body(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    fm = {}
    body = text
    if text.startswith('---'):
        # find closing ---
        m = re.search(r'^---\s*\n(.*?)\n---\s*\n', text, flags=re.S)
        if m:
            fm_text = m.group(1)
            body = text[m.end():].strip()
            # parse simple key: value pairs
            for line in fm_text.splitlines():
                if ':' in line:
                    k, v = line.split(':', 1)
                    fm[k.strip()] = v.strip()
    return fm, body


headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'token {TOKEN}'
}

files = sorted(glob.glob('.github/ISSUES/*.md'))
if not files:
    print('No issue files found in .github/ISSUES')
    raise SystemExit(0)

for path in files:
    fm, body = parse_frontmatter_and_body(path)
    title = fm.get('title') or os.path.basename(path)
    labels_raw = fm.get('labels', '')
    # labels may be comma-separated
    labels = [l.strip() for l in labels_raw.split(',') if l.strip()]

    payload = {
        'title': title,
        'body': body,
    }
    if labels:
        payload['labels'] = labels

    print(f'Creating issue from {path}: "{title}"...')
    resp = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    if resp.status_code in (200, 201):
        data = resp.json()
        print('CREATED:', data.get('html_url'))
    else:
        print('FAILED:', resp.status_code, resp.text)

print('Done.')
