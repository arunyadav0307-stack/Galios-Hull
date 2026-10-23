#!/usr/bin/env python3
"""Verify that a supplied PDF really is the blueprint's source paper (Yadav et al.).

The blueprint names exactly one source paper:

    Yadav, Singh, Islam, Prakash, Sole,
    "Hermitian hull of constacyclic codes over a class of non-chain rings
     and new quantum codes",
    Computational and Applied Mathematics 43 (2024), Paper 269,
    DOI 10.1007/s40314-024-02789-1

This script refuses to accept any other document. In particular it rejects the
Debnath et al. preprint already in the repository, which is a different paper
(different ring, different inner product, different theorems).

Usage:
    python3 research_project/tools/verify_source_pdf.py <path-to-pdf> [--record]
    python3 research_project/tools/verify_source_pdf.py --selftest

Exit status:
    0  identity checks passed (or selftest passed)
    1  the file is not the expected paper
    2  the file is missing, unreadable, or not a PDF

With --record, an identification record is appended to
research_project/source_audit/SOURCE_PDF_MANIFEST.csv.
No file is ever modified or renamed.
"""
import csv
import hashlib
import os
import re
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MANIFEST = os.path.join(ROOT, "research_project", "source_audit", "SOURCE_PDF_MANIFEST.csv")

DOI = "10.1007/s40314-024-02789-1"
EXPECTED_TITLE = ("hermitian hull of constacyclic codes over a class of "
                  "non-chain rings and new quantum codes")
TITLE_PREFIX = "hermitian hull of constacyclic codes over a class of non-chain"
EXPECTED_SURNAMES = ["yadav", "singh", "islam", "prakash", "sol"]
JOURNAL = "computational and applied mathematics"

LIGATURES = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi",
             "\ufb04": "ffl", "\ufb05": "ft", "\ufb06": "st"}

IMPERSONATORS = [
    ("debnath", "galois hulls of constacyclic codes over affine algebra rings"),
]


def norm(s):
    s = s or ""
    for lig, rep in LIGATURES.items():
        s = s.replace(lig, rep)
    s = s.replace("\u00ad", "")          # soft hyphen
    for ch in ("\u2010", "\u2011", "\u2013", "\u2014"):
        s = s.replace(ch, "-")           # hyphen / dash variants
    return re.sub(r"\s+", " ", s).strip().lower()


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def evaluate(meta_title, meta_author, raw_text):
    """Return (checks, ok) for already-normalised or raw inputs."""
    mt, ma, tx = norm(meta_title), norm(meta_author), norm(raw_text)

    impersonator = None
    for surname, fragment in IMPERSONATORS:
        if (surname in ma or surname in tx) and (fragment in mt or fragment in tx):
            impersonator = f'{surname.title()} et al. "{fragment}"'
            break

    title_hit = EXPECTED_TITLE in mt or EXPECTED_TITLE in tx or TITLE_PREFIX in mt or TITLE_PREFIX in tx
    missing = [a for a in EXPECTED_SURNAMES if a not in ma and a not in tx]
    has_doi = DOI in raw_text or "10.1007/s40314-024-02789" in raw_text
    has_journal = JOURNAL in tx or JOURNAL in mt

    checks = [
        ("A  is not a known wrong paper", impersonator is None,
         "no wrong-paper signature" if impersonator is None else f"this is {impersonator}"),
        ("B  expected title found", title_hit,
         "metadata title" if EXPECTED_TITLE in mt else
         ("page text" if EXPECTED_TITLE in tx else
          ("partial page text" if title_hit else "title not found"))),
        ("C  all five authors present", not missing,
         "all present" if not missing else f"missing {missing}"),
        ("D  journal or DOI identity", has_doi or has_journal,
         "DOI found" if has_doi else ("journal name found" if has_journal else "neither found")),
    ]
    ok = impersonator is None and title_hit and not missing and (has_doi or has_journal)
    return checks, ok


def informational(raw_text):
    tx = norm(raw_text)
    flat = tx.replace(" ", "")
    patterns = [r"u\s*e\s*=\s*1", r"u\^e\s*=\s*1", r"η\s*1\s*α\s*1", r"e\s*\|\s*\(?\s*q\s*\+\s*1"]
    hits = [p for p in patterns if re.search(p, tx)]
    return [
        ("info ring R_e / e|(q+1) signal", bool(hits),
         f"matched {hits}" if hits else "not detected on pp. 1-2 (informational only)"),
        ("info dual-containing discussed", "dual-containing" in flat or "dual containing" in tx,
         "present" if ("dual-containing" in flat or "dual containing" in tx) else "not on pp. 1-2"),
    ]


