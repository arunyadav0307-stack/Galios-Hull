# Dr. Habibul Islam Sir — Field Guide
### Google Scholar profile se nikala gaya pura research map (20 Oct 2026 tak)

**Profile:** https://scholar.google.com/citations?user=UGe7NLAAAAAJ
**Sir:** Dr. Habibul Islam — Assistant Professor of Mathematics, IIIT Bhopal
**Pehchan:** PhD IIT Patna (2021, Prof. Om Prakash ke saath kaam), Post-Doc University of St. Gallen, Switzerland (Nov 2021 – Sept 2023), phir KIIT Bhubaneswar (2023–24), phir IIIT Bhopal (Oct 2024 – present)
**Metrics (Scholar, access date):** ~801 citations, h-index 19, i10-index 29
**Official research areas:** 1) Algebraic Coding Theory 2) Quantum Error-Correcting Codes 3) Code-Based Cryptography

> Ek line me field: **Finite fields/rings ke upar cyclic–constacyclic (aur skew/group) codes banao, unke dual aur hull ka dimension nikalo, aur usse LCD codes aur quantum (EAQECC) codes banao.**

---

## 1. Field ki kahani — ek hi pipeline har paper me ghumti hai

```
Finite field/ring chuno
   F_q,  Z4+uZ4+vZ4,  F_q[u,v,w]/<...>,  M2(Fp),  Galois ring,  affine algebra A
        |
Cyclic / Constacyclic / Skew code banao
   C = <g(x)>,  g(x) | x^n - lambda   (polynomial language)
        |
Dual nikalo (Euclidean / Hermitian / k-Galois inner product)
   <x,y>_k = sum_i x_i * y_i^(p^k)      (k=0 => Euclidean, beech wala k => Hermitian type)
        |
HULL nikalo:  hull_k(C) = C ∩ C^{⊥k}
   dim hull = 0  => LCD code
   C ⊆ C^⊥       => self-orthogonal (quantum CSS ke liye chahiye)
   C = C^⊥       => self-dual
        |
APPLICATION:
   (a) Quantum codes (CSS construction) — dual-containing chahiye
   (b) EAQECC (entanglement-assisted) — hull dimension hi entanglement "c" deta hai
   (c) LCD codes — cryptography / fault-tolerant computation me kaam
   (d) Hull bada => permutation-equivalence / automorphism algorithm mushkil
```

**Tumhe har paper me yahi 4 step dikhenge.** Sirf ring badalta hai, code-family badalti hai, ya inner product badalta hai. Yahi is "school" ka signature style hai.

---

## 2. Sir ke research ke 5 pillars (themes)

### Pillar A — Codes over rings (PhD era, 2017–2021, IIT Patna)
Sabse pehle ka kaam: field ko chhod ke **ajeeb rings** par cyclic/constacyclic codes.
- `Z4 + uZ4 + vZ4`, `Z4[u]/<u^k>`, `Fp[u,v,w]/<u^2-1, v^2-1, w^2-1, ...>` (non-chain rings)
- Skew cyclic / skew constacyclic codes (Frobenius automorphism twist ke saath)
- Additive codes, mixed alphabets (`Z4Z4[u]`, `ZpZp[u,v]`)
- Matrix rings tak gaye: cyclic codes over `M2(Fp)`, `M3(Fp)`, `M4(F2+uF2)`

### Pillar B — Quantum codes banana (sabse zyada cited kaam)
Classical code se CSS/EAQECC bana ke **naye [[n,k,d]] parameters** dena hi in papers ka result hota hai.
- Sabse cited paper: *Quantum codes from cyclic codes over Fp[u,v,w]/<u²-1,v²-1,w²-1,...>* (2019, ~62 citations)
- *New quantum codes from constacyclic and additive constacyclic codes*, Quantum Inf. Process. (2020, ~57 citations)

### Pillar C — LCD / Self-dual / Double-circulant codes
Hull = 0 wale codes (LCD) banana, khaaskar non-chain rings par.
- *Construction of LCD and new quantum codes from cyclic codes over a finite non-chain ring* (2022, ~37 citations)
- *Self-dual and LCD double circulant codes over a class of non-local rings* (2022, Sole ke saath)

