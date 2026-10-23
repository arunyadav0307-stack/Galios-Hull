#!/usr/bin/env bash
# Re-create research_project/prior_art/ from the two ZIP archives tracked at the
# repository root.  The extraction is deterministic in content: the SHA-256 of
# every extracted file is recorded in research_project/source_audit/FILE_MANIFEST.csv.
#
# The extracted tree is intentionally NOT tracked by Git (see .gitignore): it is
# a byte-for-byte copy of artifacts already committed as ZIPs, so tracking it
# again would duplicate ~5.6 MB.  Re-running this script restores it.
#
# Usage:  bash research_project/tools/extract_prior_art.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
DEST="$ROOT/research_project/prior_art"
mkdir -p "$DEST"

expected_complete="c192e76c43d828ad879a7bba8494b11b44981969a0a6295203e0d7ae389d3179"
expected_phase10f="6fd1a675fa4d780db71631156ddc8bd1554d517348ba24264bf2a0cccce2ad12"

check() {
  local file="$1" want="$2" got
  got="$(sha256sum "$ROOT/$file" | awk '{print $1}')"
  if [ "$got" != "$want" ]; then
    echo "REFUSING TO EXTRACT: $file has SHA-256 $got, expected $want" >&2
    exit 1
  fi
  echo "verified $file  $got"
}

check "Galios-Hull-Complete-Work-2026-10-20.zip" "$expected_complete"
check "Galios-Hull-Submission-Phase10F.zip" "$expected_phase10f"

python3 - "$ROOT" "$DEST" <<'PY'
import sys, zipfile, os
root, dest = sys.argv[1], sys.argv[2]
for z in ("Galios-Hull-Complete-Work-2026-10-20.zip", "Galios-Hull-Submission-Phase10F.zip"):
    with zipfile.ZipFile(os.path.join(root, z)) as zf:
        bad = zf.testzip()
        if bad is not None:
            raise SystemExit(f"corrupt member {bad} in {z}")
        zf.extractall(dest)
        print(f"extracted {z}: {len([n for n in zf.namelist() if not n.endswith('/')])} files")
PY

echo "done: contents under $DEST"
