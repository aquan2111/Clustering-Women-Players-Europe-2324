#!/usr/bin/env python3
"""Switch the links between the findings files to point at .md files or .pdf files.

    python switch_links.py md  findings      # links -> other .md files   (for GitHub / VS Code preview)
    python switch_links.py pdf findings      # links -> other .pdf files  (run before exporting to PDF)
    python switch_links.py pdf findings --out findings_pdf
                 # leave 'findings' untouched; write a copy of the whole tree to 'findings_pdf' with .pdf links
    add --dry-run to only report what would change

Only links to another local file are touched: href="name.pdf" <-> href="name.md".
In-page links (#...) and web links (http...) are left alone. Line endings are preserved.
Typical use: keep the .md files in 'md' mode in the repo; before a PDF export run 'pdf',
export, run fix_pdf_links.py on the PDFs, then run 'md' again.
"""
import argparse
import re
import sys
from pathlib import Path

LINK = re.compile(r'(href="(?!https?:|#|mailto:)[^"#]+)\.(md|pdf)(")')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["md", "pdf"])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--out", help="write converted copies of a single folder into this folder (same sub-folders) instead of editing in place")
    a = ap.parse_args()
    if a.out:
        assert len(a.paths) == 1 and Path(a.paths[0]).is_dir(), "--out needs exactly one source folder"
        src, out = Path(a.paths[0]).resolve(), Path(a.out).resolve()
        assert not str(out).startswith(str(src) + "/") and not str(src).startswith(str(out) + "/") and src != out, "source and --out must be separate folders"
        files = sorted(src.rglob("*.md"))
    else:
        files = []
        for p in map(Path, a.paths):
            files += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    total = 0
    for f in files:
        raw = f.read_bytes().decode("utf-8")
        new, n = LINK.subn(lambda m: f"{m.group(1)}.{a.mode}{m.group(3)}", raw)
        changed = sum(1 for m in LINK.finditer(raw) if m.group(2) != a.mode)
        total += changed
        if a.out:
            dest = out / f.relative_to(src)
            print(f"{dest}: {changed} link(s) -> .{a.mode}")
            if not a.dry_run:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(new.encode("utf-8"))
        elif changed:
            print(f"{f}: {changed} link(s) -> .{a.mode}")
            if not a.dry_run:
                f.write_bytes(new.encode("utf-8"))
    print(f"{'would change' if a.dry_run else 'changed'} {total} link(s) in {len(files)} file(s)")


if __name__ == "__main__":
    sys.exit(main())