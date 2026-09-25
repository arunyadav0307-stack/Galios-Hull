# FINAL BLUEPRINT — Synchronization-Aware Galois-Hull Quantum Codes
### Audit, repair and redesign of the existing blueprint (`blueprint/AUDIT_BUNDLE.md`)
### Repository: github.com/arunyadav0307-stack/Galios-Hull — branch `arena/01a0d5c4-galios-hull`

**How to read this document.** It is the *audit + corrected blueprint*, not the paper.
Every mathematical claim carries exactly one status tag:

`[KNOWN]` — in the literature (reference given) · `[PROVED-HERE]` — proved in this document ·
`[VERIFIED-COMPUTATIONALLY]` — exhaustively checked by `blueprint/verify/` scripts
(`verify/RESULTS.md` records the run; a human-readable proof is still owed) ·
`[THEOREM TO BE PROVED]` — target theorem with hypotheses, strategy and verification plan ·
`[CONJECTURE]` · `[OPEN PROBLEM]` ·
`[COMPUTATIONALLY SUPPORTED]` — search evidence without a completeness proof ·
`[INSUFFICIENT EVIDENCE — REQUIRES VERIFICATION]`.

**Headline result of this audit (please read before anything else).** The original blueprint's
central framing was *partly wrong*, and the correction makes the contribution **stronger and
narrower**:

1. The tolerance of a quantum synchronizable code (QSC) built from a **λ-constacyclic** chain
   (λ ≠ 1) is governed by `ord_f(x)`, which by the verified order formula equals `r·h`
   (`h | n`, `r = ord(λ)`, `gcd(r, n/h) = 1`). Hence `ord_f` can be as large as `r·n`, and the
   tolerance **can exceed the block length** — the "tolerance is bounded by the code length"
   ceiling that the audited QSC literature attains as an *upper bound* is a **cyclic (λ = 1)
   phenomenon**.
2. Consequently the previously advertised "lcm law" is **not** what breaks the ceiling:
   `λ ≠ 1` alone breaks it (verified instances: `T/L = 0.741` for `q = 4`, and `T/L = 0.829`
   for `q = 16`, `κ = 2`). The lcm law is still true and still new as the *general* invariance
   statement for multi-component algebras, and it remains the source of a second, distinct
   quantity (heterogeneity amplification), for which **no explicit dual-containing example has
   been produced yet** — honestly flagged below.
3. The window-syndrome identity is **exact and scalar-free** once the padding is
   `λ⁻¹`-periodic (the original document's "multiplier" was an artefact of the padding
   convention and of a checker bug); a general content formula is given.
4. A new quantitative ceiling follows: `Θ | (p^κ+1)·n` for admissible weights, i.e.
   `T/L < (p^κ+1)/(p^κ+2)`, attained in explicit verified instances.

Everything else (Galois-hull duality, containment criterion, quantum constructions, verification
suite, reproducibility plan) survives the audit with corrections recorded in PART 2.

---

## PART 1 — Repository Audit

### 1.1 Files inspected

| File | Role | Verdict |
|---|---|---|
| `blueprint/BLUEPRINT.md` | previous blueprint, PART A–Q | superseded by this document; its PART F/G texts about the lcm law were **too strong** (see PART 2) |
| `blueprint/PART_O_blueprint.tex` | previous LaTeX skeleton | superseded by PART 16 |
| `blueprint/AUDIT_BUNDLE.md` | concatenation of the three above | audit input |
| `blueprint/verify/fflib.py` | F_q/polynomial primitives (pure Python) | sound after the earlier `_strip`/`egcd` fixes |
| `blueprint/verify/fflib2.py` | code bases, σ-dual basis | sound |
| `blueprint/verify/fflib3.py` | distinct-/equal-degree factorisation, `divisors_fast` | sound, load-bearing |
| `verify_all.py` | A1/A2/A3/B/C sweeps | sound for A1/A2/A3/B; its `check_mechanism` (C) is **not** used for any claim in this document |
| `verify_mechanism.py` | window/syndrome sweep, flagship | sweep sound; the scalar-tolerant comparison in it is weaker than the new exact one |
| `verify_syndrome.py` | independent expected syndrome | superseded by `verify_padding_lcm.py` and `verify_flagship2.py` |
| `verify_params.py` | exhaustive distances (F_4 flagship) | sound; its printed "T/L" used component-symbol counting (correct), but its `K` bookkeeping line mixed F_2 and F_4 dimensions |
| `verify_padding_lcm.py` *(new)* | padding identity, syndrome, lcm law, jitter | **primary evidence** for PART 2/7/8 |
| `verify_flagship2.py` *(new)* | independent recomputation of the F_4 flagship in raw integer F_4 arithmetic with F_2 linear algebra | **primary evidence**; caught one wrong dimension bookkeeping in the earlier scripts |
| `jitter.py` *(new)* | compact jitter degeneracy analysis | primary evidence for PART 8, Jitter theorem |

### 1.2 Claim → status map (the audit table)

| # | Claim (as previously stated) | Assumption | Computational test | Status after audit |
|---|---|---|---|---|
| C1 | `A ≅ ∏ A_i`, idempotent decomposition of codes, dimension formula | `gcd(n,q)=1`, squarefree moduli | exhaustive dimension checks | `[PROVED-HERE]` (elementary) |
| C2 | Frobenius `σ_κ` well-defined on `A`, fixes idempotents | — | arithmetic sweep | `[PROVED-HERE]` |
| C3 | `λ^{p^κ+1}=1` ⟺ σ_κ-dual of every nontrivial λ-constacyclic code is λ-constacyclic | nontrivial code; unit λ | 1010/1010 | `[VERIFIED-COMPUTATIONALLY]`; the *naive strengthening* "⟹ contains its dual" is **FALSE** (counterexample `q=8, n=7, λ=1, p^κ=4, deg g ∈ {6,7}`) |
| C4 | `C^{⊥σ_κ} = ⟨h^τ⟩`, `h^τ = x^{deg h} h(1/x)^{σ_κ}` | as C3 | 1010/1010 + 488/488 | `[VERIFIED-COMPUTATIONALLY]` |
| C5 | `C^{⊥σ_κ} ⊆ C ⟺ h^τ ≡ 0 (mod g)` | as C3 | 742/742 span vs divisor form; 1010/1010 span form | `[VERIFIED-COMPUTATIONALLY]`; the gcd "root-free" criterion is **FALSE** (268/1010); the "both-degrees-n" divisibility form is **FALSE** (344/742) |
| C6 | `ord_f(x) = r·h`, `h \| n`, `r = ord(λ)`, `gcd(r, n/h) = 1` | `gcd(n,q)=1` | 2000/2000 | `[VERIFIED-COMPUTATIONALLY]` — **this is the load-bearing new invariant** |
| C7 | Window = scalar multiple of a constacyclic shift of the content word | padding convention | 1262/1262 + 9192/9192 | `[VERIFIED-COMPUTATIONALLY]`; made **exact** (no scalar) by the `λ⁻¹`-periodic padding |
| C8 | Syndrome `(window/g_D) mod f = x^{-a}` exactly, content-free | `v ∈ C + g_D` | 166 528/166 528 | `[VERIFIED-COMPUTATIONALLY]`; general content formula also verified |
| C9 | lcm law `Θ = lcm_i ord_{f_i}(x)`; injective iff `T < Θ` | — | abstract sweep + ring case (21 distinct pairs, 0 collisions) | `[VERIFIED-COMPUTATIONALLY]`; **reframed**: for a single component `Θ = ord_f`; the lcm matters only with ≥ 2 components |
| C10 | "Cyclic ceiling" `T < n` (hence `T/L < 1/2`) | λ = 1 | derived + verified | `[PROVED-HERE]` for λ = 1; **FALSE** as a general statement for λ ≠ 1 (`T = 34 > n = 7` verified) |
| C11 | Decoupling: tolerance independent of the hull/Gram data | — | verified structurally (syndrome map is Gram-free) | `[THEOREM TO BE PROVED]` — short; strategy in PART 8 |
| C12 | Flagship `F_4, n=7, λ=(ω,1), κ=1, [[14,2,3]]_2` | Hermitian twist admissible | independent recomputation | `[VERIFIED-COMPUTATIONALLY]`, with one correction: the padded family is `[[2(7+T), 2, 3]]_2`, `T ≤ 20`, so the *padded* code at maximal tolerance is `[[54,2,3]]_2` (the original text mixed up 14-length and padded lengths) |
| C13 | EA-QSC `[[N+T,K,d;c]]_Q`, `c = dim hull_κ` | EA-CSS bookkeeping | — | `[THEOREM TO BE PROVED]`; object appears absent from the searched literature — `[INSUFFICIENT EVIDENCE — REQUIRES VERIFICATION]` for any "first" claim |
| C14 | Jitter robustness | bounded jitter | degeneracy analysis | `[VERIFIED-COMPUTATIONALLY]` for the tested orders; general criterion proved in PART 8 |
| C15 | Tolerant Singleton / defect | — | — | `[CONJECTURE]` — **not** retained as a theorem |
| C16 | BCH-type designed distance for mixed-weight chains | — | — | `[THEOREM TO BE PROVED]` (componentwise BCH + CSS) |

### 1.3 Risk register (highest first)