def selftest():
    good_title = "Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes"
    good_text = ("Shikha Yadav, Ashutosh Singh, Habibul Islam, Om Prakash, Patrick Solé. "
                 "Computational and Applied Mathematics 43 (2024) 269. "
                 "DOI 10.1007/s40314-024-02789-1. Let p be a prime, q=p^m, "
                 "R_e = F_{q^2}+uF_{q^2}+...+u^{e-1}F_{q^2}, u^e=1, e|(q+1).")
    bad_title = "Galois hulls of constacyclic codes over affine algebra rings"
    bad_text = "Indibar Debnath, Habibul Islam, E. Martinez-Moro, Om Prakash. arXiv:2412.08512v1."

    cases = [
        ("accepts a conforming record", good_title, "Yadav; Singh; Islam; Prakash; Sole", good_text, True),
        ("rejects the Debnath preprint", bad_title, "Indibar Debnath; Habibul Islam", bad_text, False),
        ("rejects a right-title/right-author document without journal or DOI",
         good_title, "Yadav; Singh; Islam; Prakash; Sole",
         "Shikha Yadav, Ashutosh Singh, Habibul Islam, Om Prakash, Patrick Solé.", False),
    ]
    failures = 0
    for name, mt, ma, tx, expect in cases:
        checks, ok = evaluate(mt, ma, tx)
        status = "PASS" if ok == expect else "FAIL"
        if ok != expect:
            failures += 1
        print(f"{status}  {name:62s} expected={'accept' if expect else 'reject'} got={'accept' if ok else 'reject'}")
    print()
    print("SELFTEST:", "PASS" if failures == 0 else f"FAIL ({failures} case(s))")
    return 0 if failures == 0 else 1



def display(path):
    """Absolute path when outside the repository, repository-relative otherwise."""
    rel = os.path.relpath(path, ROOT)
    return rel if not rel.startswith("..") else os.path.abspath(path)


FIELDS = ["recorded_utc", "path", "sha256", "bytes", "pages",
          "pdf_title", "pdf_author", "verdict"]


def record(path, digest, size, npages, title, author, verdict):
    """Append one identification record, idempotently.

    A row is written only if no existing row carries the same SHA-256 *and* verdict,
    so re-running the gate never inflates the evidence file. The rewrite is atomic.
    Returns True when a row was added.
    """
    rows = []
    if os.path.exists(MANIFEST):
        with open(MANIFEST, newline="") as fh:
            rows = [r for r in csv.DictReader(fh) if r.get("sha256")]
    if any(r["sha256"] == digest and r.get("verdict") == verdict for r in rows):
        return False
    rows.append({
        "recorded_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "path": display(path),
        "sha256": digest,
        "bytes": size,
        "pages": npages,
        "pdf_title": title or "",
        "pdf_author": author or "",
        "verdict": verdict,
    })
    tmp = MANIFEST + ".tmp"
    with open(tmp, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, MANIFEST)
    return True

def main(argv):
    if "--selftest" in argv[1:]:
        return selftest()
    if len(argv) < 2:
        print(__doc__)
        return 2
    path = argv[1]
    do_record = "--record" in argv[2:]

    if not os.path.isfile(path):
        print(f"FAIL  file not found: {path}")
        return 2
    with open(path, "rb") as fh:
        if fh.read(5) != b"%PDF-":
            print(f"FAIL  not a PDF (bad magic): {path}")
            return 2

    from pypdf import PdfReader

    try:
        reader = PdfReader(path)
        npages = len(reader.pages)
        head = " ".join((reader.pages[i].extract_text() or "") for i in range(min(2, npages)))
        meta = reader.metadata or {}
    except Exception as exc:  # a corrupt PDF is a blocker, not a result
        print(f"FAIL  unreadable PDF: {exc}")
        return 2

    digest, size = sha256(path), os.path.getsize(path)
    print(f"file        {path}")
    print(f"bytes       {size}")
    print(f"sha256      {digest}")
    print(f"pages       {npages}")
    print(f"pdf_title   {meta.get('/Title')!r}")
    print(f"pdf_author  {meta.get('/Author')!r}")
    print()

    checks, ok = evaluate(meta.get("/Title", ""), meta.get("/Author", ""), head)
    for name, passed, note in checks + informational(head):
        print(f"{'PASS' if passed else 'FAIL'}  {name:34s} {note}")

    print()
    if ok:
        print("VERDICT: ACCEPTED — identity consistent with DOI 10.1007/s40314-024-02789-1")
        print("NOTE   Identity is not version. Record whether this file is the version of record")
        print("       (Springer PDF) or an author/submitted version (e.g. the HAL deposit);")
        print("       theorem numbering may differ between them.")
    else:
        print("VERDICT: REJECTED — this file is not the paper named by the blueprint.")
        print("         Phase 1 must not start on it.")

    if do_record:
        added = record(path, digest, size, npages, meta.get("/Title", ""),
                       meta.get("/Author", ""), "ACCEPTED" if ok else "REJECTED")
        print(f"{'recorded ->' if added else 'already recorded ->'} "
              f"{os.path.relpath(MANIFEST, ROOT)}")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
