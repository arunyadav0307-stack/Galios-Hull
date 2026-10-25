"""
Regression check: re-run every probe in the repository and compare its output with the
committed log byte-for-byte (after removing elapsed-time lines).

Why this exists.  The project's claims rest on logs that were produced by earlier versions of
the scripts, across many commits.  Nothing so far proves that the committed scripts still
produce the committed logs.  This tool does exactly that, and reports any drift instead of
hiding it.

Usage:
    python3 tools/verify_logs.py            # run everything (slow: ~15 min, dominated by
                                            #   p3_power_attainment.py at ~760 s)
    python3 tools/verify_logs.py --fast     # skip the slow one
    python3 tools/verify_logs.py --only p3_ring_gray
    python3 tools/verify_logs.py --list

Exit code 0 only if every log reproduces exactly.

Normalisation.  Lines matching "[elapsed <number>s]" are dropped (wall-clock is not a claim).
Trailing whitespace is stripped and trailing blank lines are removed.  Nothing else is touched:
a one-character difference in a number is a failure.  The only other tolerated difference is the
shell-written banner on older logs (a timestamp, not a claim).

ASCII only, pure stdlib.
"""
import os
import re
import subprocess
import sys

# this file lives at <repo>/research_project/tools/verify_logs.py; all paths below are
# relative to the REPOSITORY root, so go up three levels.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Each case: name, parts = [(script, argv), ...], log path, slow?, artifacts = [paths that the
# script rewrites and which must come out byte-identical].
# Several phase-2 logs are *composites*: one file holding the output of two or three scripts,
# separated by "## <script>.py -- ..." headers written by the logging command.  Those are
# reconstructed by concatenating the parts, which is what the header says they are.
P2 = "research_project/phase2/"
P3 = "research_project/phase3/"
CASES = [
    ("r1_probe", [(P2 + "r1_probe/r1_probe.py", []),
                  (P2 + "r1_probe/r1_orbit_check.py", [])],
     P2 + "r1_probe/r1_probe_log.txt", False, []),
    ("r2_probe", [(P2 + "r2_probe/r2_probe.py", [])],
     P2 + "r2_probe/r2_probe_log.txt", False, []),
    ("r3_probe", [(P2 + "r3_probe/r3_probe.py", []),
                  (P2 + "r3_probe/r3_dual_formula.py", []),
                  (P2 + "r3_probe/r3_hull_dim_check.py", [])],
     P2 + "r3_probe/r3_probe_log.txt", False, []),
    ("r4_probe", [(P2 + "r4_probe/r4_probe.py", [])],
     P2 + "r4_probe/r4_probe_log.txt", False, []),
    ("r4_field_joint", [(P3 + "r4_field_joint.py", [])],
     P3 + "r4_field_joint_log.txt", False, []),
    ("p3_tables", [(P3 + "p3_tables.py", [])],
     P3 + "p3_tables_log.txt", False, []),
    ("p3_ring_gray", [(P3 + "p3_ring_gray.py", [])],
     P3 + "p3_ring_gray_log.txt", False, []),
    ("p3_quantum_dist", [(P3 + "p3_quantum_dist.py", [])],
     P3 + "p3_quantum_dist_log.txt", False, []),
    ("p3_quantum_table", [(P3 + "p3_quantum_table.py", [])],
     P3 + "p3_quantum_table_log.txt", False,
     [P3 + "QUANTUM_CODE_PARAMETER_TABLE.csv"]),
    ("p3_gray_hull_identity", [(P3 + "p3_gray_hull_identity.py", [])],
     P3 + "p3_gray_hull_identity_log.txt", False, []),
    ("p3_known_formula_check", [(P3 + "p3_known_formula_check.py", [])],
     P3 + "p3_known_formula_check_log.txt", False, []),
    ("p3_weight2_field", [(P3 + "p3_weight2_field.py", [])],
     P3 + "p3_weight2_field_log.txt", False, []),
    ("p3_nested_gray", [(P3 + "p3_nested_gray.py", [])],
     P3 + "p3_nested_gray_log.txt", True, []),
    ("p3_power_attainment_mbound", [(P3 + "p3_power_attainment.py", ["--mbound"])],
     P3 + "p3_power_attainment_mbound_log.txt", False, []),
    ("p3_power_attainment", [(P3 + "p3_power_attainment.py", [])],
     P3 + "p3_power_attainment_log.txt", True, []),
]

ELAPSED = re.compile(r"\[elapsed [0-9.]+s\]")
# Older logs begin with a shell-written banner, e.g.
#   "# P3-3 ring-level Gray coupling log -- generated 2026-10-24T00:09:08Z"
# The generator scripts do not print it; it was added by the logging command. Drop exactly that
# shape of line, and nothing else: a changed *number* in the body is still a failure.
BANNER = re.compile(r"^#\s.*\blog\b.*(--|generated).*\d{4}-\d{2}-\d{2}T")
# ... followed by one interpreter line ("Python 3.11.2" or "# python3 Python 3.11.2") and a blank
# line, also added by the logging command rather than by the script.
PYLINE = re.compile(r"^(#\s*python3\s+)?Python \d+\.\d+(\.\d+)?\s*$")