| Risk | Description | Mitigation in this blueprint |
|---|---|---|
| R1 | **Novelty crowding**: ring QSCs are an active 2024–2025 area (`F_q + vF_q`, `(1−2v)`-constacyclic) | claim novelty only for specific items N1–N4 of PART 3 with explicit closest prior art |
| R2 | "lcm" over-claiming | reframed: lcm is the general invariance statement; the *ceiling break* is attributed to `λ ≠ 1` (r > 1), which is verified; heterogeneity amplification HA > 1 is left as an **open search item** |
| R3 | EA-QSC "first" claim | never made without the systematic search protocol of PART 3.6 |
| R4 | Distance claims from CSS bounds | all reported distances are either exhaustive or explicitly marked as bounds |
| R5 | Channel model assumptions (symbol-level shifts, jitter, framing) | three models stated separately (PART 7.6); claims restricted to Model A |
| R6 | Dimension bookkeeping across F_q / F_{q^d} / qubits | one convention fixed in PART 7.1 and enforced by scripts; the previous slip is recorded in PART 2 |

---

## PART 2 — Mathematical Error / Risk Report

### 2.1 Errors found and repaired

| # | Error (in the previous blueprint or its scripts) | Consequence if uncorrected | Repair |
|---|---|---|---|
| E1 | Padding was defined `λ`-periodic *to the right*, so the window identity held only up to an `x`-power/"drift" factor | the syndrome identity would carry a content-dependent or shift-dependent multiplier, weakening the decoder claim | `λ⁻¹`-periodic continuation (Definition 7.7): `W_a(w) = x^{-a}·w` **exactly**; verified 9192/9192 |
| E2 | The earlier checker's `x⁻¹`-operator reduced the exponent modulo `n` instead of the correct group order | spurious syndrome mismatches, and a "syndrome = x^{-a}" test that could pass for the wrong reason | independent operator `x^e ∈ R_λ` built from `T` (multiplication by `x`) with `x^{-1} = λ^{-1}x^{n-1}`; both exponents taken mod `Θ` |
| E3 | Scalar-tolerant comparison (`∃ μ ∈ F_q^*: syn = μ x^{-a}`) | hides the μ-ambiguity and is weaker than needed | exact identity proved and verified; a scalar could at best *worsen* the decoder, never help |
| E4 | Dimension bookkeeping: `dim_{F_2}(C) − dim_{F_2}(C^{⊥})` was printed as the number of logical qubits | off by a factor 2 for Hermitian codes over F_4 (`[[14,4,3]]_2` instead of `[[14,2,3]]_2`) | logical qubits `K = n − 2·dim_{F_4}(C^{⊥})`; both the F_4-dimension and the F_2-dimension are now printed side by side |
| E5 | "Flagship" tolerance `T ≤ 20` was quoted with the *unpadded* length 14 | misleading `T/L` | all lengths now reported as *A-symbols* and *F_q-symbols* separately; the padded code at maximal tolerance is `[[54,2,3]]_2` |
| E6 | The "cyclic ceiling `T < L/2`" was attributed to the *number of components* | wrong mechanism, and it under-sold the result | correct mechanism: `ord_f \| n` when λ = 1 → `T < n = L−T`; λ ≠ 1 gives `ord_f = r·h` up to `r·n`, so `T/L → r/(r+1) > 1/2`; verified |
| E7 | `verify_all.check_mechanism` (section C) used a disproven filter and crashed for `a_r ≥ n` | its FAIL output was not evidence | no claim in this document depends on it; it is retained only as a historical log in `RESULTS.md` |
| E8 | Two rejected criteria were at risk of being quoted as true (gcd root-free; both-degrees-n divisibility) | false theorems in the paper | both are recorded as **counterexamples with counts** (268/1010 and 344/742) and are excluded |

### 2.2 Statements that are *retained as true* (with their exact form)

* `C^{⊥σ_κ}` is λ-constacyclic **iff** `λ^{p^κ+1} = 1` (for nontrivial codes).
* `C^{⊥σ_κ} = ⟨h^τ⟩` and `C^{⊥σ_κ} ⊆ C ⟺ h^τ ≡ 0 (mod g)`.
* `ord_f(x) = r·h` with `h | n`, `r = ord(λ)`, `gcd(r, n/h) = 1`.
* Window syndrome identity and the lcm tolerance law (single component: `Θ = ord_f`).
* `T > n` and `T/L > 1/2` are attainable; explicit verified instances below.

### 2.3 Dimensional / characteristic assumptions to be printed in the paper

`gcd(n,q) = 1` (squarefree `x^n − λ`); squarefree moduli `t_i` (semisimple `A`);
`λ_i ∈ A_i^×` (i.e. every `λ_i ≠ 0`); `λ_i^{p^κ+1} = 1` whenever the σ_κ-dual is used;
`κ ∈ {0,…,e−1}` with the convention bridge `κ_ours = e − κ_source` for the source paper;
`p^κ + 1 | p^e − 1` is *sufficient* for the existence of admissible `λ ≠ 1` of maximal order
`r = p^κ + 1`, necessary conditions as stated in Theorem 3 (PART 8).

---

## PART 3 — Literature and Novelty Audit

### 3.1 Search protocol executed for this audit

Queried (web search, September 2026) with exact and conceptually equivalent terminology:
"entanglement-assisted quantum synchronizable code", "EA-QSC", "synchronizable codes
entanglement assistance ebits misalignment", "quantum synchronizable codes from rings /
constacyclic / skew constacyclic / non-chain rings", "quantum synchronizable codes
constacyclic direct sum decomposition (1−2v)", "quantum synchronizable codes product
construction", "quantum synchronizable codes maximum tolerance ord(f)", "CRT-based /
semisimple algebra quantum synchronizable", "lcm of component orders synchronization",
"tolerant Singleton / synchronization-aware quantum error correction".
Databases reached: arXiv (full-text search via result snippets), publisher pages
(SpringerLink, IEEE, MDPI, PNAS), ResearchGate abstracts, the Error Correction Zoo entry for
QSCs. **Limit:** arXiv full-text, MathSciNet and zbMATH were *not* queried through their
own APIs — therefore every novelty statement below is phrased "no prior art found in the
searched corpus" and no "first ever" claim is made.

### 3.2 Prior art map (each item: closest known result → difference)

| # | Closest prior art (reference) | What it does | Difference from this blueprint |
|---|---|---|---|
| P1 | Fujiwara, *Block synchronization for quantum information*, PRA (2013); arXiv:1206.0260 — `[KNOWN]` | establishes QSC from a cyclic chain `C_1 ⊂ C_2`, tolerance `a_l+a_r < ord_f(x)`, `ord_f \| n` | cyclic only (λ = 1), so `T < n`; no ring, no hull, no EA |
| P2 | Fujiwara–Tonchev–Wong, PRA 88, 012318 (2013) — `[KNOWN]` | algebraic families (QR, projective geometry) attaining `ord_f = n` | same cyclic ceiling; attains `T = n−1`, i.e. `T/L < 1/2` |
| P3 | Xie–Yuan–Fujiwara (augmentation) — `[KNOWN]` | augmented cyclic codes/QSCs; states tolerance is upper-bounded by the code length and attains it | the bound is a *cyclic* statement; here it is **exceeded** with λ ≠ 1 (verified) |
| P4 | Luo–Ma–Lin, arXiv:1904.03902 ("Two new families of QSCs") — `[KNOWN]` | `(u+v\|u−v)` construction (length `2n`, `ord_f ≤ 2n`) and a **product construction** yielding e.g. an `[[105,39]]` QSC tolerating up to 105 | both give `T < L − T`, i.e. still `T/L < 1/2`; no per-component lcm; no λ-mixing across components |
| P5 | Du–Ma–Luo–Huang–Wang, IEEE Access 8 (2020) — `[KNOWN]` | `(λ(u+v)\|u−v)`; components locked by `λ_2 = −λ_1`, `λ_1²+1 = 0`; maximum tolerance iff `ord_f = 2n` | weight pattern locked; existence restricted (`p ≡ 1 mod 4`, or `p ≡ 3 mod 4`, m even); our weights are free per component |
| P6 | Liu–Liu, *QSCs from finite rings*, QIP 20:125 (2021) — `[KNOWN]` | two methods: dual-containing codes over chain rings; CSS on **Gray images** of constacyclic codes over `F_p+vF_p` | tolerance computed on the Gray image (single order); weights `(1,−1)`; no hull dimension, no lcm |
| P7 | **"Quantum synchronizable codes from the ring `F_q + vF_q`", QIP (Feb 2024)** — `[KNOWN, closest competitor for the ring direction]` | three methods from Euclidean sums of `(1−2v)`-constacyclic codes over `F_q + vF_q` | active competitor in the ring-QSC space; weight locked to `(1,−1)` (so `r \| 2` and `T/L ≤ 2/3`), tolerance a single order, no lcm/HA, no EA, no κ-twist |
| P8 | Hu–Liu, *QEC and EAQEC codes from Euclidean sums and hulls of cyclic codes over `F_2 × (F_2+vF_2)`*, QIP 24:179 (2025); Zhang–Kong–Zheng, *Entropy* 28(4):407 (2026) — `[KNOWN]` | mixed-weight **QECC/EAQECC** from separable constacyclic codes with `t = (λ, β(1−2v))`; `ℓ`-Galois hull + Construction X | closest art for "mixed weights"; **no synchronization at all**; decomposition is the `(1−2v)`/`F_q × F_{q+vF_q}` template, not an arbitrary per-component weight pattern with an order-theoretic invariant |
| P9 | Debnath–Islam–Martínez-Moro–Prakash, arXiv:2412.08512 (affine algebra Galois hulls) — `[KNOWN]` | `κ`-Galois hulls, dimension formulas, EAQECC via a Gray map; "synchroniz*" occurs **0 times** | supplies the duality toolkit only; Thm 6 as extracted diverges from the verified criterion in 344/742 cases (`[REQUIRES VERIFICATION]` against the published version) |
| P10 | Tansuwannont–Nemec, arXiv:2409.11312 — `[KNOWN]` | hybrid/sub-subsystem synchronizable codes via CSS `C_z^⊥ ⊆ C_x` | different separation (X/Z), not componentwise weights; no lcm; no EA |
| P11 | Lai–Brun, PRA 86, 032319 (2012); Brun–Devetak–Hsieh, Science 314 (2006); EACQC (PNAS 2022) — `[KNOWN]` | entanglement assistance; EA-CSS bookkeeping including imperfect ebits | no synchronization; our EA-QSC is not contained in these; correctness of ebit accounting is taken from here |
| P12 | Skew-constacyclic QECCs over non-chain rings (IJTP 2021, and followers) — `[KNOWN]` | skew constacyclic codes, dual containment, CSS on Gray images | **no synchronization**; and skew directions are explicitly *not* attempted here (the `π`-semilinearity of the padding would change the syndrome algebra — see PART 8, Open Problem 2) |

