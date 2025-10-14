#!/usr/bin/env python3
import os
import re
import unicodedata
from pathlib import Path

ROOT = "/Users/jorgemiguelsilva/FEGA_SOPs"
README = Path(ROOT) / "README.md"
SOP_DIR = Path(ROOT) / "sop"

def norm(s: str) -> str:
    s = s.lower()
    s = unicodedata.normalize('NFKD', s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    tokens = s.split()
    norm_tokens = []
    for t in tokens:
        if len(t) > 4 and t.endswith('ing'):
            t = t[:-3]
        if len(t) > 3 and t.endswith('ed'):
            t = t[:-2]
        if len(t) > 3 and t.endswith('es'):
            t = t[:-2]
        elif len(t) > 2 and t.endswith('s'):
            t = t[:-1]
        norm_tokens.append(t)
    return " ".join(norm_tokens)

def load_allowed_titles() -> list[str]:
    titles: list[str] = []
    if not README.exists():
        return titles
    with README.open('r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line.startswith('| ') and '---' not in line and not line.startswith('| Name'):
                cols = [c.strip() for c in line.strip().strip('|').split('|')]
                if cols:
                    titles.append(cols[0])
    return titles

def list_md_files() -> list[str]:
    if not SOP_DIR.exists():
        return []
    files = []
    for p in sorted(SOP_DIR.glob('*.md')):
        files.append(p.name[:-3])
    return files

def main() -> int:
    allowed = load_allowed_titles()
    allowed_norm = [norm(a) for a in allowed]
    mds = list_md_files()

    unauthorized: list[str] = []
    for md in mds:
        n = norm(md)
        # strip FEGA-SOP#### prefix if present
        n = re.sub(r'^fega sop\d{4} ', '', n)
        md_set = set(n.split())
        ok = False
        for an in allowed_norm:
            an_set = set(an.split())
            inter = md_set & an_set
            union = md_set | an_set
            j = (len(inter) / len(union)) if union else 0.0
            if j >= 0.35 or an in n or n in an:
                ok = True
                break
        if not ok:
            unauthorized.append(md)

    print("Allowed titles (from README):")
    for a in allowed:
        print(f" - {a}")
    print("\nConverted MD basenames in sop/:")
    for md in mds:
        print(f" - {md}")
    print("\nNOT in allow-list:")
    for u in unauthorized:
        print(f" - {u}")

    return 0

if __name__ == '__main__':
    raise SystemExit(main())


