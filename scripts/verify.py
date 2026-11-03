#!/usr/bin/env python3
"""Verify exported skill contents against the snapshot manifest."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    manifest = json.loads((ROOT/'manifest.json').read_text())
    errors = []
    count = 0
    for entry in manifest['skills']:
        if not entry['included']:
            continue
        count += 1
        expected = {item['path']: item['sha256'] for item in entry['files']}
        actual = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in (ROOT/entry['path']).rglob('*') if p.is_file()}
        for path in sorted(expected.keys() | actual.keys()):
            if expected.get(path) != actual.get(path):
                errors.append(path)
        skill = ROOT/entry['path']/'SKILL.md'
        text = skill.read_text()
        if not text.startswith('---\n') or '\nname:' not in text or '\ndescription:' not in text:
            errors.append(f'{skill.name}: missing skill frontmatter')
    if errors:
        raise SystemExit('Verification failed:\n'+'\n'.join(errors))
    print(f'OK: {count} skills; all exported file hashes match.')

if __name__ == '__main__':
    main()
