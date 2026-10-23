# GATE 0 BLOCKER — source identity mismatch

**Raised:** 2026-10-23 (UTC) · **Severity:** blocking · **Owner of decision:** user
**Gate affected:** Gate 0 ("the exact source PDF and the usable research environment are identified")

> **STATUS: RESOLVED BY DECISION (2026-10-23).** The user chose **Option 1** of §4:
> Yadav et al. (2024) is the source of record; Debnath et al. is excluded as a
> substitute. The identity question below is therefore closed. What remains open is
> only the *file*: see `SOURCE_ACCESS_STATUS.md` and `REPOSITORY_SOURCE_SEARCH.md`.
> The original text is preserved unchanged beneath this banner as the record of how
> the issue was found and escalated.

---

## 1. The finding

The blueprint names its source paper on p. 1 and repeats it on p. 2:

> "Source paper: Yadav et al. (2024), Computational and Applied Mathematics,
> DOI: 10.1007/s40314-024-02789-1"
>
> "Source paper: 'Hermitian hull of constacyclic codes over a class of non-chain
> rings and new quantum codes,' Shikha Yadav, Ashutosh Singh, Habibul Islam, Om
> Prakash, and Patrick Solé, Computational and Applied Mathematics (2024), DOI
> 10.1007/s40314-024-02789-1."

The only PDF in the workspace is a **different paper**:

> *Galois hulls of constacyclic codes over affine algebra rings*
> Indibar Debnath, Habibul Islam, E. Martínez-Moro, Om Prakash
> arXiv:2412.08512v1 [cs.IT], 11 Dec 2024; published as *Discrete Mathematics*
> **349**(2) (2026) 114750, DOI `10.1016/j.disc.2025.114750`.

The Yadav et al. paper appears in that PDF **only as reference [43]** (p. 26), and
its full text is not present anywhere in the workspace.

## 2. Why this is blocking rather than cosmetic

The two papers differ in every structural component the blueprint's later phases
depend on:

| Component | Blueprint / Object C (Yadav et al.) | Uploaded PDF / Object A (Debnath et al.) |
|---|---|---|
| Code alphabet | $\mathcal R_e=\mathbb F_{q^2}+u\mathbb F_{q^2}+\cdots+u^{e-1}\mathbb F_{q^2}$, $u^e=1$, $e\mid(q+1)$ | $\mathcal A=\mathbb F_q[X_1,\dots,X_\ell]/\langle t_1,\dots,t_\ell\rangle$, $t_i$ square-free |
| Field of scalars | $\mathbb F_{q^2}$ (codes are $\mathbb F_{q^2}$-linear) | $\mathbb F_q$ |
| Inner product | Hermitian (single, fixed) | $k$-Galois, second slot, $\langle x,y\rangle_{s,k}=\sum_i x_i y_i^{p^k}$ |
| Code description | generator polynomials, idempotents $\eta_l$ | idempotent generators per CRT component |
| Main objects | possible Hermitian hull dimensions, LCD conditions, dual-containing conditions, matrix Gray map, quantum codes | $k$-Galois dual/hull generators, hull-dimension formula, $k$-Galois LCD criterion, EAQECCs |
| Blueprint's ring hypothesis | $e\mid(q+1)$, multipliers $\alpha_l$ of order $r_l\mid q+1$ | $\gcd(n,p)=1$ and square-free $t_i$ |

Consequently the blueprint's Phases 3–6 — the constituent enumerator
$H_\ell(z_\ell)$, the joint enumerator $H_{\text{joint}}$, the total distribution,
the dual-containing restricted enumerator, and the Hermitian quantum construction
$[[N,2K-N,\ge d]]_q$ — are **not** statements about Object A. Executing them
against Object A would require changing the inner product, the code family, the
field, the Gray map and the quantum construction: a different project.

## 3. Availability of Object C (attempted, all failed)

