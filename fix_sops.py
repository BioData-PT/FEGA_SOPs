#!/usr/bin/env python3
import os
import re
import json
import shutil

ROOT = "/Users/jorgemiguelsilva/FEGA_SOPs"
SOP_DIR = os.path.join(ROOT, "sop")
DOCX_DIRS = [
    os.path.join(ROOT, "FEGA-Helpdesk-SOPs"),
    os.path.join(ROOT, "FEGA-Helpdesk-SOPs", "Helpdesk Portal SOPs"),
]
NEW_IMG_DIR = os.path.join(ROOT, "docs", "images")
MAP_JSON = os.path.join(SOP_DIR, "_sop_image_map.json")
README_MD = os.path.join(ROOT, "README.md")

IMG_MD_RE = re.compile(r"!\[(.*?)\]\((?!https?://)([^)]+)\)")
IMG_HTML_RE = re.compile(r"<img([^>]*?)src=\"(?!https?://)([^\"]+)\"")
CODE_RE = re.compile(r"FEGA-SOP\d{4}")

PREFIXES = [
    "@images/",
    "../docs/images/",
    "docs/images/media/",
    "docs/images/",
    "docs/images/",
    "images/docs/",
    "images/",
    "../images/",
    "./",
    "/",
]


def to_new(path: str) -> str:
    p = path.strip().split('#')[0].split('?')[0]
    for pref in PREFIXES:
        if p.startswith(pref):
            p = p[len(pref):]
            break
    # already normalized if starts with docs/images
    if p.startswith('docs/images/'):
        return '../' + p  # make relative from sop/
    # strip leading docs/ if present
    if p.startswith('docs/'):
        p = p[5:]
    return f"../docs/images/{p}"


