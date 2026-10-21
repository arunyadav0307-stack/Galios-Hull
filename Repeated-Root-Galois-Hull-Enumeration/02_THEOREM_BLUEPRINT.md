# Theorem Blueprint — Repeated-Root k-Galois Hull Enumeration
**Status:** Statements FIXED (Phase 0). Proofs Phase 3 me likhe jayenge; har proof obligation ko RR-number diya hai.
**Convention freeze:** Predecessor manuscript jaisi hi — code-first pairing, inverse-Frobenius reciprocal.
Sirf itna hoga, iske alawa koi chuppi (silent) convention-change nahi.

---

## 0. Notation (freeze)

- `p` prime; `q = p^e`, `e ≥ 1`; `0 ≤ k < e` (Galois index).
- `A ≅ ∏_{s=1}^N K_s`, `K_s = F_{q^{m_s}} = F_{p^{d_s}}`, `d_s = e m_s`. Component labels fixed.
- `σ(a) = a^{p^k}`, `ρ(a) = a^{p^{d_s−k}} = σ⁻¹` (component par; `s` aksar suppress).
- Code-first pairing: `⟨x,y⟩_{s,k} = Σ_i x_i σ(y_i)`; dual `D(C)`, hull `Hull_k(C) = C ∩ D(C)`.
- **Naya:** `ϱ ≥ 0`, `P = p^ϱ`, `n = P·n₀`, `gcd(n₀,p) = 1` (`ϱ = 0` ⟺ simple-root purana case).
- `λ = (λ_s) ∈ A*`, `M_s(x) = x^n − λ_s ∈ K_s[x]`.
- `μ_s ∈ K_s*`: `λ_s` ka ekmatra `P`-th root (Frobenius `a ↦ a^P` finite field ka bijection hai).
- `M̄_s(x) = x^{n₀} − μ_s`; `F_s` = uske distinct monic irreducible factors over `K_s`.
  To `M_s = M̄_s^P = ∏_{f∈F_s} f^P`.
- Exponent assignment: `a = (a_f)_{f∈F_s}`, `a_f ∈ {0,…,P}`; `g_a = ∏ f^{a_f}`; `C_s(a) = ⟨g_a⟩ ⊆ K_s[x]/(M_s)`.
- Reciprocal: `f#(x) = ρ(f₀)⁻¹ Σ_i ρ(f_i) x^{r−i}` (monic, degree-rakh rakhta hai) — purani paribhasha hi.
- Compatibility (har `s` par): **`λ_s^{1+p^{d_s−k}} = 1`** — tabhi `τ_s : F_s → F_s`, `τ_s(f) = f#` permutation hai.

---

## 1. Theorem statements (proof ki jimmedari ke saath)

### T1 — Parametrization (exponent assignments hi codes hain)
Har component code `C_s ⊆ K_s[x]/(M_s)` ka ekmatra monic generator `M_s` ka divisor hai, isliye
`a ↦ C_s(a)` ek bijection hai `{0,…,P}^{F_s} → {λ_s-constacyclic codes of length n over K_s}`.
CRT se global codes `A`-par `⟷` assignments ka product. Kul ginati `(P+1)^{Σ_s |F_s|}`.
*Proof:* `K_s[x]` PID hai; `(M_s)` ke upar ke ideals ⟷ monic divisors. Separable base ke distinct factors par exponent hi divisor tay karta hai. **[RR-1: routine, par non-semisimple quotient `(M_s)` me ideal-jali (lattice) saaf shabdon me likhna.]**

### T2 — Reciprocal, multiplicities ke saath; compatibility ka dohra roop
(i) `#` monic polynomials par multiplicative hai; isliye `(∏ f^{a_f})# = ∏ (f#)^{a_f}`.
(ii) Root action: `f(α)=0 ⟹ f#(α^{−p^{d_s−k}})=0` (purana lemma, bilkul waisa hi — multiplicity isse nahi badalti).
(iii) Compatibility ke samkaksh roop: `λ_s^{1+p^{d_s−k}}=1 ⟺ μ_s^{1+p^{d_s−k}}=1`.
*Proof of (iii):* `λ = μ^P` hai; `λ^{1+p^D}=1 ⟺ (μ^{1+p^D})^P=1`. Char-`p` field me `x^P=1 ⟹ (x−1)^P=0 ⟹ x=1`. ∎
Isiliye compatible case me `τ_s` separable base `M̄_s` ke factors ko permute karta hai (aur `M_s` ke factor-multisets ko bhi).
**[RR-2: (i) ka proof purani manuscript se uthega, par prime-power par multiplicativity alag se ek pankt me sabit karna — yahi is paper ki chhoti par asli takneeki chaabi hai.]**

