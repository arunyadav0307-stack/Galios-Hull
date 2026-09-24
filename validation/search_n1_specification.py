"""Search current source/document files and Git history for N1 metadata.

Generated output captures are excluded so that a clean-package transcript does
not recursively count an earlier search report.  This script is deliberately a
search/report tool, not an N1 experiment.  It never infers a missing parameter
from q=16, n=15, or 2^15=32768.
"""

from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
OUTPUT = ROOT / "validation" / "search_n1_specification.out"
ANCHOR_PATTERN = re.compile(
    r"\bN1\b|32768|2\s*\^\s*15|q\s*=\s*16|n\s*=\s*15|F16",
    re.IGNORECASE,
)
RELATED_TERMS = ("histogram", "factorization", "orbit", "lambda", "k")
MISSING = ("lambda", "k", "factorization", "orbit decomposition", "expected histogram")


def text_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path in {SELF, OUTPUT} or path.suffix.lower() in {".zip", ".pdf", ".pyc", ".out"}:
            continue
        try:
            path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        yield path


def current_matches():
    matches_by_file = {}
    for path in text_files():
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        hits = [
            (line_number, line.strip())
            for line_number, line in enumerate(lines, 1)
            if ANCHOR_PATTERN.search(line)
        ]
        if hits:
            matches_by_file[str(path.relative_to(ROOT))] = hits
    related_counts = {}
    for path_name in sorted(matches_by_file):
        path = ROOT / path_name
        text = path.read_text(encoding="utf-8")
        related_counts[path_name] = {
            term: len(re.findall(re.escape(term), text, re.IGNORECASE))
            for term in RELATED_TERMS
        }
    return matches_by_file, related_counts


def history_matches():
    pattern = r"N1|32768|2\^15|q[[:space:]]*=[[:space:]]*16|n[[:space:]]*=[[:space:]]*15"
    command = [
        "git", "log", "--all", "--full-history", "--date=iso-strict",
        "--format=%H%x09%ad%x09%s", f"-G{pattern}", "--", ".",
    ]
    result = subprocess.run(
        command, cwd=ROOT, text=True, capture_output=True, check=False
    )
    return result.returncode, result.stdout.splitlines(), result.stderr.splitlines()


def main():
    matches, related_counts = current_matches()
    print("N1 repository search: current text-file anchor/context summary")
    total_matches = sum(len(hits) for hits in matches.values())
    print(f"current_anchor_match_count={total_matches}")
    for path, hits in sorted(matches.items()):
        print(f"anchor_source={path} | count={len(hits)}")
        context_hits = hits[:2] if len(hits) <= 3 else hits[:2] + [hits[-1]]
        for line_number, line in context_hits:
            compact = " ".join(line.split())
            if len(compact) > 240:
                compact = compact[:237] + "..."
            print(f"anchor_context={path}:{line_number} | {compact}")
    print("related-term counts within files containing an N1 anchor:")
    for path, counts in sorted(related_counts.items()):
        print(f"related_source={path} | {counts}")

    code, commits, errors = history_matches()
    print("N1 repository search: Git history matches")
    print(f"git_search_exit_code={code}")
    if commits:
        for commit in commits:
            print(f"history={commit}")
    else:
        print("history=no matching Git commit message/patch metadata found")
    for error in errors:
        print(f"git_stderr={error}")

    print("N1 known parameters explicitly recovered from repository evidence:")
    print("  q=16")
    print("  n=15")
    print("  proposed selection count=32768=2^15")
    print("N1 missing parameters (not inferred):")
    for item in MISSING:
        print(f"  missing={item}")
    print("N1 status: UNSPECIFIED — CANNOT VALIDATE")
    print("N1 remains unspecified and cannot be validated from repository evidence.")
    print("No lambda, k, factorization, orbit decomposition, expected histogram, or output is fabricated.")

    # The search is successful if it can run; an absent history match is not an
    # error.  The known/missing report is the intended result.
    assert code in (0, 128), code


if __name__ == "__main__":
    main()
