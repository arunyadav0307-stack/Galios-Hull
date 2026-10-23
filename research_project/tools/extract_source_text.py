#!/usr/bin/env python3
"""Build a page-anchored text corpus and a draft heading index for Phase 1.

Phase 1 needs every statement tied to a page of the source paper. This script does
the mechanical part only:

  * extracts the text of each page, one file per page, named page_NNN.txt
  * records per-page statistics
  * lists every line that starts a numbered statement (Theorem / Lemma / ...),
    with its page and a raw heading snippet

It performs **no interpretation**. The output index is DRAFT, UNAUDITED, and exists
only so that the Phase 1 theorem register can be built against fixed page anchors.
Nothing in the output may be quoted as mathematics until it has been checked by
hand against the PDF.

Gating: by default the script refuses to run unless the given PDF passes the source
identity check (tools/verify_source_pdf.py). --force exists only to test the
mechanics on a throwaway file; forced output is stamped UNAUDITED-NOT-THE-SOURCE.

Usage:
    python3 research_project/tools/extract_source_text.py [--pdf FILE] [--out DIR] [--force]
"""
import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_source_pdf import evaluate, sha256  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_OUT = os.path.join(ROOT, "research_project", "source_audit", "source_text")

HEADING = re.compile(
    r"^\s*(Theorem|Lemma|Proposition|Corollary|Definition|Example|Remark|Table|Algorithm)"
    r"\s*([0-9]+(?:\.[0-9]+)*)?\s*[.:]?",
    re.IGNORECASE,
)


def accepted_pdf_from_manifest():
    path = os.path.join(ROOT, "research_project", "source_audit", "SOURCE_PDF_MANIFEST.csv")
    if not os.path.isfile(path):
        return None
    with open(path, newline="") as fh:
        rows = [r for r in csv.DictReader(fh) if r.get("verdict") == "ACCEPTED"]
    if not rows:
        return None
    return os.path.join(ROOT, rows[-1]["path"])


def identify(pdf):
    from pypdf import PdfReader
    r = PdfReader(pdf)
    n = len(r.pages)
    head = " ".join((r.pages[i].extract_text() or "") for i in range(min(2, n)))
    meta = r.metadata or {}
    checks, ok = evaluate(meta.get("/Title", ""), meta.get("/Author", ""), head)
    return r, meta, checks, ok


def main(argv):
    pdf = argv[argv.index("--pdf") + 1] if "--pdf" in argv else accepted_pdf_from_manifest()
    out = argv[argv.index("--out") + 1] if "--out" in argv else DEFAULT_OUT
    force = "--force" in argv

    if not pdf or not os.path.isfile(pdf):
        print("No source PDF available.")
        print("Run research_project/tools/find_and_verify_source.py --record first,")
        print("or pass --pdf FILE.")
        return 1

    reader, meta, checks, ok = identify(pdf)
    if not ok and not force:
        print(f"REFUSING: {os.path.relpath(pdf, ROOT)} is not the source paper.")
        for name, passed, note in checks:
            print(f"  {'PASS' if passed else 'FAIL'}  {name:34s} {note}")
        print("Run the verifier for the full report. Use --force only to test mechanics.")
        return 1

    stamp = "" if ok else "UNAUDITED-NOT-THE-SOURCE: "
    pages_dir = os.path.join(out, "pages")
    os.makedirs(pages_dir, exist_ok=True)

    page_rows, heading_rows = [], []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        with open(os.path.join(pages_dir, f"page_{i:03d}.txt"), "w") as fh:
            fh.write(text)
        page_rows.append({"page": i, "chars": len(text), "lines": text.count("\n") + 1,
                          "empty": int(not text.strip())})
        for line in text.splitlines():
            m = HEADING.match(line)
            if m:
                number = (m.group(2) or "").strip()
                heading_rows.append({
                    "page": i,
                    "kind": m.group(1).capitalize(),
                    "number": number,
                    "confidence": "high" if number else "low",
                    "line_head": re.sub(r"\s+", " ", line.strip())[:110],
                })

    with open(os.path.join(out, "PAGE_INDEX.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["page", "chars", "lines", "empty"])
        w.writeheader()
        w.writerows(page_rows)

    with open(os.path.join(out, "HEADING_INDEX.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["page", "kind", "number", "confidence", "line_head"])
        w.writeheader()
        w.writerows(heading_rows)

    with open(os.path.join(out, "CORPUS_META.txt"), "w") as fh:
        fh.write(f"{stamp}source      {os.path.relpath(pdf, ROOT)}\n")
        fh.write(f"{stamp}sha256      {sha256(pdf)}\n")
        fh.write(f"{stamp}pages       {len(reader.pages)}\n")
        fh.write(f"{stamp}pdf_title   {meta.get('/Title')!r}\n")
        fh.write(f"{stamp}pdf_author  {meta.get('/Author')!r}\n")
        fh.write("status      DRAFT — page anchors only; no statement has been audited\n")
        fh.write("rule        every Phase 1 claim must cite <file> p.N and be checked by hand\n")

    kinds = {}
    for h in heading_rows:
        kinds[h["kind"]] = kinds.get(h["kind"], 0) + 1
    print(f"{stamp}corpus written to {os.path.relpath(out, ROOT)}")
    print(f"  pages          {len(page_rows)}")
    print(f"  empty pages    {sum(r['empty'] for r in page_rows)}")
    print(f"  heading lines  {len(heading_rows)}  {kinds}")
    high = sum(1 for h in heading_rows if h["confidence"] == "high")
    print(f"  numbered       {high} high-confidence, {len(heading_rows) - high} low (manual triage)")
    print("  NOTE these are line-level candidates, not verified statements.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
