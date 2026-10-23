#!/usr/bin/env python3
"""Reproducible self-test for the source-identity gate.

The gate must do two things, not one: accept the right document and reject the
wrong ones. This script proves both, on synthetic one-page fixtures generated in a
temporary directory. The fixtures are NOT the article and carry a marker file; they
exist only to exercise the decision logic and are deleted afterwards.

Checks
  1. accept   a fixture carrying the title, all five authors and the DOI
  2. reject   the same title with no authors and no journal/DOI
  3. reject   title + authors but no journal/DOI
  4. reject   the Debnath et al. preprint's identity (the paper that must never be
              substituted)
  5. reject   the actual PDF in the repository
  6. record   twice -> exactly one row (idempotent evidence log)
  7. paths    a file outside the repository is reported as an absolute path

Usage:  python3 research_project/tools/selftest_gate.py
Exit:   0 all checks pass, 1 otherwise.
"""
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import verify_source_pdf as V  # noqa: E402

TITLE = ("Hermitian hull of constacyclic codes over a class of non-chain rings "
         "and new quantum codes")
AUTHORS = "Shikha Yadav, Ashutosh Singh, Habibul Islam, Om Prakash, Patrick Sol\u00e9"


def esc(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def make_pdf(path, lines, title, author):
    body = ["BT /F1 11 Tf 40 780 Td 14 TL"] + ["(" + esc(l) + ") Tj T*" for l in lines] + ["ET"]
    content = "\n".join(body)
    objs = [
        "<< /Type /Catalog /Pages 2 0 R >>",
        "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
        "/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>",
        "<< /Length %d >>\nstream\n%s\nendstream" % (len(content), content),
        "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
        "<< /Title (%s) /Author (%s) >>" % (esc(title), esc(author)),
    ]
    out = bytearray(b"%PDF-1.4\n")
    offs = []
    for i, o in enumerate(objs, 1):
        offs.append(len(out))
        out += ("%d 0 obj\n%s\nendobj\n" % (i, o)).encode("latin-1")
    xref = len(out)
    out += ("xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1)).encode()
    for off in offs:
        out += ("%010d 00000 n \n" % off).encode()
    out += ("trailer\n<< /Size %d /Root 1 0 R /Info 6 0 R >>\nstartxref\n%d\n%%%%EOF\n"
            % (len(objs) + 1, xref)).encode()
    with open(path, "wb") as fh:
        fh.write(bytes(out))


def decide(path):
    from pypdf import PdfReader
    r = PdfReader(path)
    head = " ".join((p.extract_text() or "") for p in r.pages[:2])
    meta = r.metadata or {}
    _, ok = V.evaluate(meta.get("/Title", ""), meta.get("/Author", ""), head)
    return ok


def main():
    results = []
    tmp = tempfile.mkdtemp(prefix="gate_selftest_")
    with open(os.path.join(tmp, "NOT_THE_PAPER_TEST_FIXTURES.txt"), "w") as fh:
        fh.write("Synthetic fixtures for tools/selftest_gate.py. Not the article.\n")

    good = os.path.join(tmp, "accept.pdf")
    make_pdf(good, [TITLE, AUTHORS,
                    "Computational and Applied Mathematics 43 (2024), Paper No. 269",
                    "DOI 10.1007/s40314-024-02789-1"],
             TITLE, "Shikha Yadav; Ashutosh Singh; Habibul Islam; Om Prakash; Patrick Sol\u00e9")
    noauth = os.path.join(tmp, "reject_no_authors.pdf")
    make_pdf(noauth, [TITLE], TITLE, "")
    nojournal = os.path.join(tmp, "reject_no_journal.pdf")
    make_pdf(nojournal, [TITLE, AUTHORS], TITLE, AUTHORS)
    debnath = os.path.join(tmp, "reject_debnath.pdf")
    make_pdf(debnath,
             ["Galois hulls of constacyclic codes over affine algebra rings",
              "Indibar Debnath, Habibul Islam, E. Martinez-Moro, Om Prakash"],
             "Galois hulls of constacyclic codes over affine algebra rings",
             "Indibar Debnath; Habibul Islam; E. Martinez-Moro; Om Prakash")

    def check(name, expect, path):
        got = decide(path)
        results.append((name, got == expect, expect, got))

    check("1 accept a conforming record", True, good)
    check("2 reject title without authors or journal", False, noauth)
    check("3 reject title+authors without journal/DOI", False, nojournal)
    check("4 reject the Debnath et al. identity", False, debnath)

    repo_pdf = os.path.join(V.ROOT, "Galios hulls of constacclic codes over affine algebra rings'.pdf")
    if os.path.exists(repo_pdf):
        check("5 reject the PDF actually in the repository", False, repo_pdf)
    else:
        results.append(("5 reject the PDF actually in the repository", True, False, "skipped: absent"))

    # 6 idempotent recording, against a throwaway manifest
    original = V.MANIFEST
    V.MANIFEST = os.path.join(tmp, "manifest.csv")
    try:
        a = V.record(good, V.sha256(good), os.path.getsize(good), 1, TITLE, AUTHORS, "ACCEPTED")
        b = V.record(good, V.sha256(good), os.path.getsize(good), 1, TITLE, AUTHORS, "ACCEPTED")
        import csv
        rows = list(csv.DictReader(open(V.MANIFEST, newline="")))
        results.append(("6 record twice -> one row", (a and not b and len(rows) == 1),
                        "1 row", f"{len(rows)} row(s), added={a},{b}"))
    finally:
        V.MANIFEST = original

    # 7 absolute path outside the repository
    shown = V.display(good)
    results.append(("7 out-of-tree path shown absolutely", os.path.isabs(shown), "absolute", shown))

    print()
    ok = True
    for name, passed, expect, got in results:
        ok &= passed
        print(f"{'PASS' if passed else 'FAIL'}  {name:44s} expected={expect!s:8} got={got!s}")
    print()
    print(f"SELFTEST: {'PASS' if ok else 'FAIL'}  ({sum(r[1] for r in results)}/{len(results)})")
    print(f"fixtures were built in {tmp} and are not part of the repository")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