# Composites carry a "## <script>.py -- <description>" header per part, written by the logging
# command, not by the scripts.
SECTION = re.compile(r"^## (?:[0-9]+\. )?[A-Za-z0-9_]+\.py -- ")
# p3_quantum_table_log.txt deliberately preserves a pre-rewrite failure (the numpy-free rewrite is
# recorded right after it, in the same file).  It is history, not current output.
LEGACY_FAILURE = re.compile(r"^numpy: ModuleNotFoundError")
# ... and ends with a dump of the generated CSV, which is checked separately, byte-for-byte.
CSV_DUMP_MARKER = "## csv head"


def normalise(text):
    out = []
    skip_blank = False
    for line in text.splitlines():
        if ELAPSED.search(line):
            continue
        if BANNER.match(line):
            continue
        if SECTION.match(line):
            # the logging command printed the header on its own, surrounded by blank lines;
            # drop the blank line on each side together with the header.
            if out and not out[-1]:
                out.pop()
            skip_blank = True
            continue
        if skip_blank and not line.strip():
            skip_blank = False
            continue
        skip_blank = False
        if LEGACY_FAILURE.match(line):
            continue
        if line.strip() == CSV_DUMP_MARKER:
            break
        out.append(line.rstrip())
    # drop the shell-written preamble at the head only (banner, interpreter line, blanks)
    while out and (BANNER.match(out[0].replace("\n", "")) or PYLINE.match(out[0]) or not out[0].strip()):
        if BANNER.match(out[0]) or PYLINE.match(out[0]) or not out[0].strip():
            out.pop(0)
        else:
            break
    while out and not out[-1]:
        out.pop()
    return out


def first_diff(got, want):
    """Return a short human description of the first difference, or None."""
    for i in range(max(len(got), len(want))):
        g = got[i] if i < len(got) else "<end of output>"
        w = want[i] if i < len(want) else "<end of log>"
        if g != w:
            return i + 1, g, w
    return None


def run_case(name, parts, logpath, timeout=1700, artifacts=()):
    env = dict(os.environ)
    env["PYTHONHASHSEED"] = "0"          # determinism for any set/dict ordering

    before = {}
    for a in artifacts:
        ap = os.path.join(ROOT, a)
        before[a] = open(ap, "rb").read() if os.path.exists(ap) else None

    collected = []
    for script, argv in parts:
        cmd = [sys.executable, "-u", os.path.join(ROOT, script)] + argv
        try:
            proc = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True,
                                  text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            return "TIMEOUT", f"{script} exceeded {timeout}s"
        if proc.returncode != 0:
            tail = (proc.stderr or "").strip().splitlines()[-1:] or ["(no stderr)"]
            return "ERROR", f"{script} exit {proc.returncode}: {tail[0]}"
        collected.extend(normalise(proc.stdout))

    log_abs = os.path.join(ROOT, logpath)
    if not os.path.exists(log_abs):
        return "MISSING LOG", logpath
    with open(log_abs, encoding="utf-8", errors="replace") as fh:
        want = normalise(fh.read())

    d = first_diff(collected, want)
    if d is not None:
        lineno, g, w = d
        return "DIFF", f"first diff at line {lineno}: got {g!r} / log {w!r}"

    for a in artifacts:
        ap = os.path.join(ROOT, a)
        after = open(ap, "rb").read() if os.path.exists(ap) else None
        if after != before[a]:
            return "ARTIFACT DRIFT", f"{a} changed on re-run"

    extra = " + artifacts byte-identical" if artifacts else ""
    return "PASS", f"{len(want)} lines identical{extra}"


def main():
    args = sys.argv[1:]
    if "--list" in args:
        for name, parts, log, slow, artifacts in CASES:
            desc = " ; ".join(p + (" " + " ".join(a) if a else "") for p, a in parts)
            print(f"{name:30s} {'SLOW' if slow else '    '}  {desc}")
        return 0
    fast = "--fast" in args
    only = None
    if "--only" in args:
        only = args[args.index("--only") + 1]

    print("Regression check: re-run each probe, compare with the committed log")
    print("(elapsed-time lines dropped; everything else compared exactly)")
    print()
    print(f"{'probe':30s} {'status':11s} detail")
    print("-" * 100)
    failures = 0
    ran = 0
    skipped = 0
    for name, parts, log, slow, artifacts in CASES:
        if only and only not in name:
            continue
        if fast and slow:
            skipped += 1
            print(f"{name:30s} {'SKIPPED':11s} slow case, not run under --fast")
            continue
        missing = [sc for sc, _ in parts if not os.path.exists(os.path.join(ROOT, sc))]
        if missing:
            failures += 1
            print(f"{name:30s} {'NO SCRIPT':11s} {missing[0]}")
            continue
        status, detail = run_case(name, parts, log, artifacts=artifacts)
        ran += 1
        if status != "PASS":
            failures += 1
        print(f"{name:30s} {status:11s} {detail}")
    print("-" * 100)
    print(f"ran {ran}, skipped {skipped}, failures {failures}")
    print("RESULT:", "ALL LOGS REPRODUCE" if failures == 0 else f"{failures} DID NOT REPRODUCE")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