### Pillar D — GALOIS HULLS (Post-doc St. Gallen ke baad ka main focus, 2022–2026) ⭐
Yahi abhi sabse garam (active) direction hai, aur **tumhara repo isi par hai**:
1. *Galois hulls of constacyclic codes over finite fields* — Cryptogr. Commun. 15 (2023) — hull dimension ka formula, `x^n - λ` ke factors ko arrange karke
2. *Galois hull dimensions of Gabidulin codes* — IEEE ITW 2023 (Horlemann ke saath) — rank-metric codes me hull; `e`-Galois self-dual Gabidulin codes even q ke liye bhi exist karte hain (Euclidean case me nahi karte!)
3. *Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes* — Comput. Appl. Math. 43 (2024)
4. *Study of small Galois hull dimensions of constacyclic codes* — Adv. Math. Commun. 22 (2026) — hull dimension 1 aur 2 wale codes, phir EAQECC
5. *Galois hulls of constacyclic codes over affine algebra rings* — Discrete Math. 349 (2026), Art. 114750 (Martinez-Moro ke saath) — ring `A = Fq[X1,...,Xl]/I`, CRT se fields me tod ke idempotent generators se hull

### Pillar E — Nayi directions (2025–2026, field broaden ho raha hai)
- *Dihedral quantum codes* — J. Algebra Appl. 24 (2025), Borello + Horlemann ke saath (group codes!)
- *Quantum codes from skew cyclic codes over mixed alphabets* — Comput. Appl. Math. 44 (2025)
- *Asymptotically good mixed-alphabet quasi-cyclic codes* — Comput. Appl. Math. 45 (2026) — sabse naya; ab sirf hull/quantum nahi, asymptotic goodness bhi

---

## 3. Co-author network (kiske saath kaam hota hai)

| Naam | Kaun hai | Rishta |
|---|---|---|
| **Om Prakash** (IIT Patna) | Professor | PhD supervisor — taqreeban har paper me saath |
| **Patrick Solé** (CNRS, France) | Senior coding theorist | Ring codes, LCD, self-dual |
| **Edgar Martínez-Moro** (Valladolid, Spain) | Algebraic codes / Groebner | Affine algebra paper |
| **Anna-Lena Horlemann** (St. Gallen) | Rank-metric codes | Post-doc mentor, Gabidulin + Dihedral |
| **Martino Borello** (Paris 8) | Group codes | Dihedral quantum codes |
| Shikha Patel, Shikha Yadav, R. K. Verma, Tushar Bag, Indibar Debnath, Dipak Bhunia, Ashutosh Singh | IIT Patna circle ke scholars | Co-authors rotation me |

Matlab: **IIT Patna (Om Prakash) school + European network (Solé, Martínez-Moro, Horlemann)** — dono ka mixture hai sir ka style.

---

## 4. Tumhare repo se connection (sabse important baat)

Tumhare repo (`Galios-Hull-*` zips) me jo manuscript hai —
*"Exact Joint Enumeration of k-Galois Hull Dimensions for Labeled Constacyclic Codes over Square-Free Affine Algebras"* —
wo ** seedha Pillar D ke paper #5 (Affine algebra rings, Discrete Math. 2026) ka follow-up hai**:

| | Sir ki paper (2026) | Tumhari manuscript |
|---|---|---|
| Sawal | Ek diye gaye code `C` ka hull dimension kitna hai? (formula) | **Saare** labeled codes me se kitno ka (code-dim, hull-dim) = (K, H) hai? (ginati/enumeration) |
| Jawab | Idempotent generator se hull generator + dimension formula | Bivariate generating polynomial `E(u,z) = ∏ ∏ tr(T_{w_O}(u,z)^{a_O})`, transfer-matrix trace |
| Phal (corollaries) | LCD condition, EAQECC examples | LCD count `2^(#orbits)`, mean `Σ a_O w_O/4`, variance (a=2 wala special term) |

Ye samajhna tumhare liye sabse zaroori hai: **sir "ek code ka hull" batate hain, tum "saare codes ka hull-distribution" gin rahe ho.** Interview/viva me sir yahi connection sabse pehle dekhenge.