def load_code_map():
    if not os.path.isfile(MAP_JSON):
        return {}
    with open(MAP_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return {k: v.get('code') for k, v in data.items() if isinstance(v, dict) and v.get('code')}


def ensure_dirs():
    os.makedirs(NEW_IMG_DIR, exist_ok=True)
    os.makedirs(SOP_DIR, exist_ok=True)


def find_docx_files():
    files = []
    for d in DOCX_DIRS:
        if not os.path.isdir(d):
            continue
        for name in os.listdir(d):
            if not name.lower().endswith('.docx'):
                continue
            # Exclude OLD variants only in top-level folder
            if os.path.basename(d) == 'FEGA-Helpdesk-SOPs' and name.startswith('(OLD'):
                continue
            files.append(os.path.join(d, name))
    # Deterministic order
    files.sort(key=lambda p: os.path.basename(p).lower())
    return files


def run_pandoc(src_docx: str, tmp_dir: str) -> str:
    """Run pandoc to convert docx to gfm and extract media into tmp_dir/media.
    Returns path to generated markdown file.
    """
    import subprocess
    os.makedirs(tmp_dir, exist_ok=True)
    out_md = os.path.join(tmp_dir, 'out.md')
    try:
        subprocess.check_call([
            'pandoc', src_docx, '-t', 'gfm', f'--extract-media={tmp_dir}', '-o', out_md
        ])
    except FileNotFoundError:
        raise SystemExit('Pandoc not found. Please install pandoc (e.g., brew install pandoc).')
    return out_md


def convert_docx_to_md_with_images(src_docx: str, code: str) -> dict:
    """Convert a DOCX into Markdown and normalized images.
    Returns a dict with keys: md_path, images (list of target filenames), title.
    """
    import tempfile
    tmp_dir = tempfile.mkdtemp(prefix='sop_build_')
    out_md_path = run_pandoc(src_docx, tmp_dir)
    # Collect extracted images
    media_dir = os.path.join(tmp_dir, 'media')
    extracted = []
    if os.path.isdir(media_dir):
        for n in sorted(os.listdir(media_dir)):
            p = os.path.join(media_dir, n)
            if os.path.isfile(p):
                extracted.append(p)
    # Rename and move images to NEW_IMG_DIR with FEGA-SOP prefix
    moved_names = []
    for i, p in enumerate(extracted, start=1):
        _, ext = os.path.splitext(p)
        ext = ext.lower() or '.png'
        target_name = f"{code}_image_{i}{ext}"
        target_path = os.path.join(NEW_IMG_DIR, target_name)
        # If target exists, reuse it (avoid duplicate copies)
        if not os.path.exists(target_path):
            # Ensure destination directory exists
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            try:
                shutil.move(p, target_path)
            except Exception:
                shutil.copy2(p, target_path)
        moved_names.append((os.path.basename(p), target_name))
    # Read md and rewrite image refs to images/docs/<target_name>
    with open(out_md_path, 'r', encoding='utf-8', errors='ignore') as f:
        md_txt = f.read()
    # Build map by basename -> ../docs/images/target (relative from sop/)
    base_to_target = { src_base: f"../docs/images/{tgt_name}" for src_base, tgt_name in moved_names }

    # Replace links using regex so we can consult basenames and strip absolute tmp prefixes
    def repl_md(m):
        alt, path = m.group(1), m.group(2)
        if path.startswith(('http://','https://')):
            return m.group(0)
        base = os.path.basename(path)
        if base in base_to_target:
            return f"![{alt}]({base_to_target[base]})"
        # Fallback normalization
        return f"![{alt}]({to_new(path)})"

    def repl_html(m):
        before, path = m.group(1), m.group(2)
        if path.startswith(('http://','https://')):
            return m.group(0)
        base = os.path.basename(path)
        if base in base_to_target:
            return f"<img{before}src=\"{base_to_target[base]}\""
        return f"<img{before}src=\"{to_new(path)}\""

    md_txt = IMG_MD_RE.sub(repl_md, md_txt)
    md_txt = IMG_HTML_RE.sub(repl_html, md_txt)
    # Compute target md filename
    base_title = os.path.splitext(os.path.basename(src_docx))[0]
    safe_title = base_title.strip().replace('/', '-').replace(' ', '_').strip('_')
    target_md = os.path.join(SOP_DIR, f"{code}_{safe_title}.md")
    # Write md
    with open(target_md, 'w', encoding='utf-8') as f:
        f.write(md_txt)
    # Clean tmp
    shutil.rmtree(tmp_dir, ignore_errors=True)
    return { 'md_path': target_md, 'images': [n for _, n in moved_names], 'title': safe_title }


def load_title_code_map_from_readme() -> dict:
    """Return mapping from SOP Name (README first column) -> FEGA-SOP#### code (Identifier)."""
    if not os.path.isfile(README_MD):
        return {}
    rows = []
    with open(README_MD, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line.startswith('| ') and '---' not in line and not line.startswith('| Name'):
                cols = [c.strip() for c in line.strip().strip('|').split('|')]
                if len(cols) >= 2:
                    rows.append((cols[0], cols[1]))
    title_to_code: dict[str, str] = {}
    for name, ident in rows:
        m = re.search(r"FEGA-SOP\d{4}", ident)
        if m:
            title_to_code[name] = m.group(0)
    return title_to_code


def normalize_text(s: str) -> str:
    import unicodedata
    s = s.lower()
    s = unicodedata.normalize('NFKD', s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def assign_codes_to_docx(docx_files: list[str], title_to_code: dict) -> dict:
    """Map each DOCX to a FEGA-SOP code using fuzzy match against README Name column."""
    # Precompute normalized names
    norm_title_to_code = {normalize_text(k): v for k, v in title_to_code.items()}
    mapping: dict[str, str] = {}
    for path in docx_files:
        base_title = os.path.splitext(os.path.basename(path))[0]
        n = normalize_text(base_title)
        # direct or subset match
        best = None
        best_score = 0.0
        for tnorm, code in norm_title_to_code.items():
            # token jaccard
            a = set(n.split())
            b = set(tnorm.split())
            if not a or not b:
                continue
            inter = len(a & b)
            union = len(a | b)
            j = inter / union if union else 0.0
            if j > best_score:
                best_score = j
                best = code
        # threshold to accept mapping
        if best and best_score >= 0.3:
            mapping[path] = best
    return mapping


def rebuild_all_from_docx():
    """Full rebuild from DOCX: convert, extract, normalize, and write MD files with proper names."""
    docx_files = find_docx_files()
    title_to_code = load_title_code_map_from_readme()
    docx_to_code = assign_codes_to_docx(docx_files, title_to_code)
    build_summary = {}
    for src in docx_files:
        code = docx_to_code.get(src)
        if not code:
            # skip DOCX not present in README allow-list
            continue
        result = convert_docx_to_md_with_images(src, code)
        build_summary[os.path.basename(src)] = {
            'code': code,
            'md': os.path.basename(result['md_path']),
            'images': result['images'],
        }
    # Save summary mapping
    with open(MAP_JSON, 'w', encoding='utf-8') as f:
        json.dump(build_summary, f, indent=2)


def load_allowed_codes_from_readme() -> set:
    """Parse README Identifier column and return FEGA-SOP#### codes to keep."""
    allowed: set[str] = set()
    if not os.path.isfile(README_MD):
        return allowed
    with open(README_MD, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line.startswith('| '):
                cols = [c.strip() for c in line.strip().strip('|').split('|')]
                if len(cols) >= 2 and cols[1] and cols[1] != 'Identifier' and '---' not in cols[1]:
                    m = re.search(r"FEGA-SOP\d{4}", cols[1])
                    if m:
                        allowed.add(m.group(0))
    return allowed


def filter_sop_md_by_allowed_codes(allowed: set):
    """Remove Markdown files in sop/ whose FEGA-SOP code not in allowed set."""
    for name in os.listdir(SOP_DIR):
        if not name.endswith('.md'):
            continue
        if name == 'header_template.md':
            continue
        m = re.match(r"^(FEGA-SOP\d{4})_", name)
        code = m.group(1) if m else None
        if code and code not in allowed:
            try:
                os.remove(os.path.join(SOP_DIR, name))
            except OSError:
                pass


def cleanup_markdown_files():
    """Pass to normalize any residual paths and HTML <img> tags in sop/*.md."""
    md_files = [n for n in os.listdir(SOP_DIR) if n.endswith('.md')]
    temp_media_re = re.compile(r"(?:^|[\(\s\">])(?:/[^\s\)]*)?/media/image(\d+)(\.[A-Za-z0-9]+)")
    html_img_re = re.compile(r"<img[^>]*?src=\"([^\"]+)\"[^>]*?>")
    for name in md_files:
        path = os.path.join(SOP_DIR, name)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            txt = f.read()
        # Derive FEGA-SOP code from filename prefix if present
        mcode = re.match(r"^(FEGA-SOP\d{4})_", name)
        code = mcode.group(1) if mcode else None

        # 1) Convert HTML <img ...> to Markdown ![](path)
        def repl_html_img(m):
            src = m.group(1)
            # Keep as-is path; other rules will normalize it
            return f"![ ]({src})"
        new = html_img_re.sub(repl_html_img, txt)

        # 2) Normalize docs/images without ../ to be relative
        new = new.replace('](docs/images/', '](../docs/images/')
        new = new.replace('src="docs/images/', 'src="../docs/images/')

        # 3) Replace any leftover temp media/imageN.ext using the code
        if code:
            def repl_temp(m):
                idx = m.group(1)
                ext = m.group(2)
                replacement = f" ../docs/images/{code}_image_{idx}{ext}"
                prefix = m.group(0)[0] if m.group(0) else ''
                # Ensure we keep leading delimiter
                return m.group(0)[:-len(m.group(0).lstrip())] + replacement.strip()
            # Safer manual pass preserving delimiters
            def repl_fn(match):
                full = match.group(0)
                # Find the imageN.ext inside
                m2 = re.search(r"image(\d+)(\.[A-Za-z0-9]+)", full)
                if not m2:
                    return full
                idx, ext = m2.group(1), m2.group(2)
                return re.sub(r"(?:/[^\s\)]*)?/media/image\d+\.[A-Za-z0-9]+", f"../docs/images/{code}_image_{idx}{ext}", full)
            new = temp_media_re.sub(repl_fn, new)

        if new != txt:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new)


def main():
    ensure_dirs()
    rebuild_all_from_docx()
    cleanup_markdown_files()
    # Keep only those listed in README identifiers
    allowed = load_allowed_codes_from_readme()
    if allowed:
        filter_sop_md_by_allowed_codes(allowed)
    print('Rebuilt SOP Markdown and images from DOCX with normalized naming and links.')


if __name__ == '__main__':
    main()

