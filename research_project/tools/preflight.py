#!/usr/bin/env python3
"""Pre-Phase-1 preflight: is the project ready to start Phase 1 the moment the PDF lands?

Checks, in order:
  1. repository identity (branch, HEAD, clean tree except known paths)
  2. source-appraisal files from Phase 0 exist and are non-empty
  3. the source PDF gate (delegates to find_and_verify_source.py logic)
  4. arithmetic/consistency of the recorded manifest and inventory counts
  5. availability of the tools Phase 1 needs (pypdf; optional sympy/galois)
  6. that no Phase 1 deliverable has been written prematurely

Exit status:
  0  ready: PDF accepted, Phase 1 may start
  1  not ready: PDF absent or rejected (everything else may still pass)
  2  broken: a Phase 0 artifact is missing or inconsistent

Usage:
  python3 research_project/tools/preflight.py [--quiet]
"""
import csv
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RP = os.path.join(ROOT, "research_project")

PHASE0_DELIVERABLES = [
    "PROJECT_PLAN.md",
    "PHASE_STATUS.md",
    "source_audit/SOURCE_INVENTORY.md",
    "source_audit/SOURCE_PAPER_METADATA.md",
    "source_audit/ENVIRONMENT_CAPABILITIES.md",
]
SUPPORTING = [
    "README.md",
    "source_audit/PHASE0_VERIFICATION_LOG.md",
    "source_audit/PRIOR_ART_REGISTER.md",
    "source_audit/SOURCE_ACCESS_STATUS.md",
    "source_audit/REPOSITORY_SOURCE_SEARCH.md",
    "source_audit/FILE_MANIFEST.csv",
    "source_audit/SOURCE_PDF_MANIFEST.csv",
]
PHASE1_DELIVERABLES = [
    "source_audit/SOURCE_THEOREM_REGISTER.md",
    "source_audit/SOURCE_MATHEMATICAL_AUDIT.md",
    "source_audit/SOURCE_NOTATION_GLOSSARY.md",
    "source_audit/SOURCE_EXAMPLE_RECALCULATION.md",
]

results = []          # (block, name, status, note)


def add(block, name, status, note=""):
    results.append((block, name, status, note))


def size(rel):
    p = os.path.join(RP, rel)
    return os.path.getsize(p) if os.path.isfile(p) else -1


def check_repo():
    def git(*a):
        return subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True).stdout.strip()
    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    head = git("rev-parse", "HEAD")
    dirty = [l for l in git("status", "--porcelain").splitlines() if l.strip()]
    add("repo", "branch", "INFO", branch)
    add("repo", "HEAD", "INFO", head[:12])
    add("repo", "working tree", "PASS" if not dirty else "WARN",
        "clean" if not dirty else f"{len(dirty)} uncommitted path(s)")


def check_files():
    for rel in PHASE0_DELIVERABLES:
        s = size(rel)
        add("phase0", rel, "PASS" if s > 0 else "FAIL", f"{s} B" if s > 0 else "missing or empty")
    for rel in SUPPORTING:
        s = size(rel)
        add("phase0", rel, "PASS" if s > 0 else "FAIL", f"{s} B" if s > 0 else "missing or empty")


def check_source_gate():
    """Run the finder without recording; classify the outcome."""
    code = subprocess.run(
        [sys.executable, os.path.join(RP, "tools", "find_and_verify_source.py")],
        capture_output=True, text=True, cwd=ROOT,
    )
    out = code.stdout
    tail = [l for l in out.splitlines() if l.startswith(("GATE 0", "PDFs examined", "  ACCEPTED"))]
    status = {0: "PASS", 1: "BLOCKED", 3: "BLOCKED"}.get(code.returncode, "FAIL")
    note = " | ".join(t.strip() for t in tail)[:160] or f"exit {code.returncode}"
    add("gate0", "source PDF identity", status, note)
    return code.returncode


def check_manifest_consistency():
    path = os.path.join(RP, "source_audit", "FILE_MANIFEST.csv")
    if not os.path.isfile(path):
        add("consistency", "FILE_MANIFEST.csv", "FAIL", "missing")
        return
    with open(path, newline="") as fh:
        rows = list(csv.DictReader(fh))
    by_origin = {}
    for r in rows:
        by_origin[r["origin"]] = by_origin.get(r["origin"], 0) + 1
    expect = {"repo-root": 3, "prior-art/CompleteWork": 155, "prior-art/Phase10F": 102}
    ok = all(by_origin.get(k) == v for k, v in expect.items())
    add("consistency", "inventory counts 3/155/102", "PASS" if ok else "FAIL", str(by_origin))

    dups = sum(1 for r in rows if r["duplicate_of"])
    add("consistency", "duplicate analysis", "PASS" if dups == 104 else "WARN",
        f"{dups} duplicate rows (expected 104)")


def check_tools():
    try:
        import pypdf
        add("tools", "pypdf (required)", "PASS", pypdf.__version__)
    except Exception:
        add("tools", "pypdf (required)", "FAIL", "not importable")
    for mod, role in (("sympy", "optional: exact algebra"), ("galois", "optional: finite fields")):
        try:
            m = __import__(mod)
            add("tools", f"{mod} ({role})", "PASS", getattr(m, "__version__", "?"))
        except Exception:
            add("tools", f"{mod} ({role})", "WARN", "absent; install with pip if needed")
    for exe, role in (("pdflatex", "Phase 9 only"), ("magma", "Phase 7 CAS")):
        found = subprocess.run(["bash", "-lc", f"command -v {exe}"], capture_output=True).returncode == 0
        add("tools", f"{exe} ({role})", "PASS" if found else "WARN",
            "present" if found else "absent — declare, do not simulate")


def check_no_premature_phase1():
    present = [r for r in PHASE1_DELIVERABLES if size(r) > 0]
    add("phase1", "no Phase 1 deliverable yet", "PASS" if not present else "FAIL",
        "none present" if not present else f"unexpected: {present}")


def main(argv):
    quiet = "--quiet" in argv
    check_repo()
    check_files()
    gate = check_source_gate()
    check_manifest_consistency()
    check_tools()
    check_no_premature_phase1()

    if not quiet:
        block = None
        for b, name, status, note in results:
            if b != block:
                print(f"\n[{b}]")
                block = b
            print(f"  {status:7} {name:46s} {note}")

    bad = [r for r in results if r[2] == "FAIL"]
    warn = [r for r in results if r[2] == "WARN"]
    print()
    print(f"summary: {sum(1 for r in results if r[2]=='PASS')} pass, {len(warn)} warn, {len(bad)} fail")

    if bad:
        print("\nRESULT: BROKEN — a Phase 0 artifact is missing or inconsistent.")
        return 2
    if gate == 0:
        print("\nRESULT: READY — source PDF accepted. Phase 1 may start.")
        print("Next: python3 research_project/tools/extract_source_text.py  (page-anchored corpus)")
        return 0
    print("\nRESULT: WAITING — Phase 0 is complete and consistent; Phase 1 is gated on the source PDF.")
    print("Next: put the Yadav et al. PDF in research_project/source_paper/ and run")
    print("      python3 research_project/tools/find_and_verify_source.py --record")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
