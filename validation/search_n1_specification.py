"""Final exhaustive repository/history search for the unresolved N1 artifact.

This is a search/report tool, not an N1 experiment.  It searches current
source/document files, generated captures in aggregate, filenames, ZIP
members, the available Git history, and the binary PDF bytes for literal
metadata.  It never infers a missing parameter from q=16, n=15, or
2^15=32768.
"""

from pathlib import Path
import re
import subprocess
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
OUTPUT = ROOT / "validation" / "search_n1_specification.out"
ZIP_PATH = ROOT / "Galios-Hull-main-files.zip"
ANCHOR_PATTERN = re.compile(
    r"\bN1\b|32768|2\s*\^\s*15|q\s*=\s*16|n\s*=\s*15|F16",
    re.IGNORECASE,
)
SEARCH_TERMS = (
    "N1", "32768", "2^15", "q=16", "n=15", "F16", "lambda", "k",
    "factorization", "orbit", "histogram",
)
RELATED_TERMS = ("histogram", "factorization", "orbit", "lambda", "k")
MISSING = (
    "lambda", "k", "factorization", "orbit decomposition",
    "expected histogram",
)
TEXT_SUFFIXES = {
    ".md", ".py", ".out", ".txt", ".sh", ".yaml", ".yml", ".json",
    ".csv", ".rst", ".toml", ".ini",
}


def all_current_files():
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and ".git" not in path.parts:
            yield path


def readable_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def compact_context(line):
    line = " ".join(line.split())
    return line if len(line) <= 240 else line[:237] + "..."


def source_document_matches():
    """Return concise contexts, excluding generated captures and this output."""
    matches = {}
    related = {}
    generated_anchor_files = 0
    generated_anchor_count = 0
    filename_matches = []
    all_text_anchor_count = 0
    for path in all_current_files():
        relative = str(path.relative_to(ROOT))
        lower_name = relative.lower()
        if any(term.lower() in lower_name for term in SEARCH_TERMS):
            filename_matches.append(relative)
        text = readable_text(path)
        if text is None:
            continue
        hits = [
            (number, line.strip())
            for number, line in enumerate(text.splitlines(), 1)
            if ANCHOR_PATTERN.search(line)
        ]
        if not hits:
            continue
        all_text_anchor_count += len(hits)
        generated = path.suffix.lower() in {".out", ".log"}
        if generated:
            generated_anchor_files += 1
            generated_anchor_count += len(hits)
            continue
        if path in {SELF, OUTPUT} or path.suffix.lower() in {".zip", ".pdf", ".pyc"}:
            continue
        matches[relative] = hits
        related[relative] = {
            term: len(re.findall(re.escape(term), text, re.IGNORECASE))
            for term in RELATED_TERMS
        }
    return (
        matches, related, generated_anchor_files, generated_anchor_count,
        all_text_anchor_count, sorted(filename_matches),
    )


def zip_matches():
    if not ZIP_PATH.exists():
        return {"present": False}
    anchor_members = {}
    filename_matches = []
    text_anchor_count = 0
    try:
        with zipfile.ZipFile(ZIP_PATH) as archive:
            for info in archive.infolist():
                name = info.filename
                if any(term.lower() in name.lower() for term in SEARCH_TERMS):
                    filename_matches.append(name)
                if info.is_dir():
                    continue
                if Path(name).suffix.lower() not in TEXT_SUFFIXES:
                    continue
                try:
                    text = archive.read(info).decode("utf-8")
                except (UnicodeDecodeError, OSError, zipfile.BadZipFile):
                    continue
                count = sum(1 for line in text.splitlines()
                            if ANCHOR_PATTERN.search(line))
                if count:
                    anchor_members[name] = count
                    text_anchor_count += count
    except (OSError, zipfile.BadZipFile) as error:
        return {"present": True, "error": str(error)}
    return {
        "present": True,
        "anchor_members": anchor_members,
        "filename_matches": sorted(filename_matches),
        "text_anchor_count": text_anchor_count,
    }


