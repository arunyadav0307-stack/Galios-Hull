# SOURCE THEOREM REGISTER

**Source:** Yadav, Singh, Islam, Prakash, Solé, *Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes*, Comput. Appl. Math. **43**, art. 269 (2024), DOI `10.1007/s40314-024-02789-1`.
**Version examined (binding, E-3): `hal-04825601v1`** — HAL author/submitted deposit, 23 pp., SHA-256 `7f7e6803dffe8d42912c506cc0b6d8910187be169e14c869f3275d896c27d249`.
**Page convention:** `p.N` = **physical PDF page N**, i.e. file `source_audit/source_text/pages/page_NNN.txt`. The HAL cover page is p.1, so the journal's printed page = N − 1 throughout.
**Numbering:** all numbers below are the **HAL v1** numbers (Theorems 1–19, Lemmas 3/4/5/7/17, Corollaries 9/12/14, Examples 1–3). The publisher version numbers differently (Springer's abstract refers to "Corollaries 2 and 3" and "Theorems 8 and 9"); those numbers are **not** interchangeable with these.

> **Quotation policy.** The `Verbatim` field reproduces the text of the extracted corpus exactly as the extractor returned it, inside a code fence. The extractor flattens two-dimensional layout: fraction bars are lost (`phi(j)phi(r)ordj(q2)` is a quotient), `ε`/`⊥_H`/`Σ`/`Π` come out as `ϵ`, `⊥H`, `P`, `Q`, and superscripts lose their marker (`t4` = t⁴, `xn` = xⁿ). These artefacts are **not** corrected inside the quotation; the mathematical reading that the paper's own uses confirm is given in the `Conclusion` field and, where the reading matters, in `SOURCE_NOTATION_GLOSSARY.md`. No statement is paraphrased in the `Verbatim` field.

**Inherited global hypotheses** (apply to every entry and are not repeated in full): `p` is an odd prime, `q = p^m`, the base field is `F_{q²}`, `R_e = F_{q²} + uF_{q²} + … + u^{e−1}F_{q²}` with `u^e = 1` and `e | q+1`; for `R_2`, `ε₁ = γ(1+u)`, `ε₂ = γ(1−u)` with `2γ ≡ 1 (mod p)`; `α`, `α_l ∈ F*_{q²}` have orders `r`, `r_l` with `r | q+1`, `r_l | q+1`; `n = p^v n'` with `p ∤ n'`; `Ω`, `Ω'` (and `Ω_l`, `Ω'_l`) are as defined on p.8–9 / p.12; `γ(j)`, `β(j)` as on p.9.

---

## S1-T1 — Theorem 1

| Field | Value |
|---|---|
| Kind | theorem |
| Page | p.6 |
| Verbatim | `Theorem 1. Let C = ϵ1C1 ⊕ ϵ2C2 be a linear code of length n over R2. Then it is`<br>`a λ−constacyclic code over R2 for λ = ϵ1α1 + ϵ2α2 ∈ R∗2 if and only if C1, C2 are`<br>`α1−constacyclic and α2−constacyclic codes over Fq2, respectively.` |
| Hypotheses | `C = ε₁C₁ ⊕ ε₂C₂` with `C₁, C₂` linear over `F_{q²}` (as defined p.5); `λ = ε₁α₁ + ε₂α₂` must be a **unit** of `R₂` (i.e. `α₁α₂ ≠ 0`); inherited: `q` odd, `u² = 1`. |
| Conclusion | The ring-level λ-constacyclicity of `C` and the field-level α₁/α₂-constacyclicity of the two constituent codes are equivalent. |
| Proof method | idempotents (CRT) — direct computation with `ε_i ε_j = δ_ij ε_i`. |
| Classification | structural |
| Uses in this project | Justifies every construction that is built from two constituent polynomials (Examples 1–3, Tables 1–3). |
| Status | **VERIFIED** — proof re-read p.6; the idempotent algebra it uses was checked independently (audit item A1, `code/phase1_audit.py`). |

## S1-T2 — Theorem 2

| Field | Value |
|---|---|
| Kind | theorem |
| Page | p.6 |
| Verbatim | `Theorem 2. Let C be a λ−constacyclic code of length n over Re, where λ =Pe`<br>`i=1 ηiαi ∈ R∗e. Then there exists a unique monic polynomial g(x) ∈ Re[x] such that`<br>`C = ⟨g(x)⟩ for g(x) = Pei=1 ηigi(x) where gi(x)|xn − αi for 1 ≤ i ≤ e.` |
| Hypotheses | `λ = Σ η_l α_l ∈ R*_e` (all `α_l ≠ 0`); `C` λ-constacyclic of length `n` over `R_e`; inherited: `e | q+1`. |
| Conclusion | `C` has a unique monic generator `g = Σ η_l g_l` with `g_l | x^n − α_l` in `F_{q²}[x]`. |
| Proof method | idempotents / generator polynomials (proof not given in the paper; asserted as standard). |
| Classification | structural |
| Uses in this project | The "generator polynomial" encoding used by every table row; Tables 1–3 were re-derived from `g₁, g₂` on this basis. |
| Status | **VERIFIED** (statement); the paper gives no proof, and the uniqueness/monic claim is standard for principal ideal rings of this form. Verified operationally: in all 33 table rows the printed `g_i` divides the corresponding `x^n − α_i` (`code/phase1_tables.py`). |

## S1-L3 — Lemma 3

| Field | Value |
|---|---|
| Kind | lemma |
| Page | p.7 |
| Verbatim | `Lemma 3. Let C be a linear code of length n over Re and C ⊥H be the dual code of`<br>`C. Then ψ(C ⊥H ) = ψ(C)⊥H .` |
| Hypotheses | `C` linear of length `n` over `R_e`; `ψ` the Gray map of p.6 built from a square matrix `M` of order `e` with **`M M* = νI_e`, `ν ∈ F*_{q²}`** (p.7). The `ν ≠ 0` condition is essential to the proof. |
| Conclusion | The Gray map sends the Hermitian dual of `C` onto the Hermitian dual of `ψ(C)`. |
| Proof method | Gray map + inner-product computation, using `MM* = νI`. |
| Classification | Gray map / structural |
| Uses in this project | Underlies Lemma 4/5, Theorem 6, and hence the claim that hull dimensions transport to `ψ(C)` (Tables 1–3). |
| Status | **VERIFIED** — the identity `ψ(C^{⊥H}) = ψ(C)^{⊥H}` was checked numerically on three constructions (`code/phase1_audit.py`, A7), and `MM* = νI` was verified for `M`, `M(5)`, `M(11)` (`code/phase1_examples.py`). |

## S1-L4 — Lemma 4

| Field | Value |
|---|---|
| Kind | lemma |
| Page | p.7 |
| Verbatim | `Lemma 4.Let C be a self-orthogonal code with respect to the Hermitian inner product`<br>`over Re of length n. Then ψ(C) is a self-orthogonal code with respect to the`<br>`Hermitian inner product over Fq2 of length en.` |
| Hypotheses | `C ⊆ C^{⊥H}` over `R_e`; `ψ` as above with `MM* = νI`, `ν ≠ 0`. |
| Conclusion | `ψ(C)` is Hermitian self-orthogonal of length `en` over `F_{q²}`. |
| Proof method | Lemma 3 + injectivity of `ψ`. |
| Classification | Gray map |
| Uses in this project | none directly (self-orthogonality is not used in the tables); recorded for completeness. |
| Status | **QUOTED** — proof re-read p.7 and is correct given Lemma 3; not independently instantiated because no Phase-1 computation depends on it. |

## S1-L5 — Lemma 5

| Field | Value |
|---|---|
| Kind | lemma |
| Page | p.8 |
| Verbatim | `Lemma 5. Let C be a linear code over Re of length n. Then C is a self-dual code`<br>`with respect to the Hermitian inner product if and only if ψ(C) is a self-dual code with`<br>`respect to the Hermitian inner product.` |
| Hypotheses | `ψ` bijective linear (p.7) with `MM* = νI`, `ν ≠ 0`. |
| Conclusion | Self-duality over `R_e` ⟺ self-duality of the Gray image over `F_{q²}`. |
| Proof method | Lemma 3 + bijectivity. |
| Classification | Gray map |
| Uses in this project | none directly. |
| Status | **QUOTED** — proof re-read p.8, correct given Lemma 3. |

## S1-T6 — Theorem 6

| Field | Value |
|---|---|
| Kind | theorem |
| Page | p.8 |
| Verbatim | `Theorem 6. Let C be a linear code over Re of length n. Then C is a Hermitian LCD`<br>`code if and only if ψ(C) is a Hermitian LCD code over Fq2.` |
| Hypotheses | `ψ` as above. |
| Conclusion | Hermitian-LCD-ness is preserved both ways by `ψ`. |
| Proof method | "It can be proved by following the steps of Theorem 6.2 in [32]." — **no proof given**. |
| Classification | LCD / Gray map |
| Uses in this project | The bridge that lets a hull statement about `R_e`-codes be tested on `ψ(C)`; used implicitly by every Table-1/2 hull claim, all of which were re-derived directly on `ψ(C)`. |
| Status | **VERIFIED** (operationally) — the paper's own argument is a reference, but the conclusion was confirmed on all 33 table rows by computing `hull(ψ(C))` directly and comparing with the sum of the constituent hull dimensions (`code/phase1_tables.py`, `code/phase1_audit.py` A7). |

## S1-L7 — Lemma 7

| Field | Value |
|---|---|
| Kind | lemma |
| Page | p.9 (statement), pp.9–10 (proof) |
| Verbatim | `Lemma 7. For any positive integer v and 0 ≤ a, b, c≤ pv, we have the following:`<br>`1. 0 ≤ pv − max{a, pv − a} ≤j pv2 k,`<br>`2. 0 ≤ 2pv − max{b, pv − c} −max{c, pv − b} ≤pv.` |
| Hypotheses | `v ≥ 1`, `0 ≤ a, b, c ≤ p^v`. |
| Conclusion | Two elementary range bounds on the quantities that recur in `dim Hull`. |
| Proof method | direct computation (two cases). |
| Classification | possible dimensions |
| Uses in this project | Supplies the bounds in Theorem 8/10 and the `⌊p^v/2⌋` in the dual-containing conditions. |
| Status | **VERIFIED** — both inequalities follow elementarily: (1) from `p^v/2 ≤ max{a, p^v−a} ≤ p^v`; (2) splits into the two cases the paper gives, and I re-checked both cases. |

## S1-T8 — Theorem 8

| Field | Value |
|---|---|
| Kind | theorem |
| Page | p.10 (statement), pp.10–11 (proof) |
| Verbatim | `Theorem 8. Let C = ϵ1C1 ⊕ ϵ2C2 be a λ−constacyclic code over R2, for some α−`<br>`constacyclic codes C1 = ⟨g1(x)⟩, C2 = ⟨g2(x)⟩ over Fq2, where λ = ϵ1α + ϵ2α for`<br>`α ∈ F∗q2 … Then, the dimension of Hull H (C) is of the form`<br>`X j∈Ω ordj(q2)aj + X j∈Ω′ ordj(q2)bj,`<br>`where 0 ≤ aj ≤ 2γ(j) j pv 2 k and 0 ≤ bj ≤ 2β(j)pv.` |
| Hypotheses | `C = ε₁C₁ ⊕ ε₂C₂` λ-constacyclic with **`λ = ε₁α + ε₂α`, the same `α` in both components**; `g₁, g₂` decomposed over the `Ω/Ω'` factorisation with exponents `a_ij,b_ij,c_ij` (resp. `u_ij,v_ij,w_ij`), all in `[0, p^v]`. Inherited: `r | q+1`. |
| Conclusion | The Hermitian hull dimension is `Σ_{j∈Ω} ord_j(q²) a_j + Σ_{j∈Ω'} ord_j(q²) b_j` with `0 ≤ a_j ≤ 2γ(j)⌊p^v/2⌋`, `0 ≤ b_j ≤ 2β(j)p^v`. |
| Proof method | CRT decomposition + generator polynomial of the hull `lcm(g,((x^n−α)/g)^†)` + Lemma 7. |
| Classification | possible dimensions / hull |
| Uses in this project | The hull-dimension claims of Table 2 and the "hull dimension 1" of Example 1. |
| Status | **VERIFIED** — the `lcm` hull formula was checked against linear algebra on 220 sampled divisors, the full 4096-divisor enumeration of `x¹²−1/GF(25)` gives hull dimensions exactly `{0,1,2,3}` = `0…Σ_{j∈Ω'} ord_j β(j)`, and the bound `2·3 = 6` is attained by direct linear algebra (`code/phase1_audit.py` A4). |

## S1-C9 — Corollary 9

| Field | Value |
|---|---|
| Kind | corollary |
| Page | p.12 |
| Verbatim | `Corollary 9. If gcd(n, p) = 1 , then the dimension of the Hermitian hull of`<br>`constacyclic code given in the above theorem is`<br>`X j∈Ω′ ordj(q2)bj`<br>`where 0 ≤ bj ≤ 2β(j).` |
| Hypotheses | Theorem 8's hypotheses plus `gcd(n,p) = 1` (so `p^v = 1`). |
| Conclusion | When `p ∤ n` the `Ω`-part vanishes and the hull dimension is `Σ_{j∈Ω'} ord_j(q²) b_j`, `0 ≤ b_j ≤ 2β(j)`. |
| Proof method | specialisation of Theorem 8 at `p^v = 1` using `⌊1/2⌋ = 0`. |
| Classification | possible dimensions / hull |
| Uses in this project | Cited in Theorem 11/13's proof; the `n = 12, p = 5` instance was confirmed exhaustively. |
| Status | **VERIFIED** — `⌊p^v/2⌋ = ⌊1/2⌋ = 0` is correct, and the resulting bound `Σ ord_j β(j) = 3` is exactly the maximum observed over all 4096 divisors. |

## S1-T10 — Theorem 10

| Field | Value |
|---|---|
| Kind | theorem |
| Page | p.12 (statement), p.13 (conclusion) |
| Verbatim | `Theorem 10. Let C = η1C1 ⊕ η2C2 ⊕ · · · ⊕ηeCe be a λ−constacyclic code over Re for`<br>`some αl-constacyclic codes Cl = ⟨gl(x)⟩ over Fq2 where λ = η1α1 + η2α2 + · · ·+ ηeαe`<br>`… Then the dimension of Hull H (C) is of the form`<br>`eX l=1  X j∈Ωl ordj(q2)a(l)j + X j∈Ω′l ordj(q2)b(l)j`<br>`where 0 ≤ a(l)j ≤ γl(j) j pv2 k, 0 ≤ b(l)j ≤ βl(j)pv, for 1 ≤ l ≤ e.` |
| Hypotheses | λ = Σ η_l α_l with **possibly different `α_l`** (so `Ω_l, Ω'_l` are component-specific); inherited `e | q+1`, `r_l | q+1`. |
| Conclusion | Hull dimension is the sum over components of `Σ_{Ω_l} ord a + Σ_{Ω'_l} ord b`, with the per-component bounds stated. |
| Proof method | "general case of Theorem 8 … proved using similar arguments" (no separate proof). |
| Classification | possible dimensions / hull |
| Uses in this project | Example 3 (e = 3) and Table 3's e = 3 rows in principle; but Example 3 was verified directly, without invoking the theorem. |
| Status | **QUOTED** — statement read; not independently re-derived, because no Phase-1 claim rests on it (Example 3 was recomputed from scratch, not from Theorem 10). Note the per-component bounds here are `γ_l(j)⌊p^v/2⌋` and `β_l(j)p^v`, i.e. **half** the `2γ(j)`, `2β(j)` of Theorem 8: consistent, since Theorem 8's `a_j, b_j` already sum the two `R₂` components. |

## S1-T11 — Theorem 11

| Field | Value |
|---|---|
| Kind | theorem |
| Page | p.13 |
| Verbatim | `Theorem 11. Let gcd(n, p) = 1 and Dq2 (n) denotes the set of hull dimensions of`<br>`α−constacyclic codes of length n over R2 where α ∈ F∗q2 is an element of multiplicative`<br>`order r. Then Dq2 (n) = {0} if and only if nr ∈ Sq2 .` |
| Hypotheses | `gcd(n,p) = 1`; `α` of order `r`; `S_{q²} = {j ≥ 1 : j | (q^{2k}+q) for some k ≥ 0}` (defined p.13). **Reading note:** the printed `nr` is the product `n·r`, not a quotient — the proof speaks of "each divisor of `nr`" and of `n'r`, and the factorisation of `x^n − α` is indexed by divisors of `n'r`. |
| Conclusion | Every α-constacyclic code of length `n` over `R₂` has hull dimension 0 iff `n·r ∈ S_{q²}`. |
| Proof method | Corollary 9 + the definition of `π` / `Ω'`. |
| Classification | LCD |
| Uses in this project | The Hermitian-LCD claims of Table 1 (all 7 rows re-derived independently, hull = 0). |
| Status | **VERIFIED** — the iff was tested on four `(n,r)` cases over `GF(25)` and held in all four (`code/phase1_audit.py` A5): `(6,1)` → `6 ∈ S` and hull dims `{0}`; `(12,1)`, `(14,2)`, `(6,2)` → `n·r ∉ S` and hull dimensions other than 0 occur. |

## S1-C12 — Corollary 12

| Field | Value |
|---|---|
| Kind | corollary |
| Page | p.13 |
| Verbatim | `Corollary 12. Let gcd(n, p) = 1 and α ∈ F∗q2 be an element of multiplicative order r.`<br>`Then every α−constacyclic code of length n over R2 is a Hermitian LCD code if and`<br>`only if nr ∈ Sq2 .` |
| Hypotheses | as Theorem 11. |
| Conclusion | The LCD property is uniform over all α-constacyclic codes of length `n` exactly when `n·r ∈ S_{q²}`. |
| Proof method | restatement of Theorem 11 ("From the above theorem, we can conclude…"). |
| Classification | LCD |
| Uses in this project | Table 1's title claim (Hermitian LCD codes) insofar as it is a uniform statement. |
| Status | **VERIFIED** — identical content to Theorem 11, whose iff was tested. |

## S1-T13 — Theorem 13

| Field | Value |
|---|---|
| Kind | theorem |
| Page | p.13 |
| Verbatim | `Theorem 13. Let gcd(n, p) = 1 and Dq2 (n) denotes the set of hull dimensions of`<br>`α−constacyclic codes of length n over Re where α ∈ F∗q2 is an element of multiplicative`<br>`order r. Then Dq2 (n) = {0} if and only if nr ∈ Sq2 .` |
| Hypotheses | as Theorem 11 but over `R_e`. |
| Conclusion | The `R_e` analogue of Theorem 11. |
| Proof method | stated without proof ("Similarly, we can obtain the following results"). |
| Classification | LCD |
| Uses in this project | none (Phase 1 verified only `R₂` cases). |
| Status | **QUOTED** — no proof in the source; not instantiated. Recorded as a gap, not a defect. |

## S1-C14 — Corollary 14

| Field | Value |
|---|---|
| Kind | corollary |
| Page | p.13 |
| Verbatim | `Corollary 14. Let gcd(n, p) = 1 and α ∈ F∗q2 be an element of multiplicative order r.`<br>`Then every α−constacyclic code of length n over Re is a Hermitian LCD code if and`<br>`only if nr ∈ Sq2 .` |
| Hypotheses | as Theorem 13. |
| Conclusion | Uniform LCD criterion over `R_e`. |
| Proof method | none given. |
| Classification | LCD |
| Uses in this project | none. |
| Status | **QUOTED** — as Theorem 13. |

## S1-T15 — Theorem 15

| Field | Value |
|---|---|
| Kind | theorem |
| Page | p.13 (statement begins), p.14 (conditions and proof) |
| Verbatim | `Theorem 15. Let C = ϵ1C1 ⊕ ϵ2C2 be a λ−constacyclic code over R2 for some`<br>`constacyclic codes C1 = ⟨g1(x)⟩, C2 = ⟨g2(x)⟩ over Fq2 where λ = ϵ1α1 + ϵ2α2 for`<br>`α1, α2 ∈ F∗q2 … Then C ⊥H ⊆ C if and only if 0 ≤ aij, uij ≤ j pv2 k and 0 ≤ bij + cij, vij + wij ≤ pv.` |
| Hypotheses | `C = ε₁C₁ ⊕ ε₂C₂` λ-constacyclic; `g_i` written with exponents `a_ij` (self-CR factors, `Ω_i`), `b_ij`/`c_ij` (the two members of each CR pair, `Ω'_i`) for `C₁`, and `u_ij`/`v_ij`/`w_ij` for `C₂`; inherited `r_i | q+1`. |
| Conclusion | `C^{⊥H} ⊆ C` iff each self-CR exponent is `≤ ⌊p^v/2⌋` and each CR-pair total `b_ij + c_ij ≤ p^v`. |
| Proof method | generator polynomial of the hull + `lcm(g, ((x^n−α)/g)^†) = ((x^n−α)/g)^†`. |
| Classification | dual-containing |
| Uses in this project | Justifies applying the Hermitian construction to every Table-3 row and to Examples 2–3. |
| Status | **VERIFIED** — all 14 Table-3 rows are independently dual-containing, and the violating configuration (both members of one CR pair, i.e. `b+c = 2 > p^v = 1`) is confirmed **not** dual-containing (`code/phase1_audit.py` A6, Example 2 parameters). |

## S1-T16 — Theorem 16

| Field | Value |
|---|---|
| Kind | theorem |
| Page | p.14 |
| Verbatim | `Theorem 16. Let C = η1C1 ⊕η2C2 ⊕· · ·⊕ηeCe be a λ−constacyclic code over Re, for`<br>`some αl-constacyclic codes Cl = ⟨gl(x)⟩ over Fq2, where λ = η1α1 + η2α2 + · · ·+ ηeαe`<br>`… Then C ⊥H ⊆ C if and only if 0 ≤ a(l)ij ≤ j pv2 k and 0 ≤ b(l)ij +c(l)ij ≤ pv, for all 1 ≤ l ≤ e.` |
| Hypotheses | as Theorem 15, component-wise for `1 ≤ l ≤ e`. |
| Conclusion | `R_e` analogue of the dual-containing criterion. |
| Proof method | "Analogues to this result" (no proof). |
| Classification | dual-containing |
| Uses in this project | Example 3 (e = 3) invokes it; Example 3 was nevertheless verified directly (all three constituents dual-containing, `code/phase1_examples.py`). |
| Status | **VERIFIED** (operationally for e = 3) — the three constituents of Example 3 are dual-containing, as the theorem requires; the e ≥ 4 generality is **QUOTED**. |

## S1-L17 — Lemma 17 (Hermitian construction, quoted from [22])

| Field | Value |
|---|---|
| Kind | lemma |
| Page | p.14 |
| Verbatim | `Lemma 17. [22, Hermitian construction] Let C be a linear code over Fq2 with`<br>`the parameters [n, k, d]q such that C ⊥H ⊆ C. Then there exists a quantum code of`<br>`parameters [[n, 2k − n, ≥ d]]q.` |
| Hypotheses | `C` linear over `F_{q²}`, `C^{⊥H} ⊆ C`, parameters `[n,k,d]_q`. |
| Conclusion | A quantum code `[[n, 2k−n, ≥d]]_q` exists. |
| Proof method | imported result (reference [22]). |
| Classification | quantum parameters |
| Uses in this project | The quantum parameters in Table 3 and in Examples 2–3; the `2k−n` column was recomputed for every row. |
| Status | **VERIFIED** (as applied) — the formula `2k − en` reproduces all 14 Table-3 quantum dimensions and all three examples; the external reference [22] itself is outside Phase 1. |

## S1-T18 — Theorem 18

| Field | Value |
|---|---|
| Kind | theorem |
| Page | p.14 |
| Verbatim | `Theorem 18. Let C be a linear code over R2 such that C ⊥H ⊆ C and the parameters`<br>`of ψ(C) be [2n, k, d]q. Then there exists a quantum code of parameters [[2n, 2k − 2n, ≥`<br>`d]]q.` |
| Hypotheses | `C` linear over `R₂`, `C^{⊥H} ⊆ C`, `ψ(C)` is `[2n,k,d]_q`. |
| Conclusion | Quantum code `[[2n, 2k−2n, ≥d]]_q`. |
| Proof method | Lemma 3 + Lemma 17. |
| Classification | quantum parameters |
| Uses in this project | Table-3 rows with `e = 2`. |
| Status | **VERIFIED** — proof re-read p.14–15 and is valid; instantiated in all e = 2 Table-3 rows. |

## S1-T19 — Theorem 19

| Field | Value |
|---|---|
| Kind | theorem |
| Page | p.15 |
| Verbatim | `Theorem 19. Let C be a linear code over Re such that C ⊥H ⊆ C and the parameters`<br>`of ψ(C) be [en, k, d]q. Then there exists a quantum code of parameters [[en, 2k − en, ≥`<br>`d]]q.` |
| Hypotheses | as Theorem 18 with `2n` replaced by `en`. |
| Conclusion | Quantum code `[[en, 2k−en, ≥d]]_q`. |
| Proof method | Lemma 3 + Lemma 17. |
| Classification | quantum parameters |
| Uses in this project | Example 3. |
| Status | **VERIFIED** — proof read p.15; Example 3 instantiated it (`[[18,10,≥4]]₅`). |

## S1-EX1 — Example 1

| Field | Value |
|---|---|
| Kind | example |
| Page | pp.15–16 |
| Verbatim | `Example 1.Consider α = 1, n = 12 and q = p = 5, then the order of α is r = 1, n′ =`<br>`12, and pv = 1. Further, ord j(q2) = 1 ∀j ∈ Ω∪Ω′, where Ω = {1, 2, 3, 6}, Ω′ = {4, 12}.`<br>`Also, γ(1) = 1, γ(2) = 1, γ(3) = 2, γ(6) = 2, β(4) = 1 and β(12) = 2.` |
| Hypotheses | `q = p = 5`, `α = 1`, `n = 12`, `r = 1`, `p^v = 1`; `R₂` over `GF(25)`. |
| Conclusion | `x¹²−1` factors into 6 self-CR polynomials and 3 CR pairs; `C₁ = ⟨x³+x²+t⁸x+t⁸⟩` has hull 0, `C₂ = ⟨x+t²⟩` hull 1, `ψ(C)` is `[24,20,4]_{5²}` with hull 1, and the `g'` variant is a Hermitian LCD `[24,20,4]_{5²}` code. |
| Proof method | direct computation (Magma, per p.15). |
| Classification | LCD / hull / Gray map |
| Uses in this project | Reference construction for Phase 1 recalculation. |
| Status | **VERIFIED** — every number in the example was recomputed exactly (`code/phase1_examples.py`); see `SOURCE_EXAMPLE_RECALCULATION.md`. |

## S1-EX2 — Example 2

| Field | Value |
|---|---|
| Kind | example |
| Page | p.16 |
| Verbatim | `Example 2. Consider α = 12, n = 14 and q = p = 13, then the order of α is r = 2,`<br>`n′ = 14, and pv = 1. Further, ord j(q2) = 1 ∀j ∈ Ω ∪ Ω′, where Ω = φ, Ω′ = {4, 28}.`<br>`Also, β(4) = 1 and β(28) = 6 .` |
| Hypotheses | `q = p = 13`, `α = 12` (order 2), `n = 14`, `p^v = 1`; `R₂` over `GF(169)`. |
| Conclusion | 7 CR pairs; `C₁ = ⟨x²+t²¹x+1⟩`, `C₂ = ⟨x+t⁶⟩` are dual-containing; `ψ(C)` is `[28,25,4]_{13²}` and the quantum code is `[[28,22,≥4]]₁₃`, MDS. |
| Proof method | direct computation (Magma). |
| Classification | dual-containing / Gray map / quantum parameters |
| Uses in this project | The MDS reference point (quantum Singleton residual 0). |
| Status | **VERIFIED** — all numbers recomputed exactly, including the exact minimum distance 4 and the MDS residual 0. |

## S1-EX3 — Example 3

| Field | Value |
|---|---|
| Kind | example |
| Page | pp.16–17 |
| Verbatim | `Example 3. Consider α = 4 , n = 6 and q = p = 5 , then the order of α is r = 2 ,`<br>`n′ = 6, and pv = 1. Further, ord j(q2) = 1 ∀j ∈ Ω ∪ Ω′, where Ω = φ, Ω′ = {4, 12}.`<br>`Also, β(4) = 1 and β(12) = 2.` |
| Hypotheses | `q = p = 5`, `α = 4` (order 2), `n = 6`, `p^v = 1`, `e = 3`; `η₁ = (u+4)(u+t²⁰)`, `η₂ = (u+t⁴)(u+t²⁰)`, `η₃ = (u+t⁴)(u+4)`. |
| Conclusion | `ψ(C)` is `[18,14,4]_{5²}` and the quantum code is `[[18,10,≥4]]₅`, near-MDS. |
| Proof method | direct computation (Magma). |
| Classification | dual-containing / Gray map / quantum parameters |
| Uses in this project | The `e = 3` reference construction (uses `M(5)`). |
| Status | **VERIFIED** — recomputed exactly, including the `e = 3` Gray matrix `M(5)` and exact distance 4. The printed `η_i` are unnormalised (see `SOURCE_MATHEMATICAL_AUDIT.md` item 2); this does not affect the code. |

## S1-TAB1 — Table 1

| Field | Value |
|---|---|
| Kind | table |
| Page | p.17 |
| Verbatim | `T able 1Hermitian LCD codes obtained fromλ−constacyclic codes over Re.`<br>`n λ g1(x), g2(x) ψ(C)` — 7 rows, e.g. `12 ϵ1 + ϵ2 x3 + x2 + t8x + t8, x+ t8 [24, 20, 4]52` |
| Hypotheses | `R₂` over `GF(5²)`, `GF(7²)`, `GF(11²)`, `GF(13²)` as indicated by the subscript; `t` a primitive element of that field; each row's `λ = aε₁ + bε₂`. |
| Conclusion | 7 Hermitian LCD `ψ(C)` codes, all `[24,20,4]` or `[60,57,3]`. |
| Proof method | direct computation (Magma). |
| Classification | LCD / Gray map |
| Uses in this project | Phase-1 verification target. |
| Status | **VERIFIED** — all 7 rows reproduced exactly (length, dimension, exact minimum distance, hull = 0). |

## S1-TAB2 — Table 2

| Field | Value |
|---|---|
| Kind | table |
| Page | p.18 |
| Verbatim | `T able 2λ−constacyclic codes with hull dimension 1 or 2.`<br>`n λ g1(x), g2(x) ψ(C) Hull dimension ofψ(C)` — 12 rows |
| Hypotheses | as Table 1, with the fifth column giving the hull dimension of `ψ(C)`. |
| Conclusion | 12 λ-constacyclic codes whose Gray images have hull dimension 1 or 2. |
| Proof method | direct computation (Magma). |
| Classification | hull / Gray map |
| Uses in this project | Phase-1 verification target. |
| Status | **VERIFIED** — all 12 rows reproduced exactly, including the fifth-column hull dimension (1 or 2 in every row, as tabulated). |

## S1-TAB3 — Table 3

| Field | Value |
|---|---|
| Kind | table |
| Page | p.19 |
| Verbatim | `T able 3Quantum codes obtained from Hermitian dual containingλ−constacyclic codes overRe.`<br>`n λ g1(x), g2(x) ψ(C) [[en, k,≥ d]]q en + 2− Remark / (k + 2d) Comparison` — 14 rows |
| Hypotheses | as Table 1; the fourth column is `ψ(C)`'s parameters, the fifth the quantum code, the sixth the quantum Singleton residual `en + 2 − (k + 2d)`. |
| Conclusion | 14 quantum codes, one of them MDS (`[[28,22,≥4]]₁₃`, residual 0) and the rest near-MDS or MDS-class. |
| Proof method | direct computation (Magma) + Theorem 19. |
| Classification | quantum parameters |
| Uses in this project | Phase-1 verification target; the residual column is the paper's own bookkeeping of the Singleton bound. |
| Status | **VERIFIED** — all 14 rows reproduced exactly: `[en,k,d]`, the dual-containing property, `[[en,2k−en,≥d]]`, and the residual `en+2−(k+2d)`. |

---

## Register summary

| Status | Count | Entries |
|---|---|---|
| VERIFIED | 20 | T1, T2, L3, T6, L7, T8, C9, T11, C12, T15, T16, L17, T18, T19, EX1, EX2, EX3, TAB1, TAB2, TAB3 |
| QUOTED | 5 | L4, L5, T10, T13, C14 |
| UNCLEAR | 0 | — |
| SUSPECT | 0 | — |

**Completeness check.** 19 numbered statements (Theorems 1–19 with Lemmas 3,4,5,7,17 and Corollaries 9,12,14 interleaved) + 3 examples + 3 tables = **25 entries**, all present.

**Heading-index reconciliation.** `HEADING_INDEX.csv` lists 24 heading lines for 19 distinct numbered statements plus the three examples. The one **low-confidence** line (`page 6, kind Theorem, number empty, "theorem."`) is a **false positive**: it is the end of the sentence "…the generator polynomial of a constacyclic code of length n over Re can be obtained by the next theorem." (p.6, line 30 of the corpus). It is **not** a statement and is not entered. Tables 1–3 are **absent** from `HEADING_INDEX.csv` because the extractor renders the caption as `T able 1` (space inside the word) and the deduplication pattern does not match; they were added by hand from pp.17–19.