Ek aur dhyaan wali baat jo tumhari manuscript khud note karti hai: sir ki paper me pairing ka convention (candidate-first) tumhare code-first convention se ulta hai, aur tumne `D_candidate = σ²(D_code-first)` transformation prove kiya hai. Ye detail sir ko impress karegi — dikhata hai tumne paper sach me padha hai, copy nahi kiya.

---

## 5. Field seekhne ka roadmap (kis order me padho)

### Level 0 — Prerequisites (2–3 hafte)
- Finite fields `Fq`, Frobenius `a -> a^p`, field extensions `F_{q^m}/F_q`
- Polynomial ring `Fq[x]`, `x^n - λ` ka factorization, cyclotomic cosets
- Rings: chain vs non-chain, Frobenius rings, Chinese Remainder Theorem (CRT)
- Linear codes: `[n,k,d]`, generator/parity-check, dual code

### Level 1 — Classical base (sir ki PhD-era papers se pehle ye aana chahiye)
- Cyclic codes = ideals of `Fq[x]/(x^n-1)`, generator polynomial
- Constacyclic: `x^n - λ`, negacyclic `λ = -1`
- Euclidean/Hermitian dual, reciprocal polynomial

### Level 2 — Sir ke core papers (isi order me)
1. *Galois hulls of constacyclic codes over finite fields* (2023) ← **sabse pehle ye**
2. *Cyclic codes over a non-chain ring R_{e,q} and their application to LCD codes*, Discrete Math. (2021)
3. *Construction of LCD and new quantum codes...* (2022)
4. *New quantum codes from constacyclic and additive constacyclic codes* (2020) — CSS construction samajhne ke liye

### Level 3 — Current frontier
5. *Galois hulls of constacyclic codes over affine algebra rings* (2026) ← tumhari base paper
6. *Study of small Galois hull dimensions* (2025/26)
7. *Galois hull dimensions of Gabidulin codes* (2023) — rank metric side
8. *Dihedral quantum codes* (2025) + *Asymptotically good mixed-alphabet quasi-cyclic codes* (2026) — nayi disha

### Level 4 — Quantum side ki theory
- CSS construction, stabilizer codes
- EAQECC: `[[n,k,d;c]]` — yahan `c` (entanglement) hull dimension se juda hai

---

## 6. Khule sawaal / aage ke kaam ke ideas (sir se baat karne layak)

1. **Repeated-root case:** Tumhari manuscript aur sir ki dono hi simple-root/square-free tak seemit hain (`gcd(n,p)=1`). `p | n` wala repeated-root enumeration abhi khula hai.
2. **Incompatible twist:** Jab `λ^{1+p^{d-k}} ≠ 1` ho, dual dusri family me chala jata hai — wahan enumeration nahi hua.
3. **Equivalence classes:** Abhi ginati labeled codes ki hai; isometry/equivalence classes ki ginati (Burnside-type) mushkil aur khuli hai.
4. **Distance/quantum parameters:** Hull enumerator se akele quantum distance nahi nikalta — distance ke saath joint enumeration agla bada kadam hoga.
5. **Code-based cryptography:** Sir ke homepage par teesra area likha hai, lekin publications me abhi ye sabse kam dikhta hai — ye ubharta hua gap hai, baat-cheet ke liye accha point.
6. **Group codes / Dihedral disha:** 2025 ke baad group-algebra codes me jaana nayi line hai — Gabidulin (rank-metric) ke saath ye doosri "post-hull" disha ban sakti hai.

---

## 7. Sources
- Google Scholar: https://scholar.google.com/citations?user=UGe7NLAAAAAJ
- IIIT Bhopal homepage: https://iiitbhopal.ac.in/Document/ff/Habibul%20Islam.html
- Affine algebra paper (arXiv): https://arxiv.org/html/2412.08512
- Gabidulin hulls (arXiv): https://arxiv.org/pdf/2211.05068
- ORCID: https://orcid.org/0000-0002-2196-1586

*Note: Citation counts Google Scholar ke hain aur samay ke saath badalte hain. Kuch 2026 papers abhi "Articles 1–20" list me saal ke hisaab se dikhe hain; journal volume/page final record se mila lena.*
