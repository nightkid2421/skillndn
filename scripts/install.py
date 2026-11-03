#!/usr/bin/env python3
"""Copy selected skills into an agent's skill directory without overwriting."""
import argparse
import json
import os
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skills', nargs='*', help='Skill folder names')
    parser.add_argument('--list', action='store_true', help='List available skills')
    parser.add_argument('--all', action='store_true', help='Install all included skills')
    parser.add_argument('--dest', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home()/'.codex')))/'skills')
    args = parser.parse_args()
    manifest = json.loads((ROOT/'manifest.json').read_text())
    available = {e['name']: e for e in manifest['skills'] if e['included']}
    if args.list:
        for name, entry in sorted(available.items()):
            print(f'{name}: {entry["license"]}')
        return
    if args.all and args.skills:
        parser.error('Choose either --all or named skills.')
    names = sorted(available) if args.all else list(dict.fromkeys(args.skills))
    if not names:
        parser.error('Choose skill names, --all, or --list.')
    unknown = set(names) - available.keys()
    if unknown:
        parser.error('Unknown skills: '+', '.join(sorted(unknown)))
    dest = args.dest.expanduser().resolve()
    existing = [name for name in names if (dest/name).exists() or (dest/name).is_symlink()]
    if existing:
        parser.error('Destination already exists (nothing copied): '+', '.join(existing))
    for name in names:
        shutil.copytree(ROOT/available[name]['path'], dest/name)
        print(f'Installed {name} -> {dest/name}')

if __name__ == '__main__':
    main()
