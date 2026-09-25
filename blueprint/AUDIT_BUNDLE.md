# AUDIT BUNDLE — Galois-Hull Synchronization Blueprint
### Single-file bundle for external review (e.g. pasting into an LLM for auditing)

Contents, in order:
1. `BLUEPRINT.md`      — PART A ... PART Q (the deliverable: research-paper blueprint)
2. `PART_O_blueprint.tex` — the LaTeX blueprint (PART O)
3. `verify/RESULTS.md` — computational evidence log (every number quoted in the blueprint)

**How to audit this efficiently (suggested prompts).** Ask the reviewer to check, in this order:
(a) *Internal consistency*: does every claim in PART N (abstract) appear in the PART E ledger, and is
each ledger row tagged with an honest status (`[PROVED-HERE]`, `[VERIFIED-COMPUTATIONALLY]`,
`[THEOREM TO BE PROVED]`, `[CONJECTURE]`, `[OPEN PROBLEM]`)?
(b) *No fabrication*: is there any numeric claim not traceable to `verify/RESULTS.md` or marked
`[PARAMETER TABLE]`? Is any reference in PART P invented (groups A/B are corpus- or
search-verified; group C is explicitly flagged as requiring verification)?
(c) *No false strengthening*: PART F.3 records that the naive statement
"lambda^{p^k+1}=1 implies every lambda-constacyclic code contains its sigma-dual" is FALSE;
PART F.5/Thm 3 record that the gcd-based criterion is FALSE (268/1010) and that the
"both-degrees-n" divisibility form diverges (344/742). Are these traps avoided everywhere else?
(d) *Mathematical soundness of the two headline theorems* (window-syndrome identity; lcm
tolerance law): does the stated proof strategy in PART G close the gap, and is the
`verify/verify_syndrome.py` independent-implementation argument convincing?
(e) *Novelty*: given the audit of the 14 works in PART B, is the claimed gap (PART C) real, and is
the entanglement-assisted quantum synchronizable code (EA-QSC) genuinely new, or is there prior
art the search missed?
(f) *Venue fit*: would this clear a Q1 review, and which of the reviewer objections in PART M's
risk table is the weakest defended?

---



<!-- ===================== BEGIN BLUEPRINT.md ===================== -->

# BLUEPRINT — Synchronization-Aware Galois-Hull Quantum Codes
### A research-paper blueprint (not the paper) for a Q1 quantum-information venue

**Status of this document.** This is a *blueprint*: it specifies the mathematics to be
proved, the constructions to be built, the computations to be run and the manuscript to
be written. It deliberately contains **no invented theorem and no invented number**.
Every statement is tagged:

| Tag | Meaning |
|---|---|
| `[PROVED-HERE]` | already proved in this blueprint (proof sketch given, complete proof to be written in the paper) |
| `[VERIFIED-COMPUTATIONALLY]` | statement checked exhaustively by the scripts in `blueprint/verify/` (see `verify/RESULTS.md`); a human-readable proof is still to be written |
| `[CONJECTURE]` | believed true, no proof yet; must be labelled as a conjecture in the paper |
| `[OPEN PROBLEM]` | explicitly open; stated as such |
| `[THEOREM TO BE PROVED]` | target theorem of the paper; strategy given, proof pending |
| `[COMPUTATIONAL RESULT]` / `[PARAMETER TABLE]` | placeholder to be filled by the plan in PART I/J |
| `[REFERENCE]` | to be completed from PART P; no fabricated citations |
| `INSUFFICIENT EVIDENCE — REQUIRES VERIFICATION` | audit flag |

A standing convention for the whole document: **witnessed facts are separated from
aspirational ones.** Section G lists, for every theorem, exactly what is proved, what is
computed, and what is left open.

---

## PART A — Executive Research Idea

**One-sentence idea.** *Synchronization in quantum synchronizable codes (QSCs) is governed
by the constacyclic structure of a code chain alone, while self-orthogonality — the
requirement that makes the code quantum — is governed by the Gram/hull data of that same
chain; the two requirements are logically independent, and exploiting this separation
inside the semisimple-algebra framework of Galois-hull theory yields (i) a new tolerance
law, (ii) a genuinely larger design space for QSCs, and (iii) the first
entanglement-assisted quantum synchronizable codes.*

**The object we propose to introduce.** For a finite semisimple commutative algebra
$A=\prod_i A_i$ over $\mathbb F_q$ (e.g. $A=\mathbb F_q[X]/\langle t(X)\rangle$ with $t$
squarefree, and in the flagship example $A=\mathbb F_4\times\mathbb F_4$), a unit
$\lambda=\sum_i\lambda_ie_i$ with **independent** component weights $\lambda_i$, and a chain
of $\lambda$-constacyclic $A$-linear codes $C\subseteq D$, define the *window padding rule*
of the block-synchronization channel by continuing a codeword $\lambda$-periodically,
transmitting the segment $j\in[-a_l,\,n+a_r-1]$, and decoding the misalignment $a$ from the
*Galois-twisted window syndrome*. The synchronization capability is then the **least common
multiple of the component orders of $x$**, and the quantum layer is the
$\kappa$-Galois hull of the same chain.

**The four deliverable mathematical claims.**

1. **Window-syndrome theorem** — for a $\lambda$-constacyclic chain $C=\langle g_C\rangle
   \subseteq D=\langle g_D\rangle$ with $f=g_C/g_D$, the receiver's syndrome equals
   $x^{-a}\in R_\lambda/\langle f\rangle$ *exactly* (no scalar correction), independently of
   the transmitted codeword, and the map $a\mapsto x^{-a}$ is injective on
   $[-a_l,a_r]$ **iff** $a_l+a_r<\mathrm{ord}_f(x)$.
   `[VERIFIED-COMPUTATIONALLY]` (1262 configurations, 0 failures;
   independent re-implementation in `verify_syndrome.py`).
2. **$\mathrm{lcm}$ tolerance law** — over a semisimple algebra with
   $m$ components the tolerance is $\mathrm{lcm}_i\,\mathrm{ord}_{f_i}(x)-1$, not any single
   order; consequently tolerance is *heterogeneity-amplified* and can exceed the block
   length $n$, i.e. $T/L$ can exceed $1/2$ — impossible for cyclic QSCs, where
   $T<n=L-T$. `[VERIFIED-COMPUTATIONALLY]` (21 = lcm(21,7) distinct syndrome pairs, 0
   collisions; also stable under unequal component offsets).
3. **Galois-hull synchronization theorem** — the synchronization part needs only the chain
   $C\subseteq D$; the quantum part needs only $C^{\perp_{\sigma_\kappa}}\subseteq C$, which by
   the verified criterion $h^\tau\equiv0\ (\mathrm{mod}\ g)$ is a divisibility statement in
   $R_\lambda$. Hence $\kappa$-twisted (Hermitian as the special case $\kappa=e/2$) and
   entanglement-assisted QSCs exist with $c=\dim\mathrm{hull}_{\sigma_\kappa}(C)$ ebits, and
   *asymmetric* twists $(\kappa_1,\kappa_2)$ per component are admissible.
   `[VERIFIED-COMPUTATIONALLY]` for the containment criterion (742/742) and the twist
   condition $\lambda^{p^\kappa+1}=1$ (1010/1010); `[THEOREM TO BE PROVED]` for the
   EA-QSC parameter theorem.
4. **Explicit tolerant family** — a fully computed instance:
   $\mathbb F_4$, $n=7$, $\lambda=(\omega,1)$, $\kappa=1$ (Hermitian twist) gives the classical
   data $[7,4,3]_4$ per component, the quantum code $[[14,2,3]]_2$, and an
   $(a_l,a_r)$-QSC family $[[14+T,\,2,\,3]]_2$ with tolerance $T\le20>n=7$ and
   $T/L=0.588$ at maximal length $34$ qubits.
   `[COMPUTATIONAL RESULT]` (exhaustive, `verify_params.py`).

**Why this is not a rebranding exercise.** (a) The tolerance law is *not* a restatement of
$\mathrm{ord}_f(x)$: it is a different invariant (an lcm over components) that changes which
parameter sets are admissible. (b) The separation of synchronization from
self-orthogonality is a *design principle* absent from every paper audited in PART B: all of
them derive tolerance and quantum parameters from the same single cyclic object.
(c) The mixed-weight algebra generalizes both the field QSC theory (all $\lambda_i$ equal,
$m=1$) and the ring QSC theory in the literature, which is locked to $\lambda=(1,-1)$ or to
$\lambda_1^2+1=0$ (see PART B, Liu–Liu; Du–Ma–Luo–Huang–Wang), and thus removes a genuine
existence restriction rather than renaming one. (d) The entanglement-assisted object
$\text{EA-QSC}$ is, as far as the audited corpus and a targeted literature search show,
new — but this is flagged in PART Q as requiring a systematic search before any novelty
claim is published.

---

## PART B — Source Paper Audit

Method: the 12 papers of `Quantum Synchronizable.zip` plus the Galois-hull paper were
extracted to text (`/home/user/papers/txt/`) and read; extractions of formulae are
machine-generated and therefore flagged where a symbol is uncertain. Each row is one of the
14 required audit items. `[REQ-VERIFY]` marks a statement that must be re-checked against
the published PDF before it is quoted in the paper.

### B.1 — Debnath, Islam, Martínez-Moro, Prakash, *Galois hulls of constacyclic codes over affine algebra rings* (`Galois_hulls_constacyclic_affine.txt`; arXiv:2412.08512v1)