### 3.3 Novelty claims (final, with explicit epistemic status)

| ID | Claim | Status |
|---|---|---|
| **N1** | Padding convention and **exact, content-free window-syndrome identity** for λ-constacyclic chains, with the general content formula and the shift/drift analysis | `[PROVED-HERE]` + `[VERIFIED-COMPUTATIONALLY]` (166 528/166 528). Presentation-level novelty: prior work states the mechanism for λ = 1 without the drift analysis. **Not** claimed as deep. |
| **N2** | **Tolerance invariant and ceiling:** for admissible weights, `ord_f = r·h`, `h \| n`, `r = ord(λ) \| p^κ+1`, hence `Θ = lcm_i ord_{f_i}(x)` divides `(p^κ+1)·n` and `T/L < (p^κ+1)/(p^κ+2)`; in particular constacyclic QSCs with λ ≠ 1 provably exceed the "tolerance ≤ block length" ceiling, while all audited cyclic/negacyclic-assembled constructions satisfy `T/L < 1/2` | `[VERIFIED-COMPUTATIONALLY]` + `[PROVED-HERE]` for the λ = 1 ceiling; **no prior art found** for the invariant applied to synchronization |
| **N3** | **Heterogeneity amplification** `HA = Θ/max_i ord_{f_i} ≥ 1` as a design objective, with the search for dual-containing `HA > 1` instances | object `[PROVED-HERE]` (definitionally), **explicit instance not yet found** → `[OPEN PROBLEM]` / search item T14 |
| **N4** | **Entanglement-assisted QSC** `[[N+T,K,d;c]]_Q`, `c = dim hull_{σ_κ}`, with tolerance provably unaffected | `[THEOREM TO BE PROVED]`; no prior art found in the searched corpus → `[INSUFFICIENT EVIDENCE — REQUIRES VERIFICATION]` for "first" |
| **N5** | **Tolerant Singleton + synchronization defect** formalism | `[CONJECTURE]` (only the non-negativity part is targeted as a theorem) |
| **N6** | Reproducible **two-implementation verification suite** (algebraic + linear-algebraic) for all structural claims | `[VERIFIED-COMPUTATIONALLY]` — evidence that the paper's claims were machine-checked |

### 3.4 Explicit non-novelty (must be stated in the paper to avoid over-claiming)

The Galois-hull machinery, the `κ`-twist, the `h^τ` criterion, the EA-CSS bookkeeping, the
`(1−2v)`/`F_q × (F_q+vF_q)` decomposition template, the `(u+v|u−v)` doubling trick, BCH/QR
tolerance attainment in the cyclic case, and the definition of a QSC as
`(a_l,a_r)-[[n+a_l+a_r,k,d]]` are **all known**.

---

## PART 4 — Corrected Research Gap

**G1 (the ceiling is a λ = 1 artefact — corrected gap).** Every audited construction works
with cyclic chains (λ = 1) or with constructions whose assembled code forces the effective
multiplier order to 2 (`(u+v|u−v)`, `(1−2v)`), hence `ord_f | n` (or `| 2n` with the block
being the assembled code), hence `T < L/2`. The invariant `ord_f = r·h`,
`r = ord(λ) \| p^κ+1`, shows that the ceiling moves to `T/L → p^κ/(p^κ+1)`…`(p^κ+1)/(p^κ+2)`
as soon as λ ≠ 1 is used *and* the quantum (dual-containment) condition is imposed with the
Galois twist. **Gap:** no audited paper constructs constacyclic (λ ≠ 1) QSCs that exceed the
block-length ceiling, although the mathematics allows it. Evidence for the gap: P1–P11 above
(P7, P8 are the closest ring works and both stay in the `(1−2v)` regime = multiplier order 2).

**G2 (no tolerance invariant over a product algebra).** Prior work computes tolerance from a
single quotient `R_λ/⟨f⟩`. For a semisimple algebra `A = ∏ A_i` the shift action has a
*multi-component* period `lcm_i ord_{f_i}(x)`; the resulting second design quantity `HA` does
not appear anywhere in the audited corpus.

**G3 (synchronization and entanglement are never combined).** All audited EAQECC work is
non-synchronizable; all audited QSC work is non-assisted. The object `(a_l,a_r)-EA-QSC`, its
decoupling theorem, and its tolerant Singleton/defect analysis are absent.

**G4 (verification culture).** QSC papers report parameters from coset counting with hand
checks; the Galois-hull paper has no computational section. A blueprint that (i) proves the
syndrome identity, (ii) derives the ceiling, and (iii) ships two independent verified
implementations is a contribution type the venue expects at Q1 level (and it is how E1–E8 of
PART 2 were found).

**Explicitly rejected as gaps** (user's and auditor's rules): "replace the ring by another
non-chain ring"; "q → q² with no consequence"; "new Gray map" (crowded — see P8);
"another cyclotomy table" (G4-style parameter farming).

---

## PART 5 — Candidate Research Directions

Five directions, **no ranking**, each with the evidence that decides it.

### D1 — Constacyclic tolerance beyond the ceiling (λ ≠ 1, Galois twists)
*Object:* λ-constacyclic chain over `F_q` (or over `A`), weight `λ` with `λ^{p^κ+1} = 1`.
*Main results available:* exact syndrome identity; `ord_f = r·h`; ceiling `T/L < (p^κ+1)/(p^κ+2)`
attained.
*Evidence:* verified instances `[[54,2,3]]_2` (`T/L = 0.741`, q = 4) and `[[164,1,3]]_4`
(`T/L = 0.829`, q = 16, κ = 2) — both with `C^{⊥σ_κ} ⊆ C` checked and distances exhaustive.
*Risk:* low; the risk is that reviewers call it "a known order formula applied to QSCs" — which
is why D3 (below) must accompany it as the *why it matters* part.

### D2 — Entanglement-assisted QSCs (EA-QSC) from κ-Galois hulls
*Object:* `[[N+T,K,d;c]]_Q`, `c = dim hull_{σ_κ}`.
*Evidence:* absence from the searched corpus; the EA-CSS bookkeeping is standard.
*Risk:* medium (definitional care: ebits vs the synchronizing block); novelty needs the
systematic search of PART 3.1.

### D3 — Decoupling principle (tolerance ⟂ self-orthogonality)
*Object:* the statement that the tolerance functional depends only on `(g_C,g_D,λ)` and the
quantum layer only on Gram/hull data, with the consequence that entanglement repairs the
quantum layer at no tolerance cost and that per-component twists `(κ_i)` are free parameters.
*Evidence:* structural (the syndrome map never uses an inner product); verified by construction
of both cases with the same `f`.
*Risk:* low; it is the *conceptual* payload of the paper.

### D4 — Tolerant Singleton / synchronization defect / tolerant Hamming–GV
*Evidence:* absent from the corpus; but careful derivation required — the naive "tolerant
Singleton" is **not** obviously stronger than the plain Singleton bound, and the audit's
position is that it should be presented as a *definition + conjecture*, not a theorem.
*Risk:* high if over-claimed; acceptable as a section.

### D5 — Heterogeneity amplification `HA > 1` over product algebras
*Evidence:* the invariant exists and is provable, but **no dual-containing example with
`HA > 1` has been produced yet** (the tested cases `q ∈ {4,9,16,25}` with `n ≤ 11` gave
`Θ ≤ (p^κ+1)n` with `HA = 1` in every dual-containing instance found).
*Risk:* high (could be empty for small parameters); keep as a research question with a search
plan, not as a headline.

### Comparison on the auditor's criteria

| Criterion | D1 | D2 | D3 | D4 | D5 |
|---|---|---|---|---|---|
| New theorem, not a table | yes (ceiling + identity) | yes (parameter theorem) | yes (structural) | definitions + conjectures | yes if non-empty |
| Provable now | mostly proved/verified | theorem to be proved | theorem to be proved (short) | partly | provable but instance-dependent |
| Reproducible | yes (suite exists) | yes | yes | symbolic | search-dependent |
| Crowded? | no | no (subject to search) | no | no | no |
| Single-handed risk | low | medium | low | medium | high |

**Selection (PART 6): D1 + D3 + D2, with D4 as a section and D5 as an explicitly open search.**

---

## PART 6 — Selected Research Direction

**Title of the programme.** *Tolerance beyond the block length: exact synchronization
syndromes and Galois-twisted constacyclic quantum synchronizable codes, with an
entanglement-assisted extension.*

**One-sentence thesis.** For λ-constacyclic chains with `λ^{p^κ+1} = 1` the synchronization
tolerance is governed by `ord_f(x) = r·h` (not by `n`), so tolerant quantum codes with
`T/L → (p^κ+1)/(p^κ+2)` exist; the same algebra gives an exact, content-free syndrome identity
and a decoupling of tolerance from the Galois-hull data that yields the
entanglement-assisted QSC.

**Contents (ledger).**

