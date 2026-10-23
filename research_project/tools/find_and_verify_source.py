#!/usr/bin/env python3
"""Find every PDF in the repository and report which one (if any) is the source paper.

This is the Phase 0 -> Phase 1 gate. It does not assume a filename or a location:
it walks the whole working tree (skipping .git), tests every *.pdf it finds with
the same identity logic as tools/verify_source_pdf.py, and prints one row per file.

Exit status:
    0  exactly one PDF passed identification  (recorded in SOURCE_PDF_MANIFEST.csv)
    1  no PDF passed identification           (Phase 1 must not start)
    3  more than one PDF passed               (ambiguous; human decision needed)

Usage:
    python3 research_project/tools/find_and_verify_source.py [--root DIR] [--record]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_source_pdf import evaluate, sha256, display, record, MANIFEST, ROOT  # noqa: E402

SKIP = {".git", "__pycache__", "node_modules"}
CANDIDATE_DIR = os.path.join(ROOT, "research_project", "source_paper")


def pdfs(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP)
        for name in sorted(filenames):
            if name.lower().endswith(".pdf"):
                yield os.path.join(dirpath, name)


def describe(path):
    """Return (pages, title, author, checks, ok) or None if unreadable."""
    try:
        with open(path, "rb") as fh:
            if fh.read(5) != b"%PDF-":
                return None
    except OSError:
        return None
    from pypdf import PdfReader
    try:
        r = PdfReader(path)
        n = len(r.pages)
        head = " ".join((r.pages[i].extract_text() or "") for i in range(min(2, n)))
        meta = r.metadata or {}
    except Exception:
        return None
    checks, ok = evaluate(meta.get("/Title", ""), meta.get("/Author", ""), head)
    return n, meta.get("/Title", ""), meta.get("/Author", ""), checks, ok


def main(argv):
    root = ROOT
    if "--root" in argv:
        root = argv[argv.index("--root") + 1]
    do_record = "--record" in argv

    rows, accepted = [], []
    for path in pdfs(root):
        info = describe(path)
        rel = display(path)
        if info is None:
            rows.append((rel, "-", "-", "UNREADABLE"))
            continue
        n, title, author, checks, ok = info
        verdict = "ACCEPT" if ok else "reject"
        reason = "" if ok else "; ".join(c[2] for c in checks if not c[1])[:90]
        rows.append((rel, str(n), verdict, reason))
        if ok:
            accepted.append(path)

    w = max((len(r[0]) for r in rows), default=10)
    print(f"{'PDF'.ljust(w)}  {'pp':>4}  {'verdict':7}  reason")
    print(f"{'-'*w}  {'-'*4}  {'-'*7}  {'-'*40}")
    for rel, n, verdict, reason in rows:
        print(f"{rel.ljust(w)}  {n:>4}  {verdict:7}  {reason}")

    print()
    print(f"PDFs examined: {len(rows)}   accepted: {len(accepted)}")
    for p in accepted:
        print(f"  ACCEPTED -> {display(p)}  sha256 {sha256(p)}")

    if len(accepted) == 1:
        if do_record:
            from pypdf import PdfReader
            p = accepted[0]
            info = describe(p)
            meta = PdfReader(p).metadata or {}
            added = record(p, sha256(p), os.path.getsize(p), info[0],
                           meta.get("/Title", ""), meta.get("/Author", ""), "ACCEPTED")
            print(f"  {'recorded ->' if added else 'already recorded ->'} "
                  f"{os.path.relpath(MANIFEST, ROOT)}")
        print("\nGATE 0: PASS (source file identified). Phase 1 may start on this file.")
        print("Next: tag the version (version of record vs author deposit) before registering theorems.")
        return 0
    if not accepted:
        print("\nGATE 0: BLOCKED — no PDF in the repository is the source paper.")
        print(f"Place the file in {os.path.relpath(CANDIDATE_DIR, ROOT)}/ (any name ending .pdf) and re-run.")
        return 1
    print("\nGATE 0: AMBIGUOUS — more than one PDF passed. Choose one explicitly.")
    return 3


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
