# New-paper blueprint: Galois-hull enumeration over square-free affine algebras

> **Language:** Hinglish + mathematical notation  
> **Base paper studied:** `Galois hulls of constacyclic codes over affine algebra rings` (the PDF supplied in this repository).  
> **Important:** This is a research blueprint, not a ready-to-submit manuscript. The novelty claim must be re-checked immediately before submission.

---

## 1. Sabse pehle: base paper kya karta hai, aur naya paper kis jagah se alag hoga?

### Base paper ka central contribution

The supplied paper essentially does the following:

1. Square-free affine algebra ring ko primitive idempotents/simple components me decompose karta hai.
2. Ring ke upar `lambda`-constacyclic codes ke `k`-Galois dual aur hull ke generators deta hai.
3. Factorization ke through ek formula deta hai jisse kisi **given code** ke hull dimension ko calculate kiya ja sakta hai.
4. Galois LCD conditions aur EAQECC examples deta hai.
5. Future direction ke roop me fixed hull dimension ke liye **non-isometric codes ki enumeration** ko open problem batata hai.

### Proposed paper ka genuinely naya question

> **Given `q, n, lambda, k` and a square-free affine algebra `A`, sirf possible hull dimensions nahi, balki har hull dimension par kitne codes hain, code-dimension aur hull-dimension ka joint distribution kya hai, average/variance kya hai, aur monomial-isometry ke modulo kitne inequivalent codes bachte hain?**

Iska matlab: base paper ka output mostly `dim(Hull(C))` hai; proposed paper ka output ek **enumerator / distribution / counting theorem** hoga.

### Recommended provisional title

**A Cycle-Index Method for Enumerating `k`-Galois Hulls of Separable Constacyclic Codes over Affine Algebras**

Alternative titles:

- **Joint Code–Hull Enumerators for Constacyclic Codes over Square-Free Affine Algebras**
- **Exact Distribution of Galois Hull Dimensions in Semisimple Affine-Algebra Codes**
- **Inequivalent Constacyclic Codes with Prescribed Galois Hull Dimension** — only if the Burnside/isometry phase is completed.

### One-line novelty statement

> We replace a code-by-code hull-dimension formula by a factor-orbit/cycle-index framework that gives the exact multiplicity of every `k`-Galois hull dimension, a bivariate code–hull enumerator, statistical moments, and—under a clearly defined isometry group—counts of inequivalent codes.

---

## 2. Novelty audit: kya claim nahi karna hai?

Submission se pehle literature ko dobara search karna compulsory hai. Quick audit se pata chalta hai ki:

- Galois hulls over affine algebra rings wala base work ab published version ke roop me bhi appear hota hai; preprint link: [arXiv:2412.08512](https://arxiv.org/html/2412.08512).
- `Average dimensions of Galois hulls of constacyclic codes` naam se finite fields aur `R_{m,q}` type ring par related average-dimension work available hai: [AIMS article](https://www.aimsciences.org//article/doi/10.3934/amc.2025010).
- Small Galois hull dimensions aur EAQECCs par bhi recent work available hai: [Study of small Galois hull dimensions](https://www.aimsciences.org/article/doi/10.3934/amc.2025054).
- New non-chain rings + Galois hulls + quantum constructions par 2026 work bhi milta hai: [Entropy/MDPI article](https://www.mdpi.com/1099-4300/28/4/407).

### Isliye novelty ko in cheezon par base mat karo

- “Humne ek aur ring par same hull formula nikala.”
- “Humne average hull dimension nikali.”
- “Humne kuch EAQECC tables banayi.”
- “Humne Galois dual/hull ka generator dobara likha.”

Ye sab akela weak ya already-covered lag sakta hai.

### Strong novelty package

Paper me kam se kam ye teen independent outputs hone chahiye:

1. **Exact multiplicity theorem:** `N_h = number of codes with q-dimension of hull equal to h`.
2. **Bivariate enumerator:** code dimension aur hull dimension dono ko ek saath count karna.
3. **Inequivalent-code count:** clearly defined monomial/isometry group ke modulo Burnside/cycle-index count; agar ye phase complete na ho to paper ka title “enumeration/distribution” rakhein, “inequivalent” nahi.

---

## 3. Scope ko manageable rakhne ke liye final mathematical setting

Main paper ke liye pehle **separable/simple-root regime** lo. Repeated-root case ko stretch goal rakho.

Let

\[
q=p^e,\qquad 0\le k<e,
\]

and

\[
A=\mathbb F_q[X_1,\ldots,X_\ell]
  /\langle t_1(X_1),\ldots,t_\ell(X_\ell)\rangle,
\]

where each `t_i` monic and square-free hai. Then finite commutative semisimple algebra ke roop me

\[
A\cong \prod_{s=1}^{N} K_s,
\qquad K_s\cong \mathbb F_{q^{m_s}}.
\]

Let

\[
\lambda=(\lambda_1,\ldots,\lambda_N)\in A^\times,
\qquad \lambda_s\in K_s^\times.
\]

Main theorem ke liye assume:

\[
\gcd(n,p)=1
\]

and the twist is compatible with the `k`-Galois dual:

\[
\lambda_s^{\,1+p^{e-k}}=1
\quad\text{for every }s.
\]

This compatibility ensure karegi ki dual/hull ko same constacyclic ambient algebra me factor-orbit language me handle kiya ja sake. Agar ye condition fail ho, to dual `lambda'`-constacyclic hota hai; us case ko separate extension paper/section banaya ja sakta hai.

For every component define

\[
R_s=K_s[x]/\langle x^n-\lambda_s\rangle.
\]

Because `gcd(n,p)=1`, `x^n-lambda_s` square-free hai. Let

\[
x^n-\lambda_s=\prod_{f\in\mathcal F_s}f(x)
\]

be its factorization into distinct monic irreducibles over `K_s`.

### Notation warning

`A` ke simple components generally `F_q` nahi, balki extension fields `K_s` hote hain. Isliye har component ke dimension ko `m_s=[K_s:F_q]` se multiply karna hoga. Source paper ki notation ko blindly copy na karein; proposed paper me `K_s` aur `m_s` explicitly define karna hai.

---

## 4. Core idea: factor selection ko binary cycle problem me badalna

For each irreducible factor `f`, a component constacyclic code is determined by choosing whether `f` generator polynomial me aayega ya nahi.

For `J_s\subseteq\mathcal F_s`, define

\[
g_{J_s}(x)=\prod_{f\in J_s}f(x),
\qquad
C_s(J_s)=\langle g_{J_s}(x)\rangle.
\]

Every ring code is a tuple

\[
C=(C_1(J_1),\ldots,C_N(J_N)).
\]

Thus code enumeration is a subset-enumeration problem.

### Galois factor permutation

The `k`-Galois reciprocal/Frobenius operation induces a permutation

\[
\tau_{s,k}:\mathcal F_s\longrightarrow\mathcal F_s.
\]

Paper me isko informal “reciprocal” kehne ke bajay precisely define karein: `tau_{s,k}(f)` woh irreducible factor hai jo coefficient-Frobenius plus reciprocal operation `f -> f_k^#` ke support ke roop me milta hai.

Let `O` be a cycle/orbit of `tau_{s,k}`:

\[
O=(f_0,f_1,\ldots,f_{a_O-1}),
\qquad \tau_{s,k}(f_i)=f_{i+1\pmod {a_O}}.
\]

All factors in one orbit have the same degree; write

\[
d_O=\deg_{K_s}(f_i),
\qquad w_O=m_s d_O.
\]

The weight `w_O` is the contribution in **F_q-dimension**.

For a chosen subset `J_s`, encode the orbit by a binary word

\[
\varepsilon_i=
\begin{cases}
1,& f_i\in J_s,\\
0,& f_i\notin J_s.
\end{cases}
\]

Define the number of directed `1 -> 0` boundaries

\[
b_O(J_s)=\#\{i\pmod {a_O}:\varepsilon_i=1,
\varepsilon_{i+1}=0\}.
\]

Orientation reverse hone par bhi count same rahega, isliye exact convention paper me ek baar fix karke use karein.

---

## 5. Proposed theorem package

Ye paper ka actual mathematical backbone hoga. Theorem numbers final draft me naye honge; source ke theorem numbers reuse nahi karne.

### Theorem 1 — CRT and code-factor classification

Prove:

\[
A[x]/\langle x^n-\lambda\rangle
\cong
\prod_{s=1}^{N}K_s[x]/\langle x^n-\lambda_s\rangle.
\]

Since every component polynomial square-free hai, every component ideal uniquely ek subset `J_s` se determined hai. Consequently,

\[
|\mathscr C(A,n,\lambda)|
=2^{\sum_s|\mathcal F_s|}.
\]

**Proof tasks:** CRT, componentwise ideals, unique generator selection.

### Theorem 2 — Hull dimension as a boundary statistic

For the code corresponding to `(J_1,...,J_N)`, prove

\[
\dim_{\mathbb F_q}\operatorname{Hull}_k(C)
=
\sum_{s=1}^{N}\sum_{O\in\mathcal O_s}
  w_O\, b_O(J_s).
\tag{H}
\]

The algebraic step is:

\[
\operatorname{Hull}_k(C_s)
=\langle \operatorname{lcm}(g_{J_s},h_{J_s,k}^{\#})\rangle,
\]

and the factors **not** appearing in this lcm are exactly

\[
(\mathcal F_s\setminus J_s)\cap \tau_{s,k}(J_s).
\]

On one `tau`-cycle, this set is exactly the set of `1 -> 0` boundaries. This turns the hull calculation into a cyclic binary-word calculation.

### Theorem 3 — Bivariate joint enumerator

Define

\[
\mathscr E(u,z)
=\sum_C
 u^{\dim_{\mathbb F_q}(C)}
 z^{\dim_{\mathbb F_q}(\operatorname{Hull}_k(C))}.
\]

For an orbit `O` of length `a_O` and weight `w_O`, set

\[
T_O(u,z)=
\begin{pmatrix}
1 & u^{w_O}\\
 z^{w_O} & u^{w_O}
\end{pmatrix}.
\]

Then prove the product formula

\[
\boxed{
\mathscr E(u,z)=
\prod_{s=1}^{N}\prod_{O\in\mathcal O_s}
\operatorname{tr}\big(T_O(u,z)^{a_O}\big).
}
\tag{E}
\]

Interpretation:

- `u` tracks the q-dimension of the classical code.
- `z` tracks the q-dimension of its Galois hull.
- The trace closes the binary word around the cycle.
- Product is valid because factor cycles/components are independent.

This is the main theorem that should distinguish the new paper from a code-by-code hull formula.

### Theorem 4 — Exact hull-dimension distribution

Put `u=1` in (E). For an orbit of length `a` and weight `w`, define

\[
P_{a,w}(z)=
\operatorname{tr}
\begin{pmatrix}
1&1\\ z^w&1
\end{pmatrix}^{a}.
\]

Then

\[
H_{A,n,\lambda,k}(z)
:=\sum_C z^{\dim_q\operatorname{Hull}_k(C)}
=\prod_{s,O}P_{a_O,w_O}(z).
\]

For `a>=1`, an explicit expansion is

\[
P_{a,w}(z)
=2+
\sum_{b=1}^{\lfloor a/2\rfloor}
 \frac{a}{b}\binom{a-1}{2b-1}z^{bw}.
\tag{P}
\]

Therefore, the exact number of codes with hull dimension `h` is

\[
\boxed{
N_h=[z^h]H_{A,n,\lambda,k}(z).
}
\]

The coefficient formula is the paper ka main enumerative answer.

### Theorem 5 — Statistical corollaries

Uniformly random constacyclic code ke liye:

\[
\mathbb E[\dim_q\operatorname{Hull}_k(C)]
=
\sum_{s,O:\,a_O\ge2}\frac{a_Ow_O}{4}.
\]

Variance:

\[
\operatorname{Var}(\dim_q\operatorname{Hull}_k(C))
=
\sum_{s,O:\,a_O=2}\frac{w_O^2}{4}
+
\sum_{s,O:\,a_O\ge3}\frac{a_Ow_O^2}{16}.
\]

The safest proof is generating-function differentiation. Direct random-variable proof optional hai.

Immediate corollary:

\[
\#\{C:\operatorname{Hull}_k(C)=0\}
=2^{\sum_s|\mathcal O_s|}.
\]

Yani compatible square-free regime me every factor cycle ke liye all-zero ya all-one selection choose karni hoti hai; isse exact LCD-code count milta hai.

### Optional Theorem 6 — Inequivalent-code enumeration

Agar non-isometric part complete karna ho, pehle equivalence group explicitly define karein:

\[
\Gamma_{A,n,\lambda,k}
=\{\phi:A^n\to A^n:
\phi \text{ is A-linear monomial},
\phi T_\lambda=T_\lambda\phi,
\langle\phi x,\phi y\rangle_k=\langle x,y\rangle_k\}.
\]

Here `T_lambda` is the constacyclic shift. Ye definition ensure karti hai ki code family aur hull dimension dono preserved rahen.

If `gamma` acts on factor selections, let

\[
\mathscr E_\gamma(u,z)
=\sum_{C:\gamma C=C}
 u^{\dim_q C}z^{\dim_q\operatorname{Hull}_k(C)}.
\]

Burnside se:

\[
\boxed{
N_h^{\mathrm{iso}}
=\frac1{|\Gamma|}
 \sum_{\gamma\in\Gamma}[z^h]\mathscr E_\gamma(1,z).
}
\]

**Caution:** Is theorem ko tabhi claim karein jab induced group action aur fixed-code enumerators rigorously derive ho jayein. Warna ise future work rakhein.

---

## 6. Phase-by-phase execution plan

### Phase 0 — Paper audit and research question freeze

**Duration:** 2–3 days  
**Goal:** Base paper ko samajhna, copy boundary define karna.

Tasks:

- Base paper ka 1-page contribution map banao.
- Har result ko tag karo: `reuse as lemma`, `cite only`, `do not reproduce`.
- Existing work ka search log banao: query, date, database, result, novelty impact.
- Final research question lock karo:
  - Main: exact code/hull enumerator.
  - Secondary: mean, variance, LCD count.
  - Stretch: inequivalent codes via Burnside.
- Scope freeze: `gcd(n,p)=1`, square-free `t_i`, compatible `lambda`.

**Deliverable:** `literature-gap-matrix.md` + one-paragraph problem statement.

**Go/no-go condition:** Agar kisi current paper me exactly same bivariate/cycle-index theorem mil jaye, title aur contribution ko immediately change karo.

---

### Phase 1 — Algebraic setup and notation

**Duration:** 4–6 days  
**Goal:** Ring decomposition ko clean aur self-contained banana.

Tasks:

1. CRT decomposition `A ~= product K_s` prove/quote with correct hypotheses.
2. Primitive idempotents `e_s` define karo; explicit formula sirf example ke liye.
3. Component degrees `m_s=[K_s:F_q]` record karo.
4. `lambda=(lambda_s)` and twist compatibility verify karo.
5. Explain why `gcd(n,p)=1` gives square-free `x^n-lambda_s`.
6. Define q-dimension vs K_s-dimension clearly.

**Deliverable:** Section 2 ka draft + notation table.

**Validation:** Small rings ke liye SageMath me `A.cardinality() = product_s |K_s|` verify karo.

---

### Phase 2 — Factor-orbit engine

**Duration:** 5–7 days  
**Goal:** `tau_{s,k}` ko computationally aur mathematically define karna.

Tasks:

- Har `x^n-lambda_s` ko factor karo.
- Har irreducible factor par coefficient-Frobenius + reciprocal operation apply karo.
- Confirm karo ki output same factor set me aata hai.
- Permutation cycles compute karo.
- Har cycle ke liye `(a_O, d_O, w_O)` store karo.
- Special cases test karo:
  - Euclidean `k=0`.
  - Hermitian `e` even, `k=e/2`.
  - `lambda=1`.
  - Nontrivial compatible `lambda`.

**Deliverable:** `factor_orbits.sage` or equivalent notebook + machine-readable orbit tables.

**Important check:** `tau` ka order general Galois case me 2 zaroori nahi hai. General cycles ko preserve karo; sirf Euclidean/Hermitian cases ko pair case na samjho.

---

### Phase 3 — Generator and hull factor lemma

**Duration:** 5–8 days  
**Goal:** Base paper ke hull-generator result ko apne enumerator theorem ke liye minimal lemma ke roop me use karna.

Tasks:

1. Component code `C_s(J_s)` ka generator and check polynomial likho.
2. `k`-Galois dual ke factor support ko `tau_{s,k}(F_s\setminus J_s)` prove karo.
3. Hull generator ka lcm support derive karo.
4. Complement ko `(F_s\setminus J_s) cap tau(J_s)` me simplify karo.
5. Is set ko cyclic binary transitions se identify karo.

**Deliverable:** Theorem 2 + complete proof.

**Do not do:** Source ka theorem paragraph paraphrase karke use mat karo. Apni factor-set proof likho aur source ko citation do.

---

### Phase 4 — Transfer matrix / cycle-index theorem

**Duration:** 4–6 days  
**Goal:** Main new result prove karna.

Tasks:

- One orbit par binary word weight define karo.
- Matrix `T_O(u,z)` derive karo.
- `trace(T_O^a)` ko closed walks ke roop me explain karo.
- Independent factor cycles ka product lo.
- `u=1`, `z=1`, derivatives ke corollaries derive karo.

**Deliverable:** Theorem 3, Theorem 4, Theorem 5.

**Sanity identities:**

\[
\mathscr E(1,1)=2^{\sum_s|\mathcal F_s|},
\]

and

\[
\mathscr E(u,1)
=\prod_{s}\prod_{f\in\mathcal F_s}(1+u^{m_s\deg f}).
\]

Agar ye identities fail karein, factor weights ya trace convention me error hai.

---

### Phase 5 — Exact enumeration and LCD distribution

**Duration:** 3–5 days  
**Goal:** Counting results ko usable form me present karna.

Tasks:

- `N_h=[z^h]H(z)` define karo.
- Nonzero coefficients ka support characterize karo.
- LCD count `H(0)` do.
- Maximum hull dimension ke liye coefficient / feasibility condition do.
- Pair-cycle special case ko short corollary ke roop me show karo:

\[
P_{2,w}(z)=2+2z^w.
\]

- General-cycle result ko main rakho; pair-only result ko special case rakho.

**Deliverable:** Counting theorem + at least 2 nontrivial examples.

---

### Phase 6 — Computation and exhaustive verification

**Duration:** 7–10 days  
**Goal:** Har theorem ko brute force se check karna.

For small factor counts:

1. All subsets `J_s` enumerate karo.
2. Direct generator matrix banao.
3. Galois dual/hull rank direct calculate karo.
4. Formula (H) se compare karo.
5. Polynomial `H(z)` ke coefficients se compare karo.
6. Joint enumerator ke `u` coefficients se code dimensions compare karo.

Use exact integer arithmetic only. Float/approximation avoid karo.

**Minimum tests:**

- One component field.
- Product of two fields with unequal `m_s`.
- One fixed factor + one 2-cycle.
- One 3-cycle or 4-cycle, so general-k result really test ho.
- Nontrivial lambda.
- Euclidean and Hermitian cases.

**Deliverable:** Reproducibility folder:

```text
code/
  factor_orbits.sage
  joint_enumerator.sage
  brute_force_check.sage
examples/
  example_q4_n5.json
  example_product_fields.json
README.md
```

---

### Phase 7 — Worked examples and tables

**Duration:** 4–6 days  
**Goal:** Examples theorem ko illustrate karein, source ke examples ko repeat na karein.

Recommended examples:

1. `A = F_4[u,v]/<u^2-u, v^2-v>`, `n=5`, `lambda=1`, Hermitian `k=1`.
2. A product with unequal component degrees, e.g. one `F_{q^2}` component and one `F_q` component.
3. A compatible nontrivial `lambda` of order dividing `1+p^{e-k}`.
4. A general Galois case with a cycle length `a>2`.

Har example me show karo:

- `A` ka component decomposition.
- `lambda_s`.
- Factorization of `x^n-lambda_s`.
- `tau` cycles.
- Orbit weights.
- `E(u,z)` or at least `H(z)`.
- Coefficient table `h -> number of codes`.
- Brute-force confirmation.

---

### Phase 8 — Non-isometric codes via Burnside (stretch but high-value)

**Duration:** 10–14 days  
**Goal:** Base paper ke future direction ko complete karna.

Suggested order:

1. Pehle `lambda=1` cyclic case lo.
2. Coordinate multiplier group ka exact subgroup define karo.
3. Check karo ki group `tau` factor cycles par kaise act karta hai.
4. Fixed subsets/codes enumerate karo.
5. Har group element ke liye fixed hull enumerator banao.
6. Burnside average se inequivalent counts nikalo.
7. Small cases brute-force canonical forms se verify karo.

**Fallback:** Agar full monomial group complicated ho, paper me “componentwise factor-selection equivalence” define karke clearly state karo ki ye full monomial equivalence se weaker notion hai. Terminology honest rakho.

---

### Phase 9 — Optional quantum-code application

**Duration:** 4–6 days  
**Goal:** Application ko main theorem ka natural consequence rakhna, paper ka sole contribution nahi.

For a verified field/Gray image code with parameters `[L,K,d]_q` and hull dimension `h`, apply the appropriate EAQECC construction to obtain parameters of the form

\[
[[L, K-h, d; L-K-h]]_q,
\]

subject to the exact hypotheses of the cited construction.

New angle:

- Enumerate **how many classical codes** give each entanglement consumption `c`.
- Use the bivariate enumerator to filter candidates by `(K,h)`.
- Compute minimum distance independently; hull enumerator alone distance prove nahi karta.
- Current best-known tables se comparison with access date record karo.

**Do not claim:** “New quantum codes” only because a table entry looks different. Every claim must be checked against current database and all parameter conventions.

---

### Phase 10 — Writing, proof audit, and submission readiness

**Duration:** 7–10 days  
**Goal:** Paper ko independent, reproducible aur plagiarism-safe banana.

Tasks:

- Every imported result ke saamne citation.
- Every new theorem ka dependency graph.
- Source PDF se phrase-level similarity scan.
- Notation consistency check: `q`, `p`, `e`, `k`, `m_s`, `N`, `a_O`, `d_O`, `w_O`.
- All examples scripts se regenerate.
- Tables me software version, finite-field convention, factor ordering record.
- Limitations section honestly write karo.
- Journal-specific formatting last me karo; pehle mathematics freeze karo.

---

## 7. Worked pilot example — paper start karne ke liye

Take

\[
A=\mathbb F_4[u,v]/\langle u^2-u, v^2-v\rangle.
\]

Because both polynomials split into distinct linear factors,

\[
A\cong\mathbb F_4^4.
\]

Hence `N=4`, every component has `m_s=1`. Choose

\[
n=5,\qquad \lambda=1,\qquad q=4=2^2,
\qquad k=1.
\]

Over `F_4`,

\[
x^5-1=(x-1)f_1(x)f_2(x),
\]

where `f_1,f_2` are the two irreducible quadratic factors. Under the Hermitian factor operation, the two quadratic factors form one 2-cycle and `(x-1)` is fixed. Therefore each component has:

- one fixed orbit of weight `1`,
- one 2-cycle of weight `2`.

The per-component hull polynomial is

\[
P_{1,1}(z)P_{2,2}(z)=2(2+2z^2).
\]

For four independent components,

\[
H(z)=2^8(1+z^2)^4.
\]

Thus the predicted distribution is:

| hull dimension `h` | number of codes |
|---:|---:|
| 0 | 256 |
| 2 | 1024 |
| 4 | 1536 |
| 6 | 1024 |
| 8 | 256 |

Checks:

- Total codes: `256+1024+1536+1024+256=4096=8^4`.
- Average hull dimension: `4`.
- Variance: `4`.
- LCD codes: `256=2^8`.

Is example ko paper me tabhi use karein jab SageMath se factorization, `tau` action aur every code ka direct hull rank verify ho jaye. Ye source paper ke examples ka copy nahi hai; iska purpose cycle-enumerator mechanism ko transparent banana hai.

---

## 8. Algorithm blueprint

### Algorithm A — Enumerated hull distribution

```text
Input:
  p, e, q=p^e, k, n
  square-free t_1,...,t_l
  unit lambda in A

1. Construct A and compute A ~= product_s K_s.
2. Record m_s=[K_s:F_q] and lambda_s in K_s.
3. Check gcd(n,p)=1.
4. Check lambda_s^(1+p^(e-k))=1 for every s.
5. For each s:
     a. Factor x^n-lambda_s over K_s.
     b. Build the factor permutation tau_{s,k}.
     c. Compute cycles O.
     d. For every O, store:
          a_O = cycle length,
          d_O = factor degree,
          w_O = m_s*d_O.
     e. Multiply E(u,z) by trace(T_O(u,z)^a_O).
6. Return E(u,z), H(z)=E(1,z), and coefficients N_h.
7. Run all sanity checks:
     E(1,1)=2^(sum_s |F_s|),
     H(1)=total number of codes,
     brute force on small instances.
```

### Algorithm B — Direct brute-force verifier

```text
For every component s:
  enumerate every subset J_s of irreducible factors.
  construct g_Js and the generator matrix G_s.
  compute the k-Galois dual/hull directly.
  record (dim_q(C), dim_q(Hull_k(C))).
Compare the histogram with coefficients of E(u,z).
```

### Complexity statement to target

Naive code enumeration is exponential in the total number of irreducible factors. The enumerator algorithm is polynomial in the number of factor cycles and in the target polynomial degree, because it uses `2 x 2` matrix powers and polynomial convolution. A formal complexity paragraph is worth adding, but exact model/bit complexity ko overclaim na karein.

---

## 9. Paper ka recommended section structure

### 1. Introduction

- Hulls and why exact distribution matters.
- What the base paper established.
- Clear gap: multiplicities/joint enumerator/inequivalent codes.
- Contributions in bullet form.
- Scope restrictions openly state karo.

### 2. Semisimple affine algebras and constacyclic codes

- Ring decomposition.
- Component fields and q-dimension.
- Constacyclic ideal correspondence.
- `k`-Galois factor operation.

### 3. Factor-orbit description of hulls

- Factor subsets.
- Dual factor action.
- Hull factor support.
- Boundary-statistic lemma.

### 4. Joint enumerator and exact distribution

- Transfer matrix.
- Product theorem.
- Coefficient formula.
- LCD count.

### 5. Moments and special cases

- Mean, variance.
- Euclidean/Hermitian pair-cycle corollaries.
- Conditions for all hull dimensions to occur, if provable.

### 6. Inequivalent codes (optional/high-value)

- Equivalence group.
- Fixed selections.
- Burnside formula.
- Small-case validation.

### 7. Algorithms and examples

- Pseudocode.
- Reproducible examples.
- Tables and plots of distributions.

### 8. Optional quantum application

- Only after classical enumeration is complete.
- Candidate filtering by code/hull dimension.
- Distance computation and current comparison.

### 9. Conclusion and limitations

- What was proved.
- What remains open: repeated roots, incompatible twists, full isometry classification, asymptotics.

---

## 10. Proof-dependency map

```text
CRT decomposition
      |
      v
component ideal classification
      |
      v
factor action tau_{s,k}
      |
      v
hull support = complement of lcm support
      |
      v
binary boundary statistic
      |
      v
transfer-matrix enumerator E(u,z)
      |
      +--> exact N_h
      +--> LCD count
      +--> mean/variance
      +--> EA candidate distribution
      +--> Burnside fixed-code enumerator (stretch)
```

Reviewer ko ye dependency map paper ke start/end me useful lagega, kyunki main theorem ka mechanism immediately visible ho jayega.

---

## 11. 9-week practical timeline

| Week | Target | Output |
|---:|---|---|
| 1 | Literature audit + scope freeze | Gap matrix, title, hypotheses |
| 2 | CRT/component algebra | Section 2 draft |
| 3 | Factor action + hull support | Lemmas and proof skeleton |
| 4 | Transfer matrix theorem | Main theorem draft |
| 5 | Coefficient, mean, variance corollaries | Enumeration section |
| 6 | Sage/Python implementation | Reproducible code |
| 7 | Exhaustive checks + examples | Verified tables |
| 8 | Burnside extension or quantum application | Optional section |
| 9 | Writing, similarity audit, journal formatting | Submission package |

If Week 8 ka Burnside result incomplete ho, usko force na karein; stronger, fully verified distribution paper weakly verified isometry paper se better hai.

---

## 12. Risk register and fallback plans

### Risk 1: General `k` me factor operation ka orbit structure confusing nikle

**Fallback:** Main theorem ko compatible Euclidean/Hermitian cases tak restrict karo; general `k` ko a separate proposition/algorithm rakho.

### Risk 2: `lambda` nontrivial hone par dual different twist me chala jaye

**Fallback:** Main theorem me `lambda_s^(1+p^(e-k))=1` explicitly impose karo; incompatible twists ko future work bolo.

### Risk 3: Full monomial equivalence group difficult ho

**Fallback:** Labeled-code enumeration publishable main result rakho; componentwise factor-selection equivalence ko clearly weaker auxiliary result ke roop me do.

### Risk 4: Quantum table me current best parameters improve na hon

**Fallback:** Quantum section ko “distribution of entanglement requirements” tak rakho; new-best-code claim mat karo.

### Risk 5: Source ke notation aur apne notation me mismatch

**Fallback:** Start me independent notation table banao; every formula ko direct small-case computation se test karo.

### Risk 6: Literature me same enumerator already mil jaye

**Fallback options:**

1. Weighted joint enumerator with unequal component extension degrees.
2. Burnside/isometry classification.
3. Repeated-root extension.
4. Asymptotic distribution/central-limit behavior for factor-cycle families.

---

## 13. Originality / plagiarism checklist

- [ ] Base paper ka abstract, introduction, theorem wording, proof order copy nahi kiya.
- [ ] New paper ka title aur research question different hai.
- [ ] Source ke results ko clearly cited lemmas ke roop me use kiya.
- [ ] Every new formula independently derived and brute-force tested hai.
- [ ] Source ke examples, parameter tables, variable names unnecessarily repeat nahi kiye.
- [ ] “New code” claim se pehle current database comparison kiya.
- [ ] AI-assisted drafting hua ho to journal ki AI policy follow ki.
- [ ] Authors ne final mathematics, code aur citations manually verify kiye.
- [ ] Reproducibility code and exact software versions included hain.

### Safe writing rule

Source se idea lena allowed hai; source ka sentence structure, proof sequence, notation aur examples ko cosmetic paraphrase karna allowed nahi samajhna chahiye. Naye paper ka **mathematical object** hi alag rakho: source me individual hull formula; proposed paper me factor-cycle enumerator and exact distribution.

---

## 14. Final recommended contribution list

Agar paper ko concise but strong rakhna ho, final abstract/contributions me sirf ye claims rakhein:

1. We classify separable constacyclic codes over a square-free affine algebra by component factor selections.
2. We encode the Galois hull dimension as a weighted boundary statistic on the cycles of the induced factor permutation.
3. We derive a bivariate transfer-matrix enumerator for code dimension and hull dimension.
4. We obtain exact counts, LCD counts, mean and variance of Galois hull dimensions.
5. We provide an exact algorithm and exhaustive computational verification.
6. If completed: we add a Burnside formula for inequivalent codes under a precisely defined isometry group.

Ye contribution base paper ki copy nahi, balki uske “open enumeration problem” ka structured, verifiable aur mathematically stronger follow-up hoga.

---

## 15. First 48 hours me kya karna hai?

1. `q=4, A=F_4[u,v]/<u^2-u,v^2-v>, n=5, lambda=1, k=1` pilot example ko SageMath me verify karo.
2. Factor permutation `tau` aur cycle lengths print karo.
3. Brute-force histogram nikalo.
4. `H(z)` ke coefficients se compare karo.
5. Agar match ho, Theorem 2–4 ka proof likhna start karo.
6. Agar match na ho, pehle `k`-Galois reciprocal convention fix karo; theorem likhne ki jaldi mat karo.

**Success criterion:** pilot example me direct hull histogram aur enumerator histogram exactly identical hon, aur total code count bhi match kare.