| Item | Finding |
|---|---|
| Problem | Determine $\kappa$-Galois hulls of $\lambda$-constacyclic codes over a semisimple ("affine algebra") ring $A$ and apply them to entanglement-assisted quantum codes |
| Algebraic structures | $A=\mathbb F_q[X_1,\dots,X_\ell]/\langle t_1,\dots,t_\ell\rangle$, $t_i$ squarefree ⟹ $A\cong\prod_{S(\nu)\in\hat S}\mathbb F_{q^{d_{S(\nu)}}}$; primitive idempotents $e_{S(\nu)}$; CRT over $\hat S$ |
| Code family | $\lambda$-constacyclic $A$-linear codes of length $n$, $\gcd(n,q)=1$ (plus a repeated-root extension in Thm 8 with $n=n'p^{e'}$) |
| Parameters | Length $n$, $A$-dimension, $q$-dimension $\sum_{S(\nu)}\cdots$; examples over $\mathbb F_9,\mathbb F_{25}$ |
| Duality | $\kappa$-Galois inner product $\langle x,y\rangle_\kappa=\sum x_iy_i^{p^{e-\kappa}}$ *(source convention; our $\sigma_\kappa$ corresponds to $\kappa_{\text{ours}}=e-\kappa_{\text{source}}$ — see PART F, Remark F.3.2)*; $C^{\perp_\kappa}$ is $\lambda^{-p^{e-\kappa}}$-constacyclic |
| Construction | $C=\bigoplus_{S(\nu)}C_{S(\nu)}e_{S(\nu)}$; $\mathrm{hull}_\kappa(C)=\langle\mathrm{lcm}(g,h^\#)\rangle$; containment criterion (Thm 6) $\;x^n-\lambda_{S(\nu)}\equiv0\ (\mathrm{mod}\ g_{S(\nu)}g^{(l-1)\#}_{S(\nu)})$ |
| Quantum construction | EAQECC $[[n,\,k-\dim\mathrm{hull}_\kappa,\,d;\,n-k-\dim\mathrm{hull}_\kappa]]_q$ via Gray map $\psi$; $\psi(C^{\perp_\kappa})=\psi(C)^{\perp_\kappa}$, $\psi(\mathrm{hull}_\kappa)=\mathrm{hull}_\kappa(\psi(C))$; bound $2(d-1)\le n-k+c$ |
| Bounds | Entanglement-assisted Singleton-type inequality as above; no QSC bound |
| Main theorems | Thms 1–10 + Cor. 3.1–3.5; Thm 8 gives the $q$-dimension of $\mathrm{hull}_\kappa$ via cyclotomic data $D^t_{S(\nu)}$ |
| Computational methodology | **None beyond examples** (two worked examples, Table 1 with $n,\lambda,g_1,g_2,\psi(C)$, EAQECC parameters, "Diff." column) |
| Examples/tables | Ex. 2: $\mathbb F_9$, $n=7$, $\lambda=e_1+\omega^2e_2$, $\kappa=1$ ⟹ $[[14,10,4;4]]_9$; Ex. 3: $\mathbb F_{25}$, $n=7$ ⟹ $[[26,20,4;2]]_{25}$; Remark 2 discusses $[[10,1,8;5]]_9$ |
| Limitations | Remark 1: if the Gray-map matrix is $M=I_N$ **no gain is obtained**; results are for EAQECC only; no distance computation; no decoding |
| Stated future work | Enumerate/count non-isometric constacyclic codes for a given $\kappa$-Galois hull dimension over $A$ (explicitly called open) |
| Hidden possibilities | (i) the $\kappa$-twist is used *only* to control hull dimension — never as a *synchronization* parameter; (ii) the Gray-map gain problem ($M\ne I_N$) is left open; (iii) the CRT structure is never used to *design* an order-theoretic invariant (our lcm law); (iv) word "synchroniz*" occurs **0 times** in the paper |

**Audit note (consistency check).** The literal criterion quoted above as Thm 6 was tested in
this workspace: in **344 of 742** admissible cases the divisibility statement
$x^n-\lambda\equiv0\ (\mathrm{mod}\ g\,h^\tau)$ does **not** agree with dual containment, while
the statement $h^\tau\equiv0\ (\mathrm{mod}\ g)$ agrees in **742/742** cases
(`verify/RESULTS.md`). Either the source's $g^{(l-1)\#}$ is normalized differently from my
$h^\tau$, or Thm 6 as extracted needs restatement. **INSUFFICIENT EVIDENCE — REQUIRES
VERIFICATION against the published PDF.** The blueprint uses only the verified criterion.

### B.2 — Fujiwara, *Block synchronization for quantum information* (`1206.0260v5.txt`)

| Item | Finding |
|---|---|
| Problem | Correct block misalignment (insertions/deletions at block boundaries) simultaneously with quantum errors |
| Structures | Cyclic codes over $\mathbb F_q$, ring $R=\mathbb F_q[x]/\langle x^n-1\rangle$, orbits of the shift on the code |
| Code family | Cyclic $C_1\subset C_2$, $C_1^{\perp}\subseteq C_1$, generator polynomials $g_1,g_2$, $f=g_1/g_2$ |
| Parameters | $[[n+a_l+a_r,\,2k_1-n]]_q$, $a_l+a_r<\mathrm{ord}_f(x)$; corrects $\lfloor(d_1-1)/2\rfloor$ phase and $\lfloor(d_2-1)/2\rfloor$ bit errors |
| Duality | Euclidean; $C_1^{\perp}\subseteq C_1$; containment via GCD/self-reciprocal-factor condition for cyclic codes |
| Construction | Padding with periodic continuation; syndrome $x^a\bmod f$ identifies the shift; logical states in $V_{g}=\mathrm{span}\{|C^{\perp}+r_i+g\rangle\}$ |
| Quantum construction | CSS-type stabilizer code; window syndrome subspace $|Orb_x[g]|=n$ |
| Bounds | No Singleton/Hamming-type bound for the tolerant block; tolerance maximal iff $\mathrm{ord}_f(x)=n$ |
| Main theorems | Existence theorem for $(a_l,a_r)$-QSCs; equivalence between the padding-and-syndrome mechanism and correctable misalignment |
| Computational methodology | Examples by hand |
| Examples/tables | Small illustrative examples only |
| Limitations | $T<n$ automatically; cyclic (not constacyclic, not ring); no entanglement assistance; no hull theory |
| Stated future work | Generalizations to other algebraic settings *(read in the corpus text; `[REQ-VERIFY]` for the exact wording)* |
| Hidden possibilities | (i) $\lambda\ne1$ would decouple $T$ from $n$; (ii) the syndrome argument never uses self-orthogonality — the separation principle that this blueprint formalizes |

### B.3 — Fujiwara, Tonchev, Wong, *Algebraic techniques in designing quantum synchronizable codes* (`Algebraic_techniques_...txt`, PRA 88, 012318)

| Item | Finding |
|---|---|
| Problem | Systematic design of QSCs from algebraic families (dual-containing codes) |
| Structures | Cyclotomic cosets, projective geometry codes, cyclic codes |
| Code family | Cyclic codes whose duals are contained in them; also BCH-type families |
| Parameters | QSC parameters $[[n+a_l+a_r,\cdot]]$ with tolerance bounded by $\mathrm{ord}_f$ |
| Duality | Euclidean dual containment as the quantum-enabling condition |
| Construction | Fujiwara padding + CSS islands; explicit logical-state construction |
| Quantum construction | Stabilizer codes with bounded-weight/geometry origin |
| Bounds | Tolerance upper bound and error bounds; no Singleton-type tolerant bound |
| Main theorems | Existence theorems for QSC families from projective geometry and from cyclotomy |
| Computational methodology | Tables generated from enumeration of cosets |
| Examples/tables | Parameter tables of QSCs |
| Limitations | Field-only, cyclic-only, no rings, no Galois/Hermitian twist, no entanglement assistance |
| Stated future work | Broader algebraic families *(as above, `[REQ-VERIFY]`)* |
| Hidden possibilities | The "island" construction is independent of the inner-product choice, hence open to Galois twisting |

### B.4 — Nemec, Klappenecker, *hybrid quantum error correction* (`1911.12260v2.txt`)

| Item | Finding |
|---|---|
| Problem | Codes correcting both amplitude(X)- and phase(Z)-type errors asymmetrically ("hybrid") |
| Structures | Stabilizer formalism with degenerate/non-Pauli (e.g. amplitude-damping) error models |
| Code family | Genuine hybrid codes (CWS and stabilizer) |
| Parameters | $[[n,k:1,2]]_2$-type and related; e.g. Thm 11: $n$ odd ⟹ $[[n,n-3:1,2]]_2$ |
| Duality | Knill–Laflamme conditions with detectable-error sets |
| Construction | Hybrid basis states; explicit generators |
| Quantum construction | Stabilizer/hybrid stabilizer codes |
| Bounds | Rains-type bounds for $(n,K,2)$ codes; Hamming-type counting |
| Main theorems | Thms 11, 12 (families with prescribed lengths) |
| Computational methodology | Number-theoretic construction of lengths, no QSC computation |
| Examples/tables | Length tables |
| Limitations | No synchronization model; no constacyclic/ring structure; binary |
| Stated future work | Extensions to other error models |
| Hidden possibilities | Hybrid (classical+quantum) message structure combined with the ring structure could give hybrid-tolerant codes — **listed as an open possibility, not claimed** |

### B.5 — Tansuwannont, Nemec, *hybrid subsystem QSCs* (`2409.11312v2.txt`)

| Item | Finding |
|---|---|
| Problem | Subsystem/hybrid generalization of synchronization |
| Structures | Subsystem stabilizer codes, gauge group, CSS pair $C_x,C_z$ with $C_z^{\perp}\subseteq C_x$ |
| Code family | Subsystem QSCs; hybrid subsystem QSCs |
| Parameters | $[[n,k,d]]$ with $k=k_x+k_z-n$ (their Thm 1) |
| Duality | CSS orthogonality $C_z^{\perp}\subseteq C_x$ — *not* a hull condition |
| Construction | Gauge fixing + Fujiwara padding; subsystem window syndromes |
| Quantum construction | Subsystem codes; error correction and misalignment handled by different generators |
| Bounds | Translation of subsystem quantum bounds |
| Main theorems | Thm 1 and the hybrid subsystem synchronization construction |
| Computational methodology | Symbolic/example level |
| Examples/tables | Illustrative examples |
| Limitations | Field-only, cyclic-only, no Galois twist; the CSS pair is *not* required to be a constacyclic chain (so tolerance is inherited from a cyclic sub-code) |
| Stated future work | Broader subsystem families |
| Hidden possibilities | The $C_x\ne C_z$ freedom is a *second* separation of concerns (X-side vs Z-side) and composes with our component separation; flagged as `[OPEN PROBLEM]` |

### B.6 — Du, Ma, Luo, Huang, Wang, *On a family of QSCs based on the $(\lambda(u+v)|u-v)$ construction* (`On_a_Family_...txt`; IEEE Access 8, 2020)

| Item | Finding |
|---|---|
| Problem | QSCs from a non-chain-ring construction of negacyclic codes |
| Structures | $R=\mathbb F_q[u,v]/\langle u^2-1,v^2-1,uv-vu\rangle$; the map $(\lambda(u+v)\mid u-v)$; components $\lambda_1,\lambda_2$ with $\lambda_2=-\lambda_1$, $\lambda_1^2+1=0$ |
| Code family | $\lambda$-constacyclic components assembled into a negacyclic code of length $2n$; $g=g_1g_2$ |
| Parameters | $[2n,k_1+k_2,\min\{2d_1,2d_2,\max\{d_1,d_2\}\}]$; QSC length $4n$ |
| Duality | Euclidean on the assembled negacyclic code; $C^{\perp}=C_1^{\perp}\curlyvee C_2^{\perp}$ |
| Construction | Generator matrix $G=\begin{pmatrix}-\lambda_2G_1&G_1\\ \lambda_1G_2&-G_2\end{pmatrix}$; Theorem 2 |
| Quantum construction | QSC from dual-containing negacyclic codes; existence requires $p\equiv1\bmod4$ (any $m$) or $p\equiv3\bmod4$ with even $m$ |
| Bounds | Maximum tolerance iff $\mathrm{ord}(f(x))=2n$ |
| Main theorems | Thms 1–5 incl. the parameter theorem for the assembled code |
| Computational methodology | Explicit examples/tables |
| Examples/tables | Parameter tables of tolerant QSCs |
| Limitations | Weights **locked** ($\lambda_2=-\lambda_1$, $\lambda_1^2+1=0$); ring is fixed; tolerance still a single order; no Galois/Hermitian twist; no entanglement assistance |
| Stated future work | Other ring constructions |
| Hidden possibilities | The locking condition is an *existence restriction* imposed by the need to make the assembled code literally negacyclic; abandoning it (our mixed-weight formulation) is where the new design space comes from |

### B.7 — Li, Zhu, *constacyclic QSCs* (`s10773-022-05163-1.txt`, IJTP 2022) `[REQ-VERIFY: exact title/volume]`

| Item | Finding |
|---|---|
| Problem | QSCs with exact minimum distance and high misalignment tolerance from constacyclic codes |
| Structures | Cyclic/constacyclic codes over $\mathbb F_q$, cyclotomic cosets |
| Code family | $\lambda$-constacyclic codes of length $n=q^{2\ell}-1$ (and relatives) |
| Parameters | $(a_l,a_r)$-$[[n+a_l+a_r,\,n-4\ell(\delta_1-1-\lfloor\delta_1/q\rfloor)]]_q$; corrects $\lfloor(\delta_1-1)/2\rfloor$ phase and $\lfloor(\delta_2-1)/2\rfloor$ bit errors (Thms 3.13, 3.14) |
| Duality | Euclidean dual containment; explicit GCD-of-coset conditions on $\delta_0$ |
| Construction | Two cyclic/constacyclic codes $C_1,C_2$ with $g_1,g_2$, coset sets |
| Quantum construction | Stabilizer QSC with designed distance |
| Bounds | Tolerance $a_l+a_r<n$; exact minimum distance |
| Main theorems | Thms 3.13, 3.14 (two congruence cases $q\equiv3,1\bmod4$) |
| Computational methodology | Explicit parameter examples (e.g. $q=5,\ell=2$: $[624,600,8]$, $[624,616,3]$ components; $(a_l,a_r)$-$[[624+a_l+a_r,576]]_5$) |
| Examples/tables | Examples 3.15, 3.16 and parameter tables |
| Limitations | Field-only; weights $\lambda$ appear but the *tolerance* is still governed by one order; $T<n$; no entanglement assistance |
| Stated future work | Extensions to other lengths |
| Hidden possibilities | The "highest possible tolerance" claim is *relative to* $\mathrm{ord}_f$; a multi-component lcm law would relax the notion of "highest possible" — flagged in PART K |

### B.8 — Shi, Yue, Huang, *Whiteman cyclotomy QSCs* (`s12095-021-00501-2.txt`) `[REQ-VERIFY: journal/title]`

| Item | Finding |
|---|---|
| Problem | Two classes of QSCs from cyclotomic classes of order two |
| Structures | Whiteman cyclotomy, cyclotomic classes over $\mathbb Z_{2q}$ |
| Code family | Cyclic codes arising from the cyclotomic classes (optimal/almost optimal) |
| Parameters | QSC parameters inherited from the cyclic codes; good bit/phase error capability |
| Duality | Euclidean dual containment |
| Construction | Fujiwara padding with cyclotomic generators |
| Quantum construction | Stabilizer QSC |
| Bounds | Optimality of the underlying cyclic codes |
| Main theorems | Two construction theorems for the cyclotomic classes |
| Computational methodology | Cyclotomic-coset computation |
| Examples/tables | Parameter tables |
| Limitations | Field-only, cyclic-only, $T<n$ |
| Stated future work | Other cyclotomies |
| Hidden possibilities | None beyond parameter enrichment; confirms the "parameter-only" culture of the corpus (evidence for gap G3) |

### B.9 — Wang, Zhou, *BCH-type QSCs of length $(q^m-1)/a$* (`s12095-025-00815-5.txt`) `[REQ-VERIFY]`

| Item | Finding |
|---|---|
| Problem | QSCs from (non-primitive, narrow-sense) BCH codes |
| Structures | Cyclotomic cosets, BCH bounds |
| Code family | Cyclic codes of length $(q^m-1)/a$; BCH-type |
| Parameters | QSCs with BCH-designed distances; one occurrence of a constacyclic variant |
| Duality | Dual containment by coset arguments |
| Construction | Fujiwara padding |
| Quantum construction | Stabilizer |
| Bounds | BCH bound |
| Main theorems | Construction theorems for the BCH family |
| Computational methodology | Coset enumeration + tables |
| Examples/tables | Parameter tables |
| Limitations | Field-only; no ring; $T<n$ |
| Stated future work | Further lengths |
| Hidden possibilities | BCH designed-distance technology transfers to our mixed-weight construction (PART G, Thm 10) |

### B.10 — Liu, Kai, *BCH + QR QSCs* (`s12190-022-01811-1.txt`) `[REQ-VERIFY: journal]`

| Item | Finding |
|---|---|
| Problem | QSCs from BCH codes and quadratic-residue codes |
| Structures | Cyclotomic cosets; QR codes |
| Code family | BCH/QR cyclic codes |
| Parameters | QSC parameters with designed distances |
| Duality | Dual containment |
| Construction | Fujiwara padding |
| Quantum construction | Stabilizer |
| Bounds | BCH bound |
| Main theorems | Construction theorems |
| Computational methodology | Tables |
| Examples/tables | Parameter tables |
| Limitations | Field-only, $T<n$ |
| Stated future work | Extension to other families |
| Hidden possibilities | As B.9 |

### B.11 — Du, Ma, Liu, *repeated-root QC QSCs* (`s40314-023-02298-7.txt`) `[REQ-VERIFY: journal]`

| Item | Finding |
|---|---|
| Problem | QSCs (and QECCs) from repeated-root quasi-cyclic codes |
| Structures | $\mathbb F_q[x]/\langle x^{2\ell p^s}-1\rangle$; 2-generator QC codes |
| Code family | Repeated-root QC codes of length $2\ell p^s$; the only *quasi-cyclic* member of the QSC corpus |
| Parameters | Theorem 3 gives the generator structure; QSC parameters derived |
| Duality | Euclidean dual of the 2-generator QC code |
| Construction | Generator pairs $(\prod_t(M_t)^{i(t)-1},\,k(x)\prod_t(M_t)^{i(t)-1})$ |
| Quantum construction | Stabilizer QSC from the QC code |
| Bounds | Length/dimension formulas; no Singleton-type tolerant bound |
| Main theorems | Thm 3 and its analogue for the second generator form |
| Computational methodology | Explicit factorization of $x^{2\ell p^s}-1$ |
| Examples/tables | Examples with repeated-root factors |
| Limitations | Not constacyclic; no rings; no Galois twist; no hull dimension |
| Stated future work | Other QC lengths |
| Hidden possibilities | QC structure would allow *multi-block* synchronization (open) |

### B.12 — La Guardia, *asymmetric quantum BCH codes* (`0239-0252.txt`, QIC 11(3&4):239–252, 2011)

| Item | Finding |
|---|---|
| Problem | Asymmetric quantum codes ($d_z\ne d_x$) from BCH codes |
| Structures | Cyclotomic cosets, BCH bound, CSS |
| Code family | BCH codes of length $q^m-1$ |
| Parameters | $[[n,n-m(4q-5)-2,\,d_z\ge(2q+2)/d_x\ge2q]]_q$ (Thm 4), generalized to $[[n,n-m(4q-c-5)-2,\ldots]]_q$ (Thm 5) |
| Duality | CXS/CSS formulas (their Thm 3) with $d_x=\min\{\mathrm{wt}(C_1\setminus C_2),\mathrm{wt}(C_2^{\perp}\setminus C_1^{\perp})\}$ |
| Construction | Coset-based defining sets |
| Quantum construction | CSS (asymmetric) |
| Bounds | BCH bound |
| Main theorems | Thms 4, 5 |
| Computational methodology | Hand-verified coset counts |
| Examples/tables | Example parameter lists |
| Limitations | Not synchronizable; not rings |
| Stated future work | Other classical families |
| Hidden possibilities | **Asymmetry is our blueprint's analogue for $\kappa$:** an asymmetric pair $(\kappa_1,\kappa_2)$ of twists plays the role that $(d_x,d_z)$ plays here |

### B.13 — Liu, Liu, *Quantum synchronizable codes from finite rings* (`[REFERENCE]` QIP 20:125–144, 2021, DOI 10.1007/s11128-021-03058-4; identified by targeted search, PDF not in the corpus)

| Item | Finding |
|---|---|
| Problem | QSCs from cyclic/constacyclic codes over finite rings |
| Structures | Finite chain rings; semi-local rings $\mathbb F_p+v\mathbb F_p$ with $v^2=v$ |
| Code family | (i) dual-containing codes over chain rings; (ii) Gray images of constacyclic codes over $\mathbb F_p+v\mathbb F_p$ |
| Parameters | QSC parameters whose "synchronization capabilities attain the upper bound" |
| Duality | Euclidean; dual containment for the chain-ring method |
| Construction | CSS on ring codes; CSS on Gray images |
| Quantum construction | Stabilizer QSCs |
| Bounds | Tolerance $\le$ upper bound; no lcm-type law |
| Main theorems | Two construction theorems (one per method) |
| Computational methodology | Examples |
| Examples/tables | Example QSCs |
| Limitations | Weight restricted (the companion literature uses $(1-2v)$-constacyclic, i.e. component weights $(1,-1)$); components always the same field; the tolerance is a single order; no Galois twist; no entanglement assistance |
| Stated future work | `[REQ-VERIFY]` |
| Hidden possibilities | The Gray-map route shows ring structure is physically acceptable to the community; but it treats the *Gray image* as the code, which forces $T$ to be computed in the image — our treatment keeps the channel on $A$-symbols (PART H, Model H.2.1) and states the difference explicitly |

### B.14 — Xie, Yuan, Fujiwara, *Quantum synchronizable codes from augmentation of cyclic codes* (`Quantum_Synchronizable_Codes_From_Augmen.txt`; venue unconfirmed, `[REQ-VERIFY]`)

| Item | Finding |
|---|---|
| Problem | Obtain QSCs of positive dimension from augmented cyclic codes, avoiding the dimension loss caused by requiring $C^\perp\subseteq C$ |
| Structures | Binary cyclic codes, quadratic-residue (QR) codes, augmentation, $\mathbb F_2[x]/\langle x^n-1\rangle$ |
| Code family | $C_2\subset C_1$ cyclic with $C_2^\perp\subseteq C_2$ (their Thm 3.1, quoted from the founding paper); augmented QR codes |
| Parameters | QSC parameters of positive dimension; QR-code lengths |
| Duality | Euclidean dual containment; deleting a minimal polynomial of the QR code preserves dual containment (their Lemma 4.4) |
| Construction | Fujiwara padding applied to the augmented code as $C_1$ together with the dual-containing QR code as $C_2$ |
| Quantum construction | Stabilizer QSC |
| Bounds | They state (quoting the founding paper) that the maximum tolerable magnitude of a QSC is **upper bounded by its length**, and prove their QR-based family attains this bound |
| Main theorems | Thm 3.1 (existence, quoted), Lemma 4.4, attainment theorem for QR-based QSCs |
| Computational methodology | Explicit QR-code computations and examples |
| Examples/tables | Tables of augmented QR QSCs |
| Limitations | Binary, cyclic-only; augmentation enriches the *code* but not the *class*; no rings, no hull dimensions, no Galois twists |
| Stated future work | `[REQ-VERIFY]` |
| Hidden possibilities | Their length bound is the clearest published expression of the ceiling that the $\mathrm{lcm}$ law of this blueprint removes for mixed-weight algebras: in the single-component cyclic setting $\mathrm{ord}_f(x)\mid n$, so $T<n$; with $m\ge2$ or $\lambda\ne1$ the same *mechanism* yields $T>n$ `[VERIFIED-COMPUTATIONALLY]`. Their statement must nevertheless be re-read in context before being contrasted (it may be intended as $T\le L$), hence the flag `[REQ-VERIFY]`. |

**Corpus-level aggregate evidence (used for PART C).**  (Audited works: 12 corpus papers B.2–B.14 plus the Galois-hull framework paper B.1 and the external ring-QSC paper B.13 = 14 works.)

| Statistic | Value |
|---|---|
| Papers in the QSC corpus mentioning "constacyclic"/"negacyclic" | 3 of 12 (Li–Zhu; Du–Ma–Luo–Huang–Wang; one incidental mention in La Guardia) |
| Papers using $\kappa$-Galois (non-Euclidean, non-Hermitian-special-case) inner products | 0 of 12 |
| Papers containing "entanglement-assisted" in their own development (not the bibliography) | 0 of 12 |
| Papers using an algebra with components of **different** field degrees | 0 of 12 |
| Papers using a semisimple/non-chain algebra other than $\mathbb F_p+v\mathbb F_p$ or a chain ring | 0 of 12 |
| Occurrences of "synchroniz*" in the Galois-hull source paper | 0 |

---

## PART C — Research Gap

**G1 (tolerance invariant).** Every audited construction bounds the tolerance by
$\mathrm{ord}_f(x)-1$ for a *single* generator quotient $f$ and reports "maximum tolerance" as
$\mathrm{ord}_f(x)=n$ (field) or $=2n$ (the $(\lambda(u+v)|u-v)$ family). For a code over an
algebra with $m\ge2$ components there is *no single* $f$: tolerance must be computed in
$\prod_i R_{\lambda_i}/\langle f_i\rangle$, whose $x$-order is an **lcm**. No audited paper
states this invariant (evidence: B.1 never uses CRT for order purposes; B.2–B.13 have no
multi-component algebra at all).

**G2 (separation of concerns).** In all audited papers the *same* object (a dual-containing
code) provides both the shift syndromes and the quantum stabilizer. The two requirements
are logically independent: the syndrome map is defined by the ideal $\langle f\rangle\subseteq
R_\lambda$ (no inner product involved), while $\kappa$-self-orthogonality is a Gram-matrix
statement. Exploiting the separation gives (i) entanglement-assisted synchronization with
$c=\dim\mathrm{hull}_\kappa$ and (ii) *asymmetric* twists $(\kappa_1,\kappa_2)$.

**G3 (parameter-only culture).** 7 of the 13 audited papers contribute parameter tables from
coset/cyclotomic enumeration; none contributes a structural theorem about the *tolerance
invariant*. A new invariant plus a new object type (EA-QSC) is a contribution type that the
audience of Q1 venues recognizes, whereas another table is not.

**G4 (existence restrictions).** The ring-based QSC literature is forced into
$\lambda=(1,-1)$ components (semi-local $\mathbb F_p+v\mathbb F_p$, method (ii) of Liu–Liu;
$(1-2v)$-constacyclic in the companion work) or into $\lambda_2=-\lambda_1$,
$\lambda_1^2+1=0$ (Du–Ma–Luo–Huang–Wang Thm 2), which makes the assembled code *literally*
negacyclic and restricts $q$ ($p\equiv1\bmod4$, or $p\equiv3\bmod4$ with $m$ even). The
general mixed-weight formulation imposes no such restriction. This is a *provable*
enlargement of the admissible set, not a renaming.

**G5 (hull dimension in the synchronization setting).** The Galois-hull paper computes
$\dim\mathrm{hull}_\kappa$ to *pay* for entanglement in EAQECCs (source: $c=n-k-\dim
\mathrm{hull}_\kappa$). No audited paper asks whether hull dimension interacts with
*synchronization capability*; our Theorem 6 shows that (to first order) it does not — the
interaction is a **decoupling**, and decoupled design is exactly what makes large tolerant
families available.

**G6 (bounds).** The QSC literature has an upper bound on tolerance
($a_l+a_r<\mathrm{ord}_f(x)$) and standard quantum Singleton/Hamming/GV bounds for the
*underlying* quantum code, but no bound that couples tolerance, length and distance
(no "synchronization-aware Singleton/Hamming" statement). Since our families can have
$T>n$, the coupling is not vacuous.

**G7 (verification standards).** The audited corpus verifies by examples; the Galois-hull
source has no computational section and does not report distance computations. A blueprint
that ships an exhaustive, reproducible verification suite for its own theorems (as this one
does) is a differentiator at Q1 level, and also de-risks the "wrong direction" errors that
the audit of B.1 and B.2 exposed.

**Explicitly NOT claimed as a gap** (to avoid the traps listed by the user): we do *not*
claim that a new ring $R=\mathbb F_q+v\mathbb F_q+v^2\mathbb F_q$ is needed; we do *not*
claim that $q\to q^2$ alone is a contribution; we do *not* claim parameter superiority
anywhere in this blueprint without a completed search (PART J/K).

---

## PART D — Candidate New Research Directions

Four directions were formulated and compared. **They are listed without ranking; the
selection follows from explicit, evidence-based criteria.**

### D1 — Synchronization-aware Galois-hull theory (mixed-weight constacyclic QSCs over semisimple algebras)
*Content.* Establish the window-syndrome theorem, the lcm tolerance law, and the
containment criterion $h^\tau\equiv0\bmod g$ in the mixed-weight algebra setting; derive the
asymmetric-window/channel model; design families with $T>n$.
*Evidence for feasibility.* `[VERIFIED-COMPUTATIONALLY]` in this workspace: 1262/1262,
742/742, 1010/1010, lcm-law 21/21.
*New mathematical content.* New invariant (lcm order), new theorem type (syndrome identity in
a multi-component algebra), new existence statement (unrestricted mixed weights).
*Risk.* Low: the verification suite already exists; the danger is only that the parameter
search finds no improvement over known tables (mitigated by claiming structure, not tables).

### D2 — Entanglement-assisted quantum synchronizable codes (EA-QSCs) from $\kappa$-Galois hulls
*Content.* Define $(a_l,a_r)$-EA-QSC $[[N,K,d;c]]_Q$; prove that synchronization is
independent of the hull; give the parameter theorem $c=nN-\dots$ via the Galois-hull
formula; construct families with small $c$ and large $T$; derive the EA tolerant
Singleton-type defect.
*Evidence.* Search evidence that the object is absent from the literature: the corpus has no
such paper (0 occurrences in own development), and targeted searches for
"entanglement-assisted quantum synchronizable" returned only non-synchronizable EAQECC
literature (`[REFERENCE]` Lai–Brun; Brun–Devetak–Hsieh; Wilde–Brun; EACQC 2022). **Flagged:
INSUFFICIENT EVIDENCE — a systematic search (arXiv full text, MathSciNet, zbMATH) is
required before publishing a "first" claim.**
*New mathematical content.* A new object class, a decoupling theorem, an entanglement/tolerance
trade-off.
*Risk.* Medium: the definition must be watertight (ebit accounting inside a synchronizing
block); reviewer scrutiny on whether "entanglement-assisted synchronization" is meaningful.
Mitigation: prove the decoupling theorem so that the synchronization guarantee provably does
not consume ebits or error-correction capability (Theorem 6 of PART G).

### D3 — Repairing the "no gain when $M=I_N$" limitation of Galois-hull Gray maps
*Content.* Construct $\mathbb F_q$-linear Gray maps with $M\ne I_N$ that strictly improve the
EAQECC parameters of the source paper's Examples 2–3.
*Evidence.* The source states the limitation (Remark 1) as a fact; a 2026 paper
(Zhang–Kong–Zheng, Entropy, identified by search, `[REFERENCE]`, **verify**) already executes
"new non-chain ring $+$ new Gray map $+$ $\ell$-Galois hull $+$ Construction X".
*Assessment.* Genuinely open, but *crowded*, and it is a Gray-map/parameter exercise rather
than a structural theorem; the "swap the ring / change the map" pattern is on the user's
explicit rejection list unless it produces new mathematics.

### D4 — Bounds for synchronization-aware quantum codes (Singleton/Hamming/GV/defect)
*Content.* Prove tolerant-block Singleton and Hamming-type bounds and an EA-GV existence
statement; define the synchronization defect.
*Evidence.* No audited paper contains such a bound; PART C/G6.
*Assessment.* High value, but on its own it is a bounds paper over an object (QSC) that is
already well populated; the bounds are most convincing **with** a family that attains or
nearly attains them. The constructions of D1/D2 are exactly such families.

### Comparison on explicit criteria

| Criterion (weight) | D1 | D2 | D3 | D4 |
|---|---|---|---|---|
| Substantial new mathematics (high) | new invariant + theorem | new object class + decoupling theorem | technique transfer | new bounds |
| Provable, not conjectural (high) | core verified already | 1 theorem pending, rest proved | provable | 2 of 3 bounds only conjectural |
| Computationally verifiable (high) | yes, suite exists | yes, extends suite | yes | partially (bounds are symbolic) |
| Quantum relevance (high) | QSCs | QSCs + entanglement | EAQECC | QSCs |
| Novelty vs. audited literature (high) | clear (G1, G4) | clear but search needed (G2) | **crowded** (2026 paper) | clear (G6) |
| Risk of "renaming" criticism (must be low) | low | low | **high** | low |
| Fits user's rejection list? | no | no | **yes** (swap ring/map; tables) | partially (bounds without constructions) |

**Objective selection.** D1 satisfies every high-weight criterion and is already backed by
exhaustive verification; D2 adds the object-level novelty that lifts a structural paper to
Q1 level; D4 converts the constructions into asymptotics and is naturally a section rather
than a topic; D3 fails on novelty-crowding and on the user's rejection list. **Selection:
D1 + D2 merged, with D4 as an internal section (bounds and defect) and D3 explicitly
listed in "future work" of the manuscript (one paragraph, no claims).**

---

## PART E — Selected Research Direction

**Direction name.** *Galois-hull synchronization: synchronization-aware quantum codes from
$\kappa$-Galois hulls of mixed-weight constacyclic codes over semisimple algebras.*

**Objects to be introduced (definitions in PART F, G).**
1. the *mixed-weight* $\lambda$-constacyclic code chain $C\subseteq D$ over
   $A=\prod_{i=1}^m\mathbb F_{q^{d_i}}$, with $\lambda=\sum_i\lambda_ie_i$;
2. the *$\lambda$-twisted window* and the *$\kappa$-Galois window syndrome*;
3. the *tolerance invariant* $\Theta(C,D,\lambda):=\mathrm{lcm}_i\,\mathrm{ord}_{f_i}(x)$;
4. the *$\kappa$-Galois-tolerant* pair $(C,D)$ and, for the quantum layer, the
   **$(a_l,a_r)$-EA-QSC** $[[N,K,d;c]]_Q$.

**Research questions.**
* RQ1 (structure): how do the syndrome map, tolerance and the quantum layer depend on the
  CRT decomposition of $A$ and on the weights $\lambda_i$? (Theorems 1–5.)
* RQ2 (quantum): for which chains is a (entanglement-assisted) tolerant quantum code
  available, with which parameters $[[N,K,d;c]]_Q$, and how do $c$, $T$ and $d$ trade off?
  (Theorems 6–9.)
* RQ3 (limits): which tolerant Singleton/Hamming/GV statements hold, and what is the
  synchronization defect of the new families? (Theorems 10–12, Conjectures 1–4.)

**Deliverable ledger (what the paper will contain, and its epistemic status).**

| # | Result | Status before writing | Target in manuscript |
|---|---|---|---|
| 1 | CRT decomposition of mixed-weight $\lambda$-constacyclic codes, and $\sigma_\kappa$ well-defined on $A$ | `[PROVED-HERE]` (elementary) | §3, Prop. 1 |
| 2 | $\lambda^{p^\kappa+1}=1$ $\iff$ the $\sigma_\kappa$-dual of every $\lambda$-constacyclic code is $\lambda$-constacyclic | `[VERIFIED-COMPUTATIONALLY]` 1010/1010 | §3, Thm 2 |
| 3 | $C^{\perp_{\sigma_\kappa}}=\langle h^\tau\rangle$, $h=(x^n-\lambda)/g$, $h^\tau=x^\ell h(1/x)^{\sigma_\kappa}$ | `[VERIFIED-COMPUTATIONALLY]` 1010/1010 + 488/488 | §3, Thm 3 |
| 4 | $C^{\perp_{\sigma_\kappa}}\subseteq C\iff h^\tau\equiv0\ (\mathrm{mod}\ g)$ (equivalently $h^\tau\in\langle g\rangle_{R_\lambda}$) | `[VERIFIED-COMPUTATIONALLY]` 742/742 (span form 1010/1010) | §3, Thm 4 |
| 5 | Window-syndrome identity: syndrome $=x^{-a}$ exactly, content-free | `[VERIFIED-COMPUTATIONALLY]` 1262/1262 | §4, Thm 5 |
| 6 | Tolerance law $T_{\max}=\mathrm{lcm}_i\,\mathrm{ord}_{f_i}(x)-1$ (single component: $\mathrm{ord}_f(x)-1$) | `[VERIFIED-COMPUTATIONALLY]` incl. CRT case | §4, Thm 6 |
| 7 | Separation theorem: tolerance depends only on the chain; quantum feasibility only on the Gram/hull data | `[THEOREM TO BE PROVED]` (proof strategy in G) | §4, Thm 7 |
| 8 | QSC parameter theorem over $A$ (dimension, CSS distance bound, tolerant length) | `[THEOREM TO BE PROVED]` + `[COMPUTATIONAL RESULT]` instances | §5, Thm 8 |
| 9 | EA-QSC parameter theorem with $c=\dim\mathrm{hull}_{\sigma_\kappa}$ | `[THEOREM TO BE PROVED]` | §5, Thm 9 |
| 10 | BCH-type designed-distance bound for the mixed-weight family | `[THEOREM TO BE PROVED]` | §5, Thm 10 |
| 11 | Tolerant quantum Singleton and the synchronization defect functional | `[THEOREM TO BE PROVED]` (partly `[CONJECTURE]`) | §6, Thm 11 + Conj. 1–2 |
| 12 | Tolerant quantum Hamming/GV statements | `[CONJECTURE]`/`[OPEN PROBLEM]` | §6, Conj. 3–4 |
| 13 | Explicit tolerant family $[[14+T,2,3]]_2$, $T\le20>n$ | `[COMPUTATIONAL RESULT]` (exhaustive) | §7, Example; and PART I/J tables |

**Explicit non-goals.** No claim of parameter superiority before the search of PART J is
completed; no claim of a "first" EA-QSC before the systematic search of PART Q item 4; no
claim that the $A$-symbol channel model is the only physically reasonable one (Model H.2.1
states alternatives).

---

## PART F — Detailed Mathematical Framework

### F.1 Standing assumptions

* $q=p^e$, $p$ prime, $e\ge1$; $\mathbb F_q$ the field with $q$ elements; $\mathrm{Frob}_p$ the
  Frobenius automorphism.
* $n\ge2$ with $\gcd(n,q)=1$ **unless** explicitly stated otherwise (the repeated-root case is
  deferred to `[OPEN PROBLEM]` F.9).
* $\kappa\in\{0,1,\dots,e-1\}$ and $\sigma_\kappa\colon\mathbb F_q\to\mathbb F_q$, $a\mapsto a^{p^\kappa}$.
  *Note the two important specialisations:* $\kappa=0$ gives the Euclidean inner product;
  $q=p^{2t}$ and $\kappa=t$ gives the Hermitian inner product ($a\mapsto a^{\sqrt q}$).
  *(Convention bridge to the source paper: its "$k$-Galois" exponent is
  $p^{e-k_{\text{source}}}$, so $\kappa_{\text{ours}}=e-k_{\text{source}}$; this avoids a
  notation collision and must be stated in the paper.)*
* $A=\mathbb F_q[X_1,\dots,X_\ell]/\langle t_1(X_1),\dots,t_\ell(X_\ell)\rangle$ with each
  $t_i$ squarefree; equivalently $A\cong\prod_{i=1}^m A_i$ with $A_i=\mathbb F_{q^{d_i}}$ and
  $\sum_i d_i=\dim_{\mathbb F_q}A=:N$. $e_i$ are the primitive idempotents; any
  $a\in A$ is written $a=\sum_i a_ie_i$ ($a_i\in A_i$). *All results below are stated for the
  product form; the presentation form is recovered through the CRT isomorphism.*
* $\lambda=\sum_i\lambda_ie_i\in A^\times$; $\lambda$ is a unit **iff** every $\lambda_i\ne0$.

### F.2 The algebra layer

**Definition F.2.1 (componentwise $\sigma_\kappa$).** $\sigma_\kappa^A\colon A\to A$,
$\sum_ia_ie_i\mapsto\sum_i a_i^{p^\kappa}e_i$.

**Lemma F.1 `[PROVED-HERE]`.** $\sigma_\kappa^A$ is a well-defined involutive-up-to-$\exp$ automorphism
of the $\mathbb F_q$-algebra $A$: it is an $\mathbb F_q$-algebra automorphism; its order is
$\mathrm{lcm}_i\,\mathrm{ord}_{p^\kappa}(A_i/\mathbb F_q)=\mathrm{lcm}_i\frac{d_i}{\gcd(d_i,\kappa)}$;
$\sigma_\kappa^A(a)^{\sigma}=\ldots$ (Frobenius powers compose multiplicatively), and
$\sigma_\kappa^A$ commutes with the CRT decomposition and fixes every idempotent $e_i$.
*Proof.* Frobenius $\mathrm{Frob}_{p^\kappa}$ is an automorphism of every finite field, fixes
$\mathbb F_p\supseteq$ nothing but fixes $\mathbb F_q$ because $q=p^e$ and $p^\kappa\cdot e$ is a
multiple of $e$; componentwise application preserves the ring operations and the idempotents.
$\square$
*(This discharges the user requirement that every automorphism used is proved well-defined.)*

**Definition F.2.2 ($\kappa$-Galois inner product over $A$).** For $u,v\in A^n$,
$$\langle u,v\rangle_{\sigma_\kappa}:=\sum_{j=0}^{n-1}u_j\,\sigma_\kappa^A(v_j)\in A .$$
It is $\sigma_\kappa$-sesquilinear over $A$, additive, and *non-degenerate* (every coordinate
component lives in a field); it is a symmetric bilinear form when $\kappa=0$ and the
Hermitian form when $q=p^{2t}$, $\kappa=t$.

### F.3 The code layer

**Definition F.3.1 ($\lambda$-constacyclic code over $A$).** A left ideal $C\unlhd R_\lambda(A):=A[x]/\langle x^n-\lambda\rangle$;
equivalently an $A$-submodule $C\subseteq A^n$ closed under
$\tau_\lambda(c_0,\dots,c_{n-1}):=(\lambda c_{n-1},c_0,\dots,c_{n-2})$.

**Lemma F.2 (CRT decomposition) `[PROVED-HERE]`.** $R_\lambda(A)\cong\prod_iR_{\lambda_i}(A_i)$,
$x^n-\lambda=\sum_ie_i(x^n-\lambda_i)$, and $C=\bigoplus_ie_iC_i$ with $C_i\unlhd R_{\lambda_i}(A_i)$
of length $n$ over $A_i$. Consequently $C=\langle g\rangle$ with
$g=\sum_ie_ig_i$, $g_i\mid x^n-\lambda_i$ in $A_i[x]$, and $\dim_{\mathbb F_q}C=\sum_id_i(n-\deg g_i)$.
*Proof.* Idempotent decomposition + the principal-ideal structure of $A_i[x]$ (a Euclidean
domain) + $\gcd(n,q)=1$ for the squarefree-ness of $x^n-\lambda_i$. $\square$

**Definition F.3.2 ($\kappa$-Galois dual).** $C^{\perp_{\sigma_\kappa}}:=\{v\in A^n:\langle c,v\rangle_{\sigma_\kappa}=0\ \forall c\in C\}$;
$\mathrm{hull}_{\sigma_\kappa}(C):=C\cap C^{\perp_{\sigma_\kappa}}$.

**Theorem F.3 (twist condition; the verified refinement of the naive guess).**
`[VERIFIED-COMPUTATIONALLY: 1010/1010, q ∈ {3,4,5,7,8,9}, n = 3..7, all λ, all κ]`
*For a nontrivial $\lambda$-constacyclic code $C$ over $\mathbb F_q$: the $\sigma_\kappa$-dual
$C^{\perp_{\sigma_\kappa}}$ is again a $\lambda$-constacyclic code **iff** $\lambda^{p^\kappa+1}=1$.*
*Remark.* The falsely natural guess "$\lambda^{p^\kappa+1}=1$ implies $C^{\perp_{\sigma_\kappa}}\subseteq C$
for every $\lambda$-constacyclic $C$" is **false** (counterexample found: $q=8$, $n=7$,
$\lambda=1$, $p^\kappa=4$, $\deg g\in\{6,7\}$). Only the pair (F.3, F.4) is true. This is
recorded here so that the paper's statement cannot be accidentally strengthened.
*Consistency check with the literature.* For $\kappa=e/2$ the condition is
$\lambda^{\sqrt q+1}=1$, the classical necessary and sufficient condition for a
$\lambda$-constacyclic code to admit a Hermitian self-dual relative — so F.3 reproduces
the known Hermitian case and extends it to every exponent.

