# Exact Joint Enumeration of k-Galois Hull Dimensions of Repeated-Root Constacyclic Codes over Square-Free Affine Algebras

**Status: IDEA FIXED — Phase 0 locked (20 Oct 2026)**
**Field:** Algebraic Coding Theory (Dr. Habibul Islam sir's line: Galois hulls → EAQECC)
**Predecessor manuscript:** *Exact Joint Enumeration of k‑Galois Hull Dimensions for Labeled Constacyclic Codes over Square-Free Affine Algebras* (simple-root case, `gcd(n,p)=1`, submission package Phase 10F in this repo)

---

## 1. The one-sentence paper

> Simple-root duniya me har irreducible factor ya to generator me "hai" ya "nahi" (binary choice) tha.
> Repeated-root duniya (`p | n`) me har factor ki **multiplicity** `a ∈ {0,1,…,P}` hoti hai.
> Is paper me hum saare multiplicity-assignments ko **code-dimension aur k-Galois hull-dimension ke saath jointly** ginte hain —
> ek `(P+1)`-state transfer matrix ke trace se — square-free affine algebra ke saare components par ek saath.

## 2. Central result (candidate main theorem — proof Phase 3 me pakka hoga)

Setup (purani manuscript wali hi notation freeze hai): `q = p^e`, `A ≅ ∏_{s=1}^N K_s`,
`K_s = F_{q^{m_s}} = F_{p^{d_s}}`, `d_s = e m_s`, `0 ≤ k < e`, code-first pairing
`⟨x,y⟩_{s,k} = Σ_i x_i y_i^{p^k}`.
**Naya:** `n = P·n₀`, `P = p^ϱ`, `ϱ ≥ 0`, `gcd(n₀,p) = 1`.
Har component me `μ_s` = `λ_s` ka ekmatra `P`-th root (finite field me Frobenius bijection hai),
`x^n − λ_s = (x^{n₀} − μ_s)^P`, aur `x^{n₀} − μ_s = ∏_{f∈F_s} f` (alag-alag irreducible factors).
Code ⟷ exponent assignment `a : F_s → {0,…,P}`, `g = ∏ f^{a_f}`.
Compatibility (purani wali hi): `λ_s^{1+p^{d_s−k}} = 1`, jisse reciprocal action `τ(f) = f^{#}` distinct factors ko permute karta hai.

Har `τ`-orbit `O = (f₀,…,f_{L−1})` (common degree, weight `w_O = m_s·deg f`) par exponent word
`α = (α₀,…,α_{L−1}) ∈ {0,…,P}^L` ke liye:

- **Code dimension** contribution: `w_O · Σ_i (P − α_i)`
- **Hull dimension** contribution: `w_O · Σ_i min(P − α_i, α_{i−1})` (cyclic indices)

Aur global joint enumerator:

```
E(u,z) = ∏_s ∏_O  tr( T^{(P)}_{w_O}(u,z)^{L_O} ),
T^{(P)}_w(u,z)_{a,b} = u^{w(P−b)} · z^{w·min(P−b, a)}      a,b ∈ {0,…,P}
```

Coefficient `[u^K z^H] E(u,z)` = un labeled codes ki exact ginati jinka global `F_q`-code-dimension `K`
aur global `F_q`-hull-dimension `H` hai.

**Sanity anchor:** `P = 1` rakhne par `T^{(1)}_w = [[u^w, 1],[u^w z^w, 1]]` — bilkul purani theorem. Nayi theorem purani ko nigalti hai, usse takrati nahi.

## 3. Headline corollaries (blueprint me statements taiyar)

| Corollary | Result |
|---|---|
| Total codes | `(P+1)^{Σ_s |F_s|}` |
| Code-dimension distribution | har factor par geometric factor `1 + u^{w_f} + … + u^{P w_f}` |
| LCD count | `2^{#τ-orbits}` (har orbit par sirf all-0 ya all-P assignment; `P` par nirbhar nahi!) |
| Self-orthogonal characterization | har orbit-edge par `α_{i−1} + α_i ≥ P`; ginati `∏ tr(B_P^{L_O})`, `B_{a,b}=1_{a+b≥P}` |
| Dual-containing characterization | har edge par `α_{i−1} + α_i ≤ P` |
| Mean hull dimension | `E[H] = [P(2P+1)/(6(P+1))] · Σ_O w_O L_O` |
| Variance | orbit-length `L=1, 2, ≥3` ke alag cases (purane `a=2` exception ka bada roop) |

## 4. Scope — kya claim NAHI karenge (purani manuscript wali imaandari)

- Ginati **labeled** exponent assignments ki hai; equivalence/isometry classes nahi.
- Sirf **compatible twists** (`λ_s^{1+p^{d_s−k}} = 1`). Incompatible case alag paper ka sawaal hai.
- `A` square-free hi rahega (components fields hain); non-reduced `A` is paper me nahi.
- Enumerator se akele **koi quantum distance claim nahi**. EAQECC sirf tab, jab kisi concrete code ka distance alag se jana ho.
- Koi "first / pehli baar" wala dawa nahi — jab tak Phase 1 ka full-text audit band na ho jaye.

## 5. Files

| File | Kya hai |
|---|---|
| `01_LITERATURE_AUDIT.md` | Preliminary literature audit: sabse qareebi papers, overlap matrix, novelty boundary, mandatory full-text checks |
| `02_THEOREM_BLUEPRINT.md` | Saare theorem statements, proof skeleton, proof obligations (RR-1…RR-9), section architecture |
| `03_RESEARCH_PLAN.md` | Phase-by-phase plan, timeline, decision gates, target journals |
| `code/validate_repeated_root.py` | Brute-force prototype: vector-space se hull nikal ke exponent-formula aur transfer-trace se milata hai |
| `code/validation_output.txt` | Prototype ka chala hua output (GF(4), k=1, P=2 aur P=4 cases) |

## 6. Prototype status (Phase 0 me hi verified ✅)

`GF(4)`, `k=1`, `λ=1` par 4 cases — `n=6, 10, 14` (`P=2`) aur `n=20` (`P=4`), kul 27+27+27+125 = 206 exponent assignments —
me teeno hisaab (brute-force vector hull / exponent formula / transfer trace) **bilkul barabar** aaye,
aur LCD count har case me `2^{#orbits}` mila. Matlab central formula ka dil sahi jagah par hai;
ab kaam hai use **prove** karna aur affine components par uthana.

## 7. Kaam kaise chalega — Commander/Worker vyavastha

- **ChatGPT = Commander** (plan, command, review) · **Arena AI = Worker** (repo me asal kaam) · **Tum = Boss** (dono ke beech message le jaana).
- ChatGPT ko shuru karne ke liye: **`CHATGPT_STARTER_PROMPT.md` ki poori file copy karke ChatGPT me paste kar do.**
- Command/Report ka format: `COMMAND_PROTOCOL.md` · Kaamo ki soochi: `TASK_QUEUE.md` · Roz ka hisaab: `ARENA_WORKLOG.md`
- Uske baad chal aisa hoga: ChatGPT command dega → tum yahan paste karoge → mai kaam karke REPORT dunga → tum woh report ChatGPT ko paste karoge → woh agli command dega.
