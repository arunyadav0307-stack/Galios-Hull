# The joint code–hull distribution of repeated-root constacyclic codes over affine algebras via transfer matrices

*[Author names and affiliations to be inserted] — Draft of 21 October 2026*
*Markdown companion of `P1_15_MANUSCRIPT_DRAFT.tex` (same content; the LaTeX file is the primary source). No novelty or priority claim is made anywhere in this draft.*

**Abstract.** Let $A \cong \prod_{s=1}^{N} K_s$ be a square-free affine algebra over $\mathbb{F}_q$, let $P = p^{\varrho}$ be a power of the characteristic, and let $n = P n_0$ with $\gcd(n_0,p)=1$. For compatible twists $\lambda_s$ we study the $\lambda_s$-constacyclic codes of length $n$ over each $K_s = \mathbb{F}_{q^{m_s}}$ in the repeated-root regime $x^n - \lambda_s = (x^{n_0} - \mu_s)^P$, parametrized by exponent assignments $a_f \in \{0,\dots,P\}$ on the distinct irreducible factors of the separable polynomial $x^{n_0} - \mu_s$. Using the code-first $k$-Galois pairing, we give the Galois dual and hull of such a code in exponent form: on each orbit of the reciprocal involution $\tau_s$, the hull dimension is a sum of edge terms $\min(P-\alpha_i, \alpha_{i-1})$. Our main result is a joint enumerator $\mathcal{E}(u,z) = \sum_a u^{\dim_{\mathbb{F}_q} C(a)} z^{\dim_{\mathbb{F}_q} \mathrm{Hull}_k(C(a))} = \prod_s \prod_O \mathrm{tr}\big(T^{(P)}_{w_O}(u,z)^{L_O}\big)$, where $T^{(P)}_w(u,z)_{a,b} = u^{w(P-b)} z^{w\min(P-b,a)}$ is a $(P{+}1)$-state transfer matrix attached to each $\tau_s$-orbit. We derive the total count, the code-dimension distribution, the LCD count $2^{\#\mathrm{orbits}}$ (independent of $P$), characterizations and counts of self-orthogonal and dual-containing codes, and exact mean and variance formulas for the hull dimension, in which orbits of length one require a separate term $\nu_P = \lfloor P^2/4\rfloor/(P+1)$. At $P=1$ the enumerator specializes to the binary-state simple-root formula. All counts are over labeled exponent assignments.

**Keywords:** constacyclic codes; repeated-root codes; Galois hull; joint enumerator; transfer matrix; affine algebra. **MSC:** 94B15, 94B05, 11T71.

---

## 1. Introduction

For a linear code $C$ over a finite field, the hull — the intersection of $C$ with its dual — controls several constructions, including the amount of entanglement needed in entanglement-assisted quantum codes and the behaviour of LCD (linear complementary dual) codes. Replacing the Euclidean inner product by a Galois inner product leads to the $k$-Galois hull $\mathrm{Hull}_k(C) = C \cap D(C)$, where $D(C)$ is the dual with respect to a Frobenius-twisted pairing. Galois hulls of constacyclic codes have been determined, at the level of hull dimensions and hull generators, in a number of settings. Over finite fields, Debnath, Prakash and Islam determined the Galois hull dimension of constacyclic codes and the number of such codes with a given Galois hull dimension [DPI2023] (see also the correction [DPI2023corr]); average Galois hull dimensions over finite fields and over an auxiliary ring were computed by Debnath and Prakash [DP2025], and constacyclic codes with small Galois hull dimension were studied by Debnath, Islam, Yadav and Prakash [DIYP2026]. Over affine algebra rings, Debnath, Islam, Martínez-Moro and Prakash obtained Galois hull formulas for constacyclic codes [DIMP2026], working mainly in a simple-root (idempotent) framework with a repeated-root case under additional hypotheses on the order of the twist. Eldin and Solé developed generator polynomial matrices for the Galois hulls of multi-twisted codes, of which constacyclic codes are the index-one case [ES2026]. Galois hulls over chain and serial rings appear in [Talbi2021], and Galois hulls have likewise been used for quantum-code constructions over a finite non-chain ring [ZKZ2026]; repeated-root constacyclic codes and their (Euclidean) duals, including LCD and self-dual enumerations in special lengths, have a substantial literature [CDL2015, Sharma2015, WZLL2023, ZWLL2025].

The present paper studies a distributional question in the repeated-root setting. Fix a square-free affine algebra $A \cong \prod_{s=1}^{N} K_s$ and a length $n = P n_0$ in which the characteristic divides $n$ through the prime power $P = p^{\varrho}$, while $\gcd(n_0, p) = 1$. Every constacyclic code over $A$ is then described, component by component, by exponents $a_f \in \{0, \dots, P\}$ attached to the distinct irreducible factors of a separable polynomial $x^{n_0} - \mu_s$. Rather than the dimension of a single hull, we determine the *joint distribution* of the pair $(\dim_{\mathbb{F}_q} C, \dim_{\mathbb{F}_q} \mathrm{Hull}_k(C))$ over all labeled exponent assignments, for compatible twists. The joint law is captured by a transfer-matrix enumerator: each orbit of the reciprocal involution on the factor set contributes the trace of a power of a $(P{+}1)$-state matrix whose entries record, edge by edge, the code-dimension and hull-dimension contributions (Theorem 6.3). From the enumerator we extract the total number of codes, the code-dimension distribution, the number of LCD codes, characterizations and counts of self-orthogonal and dual-containing codes, and exact first and second moments of the hull dimension. A point that requires care is the case of an orbit of length one: its hull edge is a self-loop $\min(P-A, A)$, whose mean $\nu_P = \lfloor P^2/4 \rfloor / (P+1)$ differs from the mean $\mu_P = P(2P+1)/(6(P+1))$ of an ordinary edge; conflating the two gives an incorrect hull mean as soon as a fixed factor of the reciprocal involution is present.

The paper is organized as follows. Section 2 fixes the conventions, in particular the code-first Galois pairing on which the dual formulas depend. Sections 3–5 develop the parametrization, the Galois dual, and the hull formula in exponent form. Section 6 proves the transfer-matrix enumerator and its specialization at $P=1$. Sections 7 and 8 contain the counting corollaries and the moment formulas. Section 9 gives worked examples and describes the computational verification; Section 10 records the scope and limitations. Throughout, counts are over labeled exponent assignments, not over equivalence or isometry classes of codes.

## 2. Preliminaries and conventions

Let $p$ be a prime, $q = p^e$, and let $0 \le k < e$ be a fixed Galois index. Let $A \cong \prod_{s=1}^{N} K_s$, $K_s = \mathbb{F}_{q^{m_s}} = \mathbb{F}_{p^{d_s}}$, $d_s = e m_s$, with fixed component labels. (Standard terminology for constacyclic codes follows [HP2003, MS1977].) On $K_s$ write $\sigma(\alpha) = \alpha^{p^k}$ and $\rho(\alpha) = \alpha^{p^{d_s - k}} = \sigma^{-1}$.

**Definition (code-first Galois pairing).** For one component (the subscript $s$ suppressed), the $k$-Galois pairing on $K^n$ is $\langle x, y \rangle_k = \sum_{i=0}^{n-1} x_i \, \sigma(y_i)$, the *code-first* dual of a code $C \subseteq K^n$ is $D(C) = \{ y \in K^n : \langle c, y \rangle_k = 0 \text{ for all } c \in C\}$, and the $k$-Galois hull is $\mathrm{Hull}_k(C) = C \cap D(C)$. The Euclidean dual is denoted $C^\perp$.

The slot order is part of the definition: the candidate $y$ occupies the $\sigma$-twisted slot, and this is what makes $D(C) = \rho(C^\perp)$ (coordinatewise $\rho$; Proposition 4.2) rather than the analogous statement with $\sigma$. All dual formulas below use this convention. The global pairing on $A^n$ is the tuple of component pairings; a code over $A$ is an $A$-submodule of $A^n$.

Fix $\varrho \ge 0$, $P = p^{\varrho}$, and $n = P n_0$ with $\gcd(n_0, p) = 1$. Let $\lambda = (\lambda_s) \in A^*$ and $M_s(x) = x^n - \lambda_s \in K_s[x]$. Since $a \mapsto a^P$ is a bijection of the finite field $K_s$, there is a unique $\mu_s \in K_s^*$ with $\mu_s^P = \lambda_s$. Writing $\bar M_s(x) = x^{n_0} - \mu_s$, we have $M_s = \bar M_s^{\,P}$ in characteristic $p$, and $\bar M_s$ is separable because $\bar M_s' = n_0 x^{n_0-1}$ and every root of $\bar M_s$ is nonzero. Let $\mathcal{F}_s$ be the set of distinct monic irreducible factors of $\bar M_s$ over $K_s$; then $M_s = \prod_{f \in \mathcal{F}_s} f^P$.

An *exponent assignment* on component $s$ is a tuple $a = (a_f)_{f \in \mathcal{F}_s}$ with $a_f \in \{0, \dots, P\}$; put $g_a = \prod_f f^{a_f}$ and $C_s(a) = \langle g_a \rangle \subseteq K_s[x]/(M_s)$. A global assignment is a tuple of component assignments.

For a monic polynomial $f(x) = \sum_{i=0}^{r} c_i x^i$ with $f(0) = c_0 \ne 0$, define the (Frobenius-twisted) reciprocal $f^{\#}(x) = \rho(c_0)^{-1} \sum_{i=0}^{r} \rho(c_i)\, x^{\,r-i}$, which is monic of degree $r$. Every $f \in \mathcal{F}_s$ satisfies $f(0) \ne 0$ since $\bar M_s(0) = -\mu_s \ne 0$.

**Definition (compatibility and the involution $\tau_s$).** The twist $\lambda_s$ is *compatible* if $\lambda_s^{\,1 + p^{d_s - k}} = 1$. Under compatibility, $\tau_s : \mathcal{F}_s \to \mathcal{F}_s$, $\tau_s(f) = f^{\#}$, is a permutation (Theorem 3.2). We assume compatibility for every $s$ from Section 4 on. A $\tau_s$-orbit is written $O = (f_0, \dots, f_{L-1})$ with $\tau_s(f_i) = f_{i+1}$, indices modulo $L = L_O$; we set $\alpha_i = a_{f_i}$ and call $\alpha_{i-1}$ the predecessor of $\alpha_i$. Since $\#$ preserves degrees, all factors in an orbit have the same degree; the *weight* of $O$ and of a factor $f$ is $w_O = m_s \deg_{K_s} f$ and $w_f = m_s \deg_{K_s} f$.

Dimensions over $\mathbb{F}_q$ are recovered from dimensions over $K_s$ by $\dim_{\mathbb{F}_q} V = m_s \dim_{K_s} V$. We write $u, z$ for indeterminates and work in $\mathbb{Z}[u,z]$.

## 3. Parametrization and the reciprocal operation

**Theorem 3.1 (T1: parametrization).** The map $a \mapsto C_s(a) = \langle g_a \rangle$ is a bijection from $\{0,\dots,P\}^{\mathcal{F}_s}$ onto the set of $\lambda_s$-constacyclic codes of length $n$ over $K_s$, and $\dim_{K_s} C_s(a) = n - \sum_{f} a_f \deg f$. Consequently there are $(P+1)^{\sum_s |\mathcal{F}_s|}$ labeled global assignments, and global codes (as $A$-submodules) correspond to tuples of component assignments.

*Proof.* Ideals of $K_s[x]/(M_s)$ correspond to ideals $(M_s) \subseteq I$ of the principal ideal domain $K_s[x]$, hence to monic divisors $\bar g$ of $M_s$; by unique factorization and $M_s = \prod f^P$, monic divisors are exactly the $g_a$. For a monic divisor $g$ of degree $r$, multiplication by $g$ identifies $\langle g \rangle \subseteq K_s[x]/(M_s)$ with $K_s[x]/((M_s)/g)$, of dimension $n - r$. No separability hypothesis is used. ∎

**Theorem 3.2 (T2: the reciprocal operation).**
(i) $\#$ is multiplicative on monic polynomials with nonzero constant term; hence $\big(\prod_f f^{a_f}\big)^{\#} = \prod_f (f^{\#})^{a_f}$ for all exponents $a_f \ge 0$.
(ii) If $f(\alpha) = 0$ with $\alpha \ne 0$ in an algebraic closure, then $f^{\#}\big(\alpha^{-p^{d_s-k}}\big) = 0$; in fact $f^{\#}$ is the minimal polynomial of $\alpha^{-p^{d_s-k}}$.
(iii) $\lambda_s^{1+p^{d_s-k}} = 1 \iff \mu_s^{1+p^{d_s-k}} = 1$. Under compatibility, $\tau_s$ permutes $\mathcal{F}_s$ and preserves degrees.

*Proof.* Let $\bar\rho$ be the coefficientwise extension of $\rho$ to $K_s[x]$; it is a ring automorphism with inverse $\bar\sigma$. For (i), $\overline\rho(fg) = \bar\rho(f)\bar\rho(g)$, reversal $x^{r}f(1/x)$ is multiplicative in fixed degrees, and the normalizing constants multiply since $(fg)_0 = f_0 g_0$; combining the three gives $(fg)^{\#} = f^{\#} g^{\#}$, and induction on the number of factors gives the displayed identity. For (ii), apply the Frobenius map $t \mapsto t^{p^{d_s-k}}$ of the algebraic closure to $\sum c_i \alpha^i = 0$ to get $\sum \rho(c_i) \beta^{-i} = 0$ for $\beta = \alpha^{-p^{d_s-k}}$; multiplying by $\beta^r$ yields $\rho(c_0) f^{\#}(\beta) = 0$. The same Frobenius transport preserves degrees of minimal polynomials, so $f^{\#}$ is the (monic irreducible) minimal polynomial of $\beta$. For (iii), $(\mu_s^{1+p^{d_s-k}})^P = \lambda_s^{1+p^{d_s-k}}$ and in characteristic $p$, $y^P = 1$ implies $y = 1$; now (ii) shows $\tau_s(f)$ is the minimal polynomial of a root $\beta$ with $\beta^{n_0} = \rho(\mu_s)^{-1} = \mu_s$ (using compatibility in the form $\rho(\mu_s) = \mu_s^{-1}$), so $\tau_s(f) \mid \bar M_s$; bijectivity follows by applying the same construction with $\sigma$ in place of $\rho$, which gives the inverse map. ∎

## 4. The Galois dual

**Lemma 4.1 (Euclidean dual generator).** Let $g$ be a monic divisor of $x^n - \lambda$, $\lambda \in K^*$, $h = (x^n-\lambda)/g$, $r = \deg g$, $s = n - r$, and $C = \langle g \rangle$ under the coefficient identification. Then $h_0 \ne 0$, and with $h^{\natural}(x) = h_0^{-1} \sum_{i=0}^{s} h_i x^{s-i}$ (the ordinary reciprocal, without Frobenius), $C^\perp = \langle h^{\natural} \rangle$, a $\lambda^{-1}$-constacyclic code.

*Proof.* From $gh = x^n - \lambda$, $g_0 h_0 = -\lambda \ne 0$. Both $\langle h^{\natural} \rangle$ and $C^\perp$ have dimension $r$: the first by the divisor dimension count of Theorem 3.1 (applied to any modulus), the second by rank–nullity. We show orthogonality. For polynomials $a, d$ of degree $< n$, write $\mathrm{rev}_n(d) = x^{n-1} d(1/x)$; then $\sum_i a_i d_i = [x^{n-1}]\big(a(x) \mathrm{rev}_n(d)(x)\big)$. Take $a = gu$, $\deg u < s$, and $d = h^{\natural} v$, $\deg v < r$. Since $h^{\natural}(1/x) = h_0^{-1} x^{-s} h(x)$, one computes $\mathrm{rev}_n(d) = h_0^{-1} h(x) V(x)$ with $V(x) = x^{r-1} v(1/x)$, $\deg V \le r-1$. Hence $a(x)\mathrm{rev}_n(d)(x) = h_0^{-1} (x^n - \lambda) u(x) V(x)$ with $\deg(uV) \le n-2$; the coefficient of $x^{n-1}$ is $0$. Thus $\langle h^{\natural}\rangle \subseteq C^\perp$, and equality follows by dimensions. That $h^{\natural} \mid x^n - \lambda^{-1}$ follows from $(gh)^* = g^* h^* = -\lambda(x^n - \lambda^{-1})$ for the unnormalized reciprocal $\phi^*(x) = x^{\deg\phi}\phi(1/x)$. ∎

**Proposition 4.2 (transport by $\rho$).** Let $K = \mathbb{F}_{p^d}$ with $\sigma, \rho$ as in Section 2. For every $K$-linear code $C \subseteq K^n$, $D(C) = \rho(C^\perp)$ (coordinatewise). Consequently, for $C = \langle g \rangle \subseteq K[x]/(x^n-\lambda)$ and $h = (x^n-\lambda)/g$, $D(C) = \langle h^{\#} \rangle \subseteq K[x]/(x^n - \lambda^{-p^{d-k}})$; if $\lambda$ is compatible, the modulus is again $x^n - \lambda$.

*Proof.* By the code-first definition, $y \in D(C)$ iff $\sum_i c_i \sigma(y_i) = 0$ for all $c \in C$, i.e. iff $\sigma(y) \in C^\perp$ (coordinatewise), i.e. iff $y \in \rho(C^\perp)$ since $\rho = \sigma^{-1}$; this is exactly where the slot order enters. Coefficientwise application of an automorphism sends the ideal $\langle e \rangle$ in $K[x]/(x^n-\eta)$ to $\langle \bar\rho(e)\rangle$ in $K[x]/(x^n - \rho(\eta))$; applying this to Lemma 4.1 and comparing $\bar\rho(h^{\natural})$ with $h^{\#}$ gives the generator. Compatibility $\lambda^{1+p^{d-k}}=1$ gives $\lambda^{-p^{d-k}} = \lambda$. ∎

**Theorem 4.3 (T3: dual exponents).** For every assignment $a$, with $h_a = M_s / g_a$, $D(C_s(a)) = \langle h_a^{\#} \rangle$; under compatibility this is a $\lambda_s$-constacyclic code in the same quotient. On a $\tau_s$-orbit $O = (f_0,\dots,f_{L-1})$ with $\alpha_i = a_{f_i}$, the exponent of $f_i$ in $h_a^{\#}$ is $\beta_i = P - \alpha_{i-1}$ (indices mod $L$).

*Proof.* The generator statement is Proposition 4.2. For the exponents, $h_a = \prod_{f} f^{P - a_f}$, so by Theorem 3.2(i) and the permutation property, $h_a^{\#} = \prod_f (\tau_s f)^{P-a_f} = \prod_{g} g^{P - a_{\tau_s^{-1} g}}$; for $g = f_i$, $\tau_s^{-1}(f_i) = f_{i-1}$, giving $P - \alpha_{i-1}$. ∎

**Remark.** Without compatibility, $D(C_s(a)) = \langle h_a^{\#}\rangle$ and the exponent formula remain valid, but in the modulus $x^n - \lambda_s^{-p^{d_s-k}}$. Compatibility is what allows the dual to be viewed inside the same constacyclic family; it cannot simply be dropped (e.g. in $\mathbb{F}_9$ with $k=1$, a twist $\lambda$ of order $8$ satisfies $\lambda^{1+3} = \lambda^4 = -1 \ne 1$ and indeed $\lambda^{-3} \ne \lambda$).

## 5. The Galois hull

**Lemma 5.1 (intersection of ideals).** For monic divisors $g, l$ of a monic $M \in K[x]$, the images of $(g)$ and $(l)$ in $K[x]/(M)$ intersect in the image of $(\mathrm{lcm}(g,l))$, and $\mathrm{lcm}(g,l) = \prod_{\pi} \pi^{\max(v_\pi(g), v_\pi(l))}$.

*Proof.* In $K[x]$, $(g) \cap (l) = (\mathrm{lcm}(g,l))$ since both consist of the common multiples of $g$ and $l$, characterized valuation-wise by the displayed maximum. If $y$ lies in both images in the quotient, any lift $Y$ satisfies $Y \in (g)$ and $Y \in (l)$ because $(M) \subseteq (g), (l)$; hence $Y \in (\mathrm{lcm}(g,l))$. The reverse inclusion is immediate from $g, l \mid \mathrm{lcm}(g,l)$. ∎

**Theorem 5.2 (T4: hull generator and dimensions).** Under compatibility, for every assignment $a$, $\mathrm{Hull}_k(C_s(a)) = \langle \mathrm{lcm}(g_a, h_a^{\#}) \rangle$, the exponent of $f_i$ in the hull generator being $\max(\alpha_i, P-\alpha_{i-1})$. Moreover
$$\dim_{\mathbb{F}_q} C(a) = \sum_{s} \sum_{O} w_O \sum_{i} (P - \alpha_i), \qquad \dim_{\mathbb{F}_q} \mathrm{Hull}_k(C(a)) = \sum_{s} \sum_{O} w_O \sum_i \min(P-\alpha_i,\, \alpha_{i-1}),$$
the inner sums over orbit positions (indices mod $L_O$).

*Proof.* Work in one component. By Theorems 3.1 and 4.3, $C(a)$ and $D(C(a))$ are the images of $(g_a)$ and $(h_a^{\#})$, both dividing $M = x^n-\lambda$; Lemma 5.1 gives the hull generator, whose $f_i$-exponent is $\max(\alpha_i, \beta_i) = \max(\alpha_i, P-\alpha_{i-1})$. Dimensions are $n - \deg(\text{generator})$ over $K$; grouping factors by orbits (constant degree on an orbit) and using $P - \max(u,v) = \min(P-u, P-v)$ with $v = P-\alpha_{i-1}$ gives the hull formula; multiplication by $m_s$ and summation over $s$ gives the $\mathbb{F}_q$-dimensions. ∎

## 6. The transfer-matrix enumerator

For $P \ge 1$, $w \ge 1$, define the $(P{+}1)\times(P{+}1)$ matrix over $\mathbb{Z}[u,z]$
$$T^{(P)}_w(u,z)_{a,b} = u^{\,w(P-b)}\, z^{\,w \min(P-b,\, a)}, \qquad a, b \in \{0,\dots,P\},$$
the row index $a$ being the previous exponent and the column index $b$ the current one.

**Theorem 6.1 (T5: local transfer trace).** For a $\tau_s$-orbit $O$ of length $L$ and weight $w$,
$$\mathrm{tr}\big(T^{(P)}_w(u,z)^L\big) = \sum_{\alpha \in \{0,\dots,P\}^L} u^{\,w \sum_i (P-\alpha_i)}\, z^{\,w \sum_i \min(P-\alpha_i,\, \alpha_{i-1})}, \quad \text{indices mod } L.$$

*Proof.* Expanding the matrix power, $(T^L)_{a_0,a_L} = \sum_{a_1,\dots,a_{L-1}} \prod_{j=1}^{L} T_{a_{j-1},a_j}$; setting $a_L = a_0$ and summing over $a_0$ gives $\mathrm{tr}(T^L) = \sum_{a_0,\dots,a_{L-1}} \prod_{j=1}^{L} T_{a_{j-1},a_j}$. These closed walks are in bijection with assignments $\alpha = (\alpha_0,\dots,\alpha_{L-1})$ (orbit positions are labeled; a walk and its rotation are different assignments). The $j$-th edge contributes $u^{w(P-a_j)} z^{w\min(P-a_j, a_{j-1})}$; summing exponents over the walk and reindexing gives the claim. For $L=1$ the single edge is the self-loop $a_0 \to a_0$ and the formula reads $\sum_a u^{w(P-a)} z^{w\min(P-a,a)}$, as required. ∎

**Proposition 6.2 (product assembly).** Ideals of $A[x]/(x^n-\lambda) \cong \prod_s K_s[x]/(x^n-\lambda_s)$ are exactly the products of component ideals; the global dual and hull decompose componentwise; and $\dim_{\mathbb{F}_q} C = \sum_s m_s \dim_{K_s} C_s$, likewise for the hull.

*Proof.* The ring isomorphism is coefficientwise; quotienting a product by the product ideal $(x^n-\lambda_s)_s$ gives the product of quotients (this is the direct-product structure of the square-free algebra $A$ itself; no coprimality between components is involved). Ideals of a finite product of rings are products of ideals (project, and recover the components with the idempotents of $A$). The pairing is componentwise and vanishes exactly when every component does, giving the dual and hull statements; dimensions add over the direct sum $A^n \cong \bigoplus_s K_s^n$ with the factor $[K_s:\mathbb{F}_q] = m_s$. ∎

**Theorem 6.3 (T6: joint enumerator).** Under the standing hypotheses (common $P, n, k$; compatible twists; labeled components),
$$\mathcal{E}(u,z) := \sum_{\text{labeled } a} u^{\dim_{\mathbb{F}_q} C(a)} z^{\dim_{\mathbb{F}_q} \mathrm{Hull}_k(C(a))} = \prod_{s=1}^{N} \prod_{O \in \mathcal{O}_s} \mathrm{tr}\Big(T^{(P)}_{w_O}(u,z)^{L_O}\Big),$$
where $\mathcal{O}_s$ is the set of $\tau_s$-orbits. The coefficient of $u^K z^H$ is the number of labeled assignments with $\dim_{\mathbb{F}_q} C = K$ and $\dim_{\mathbb{F}_q} \mathrm{Hull}_k(C) = H$.

*Proof.* By Theorem 3.1 and Proposition 6.2, a global assignment is the disjoint union of its orbit restrictions $\alpha^{(O)} \in \{0,\dots,P\}^{L_O}$, and by Theorem 5.2 each of the two dimensions is a sum over $(s,O)$ of a quantity depending only on $\alpha^{(O)}$. The finite distributive law (expanding a product of sums over a Cartesian product index set) factorizes the global sum into the product of the orbit sums $\mathcal{E}_O(u,z) = \sum_{\alpha} u^{w_O \sum (P-\alpha_i)} z^{w_O \sum \min(P-\alpha_i,\alpha_{i-1})}$, and Theorem 6.1 identifies $\mathcal{E}_O(u,z) = \mathrm{tr}(T^{(P)}_{w_O}(u,z)^{L_O})$. ∎

**Remark (hypotheses of the identity).** As an identity in $\mathbb{Z}[u,z]$, Theorem 6.1 holds for every integer $P \ge 1$; the prime-power form $P = p^{\varrho}$ is needed for the field construction behind Theorems 3.1–5.2, not for the matrix identity. The enumerator counts labeled assignments; the trace formula is insensitive to reversing the orbit orientation (the distribution is unchanged under $\alpha_i \mapsto \alpha_{-i}$), so the predecessor convention $\alpha_{i-1}$ in Theorem 5.2 is an essential part of the statement, fixed by the code-first pairing of Section 2.

**Proposition 6.4 (simple-root recovery at $P=1$).** At $\varrho = 0$ ($P=1$), assignments are binary, $g_a$ is a squarefree divisor, the hull edge term $\min(1-\alpha_i, \alpha_{i-1})$ is the indicator of the transition $1 \to 0$ along the orbit, and
$$T^{(1)}_w(u,z) = \begin{pmatrix} u^w & 1 \\ u^w z^w & 1 \end{pmatrix} \qquad (\text{rows/columns } a,b \in \{0,1\}),$$
so Theorem 6.3 specializes to the binary-state simple-root joint enumerator with the same conventions.

*Proof.* For $P=1$, $\min(1-b, a)$ is $1$ exactly for $(a,b) = (1,0)$; reading off the four entries gives the matrix, and $\mu_s = \lambda_s$, $\bar M_s = M_s$ gives the squarefree parametrization. ∎

## 7. Counting corollaries

**Corollary 7.1 (C1: total count).** $\mathcal{E}(1,1) = (P+1)^{\sum_s |\mathcal{F}_s|}$.

*Proof.* At $u=z=1$ each $T^{(P)}_w$ is the all-ones matrix $J$ with $J^L = (P+1)^{L-1} J$, so $\mathrm{tr}(J^{L_O}) = (P+1)^{L_O}$; product over orbits gives $(P+1)^{\sum_s \sum_O L_O} = (P+1)^{\sum_s |\mathcal{F}_s|}$. ∎

**Corollary 7.2 (C2: code-dimension distribution).** $\displaystyle \mathcal{E}(u,1) = \prod_{s} \prod_{f \in \mathcal{F}_s} \big(1 + u^{w_f} + \dots + u^{P w_f}\big)$.

*Proof.* At $z=1$ the entry $T_{a,b} = u^{w(P-b)}$ is independent of the row, so $T = c\,r$ is rank one with $r \cdot c = \sum_{j=0}^{P} u^{wj}$; then $\mathrm{tr}(T^L) = (r\cdot c)^{L-1} \mathrm{tr}(T) = \big(\sum_{j=0}^P u^{wj}\big)^L$. Within an orbit all $w_f$ equal $w_O$, giving $\prod_{f \in O} (1 + u^{w_f} + \dots + u^{Pw_f})$ per orbit. ∎

**Corollary 7.3 (C3: LCD count).** The number of labeled assignments with $\mathrm{Hull}_k(C(a)) = 0$ is $2^{\#\text{orbits}}$, independent of $P$.

*Proof.* The hull dimension is a sum of nonnegative terms $w_O \min(P-\alpha_i, \alpha_{i-1})$; it vanishes iff every orbit satisfies $\min(P-\alpha_i, \alpha_{i-1}) = 0$ for all $i$. On one orbit, if some $\alpha_m \notin \{0,P\}$ (so $P \ge 2$), then $\min(P-\alpha_{m+1}, \alpha_m) = 0$ with $\alpha_m > 0$ forces $\alpha_{m+1} = P$, and inductively every $\alpha_i = P$ around the cycle, a contradiction (for $L=1$, $\min(P-\alpha_0,\alpha_0) = 0$ already forces $\alpha_0 \in \{0,P\}$). Hence each $\alpha_i \in \{0,P\}$; if both values occurred, at a boundary position with $\alpha_i = 0$, $\alpha_{i-1} = P$ the term would be $\min(P,P) = P \ge 1$. So exactly two tuples per orbit ($\alpha \equiv 0$ or $\alpha \equiv P$), independently across orbits. ∎

**Corollary 7.4 (C4: self-orthogonal and dual-containing codes).** $C(a) \subseteq D(C(a))$ if and only if $\alpha_{i-1} + \alpha_i \ge P$ on every orbit edge, and then the count is $\prod_O \mathrm{tr}(B_P^{L_O})$ with $(B_P)_{a,b} = 1$ iff $a+b \ge P$. Dually, $D(C(a)) \subseteq C(a)$ if and only if $\alpha_{i-1} + \alpha_i \le P$ on every edge, with count $\prod_O \mathrm{tr}((B'_P)^{L_O})$, $(B'_P)_{a,b} = 1$ iff $a+b \le P$. The two counts are equal.

*Proof.* Since $\mathrm{Hull} = C \cap D(C) \subseteq C$, $C \subseteq D(C)$ iff $\dim \mathrm{Hull} = \dim C$. By Theorem 5.2, $\dim C - \dim \mathrm{Hull} = \sum_{s,O} w_O \sum_i \max(0, P-\alpha_i-\alpha_{i-1})$ because $(P-\alpha_i) - \min(P-\alpha_i,\alpha_{i-1}) = \max(0, P-\alpha_i-\alpha_{i-1})$; every summand is nonnegative, so the total vanishes iff every edge satisfies $\alpha_{i-1}+\alpha_i \ge P$. The admissible tuples on one orbit are the closed walks of the $0$–$1$ matrix $B_P$, counted by $\mathrm{tr}(B_P^{L_O})$ as in Theorem 6.1. For the dual side, $\dim D(C) = \sum w_O \sum_i \alpha_{i-1} = \sum w_O \sum_i \alpha_i$ by Theorem 4.3, and $\alpha_{i-1} - \min(P-\alpha_i,\alpha_{i-1}) = \max(0, \alpha_i+\alpha_{i-1}-P)$; the same argument gives the condition $\alpha_{i-1}+\alpha_i \le P$ and the count $\mathrm{tr}((B'_P)^{L_O})$. The involution $\alpha_i \mapsto P-\alpha_i$ maps one edge condition to the other, so the counts agree. ∎

## 8. Moments of the hull dimension

Choose a labeled assignment uniformly at random; equivalently, all exponents $A_i$ (over all components, orbits, positions) are independent and uniform on $\{0,\dots,P\}$. For one orbit write $X_i = \min(P-A_i, A_{i-1})$ (indices mod $L$) and $S_L = \sum_i X_i$; the orbit contributes $w_O S_{L_O}$ to $\dim_{\mathbb{F}_q}\mathrm{Hull}_k$ (Theorem 5.2). Set
$$\mu_P = \frac{P(2P+1)}{6(P+1)}, \qquad \nu_P = \frac{\lfloor P^2/4 \rfloor}{P+1}.$$

**Lemma 8.1 (edge moments).** For independent $U, V$ uniform on $\{0,\dots,P\}$, $\mathbb{E}[\min(U,V)] = \mu_P$ and $\mathbb{E}[\min(U,V)^2] = \frac{P(P^2+P+1)}{6(P+1)}$. For $0 \le c \le P$, $F(c) := \mathbb{E}[\min(c,U)] = \frac{c(2P-c+1)}{2(P+1)}$.

*Proof.* For a nonnegative integer variable, $\mathbb{E}[X] = \sum_{t\ge1} \Pr(X \ge t)$ and $\mathbb{E}[X^2] = \sum_{t\ge1} (2t-1)\Pr(X\ge t)$. Here $\Pr(\min(U,V) \ge t) = ((P-t+1)/(P+1))^2$ for $1 \le t \le P$; summing via $\sum_{r=1}^P r^2 = P(P+1)(2P+1)/6$ and $\sum r^3 = (P(P+1)/2)^2$ gives both formulas. The last claim is $F(c) = \sum_{t=1}^c (P-t+1)/(P+1)$. ∎

**Theorem 8.2 (C5: means).** $\displaystyle \mathbb{E}[\dim_{\mathbb{F}_q} C] = \frac{n}{2} \sum_s m_s$, and
$$\mathbb{E}[\dim_{\mathbb{F}_q} \mathrm{Hull}_k(C)] = \nu_P \sum_{O:\, L_O = 1} w_O + \mu_P \sum_{O:\, L_O \ge 2} w_O L_O .$$

*Proof.* $\mathbb{E}[P - A_f] = P/2$ and $\sum_{f \in \mathcal{F}_s} \deg f = n_0$ give the first formula via Theorem 5.2. For the hull, linearity over orbits reduces to $\mathbb{E}[S_L]$. If $L \ge 2$, each $X_i$ is the minimum of two independent uniforms (for $L=2$, $X_0, X_1$ are the two ordered pairings of the same two distinct variables), so $\mathbb{E}[S_L] = L\mu_P$ by Lemma 8.1. If $L = 1$, $\mathbb{E}[S_1] = \frac{1}{P+1}\sum_{a=0}^P \min(P-a,a)$; the summands are symmetric under $a \mapsto P-a$, giving $P^2/4$ for $P = 2m$ and $(P^2-1)/4$ for $P = 2m+1$, i.e. $\lfloor P^2/4 \rfloor$; hence $\mathbb{E}[S_1] = \nu_P$. Note $\nu_1 = 0$: at $P=1$ an $L_O=1$ orbit contributes nothing, and $\mathbb{E}[\mathrm{Hull}] = \frac14 \sum_{L_O\ge2} w_O L_O$. ∎

For the variance, orbit contributions are independent (disjoint exponent variables), so with $V_L(P) := \mathrm{Var}(S_L)$, $\mathrm{Var}(\dim_{\mathbb{F}_q}\mathrm{Hull}_k) = \sum_{s,O} w_O^2 V_{L_O}(P)$; note the squared weights, in contrast to the mean.

**Lemma 8.3 (variance pieces).**
(i) $L=1$: $V_1(P) = \dfrac{P(P+2)(P^2+2P+4)}{48(P+1)^2}$ if $P$ is even, and $V_1(P) = \dfrac{(P-1)(P+3)}{48}$ if $P$ is odd.
(ii) For $L \ge 3$, two adjacent edges satisfy $\mathrm{Cov}(X_i, X_{i+1}) = \kappa_P := -\dfrac{P(P+2)(7P^2+14P+9)}{360(P+1)^2} < 0$, while non-adjacent edge pairs are independent.
(iii) For $L=2$: $\mathbb{E}[X_0 X_1] = \dfrac{P^2(P-1)}{12(P+1)}$ and $\mathrm{Cov}(X_0,X_1) = -\dfrac{P^2(P+2)^2}{36(P+1)^2}$.

*Proof.* (i) $\mathbb{E}[\min(P-A,A)^2] = \frac{1}{P+1}\sum_a \min(P-a,a)^2$; for $P = 2m$ the squared values are $0^2,\dots,(m-1)^2,m^2,(m-1)^2,\dots,0^2$, summing to $m(2m^2+1)/3$, and for $P=2m+1$ each of $0^2,\dots,m^2$ occurs twice, summing to $m(m+1)(2m+1)/3$; subtracting $\nu_P^2$ (Theorem 8.2) and simplifying gives the claim.
(ii) $X_i, X_{i+1}$ share exactly the variable $A_i$. Conditioning on $A_i = b$ makes them conditionally independent with means $F(P-b)$ and $F(b)$ (Lemma 8.1), so $\mathbb{E}[X_iX_{i+1}] = \frac{1}{P+1}\sum_{b=0}^P F(P-b)F(b) = \frac{P(P-1)(11P^2+15P+6)}{120(P+1)^2}$ by the power sums $\sum b^j$, $j \le 4$; subtracting $\mu_P^2$ gives $\kappa_P$, negative for $P \ge 1$. Non-adjacent edges depend on disjoint pairs of variables, hence are independent.
(iii) $X_0 \ge s$ and $X_1 \ge t$ hold simultaneously iff $s + t \le P$, in which case each of the two variables has $P-s-t+1$ admissible values; thus $\mathbb{E}[X_0X_1] = \sum_{s,t\ge1} \Pr(X_0\ge s, X_1\ge t) = \frac{1}{(P+1)^2} \sum_{r=1}^{P-1} (P-r) r^2 = \frac{P^2(P-1)}{12(P+1)}$, and subtracting $\mu_P^2$ gives the covariance. ∎

**Theorem 8.4 (C6: variance of the hull dimension).** $\displaystyle \mathrm{Var}\big(\dim_{\mathbb{F}_q} \mathrm{Hull}_k(C)\big) = \sum_{s} \sum_{O \in \mathcal{O}_s} w_O^2\, V_{L_O}(P)$, where $V_1(P)$ is as in Lemma 8.3(i), $V_2(P) = \dfrac{P(P+2)(P^2+2P+3)}{18(P+1)^2}$, and $V_L(P) = \dfrac{L\, P(P+2)(P^2+2P+2)}{60(P+1)^2}$ for $L \ge 3$.

*Proof.* Independence across orbits gives the weighted sum. For one orbit: $L=1$ is Lemma 8.3(i). For $L=2$, $\mathrm{Var}(S_2) = 2\mathrm{Var}(X) + 2\mathrm{Cov}(X_0,X_1)$; with $\mathrm{Var}(X) = \frac{P(P+2)(2P^2+4P+3)}{36(P+1)^2}$ (from Lemma 8.1) and (iii), the bracket factors as $P(P+2)(P^2+2P+3)$, giving $V_2(P)$. For $L \ge 3$, $\mathrm{Var}(S_L) = L\mathrm{Var}(X) + 2L\kappa_P$ (exactly the $L$ adjacent pairs contribute, by (ii)), and $\mathrm{Var}(X) + 2\kappa_P = \frac{P(P+2)(P^2+2P+2)}{60(P+1)^2}$. At $P=1$: $V_1(1) = 0$, $V_2(1) = 1/4$, $V_L(1) = L/16$. The $L=2$ formula is not the $L \ge 3$ formula evaluated at $L=2$ (at $P=2$: $44/81$ versus $8/27$), because the two edges of a 2-orbit share both variables. ∎

## 9. Examples and computational verification

**Example 9.1 (one orbit, $P=2$, $L=2$, $w=1$, by hand).** The nine assignments $\alpha = (\alpha_0,\alpha_1)$ give $(\sum_i (2-\alpha_i), \sum_i \min(2-\alpha_i,\alpha_{i-1}))$ as follows: $(0,0)\mapsto(4,0)$, $(0,1)\mapsto(3,1)$, $(0,2)\mapsto(2,2)$, $(1,0)\mapsto(3,1)$, $(1,1)\mapsto(2,2)$, $(1,2)\mapsto(1,1)$, $(2,0)\mapsto(2,2)$, $(2,1)\mapsto(1,1)$, $(2,2)\mapsto(0,0)$. Hence $\mathbb{E}[S_2] = 10/9 = 2\mu_2$, $\mathrm{Var}(S_2) = 44/81 = V_2(2)$ (the $L=2$ case of Theorem 8.4), and exactly two assignments have hull contribution $0$, as Corollary 7.3 requires per orbit.

**Example 9.2 (simple-root orbit, $P=1$, $L=3$, $w=1$).** The joint distribution is $\{(0,0):1,\ (1,1):3,\ (2,1):3,\ (3,0):1\}$: the hull contribution counts $1\to0$ transitions (Proposition 6.4), with $\mathbb{E} = 3/4 = 3\mu_1$ and variance $3/16 = V_3(1)$.

**Example 9.3 (a repeated-root field case).** Take $K = \mathbb{F}_4$, $k=1$, $\lambda=1$, $P=2$, $n_0=5$, $n=10$. The factors of $x^5-1$ over $\mathbb{F}_4$ have degrees $1,2,2$, with $\tau$-orbit lengths $1,2$; there are $3^3=27$ assignments. The joint $(\dim_K C, \dim_K \mathrm{Hull}_1(C))$ distribution, computed directly from generator polynomials and the rank of the code-first Gram matrix $\big(\sum_j B_{t,j}\sigma(B_{r,j})\big)$, is
$$\{(0,0):1, (1,1):1, (2,0):1, (2,2):2, (3,3):2, (4,2):2, (4,4):3, (5,5):3, (6,2):2, (6,4):3, (7,3):2, (8,0):1, (8,2):2, (9,1):1, (10,0):1\},$$
in agreement with Theorems 5.2 and 6.3. It gives $\mathbb{E}[\mathrm{Hull}] = 23/9 = \nu_2 + 2\cdot 2\mu_2 = \tfrac13 + \tfrac{20}{9}$ (the length-one orbit contributes through $\nu_2$, not $\mu_2$), $\mathrm{Var}(\mathrm{Hull}) = 194/81$ from Theorem 8.4, LCD count $4 = 2^2$, and self-orthogonal $=$ dual-containing count $12$.

**Example 9.4 (orbit of length 6).** Take $K = \mathbb{F}_8$, $k=1$, $\lambda=1$, $P=2$, $n_0=7$, $n=14$. The seven linear factors of $x^7-1$ form $\tau$-orbits of lengths $1$ and $6$; over the $3^7 = 2187$ assignments the Gram-rank computation again agrees with Theorems 5.2 and 6.3 assignment by assignment, with $\mathbb{E}[\mathrm{Hull}] = 11/3$, $\mathrm{Var}(\mathrm{Hull}) = 10/9 = V_1(2) + V_6(2) = \tfrac29 + \tfrac89$, LCD count $4$, and self-orthogonal $=$ dual-containing count $258$. Because the exponent formula is checked against the actual hull dimensions of actual codes on an orbit of length $6$, this example also certifies the predecessor orientation $\alpha_{i-1}$: on such an orbit the predecessor and successor readings give different hull dimensions for generic $\alpha$, so the check would detect a transposed convention (cf. the remark after Theorem 6.3).

**Example 9.5 (two components).** For $A = \mathbb{F}_2 \times \mathbb{F}_4$ ($q=2$, $k=0$, $\lambda=(1,1)$, $P=2$, $n_0=7$), the orbit data $(L_O, w_O)$ are $(1,1), (2,3)$ and $(1,2), (2,6)$. Convolving the per-orbit distributions of Theorem 6.1 gives the global joint distribution over $3^6 = 729$ labeled assignments, with LCD count $16 = 2^4$, self-orthogonal and dual-containing counts $144$ each, $\mathbb{E}[\mathrm{Hull}] = 11$ (Theorem 8.2), and $\mathrm{Var}(\mathrm{Hull}) = 230/9$ (Theorem 8.4); the same numbers result from adding independently computed component dimensions.

**Computational verification.** All formulas above were checked by exact (integer and rational) computation in three independent ways: direct enumeration of exponent tuples; the transfer traces of Theorem 6.1 evaluated both as polynomial matrices and at integer points; and Gram-rank brute force over explicitly constructed codes in the cases of Examples 9.3–9.5 and further cases ($\mathbb{F}_4$ with $n_0=3$; $\mathbb{F}_9$ with $k=1$, $\lambda = \pm 1$, $P=3$; $\mathbb{F}_3$ with $\lambda=-1$, $P=3$), comprising $2769$ field-level assignments in total, in addition to an orbit grid of $52$ pairs $(P,L)$, $P \in \{1,2,3,4,5,7,8,9\}$. The moment closed forms were also re-derived symbolically from their defining sums. These computations are supporting evidence for the tested cases; the proofs of Sections 3–8 are independent of them.

## 10. Limitations and scope

- **Labeled counting.** All enumerations count labeled exponent assignments over a fixed labeled decomposition $A \cong \prod_s K_s$. They are not counts of equivalence or isometry classes of codes, and no such interpretation should be attached to $\mathcal{E}(u,z)$.
- **Compatible twists only.** For incompatible $\lambda_s$, Theorem 4.3 persists in the two-modulus form $x^n - \lambda_s^{-p^{d_s-k}}$, but the hull formula and everything following it are not asserted.
- **Square-free affine algebra.** The assembly (Proposition 6.2) uses the direct-product structure of $A$; non-reduced alphabets (e.g. chain rings) are outside the scope.
- **Moment model.** The means and variances of Section 8 refer to the uniform distribution on labeled assignments. Orbit contributions are independent in this model; edges within an orbit are not (Lemma 8.3), and the $L=1$, $L=2$, $L\ge3$ regimes are genuinely distinct.
- **Convention dependence.** The predecessor index $\alpha_{i-1}$ in Theorems 4.3–6.3 is tied to the code-first pairing of Section 2; reading the pairing in the opposite order replaces $\rho$ by $\sigma$ and $\alpha_{i-1}$ by $\alpha_{i+1}$. Since the joint distribution is unchanged under orbit reversal, this convention must be stated, as here, rather than inferred from the enumerator.

**Remark (conditional quantum remark).** In the finite-field case ($N=1$, $m_1=1$), a code $C$ with parameters $[n, K]$ and $\dim \mathrm{Hull}_k(C) = H$ whose minimum distance $d$ is known independently gives, by the standard entanglement-assisted construction [BDS2006], an $[[n, K-H, d;\, n-K-H]]$ entanglement-assisted quantum code. The enumerator of Theorem 6.3 determines the joint distribution of $(K, H)$ only; it yields no distance information, and no quantum parameter should be claimed from it alone. The affine case requires, in addition, control of distances under the product decomposition.

## 11. Conclusion

For repeated-root constacyclic codes over a square-free affine algebra with compatible twists, the joint distribution of code dimension and Galois hull dimension over all labeled exponent assignments is given by a product of transfer-matrix traces indexed by the orbits of the reciprocal involution. The enumerator yields the total count, the code-dimension distribution, the LCD count $2^{\#\mathrm{orbits}}$, the self-orthogonal and dual-containing counts, and exact mean and variance formulas in which length-one orbits enter through the separate constant $\nu_P$. At $P=1$ the theory reduces to the binary simple-root enumerator. Natural directions for further work include the incompatible-twist regime, where the dual already exists in a two-modulus form but the hull intersection must be reconsidered; counting up to monomial equivalence rather than by labeled assignments; and distance questions, which the enumerator alone does not address.

## References

- [BDS2006] T. Brun, I. Devetak, and M.-H. Hsieh, Correcting quantum errors with entanglement, *Science* 314 (2006), 436–439.
- [CDL2015] B. Chen, H. Q. Dinh, and H. Liu, *Finite Fields and Their Applications* 33 (2015), 137–159. doi:10.1016/j.ffa.2014.11.006.
- [DP2025] I. Debnath and O. Prakash, Average dimensions of Galois hulls of constacyclic codes, *Advances in Mathematics of Communications* 19(6) (2025), 1569–1604. doi:10.3934/amc.2025010.
- [DIMP2026] I. Debnath, H. Islam, E. Martínez-Moro, and O. Prakash, Galois hulls of constacyclic codes over affine algebra rings, *Discrete Mathematics* 349(2) (2026), Article 114750. doi:10.1016/j.disc.2025.114750; arXiv:2412.08512.
- [DIYP2026] I. Debnath, H. Islam, S. Yadav, and O. Prakash, Study of small Galois hull dimensions of constacyclic codes, *Advances in Mathematics of Communications* 22 (2026), 1–18. doi:10.3934/amc.2025054.
- [DPI2023] I. Debnath, O. Prakash, and H. Islam, Galois hulls of constacyclic codes over finite fields, *Cryptography and Communications* 15(1) (2023), 111–127. doi:10.1007/s12095-022-00591-6.
- [DPI2023corr] I. Debnath, O. Prakash, and H. Islam, Correction to: Galois hulls of constacyclic codes over finite fields, *Cryptography and Communications* 15 (2023), 129–130. doi:10.1007/s12095-022-00602-6.
- [ES2026] R. F. Taki Eldin and P. Solé, Generator polynomial matrices of the Galois hulls of multi-twisted codes, *Finite Fields and Their Applications* 109 (2026), Article 102712. doi:10.1016/j.ffa.2025.102712; arXiv:2305.15237.
- [HP2003] W. C. Huffman and V. Pless, *Fundamentals of Error-Correcting Codes*, Cambridge University Press, 2003.
- [MS1977] F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes*, North-Holland, 1977.
- [Sharma2015] A. Sharma, *Cryptography and Communications* 7 (2015), 229–255. doi:10.1007/s12095-014-0106-5.
- [Talbi2021] Talbi, Batoul, Fotue Tabue, and Martínez-Moro, Galois hulls of cyclic serial codes over a finite chain ring, arXiv:2102.06995 (2021).
- [WZLL2023] Wu, Zhu, Liu, and Li, *Advances in Mathematics of Communications* 17(5) (2023), 1154–1180. doi:10.3934/amc.2021044.
- [ZKZ2026] Zhang, Kong, and Zheng, Quantum codes from Galois hulls of constacyclic codes over a finite non-chain ring, *Entropy* 28 (2026), 407. doi:10.3390/e28040407.
- [ZWLL2025] Zhang, Wang, Luo, and Li, *Finite Fields and Their Applications* 101 (2025), Article 102542. doi:10.1016/j.ffa.2024.102542.