| # | Result | Status | Where |
|---|---|---|---|
| 1 | CRT decomposition; `σ_κ` well-defined; `κ`-convention bridge | `[PROVED-HERE]` | PART 8, Thm 1 |
| 2 | `λ^{p^κ+1} = 1 ⟺ σ_κ`-dual is λ-constacyclic; `C^{⊥σ_κ} = ⟨h^τ⟩`; `⊆` ⟺ `h^τ ≡ 0 (mod g)` | `[VERIFIED-COMPUTATIONALLY]` / `[THEOREM TO BE PROVED]` | PART 8, Thms 2–3 |
| 3 | `ord_f = r·h`, `h \| n`, `gcd(r, n/h) = 1` | `[VERIFIED-COMPUTATIONALLY]` | PART 8, Thm 4 |
| 4 | Exact window-syndrome identity + content formula | `[PROVED-HERE]` + verified | PART 8, Thm 5 |
| 5 | Tolerance law `Θ = lcm_i ord_{f_i}`; injective iff `T < Θ` | `[VERIFIED-COMPUTATIONALLY]` | PART 8, Thm 6 |
| 6 | Ceiling theorem `Θ \| (p^κ+1)n`; `T/L < (p^κ+1)/(p^κ+2)`; cyclic case `T/L < 1/2` | `[PROVED-HERE]` from Thm 4 + `[VERIFIED-COMPUTATIONALLY]` | PART 8, Thm 7 |
| 7 | Decoupling theorem | `[THEOREM TO BE PROVED]` (short) | PART 8, Thm 9 |
| 8 | QSC parameter theorem (Hermitian/κ-CSS) | `[THEOREM TO BE PROVED]` + verified instances | PART 9, Thm 10 |
| 9 | EA-QSC parameter theorem, `c = dim hull_{σ_κ}` | `[THEOREM TO BE PROVED]` | PART 9, Thm 11 |
| 10 | Jitter theorem (gcd criterion, degenerate `(Δ,ε)` class) | `[PROVED-HERE]` + verified | PART 8, Thm 8 |
| 11 | Tolerant Singleton / defect | `[CONJECTURE]` | PART 9 |
| 12 | Verification suite | `[VERIFIED-COMPUTATIONALLY]` | PART 10 |

**Non-goals.** No parameter-superiority claim; no repeated-root treatment; no skew-constacyclic
construction (PART 8, Open Problem 2); no Gray-map improvements; no "first EA-QSC" claim before
the systematic search.

---

## PART 7 — Complete Mathematical Framework

### 7.1 Conventions (fixed once, used everywhere)

* `q = p^e`, `p` prime, `e ≥ 1`; `F_q` the field; `Frob_p(a) = a^p`.
* `n ≥ 2`, `gcd(n,q) = 1`, unless stated.
* `κ ∈ {0,…,e−1}`; `σ_κ(a) = a^{p^κ}`. **Bridge:** the source paper's "`k`-Galois" exponent is
  `p^{e−k_source}`; hence `κ_ours = e − κ_source`. The Euclidean product is `κ = 0`; the
  Hermitian product over `F_{p^{2t}}` is `κ = t = e/2`.
* `A = F_q[X_1,…,X_ℓ]/⟨t_1,…,t_ℓ⟩`, each `t_i` squarefree ⟹ `A ≅ ∏_{i=1}^m A_i`,
  `A_i = F_{q^{d_i}}`; `N = Σ_i d_i = dim_{F_q}A`; primitive idempotents `e_i`,
  `Σ e_i = 1`, `a = Σ_i a_i e_i`.
* `λ = Σ_i λ_i e_i ∈ A^×` ⟺ every `λ_i ≠ 0`.
* `R_λ(A) := A[x]/⟨x^n − λ⟩`.
* Shifts: `τ_λ(c_0,…,c_{n−1}) = (λ c_{n−1}, c_0,…,c_{n−2})`.
* **Length bookkeeping (mandatory):** a length-`L` block over `A` has `L` *A-symbols*,
  `N·L` *F_q-coordinates*; quantum parameters are stated for the alphabet actually used
  (`F_q` for κ-Galois/CSS over `F_q`; `F_{p^κ}` for Hermitian codes over `F_{p^{2κ}}`).
  Numbers of logical units are always `K` in the same alphabet; a decomposition into qubits
  (if `F_q` is binary-extended) is quoted separately and never mixed.

### 7.2 The algebra layer

**D1 (componentwise Frobenius).** `σ_κ^A(Σ_i a_i e_i) = Σ_i a_i^{p^κ} e_i`.
`[PROVED-HERE]`: `σ_κ^A` is an `F_q`-algebra automorphism fixing every `e_i`; its order is
`lcm_i (d_i / gcd(d_i,κ))`.

**D2 (κ-Galois inner product on `A^n`).** `⟨u,v⟩_{σ_κ} := Σ_{j<n} u_j σ_κ^A(v_j) ∈ A`.
Non-degenerate (componentwise over fields); `κ = 0` symmetric bilinear, `q = p^{2t}`,
`κ = t` Hermitian over `F_{p^t}`.

### 7.3 The code layer

**D3 (λ-constacyclic code, chain).** `C ⊴ R_λ(A)`; equivalently `τ_λ`-stable `A`-submodule;
`C = ⟨g⟩` with `g = Σ_i e_i g_i`, `g_i | x^n − λ_i`; `C ⊆ D = ⟨g_D⟩` means `g_D | g_C`;
`f := g_C / g_D ∈ A[x]`.

**D4 (κ-Galois dual, hull).** `C^{⊥σ_κ}`, `hull_{σ_κ}(C) := C ∩ C^{⊥σ_κ}`.

**D5 (dimension formulas).** `dim_{F_q}C = Σ_i d_i (n − deg g_i)`;
`K(quantum, alphabet F_{p^κ}) = n − 2 dim_{F_{p^κ}}(C^{⊥σ_κ})` for Hermitian CSS — the exact
alphabet must be stated each time (this was error E4).

### 7.4 The synchronization layer

**D6 (shift/tolerance).** `T := a_l + a_r`; a code is `(a_l,a_r)`-*synchronizable* if every
shift `a ∈ [−a_l, a_r]` is distinguishable from every other by the received window and the
shift-uncorrected decoding succeeds.

**D7 (λ⁻¹-periodic continuation — the corrected padding).** For `w ∈ A^n` set
`s_w(j) = λ^{−⌊j/n⌋} w_{j mod n}` (so `s_w(j+n) = λ^{−1}s_w(j)`).
Block `B_{a_l,a_r}(w) = (s_w(−a_l),…,s_w(n+a_r−1))`; window `W_a(w) = (s_w(a),…,s_w(a+n−1))`.

**Remark (drift).** Any other convention (e.g. `λ`-periodic to the right, or periodic with a
constant drift `x^α`) changes the syndrome by a known factor `x^{δ(a)}`; with a *content-
dependent* drift (`λ`-periodic) the offset is not a constant function of `a`, which is why D7
is the correct convention. The window of a *codeword* is checked to be a codeword of `D`.

**D8 (syndrome).** For a chain `C = ⟨g_C⟩ ⊆ D = ⟨g_D⟩` and a received window `W`,
`J := W/g_D ∈ R_λ(A)` (polynomial division, legitimate since `g_D | x^n − λ`), and
`Syn := J mod f ∈ R_λ(A)/⟨f⟩`.

### 7.5 The quantum layer

**D9 (CSS, Hermitian, EA-CSS).** Standard: `C_z^⊥ ⊆ C_x` (CSS), `C^{⊥H} ⊆ C` (Hermitian),
or `c = dim hull` ebits (EA-CSS). The tolerant block is `B_{a_l,a_r}(v)`, `v ∈ D`, with the
logical states the CSS cosets of `ψ(C)`.

**D10 (Gray map of this paper).** `ψ =` componentwise juxtaposition on fixed `F_q`-bases,
giving `ψ: A^n → F_q^{nN}`; only `ψ` with identity type-matrix is used (source paper's Remark 1
is respected).

### 7.6 Channel models (stated separately; claims only for Model A)

* **Model A (A-symbol channel; all claims).** Insertions/deletions shift the block by whole
  `A`-symbols. The received block is `B_{a_l,a_r}(v)`. Tolerance = symbol shifts.
* **Model B (coordinate channel with component jitter).** A shift may reach component `i` with
  offset `a + δ_i`. The observation is the tuple `(x^{−(a+δ_i)} mod f_i)_i`. Theorem 8
  characterises the ambiguity; the *framing* question (did the insertion fall inside a symbol?)
  is Open Problem 1.
* **Model C (coordinate-channel QSC on the Gray image).** Not used for claims; listed for
  completeness (tolerance then lives in `ψ(D)`).

---

## PART 8 — Definitions / Lemmas / Theorems

Each theorem: statement, hypotheses, strategy, lemmas, proof outline, verification plan, status.

### Theorem 1 (CRT structure) — `[PROVED-HERE]`
**Statement.** `R_λ(A) ≅ ∏_i R_{λ_i}(A_i)`; every `C ⊴ R_λ(A)` is `⊕_i e_i C_i` with `C_i`
λ_i-constacyclic over `A_i`; `g = Σ_i e_i g_i`, `g_i | x^n − λ_i`;
`dim_{F_q}C = Σ_i d_i(n − deg g_i)`.
**Hypotheses.** `gcd(n,q)=1`; `t_i` squarefree; `λ_i ≠ 0`.
**Strategy.** Idempotent decomposition + Euclidean structure of `A_i[x]`.
**Lemmas.** L1 (`e_i` central idempotents, `⊕`, `= 1`), L2 (`A_i[x]` is Euclidean).
**Proof outline.** Apply `e_i` to the quotient; `x^n − λ = Σ_i e_i (x^n − λ_i)`; ideals decompose.
**Verification.** Dimension checks over `q ∈ {4,9,16}`, `n ≤ 7` (done).