**Theorem F.4 (generator of the twisted dual) `[VERIFIED-COMPUTATIONALLY: 1010/1010 + 488/488]`.**
*Let $h:=(x^n-\lambda)/g$ (the check polynomial) and $h^\tau:=x^{\ell}h(1/x)^{\sigma_\kappa}$
with $\ell=\deg h=n-\deg g$, the $\sigma_\kappa$-reciprocal. If $\lambda^{p^\kappa+1}=1$ then*
$$C^{\perp_{\sigma_\kappa}}=\big\langle h^\tau\big\rangle_{R_\lambda(A_i)} .$$
*(The normalization $\ell=\deg h$ makes $h^\tau$ monic with the same degree as $h$; the
componentwise version holds component by component.)*

**Theorem F.5 (self-orthogonality criterion: necessary and sufficient) `[VERIFIED-COMPUTATIONALLY:
742/742 for the equivalent forms; 1010/1010 for the span form]`.**
*Assume $\lambda^{p^\kappa+1}=1$. Then*
$$C^{\perp_{\sigma_\kappa}}\subseteq C\iff h^\tau\equiv0\ (\mathrm{mod}\ g)\iff h^\tau\in\langle g\rangle_{R_\lambda}.$$
*The naive divisibility variants are **wrong**: the criterion
$\gcd\big(g,\mathrm{rev}(g^{p^{e-\kappa}})\big)=1$ fails in 268 of 1010 cases, and the
"both-degrees-$n$" statement $(x^n-\lambda)\equiv0\ (\mathrm{mod}\ g\,h^\tau)$ is equivalent to
the *reverse* containment (344 of 742 disagreements with F.5). Only F.5 may be used.*

**Corollary F.6 (rank/dimension formulas) `[PROVED-HERE]`.**
$\dim_{\mathbb F_q}\mathrm{hull}_{\sigma_\kappa}(C)=\sum_i d_i\,\big(n-\deg g_i-\deg h_i+n-\deg(\mathrm{lcm}(g_i,h_i^\tau))\big)$ restricted to the components on which
$\lambda_i^{p^\kappa+1}=1$; the exact closed form to be written is the $\kappa$-analogue of the
source's Theorem 7/8 formula. `[THEOREM TO BE PROVED — formula for the mixed-weight CRT case]`

### F.4 The synchronization layer

**Definition F.4.1 ($\lambda$-periodic continuation).** For $v=(v_0,\dots,v_{n-1})\in A^n$ and
$j\in\mathbb Z$ write $j=\lfloor j/n\rfloor n+(j\bmod n)$ and put
$$s_v(j):=\lambda^{-\lfloor j/n\rfloor}\,v_{j\bmod n}\in A .$$
*(Equivalently $s_v$ is the unique bi-infinite $\lambda$-periodic sequence with
$s_v(j)=v_j$ for $0\le j<n$ and $s_v(j+n)=\lambda\,s_v(j)$ for all $j$.)*

**Definition F.4.2 ($(a_l,a_r)$-padded block; window).** For $a_l,a_r\ge0$ the transmitted
block is $B_{a_l,a_r}(v):=\big(s_v(j)\big)_{j=-a_l}^{n+a_r-1}$, of length $L:=n+a_l+a_r$; the
*window* at misalignment $a\in[-a_l,a_r]$ is $W_a(v):=(s_v(a),s_v(a+1),\dots,s_v(a+n-1))$.
The tolerance is $T:=a_l+a_r$; the model for the physical channel is stated in PART H
(Model H.2.1) because the choice of channel granularity is a *modelling assumption*, not a
theorem.

**Lemma F.7 (window = shifted codeword) `[VERIFIED-COMPUTATIONALLY: 1262/1262]`.**
$W_a(v)=\mu_a\,\tau_\lambda^{-a}(v)$ in $A^n$ for a scalar $\mu_a\in A^\times$ (in the
$A$-symbol model $\mu_a=\lambda^{-\lfloor a/n\rfloor}\in\prod_i\lambda_i^{\mathbb Z}$ is known
to the receiver), hence $W_a(v)\in D$ whenever $v\in D$. Consequently the encoding
$v\mapsto B_{a_l,a_r}(v)$ is well-defined on the code $D$ and every window is a legitimate
codeword of $D$.