### T3 — Code-first dual ke exponents
`h_a = M_s / g_a` rakho. To code-first dual `D(C_s(a)) = ⟨h_a#⟩` (twist `λ_s^{−p^{d_s−k}}`; compatible case me wahi `λ_s`).
Exponenton me: agar `τ_s`-orbit ko aise likhein `τ(f_i) = f_{i+1}` (indices mod `L`), `α_i = a_{f_i}`, to dual generator ka exponent
```
β_i = P − α_{i−1}        (har i par)
```
*Proof ki disha:* (a) Euclidean dual `⟨h*⟩` hai — purani reciprocal-lemma ka proof separability istemal **nahi** karta (sirf `g·h = x^n − λ` aur coefficient-pairing), isliye repeated-root par jyon ka tyon chalega; (b) code-first = coordinatewise `ρ` lagana, jo generator ko `#` me badalta hai; (c) exponents T2(i) se. **[RR-3: (a) ko bina idempotent/root-counting ke dobara likhna — yahi reviewer ka pehla sawaal hoga: "non-separable modulus me dual generator?" Iska jawab proof me sabse saaf jagah par.]**
**[RR-4: `ρ` lagane se twist `λ^{−p^{d_s−k}}` banta hai — purani hisaab-kitab, par `M_s = M̄_s^P` ke saath ek baar haath se jaanchna (prototype ne GF(4) par vector-level par yahi jaancha hai ✅).]**

### T4 — Hull ka generator aur dimension (paper ka dil)
Compatible case me `Hull_k(C_s(a)) = ⟨lcm(g_a, h_a#)⟩`, exponent `max(α_i, P − α_{i−1})` har factor par. Isiliye
```
dim_{F_q} Hull_{A,k}(C(a)) = Σ_s Σ_{O∈O_s} w_O · Σ_{i∈Z_L} min(P − α_i, α_{i−1}),
dim_{F_q} C(a)             = Σ_s Σ_{O∈O_s} w_O · Σ_{i∈Z_L} (P − α_i),
```
jahan `w_O = m_s · deg_{K_s}(f)` (orbit ke saare factors ka degree barabar — `τ` degree bachata hai).
*Proof:* Principal ideals ka intersection lcm se banta hai (T1 wali divisor-jali); dimension `= n − deg(generator)` component par, phir `m_s` se `F_q`-dimension. `P − max(u,v) = min(P−u, P−v)` wali pehchan aakhri kadam hai. **[RR-5: quotient ring `K_s[x]/(M_s)` me "ideals ka intersection = lcm ka ideal" — `M_s` non-squarefree hone par bhi satya hai kyunki upar wala ring (PID) me soch sakte hain; ek lemma me band karna.]**

### T5 — Local transfer trace
Ek orbit (`L`, `w`) ke liye `(P+1)×(P+1)` matrix `T = T^{(P)}_w(u,z)`, `T_{a,b} = u^{w(P−b)} z^{w·min(P−b,a)}` (kram: purba-awastha `a` → nayi `b`) ho, to
```
tr(T^L) = Σ_{α∈{0,…,P}^L} u^{w Σ_i (P−α_i)} z^{w Σ_i min(P−α_i, α_{i−1})}.
```
*Proof:* Band walk (closed walk) ka vistaar — diagonal condition cycle band karti hai; kenare (edge) ka bhaar T4 ke do yogdaano ko ek saath likhta hai. Purane `P=1` proof ka seedha vistaar. **[RR-6: routine.]**

### T6 — Global joint enumerator (MAIN THEOREM)
Upar ki hypotheses ke under,
```
E(u,z) := Σ_{labeled a} u^{dim_{F_q} C(a)} z^{dim_{F_q} Hull_k(C(a))}
        = ∏_{s=1}^N ∏_{O∈O_s} tr( T^{(P)}_{w_O}(u,z)^{L_O} ).
```
*Proof:* Components aur orbits par swatantrata (independence); T4 + T5 ka guna. `P=1` par purani main theorem ki recovery saath me dikhani hai. **[RR-7: routine — par ye paper ka mukhya vakya hai, isiliye hypotheses ek jagah gin kar.]**

### Corollaries (T6 ke vishesh roop)
- **C1 Total:** `E(1,1) = (P+1)^{Σ_s |F_s|}`.
- **C2 Code-dimension distribution:** `E(u,1) = ∏_s ∏_{f∈F_s} (1 + u^{w_f} + ⋯ + u^{P w_f})`, `w_f = m_s deg f`.
- **C3 LCD count:** `#{a : Hull = 0} = 2^{#orbits}`.
  *Proof ki chaabi:* ek orbit par `min(P−α_i, α_{i−1})=0 ∀i` hona ⟺ ya to saare `α_i=0` ya saare `α_i=P`.
  (Agar kahin `α_i=P` hai to agla bhi `P` — band cycle me saare `P`; agar `P` kahin nahi aur kahin `α_i∈{1,…,P−1}` hai to uske agle kenare par yogdaan `≥1`.) Dhyaan: ginati `P` se swatantra hai — ye chhota par sundar tathya alag se chamkana.
