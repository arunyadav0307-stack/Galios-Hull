# Phase 6 deliverable — Quantum construction theorem

**Status: this is a composition of published results, verified on this project's objects. It is NOT a
new theorem.** The blueprint asks for `QUANTUM_CONSTRUCTION_THEOREM.md` and also forbids presenting a
routine corollary as new. Both are honoured by stating it fully and labelling it.

From `4997773`.

---

## 1. Statement

**Theorem (Hermitian construction through the Gray map).**
Let `e \| (q+1)`, `M` any matrix over `F_{q²}` with `M M^* = ν I_e` and `ν ≠ 0`, and let
`C ⊂ R_e^n` be a `λ`-constacyclic code with `C^{⊥_H} ⊆ C`. Put `K := dim_F ψ(C)`. Then there exists a
quantum code over `F_q` with parameters

```
[[ en , 2K − en , ≥ d(ψ(C)) ]]_{q}.
```

*Proof (composition, every step cited).*
1. `ψ` is injective and `F`-linear (`M` invertible since `ν ≠ 0`), so `dim ψ(C) = dim C = K`.
2. `ψ(C^{⊥_H}) = ψ(C)^{⊥_H}` — source paper, Lemma 3 (p. 6), whose proof uses `M M^* = ν I_e` and
   `ν ≠ 0`.
3. Hence `C^{⊥_H} ⊆ C` gives `ψ(C)^{⊥_H} = ψ(C^{⊥_H}) ⊆ ψ(C)`, so `ψ(C)` is a Hermitian
   dual-containing `[en, K, d]_{q²}` code.
4. Lemma 17 of the source (Hermitian construction, citing [22]): a `[N, k, d]_{q²}` code with
   `C^{⊥_H} ⊆ C` yields `[[N, 2k − N, ≥ d]]_q`. Apply with `N = en`, `k = K`. ∎

This is exactly the source's Theorem 19 with the hypothesis made explicit. **No novelty.**

## 2. Field conventions — checked explicitly

The blueprint demands that the exact field convention, image length, dimension, distance bound and
dual-containing condition be verified. Each is checked against the data rather than asserted:

| Item | Convention | How verified |
|---|---|---|
| base field of the code | `F = F_{q²}` | all computations in `F_{q²}`; distances are Hamming over `F_{q²}` |
| field of the **quantum** code | `F_q`, **not** `F_{q²}` | Lemma 17 produces a code over `F_q`; the CSV labels it `[[·]]_q` |
| image length | `en` | CSV column `en`; equals `e * n` |
| image dimension | `K = dim_F ψ(C) = dim C` | **computed as rank of the explicit Gray image**, then compared with `Σ_ℓ dim C_ℓ`: agrees **504/504** rows |
| dual-containing of the image | `ψ(C)^{⊥_H} ⊆ ψ(C)` | follows from Lemma 3; the underlying ring code is dual-containing by the componentwise criterion (`DUAL_CONTAINING_ENUMERATION.md`) |
| distance | `d = d(ψ(C))`, **exact** | enumerated minimum weight of `ψ(C)`; CSV column `distance_exact` is `yes` for every row |

**The `≥` is real and is not slack we introduced.** The construction gives `≥ d`; because `d` here is
computed exactly, `≥ d` could be replaced by `= d`. The `≥` is retained to match the published form.

## 3. Hypotheses that are easy to get wrong (all handled)

| Trap | Handling |
|---|---|
| `ν = 0`, i.e. `M` singular | excluded; the paper's `e = 2` matrix has `ν = 2`, which is `0` in characteristic 2, so it is **rejected** over `F_4` and a different admissible `M` is used (`P3_3_RING_GRAY.md` §6) |
| `M` treated as canonical | `M` is a free parameter of the construction; every row of the CSV records the `M` used (L-3) |
| Gray distance assumed additive over components | false; `P3_3_RING_GRAY.md` Thm 5, and it is the whole content of the R4 direction |
| hull dimension assumed to determine distance | false; `P3_1_TABLES.md` §4 (C3, 5/5 instances) |
| quantum code confused with the classical `F_{q²}` code | the two are recorded in separate columns |

## 4. What this theorem does *not* give

* It does not bound `d` better than the exact enumeration; the bound `d ≥ min_ℓ d_ℓ` of
  `P3_3_RING_GRAY.md` Thm 2 is available independently of `M` and is the only convention-free
  statement.
* It says nothing about whether the resulting parameters are **good**. See
  `QUANTUM_PARAMETER_VERIFICATION.md` §4: at these lengths quantum-MDS is nearly automatic and the
  non-trivial subspace is small.
* It does not produce new codes. The source's own Section 5 tables remain the stronger parameter sets.

## 5. Classification

`K` (known or routine) — the composition is the source's Theorem 19. Its role here is to make the
distribution of `P3_4_QUANTUM_DISTRIBUTION.md` well founded and auditable, not to contribute a theorem.