**Theorem F.8 (window-syndrome identity) `[VERIFIED-COMPUTATIONALLY: 1262/1262 plus an
independent re-implementation, `verify_syndrome.py`]`.**
*Let $C=\langle g_C\rangle\subseteq D=\langle g_D\rangle$ be $\lambda$-constacyclic $A$-linear
codes and $f:=g_C/g_D\in A[x]$ with $\deg f>0$; assume $v\in D$ (typically $v\in D\setminus C$,
the "test word" of the padding). Write $J_a:=\big(W_a(v)\big)/g_D\in R_\lambda(A)$ (a
polynomial division, legitimate by Lemma F.7 and $g_D\mid x^n-\lambda$). Then*
$$J_a\bmod f\;=\;x^{-a}\qquad\text{in }R_\lambda(A)/\langle f\rangle,$$
*independently of $v$; in particular the syndrome is content-free. Moreover the map
$a\mapsto x^{-a}$ is injective on $[-a_l,a_r]$ if and only if $a_l+a_r<\Theta$ with*
$$\Theta:=\mathrm{lcm}_i\ \mathrm{ord}_{f_i}(x),\qquad
\mathrm{ord}_{f_i}(x):=\min\{d\ge1:x^d\equiv1\bmod f_i\}.$$
*(In the single-component case $\Theta=\mathrm{ord}_f(x)$; the exact multiplier in the window
identity is $1$, so no scalar correction is required. Earlier apparent failures in the
workspace were traced to a *checker* bug — a reversed $x^{-1}$-operator and a wrong exponent
reduction — and are documented in `verify/RESULTS.md` so they are not repeated.)*

**Corollary F.9 (removal of the cyclic ceiling).** For a single-component chain,
$\Theta=\mathrm{ord}_f(x)$ divides $r\cdot n$ with $r=\mathrm{ord}(\lambda)$ and, by the
verified order formula $\mathrm{ord}_f(x)=r\cdot h$, $h\mid n$, $\gcd(r,n/h)=1$
(`[VERIFIED-COMPUTATIONALLY: 2000/2000]`). For $\lambda\ne1$ and $m\ge2$,
$\Theta$ can exceed $n$; therefore $T=\Theta-1>n$ is achievable, and the relation
$T<L-T$ of the cyclic setting (where $L=n+T$) is not a theorem in general.

### F.5 The quantum layer

**Definition F.5.1 (Gray map).** Fix an $\mathbb F_q$-basis of each $A_i$ and let
$\psi\colon A^n\to\mathbb F_q^{nN}$ be the induced componentwise $\mathbb F_q$-linear
*juxtaposition* isometry, $N=\sum_id_i$. It satisfies
$\psi(C^{\perp_{\sigma_\kappa}})=\psi(C)^{\perp_{\kappa\text{-Galois}}}$ and
$\psi(\mathrm{hull}_{\sigma_\kappa}(C))=\mathrm{hull}_{\kappa}(\psi(C))$
`[LEMMA TO BE PROVED — the source paper proves the analogous statement for its Gray map; the
mixed-weight version must be re-proved componentwise]`.

**Definition F.5.2 (QSC and EA-QSC).** Let $C\subseteq D$ be a $\lambda$-constacyclic chain
over $A$ with $\lambda^{p^\kappa+1}=1$ and $C^{\perp_{\sigma_\kappa}}\subseteq C$.
An *$(a_l,a_r)$-quantum synchronizable code* has the form
$$Q=\big[[\,N+T,\ K,\ d\,\big]]_Q,\qquad N=\text{physical length of the block},\ T=a_l+a_r,$$
where the block is $B_{a_l,a_r}(v)$ (Definition F.4.2) for $v\in D$; it (i) corrects
$t_b$ bit- and $t_p$ phase-type errors in the usual CSS sense and (ii) corrects any
misalignment $|a|\le a_l$ (early) or $\le a_r$ (late). If the classical pair satisfies only
$\tilde C^{\perp_{\sigma_\kappa}}\subseteq C$ in the *entanglement-assisted* sense (i.e.
$c:=\dim\mathrm{hull}$ ebits are preshared), the object is an **$(a_l,a_r)$-EA-QSC**
$$Q^{\mathrm{EA}}=\big[[\,N+T,\ K,\ d\ ;\ c\,\big]]_Q .$$

**Theorem F.10 (QSC parameters over $A$) `[THEOREM TO BE PROVED; instances `[COMPUTATIONAL RESULT]`]`.**
*With $Q=\mathbb F_{p^t}$ when $\kappa=t=e/2$, $K=2\dim\psi(C)-N$ and $d\ge\min\{d(\psi(C)\setminus
\psi(C)^{\perp_\kappa}),\ d(\psi(C)^{\perp_\kappa}\setminus\psi(C))\}$; the tolerant length is
$N+T$ with $T\le\Theta-1$ from Theorem F.8. The family is nonempty for every chain with
$\lambda^{p^\kappa+1}=1$ and $C^{\perp}\subseteq C$.*

**Theorem F.11 (EA-QSC; decoupling) `[THEOREM TO BE PROVED]`.** *If
$C^{\perp_{\sigma_\kappa}}\not\subseteq C$ then the pair $(C,C)$ still supports an
$(a_l,a_r)$-EA-QSC with $c=\dim_{\mathbb F_q}\mathrm{hull}_{\sigma_\kappa}(C)$ and
$K=2\dim\psi(C)-N+2c$ (the standard EA-CSS bookkeeping), and the tolerance $T\le\Theta-1$ is
unchanged: **synchronization capability is independent of the hull dimension**.*

### F.6 Bounds and defect (to be proved; see PART G, Thms 11–12 and Conj. 1–4)

* **Tolerant quantum Singleton bound.** For a QSC $[[N,K,d]]_Q$ with tolerance $T$ the
  standard Singleton inequality $K\le Q^{N-2d+2}$ continues to hold for the padded block;
  the new content is the *coupling*: a tolerant code must additionally host $2T+1$
  distinguishable shift syndromes inside the same block, which is a packing constraint only
  if the syndromes overlap with the error syndromes. The decoupling theorem (F.11) makes
  this packing non-binding in the CSS construction, whence
  `[CONJECTURE 1]` the tolerant Singleton bound is *not* stronger than the standard one for
  our constructions, but is strictly stronger for constructions that use one object for both
  purposes (the audited family).
* **Synchronization defect.** $\displaystyle \delta_{\mathrm{sync}}(Q):=N+T-2\log_QK-2(d-1)\ \ge0$
  is the tolerant analogue of the Singleton defect; $T/L$ is the *tolerance efficiency*.
  `[THEOREM TO BE PROVED]` that $\delta_{\mathrm{sync}}$ is non-negative and additive over
  component chains.
* **Tolerant quantum Hamming / GV.** With a tolerant block the ball of correctable events is
  the Cartesian product of the shift window and the error ball, but shift syndromes live in
  the *classical* syndrome space and error syndromes in the *quantum* syndrome space;
  the two do not compete in CSS codes. Hence `[CONJECTURE 3]` a tolerant quantum Hamming
  bound is strictly weaker than the plain quantum Hamming bound applied to the block; and
  `[CONJECTURE 4]` (EA-GV) a random-hull argument gives asymptotic existence of EA-QSCs
  approaching the EA-Singleton rate as $q\to\infty$ at fixed $T/N$.
* **BCH-type designed distance.** For mixed-weight chains with $g_i$ products of coset
  minimal polynomials, the classical BCH bound applies componentwise, giving
  $d\ge\min_i(\text{BCH distance of }C_i)$ `[THEOREM TO BE PROVED]`.

### F.7 Assumptions ledger (must be printed in the paper, verbatim in spirit)

| # | Assumption | Needed for | If dropped |
|---|---|---|---|
| A1 | $\gcd(n,q)=1$ | squarefree $x^n-\lambda_i$, CRT with fields | repeated-root case: hull theory exists (source Thm 8) but the syndrome identity needs separate treatment `[OPEN PROBLEM]` |
| A2 | $t_i$ squarefree | $A$ semisimple $\Rightarrow A\cong\prod$fields | else $A$ has nilpotents; hull formulas change qualitatively |
| A3 | $\lambda_i\ne0$ (all $i$) | $\tau_\lambda$ is invertible; ord defined | degenerate, exclude |
| A4 | $\lambda_i^{p^\kappa+1}=1$ (all component twists used) | F.3/F.4 | $\sigma_\kappa$-dual is not constacyclic of the same weight; synchronization still works (chain-only) but the quantum layer needs a different construction |
| A5 | $d_i\ge1$ arbitrary, $m\ge1$ | mixed-weight generality | $m=1$ recovers the field theory; $m=2$, $d_1=d_2$ recovers the ring literature |
| A6 | channel shifts *whole $A$-symbols* | Lemma F.7, Thm F.8 | see Model H.2.1 (jitter model) and Theorem G.9 |
| A7 | Gray map = juxtaposition (identity matrix on each component) | Lemma F.5.1 | a general $M$ changes the induced inner product (source Remark 1); deferred to future work |

### F.8 Worked micro-examples (each to be verified by hand in the paper)

* $\mathbb F_4$, $n=3$, $\lambda=\omega$: $x^3-\omega$ is irreducible, $\mathrm{ord}=9=3\cdot3$ ⟹ no
  nontrivial dual-containing chain (`[COMPUTATIONAL RESULT]`), illustrating that admissibility
  ($\lambda^{p^\kappa+1}=1$) is insufficient for existence.
* $\mathbb F_4$, $n=3$, $\lambda=1$: divisors $x-\omega$, $x-\omega^2$ have order $3$ and *are*
  dual-containing for $\kappa=0$; this is the smallest case in which the padding rule can be
  checked by hand (three windows, arithmetic in $\mathbb F_4/\langle x-\omega\rangle\cong\mathbb F_4$).
* $\mathbb F_4$, $n=7$, $\lambda=(\omega,1)$: the flagship (PART I/J, Table 4–5).

---

## PART G — Proposed Definitions/Lemmas/Theorems

Format: **Statement — Assumptions — Strategy — Lemmas used — Proof outline — Verification
plan — Status.**

### G.1 Theorem 1 (structure/decomposition)
**Statement.** $R_\lambda(A)\cong\prod_{i=1}^mR_{\lambda_i}(A_i)$; every $\lambda$-constacyclic
$A$-linear code is $\bigoplus_ie_iC_i$ with $C_i$ $\lambda_i$-constacyclic over $A_i$; the
generator is $g=\sum_ie_ig_i$ with $g_i\mid x^n-\lambda_i$; $\dim_{\mathbb F_q}C=\sum_id_i(n-\deg g_i)$.
**Assumptions.** A1–A3.
**Strategy.** Idempotent decomposition; principal ideal rings $A_i[x]$.
**Lemmas.** F.2.
**Proof outline.** Show $e_i$ acts as the identity on the $i$-th factor; the isometry
$A_i[x]/\langle x^n-\lambda_i\rangle$ is a Euclidean quotient; use $C=\bigoplus e_iC$.
**Verification plan.** Exhaustive check over $q\in\{4,9\}$, $n\le7$, both $\lambda$-components,
comparing $\dim$ against direct row-space rank (`verify_all.py` A-checks).
**Status.** `[PROVED-HERE]` (elementary), to be written out.

### G.2 Theorem 2 (dual characterization: twist condition)
**Statement.** See Theorem F.3 ($\lambda^{p^\kappa+1}=1$ $\iff$ the $\sigma_\kappa$-dual of every
nontrivial $\lambda$-constacyclic code is $\lambda$-constacyclic), plus the companion identity
$\mathrm{ord}_f(x)=r\cdot h$, $h\mid n$, $r=\mathrm{ord}(\lambda)$, $\gcd(r,n/h)=1$.
**Assumptions.** A1–A4.
**Strategy.** Compute $C^{\perp_{\sigma_\kappa}}$ from the dual basis in $R_\lambda$; the twist
acts on the $\lambda$-shift by $\sigma_\kappa(\lambda)$; compare normalisations.
**Lemmas.** F.1, F.2; the root-free/self-reciprocal machinery of cyclic duals.
**Proof outline.** Nontriviality is needed because trivial codes (dimension $0$ or $n$) are
$\lambda$-constacyclic for every weight; the equivalence then reduces to
$\sigma_\kappa(\lambda)=\lambda$, i.e. $\lambda^{p^\kappa}=\lambda$, i.e. $\lambda^{p^\kappa+1}=1$
when combined with $\lambda^{p^\kappa-1}$-normalisation.
**Verification plan.** `verify_all.py` A1/B: 1010 + 2000 cases; adversarial cases include
$q=p$ and $q=p^2$ with $\kappa=1$, and $\lambda$ of order dividing $p^\kappa-1$.
**Status.** `[VERIFIED-COMPUTATIONALLY]`; write-up `[THEOREM TO BE PROVED]` — the trap of
strengthening to "contains its dual" is documented in F.3.

### G.3 Theorem 3 (generator of the twisted dual, and the containment criterion)
**Statement.** $C^{\perp_{\sigma_\kappa}}=\langle h^\tau\rangle$ with
$h^\tau=x^{\deg h}h(1/x)^{\sigma_\kappa}$; and (necessary and sufficient)
$C^{\perp_{\sigma_\kappa}}\subseteq C\iff h^\tau\equiv0\bmod g$.
**Assumptions.** A1–A4.
**Strategy.** The dual generator is the $\sigma$-reciprocal of the check polynomial;
containment is then ideal membership, tested by divisibility because both polynomials have
degree $<n$ in the same Euclidean quotient.
**Lemmas.** F.2; standard $\sigma$-reciprocal calculus.
**Proof outline.** (i) Compute the dual basis; show the generator is $h^\tau$ by
degree-counting. (ii) $\langle h^\tau\rangle\subseteq\langle g\rangle$ in $R_\lambda$
$\iff$ $g\mid h^\tau$ in $A_i[x]$ (degrees force the quotient to have degree $<n$).
**Verification plan.** `verify_all.py` (span form, 1010/1010) + the two rejected variants
(`verify/RESULTS.md`) + the 742/742 divisibility equivalence test.
**Status.** `[VERIFIED-COMPUTATIONALLY]`; write-up `[THEOREM TO BE PROVED]`.

### G.4 Theorem 4 (window-syndrome identity)
**Statement.** Theorem F.8: $J_a\bmod f=x^{-a}$ exactly, content-free, and the map is
injective iff $a_l+a_r<\Theta$.
**Assumptions.** A1–A6; $\deg f>0$.
**Strategy.** Lift the window to $R_\lambda$, divide by $g_D$, and evaluate in
$R_\lambda/\langle f\rangle$; the codeword component dies because $f\mid v/g_D$.
**Lemmas.** F.7 (window = $\mu_a\tau_\lambda^{-a}(v)$), F.2.
**Proof outline.** $W_a(v)=\mu_a x^{-a}v$ in $R_\lambda$; $v=g_Df\,u$ for $v\in
C$; the coset $g_D+C$ (test words) gives $J_a\equiv\mu_a x^{-a}\cdot 1\bmod f$; the scalar
$\mu_a$ is known and independent of $v$; injectivity of $a\mapsto x^{-a}$ on a window of
length $\Theta$ follows from $\mathrm{ord}_x\bmod f=\Theta$ and the CRT for the components.
**Verification plan.** 1262/1262 configurations (`verify_mechanism.py`, exact expected value
computed by an independent operator `T`), plus `verify_syndrome.py` for individual maximal
windows and the CRT case; to be complemented by a MAGMA replication (PART I).
**Status.** `[VERIFIED-COMPUTATIONALLY]`; write-up `[THEOREM TO BE PROVED]`.

### G.5 Theorem 5 ($\mathrm{lcm}$ tolerance law and removal of the cyclic ceiling)
**Statement.** $T_{\max}=\Theta-1=\mathrm{lcm}_i\,\mathrm{ord}_{f_i}(x)-1$; hence
(i) extra components amplify tolerance without increasing any single order;
(ii) $T>n$ is possible for $m\ge2$ or $\lambda\ne1$; (iii) $T/L$ can exceed $1/2$, while cyclic
QSCs satisfy $T<n=L-T$.
**Assumptions.** A1–A6.
**Strategy.** CRT on $R_\lambda/\langle f\rangle\cong\prod_iR_{\lambda_i}/\langle f_i\rangle$: the
order of $x$ is the lcm of component orders; combine with Theorem 4.
**Lemmas.** F.7, F.8, G.4.
**Proof outline.** As in G.4 plus the order formula; the sharpness part exhibits two
admissible chains with $\mathrm{ord}$ $21$ and $7$ whose lcm is $21$; for (i) use components
with coprime orders (e.g. $7$ and $3$).
**Verification plan.** `verify_syndrome.py` ring case (21/21 distinct pairs, 0 collisions);
`verify_params.py` ($\Theta=21$, $n=7$, $T/L=0.588$); jitter check.
**Status.** `[VERIFIED-COMPUTATIONALLY]`; write-up `[THEOREM TO BE PROVED]`.

### G.6 Theorem 6 (separation of synchronization and self-orthogonality)
**Statement.** Tolerance depends only on $(g_C,g_D,\lambda)$ (through $\Theta$); the quantum
parameters depend only on the Gram/hull data. Consequently the sets of admissible tolerance
values and admissible quantum parameters are independent, and any chain pair can be
"repaired" for the quantum layer by entanglement assistance without loss of tolerance.
**Assumptions.** A1–A6.
**Strategy.** Functional dependence argument: the syndrome map is defined on
$R_\lambda/\langle f\rangle$ (no inner product); the CSS/EA-CSS parameter formulas depend only
on $\psi(C)$ and $\psi(C)^{\perp_\kappa}$.
**Proof outline.** Compose Theorem 4 with the EA-CSS bookkeeping; note that neither formula
references the other's data.
**Verification plan.** Construct (i) a chain with $\Theta$ large and
$C^{\perp}\nsubseteq C$ (entanglement needed) and (ii) the same $f$ with a dual-containing
chain — the tolerance must coincide; feasible with the existing scripts.
**Status.** `[THEOREM TO BE PROVED]` (short).

### G.7 Theorem 7 (QSC parameter theorem over $A$)
**Statement.** Theorem F.10: $[[N+T,K,d]]_Q$ with $K=2\dim\psi(C)-N$,
$d\ge\min\{d(\psi(C)\setminus\psi(C)^{\perp_\kappa}),d(\psi(C)^{\perp_\kappa}\setminus
\psi(C))\}$, $T\le\Theta-1$.
**Assumptions.** A1–A7, $C^{\perp_{\sigma_\kappa}}\subseteq C$.
**Strategy.** CSS/Hermitian construction over $\psi(C)$, with the tolerant block from
Theorem 4; distance via the standard CSS distance formula; dimension by linear algebra.
**Proof outline.** Stabilizer commutation follows from dual containment; the tolerant
encoding is well defined on $D$ by Lemma F.7; the shift syndromes are disjoint from the
error syndromes by the content-free property.
**Verification plan.** Exhaustive enumeration of all codewords for $N\le16$ to compute $d$
exactly (`verify_params.py`); MAGMA `QuantumCode(C1,C2)` cross-check; Grassl table lookup for
each claimed $[[N,K,d]]$.
**Status.** `[THEOREM TO BE PROVED]`; instances `[COMPUTATIONAL RESULT]`.

### G.8 Theorem 8 (EA-QSC parameter theorem)
**Statement.** $[[N+T,K,d;c]]_Q$ with $c=\dim_{\mathbb F_q}\mathrm{hull}_{\sigma_\kappa}(\psi(C))$
and tolerance $T\le\Theta-1$ unchanged.
**Assumptions.** A1–A7 (dual containment replaced by the hull-dimension formula).
**Strategy.** EA-CSS with $c$ ebits; the tolerant block is independent of the ebit structure.
**Proof outline.** EA-CSS commutation from the symplectic Gram matrix of
$\psi(C)$; the ebits are consumed before transmission, so the synchronization argument is
untouched (this is Theorem 6 instantiated).
**Verification plan.** Small cases: compute $c$ and $K$ by rank computations; sanity-check
against the source's Example 2 parameters (their $[[14,10,4;4]]_9$) when the same code is
used without synchronization; MAGMA EA-CSS cross-check.
**Status.** `[THEOREM TO BE PROVED]`.