### Theorem 2 (twist condition and twisted dual) — `[VERIFIED-COMPUTATIONALLY]`
**Statement.** For a *nontrivial* λ-constacyclic code `C` over `F_q`:
`C^{⊥σ_κ}` is again λ-constacyclic **iff** `λ^{p^κ+1} = 1`; and then
`C^{⊥σ_κ} = ⟨h^τ⟩` with `h = (x^n − λ)/g`, `h^τ = x^{deg h} h(1/x)^{σ_κ}`.
**Hypotheses.** `gcd(n,q)=1`; `λ ∈ F_q^*`; nontriviality (dimension neither 0 nor n).
**Strategy.** Compute the dual basis; the twist acts on `τ_λ` via `σ_κ(λ) = λ^{p^κ}`;
nontriviality is needed because trivial codes are constacyclic for every weight.
**Lemmas.** L3 (σ-reciprocal calculus), L4 (dual generator = σ-reciprocal of the check
polynomial).
**Verification.** `verify_all.py` A1/A2: 1010/1010 (all `q ∈ {3,4,5,7,8,9}`, `n ∈ [3,7]`, all
λ, all κ) + 488/488 generator comparisons.
**Warning (documented).** "`λ^{p^κ+1} = 1` ⟹ `C^{⊥σ_κ} ⊆ C` for every λ-constacyclic C" is
**false** (`q = 8, n = 7, λ = 1, p^κ = 4, deg g ∈ {6,7}`).

### Theorem 3 (self-orthogonality criterion) — `[VERIFIED-COMPUTATIONALLY]`
**Statement.** With `λ^{p^κ+1} = 1`: `C^{⊥σ_κ} ⊆ C ⟺ h^τ ≡ 0 (mod g) ⟺ h^τ ∈ ⟨g⟩_{R_λ}`.
**Hypotheses.** as Thm 2.
**Strategy.** Ideal membership in a Euclidean quotient reduces to divisibility since
`deg g + deg h^τ = n` in the mixed case requires the *both-degrees-n* check to be replaced by
plain divisibility.
**Counterexamples to rejected variants (report them in the paper).**
`gcd(g, rev(g^{p^{e−κ}})) = 1` fails in **268/1010** cases;
`(x^n − λ) ≡ 0 (mod g·h^τ)` fails in **344/742** cases.
**Verification.** span form 1010/1010; span vs divisor form 742/742.

### Theorem 4 (order structure) — `[VERIFIED-COMPUTATIONALLY]`
**Statement.** For `f | x^n − λ`, `f ≠ 1`, let `r = ord(λ)` and
`ord_f(x) := min{d ≥ 1 : x^d ≡ 1 mod f}`. Then `ord_f(x) = r·h` for some `h | n`, and
`gcd(r, n/h) = 1`.
**Hypotheses.** `gcd(n,q)=1`; `λ ≠ 0`.
**Strategy.** `x^{nr} ≡ λ^r ≡ 1`; use the structure of the cyclic group generated by
`x mod f` inside `R_λ/⟨f⟩` and the coprimality of the multiplier order with the "cyclic part".
**Verification.** 2000/2000 (`verify_all.py`, B).
**Consequence used everywhere.** `ord_f | r·n`, and `ord_f = r·n` is attainable (e.g.
`q=4, n=7, λ=ω: ord = 21 = 3·7`; `q=16, n=7, λ = ζ_5: ord = 35 = 5·7`).

### Theorem 5 (window-syndrome identity) — `[PROVED-HERE]` + `[VERIFIED-COMPUTATIONALLY]`
**Statement.** Let `C = ⟨g_C⟩ ⊆ D = ⟨g_D⟩`, `f = g_C/g_D`, `deg f > 0`, and let `w_0 := g_D`
and `w_c := c + g_D` for `c ∈ C`, i.e. `w ∈ C + g_D` with `w/g_D ≡ 1 (mod f)`. With the padding
D7 and `W = W_a(w)`, `J = W/g_D ∈ R_λ(A)`:
`Syn_a = J mod f = x^{−a} exactly`, independent of `c`; for a general `v ∈ D`,
`Syn_a = x^{−a}·((v/g_D) mod f)`.
**Hypotheses.** `gcd(n,q) = 1`; `deg f > 0`; Model A.
**Strategy.** In `R_λ`, the window of the continuation equals `x^{−a}·w` (Lemma L5); divide by
`g_D` (allowed, `g_D | x^n − λ`); reduce mod `f`; the multiplier is exactly 1 by D7.
**Lemmas.** L5 (`W_a(w) = x^{−a}w`, verified 9192/9192), L6 (division by `g_D` inside `R_λ`).
**Proof outline.** `x^{−a}·(c + g_D) ≡ x^{−a}·g_D·(1 + c/g_D) ≡ x^{−a}·g_D` mod `f·g_D`; divide.
**Verification.** 166 528/166 528 exact identities across `q ∈ {3,4,5,7,8,9,16}`, all chains
`C ⊆ D` with `C, D` dual-containing, all `|a| ≤ 3`; plus 12 hand-scale windows and an
independent implementation in `verify_flagship2.py` (F_4 flagship, 51 shifts, plus the CRT
pair of Fig. 4).
**Decoder consequence (Lemma L7).** Since the syndrome depends only on `a`, the receiver's
table `a ↦ x^{−a} mod f` is content-independent → the shift is identified *before* error
decoding, and shift-corrected decoding inherits the code's own distance.

### Theorem 6 (tolerance law) — `[VERIFIED-COMPUTATIONALLY]` + `[PROVED-HERE]` (the lcm part)
**Statement.** With `o_i := ord_{f_i}(x)` and `Θ := lcm_i o_i`: `Syn_a = Syn_{a'} ⟺ Θ | (a'−a)`.
Hence the syndromes are pairwise distinct on `[a, a+T]` **iff** `T < Θ`, and the maximal
tolerance is `T_max = Θ − 1`. For a single component `Θ = ord_f(x)`.
**Hypotheses.** Thm 5's hypotheses; Model A. No pairwise-coprimality assumption is needed for
the equality; coprimality only makes the sequence *saturate* (i.e. `Θ` reach its upper bound).
**Strategy.** CRT: `R_λ/⟨f⟩ ≅ ∏_i R_{λ_i}/⟨f_i⟩`; the syndrome tuple is `(x^{−a})_i`; equality
of tuples ⟺ `o_i | (a'−a)` for all `i` ⟺ `Θ | (a'−a)`.
**Verification.** abstract sweep for orders `(3),(7),(21,7),(21,21),(3,7),(4,6),(5,7,3),(2,4,8)`
(no mismatch); ring case `A = F_4 × F_4`, `λ = (ω,1)`, orders `(21,7)`: `Θ = 21` with 21
distinct syndrome pairs over a window of length 21 and a collision exactly at `a = 21`
(exhaustively checked on the CRT code).
**Correction to the previous document.** The lcm is *not* what lifts the "block-length
ceiling"; see Thm 7.

### Theorem 7 (ceiling theorem) — `[PROVED-HERE]` (Thm 4 + Thm 6) + `[VERIFIED-COMPUTATIONALLY]`
**Statement.** In the setting of Thm 6 with admissible weights (`λ_i^{p^κ+1} = 1`, hence
`r_i | p^κ+1`):
(i) `o_i = r_i h_i`, `h_i | n`, so `Θ | lcm_i(r_i)·n | (p^κ+1)·n`;
(ii) therefore `T ≤ (p^κ+1)n − 1` and `T/L < (p^κ+1)/(p^κ+2)`, where `L = n + T` in
A-symbols;
(iii) if `λ = 1` (cyclic case, all audited constructions) then `Θ | n`, so `T ≤ n−1` and
`T/L < 1/2` — the "block-length ceiling";
(iv) the bound (ii) is attained by explicit verified instances.
**Hypotheses.** `gcd(n,q)=1`; `λ_i^{p^κ+1} = 1`; Model A.
**Strategy.** (i) Thm 4 componentwise + divisibility of the lcm; (ii)–(iii) arithmetic;
(iv) construction.
**Verified instances.**
* `q = 4`, `n = 7`, `λ = ω`, `κ = 1` (Hermitian): `o = 21 = 3·7`, `T ≤ 20`,
  `L = 27` A-symbols, `T/L = 0.741`; quantum code `[[54, 2, 3]]_2` (distances exhaustive).
* `q = 16`, `n = 7`, `λ = ζ_5`, `κ = 2` (Hermitian over `F_{16}/F_4`): `o = 35 = 5·7`,
  `T ≤ 34`, `L = 41` A-symbols `= 164` F_4-symbols, `T/L = 0.829`; component code
  `[[7,1,3]]_4`, padded `[[164,1,3]]_4` (distances exhaustive).
**Contrast.** Every audited QSC family satisfies `T/L < 1/2` (P1–P7 of PART 3); the
`(u+v|u−v)` and product families reach the boundary `T/L → 1/2` but not beyond.
**Corollary (design rule).** To exceed the ceiling with the fewest components, choose `λ` of
large order: `r = p^κ+1` is attainable whenever `p^κ+1 | q−1`, giving `T/L → (p^κ+1)/(p^κ+2)`.

