# research_project/ — Hull-Dimension Enumeration over Finite Rings

A phase-gated, proof-first research project executed under the **Arena Master
Research Blueprint** (7 pp., SHA-256 `abcecc47…ae23`, `arunyadav0307-stack/JOINT@main`).

**Current status: Phase 0 complete · source of record designated (Yadav et al.,
CAM 43:269, 2024) · Gate 0 still BLOCKED because that paper's full text is not yet
in the workspace.** No Phase 1 work has begun. See `PHASE_STATUS.md` and
`source_audit/SOURCE_ACCESS_STATUS.md`.

---

## Read in this order

| # | File | What it settles |
|---|---|---|
| 1 | `PHASE_STATUS.md` | what passed, what is blocked, what is unresolved, what happens next |
| 2 | `source_audit/SOURCE_ACCESS_STATUS.md` | what is needed to unblock Phase 1, and every access route tried |
| 3 | `source_audit/SOURCE_IDENTITY_BLOCKER.md` | the source-identity issue and its recorded resolution |
| 4 | `PROJECT_PLAN.md` | scope, phase/gate table, rules, assumptions, risks |
| 5 | `source_audit/SOURCE_INVENTORY.md` | every file, hash, archive and prior document in the workspace |
| 6 | `source_audit/SOURCE_PAPER_METADATA.md` | the three distinct papers in play and their access status |
| 7 | `source_audit/ENVIRONMENT_CAPABILITIES.md` | what the sandbox can and cannot do |
| 8 | `source_audit/PRIOR_ART_REGISTER.md` | the earlier work found in the ZIPs and how it is treated |
| 9 | `source_audit/PHASE0_VERIFICATION_LOG.md` | commands, outputs, exit codes behind every claim above |

## The short version

* The blueprint names **Yadav, Singh, Islam, Prakash, Solé**, *Comput. Appl. Math.*
  **43** (2024) 269, DOI `10.1007/s40314-024-02789-1` as its source paper.
* The uploaded PDF is **Debnath, Islam, Martínez-Moro, Prakash**, *Galois hulls of
  constacyclic codes over affine algebra rings*, arXiv:2412.08512v1 / *Discrete
  Math.* **349**(2) (2026) 114750 — a different ring, a different ($k$-Galois)
  inner product, and different theorems. It cites the blueprint's paper as [43].
* The blueprint's paper is **the designated source of record**, but it is not in
  the workspace and this agent cannot fetch it (publisher paywall; the only free
  copy at HAL is behind an interactive anti-bot challenge). It must be supplied as a
  file; a verifier is armed to accept only the right document.
* The two ZIPs hold earlier work: a finished 19-page manuscript on the $k$-Galois
  affine-algebra question, and a later audit that declares the joint-enumerator
  direction non-novel and the manuscript stage blocked. Both are registered as
  prior art, neither is treated as authority.

## Layout

```
research_project/
├── README.md                  this file
├── PROJECT_PLAN.md            scope, phases, gates, rules, assumptions, risks
├── PHASE_STATUS.md            per-phase status with evidence
├── source_audit/
│   ├── SOURCE_INVENTORY.md
│   ├── SOURCE_PAPER_METADATA.md
│   ├── ENVIRONMENT_CAPABILITIES.md
│   ├── PRIOR_ART_REGISTER.md
│   ├── SOURCE_IDENTITY_BLOCKER.md
│   ├── SOURCE_ACCESS_STATUS.md
│   ├── SOURCE_PDF_MANIFEST.csv
│   ├── FILE_MANIFEST.csv      260 rows: sha256, bytes, origin, duplicate_of, path
│   └── PHASE0_VERIFICATION_LOG.md
├── logs/phase0_evidence.out   raw command transcript
├── tools/inventory.py         regenerates FILE_MANIFEST.csv
├── tools/verify_source_pdf.py identity gate for the supplied source PDF
├── tools/extract_prior_art.sh verifies + extracts the two ZIPs
└── prior_art/                 extracted copies (git-ignored)
```

Later phases will add `literature/`, `theory/`, `proofs/`, `code/`, `data/`,
`verification/`, `paper/`, with the blueprint's exact deliverable names.

## Reproduce Phase 0

```bash
cd /home/user/Galios-Hull
bash research_project/tools/extract_prior_art.sh                 # verifies ZIP hashes first
python3 research_project/tools/inventory.py > research_project/source_audit/FILE_MANIFEST.csv
bash -c 'sha256sum *'                                            # root artifact hashes
```

Nothing outside `research_project/` is written, and no original file is modified.

## Rules in force

1. No invented theorem, citation, DOI, parameter, output or verification result.
2. Every claim carries a path, page, hash or transcript.
3. Originals are never overwritten; prior audits are inputs, not authority.
4. `PASS` needs evidence; `PASS` is never assigned because a document exists.
5. No manuscript before the blueprint's five conditions are met; if they fail, the
   deliverable is a feasibility report.
6. No push or publication without explicit authorisation.