| Route | Result |
|---|---|
| Search the repository and both ZIPs by filename, title, DOI | no match; only one source PDF exists, hashing to Object A |
| Springer landing page (`link.springer.com/article/10.1007/s40314-024-02789-1`) | abstract + reference list only; "This is a preview of subscription content"; PDF USD 39.95 |
| Direct HTTPS from the sandbox | TLS handshake blocked (`SSL_ERROR_SYSCALL`) — egress is restricted to an allowlist |
| Search for an arXiv / repository copy | no arXiv version found; the item is a Springer-only publication |
| Institutional access | not available to this agent |

**Therefore the agent cannot obtain Object C.** Only the user (institutional
access, purchase, or an author copy) can supply it.

## 4. Options and consequences

### Option 1 — User supplies the Yadav et al. PDF (recommended)

* Put the file in the repository root (or give a reachable URL) and say so.
* Phase 1 then audits Object C exactly as the blueprint specifies; Phases 3–6
  proceed in the blueprint's own ring $\mathcal R_e$; Gate 2 tests the *Hermitian
  non-chain-ring* enumerator.
* Phase 1 also needs the theorem numbering and hypotheses of the *version of
  record* (CAM 43:269, 2024). If only a preprint is supplied, the metadata file
  must mark that version explicitly.
* **Cost:** one file from the user. **Fidelity to the blueprint: full.**

### Option 2 — Re-scope to the uploaded paper (Debnath et al., arXiv v1)

* Phase 1 audits Object A; Phases 3–6 are re-written for the $k$-Galois setting.
  Every deviation from the blueprint is recorded in a deviation register, and the
  proposed objects become $k$-Galois hull enumerators over
  $\mathbb F_q[X]/\langle t\rangle$ components.
* This is what the earlier `02_F11_Audit/` stream did; its own conclusion was that
  the *joint* enumerator collapses to a product of known local results (Gate 2
  fail). That conclusion is **not** accepted here on trust — it would be re-tested
  independently — but it is a strong prior that this route ends in a feasibility
  report rather than a manuscript.
* **Fidelity to the blueprint: partial, with documented substitutions.**

### Option 3 — Narrow the objective to the F11 hypothesis gap in Object A

* Auditing/correcting a specific technical defect is a legitimate research output,
  but it is **not** the blueprint's objective (new theorems + hull enumeration),
  and the prior stream reports that the decisive evidence requires the paywalled
  version of record.
* Would require a revised blueprint and its own gate structure.

### Option 4 — Stop

* Record Gate 0 as BLOCKED and archive Phase 0. No further phases.

## 5. Recommendation

**Option 1.** The blueprint is a complete, phase-gated plan for Object C; every
later gate is written in terms of that paper's ring and Hermitian structure.
Running it against a different paper would start the project by silently rewriting
its own specification — precisely what the blueprint forbids.

If Object C cannot be obtained, **Option 2** is the only route that preserves the
blueprint's phase skeleton, and it must be entered with an explicit deviation
register and with the expectation (not certainty) that Gate 2 may fail.

## 6. What is already complete regardless of the decision

* Repository inventory, hashes, archive integrity: done (`FILE_MANIFEST.csv`).
* Identification of all three bibliographic objects and their access status: done
  (`SOURCE_PAPER_METADATA.md`).
* Environment capabilities: done (`ENVIRONMENT_CAPABILITIES.md`).
* Prior-art register and conflict list: done (`PRIOR_ART_REGISTER.md`).
* Object A is readable end-to-end (27 pp., searchable text layer), so Phase 1 can
  begin on Object A **today** if Option 2 is chosen.

## 7. Decision requested

> Which object is the source paper of record for this project?
>
> 1. **Yadav et al. (Object C)** — I will supply the PDF / access.
> 2. **Debnath et al. (Object A)** — proceed on the paper actually present, with a
>    deviation register.
> 3. **Reframe** around the F11 defect.
> 4. **Stop** at Phase 0.

Until an answer is recorded, Gate 0 is **BLOCKED** and Phase 1 does not start.