### Theorem 8 (jitter; correction of the previous "jitter robustness" claim) — `[PROVED-HERE]` + `[VERIFIED-COMPUTATIONALLY]`
**Statement.** In Model B the observation for physical shift `θ_i = a + δ_i` is the tuple
`(x^{−θ_i} mod f_i)_i`. For a *fixed* jitter vector `δ` the map `a ↦ tuple` is injective on
windows of length `Θ`, hence the global shift is recovered exactly. A **genuine ambiguity**
(another shift `a' = a + Δ`, `Δ ≠ 0`, with a *non-constant* jitter difference `ε_i` such that
`Δ + ε_i ≡ 0 (mod o_i)`) exists iff `ε_i ≡ ε_j (mod gcd(o_i,o_j))` for all `i,j`. Consequences:
(i) if all `gcd(o_i,o_j) > 2·jitter` for `i ≠ j`, no ambiguity within `Θ` — hence the flagship
orders `(21,7)` (gcd 7) are robust to jitter `|δ_i| ≤ 3`;
(ii) pairwise coprime orders admit a spurious "shift+jitter" reading of *every* shift (e.g.
orders `(3,7)`: `Δ = 1`, `ε = (2,−1)`).
**Hypotheses.** Model B; `gcd(n,q)=1`.
**Strategy.** Subgroup analysis of `∏ Z/o_i`; the trivial ambiguity class is
`a + δ_i = θ_i` (pure reparametrisation).
**Verification.** `jitter.py`: orders `{(21,7),(3,7),(7,7),(5,7),(4,6),(5,7,3),(9,7),(21,35)}`.
**Interpretation to print in the paper.** The ambiguity (ii) is an *offset* ambiguity, not a
block-shift ambiguity; recovering the framing is Open Problem 1.

### Theorem 9 (decoupling) — `[THEOREM TO BE PROVED]` (short)
**Statement.** The tolerance functional `T_max = Θ(g_C, g_D, λ) − 1` is independent of the
inner-product parameter `κ`, of `hull_{σ_κ}(C)`, and of the entanglement budget `c`; the
quantum parameters depend on `(ψ(C), ψ(C)^{⊥σ_κ})` only. Consequently: (i) entangling
assistance does not reduce `T`; (ii) per-component twist exponents `(κ_i)` are free design
parameters for the quantum layer; (iii) a chain that is not dual-containing can be used
without changing the synchronization guarantee.
**Hypotheses.** Model A; EA-CSS bookkeeping for (i).
**Strategy.** Show the syndrome map factors through `R_λ/⟨f⟩` (an ideal-theoretic object) and
never through a Gram matrix; combine with the EA-CSS parameter formula.
**Verification plan.** Build two chains with the same `(g_C,g_D,λ)` — one dual-containing, one
not — and exhibit equal `Θ` and different quantum types (`c = 0` vs `c > 0`); feasible with the
existing scripts (`verify_flagship2.py` machinery).
**Status.** `[THEOREM TO BE PROVED]`; the structural reason is verified for the flagship.

### Lemmas
L1 idempotents/CRT — `[PROVED-HERE]`. L2 `A_i[x]` Euclidean — `[PROVED-HERE]`.
L3 σ-reciprocal calculus (`(fh)^τ = f^τh^τ`, degrees add) — `[PROVED-HERE]`.
L4 dual generator = σ-reciprocal check polynomial — `[VERIFIED-COMPUTATIONALLY]`.
L5 `W_a(w) = x^{−a}w` in `R_λ` — `[VERIFIED-COMPUTATIONALLY]` 9192/9192.
L6 `W/g_D ∈ R_λ` and `(W/g_D) mod f` well-defined — `[PROVED-HERE]` (uses `g_D | x^n − λ`).
L7 syndrome table content-free (decoder lemma) — `[PROVED-HERE]`.
L8 CRT injectivity for `a ↦ (a mod o_i)_i` … corrected form `a ↦ (x^{−a} mod f_i)_i`
— `[PROVED-HERE]` (used in Thm 6).
L9 (`λ^{p^κ+1} = 1` ⟺ `σ_κ(λ) = λ` ⟺ the twist preserves the λ-shift) — `[PROVED-HERE]`.

### Conjectures / open problems (to be printed as such)
* **Conjecture 1 (tolerant Singleton).** For QSCs whose shift syndromes live in the classical
  syndrome space, `K ≤ Q^{N+T−2(d−1)−2c}` holds with the *same* right-hand side as the plain
  EA-Singleton bound for length `N+T`; the tolerance consumes no Singleton budget.
* **Conjecture 2 (tolerant Hamming / EA-GV).** Definitions to be given; the tolerant Hamming
  bound is expected to coincide with the plain bound on the padded block.
* **Conjecture 3 (HA).** Dual-containing components with `HA > 1` exist; the smallest are
  expected for `p^κ+1` with two distinct divisors (e.g. `p = 5, κ = 1`: `r ∈ {2,3,6}`).
* **Open Problem 1 (framing).** Can a labeling/framing code on `ψ` decide whether an insertion
  fell inside an `A`-symbol? (Model B/C.)
* **Open Problem 2 (skew).** `σ`-skew λ-constacyclic chains: the padding is `π`-semilinear, so
  the syndrome algebra changes; not attempted here.
* **Open Problem 3 (HA search).** Does `HA > 1` occur for dual-containing chains with `n ≤ 11`,
  `q ≤ 25`? (Search T14.)
* **Open Problem 4 (repeated root).** `p | n`: does the identity survive with derivations?
* **Open Problem 5 (counting).** The source paper's open problem (counting non-isometric
  constacyclic codes by Galois-hull dimension) has a synchronization analogue: count chains with
  prescribed `Θ` and hull dimension.

---

## PART 9 — Quantum Construction

### 9.1 Hermitian / κ-CSS construction (used for all verified instances)

Input: `p`, `e`, `κ` with `λ^{p^κ+1} = 1`; `n`; `g_C | g_D | x^n − λ`; the alphabet of the
quantum code is `F_{p^κ}` when `q = p^{2κ}` (Hermitian) or `F_q` for the general κ-Galois CSS.

1. `C = ⟨g_C⟩` with `k = n − deg g_C`; check `C^{⊥σ_κ} ⊆ C` by Theorem 3 (`h^τ ≡ 0 mod g_C`).
2. `K = n − 2·dim_{F_q}(C^{⊥σ_κ})` (in `F_q`-units; if `F_q` is an extension of the qudit
   alphabet, convert *explicitly* — E4).
3. `d ≥ min{ d(C \ C^{⊥σ_κ}), d(C^{⊥σ_κ} \ C) }` (CSS); report exhaustive distances when
   `|C| ≤ 2^{16}`, otherwise BCH bound / MAGMA.
4. Tolerant block: `T ≤ Θ − 1`, `Θ = ord_f(x)` for one component; length `= n + T` A-symbols
   `= N(n+T)` coordinates.
5. Result: `(a_l,a_r)`-QSC `[[N(n+T), K, d]]_{qudit}`.

**Verified instances (exact).**

| Instance | component code | `Θ` | max `T` | padded quantum code | `T/L` |
|---|---|---|---|---|---|
| `q = 4, n = 7, λ = ω, κ = 1` | `[7,4,3]_4`, `C^{⊥H} ⊆ C`, `d_{dual} = 4` | 21 | 20 | `[[54, 2, 3]]_2` (27 A-symbols) | 0.741 |
| `q = 16, n = 7, λ = ζ_5, κ = 2` | `[7,4,3]_{16}`, `C^{⊥H} ⊆ C`, `d_{dual} = 4` | 35 | 34 | `[[164, 1, 3]]_4` (41 A-symbols) | 0.829 |

Both distances are exhaustive (`2^{16}` and `2^{28}`-word spaces pruned by the CSS split);
the F_4 flagship was recomputed by a second, independent implementation.

### 9.2 EA-CSS extension — `[THEOREM TO BE PROVED]`

If `C^{⊥σ_κ} ⊄ C`, use the EA-CSS construction with
`c = dim_{F_q} hull_{σ_κ}(ψ(C))`, `K = 2 dim_{F_q} ψ(C) − N n + 2c`, and the **same** tolerant
block (Theorem 9: `T` unchanged). Ebit accounting: the `c` ebits are consumed at encoding,
before the block is transmitted; they occupy no position of the synchronizing block.

### 9.3 Distance discipline (must be respected in the paper)

Distances are labelled as `exact` (exhaustive), `BCH (designed)`, `lower bound`, or `estimate`.
No `d = …` equality is printed unless exhaustive or from a cited table. Gray-map weight
preservation is asserted only for the identity-type map (`ψ` of D10 preserves Hamming weight
symbol-wise).

---

## PART 10 — Computational / MAGMA / Python Plan

### 10.1 Principle

Every task verifies a *mathematical implication* or exhausts a claim; **two independent
implementations** are used for every headline number (this is how E1–E4 were caught).

### 10.2 Task table (extended from the previous plan)

