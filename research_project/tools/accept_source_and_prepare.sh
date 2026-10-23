#!/usr/bin/env bash
# One command from "I have the PDF" to "Phase 1 can start".
#
#   bash research_project/tools/accept_source_and_prepare.sh /path/to/yadav.pdf
#
# Steps, stopping at the first failure:
#   1. stage the file in research_project/source_paper/ without touching the original
#   2. identify it; if it is NOT the source paper, unstage it and stop (nothing kept)
#   3. on success: keep the file, record its SHA-256, build the page-anchored corpus
#   4. run the preflight check and print the Phase 1 entry conditions
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
DROP="$ROOT/research_project/source_paper"

if [ $# -lt 1 ]; then
  echo "usage: bash research_project/tools/accept_source_and_prepare.sh <path-to-yadav-pdf>" >&2
  exit 2
fi
SRC="$1"
[ -f "$SRC" ] || { echo "no such file: $SRC" >&2; exit 2; }

mkdir -p "$DROP"
BASE="$(basename "$SRC")"
DEST="$DROP/$BASE"

if [ -e "$DEST" ]; then
  if cmp -s "$SRC" "$DEST"; then
    echo "1. already staged  $DEST"
  else
    echo "refusing to overwrite a different file at $DEST" >&2
    exit 2
  fi
else
  cp "$SRC" "$DEST" || { echo "copy failed" >&2; exit 2; }
  echo "1. staged  $DEST"
fi
echo "   sha256  $(sha256sum "$DEST" | awk '{print $1}')"
echo

echo "2. identifying ..."
python3 "$ROOT/research_project/tools/find_and_verify_source.py"
STATUS=$?
if [ $STATUS -ne 0 ]; then
  echo
  echo "NOT ACCEPTED (exit $STATUS). Removing the staged copy so the drop folder stays clean."
  rm -f "$DEST"
  echo "The original at $SRC was not modified."
  exit $STATUS
fi

echo
echo "3. recording and building the page-anchored corpus ..."
python3 "$ROOT/research_project/tools/find_and_verify_source.py" --record >/dev/null
python3 "$ROOT/research_project/tools/extract_source_text.py"
EXTRACT=$?
if [ $EXTRACT -ne 0 ]; then
  echo "corpus build failed (exit $EXTRACT)" >&2
  exit $EXTRACT
fi

echo
echo "4. preflight ..."
python3 "$ROOT/research_project/tools/preflight.py"

echo
echo "Next (Phase 1, blueprint §1A): state the version of this file — version of"
echo "record (Springer) or author deposit (HAL) — in SOURCE_PDF_MANIFEST.csv, then"
echo "build SOURCE_THEOREM_REGISTER.md from source_audit/source_text/."