- **C4 Self-orthogonal / dual-containing kirdaar:** `C ⊆ D(C)` ⟺ har orbit-edge par `α_{i−1}+α_i ≥ P`; ginati `∏_O tr(B_P^{L_O})`, `(B_P)_{a,b} = 1` agar `a+b ≥ P` varna `0`. Ulta: `D(C) ⊆ C` ⟺ `α_{i−1}+α_i ≤ P` har edge par. (Dono T4 ke yogdaano ki tulna se — hull ka yogdaan code ke yogdaan ko edge-dar-edge (termwise) nahi paar kar sakta, isiliye vaishvik (global) barabari kenare-dar-kenare majboor karti hai.)
- **C5 Mean:** Uniform random labeled assignment par `E[dim C] = (n/2)·(Σ_s m_s)` (kul `F_q`-lambai ka aadha) aur
  `E[Hull] = [P(2P+1) / (6(P+1))] · Σ_O w_O L_O`.
  *Chaabi:* ek kenare par `min(P−α_i, α_{i−1})` do swatantra uniform `{0,…,P}` ka `min` hai; `E[min] = Σ_{t=1}^P ((P−t+1)/(P+1))² = P(2P+1)/(6(P+1))`. `P=1` par `1/4` — purana mean wapas. ✅
- **C6 Variance:** Orbit-swatantra yog; `L=1` (self-loop: `min(P−A,A)`), `L=2` (do kenare ek hi jodi ko saanjha karte hain), `L≥3` (sirf padosi kenare sah-sambandhit) — teeno cases ke band sutra (closed forms) Phase 4 me `P` ke parimaani (polynomial) roop me nikale jayenge. `P=1` par purana `a=2` wala exception iska sabse chhota roop hai. **[RR-8]**
- **C7 (shartiya) EAQECC:** Finite-field case (`N=1, m_1=1`) me jis code ka distance `d` jana ho, usse standard `[[n, K−H, d; n−K−H]]` EAQECC. Affine case me sirf tab, jab component distances se Gray/CRT distance pakka ho. **Enumerator akela quantum dawa nahi karega.** **[RR-9: is khand ko sabse aakhir me, sabse savdhaani se.]**

---

## 2. Layer-decomposition (Phase 4 ka vaikalpik hathiyaar — band sutro ke liye)
`α_i = Σ_{t=1}^P ε_i^{(t)}`, `ε_i^{(t)} = 1[α_i ≥ t]` (nested binary layers) likhne par
`min(P−α_i, α_{i−1}) = Σ_{t=1}^P ε_{i−1}^{(t)} (1 − ε_i^{(P−t+1)})`.
Yeh T5 ke trace ko `P` binary layers ke jode (pairing `t ↔ P−t+1`) me todta hai — one-orbit polynomial ke
band sutra aur variance ke closed form ke liye ye sabse ummeed bhara rasta hai. Zarurat pade tabhi kholenge;
main theorem iske bagair bhi khada hai.

## 3. Proof-dependency naksha
```
T1 (bijection) ──┬─► T3 (dual exponents) ──► T4 (hull formula) ──► T5 (trace) ──► T6 (enumerator) ──► C1–C6
T2 (reciprocal) ─┘            ▲                        ▲
Euclidean-dual lemma ─────────┘                        │
lcm-lemma (RR-5) ──────────────────────────────────────┘
```

## 4. Section architecture (manuscript, ~10 khand)
1. Introduction (gap: simple-root seema; L3/L4/L8 se imaandar doori) · 2. Preliminaries (freeze) ·
3. Repeated-root factorization aur exponent-parametrization (T1–T2) · 4. Galois dual (T3) ·
5. Hull formula (T4) · 6. Transfer matrix aur global enumerator (T5–T6) ·
7. Corollaries: ginatiyan, LCD, self-orthogonal, mean/variance (C1–C6) ·
8. Examples aur computational validation (prototype cases + ek do-component affine example) ·
9. Seemayein aur vistar (incompatible twist, non-reduced `A`, non-isometric ginati) · 10. Conclusion

## 5. Khule proof obligations — checklist
- [ ] RR-1 divisor-jali saaf shabdon me (non-semisimple quotient)
- [ ] RR-2 `#` ki prime-power multiplicativity
- [ ] RR-3 Euclidean-dual lemma bina separability ke (paper ka sabse nazuk proof)
- [ ] RR-4 twist-hisaab `M̄_s^P` ke saath haath se jaanch (prototype ✅ vector-level)
- [ ] RR-5 intersection = lcm lemma
- [ ] RR-6 band-walk vistaar
- [ ] RR-7 main theorem ki hypotheses ek jagah
- [ ] RR-8 variance ke teeno cases ke closed forms (parimaani pehchano se jaanch sahit)
- [ ] RR-9 EAQECC khand ki shartein (sirf jana-hua distance)
- [x] **Prototype:** GF(4), `k=1`, `n ∈ {6,10,14}` (`P=2`), `n=20` (`P=4`) — brute force = exponent formula = transfer trace, 206 assignments ✅ (`code/`)
- [ ] **Prototype-2 (Phase 2):** do-component affine example (`A = F₂ × F₄`, `k=0`) aur ek `p=3` case (`F₉`) — Sage/`galois` package se