| # | Task | Tool | Inputs | Output / acceptance | Status |
|---|---|---|---|---|---|
| T1 | field/poly self-tests | Py | small fields | 100 % agreement | done (earlier turns) |
| T2 | factorisation `x^n − λ`, divisor enumeration | Py + MAGMA `Factorization` | `q ≤ 25`, `n ≤ 15` | identical factor/order lists | partially done |
| T3 | Thm 2 (twist ⟺ `λ^{p^κ+1}=1`) | Py + MAGMA | all `q`, `n ≤ 7`, all λ, κ | 0 counterexamples | done 1010/1010 |
| T4 | Thm 3 (`h^τ ≡ 0 ⟺ ⊆`) | Py + MAGMA | as T3 | 0 counterexamples; rejected variants counted | done (742/742, 1010/1010) |
| T5 | Thm 4 (`ord = r·h`) | Py | `n ≤ 30`, `q ≤ 25` | 0 counterexamples | done 2000/2000 |
| T6 | Thm 5 (padding identity) | Py (independent arith.) | random words, all `a` | exact equality | done 9192/9192 |
| T7 | Thm 5 (syndrome identity) | Py + MAGMA | all chains, `|a| ≤ 3` | exact, content-free | done 166 528/166 528 |
| T8 | Thm 6 (lcm / collision at `Θ`) | Py | abstract + CRT code | injective iff `T < Θ` | done |
| T9 | Thm 7 (ceiling; attainability) | Py | `p ∈ {2,3,5}`, `κ ≤ 4` | instances at `T/L → (p^κ+1)/(p^κ+2)` | done (`0.741`, `0.829`) |
| T10 | exact distances | Py exhaustive + MAGMA | `|C| ≤ 2^{16}` | identical `d` | done (F_4, F_16) |
| T11 | larger distances | MAGMA (`BCHBound`, `MinimumDistance`, `BKLC` upper) | `N ≤ 200` | interval reported | **to do** |
| T12 | quantum parameters + tables | both | search output | `[[N,K,d;c]]` + `T`, `T/L`, `HA` | partially (2 instances) |
| T13 | EA-QSC instances (`c > 0`) | both | non-dual-containing chains | `c = dim hull` verified by rank | **to do** |
| T14 | HA > 1 search | Py/MAGMA | `q ≤ 25`, `n ≤ 11`, dual-containing | first explicit `HA > 1` chain or report "none found" | **to do / Open Problem 3** |
| T15 | jitter/ambiguity | Py | arbitrary orders | criterion of Thm 8 | done |
| T16 | decoder simulation | Py/`stim`-style | small instances | syndrome table recovers `a` for all `a` | **to do** |
| T17 | non-existence witnesses | Py | small `q,n,λ` | list of `(λ,n)` with no tolerant chain (e.g. `F_4, n=3, λ=ω`) | partly done |

### 10.3 Algorithms to be printed (pseudocode)

```
SigmaDual(C, κ):  G = Gram(⟨b_s,b_t⟩_{σ_κ}); return nullspace(G)
TwistedReciprocal(h, κ): return x^{deg h}·h(1/x)^{σ_κ}
Tolerance(chain, A, λ): Θ = lcm_i  min{ d>0 : x^d ≡ 1 mod f_i }   (x-powers in R_{λ_i})
Syn(W, g_D, f): J = W/g_D in R_λ ; return J mod f
JitterAmbiguity(orders, J): {(Δ,ε): ε_i ≡ ε_j mod gcd(o_i,o_j), Δ ≡ −ε_i mod o_i}
ExhaustiveDistance(basis, alphabet, split): prune by CSS split; return exact d
EACSSParam(C1, C2): c = dim(C1 ∩ C2^{⊥σ}); K, d from EA-CSS
```

### 10.4 Reproducibility deliverables

`blueprint/verify/` (pure Python, no external math dependency for T1–T10, T14–T17) +
`RESULTS.md` (command → raw output table) + MAGMA scripts for T2/T3/T4/T11/T12/T13 + the
manual-check list: (i) `q=4, n=3, λ=1`, three windows; (ii) the F_4 flagship syndrome table;
(iii) the collision at `a = Θ = 21`; (iv) the two rejected criteria counts.

---

## PART 11 — Parameter Search

### 11.1 Search space and constraints

`(p, e, κ)`, `A` (component degrees `d_i`), `n`, `(λ_i)`, `(g_{i,C}, g_{i,D})`, `(a_l,a_r)` with:
`gcd(n,q) = 1`; `λ_i^{p^κ+1} = 1` (admissibility); `g_{i,D} | g_{i,C} | x^n − λ_i`,
`deg(g_{i,C}/g_{i,D}) > 0`; dual containment for the non-assisted case; `T ≤ Θ − 1`.

### 11.2 Stages

1. **Component table.** For each `(p,e,κ,λ)`: all divisors, `ord_f`, dual-containing flag,
   `[n,k,d]`, `k_q`. (Cache.)
2. **Chain assembly.** For each component and each factor pair with `ord_f` known; compute `Θ`,
   maximal window, `T/L`; keep the *new* quantities `Θ/n` and `HA = Θ/max_i ord_{f_i}`.
3. **Quantum layer.** `K`, `c`, `d` (exhaustive or bound).
4. **Pareto filtering** in `(T/L, K/L, d)`; no dominance-only discarding (tolerance is the topic).
5. **Comparison** only against rows of PART 12 with the same alphabet, length class and
   error-correction class; verdicts stated as measurable differences.
6. **Negative results** reported (e.g. `F_4, n=3, λ=ω`: no tolerant chain; `q=25, n=3`:
   no dual-containing component).

### 11.3 Objectives

`TE = T/L` (tolerance efficiency, symbol units); `ρ = K/(Nn)`; `Δ_Sing` (EA-Singleton gap);
`HA` (heterogeneity amplification); `r = ord(λ)` (the mechanism behind TE).

### 11.4 Search pseudocode

```
for (p,e,κ):  for λ with λ^{p^κ+1} = 1:  build component table (ord_f, dual-containing, k_q)
for each tuple of components:
    Θ = lcm(ord_{f_i}) ;  if Θ ≤ n: continue           # no ceiling break
    T = Θ − 1 ;  L = n + T ;  TE = T/L ;  HA = Θ/max ord
    if all components dual-containing: K = n − 2·dim_Fq(C^{⊥σ}) ; d = Exhaustive/CSS bound
    else: c = dim hull ; K = 2 dim ψ(C) − Nn + 2c
    record (p,e,κ,λ-pattern,n,Θ,T,L,K,d,c,TE,HA)
Pareto-filter; compare with PART 12; report best findings and all negatives
```

### 11.5 Expected outcomes (audit-calibrated, no over-promising)

* Confirmed by the audit: `TE → (p^κ+1)/(p^κ+2)` is attainable with a *single* component and
  `λ` of maximal order; verified for `(p,κ) = (2,1)` and `(2,2)`.
* To be searched: `HA > 1` instances (Open Problem 3/T14); EA-QSC instances with small `c`;
  instances with `d ≥ 5` by choosing BCH-type `g_i`.
* Risk: the headline instances are short and have small `K`; the paper therefore claims the
  *structural* result (ceiling + identity + decoupling), with parameter tables as illustration
  and no superiority claim.

---

## PART 12 — Literature Comparison Framework

### 12.1 Required columns

`Reference | Algebra | Field/Ring | Code Family | Length | Duality | Quantum Construction | Distance | Synchronization | Tolerance | Entanglement | Main New Feature`

### 12.2 Fairness rules

1. Tolerance is reported as stated by the source; a footnote converts to `T/L` **only** when the
   source fixes the padded length. Never silently re-normalise.
2. Alphabets are quoted as in the source; conversions (qudits ↔ qubits) are footnoted and
   never used to hide a difference.
3. Bounds are marked `≥` / `≤`; exhaustive values are marked `exact`.
4. No evaluative words ("better", "superior"); only measurable differences
   (`ΔT`, `Δd`, `ΔK`, `ΔT/L`) with the comparison criterion stated.

### 12.3 Baseline table (to be completed with real numbers; `—` = not applicable/not reported)

| Reference | Algebra | Field/Ring | Code Family | Length | Duality | Quantum Constr. | Distance | Synchronization | Tolerance | Entanglement | Main New Feature |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Fujiwara (2013) `[REF]` | `F_q` | field | cyclic chain | `n` | Euclidean dual-containing | CSS | `⌊(d_i−1)/2⌋` | yes | `T < ord_f \| n` | no | founding QSC |
| Fujiwara–Tonchev–Wong (2013) `[REF]` | cyclotomy | field | cyclic (QR/PG) | `n` | “ | CSS | designed | yes | `T = n−1` (max) | no | attains cyclic ceiling |
| Xie–Yuan–Fujiwara `[REF]` | field | field | augmented cyclic/QR | `p` | “ | CSS | d of QR | yes | `T < n` | no | augmentation framework |
| Luo–Ma–Lin 2019 `[REF]` | `F_q[u,v]`/product | field | `(u+v\|u−v)`, product codes | `2n`, `n₁n₂` | “ | CSS | component-based | yes | `T < ord_f ≤ 2n`; e.g. `[[105,39]]`, `T ≤ 104` | no | doubling + product |
| Du–Ma–Luo–Huang–Wang 2020 `[REF]` | non-chain ring | ring | `(λ(u+v)\|u−v)` | `2n` comp., QSC `4n` | “ | CSS | `min{2d₁,2d₂,max{…}}` | yes | `max` iff `ord_f = 2n` | no | constacyclic assembly |
| Liu–Liu 2021 `[REF]` | chain ring; `F_p+vF_p` | ring | constacyclic / Gray image | `n`, `2n` | “ | CSS | not reported | yes | “upper bound” | no | first ring QSCs |
| **QIP 2024, "QSC from `F_q + vF_q`"** `[REF]` | `F_q+vF_q` | ring | `(1−2v)`-constacyclic sums | `n`, `2n` | “ | CSS | not reported | yes | “upper bound” | no | three ring methods |
| Li–Zhu 2022 `[REF]` | field | field | constacyclic, BCH-type | `q^{2ℓ}−1` | “ | CSS | exact `δ` | yes | `T < n` | no | exact distance |
| Wang–Zhou / Liu–Kai / Xie et al. `[REF]` | cyclotomy | field | BCH/QR/cyclotomic | various | “ | CSS | BCH | yes | `T < n` | no | parameter families |
| Du–Ma–Liu `[REF]` | `F_q[x]/⟨x^{2ℓp^s}−1⟩` | field | repeated-root QC | `2ℓp^s` | “ | CSS | — | yes | inherited | no | quasi-cyclic QSCs |
| Tansuwannont–Nemec 2024 `[REF]` | operator algebra | field | hybrid/subsystem | `n` | CSS pair | subsystem | — | yes | inherited | no | hybrid QSCs |
| Hu–Liu 2025 / Zhang–Kong–Zheng 2026 `[REF]` | `F_q × (F_q+vF_q)` | ring | separable constacyclic, `(λ, β(1−2v))` | `n` | κ/ℓ-Galois hull | QECC / EAQECC (Construction X) | reported | **no** | — | yes | mixed weights (QECC only) |
| Galois hulls over affine algebras `[REF]` | semisimple `A` | ring/alg. | λ-constacyclic | `n` | κ-Galois hull | EAQECC via Gray map | examples | **no** | — | yes | general hull formulas |
| **This work** | `∏ F_{q^{d_i}}` | alg./ring | λ-constacyclic chain, mixed weights, κ-twist | `n` per component; block `n+T` | κ-Galois dual | κ-CSS / Hermitian / EA-CSS | exact for small, bounds otherwise | yes | `T ≤ lcm_i ord_{f_i} − 1`, `T/L → (p^κ+1)/(p^κ+2)` | optional | ceiling break + exact syndrome + decoupling + EA-QSC |