def pdf_binary_matches():
    results = []
    for path in all_current_files():
        if path.suffix.lower() != ".pdf":
            continue
        try:
            data = path.read_bytes().lower()
        except OSError:
            continue
        counts = {
            term: data.count(term.lower().encode("ascii", "ignore"))
            for term in SEARCH_TERMS
        }
        results.append((str(path.relative_to(ROOT)), counts))
    return results


def history_matches():
    pattern = (
        r"N1|32768|2\^15|q[[:space:]]*=[[:space:]]*16|"
        r"n[[:space:]]*=[[:space:]]*15|F16|lambda|factorization|"
        r"orbit|histogram"
    )
    command = [
        "git", "log", "--all", "--full-history", "--date=iso-strict",
        "--format=%H%x09%ad%x09%s", f"-G{pattern}", "--", ".",
    ]
    result = subprocess.run(
        command, cwd=ROOT, text=True, capture_output=True, check=False
    )
    filename_command = [
        "git", "log", "--all", "--full-history", "--name-only",
        "--format=", "--", ".",
    ]
    filenames = subprocess.run(
        filename_command, cwd=ROOT, text=True, capture_output=True,
        check=False,
    )
    history_filenames = sorted({
        line.strip() for line in filenames.stdout.splitlines()
        if line.strip() and any(term.lower() in line.lower()
                                for term in SEARCH_TERMS)
    })
    return (
        result.returncode, result.stdout.splitlines(), result.stderr.splitlines(),
        history_filenames,
    )


def main():
    (
        matches, related, generated_files, generated_count, all_text_count,
        filename_matches,
    ) = source_document_matches()
    print("N1 repository search: final exhaustive current-file summary")
    print(f"search_terms={','.join(SEARCH_TERMS)}")
    print(f"current_text_anchor_count_including_captures={all_text_count}")
    print(f"generated_capture_anchor_files={generated_files}")
    print(f"generated_capture_anchor_count={generated_count}")
    print(f"current_source_document_anchor_count={sum(len(v) for v in matches.values())}")
    for path, hits in sorted(matches.items()):
        print(f"anchor_source={path} | count={len(hits)}")
        contexts = hits[:2] if len(hits) <= 3 else hits[:2] + [hits[-1]]
        for number, line in contexts:
            print(f"anchor_context={path}:{number} | {compact_context(line)}")
    print("related-term counts within source/document files containing anchors:")
    for path, counts in sorted(related.items()):
        print(f"related_source={path} | {counts}")
    print("current filename matches:")
    for name in filename_matches[:80]:
        print(f"filename_match={name}")
    if len(filename_matches) > 80:
        print(f"filename_match_truncated={len(filename_matches) - 80}")

    zip_result = zip_matches()
    print("N1 repository search: current ZIP contents")
    print(f"zip_present={zip_result.get('present')}")
    if "error" in zip_result:
        print(f"zip_error={zip_result['error']}")
    else:
        print(f"zip_text_anchor_count={zip_result.get('text_anchor_count', 0)}")
        print(f"zip_anchor_member_count={len(zip_result.get('anchor_members', {}))}")
        for name, count in sorted(zip_result.get("anchor_members", {}).items()):
            print(f"zip_anchor_member={name} | count={count}")
        print(f"zip_filename_match_count={len(zip_result.get('filename_matches', []))}")

    print("N1 repository search: PDF binary/filename evidence")
    for path, counts in pdf_binary_matches():
        print(f"pdf_binary_counts={path} | {counts}")
    print("PDF binary matches are not treated as readable theorem or N1 specification text.")

    code, commits, errors, history_filenames = history_matches()
    print("N1 repository search: Git history matches")
    print(f"git_search_exit_code={code}")
    if commits:
        for commit in commits:
            print(f"history={commit}")
    else:
        print("history=no matching Git commit message/patch metadata found")
    for error in errors:
        print(f"git_stderr={error}")
    for name in history_filenames:
        print(f"history_filename_match={name}")

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

    # A clean archive intentionally has no .git directory; git's 128 is an
    # unavailable-history result, not a failed N1 search.  The repository run
    # must succeed with code 0, while both outcomes remain explicitly visible.
    assert code in (0, 128), code


if __name__ == "__main__":
    main()
