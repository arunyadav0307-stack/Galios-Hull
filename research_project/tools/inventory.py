#!/usr/bin/env python3
"""Generate a SHA-256 inventory of the repository artifacts and the extracted prior-art trees.

Usage:
    python3 research_project/tools/inventory.py > research_project/source_audit/FILE_MANIFEST.csv

The output is a CSV with columns:
    sha256, bytes, mtime_utc, origin, duplicate_of, path

`origin` is one of:
    repo-root              -- file tracked at the repository root
    prior-art/CompleteWork -- file extracted from Galios-Hull-Complete-Work-2026-10-20.zip
    prior-art/Phase10F     -- file extracted from Galios-Hull-Submission-Phase10F.zip

`duplicate_of` names an earlier path with the identical SHA-256 (empty when unique).
Nothing is written outside the repository; nothing is modified.
"""
import csv
import hashlib
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_ROOT = os.path.join(ROOT, "research_project", "prior_art")
ROOTS = [
    ("repo-root", ROOT, 1),                       # depth 1 = root files only
    ("prior-art/CompleteWork", os.path.join(CSV_ROOT, "Galios-Hull-Complete-Work-2026-10-20"), None),
    ("prior-art/Phase10F", os.path.join(CSV_ROOT, "Galios-Hull-kGalois-Phase10F"), None),
]
SKIP_DIRS = {".git", "prior_art", "__pycache__"}


def sha256(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def walk(origin, base, depth):
    if not os.path.isdir(base):
        return
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        rel_dir = os.path.relpath(dirpath, base)
        if depth is not None and rel_dir != ".":
            dirnames[:] = []
            continue
        for name in sorted(filenames):
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, ROOT)
            yield origin, rel, full


def main():
    rows = []
    seen = {}
    for origin, base, depth in ROOTS:
        for org, rel, full in walk(origin, base, depth):
            digest = sha256(full)
            st = os.stat(full)
            dup = seen.get(digest, "")
            seen.setdefault(digest, rel)
            rows.append(
                {
                    "sha256": digest,
                    "bytes": st.st_size,
                    "mtime_utc": datetime.fromtimestamp(st.st_mtime, timezone.utc)
                    .strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "origin": org,
                    "duplicate_of": dup,
                    "path": rel,
                }
            )
    rows.sort(key=lambda r: (r["origin"], r["path"]))
    out = csv.DictWriter(sys.stdout, fieldnames=["sha256", "bytes", "mtime_utc", "origin", "duplicate_of", "path"])
    out.writeheader()
    out.writerows(rows)


if __name__ == "__main__":
    main()