*(Every `[REF]` must be completed from PART 3's verified bibliographic data before submission;
rows without numbers are to be filled by the search T11–T13. No row may be filled with a number
that is neither read from the source nor computed here.)*

---

## PART 13 — Figures and Tables

### Figures (4 required + 2 optional)

**Fig. 1 — Algebraic decomposition.** `A = F_q[X]/⟨t⟩` → CRT → components `A_i` with weight
`λ_i`, orders `r_i = ord(λ_i)`, `h_i | n`, and the lcm arrow giving `Θ`; annotate the ceiling
`T/L ≤ Θ/(n+Θ)`.

**Fig. 2 — Pipeline.** "Finite ring/algebra → λ-constacyclic chain → σ_κ-dual & hull →
(dual containment | entanglement) → λ⁻¹-periodic padding & window syndrome → CSS/EA-CSS →
`[[N(n+T), K, d(;c)]]`", with two rails (tolerance; quantum data) meeting only at the end — the
visual form of the decoupling theorem.

**Fig. 3 — Tolerance map.** `T/L` versus `ord_f/n`; the cyclic ceiling line `T/L = 1/2`; the
points of all audited families (from PART 12) clustered below it; the two verified points of
this work above it (`0.741`, `0.829`); the asymptote `(p^κ+1)/(p^κ+2)`.

**Fig. 4 — Computational workflow.** Nodes T1–T17 with theorem labels and MAGMA replica block.

**Fig. 5 (optional) — Window/syndrome picture.** Slots `[−a_l, n+a_r−1]`, the sliding window,
the syndrome table `a ↦ x^{−a}`, and the collision at `a = Θ`.

**Fig. 6 (optional) — Decoder block diagram** with the shift-table lookup before CSS decoding.

### Tables (6 required)

**Tab. 1 — Notation** (`q,p,e,κ,σ_κ,A,A_i,e_i,N,λ,λ_i,R_λ,g,g_i,h,h^τ,C,D,f,f_i,r_i,h_i,Θ,ord_f,μ,a_l,a_r,T,L,K,d,c,HA,TE` + where defined + assumption).
**Tab. 2 — Literature comparison** (PART 12 columns).
**Tab. 3 — Component code data** (`q, n, λ, r, deg g, ord_f, [n,k,d], dual-containing, k_q`).
**Tab. 4 — Valid parameter sets** (admissible `(p,e,κ,λ)` patterns; maximal `Θ`; negative entries
included, e.g. `F_4, n=3, λ=ω`; `q=25, n=3`).
**Tab. 5 — Quantum codes** (`[[N(n+T), K, d(;c)]]`, `T`, `(a_l,a_r)`, `T/L`, `HA`, distance method);
must contain the two verified instances.
**Tab. 6 — Bounds/defect** (EA-Singleton for length `N(n+T)`; measured `Δ_Sing`; tolerant-Hamming
status flagged `[CONJECTURE]`).

---

## PART 14 — Q1-Level Manuscript Architecture

| § | Section | Content | Pages |
|---|---|---|---|
| 1 | Introduction | synchronization vs error correction; the same-object assumption; contributions C1–C5; the ceiling figure | 1.5 |
| 2 | Related work | prior-art map of PART 3.2 in prose; explicit non-novelty paragraph | 1.5 |
| 3 | Algebraic preliminaries | conventions (7.1), `A`, `σ_κ`, `R_λ`, chains, hulls, Gray map, models A/B/C | 2 |
| 4 | Duality and hull characterization | Thms 1–3; the rejected criteria as a remark with counts | 2 |
| 5 | Synchronization theory | padding D7, Lemma L5, Thm 5, Thm 6, decoder (Lemma L7); drift remark | 3 |
| 6 | The tolerance ceiling | Thm 4, Thm 7, corollaries; comparison with the cyclic ceiling | 2 |
| 7 | Quantum constructions | Thms 10–11; verified instances; distance discipline | 3 |
| 8 | Decoupling and consequences | Thm 9; asymmetric twists `(κ_i)`; EA-QSC design rules | 1.5 |
| 9 | Bounds, defect and conjectures | Conjectures 1–3; explicit "not proved" wording | 1.5 |
| 10 | Computational results | tables 3–5; reproducibility summary; negative results | 2.5 |
| 11 | Discussion | what is new, what is not; limits of the A-symbol model; reviewer-risk table | 1 |
| 12 | Limitations and open problems | Open Problems 1–5 | 0.75 |
| 13 | Conclusion | — | 0.5 |
| A | Proofs deferred | Thms 2–4, 9 details; Lemma L4 | 3 |
| B | Reproducibility | scripts, versions, commands, raw outputs, manual checks | 1.5 |
| C | Full tables | search output | 2 |

**Contribution list (paper-ready, no marketing).**

| ID | Contribution | Mathematical object | Main result | Evidence |
|---|---|---|---|---|
| C1 | Exact, content-free window syndrome for λ-constacyclic chains, with the correct padding convention and the general content formula | `B_{a_l,a_r}(w)`, `Syn_a` (D7, D8) | Theorem 5 | proof sketch + 166 528/166 528 checks |
| C2 | Tolerance invariant and ceiling: `Θ = lcm_i ord_{f_i}` with `ord_f = r·h`, hence `Θ | (p^κ+1)n` and `T/L < (p^κ+1)/(p^κ+2)`; the cyclic ceiling `T/L < 1/2` is the `λ = 1` case | `Θ`, `(r,h)`; Thm 4, 7 | verification 2000/2000, instances at 0.741 and 0.829 |
| C3 | Decoupling of synchronization from Galois self-orthogonality, enabling κ-twists per component and entanglement assistance at no tolerance cost | `hull_{σ_κ}`, `c` | Theorem 9 | structural + planned verification |
| C4 | Entanglement-assisted QSC (definition + parameter theorem) | `(a_l,a_r)`-EA-QSC | Theorem 11 | `[THEOREM TO BE PROVED]`; prior-art search ongoing |
| C5 | Tolerant Singleton/defect framework with explicitly labelled conjectures | `Δ_Sing`, tolerant Hamming | Conjectures 1–3 | definitions only |

**Reviewer-risk table.** "This is a known order formula applied to QSCs" → answered by the
ceiling theorem (a *provable* impossibility for all audited constructions and attainability
here) and by Fig. 3; "EA-QSC is not new" → the systematic search is a precondition, with the
fallback that C1–C3 stand alone; "the A-symbol model is unrealistic" → Models B/C and Open
Problem 1 are stated; "parameters are small" → no superiority is claimed, the claim is
structural.

---

## PART 15 — Provisional Title + Abstract + Keywords

### Titles (PROVISIONAL, five)

1. **Tolerance beyond the block length: constacyclic quantum synchronizable codes with exact window syndromes** *(PROVISIONAL)*
2. **Breaking the cyclic ceiling in quantum synchronizable codes: multiplier orders, λ-constacyclic chains and Galois twists** *(PROVISIONAL)*
3. **Exact synchronization syndromes and the decoupling of tolerance from self-orthogonality in quantum codes** *(PROVISIONAL)*
4. **Galois-twisted constacyclic synchronization: entropy-free tolerance amplification and entanglement-assisted quantum synchronizable codes** *(PROVISIONAL)*
5. **From cyclic ceilings to multiplier orders: a verified theory of tolerant quantum codes over semisimple algebras** *(PROVISIONAL)*

### Abstract (PROVISIONAL, 191 words)

> Quantum synchronizable codes (QSCs) correct block misalignment together with quantum noise.
> Their tolerance is governed by the order of a shift operator, and in every published family
> the padded block satisfies `T/L < 1/2`, because cyclic chains force the shift order to divide
> the block length. We show that this ceiling is an artefact of the cyclic weight `λ = 1`. For a
> λ-constacyclic chain `C ⊆ D` over `F_q` with `λ^{p^κ+1} = 1`, we first prove that a
> λ⁻¹-periodic padding makes the receiver's window syndrome equal to `x^{−a}` exactly and
> independently of the transmitted codeword; we then prove that the shift order satisfies
> `ord_f = r·h` with `h | n`, `r = ord(λ) | p^κ+1`, so that the tolerance obeys
> `T/L < (p^κ+1)/(p^κ+2)` and exceeds the block-length ceiling whenever `λ ≠ 1`. Verified
> instances include `[[54,2,3]]_2` (`T/L = 0.741`) and `[[164,1,3]]_4` (`T/L = 0.829`). Because
> the syndrome map is independent of the inner product, κ-Galois self-orthogonality decouples
> from synchronization, which yields an entanglement-assisted QSC with
> `c = dim hull_{σ_κ}` and unchanged tolerance. All structural claims are accompanied by two
> independent machine verifications, including counterexamples to two plausible but false
> criteria.

### Keywords

Quantum synchronizable codes; block synchronization; constacyclic codes; Galois hull; Hermitian
dual; entanglement-assisted quantum error correction; semisimple algebras; tolerance;
finite fields; reproducible computation.