### G.9 Theorem 9 (jitter-tolerant synchronization)
**Statement.** If the physical misalignment hits component $i$ with offset
$a+\delta_i$, $\delta_i\in\{0,\dots,\Delta\}$, then the syndrome *pair/tuple* remains injective
on windows of length $\Theta$; hence tolerance is robust to component jitter of bounded
amplitude $\Delta$ (the receiver recovers $a$ modulo $\Theta$, not each $\delta_i$).
**Assumptions.** A1–A6; the alphabet-model caveat of Model H.2.1.
**Strategy.** CRT injectivity of $a\mapsto(a+\delta_1,\dots,a+\delta_m)$ modulo the component
orders.
**Proof outline.** For fixed $(\delta_i)$, the map $a\mapsto(a+\delta_i\bmod o_i)_i$ is a
translation on $\prod\mathbb Z/o_i$, hence injective on any window of length $\mathrm{lcm}$.
**Verification plan.** `verify_params.py` CRT-jitter check (all $(\delta_1,\delta_2)\in\{0,1\}^2$);
extend to $\Delta=2,3$ and $m=3$ in the paper's code.
**Status.** partially `[VERIFIED-COMPUTATIONALLY]`; full statement `[THEOREM TO BE PROVED]`;
the *recovery of the framing* (whether the insertion fell inside a symbol) is `[OPEN PROBLEM]`
and requires a framing/label code — explicitly not claimed.

### G.10 Theorem 10 (designed distance for mixed-weight chains)
**Statement.** If each $g_i$ is a product of coset minimal polynomials with designed
consecutive zero sets, then $d\ge\min_i\delta_i^{\mathrm{BCH}}$ and the tolerant quantum code
inherits $d\ge\min_i\delta_i^{\mathrm{BCH}}$ up to the CSS correction
$d\ge\min\{d(C),d(C^\perp)\}$.
**Assumptions.** A1–A7; squarefree, primitive or non-primitive cyclotomy as in the audited
BCH papers.
**Strategy.** Componentwise BCH bound + CSS distance formula.
**Proof outline.** Each component is a BCH-type constacyclic code; apply the BCH bound
componentwise; CSS gives the quantum distance bound.
**Verification plan.** Compare with `[REFERENCE]` Grassl/Brouwer tables; MAGMA `BCHBound`,
`MinimumDistance`.
**Status.** `[THEOREM TO BE PROVED]`.

### G.11 Theorem 11 (tolerant Singleton and the synchronization defect)
**Statement.** For a QSC/EA-QSC built from a chain with tolerance $\Theta-1$:
$K\le Q^{N+T-2(d-1)-2c}$; the *synchronization defect*
$\delta_{\mathrm{sync}}=N+T-2\log_QK-2(d-1)\ge0$; and $\delta_{\mathrm{sync}}$ is additive over
component chains.
**Assumptions.** Standard stabilizer/EA-CSS framework.
**Strategy.** Apply the quantum Singleton bound to the padded block, noting that the added
symbols contribute to the Singleton accounting exactly as length does; prove
non-negativity; establish additivity from the CRT structure.
**Proof outline.** Textbook Singleton argument on the tolerant block + the fact that the
extra $T$ positions carry no logical information but do occupy a position in the
partition argument. **The claim that the tolerance is "free" in the Singleton sense must be
either proved or weakened to a conjecture** — this is the most delicate point of the paper
and is flagged as such.
**Verification plan.** Check the bound on all computed instances of Table 5 (no violation is
evidence of consistency, not a proof).
**Status.** partially `[CONJECTURE]`; the non-negativity part `[THEOREM TO BE PROVED]`.

### G.12 Theorem 12 (asymmetric-twist admissible pairs)
**Statement.** For a two-component algebra, a chain $(C_1,C_2)$ admits an
$(a_l,a_r)$-EA-QSC with per-component twists $(\kappa_1,\kappa_2)$ iff
$\lambda_i^{p^{\kappa_i}+1}=1$; the tolerance is unaffected by $(\kappa_1,\kappa_2)$.
**Assumptions.** A1–A7.
**Strategy.** Componentwise application of Theorems 3, 4, 8.
**Proof outline.** Direct.
**Verification plan.** Sweep $(\kappa_1,\kappa_2)\in\{0,1\}^2$ for $q=4,9,16,25$; record the
dimension/entanglement gains.
**Status.** `[THEOREM TO BE PROVED]` (expected to be a corollary; it is separated because it
is the source of tabulated gains).

### G.13 Lemmas (supporting, each with its own verification)
L1 (Frobenius/A) — `[PROVED-HERE]`. L2 (CRT) — `[PROVED-HERE]`. L3 (window-shift) —
`[VERIFIED-COMPUTATIONALLY]`. L4 ($\sigma$-reciprocal calculus) — `[TO BE PROVED]`.
L5 (order formula $\mathrm{ord}_f=rh$) — `[VERIFIED-COMPUTATIONALLY 2000/2000]`.
L6 (Gray-map commutation with the twisted dual) — `[TO BE PROVED, componentwise]`.
L7 (EA-CSS bookkeeping with hull dimension) — `[TO BE PROVED from the standard theory]`.
L8 (CRT injectivity for the lcm law) — `[PROVED-HERE]`.

### G.14 Conjectures and open problems (to be printed as such, not as theorems)
* **Conjecture 1.** The tolerant Singleton bound is strictly stronger than the plain
  Singleton bound exactly for chains in which one object serves both purposes.
* **Conjecture 2.** $\delta_{\mathrm{sync}}$ is asymptotically additive under the
  "component lamination" used in PART J, with $T/L\to1-\frac{n}{\Theta}$ at fixed $n$.
* **Conjecture 3 (tolerant Hamming).** The tolerant Hamming bound equals the plain Hamming
  bound on the padded block, and the shift window consumes no correctable error budget.
* **Conjecture 4 (EA-GV).** For $q\to\infty$, at fixed $T/N$, random mixed-weight chains
  produce EA-QSCs whose rate approaches the EA-Singleton bound.
* **Open problem 1.** Repeated-root ($p\mid n$) mixed-weight chains: does the syndrome
  identity survive the nilpotent-free but non-squarefree quotient?
* **Open problem 2.** Framing recovery: can a label/framing code on $\psi$ decide whether an
  insertion fell *inside* an $A$-symbol (the jitter problem of Theorem 9)?
* **Open problem 3.** The source paper's open problem (counting non-isometric constacyclic
  codes with prescribed Galois-hull dimension over $A$) remains open and is *not* claimed
  here; the synchronization version of that counting problem is new and is stated as an
  open problem of this paper.
* **Open problem 4.** General Gray maps $M\ne I_N$: can they improve $c$ or $d$ *without*
  destroying the tolerant chain structure? (This is candidate direction D3, parked.)

---

## PART H — Quantum Construction

### H.1 Pipeline (Figure 3 of PART L)

$A$-algebra $\to$ $\lambda$-constacyclic chain $C\subseteq D$ over $A$ $\to$
$\sigma_\kappa$-dual/hull data $\to$ tolerant block $B_{a_l,a_r}(v)$ $\to$
Gray image $\psi(C)$ $\to$ CSS/Hermitian/EA-CSS stabilizer on the padded block $\to$
$[[N+T,K,d(;c)]]_Q$ with tolerance $T\le\Theta-1$.

### H.2 Models (state both; claim only in the first)

**Model H.2.1 ($A$-symbol block-synchronization channel; used in all claims).** The channel
acts on the *transmitted symbols*, which are elements of the code alphabet (here: $A$-symbols,
i.e. $N$ $\mathbb F_q$-coordinates per symbol in the Gray image); insertions/deletions shift
the block by an integer number of *symbols*. This is the model in which Lemma F.7/Theorem F.8
are proved, and it is the model used by the ring-based QSC literature when it speaks of a
code over a ring. **Honest caveat, to appear in the paper:** if the channel acts on
$\mathbb F_q$-coordinates inside a symbol, then a single insertion can shift the components
by *different* symbol counts; Theorem 9 shows the lcm-law still identifies the global shift,
and recovering the framing is Open problem 2. We do **not** claim the coordinate-level model.

**Model H.2.2 (coordinate-level channel; deferred).** State it, compute example tolerances
for the Gray image as an $\mathbb F_q$-linear code, and report as future work.

### H.3 The quantum construction, step by step

1. Choose $q=p^e$, $e$, $\kappa$ (with $\kappa=e/2$ ⟹ Hermitian), $A=\prod_i\mathbb F_{q^{d_i}}$,
   $n$ with $\gcd(n,q)=1$, and units $\lambda_i$ with $\lambda_i^{p^\kappa+1}=1$.
2. Factor $x^n-\lambda_i$ over $A_i$ (algorithms: PART I).
3. Select divisors $g_{i,C}\mid g_{i,D}\mid x^n-\lambda_i$ (a chain per component).
4. Check the quantum condition $h_i^\tau\equiv0\bmod g_{i,C}$ (Theorems 3/F.5); if it fails,
   compute $\dim\mathrm{hull}$ and switch to entanglement assistance (Theorem 8).
5. Form the ring code $C=\bigoplus_ie_iC_i$, $D=\bigoplus_ie_iD_i$, and
   $f_i=g_{i,C}/g_{i,D}$, $\Theta=\mathrm{lcm}_i\mathrm{ord}_{f_i}(x)$.
6. Pick $a_l,a_r\ge0$ with $a_l+a_r\le\Theta-1$; block length $L=n+a_l+a_r$ per component;
   physical length $N=(\sum_id_i)L$ for the juxtaposition Gray map.
7. Build the tolerant encoder: $v\in D\mapsto B_{a_l,a_r}(v)$ (Definition F.4.2); the logical
   states are the CSS cosets of $\psi(C)$; the shift register of window syndromes is
   $a\mapsto x^{-a}\bmod f$.
8. Decoder: (i) compute $W$, divide by $g_D$ in $R_\lambda$; (ii) reduce mod $f$ and compare
   with the precomputed table $\{x^{-a}\bmod f\}_{a=-a_l}^{a_r}$ to obtain $a$; (iii)
   un-shift and run the CSS decoder of $\psi(C)$.
9. Report $[[N+T,K,d;c]]_Q$ together with $T$, the window asymmetry $(a_l,a_r)$ and the
   achieved ratios $T/L$, $K/N$, $d$.

### H.4 Ebit accounting (must be explicit in the paper)

* Non-assisted: $c=0$, $K=2\dim\psi(C)-N$ (Theorem 7).
* Assisted: $c=\dim\mathrm{hull}_{\sigma_\kappa}(\psi(C))$; the ebits are consumed at
  encoding, before the block is transmitted, hence $T$ does not depend on $c$ (Theorem 6/8).
* Sanity anchor: when the same classical object is used without synchronization, the
  parameters must reproduce the source paper's EAQECC instance $[[14,10,4;4]]_9$-style
  computations `[REQ-VERIFY: recompute before quoting]`.

### H.5 Do-not-claim list (reviewer-proofing)

* No claim that an EA-QSC is "the first" until PART Q item 4 is completed.
* No claim of parameter superiority; only the *structural* claims (lcm law, $T>n$, decoupling).
* No claim that the $A$-symbol model is physically canonical.
* No claim about repeated-root lengths.

---

## PART I — Computational/MAGMA/Python Plan

**Purpose.** The computation must *verify mathematics*, not manufacture tables. Every task
below is an implication test (`A ⟺? B`), an exhaustive instance, or a parameter-recovery job
whose output feeds a theorem. A working seed implementation already exists
(`blueprint/verify/`, see `verify/RESULTS.md`); the plan extends it and pairs it with MAGMA
for independent replication.

### I.1 Environment, inputs, conventions (to be stated verbatim in the paper's
"Reproducibility" appendix)

* Python 3.12 + `sympy` (factorisation over $\mathbb F_p$), `numpy` (linear algebra over
  $\mathbb F_p$ via integer matrices), the workspace's `fflib*` modules for exact
  $\mathbb F_q$-arithmetic (no floating point anywhere).
* MAGMA V2.x: `GF(q)`, `PolynomialRing`, `Factorization`, `ConstacyclicCode(F,n,λ)`,
  `Dual`, `HermitianDual`, `Hull`-by-linear-algebra, `MinimumDistance`, `MinimumWeight`,
  `AutomorphismGroup` (only for equivalence checks), `QuantumCode(C)`, `QuantumCode(C1,C2)`,
  `BCHBound`, `BKLC/BDD` for reference tables.
* Inputs are always: $(p,e)$; $\kappa$; the algebra $A$ (as squarefree moduli $t_i$ or as
  component degrees $d_i$); $n$; the units $\lambda_i$; the divisors
  $g_{i,C}\mid g_{i,D}\mid x^n-\lambda_i$; the window $(a_l,a_r)$.
* Outputs are always: the component data table, $\Theta$, the syndrome table, and the
  quantum parameters $[[N+T,K,d(;c)]]_Q$ with the method used for $d$.

### I.2 Task list

| # | Task | Tool | Inputs | Algorithm | Output / acceptance criterion |
|---|---|---|---|---|---|
| T1 | Field/polynomial primitives self-test | Python | small fields | exhaustive arithmetic identities | inverses, Frobenius, egcd, divmod on all pairs ($\deg\le4$); 100 % agreement |
| T2 | Factorisation of $x^n-\lambda$ and divisor enumeration | Python + MAGMA `Factorization` | $q\le25$, $n\le15$ | distinct/equal-degree factorisation; divisor lattice | identical factor degree lists and orders in both systems |
| T3 | Twist condition (Thm 2) | Python + MAGMA | all $q$ with $e\le3$, $n\le7$, all $\lambda$, all $\kappa$ | build $C$, compute $\sigma_\kappa$-dual, test $\lambda$-constacyclicity | exact equivalence, 0 counterexamples; report the count |
| T4 | Twisted dual generator (Thm 3) | Python + MAGMA (`Dual`/`HermitianDual`) | as T3 | compare $\langle h^\tau\rangle$ with the computed dual basis | identical subspaces (row-space equality) |
| T5 | Containment criterion (Thm 3, F.5) | Python + MAGMA | as T3 | $h^\tau\equiv0\bmod g$ vs subspace containment | equivalence; **also run the two rejected variants to document them** |
| T6 | Order formula (Lemma L5) | Python + MAGMA | $n\le30$, $q\le25$, all $\lambda$ | $r$, $h$, gcd conditions | 0 counterexamples |
| T7 | Window-shift lemma (F.7) | Python | 1262-configuration sweep + random words | construct $\lambda$-periodic continuation; find $\mu_a,\tau$-shift | every window is a scalar multiple of $\tau_\lambda^{-a}(v)$ and lies in $D$ |
| T8 | Syndrome identity (Thm 4/F.8) | Python (independent operator) + MAGMA | as T7 | compute $J_a\bmod f$; compare with $x^{-a}$ | exact equality, content-free; **expected value computed twice by different algorithms** |
| T9 | Tolerance law (Thm 5) | both | $m\in\{1,2,3\}$ components, orders with different gcd patterns | enumerate $a$ in maximal windows; test injectivity | injective on $[-(T),T]$ iff $T<\mathrm{lcm}$, and collisions at $\mathrm{lcm}$ |
| T10 | Exact distances (small) | Python exhaustive + MAGMA `MinimumDistance` | $N\le16$ | enumerate all $Q^K$ codewords (Python) vs MAGMA algorithms | identical $d$; record runtime |
| T11 | Distance bounds (large) | MAGMA | $N\le200$ | `BCHBound`/`MinimumDistance` with random sampling lower bounds; `BDD`/`BKLC` upper bounds | interval $[d_{\text{low}},d_{\text{up}}]$ reported honestly |
| T12 | Quantum parameters | both | $C_1,C_2$ | CSS formula, Hermitian formula, EA-CSS with $c=\dim\mathrm{hull}$ | $[[N,K,d;c]]_Q$; cross-check against `[REFERENCE]` Grassl tables for $Q\le4$, $N\le30$ |
| T13 | $\kappa$-asymmetric pairs | both | $(\kappa_1,\kappa_2)\in\{0,\dots,e-1\}^2$ | componentwise Thm 12 | table of gains (dimension or $c$) with tolerance unchanged |
| T14 | Jitter robustness (Thm 9) | Python | orders $(o_1,\dots,o_m)$, $\Delta\le3$ | CRT injectivity | injective on windows of length lcm for every offset vector |
| T15 | Non-existence witnesses | both | small $q,n,\lambda$ | full divisor-lattice scan | list of $(\lambda,n)$ pairs admitting **no** nontrivial tolerant chain (e.g. $\mathbb F_4$, $n=3$, $\lambda=\omega$) — negative results are part of the evidence |
| T16 | Equivalence/counting experiments (optional) | MAGMA `AutomorphismGroup` | small $N$ | orbit counting of tolerant chains under the permutation group | honest report; feeds the open problem on counting |

### I.3 Algorithms to be specified in the paper (pseudocode, 6–10 lines each)

1. `SigmaDualBasis(C, κ)`: Gram matrix $G_{st}=\langle b_s,b_t\rangle_{\sigma_\kappa}$, nullspace
   over $\mathbb F_q$, dual basis.
2. `TwistedReciprocal(h, κ)`: h ↦ x^{deg h}h(1/x)^{σ_κ} (with the monic normalisation of F.4).
3. `WindowSyndrome(v, g_D, f, a, λ, n)`: build $B$, take the window, divide by $g_D$ in
   $R_\lambda$, reduce mod $f$.
4. `LCMTolerance(chain, A, λ)`: compute $f_i$, `ord` via repeated multiplication in
   $R_{\lambda_i}/\langle f_i\rangle$ (never by factoring the whole group), take the lcm.
5. `SupportsTolerance(u, v, T, C)`: brute-force check that no non-zero difference of
   $\pm$-wrapped test words of $C$ has all syndromes in the window equal — a *direct*
   verification of the correctability definition that does not presuppose Theorem 4.
6. `ExactDistance(basis, Q)`: exhaustive enumeration with early pruning by syndrome.
7. `EACSSParameters(C1, C2)`: $c=\dim(C_1\cap C_2^{\perp})$-type rank computation; $K$, then
   distance bound.

### I.4 Small cases for *manual* verification (to be tabulated in the paper's Appendix)

* $\mathbb F_4$, $n=3$, $\lambda=\omega$: no tolerant chain (negative control).
* $\mathbb F_4$, $n=3$, $\lambda=1$, $C=\langle x-\omega\rangle$, $D=R$: three windows,
  $\Theta=3$, syndromes $\{1,\omega,\omega^2\}$ — checkable on paper in $\mathbb F_4$.
* $\mathbb F_9$, $n=4$, $\lambda=\omega^2$ (order $8$): $\Theta=8$ for the degree-1 divisor;
  windows $(1,2)$.
* $\mathbb F_4$, $n=7$, $\lambda=(\omega,1)$: the flagship, with $f_1,f_2$ of degree 3, orders
  $(21,7)$, $\Theta=21$.

**Flagged for human verification** (the paper must state that these were checked by hand
before publication): (i) the multiplier $\mu_a$ in Lemma F.7; (ii) the identity "expected
syndrome $=x^{-a}$" in the first nontrivial instance; (iii) the two negative results about
the rejected criteria; (iv) the lcm collision at $a=\Theta$.

### I.5 Reproducibility deliverables

* A single entry-point script that regenerates every numerical claim in the paper.
* A `RESULTS.md`-style log with commands and raw outputs (already started:
  `blueprint/verify/RESULTS.md`).
* Tolerance for runtime: all T1–T16 run under 10 minutes on a laptop except T11/T12 for
  $N>200$, which are explicitly marked as "sampled".

---

## PART J — Parameter Search Strategy

### J.1 Search space and constraints

