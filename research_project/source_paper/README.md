# Drop the source paper here

Place the **Yadav, Singh, Islam, Prakash, Solé (2024)** PDF in this directory —
any filename ending in `.pdf`.

Bibliographic target:
- Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes
- *Computational and Applied Mathematics* **43**, Paper 269 (2024)
- DOI `10.1007/s40314-024-02789-1`

Then run, from the repository root:

```bash
python3 research_project/tools/find_and_verify_source.py --record
```

The gate walks the repository, identifies every PDF by content, prints a verdict
per file, records the accepted file with its SHA-256 in
`source_audit/SOURCE_PDF_MANIFEST.csv`, and exits 0 only when exactly one PDF is
the source paper. The Debnath et al. preprint and the prior manuscripts are
rejected by construction.

Nothing else is needed; Phase 1 starts as soon as the gate reports ACCEPT.