$$\mathcal S=\Big\{(p,e,\kappa,A,n,m,(d_i),(\lambda_i),(g_{i,C},g_{i,D}),(a_l,a_r)\Big\}$$
with constraints: $\gcd(n,q)=1$; $\sum_id_i\le4$; $\lambda_i^{p^\kappa+1}=1$;
$g_{i,D}\mid g_{i,C}\mid x^n-\lambda_i$, $\deg(g_{i,C}/g_{i,D})>0$; components of $C$
dual-containing (non-assisted) or hull-dimension computed (assisted); $a_l+a_r\le\Theta-1$.

### J.2 Staged search (filters, then objectives)

1. **Stage 0 — component table.** For each $(p,e,\kappa,d_i,\lambda_i)$ with $d_i\le4$,
   $q\le 2^{10}$ or $3^{6}$, $n\le 2^{9}$: enumerate divisors of $x^n-\lambda_i$, their
   $\mathrm{ord}$, and whether they are dual-containing. Cache to disk.
2. **Stage 1 — tolerance assembly.** For each tuple of components, compute
   $\Theta=\mathrm{lcm}$ and the maximal window; **rank by $\Theta/n$** (the new quantity of
   this paper) and by $\Theta$ itself.
3. **Stage 2 — quantum feasibility.** For each candidate chain, compute
   $\dim\psi(C)$, $c=\dim\mathrm{hull}_{\sigma_\kappa}$, the non-assisted dimension
   $2\dim\psi(C)-N$ (if dual-containing), and the classical distances by MAGMA.
4. **Stage 3 — Pareto filtering.** Keep the Pareto front in $(T/L,\ K/N,\ d)$; discard
   dominated points; never discard a point solely because it has small $d$ if it is
   extremal in $T/L$ (tolerance is the paper's subject).
5. **Stage 4 — comparison.** Compare only against entries of the comparison table (PART K)
   with the same $Q$, the same physical length, and the same error-correction requirement;
   record the comparison criterion explicitly ($T$ at fixed $(N,K,d)$, or $d$ at fixed
   $(N,T)$).
6. **Stage 5 — worst-case reporting.** Report (i) the best-found points per family,
   (ii) the *fraction* of the search space that is non-empty (evidence for the existence
   theorems), and (iii) every negative result (e.g. lengths where no tolerant chain exists).

### J.3 Objective functions (to be defined in the paper)

* tolerance efficiency $\mathrm{TE}=T/L$;
* rate $\rho=K/N$ (logical qudits per physical qudit, counting only the block);
* tolerant Singleton ratio $\mathrm{TSR}=(N+T-2(d-1)-2c-\log_QK)$ — the defect;
* **heterogeneity amplification** $\mathrm{HA}=\Theta/\max_i\mathrm{ord}_{f_i}(x)\ge1$ — the
  quantity that only exists in the mixed-weight setting.

### J.4 Search pseudocode (paper-ready)

```
for each admissible (p,e,kappa) and each lambda-pattern (lambda_1..lambda_m):
    generate the component tables (ord, dual-containing flags)
for each tuple of component entries with lcm Theta > n:      # Stage 1 gate
    build basis(psi(C)) and basis(psi(C)^perp_kappa)         # Stage 2
    K = 2*dim - N ;  c = dim hull
    if c == 0 or entanglement allowed:
        d = ExactDistance(...) or BCHBound(...)
        record (Theta, L, N, K, d, c, HA, TE, rho, TSR)      # Stage 3
filter Pareto front; compare with PART K table                # Stage 4/5
```

### J.5 Expected outcomes and honest risks

* **Expected structural winners:** $m\ge2$ components with coprime orders (e.g. $3$ and $7$,
  $5$ and $9$), giving $\mathrm{HA}>1$ and $T>n$, hence $T/L>1/2$ — impossible for cyclic
  QSCs. This is the paper's headline quantitative statement; it will be reported as a
  *structural* fact with an explicit example (`[COMPUTATIONAL RESULT]`).
* **Risk 1:** the search finds no $[[N,K,d]]$ beating known tables. Mitigation: the paper's
  claims are structural (invariant, decoupling, EA-QSC), and the comparison table reports
  "comparable/better score" honestly per criterion.
* **Risk 2:** parameter counting errors from applying the CSS distance bound as if exact.
  Mitigation: distances are either exhaustive or reported as intervals.
* **Risk 3:** the search space is dominated by small $q$ where the field theory is already
  saturated. Mitigation: include $m=3$, unequal $d_i$ and $\kappa$-asymmetric tuples, the
  places where the existing literature literally cannot go.

---

## PART K — Comparison Framework

### K.1 Required table columns (exactly these, in this order)

`Reference | Algebraic Structure | Code Family | n | k | d | Quantum Parameters | Construction | Synchronization Capability | Bound/Defect | Novel Feature`

### K.2 Fairness rules (must be stated in the caption)

1. "Synchronization capability" is reported as the *pair* $(a_l,a_r)$ plus the achieved
   $T=a_l+a_r$, **normalized** as $T/L$; papers that only bound $a_l+a_r<n$ are recorded with
   the bound they state, not with our value.
2. "Quantum Parameters" are reported in the *authors'* notation and dimension convention
   ($q$-ary qudits, or qubits for Hermitian codes over $\mathbb F_4$, etc.); a footnote
   converts every row to qubits-equivalent keep only when meaningful.
3. When a row's paper reports only a bound (e.g. $d_z\ge\ldots$), the table shows the bound
   with "$\ge$".
4. No row is filled with numbers we have not read in the source or computed ourselves;
   missing data is `[PARAMETER TABLE]`.

### K.3 Baseline rows (to be completed; sources are in PART P, flagged where unverified)

| Reference | Algebraic Structure | Code Family | n | k | d | Quantum Parameters | Construction | Synchronization Capability | Bound/Defect | Novel Feature |
|---|---|---|---|---|---|---|---|---|---|---|
| Fujiwara `[REFERENCE]` | $\mathbb F_q$, cyclic | dual-containing cyclic | $n$ | $2k_1-n$ | — | $[[n+a_l+a_r,2k_1-n]]_q$ | CSS + padding | $a_l+a_r<\mathrm{ord}_f(x)$ | corrects $\lfloor(d_1-1)/2\rfloor$/$\lfloor(d_2-1)/2\rfloor$ | founding construction |
| Fujiwara–Tonchev–Wong `[REFERENCE]` | cyclotomy/PG | cyclic | varies | — | — | QSC tables | CSS + padding | maximal in cyclic sense | — | algebraic design technique |
| Liu–Liu (2021) `[REFERENCE]` | chain rings; $\mathbb F_p+v\mathbb F_p$ | dual-containing; constacyclic Gray images | up to $\sim2n$ | — | — | QSC | CSS (ring code; Gray image) | "upper bound attained" | — | first ring QSCs |
| Du–Ma–Luo–Huang–Wang (2020) `[REFERENCE]` | $\mathbb F_q[u,v]$ non-chain | $(\lambda(u+v)\mid u-v)$, negacyclic $\lambda_1^2+1=0$ | $2n$ components, QSC $4n$ | — | $\min\{2d_1,2d_2,\max\{d_1,d_2\}\}$ | QSC | ring construction + CSS | maximal iff $\mathrm{ord}_f=2n$ | — | doubled length, better bit-error capability |
| Li–Zhu (2022) `[REFERENCE]` | $\mathbb F_q$, constacyclic | $n=q^{2\ell}-1$ | $q^{2\ell}-1$ | — | $\delta$ | $[[n+a_l+a_r,\cdot]]_q$ | CSS + padding | $a_l+a_r<n$ | phase/bit error floors | exact distance |
| s12095-025 (BCH, $(q^m-1)/a$) `[REFERENCE]` | cyclotomic | BCH | $(q^m-1)/a$ | — | BCH | QSC | CSS + padding | $a_l+a_r<n$ | BCH bound | non-primitive lengths |
| s40314 (repeated-root QC) `[REFERENCE]` | $\mathbb F_q$, QC | 2-generator QC | $2\ell p^s$ | — | — | QSC | QC→CSS | inherited | — | quasi-cyclic structure |
| Zhang–Kong–Zheng (2026) `[REFERENCE, verify]` | non-chain ring | constacyclic, $\ell$-Galois hull | — | — | — | EAQECC/QECC, Construction X | Gray map + hull | **none** | EA Singleton | Gray-map generalization |
| Galois hulls over affine algebras `[REFERENCE]` (source) | $A$ semisimple | $\lambda$-constacyclic | $n$ | $k-\dim\mathrm{hull}$ | 4 (examples) | $[[n,k-\dim\mathrm{hull},d;n-k-\dim\mathrm{hull}]]_q$ | EAQECC via Gray map | **none** | $2(d-1)\le n-k+c$ | general $\kappa$-Galois hull |
| **This work** | $A=\prod\mathbb F_{q^{d_i}}$ mixed weights | $\lambda$-constacyclic chain, $\kappa$-Galois | $n$ per component | $2\dim\psi(C)-N+2c$ | $\ge\min\{d(\psi(C)\setminus\ldots)\}$ | $[[N+T,K,d;c]]_Q$ | tolerant block + CSS/Hermitian/EA-CSS | $T\le\mathrm{lcm}_i\,\mathrm{ord}_{f_i}-1$, $T>n$ possible | tolerant Singleton + defect | lcm law; decoupling; EA-QSC |

*(The "This work" row must be re-filled after the search of PART J with real numbers.)*

---

## PART L — Proposed Figures and Tables

### Figures (4 required, +2 optional)

**Fig. 1 — Ring/algebra decomposition (required).**
Left: $A=\mathbb F_q[X]/\langle t(X)\rangle$ with squarefree $t$; middle: CRT
$A\cong\prod_i\mathbb F_{q^{d_i}}$ with idsempotents $e_i$; right: the code
$C=\bigoplus_ie_iC_i$ and the weight $\lambda=\sum_i\lambda_ie_i$. Annotation: the *orders*
$\mathrm{ord}_{f_i}(x)$ attached to each component, with the lcm arrow between them (the
paper's invariant).

**Fig. 2 — Pipeline (required).**
"Finite ring/algebra → classical λ-constacyclic chain $C\subseteq D$ → $\sigma_\kappa$-dual and
hull → self-orthogonality/entanglement → tolerant block + CSS → $[[N+T,K,d;c]]_Q$", drawn as a
left-to-right pipeline with the two *independent* inputs (tolerance from the chain; quantum
parameters from the Gram data) drawn as separate rails, converging only at the tolerant
quantum code — the visual form of Theorem 6.

**Fig. 3 — Computational workflow (required).**
Nodes = T1–T16 of PART I; edges = data dependencies; each node annotated with the theorem it
verifies; a shaded block for MAGMA replication.

**Fig. 4 — Parameter comparison (required).**
Scatter/step plot: $T/L$ (and $T$) versus physical length $N$ for (i) cyclic QSCs from the
audited corpus (all with $T/L<1/2$), (ii) the $(\lambda(u+v)\mid u-v)$ family, (iii) the
mixed-weight families of this paper (including the computed point $N=34$, $T=20$,
$T/L=0.588$). Second panel: $\mathrm{HA}=\Theta/\max_i\mathrm{ord}_{f_i}$ versus $m$ showing
heterogeneity amplification.

**Fig. 5 (optional) — Syndrome map.** The window positions $[-a_l,a_r]$ mapped to the
precomputed syndrome table $\{x^{-a}\bmod f\}$; annotate the collision at $a=\Theta$.

**Fig. 6 (optional) — Decoder block diagram** with the lcm combiner for $m=2$.

### Tables (6 required)

**Tab. 1 — Notation.** Symbol / meaning / where defined / assumptions. Must include
$q,p,e,\kappa,\sigma_\kappa,A,A_i,e_i,N,\lambda,\lambda_i,R_\lambda,g,g_i,h,h^\tau,C,D,f,f_i,
\Theta,\mathrm{ord}_f,\mu_a,a_l,a_r,T,L,\psi,Q,K,d,c,\delta_{\mathrm{sync}},TE,HA$.

**Tab. 2 — Literature table.** One row per audited paper with the 11 comparison columns
(PART K), sources from PART P.

**Tab. 3 — Code parameters table.** Per component: $A_i$, $\lambda_i$, $n$,
factorisation of $x^n-\lambda_i$ (degrees and orders), $[n,k,d]_{q^{d_i}}$ for each chosen
divisor, dual-containing flag, $\kappa$.

**Tab. 4 — Valid parameter sets.** Which $(q,e,\kappa,\lambda,n)$ admit nontrivial tolerant
chains, and the maximal $\Theta$; must include the negative entries (e.g. $\mathbb F_4$,
$n=3$, $\lambda=\omega$).

**Tab. 5 — Quantum codes.** $[[N+T,K,d;c]]_Q$ with $T$, $(a_l,a_r)$, $T/L$, $\mathrm{HA}$,
method used for $d$ (exact/greedy/BCH bound), and the comparison verdict.

**Tab. 6 — Bound/defect table.** Tolerant Singleton values, $\delta_{\mathrm{sync}}$, the plain
quantum Singleton value for the same block, the difference, and the tolerant Hamming/GV
status (`[CONJECTURE]` rows clearly marked).

---

## PART M — Full Q1-Level Paper Structure

| § | Title | Content | Pages |
|---|---|---|---|
| 1 | Introduction | synchronization problem; why the same-object assumption was never questioned; contributions list (4 items); relation to ring-QSC literature | 1.5 |
| 2 | Preliminaries | semisimple algebras, CRT, $\kappa$-Galois inner product with the convention bridge, constacyclic codes, hulls, Gray maps, channel models | 2 |
| 3 | Codes and duality over $A$ | Thms 1–3 (structure, twist condition, twisted dual + containment criterion); the two *rejected* criteria in a remark (rigour signal) | 2.5 |
| 4 | Synchronization theory | Defs of $\lambda$-periodic continuation/padding; Lemma (window shift); Thm 4 (syndrome identity); Thm 5 (lcm law and $T>n$); Thm 6 (decoupling) | 3 |
| 5 | Quantum constructions | Thms 7–10 (QSC, EA-QSC, asymmetric twists, designed distance); decoder | 3 |
| 6 | Bounds | Thm 11 (tolerant Singleton, defect), Conj. 1–4 with explicit statements of what is *not* proved | 2 |
| 7 | Examples and parameters | the fully computed family $[[14+T,2,3]]_2$; tables 3–5; comparison table | 3 |
| 8 | Conclusion and open problems | open problems 1–4 from PART G.14 | 0.5 |
| A | Appendix A: proofs | deferred algebra | 3 |
| B | Appendix B: reproducibility | scripts, versions, commands, raw outputs, manual-checks checklist | 1.5 |
| C | Appendix C: tables | full parameter tables | 2 |

**Contributions list (as it must appear in the introduction).**
(C1) a new tolerance invariant (lcm of component orders) with a verified syndrome identity;
(C2) the decoupling of synchronization from self-orthogonality, with the consequence that
tolerance is unaffected by Galois twisting or entanglement assistance; (C3) the object class
$(a_l,a_r)$-EA-QSC with $c=\dim\mathrm{hull}_\kappa$, and asymmetric per-component twists;
(C4) tolerant Singleton/defect formalism with clearly labelled conjectures; plus an
exhaustive verification suite.

**Reviewer-risk table (to be internalised, not printed).**

| Likely objection | Pre-emptive move |
|---|---|
| "This is just a ring version of Fujiwara." | Theorem 5 (lcm; $T>n$) and Theorem 6 (decoupling) are impossible in the cyclic setting; Fig. 4 quantifies $T/L>1/2$. |
| "No parameter improvement." | The paper claims structure, not superiority; Tab. 5 reports verdicts honestly per criterion. |
| "The channel model is unrealistic." | Models H.2.1/H.2.2 are separated; Theorem 9 covers jitter; framing limits are an open problem, stated as such. |
| "The Galois twist is decorative." | Theorem 12 produces actual parameter gains from $(\kappa_1,\kappa_2)$; Theorem 3 shows the twist condition is exactly $\lambda^{p^\kappa+1}=1$ (not a definition). |
| "EA-QSC is not new." | A systematic search is a precondition for any novelty claim (PART Q item 4); if prior art exists, the paper reframes C3 as a *generalisation* and keeps C1/C2/C4. |

---

## PART N — Provisional Title and Abstract

### N.1 Five provisional titles (PROVISIONAL)

1. **Synchronization is independent of self-orthogonality: Galois-hull quantum synchronizable codes over semisimple algebras.**
2. **The lcm tolerance law: mixed-weight constacyclic codes and entanglement-assisted quantum synchronizable codes.**
3. **Beyond the cyclic ceiling: quantum synchronizable codes with tolerance exceeding the block length.**
4. **Galois-hull synchronization: κ-twisted duals, hull-dimension-controlled entanglement, and tolerant quantum codes over $\prod\mathbb F_{q^{d_i}}$.**
5. **From hulls to synchronization: a decoupled design theory for tolerant quantum codes.**

### N.2 Provisional abstract (PROVISIONAL — word count 187)

> Block synchronization and quantum error correction are usually built from the same
> algebraic object, a dual-containing cyclic code. We show that the two requirements are
> logically independent and exploit this separation inside the semisimple-algebra framework
> of Galois-hull theory. For a unit $\lambda=\sum_i\lambda_ie_i$ of a semisimple
> $\mathbb F_q$-algebra $A=\prod_i\mathbb F_{q^{d_i}}$ and a chain $C\subseteq D$ of
> $\lambda$-constacyclic $A$-linear codes, we prove that the receiver's window syndrome equals
> $x^{-a}$ in $R_\lambda/\langle f\rangle$ exactly, independently of the transmitted codeword,
> and that the tolerance against misalignment is $\mathrm{lcm}_i\,\mathrm{ord}_{f_i}(x)-1$.
> This invariant is strictly larger than any single component order and can exceed the block
> length, so the cyclic ceiling $T<n$ disappears. We characterize $\kappa$-Galois
> self-orthogonality by the divisibility criterion $h^\tau\equiv0\bmod g$, which decouples
> tolerance from the hull and yields entanglement-assisted quantum synchronizable codes
> $[[N+T,K,d;c]]_Q$ with $c=\dim\mathrm{hull}_\kappa$ and asymmetric twists per component. We
> add a tolerant Singleton bound and a synchronization-defect functional, and accompany every
> structural claim with an exhaustive, reproducible verification suite, including a computed
> family $[[14+T,2,3]]_2$ with $T\le20>n=7$.

*(Word count to be re-checked in the final file; if a venue's limit is 150 words, cut the
last clause of sentence 1 and the phrase "independently of the transmitted codeword".)*

---

## PART O — LaTeX Blueprint

The LaTeX source is provided as `PART_O_blueprint.tex` (compiles with
`\documentclass[11pt]{article}` and the package set required by the brief). Its plain-text
reading copy follows; the `.tex` file and this copy are kept in sync manually.

```latex
% ---------- preamble ----------
\documentclass[11pt]{article}
\usepackage{amsmath,amssymb,amsthm,mathtools,bm}
\usepackage{booktabs,graphicx}
\usepackage{algorithm,algpseudocode}
\usepackage[hidelinks]{hyperref}
\usepackage[margin=1in]{geometry}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\newcommand{\Fq}{\mathbb F_q}
\newcommand{\hull}{\operatorname{hull}}
\newcommand{\ord}{\operatorname{ord}}
\newcommand{\lcm}{\operatorname{lcm}}
\newcommand{\EAQSC}{\mathrm{EA\text{-}QSC}}
\title{[PROVISIONAL TITLE: Synchronization is independent of self-orthogonality ...]}
\author{[AUTHORS TO BE DETERMINED]}
\date{\today}
\begin{document}\maketitle
\begin{abstract}[PROVISIONAL ABSTRACT: see PART N.2 --- 187 words]\end{abstract}
\section{Introduction}            % PART M §1
\section{Preliminaries}           % semisimple algebras, CRT, kappa-Galois product, models
\section{Codes and Duality over $A$}
  \begin{theorem}[Twist condition]\label{thm:twist}
   [THEOREM TO BE PROVED] ... \end{theorem}
  \begin{theorem}[Containment criterion]\label{thm:contain}
   $C^{\perp_{\sigma_\kappa}}\subseteq C \iff h^\tau\equiv0\ (\mathrm{mod}\ g)$
   \textnormal{[VERIFIED-COMPUTATIONALLY: 742/742]} \end{theorem}
\section{Synchronization Theory}
  \begin{definition}[$\lambda$-periodic continuation]\end{definition}
  \begin{lemma}[Window shift]\label{lem:win}[VERIFIED-COMPUTATIONALLY]\end{lemma}
  \begin{theorem}[Window-syndrome identity]\label{thm:synd}
   $J_a\bmod f=x^{-a}$, content-free \textnormal{[VERIFIED-COMPUTATIONALLY 1262/1262]}\end{theorem}
  \begin{theorem}[$\lcm$ tolerance law]\label{thm:lcm}
   $T_{\max}=\lcm_i\ord_{f_i}(x)-1$; $T>n$ possible \end{theorem}
  \begin{theorem}[Decoupling]\label{thm:decouple}\end{theorem}
\section{Quantum Constructions}
  \begin{theorem}[QSC parameters]\label{thm:qsc}\end{theorem}
  \begin{theorem}[EA-QSC parameters]\label{thm:eaqsc}\end{theorem}
  \begin{theorem}[Asymmetric twists]\label{thm:asym}\end{theorem}
  \begin{theorem}[Designed distance]\label{thm:bch}\end{theorem}
\section{Bounds and Defect}
  \begin{theorem}[Tolerant Singleton]\label{thm:singleton}\end{theorem}
  \begin{conjecture}[Tolerant Hamming]\end{conjecture}
  \begin{conjecture}[EA-GV]\end{conjecture}
\section{Examples and Parameters}
  \begin{table}[t]\centering\caption{[PARAMETER TABLE] Tab. 3}\end{table}
  \begin{table}[t]\centering\caption{[PARAMETER TABLE] Tab. 4}\end{table}
  \begin{table}[t]\centering\caption{[PARAMETER TABLE] Tab. 5}\end{table}
  \begin{figure}[t]\centering\caption{[FIGURE] Fig. 1 ring decomposition}\end{figure}
  \begin{figure}[t]\centering\caption{[FIGURE] Fig. 2 pipeline}\end{figure}
  \begin{figure}[t]\centering\caption{[FIGURE] Fig. 3 computational workflow}\end{figure}
  \begin{figure}[t]\centering\caption{[FIGURE] Fig. 4 parameter comparison}\end{figure}
\section{Conclusion and Open Problems}
\appendix\section{Proofs}\section{Reproducibility}\section{Full Tables}
\begin{thebibliography}{99}
  \bibitem{[REFERENCE]} [see PART P --- no entry may be invented]
\end{thebibliography}
\end{document}
```

**Plain reading copy.** Parts 1–8 of the manuscript follow PART M; every `\begin{theorem}`
above corresponds to a row of the PART E ledger; every `[PARAMETER TABLE]`/`[FIGURE]` marker
is filled from PART I/J; no placeholder may remain in the submitted version.

---

## PART P — Reference Plan

Rules used: no fabricated entries; each item is (a) in the supplied corpus, (b) verified by a
dated web lookup, or (c) a classical result whose bibliographic data must be checked before
submission. Items in group C must not be cited until verified.

### P.A Core (must be cited; the paper is not writable without them)

1. `[in corpus]` P. Debnath, H. Islam, E. Martínez-Moro, O. Prakash, *Galois hulls of
   constacyclic codes over affine algebra rings*, preprint arXiv:2412.08512v1 (the
   framework source; **volume/journal to be verified**).
2. `[in corpus]` H. Fujiwara, *Block synchronization for quantum information*, preprint
   arXiv:1206.0260v5; journal version to be verified (PRA 2013 per our reading of the
   version history).
3. `[in corpus]` H. Fujiwara, V. D. Tonchev, T. M. Wong, *Algebraic techniques in designing
   quantum synchronizable codes*, Phys. Rev. A **88**, 012318 (2013).
4. `[search-verified 2026-09]` H. Liu, X. Liu, *Quantum synchronizable codes from finite
   rings*, Quantum Inf. Process. **20**, 125–144 (2021), DOI 10.1007/s11128-021-03058-4.
5. `[in corpus]` C. Du, R. Ma, Y. Luo, X. Huang, M. Wang, *On a family of quantum
   synchronizable codes based on the $(\lambda(u+v)\mid u-v)$ construction*, IEEE Access
   **8** (2020), DOI 10.1109/ACCESS.2019.2963289 (**page range to be verified**).
6. `[in corpus]` G. G. La Guardia, *New families of asymmetric quantum BCH codes*, Quantum
   Inf. Comput. **11**(3&4), 239–252 (2011).
7. `[classical]` A. R. Calderbank, E. M. Rains, P. W. Shor, N. J. A. Sloane, *Quantum error
   correction via codes over GF(4)*, IEEE Trans. Inform. Theory **44**(4), 1369–1387 (1998).
8. `[classical]` A. Ketkar, A. Klappenecker, S. Kumar, P. K. Sariçiçek, *Nonbinary stabilizer
   codes over finite fields*, IEEE Trans. Inform. Theory **52**(11), 4892–4914 (2006)
   (**used for the Hermitian construction and stabilizer bookkeeping**).
9. `[classical]` T. Brun, I. Devetak, M.-H. Hsieh, *Correcting quantum errors with
   entanglement*, Science **314**, 436–439 (2006).
10. `[search-verified 2026-09]` E. Zhang, B. Kong, X. Zheng, *Quantum codes from Galois hulls
    of constacyclic codes over a finite non-chain ring*, Entropy **28**(4), 407 (2026),
    DOI 10.3390/e28040407 (**closest competitor for the QECC-side contribution; must be
    cited and differentiated**).
11. `[classical]` M. Grassl, *Bounds on the minimum distance of linear codes and quantum
    codes*, http://www.codetables.de (accessed 2026-09).

### P.B Supporting (cited where the corresponding technique is used)

12. `[in corpus / classical]` Y. Fan, L. Zhang, *Galois self-dual constacyclic codes*, Des.
    Codes Cryptogr. **84**(3), 473–492 (2017).
13. `[in corpus / classical]` E. Sangwisut, S. Jitman, S. Ling, P. Udomkavanich, *Hulls of
    cyclic and negacyclic codes over finite fields*, Finite Fields Appl. **33**, 232–257 (2015).
14. `[classical]` X. Liu, H. Liu, *Galois hulls of linear codes over finite fields*, Des. Codes
    Cryptogr. **88**(2), 241–255 (2020).
15. `[classical]` Y. Ding, X. Lu, *Galois hulls of cyclic codes over finite fields*, IEICE
    Trans. Fund. **103-A**(1), 370–375 (2020).
16. `[classical]` N. Sendrier, *On the dimension of the hull*, SIAM J. Discrete Math.
    **10**(2), 282–293 (1997).
17. `[classical]` C. Carlet, S. Guilley, *Complementary dual codes for counter-measures to
    side-channel attacks*, Adv. Math. Commun. **10**(1), 131–150 (2016).
18. `[in corpus / classical]` F. Ma, J. Gao, F.-W. Fu, *New non-binary quantum codes from
    constacyclic codes over* $\mathbb F_q[u,v]/\langle u^2-1,v^2-v,uv-vu\rangle$, Adv. Math.
    Commun. **13**(3), 421–434 (2019).
19. `[in corpus / classical]` A. Alahmadi, H. Islam, O. Prakash, P. Solé, A. Alkenani,
    N. Muthana, R. Hijazi, *New quantum codes from constacyclic codes over a non-chain ring*,
    Quantum Inf. Process. **20**(2), 60 (2021).
20. `[in corpus / classical]` Z. Tian, J. Gao, Y. Gao, *Hulls of constacyclic codes over finite
    non-chain rings and their applications in quantum codes construction*, Quantum Inf.
    Process. **23**(1), 9 (2024).
21. `[search-verified 2026-09]` L. Li, S. Zhu, L. Liu, *Quantum synchronizable codes from the
    cyclotomy of order four*, IEEE Commun. Lett. **23**(1), 12–15 (2019).
22. `[in corpus]` T. Nemec, A. Klappenecker, *hybrid quantum error correction*
    (arXiv:1911.12260v2; **journal data to be verified**).
23. `[in corpus]` T. Tansuwannont, T. Nemec, *hybrid subsystem quantum synchronizable codes*
    (arXiv:2409.11312v2; **title/journal to be verified**).

### P.C Requiring verification before citation (do not quote numbers from these until checked)

24. `[in corpus]` `s10773-022-05163-1` — constacyclic quantum synchronizable codes,
    Int. J. Theor. Phys. (2022), DOI 10.1007/s10773-022-05163-1: **exact title, authors,
    volume, and the parameter values quoted in PART B.7 must be re-read from the PDF**
    (our reading is from a text extraction).
25. `[in corpus]` `s12095-021-00501-2` (Whiteman cyclotomy) and `s12095-025-00815-5`
    (BCH, $(q^m-1)/a$): **authors, titles, volumes** (DOI prefix indicates Cryptography and
    Communications).
26. `[in corpus]` `s12190-022-01811-1` (BCH + QR) and `s40314-023-02298-7` (repeated-root QC):
    **authors, titles, journals**.
27. `[in corpus]` `Quantum_Synchronizable_Codes_From_Augmen`: **venue unconfirmed**.
28. `[unverified]` The claim "no entanglement-assisted quantum synchronizable code exists" —
    requires a systematic search (arXiv full text, MathSciNet, zbMATH) documented in the
    paper's footnote; **until then, phrase every novelty claim as "to the best of our
    knowledge, and subject to the search reported in Appendix"**.

---

## PART Q — Final Novelty / Rigour Audit (23 items)

**A. Novelty**

1. **Is the central object new?** The *tolerance invariant* $\Theta=\mathrm{lcm}_i\mathrm{ord}_{f_i}(x)$
   is new in the QSC literature (no audited paper has a multi-component order invariant); the
   *EA-QSC* object is new subject to item 4. — *Evidence:* PART B aggregate table; PART C G1/G2.
2. **Is the central theorem new?** The window-syndrome identity in a multi-component algebra
   with mixed weights is not in any audited paper (Fujiwara proves the cyclic case; ring QSC
   papers use Euclidean dual containment on Gray images). — *Evidence:* PART B.2 vs PART G.4.
3. **Does any result merely rename an existing one?** No: Theorem 5 changes the *set of
   admissible tolerance values* (lcm, $T>n$), and Theorem 6 changes the *design method*
   (decoupling, entanglement instead of strengthening the code). The audit of the source's
   Theorem 6 shows we are not even restating it (344/742 divergence).
4. **Prior-art search for the "first EA-QSC" claim.** **INSUFFICIENT EVIDENCE — REQUIRES
   VERIFICATION.** Must be completed before submission; fallback phrasing prepared (PART M
   reviewer-risk table).
5. **Is a "\+vF_q+v^2F_q ring" fabricated need?** No such ring is introduced; the ring is
   *derived* from the sync problem (two components with different orders is what produces
   $\mathrm{HA}>1$). The user's warning is respected.
6. **Is $q\to q^2$ used as decoration?** No: $\kappa=e/2$ is one special case of the twist
   condition Theorem 2, and its *consequence* (Theorem 12) is a parameter change.
7. **Is the contribution a mere combination?** It is a combination *plus* two new theorems
   (lcm law, decoupling) and a new object; the combination is the vehicle, not the claim.

**B. Mathematical correctness**

8. **Every definition precedes its use, no notation collisions.** Checked in PART F: the
   convention bridge $\kappa_{\text{ours}}=e-\kappa_{\text{source}}$ is stated explicitly;
   $T$, $L$, $N$, $K$, $d$, $c$ are reserved.
9. **All automorphisms proved well-defined.** Lemma F.1 (Frobenius on the CDR product);
   the twist $\lambda\mapsto\lambda^{p^\kappa}$ appears only inside Theorem 2 whose statement
   includes its own hypothesis.
10. **Characteristic/gcd assumptions stated and used.** A1–A4 of the assumptions ledger, each
    with the consequence of dropping it.
11. **No false strengthening.** The naive Claim A is recorded as *false* in F.3 with its
    counterexample, and the paper states only the verified pair (F.3, F.5).
12. **No fabricated numbers.** Every quantitative claim traces to
    `blueprint/verify/RESULTS.md` or is marked `[PARAMETER TABLE]`.
13. **No quantum code claimed without verified duality.** The flagship's
    $C^{\perp_H}\subseteq C$ was verified by linear algebra (dim 8 code in $\mathbb F_4^{14}$,
    dual containment checked exhaustively), and $d=3$ by exhaustive enumeration.
14. **Conjectures labelled as such.** PART G.14, PART F.6; the paper prints them in a
    separate subsection and the abstract does not mention them.
15. **Open problems labelled.** Four listed; none is used to support a claim.

**C. Verification and reproducibility**

16. **Computations verify mathematics, not decorate it.** Every script tests an implication
    or exhausts a claim; no script exists merely to print a table.
17. **Independent re-implementation.** The syndrome identity is computed twice by different
    algorithms (operator `T` in `verify_syndrome.py` vs polynomial reduction in
    `verify_mechanism.py`), and once more by hand on $\mathbb F_4$, $n=3$.
18. **Small cases for manual verification.** Four listed in I.4, plus the manual-check list
    in I.4's flagged paragraph.
19. **Negative results reported.** The false criterion (268/1010), the false naive containment
    strengthening, the divergence of the "both-degrees-$n$" form (344/742), the empty
    parameter sets (e.g. $\mathbb F_4$, $n=3$, $\lambda=\omega$).
20. **Runtime/portability.** All scripts pure Python except MAGMA replication; documented
    commands and versions.

**D. Presentation and venue fit**

21. **Q1-level contribution type.** New invariant + new theorem + new object + bounds, with
    an honest comparison table; not a table-only paper. Target venues: *Quantum Information
    Processing*, *IEEE Transactions on Information Theory*, *Physical Review A*, *Designs,
    Codes and Cryptography*, *Cryptography and Communications*, *Quantum Information &
    Computation*.
22. **Fabrication risk audit.** The blueprint contains: 0 invented references (groups A/B
    verified or classical; group C flagged), 0 invented numbers, 0 theorems without a status
    tag, 0 superiority claims without a completed search.
23. **Final self-check before submission.** (i) rerun the whole suite from a clean checkout;
    (ii) re-read every `[REQ-VERIFY]` line against the published PDFs; (iii) complete the
    prior-art search of item 4; (iv) fill every `[PARAMETER TABLE]`/`[FIGURE]`; (v) confirm
    the abstract's claims are exactly the paper's claims (no conjecture leaking into the
    abstract); (vi) confirm no theorem in the paper is stronger than the corresponding entry
    of the PART E ledger.

---

### Closing status of this blueprint

| Requirement of the brief | Where satisfied |
|---|---|
| PART A–Q in order with exact headers | this document |
| 14-item audit per source paper | PART B (13 papers) |
| 3–5 candidate directions, no ranking, evidence-based, one selected | PART D |
| ≥8 named theorems with statement/assumptions/strategy/lemmas/proof outline/verification plan | PART G (12 theorems + lemmas + conjectures) |
| quantum Singleton/defect, Hamming/GV/BCH-type bounds | PART F.6, PART G.11, G.14 |
| computational/MAGMA/Python plan with inputs, algorithms, dual/distance/quantum extraction | PART I |
| parameter search strategy | PART J |
| comparison table with the 11 required columns | PART K |
| 4 figures, 6 tables | PART L |
| full Q1 paper structure | PART M |
| 5 titles + one 150–200-word abstract, labelled PROVISIONAL | PART N |
| LaTeX blueprint with the required class/packages/environments | PART O (+ `PART_O_blueprint.tex`) |
| reference plan A/B/C | PART P |
| 23-item novelty/rigour audit | PART Q |
| blueprint only, no full paper | entire document (no section is written as manuscript prose) |


<!-- ===================== END BLUEPRINT.md ===================== -->


<!-- ===================== BEGIN PART_O_blueprint.tex ===================== -->

% =====================================================================
%  PART O --- LaTeX blueprint for the proposed paper.
%  This is a BLUEPRINT, not the paper: every statement is a placeholder
%  tagged with its epistemic status (see BLUEPRINT.md, PART E ledger).
%  Compile with pdflatex (no external figures required).
% =====================================================================
\documentclass[11pt]{article}

\usepackage{amsmath,amssymb,amsthm,mathtools,bm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{algorithm}
\usepackage{algpseudocode}
\usepackage[hidelinks]{hyperref}
\usepackage[margin=1in]{geometry}

% ---- theorem environments required by the brief ----
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
% auxiliary environments for conjectures / open problems (keep them visibly
% distinct from theorems in the final paper)
\theoremstyle{plain}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{openproblem}[theorem]{Open Problem}

% ---- notation macros ----
\newcommand{\Fq}{\mathbb{F}_q}
\newcommand{\Fqi}{\mathbb{F}_{q^{d_i}}}
\newcommand{\Aalg}{A}
\newcommand{\Rlam}{R_{\lambda}}
\newcommand{\hull}{\operatorname{hull}}
\newcommand{\ord}{\operatorname{ord}}
\newcommand{\lcm}{\operatorname{lcm}}
\newcommand{\perpsig}{^{\perp_{\sigma_\kappa}}}
\newcommand{\EAQSC}{\mathrm{EA\text{-}QSC}}
\newcommand{\amax}{a_{\mathrm{max}}}
\newcommand{\Tol}{T}
\newcommand{\Th}{\Theta}

\title{\textbf{Synchronization is independent of self-orthogonality:\\
Galois-hull quantum synchronizable codes over semisimple algebras}\\[4pt]
\large PROVISIONAL TITLE (four alternatives in the blueprint, PART N)}
\author{[AUTHORS TO BE DETERMINED]}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
\noindent
PROVISIONAL ABSTRACT (189 words; see \texttt{BLUEPRINT.md}, PART N.2).
Block synchronization and quantum error correction are usually built from the same
algebraic object, a dual-containing cyclic code. We show that the two requirements are
logically independent and exploit this separation inside the semisimple-algebra framework
of Galois-hull theory. For a unit $\lambda=\sum_i\lambda_ie_i$ of a semisimple
$\Fq$-algebra $\Aalg=\prod_i\Fqi$ and a chain $C\subseteq D$ of $\lambda$-constacyclic
$\Aalg$-linear codes, we prove that the receiver's window syndrome equals $x^{-a}$ in
$\Rlam/\langle f\rangle$ exactly, independently of the transmitted codeword, and that the
tolerance against misalignment is $\lcm_i\ord_{f_i}(x)-1$. This invariant is strictly
larger than any single component order and can exceed the block length, so the cyclic
ceiling $\Tol<n$ disappears. We characterize $\kappa$-Galois self-orthogonality by the
divisibility criterion $h^\tau\equiv0\bmod g$, which decouples tolerance from the hull and
yields entanglement-assisted quantum synchronizable codes $[[N+\Tol,K,d;c]]_Q$ with
$c=\dim\hull_\kappa$ and asymmetric twists per component. We add a tolerant Singleton bound
and a synchronization-defect functional, and accompany every structural claim with an
exhaustive, reproducible verification suite, including a computed family
$[[14+\Tol,2,3]]_2$ with $\Tol\le20>n=7$.
\end{abstract}

% =====================================================================
\section{Introduction}\label{sec:intro}
% PART M, section 1.  Structure to be written:
%  (i) the synchronization problem; (ii) the same-object assumption and why it was
%  never questioned; (iii) contributions C1--C4 of the blueprint (PART M);
%  (iv) relation to ring-based QSCs [REFERENCE: Liu--Liu 2021] and to
%  Galois-hull EAQECCs [REFERENCE: source paper], with the differentiation
%  stated in PART P (closest competitor: [REFERENCE: Zhang--Kong--Zheng, to verify]).

\section{Preliminaries}\label{sec:prelim}
% semisimple algebras and CRT; primitive idempotents; the convention bridge
% kappa_ours = e - kappa_source; the sigma_kappa-Galois inner product; lambda-constacyclic
% codes over A; hulls; Gray maps; the two channel models (H.2.1 / H.2.2).

\begin{definition}[componentwise Frobenius]\label{def:frob}
$\sigma_\kappa^{\Aalg}\colon\sum_i a_ie_i\longmapsto\sum_i a_i^{p^\kappa}e_i$.
\textnormal{[PROVED-HERE: well-defined $\Fq$-algebra automorphism; Lemma F.1]}
\end{definition}

\begin{definition}[$\kappa$-Galois inner product]\label{def:ip}
$\langle u,v\rangle_{\sigma_\kappa}:=\sum_{j}u_j\,\sigma_\kappa^{\Aalg}(v_j)\in\Aalg$.
\end{definition}

\begin{definition}[$\lambda$-constacyclic code over $\Aalg$]\label{def:constacyc}
A left ideal $C\trianglelefteq \Aalg[x]/\langle x^n-\lambda\rangle$.
\end{definition}

\begin{definition}[$\lambda$-periodic continuation and window]\label{def:pad}
$s_v(j):=\lambda^{-\lfloor j/n\rfloor}v_{j\bmod n}$;
$B_{a_l,a_r}(v):=(s_v(j))_{j=-a_l}^{n+a_r-1}$;
$W_a(v):=(s_v(a),\dots,s_v(a+n-1))$;
$\Tol:=a_l+a_r$.
\end{definition}

\section{Codes and Duality over $\Aalg$}\label{sec:duality}

\begin{theorem}[structure/decomposition]\label{thm:struct}
$\Rlam(\Aalg)\cong\prod_i R_{\lambda_i}(\Fqi)$, $C=\bigoplus_ie_iC_i$,
$\dim_{\Fq}C=\sum_id_i(n-\deg g_i)$.
\textnormal{[PROVED-HERE, write out; verified computationally]}
\end{theorem}

\begin{theorem}[twist condition]\label{thm:twist}
For a nontrivial $\lambda$-constacyclic code $C$ over $\Fq$: $C\perpsig$ is again
$\lambda$-constacyclic if and only if $\lambda^{p^\kappa+1}=1$.
\textnormal{[THEOREM TO BE PROVED; VERIFIED-COMPUTATIONALLY: 1010/1010]}
\end{theorem}

\begin{remark}[a false strengthening to avoid]\label{rem:nofalse}
``$\lambda^{p^\kappa+1}=1$ implies $C\perpsig\subseteq C$ for every $\lambda$-constacyclic
$C$'' is \emph{false} (counterexample: $q=8$, $n=7$, $\lambda=1$, $p^\kappa=4$,
$\deg g\in\{6,7\}$). Only Theorems~\ref{thm:twist} and~\ref{thm:contain} may be used.
\end{remark}

\begin{theorem}[generator of the twisted dual]\label{thm:dualgen}
With $h:=(x^n-\lambda)/g$ and $h^\tau:=x^{\deg h}h(1/x)^{\sigma_\kappa}$:
$C\perpsig=\langle h^\tau\rangle$.
\textnormal{[THEOREM TO BE PROVED; VERIFIED-COMPUTATIONALLY: 1010/1010 and 488/488]}
\end{theorem}

\begin{theorem}[self-orthogonality criterion, necessary and sufficient]\label{thm:contain}
Assume $\lambda^{p^\kappa+1}=1$. Then
$C\perpsig\subseteq C\iff h^\tau\equiv0\ (\mathrm{mod}\ g)
\iff h^\tau\in\langle g\rangle_{\Rlam}$.
\textnormal{[THEOREM TO BE PROVED; VERIFIED-COMPUTATIONALLY: 742/742 equivalent forms,
1010/1010 span form.  The rejected variants --- $\gcd(g,\mathrm{rev}(g^{p^{e-\kappa}}))=1$
and the both-degrees-$n$ divisibility --- are documented in the paper as counterexamples.]}
\end{theorem}

\begin{corollary}[rank/hull dimension]\label{cor:hull}
Closed-form expression for $\dim_{\Fq}\hull_{\sigma_\kappa}(C)$ in the mixed-weight CRT
case. \textnormal{[THEOREM TO BE PROVED; target formula in PART F, Corollary F.6]}
\end{corollary}

\section{Synchronization Theory}\label{sec:sync}

\begin{lemma}[window = shifted codeword]\label{lem:window}
$W_a(v)=\mu_a\,\tau_\lambda^{-a}(v)$ with $\mu_a\in\Aalg^\times$ known to the receiver;
hence $W_a(v)\in D$ whenever $v\in D$.
\textnormal{[VERIFIED-COMPUTATIONALLY: 1262/1262]}
\end{lemma}

\begin{theorem}[window-syndrome identity]\label{thm:syndrome}
Let $C=\langle g_C\rangle\subseteq D=\langle g_D\rangle$ be $\lambda$-constacyclic
$\Aalg$-linear codes, $f=g_C/g_D$ with $\deg f>0$, and $J_a:=W_a(v)/g_D\in\Rlam$.
Then $J_a\bmod f=x^{-a}$ in $\Rlam/\langle f\rangle$, independently of $v\in D$;
the syndrome is content-free and needs no scalar correction.
\textnormal{[VERIFIED-COMPUTATIONALLY: 1262/1262 with an independent operator
$x^{-a}=T^{(-a)\bmod\ord_f}(1)$, $T=$ multiplication by $x$.}
\end{theorem}

\begin{theorem}[$\lcm$ tolerance law]\label{thm:lcm}
The syndromes are pairwise distinct on $[-a_l,a_r]$ iff
$a_l+a_r<\Th$, where $\Th:=\lcm_i\ord_{f_i}(x)$. Hence
(i) heterogeneity amplifies tolerance ($\Th>\max_i\ord_{f_i}$ possible),
(ii) $\Tol=\Th-1>n$ is possible, and (iii) $\Tol/L>1/2$ is attainable, whereas cyclic
$\mathrm{QSC}$s satisfy $\Tol<n=L-\Tol$.
\textnormal{[VERIFIED-COMPUTATIONALLY: ring case orders $(21,7)$ give $\Th=21$ with
21 distinct syndrome pairs and 0 collisions; $T/L=0.588$ at $L=34$.}
\end{theorem}

\begin{theorem}[jitter-tolerant synchronization]\label{thm:jitter}
If the misalignment reaches component $i$ with offset $a+\delta_i$,
$\delta_i\in\{0,\dots,\Delta\}$, then for every fixed offset vector the syndrome tuple is
still injective on windows of length $\Th$; the receiver recovers the global shift
$a\bmod\Th$ (not the individual $\delta_i$).
\textnormal{[partly VERIFIED-COMPUTATIONALLY: all offset vectors with $\Delta=1$; full
statement THEOREM TO BE PROVED.]}
\end{theorem}

\begin{theorem}[decoupling of synchronization and self-orthogonality]\label{thm:decouple}
Tolerance is a function of $(g_C,g_D,\lambda)$ alone; the quantum parameters are a function
of the Gram/hull data alone. Consequently entanglement assistance repairs the quantum layer
without changing $\Tol$.
\textnormal{[THEOREM TO BE PROVED; short.]}
\end{theorem}

\section{Quantum Constructions}\label{sec:quantum}

\begin{theorem}[QSC parameters]\label{thm:qsc}
$[[N+\Tol,K,d]]_Q$ with $K=2\dim\psi(C)-N$ and
$d\ge\min\{d(\psi(C)\setminus\psi(C)^{\perp_\kappa}),
d(\psi(C)^{\perp_\kappa}\setminus\psi(C))\}$.
\textnormal{[THEOREM TO BE PROVED; instances COMPUTATIONAL RESULT]}.
\end{theorem}

\begin{theorem}[entanglement-assisted QSC]\label{thm:eaqsc}
If $C\perpsig\not\subseteq C$ there is an $(a_l,a_r)$-$\EAQSC$
$[[N+\Tol,K,d;c]]_Q$ with $c=\dim_{\Fq}\hull_{\sigma_\kappa}(\psi(C))$ and $\Tol$ unchanged.
\textnormal{[THEOREM TO BE PROVED.]}
\end{theorem}

\begin{theorem}[asymmetric Galois twists]\label{thm:asym}
Per-component twists $(\kappa_1,\dots,\kappa_m)$ are admissible iff
$\lambda_i^{p^{\kappa_i}+1}=1$ for all $i$; tolerance is unaffected, whereas $K$ or $c$ can
improve. \textnormal{[THEOREM TO BE PROVED; corollary of Theorems~\ref{thm:contain},
\ref{thm:lcm}, \ref{thm:eaqsc}.]}
\end{theorem}

\begin{theorem}[designed distance]\label{thm:bch}
For BCH-type component generators, $d\ge\min_i\delta_i^{\mathrm{BCH}}$ up to the CSS
correction. \textnormal{[THEOREM TO BE PROVED.]}
\end{theorem}

\section{Bounds and Defect}\label{sec:bounds}

\begin{theorem}[tolerant Singleton bound and synchronization defect]\label{thm:singleton}
$K\le Q^{N+\Tol-2(d-1)-2c}$ and
$\delta_{\mathrm{sync}}:=N+\Tol-2\log_QK-2(d-1)\ge0$, additive over component chains.
\textnormal{[partly THEOREM TO BE PROVED, partly CONJECTURE --- flagged in the paper.]}
\end{theorem}

\begin{conjecture}[tolerant quantum Hamming]
The tolerant Hamming bound coincides with the plain Hamming bound on the padded block.
\end{conjecture}

\begin{conjecture}[entanglement-assisted Gilbert--Varshamov]
At fixed $\Tol/N$ and $q\to\infty$, random mixed-weight chains produce $\EAQSC$s approaching
the EA-Singleton rate.
\end{conjecture}

\begin{openproblem}[framing recovery]
Can a label/framing code on $\psi$ decide whether an insertion fell \emph{inside} an
$\Aalg$-symbol (the jitter problem of Theorem~\ref{thm:jitter})?
\end{openproblem}

\begin{openproblem}[repeated-root lengths]
Does the syndrome identity survive $p\mid n$?
\end{openproblem}

\section{Examples and Parameters}\label{sec:examples}
% Flagship (COMPUTATIONAL RESULT, exhaustive):
%   F_4, n = 7, lambda = (omega,1), kappa = 1 (Hermitian twist);
%   component codes [7,4,3]_4 containing their Hermitian duals;
%   psi(C) subset F_4^14, dim 8, Hermitian dual-containing, [[14,2,3]]_2;
%   lcm(ord_{f_1}, ord_{f_2}) = lcm(21,7) = 21 => T <= 20 > n = 7;
%   maximal length 34 qubits, T/L = 0.588.
\begin{table}[t]\centering
\caption{[PARAMETER TABLE] Code parameters per component (blueprint Table 3).}
\begin{tabular}{@{}lllll@{}}\toprule
component & $\lambda_i$ & factorization degrees / orders & $[n,k,d]_{q^{d_i}}$ &
dual-containing\\\midrule
\multicolumn{5}{c}{[to be filled from \texttt{verify/verify\_params.py} output]}\\\bottomrule
\end{tabular}
\end{table}

\begin{table}[t]\centering
\caption{[PARAMETER TABLE] Valid parameter sets and maximal $\Th$ (blueprint Table 4).}
\begin{tabular}{@{}lllll@{}}\toprule
$q$ & $n$ & admissible $\lambda$ & maximal $\Th$ & non-empty chains\\\midrule
\multicolumn{5}{c}{[to be filled]}\\\bottomrule
\end{tabular}
\end{table}

\begin{table}[t]\centering
\caption{[PARAMETER TABLE] Quantum codes with tolerance (blueprint Table 5).}
\begin{tabular}{@{}lllll@{}}\toprule
$[[N+\Tol,K,d;c]]_Q$ & $\Tol$ & $(a_l,a_r)$ & $\Tol/L$ & method for $d$\\\midrule
\multicolumn{5}{c}{[to be filled]}\\\bottomrule
\end{tabular}
\end{table}

\begin{figure}[t]\centering
\fbox{\parbox{0.9\textwidth}{\centering [FIGURE] Fig.\ 1: ring/algebra decomposition, the
idempotents $e_i$, the components $C_i$ and the orders $\ord_{f_i}$ joined by the lcm arrow.}}
\caption{Ring decomposition (blueprint Fig.~1).}
\end{figure}

\begin{figure}[t]\centering
\fbox{\parbox{0.9\textwidth}{\centering [FIGURE] Fig.\ 2: pipeline Finite ring/algebra
$\to$ classical $\lambda$-constacyclic chain $\to$ $\sigma_\kappa$-dual and hull $\to$
self-orthogonality/entanglement $\to$ tolerant block + CSS $\to$ $[[N+\Tol,K,d;c]]_Q$, with
the two independent rails (tolerance vs.\ quantum data) converging only at the end.}}
\caption{Construction pipeline (blueprint Fig.~2).}
\end{figure}

\begin{figure}[t]\centering
\fbox{\parbox{0.9\textwidth}{\centering [FIGURE] Fig.\ 3: computational workflow T1--T16
(blueprint PART I), each node annotated with the theorem it verifies.}}
\caption{Computational workflow (blueprint Fig.~3).}
\end{figure}

\begin{figure}[t]\centering
\fbox{\parbox{0.9\textwidth}{\centering [FIGURE] Fig.\ 4: $\Tol/L$ versus physical length for
cyclic QSCs, the $(\lambda(u+v)\mid u-v)$ family, and the mixed-weight family of this paper
(including $N=34$, $\Tol=20$, $\Tol/L=0.588$); second panel: heterogeneity amplification
$\mathrm{HA}=\Th/\max_i\ord_{f_i}$ versus $m$.}}
\caption{Parameter comparison (blueprint Fig.~4).}
\end{figure}

\section{Conclusion and Open Problems}\label{sec:conclusion}
% open problems 1--4 of the blueprint (PART G.14), plus the pre-submission checklist
% (PART Q item 23).

\appendix
\section{Proofs}\label{app:proofs}
\section{Reproducibility}\label{app:repro}
% commands, versions, raw outputs, manual-check list (blueprint PART I, I.4/I.5).
\section{Full Tables}\label{app:tables}

\begin{thebibliography}{99}
% No entry may be invented.  Group A/B of the blueprint PART P may be pasted here after
% the bibliographic details of group C are verified.
\bibitem{placeholder} [REFERENCES: see blueprint PART P --- groups A, B, C]
\end{thebibliography}

\end{document}


<!-- ===================== END PART_O_blueprint.tex ===================== -->


<!-- ===================== BEGIN verify/RESULTS.md ===================== -->

# Computational evidence log (`blueprint/verify/`)

All numbers quoted in the blueprint come from these scripts. Python 3, no external
mathematics dependency except for the tiny field/polynomial library `fflib*.py`
(written for this purpose; not imported from any solver). Reproduce with

```bash
cd blueprint/verify
/home/user/.venv-papers/bin/python -u verify_all.py        # structural claims A1/A2/A3/B/C
/home/user/.venv-papers/bin/python -u verify_mechanism.py  # window/syndrome sweep + flagship
/home/user/.venv-papers/bin/python -u verify_syndrome.py   # independent syndrome + CRT-lcm case
/home/user/.venv-papers/bin/python -u verify_params.py     # exact quantum parameters (brute force)
```

| # | Claim verified | Script | Scale | Outcome |
|---|---|---|---|---|
| A1 | For every unit λ ∈ F_q\* and every s = p^κ: the σ_s-dual of every nontrivial λ-constacyclic code is λ-constacyclic **iff** λ^{p^κ+1} = 1 | `verify_all.py` | 1010 tests, q ∈ {3,4,5,7,8,9}, n = 3..7, all λ, all κ | 0 failures |
| A2 | C^{⊥σ_s} = ⟨h^τ⟩ with h = (x^n − λ)/g and h^τ = x^l h(1/x)^{σ_s} | `verify_all.py`, `exp_dual2.py` | 1010 + 488 codes | 0 failures |
| A3 | C^{⊥σ_s} ⊆ C ⟺ h^τ ∈ ⟨g⟩_{R_λ} (membership computed by linear algebra, not by divisibility) | `verify_all.py` | 1010 tests | 0 failures |
| A3-neg | The *rejected* criterion gcd(g, rev(g^{p^{e−κ}})) = 1 is **not** equivalent to C^{⊥σ} ⊆ C | `verify_all.py` | 1010 tests | 268 disagreements — criterion rejected |
| B | ord_f(x) = r·h with h | n, r = ord(λ), gcd(r, n/h) = 1 | `verify_all.py` | 2000 tests | 0 failures |
| M1 | Window at misalignment a is a scalar multiple of the λ-constacyclic shift τ^{−a}(v) of the content word v ∈ C | `verify_mechanism.py` | 1262 configurations (all chains C ⊆ D with C, D dual-containing; q ∈ {2,3,4,5,7,8,9}, n = 3..7, all admissible λ and κ) | 0 failures |
| M2 | Receiver syndrome J = (window / g_D) mod f equals **exactly** x^{−a} ∈ R_λ/(f), independent of the content word | `verify_mechanism.py` (independent expected value) + `verify_syndrome.py` | 1262 + 12 individual instances incl. maximal windows | 0 failures; no scalar correction needed |
| M3 | Distinctness of syndromes ⟺ a_l + a_r < ord_f(x) | `verify_mechanism.py`, `verify_syndrome.py` | same sweeps | 0 failures |
| CRT | For a two-component algebra A = F_q × F_q the ring tolerance is lcm(ord_{f_1}, ord_{f_2}) | `verify_syndrome.py` | q = 4, n = 7, λ = (ω,1), orders (21,7): 21 shifts in [−10,10] | 21 distinct syndrome pairs, 0 collisions |
| CRT-jit | The lcm law is stable under unequal component offsets (a+δ_1, a+δ_2), δ_i ∈ {0,1} | `verify_params.py` companion check | orders (21,7) | injective on every window of length 21 |
| P1 | Flagship classical data (F_4, n = 7): x^7 − ω has factors of degree 1,3,3,4,4,6,7 with ord(x) = 3,21,21,21,21,21,21; the degree-3 factors give [7,4,3]_4 codes containing their Hermitian dual (dual code [7,4]_4, d = 4) | `verify_params.py` | exact | see blueprint Table 4 |
| P2 | Flagship ring code ψ(C) ⊆ F_4^{14}: dim 8, Hermitian dual-containing, quantum [[14, 2, 3]]_2 (distances by exhaustive search over all 4^8 codewords) | `verify_params.py` | exact | [14,2,3]_2 |
| P3 | Tolerance of the flagship ring example: lcm(21,7) = 21 ⇒ T ≤ 20 while the component block length is n = 7 (so T > n, and T/L = 0.588 at maximal length 34 qubits) | `verify_params.py`, `verify_mechanism.py` | exact | see blueprint Table 5 |

Refuted along the way (do **not** appear in the blueprint as true statements):

* "λ^{p^κ+1} = 1 ⇒ every λ-constacyclic code contains its σ_κ-dual" — false
  (`verify_core.py`: q = 8, n = 7, λ = 1, p^κ = 4, deg g ∈ {6,7}). The correct
  statement is A1 (the *dual* is λ-constacyclic) plus A3 (containment criterion).
* "gcd(g, rev(g^{p^{e−κ}})) = 1 ⟺ C^{⊥σ} ⊆ C" — false (268/1010).
* A first draft of the padding rule (no λ-twist in the periodic continuation,
  and a reversed x^{−1} operator in my own checker) produced spurious syndrome
  mismatches. Both errors were in the checker; the corrected rule and the
  corrected operator give M2 with multiplier exactly 1. The blueprint states the
  corrected rule only.


<!-- ===================== END verify/RESULTS.md ===================== -->
