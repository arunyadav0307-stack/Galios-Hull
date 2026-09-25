// Typst port of manuscript/main.tex (same text, mathematics, and numbering).
// Used ONLY to render manuscript/main.pdf in this sandbox, which has no TeX
// engine and no network route to TeX distributions. The LaTeX source remains
// the authoritative manuscript; see CHANGELOG.md (build-chain note).

#set page(paper: "us-letter", margin: 1in)
#set text(size: 11pt)
#set par(justify: true, first-line-indent: 1.5em, spacing: 0.65em)
#set block(spacing: 0.9em)
#set heading(numbering: "1.")
#show heading.where(level: 1): set text(size: 14.4pt, weight: "bold")
#show heading.where(level: 2): set text(size: 12pt, weight: "bold")
#set math.equation(numbering: "(1)")
#show figure.where(kind: table): set figure.caption(position: top)
#show figure.where(kind: "theorem"): it => block(width: 100%, breakable: true)[#set par(first-line-indent: 0pt); *#it.supplement #it.counter.display(it.numbering)*#it.body]
#show figure.where(kind: "lemma"): it => block(width: 100%, breakable: true)[#set par(first-line-indent: 0pt); *#it.supplement #it.counter.display(it.numbering)*#it.body]
#show figure.where(kind: "proposition"): it => block(width: 100%, breakable: true)[#set par(first-line-indent: 0pt); *#it.supplement #it.counter.display(it.numbering)*#it.body]
#show figure.where(kind: "corollary"): it => block(width: 100%, breakable: true)[#set par(first-line-indent: 0pt); *Corollary 4.#it.counter.display(it.numbering)*#it.body]
#show figure.where(kind: "example"): it => block(width: 100%, breakable: true)[#set par(first-line-indent: 0pt); *#it.supplement #it.counter.display(it.numbering)*#it.body]
#let E(l) = context [Equation~(#counter(math.equation).at(l).at(0))]
#let T(l) = context [Theorem~#counter(figure.where(kind: "theorem")).at(l).at(0)]
#let Tn(l) = context [#counter(figure.where(kind: "theorem")).at(l).at(0)]
#let L(l) = context [Lemma~#counter(figure.where(kind: "lemma")).at(l).at(0)]
#let Ln(l) = context [#counter(figure.where(kind: "lemma")).at(l).at(0)]
#let P(l) = context [Proposition~#counter(figure.where(kind: "proposition")).at(l).at(0)]
#let Pn(l) = context [#counter(figure.where(kind: "proposition")).at(l).at(0)]
#let C(l) = context [Corollary~4.#counter(figure.where(kind: "corollary")).at(l).at(0)]
#let Cn(l) = context [4.#counter(figure.where(kind: "corollary")).at(l).at(0)]
#let S(l) = context { let n = counter(heading).at(l); [Section~#n.map(str).join(".")] }
#let Sn(l) = context { let n = counter(heading).at(l); [#n.map(str).join(".")] }
#let Tab(l) = context [Table~#counter(figure.where(kind: table)).at(l).at(0)]
#let Ex(l) = context [Example~#counter(figure.where(kind: "example")).at(l).at(0)]
#let Exn(l) = context [#counter(figure.where(kind: "example")).at(l).at(0)]
#let Proof(body) = block(width: 100%, breakable: true)[#set par(first-line-indent: 0pt); *Proof.* #body #h(1fr) #sym.square.stroked]
#let U(body) = [#set math.equation(numbering: none); #body]

// ---------- front matter ----------
#align(center, text(size: 14.4pt, weight: "bold")[Exact Joint Enumeration of $k$-Galois Hull Dimensions for Labeled Constacyclic Codes over Square-Free Affine Algebras])
#line(length: 100%, stroke: 0.8pt)

*Abstract*

We study the joint distribution of code dimension and $k$-Galois hull dimension for a fixed labeled family of constacyclic codes over a square-free affine algebra. Decomposing the algebra into finite-field components, the condition $"gcd"(n, p) = 1$ makes every component constacyclic modulus simple-root, so that each component code is determined by a binary selection of irreducible factors. For the code-first second-slot pairing, we first derive the inverse-Frobenius reciprocal, its action on irreducible factors, and the resulting hull-support formula. Under a compatible same-factor-set condition, this support then becomes a weighted cyclic $1$-to-$0$ boundary statistic on reciprocal factor orbits. A weighted two-state transfer matrix and a cyclic trace give the exact labeled joint generating polynomial in the code-dimension and hull-dimension variables. Its specializations yield the total labeled-code count, the code- and hull-dimension distributions, the LCD count, and the mean and variance of the hull dimension, including the short-orbit variance exception. The candidate-first comparison convention is treated separately. All results are conditional on the stated hypotheses, and no priority claim is made.

#block[*Keywords:* $k$-Galois hulls; constacyclic codes; square-free affine algebras; exact labeled enumeration; generating polynomials; transfer matrices; finite-field decomposition.]
#block[*2020 MSC:* 94B05, 94B15, 05A15.]
#line(length: 100%, stroke: 0.8pt)

// ---------- 1. Introduction ----------
= Introduction

The intersection of a linear code with its dual, its hull, is a structural invariant of the code. Hulls appear in the study of code intersections, complementary-dual codes, automorphism questions, and conditional quantum-code constructions. The $k$-Galois hull generalizes the Euclidean and Hermitian cases by applying a Frobenius automorphism in one slot of the pairing. For constacyclic codes, the ambient polynomial factorization makes duality and intersection questions amenable to algebraic analysis.

Exact enumeration questions have been studied in several narrower settings. Hulls of cyclic and negacyclic codes over finite fields, including fixed-dimension counts, were treated through reciprocal factors and related polynomial descriptions \[1\]. For constacyclic codes over finite fields, Galois-hull formulas and restricted prescribed-dimension counts were reported together with a correction record; the complete corrected theorem text is not imported here \[2, 3\]. Average-dimension and small-dimension Galois-hull records provide further neighboring context \[4, 5\].

Related exact counts are available for cyclic serial codes over a finite chain ring \[6\], for cyclic codes over $bb(Z)_4$ \[7, 8\], for double cyclic codes \[9\], and for double or four circulant codes \[10\]. A restricted direct-product and non-chain record also supplies adjacent componentwise hull formulas \[11\]. The closest structural record for the present setting studies Galois hulls of constacyclic codes over an affine algebra through finite-field component decompositions \[12, 13\]. Its accessible theorem-bearing version and its final publisher record are distinct records, and its convention places the candidate in the opposite slot from the convention used below; we therefore state and prove the convention transformation rather than silently identifying the two dual codes. #Tab(<tab:literature>) summarizes this scoped comparison.

#align(center)[
#show table.cell: set text(size: 8pt)
#show table.cell: set par(justify: false, first-line-indent: 0pt)
#figure(
table(columns: (23fr, 34fr, 31fr), stroke: 0.5pt, align: left,
[*Literature setting*], [*Result used in this paper*], [*Scope qualification*],
[Finite-field cyclic/negacyclic], [Hull formulas and fixed-dimension counts \[1\]], [Narrower field and cyclic/negacyclic families.],
[Finite-field constacyclic], [Galois-hull formulas and restricted counts \[2, 3\]], [Correction recorded; complete corrected text requires a pre-submission check.],
[Chain-ring and $bb(Z)_4$], [Fixed-hull or average-type enumeration \[6, 7, 8\]], [Nilpotent/chain-ring hypotheses differ from the reduced affine product.],
[Non-chain and generalized cyclic], [Component hull formulas or prescribed-hull counts \[11, 9, 10\]], [Different rings or code families; no target-product transfer.],
[Average/small-dimension Galois hulls], [Adjacent average and small-dimension records \[4, 5\]], [Background only; not the complete labeled joint polynomial.],
),
caption: [Literature comparison used for scoped background. The table does not assert an exhaustive priority result.],
) <tab:literature>
]

#h(1.5em)An exact joint enumeration of labeled constacyclic codes over a square-free affine algebra by code dimension and hull dimension together, in the form of a complete bivariate generating polynomial, is not established in the scoped literature above. This paper addresses the following conditional question. Suppose that a fixed square-free affine algebra has labeled field components, that each component modulus $x^n - lambda_s$ is simple-root, and that the inverse-Frobenius reciprocal preserves the same factor set. Can all distinct labeled factor selections be counted jointly by their global code dimension and their code-first $k$-Galois hull dimension? The answer is an exact product over reciprocal factor orbits.

Our contribution, stated without any priority claim, is a self-contained exact joint generating polynomial for code dimension and code-first $k$-Galois hull dimension under explicit square-free, simple-root, compatible-twist, fixed-component, and labeled-factor hypotheses. The polynomial factors over reciprocal factor orbits and is expressed through a weighted two-state transfer matrix and a cyclic trace. We derive the inverse-Frobenius reciprocal and its factor action, the code-first dual generator and hull-support formula, the cyclic boundary statistic, the one-orbit polynomial and its transfer-matrix form, and the global joint enumerator with its total-count, distribution, LCD-count, mean, and variance consequences. The candidate-first comparison convention is treated separately, and finite instances are validated computationally through independent routes. We did not find in the scoped literature an exact prior theorem identical to the weighted bivariate product proved here; this is not a universal absence claim.

The joint enumerator determines, by coefficient extraction, how many labeled codes realize each pair of code and hull dimensions; its specializations give the LCD count and the mean and variance of the hull dimension over the labeled family. Hull-dimension data of this kind may provide input to a quantum-code construction only after additional independent hypotheses and proofs: no quantum distance, parameter, optimality, or fault-tolerance conclusion follows from the enumerator alone.

This paper is organized as follows. #S(<sec:prelim>) collects the preliminaries: the square-free affine algebra and its decomposition, constacyclic codes with labeled factor selections, and the code-first Galois pairing with its global form. #S(<sec:duality>) develops code-first duality for component codes: the inverse-Frobenius reciprocal and compatibility condition, the dual generator with the candidate-first comparison, and the hull-support formula with its cyclic boundary statistic. #S(<sec:enumeration>) gives the exact enumeration: the one-orbit polynomial, the transfer-matrix representation, the global joint enumerator, and its consequences. #S(<sec:examples>) presents worked examples and the computational validation. #S(<sec:conclusion>) concludes with the scope of the results and directions for future work.

// ---------- 2. Preliminaries ----------
= Preliminaries <sec:prelim>

This section fixes the notation and standing hypotheses used throughout the paper. #Tab(<tab:notation>) at the end of the section collects the symbols for reference.

== Square-free affine algebras and their decomposition

Throughout, $p$ is prime and
#U[$ q = p^e, quad e gt.eq 1. $]
For each component index $s$, let
#U[$ K_s = bb(F)_(q^(m_s)) = bb(F)_(p^(d_s)), quad d_s = e m_s, quad m_s gt.eq 1. $]
The component labels are fixed once and for all, and $cal(A)$ always denotes the ambient affine algebra.

The affine algebra is presented as
$ cal(A) = bb(F)_q [X_1, dots, X_ell] \/ \<t_1(X_1), dots, t_ell(X_ell)\>, $ <eq:algebra>
where $ell gt.eq 1$ and each $t_i$ is monic, square-free, and of positive degree. Since each $t_i$ is square-free, $cal(A)$ is reduced.

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(Square-free component decomposition).* _The affine algebra_ #E(<eq:algebra>) _has a fixed labeled decomposition_
$ cal(A) tilde.equiv product_(s=1)^N K_s, $ <eq:decomp>
_with finite fields_ $K_s = bb(F)_(q^(m_s))$.]) <prop:decomposition>

#Proof([Factor each relation $t_i$ into pairwise coprime monic irreducibles over $bb(F)_q$. Square-freeness gives pairwise comaximal factors. The Chinese remainder theorem first decomposes each one-variable quotient into finite fields and then decomposes their tensor product into a finite product of finite fields. The component labels are fixed by the chosen decomposition. The positive-degree hypothesis excludes the zero quotient case.])

#h(1.5em)We fix the labeled isomorphism #E(<eq:decomp>) of #P(<prop:decomposition>) throughout. Thus an element of $cal(A)$ is written as a tuple $(a_s)_s$, the primitive product idempotents are fixed by the component labels, and all global constructions below use these tuple coordinates. Dimensions of global objects are taken over $bb(F)_q$, whereas component dimensions are taken over $K_s$.

== Constacyclic codes and labeled factor selections

Fix $n gt.eq 1$ with $"gcd"(n, p) = 1$ and choose $lambda_s in K_s^*$ for every component. Set
#U[$ M_s(x) = x^n - lambda_s. $]
Since $"gcd"(n, p) = 1$, each $M_s$ is square-free. Let $cal(F)_s$ be the set of distinct monic irreducible factors of $M_s$ over $K_s$. For a subset $J_s subset.eq cal(F)_s$, define
#U[$ g_(J_s)(x) = product_(f in J_s) f(x), quad h_(J_s)(x) = M_s(x) / g_(J_s)(x). $]
The component code $C_s(J_s)$ is the principal ideal generated by $g_(J_s)$ in $K_s[x] / \<M_s\>$. We use $epsilon = 1$ for a factor selected in the generator; thus a selected factor contributes to codimension rather than directly to code dimension.

#figure(kind: "lemma", supplement: [Lemma], placement: none, numbering: "1", [*~(Factor-selection parametrization).* _For each $s$, the distinct constacyclic ideals in the simple-root quotient $K_s[x] / \<M_s\>$ are in bijection with subsets $J_s subset.eq cal(F)_s$. Their $K_s$-dimension is_
#U[$ "dim"_(K_s) C_s(J_s) = n - sum_(f in J_s) "deg"(f). $]
_The global product code has $bb(F)_q$-dimension_
#U[$ "dim"_(bb(F)_q) C(J) = sum_(s=1)^N m_s "dim"_(K_s) C_s(J_s). $]]) <lem:factor-selection>

#Proof([The simple-root quotient is a product of fields indexed by the distinct irreducible factors of $M_s$. A principal ideal is obtained by choosing which factor components vanish, equivalently by choosing the product $g_(J_s)$. Unique factorization gives injectivity of the selection-to-ideal map, and every ideal is obtained in this way. The usual degree formula gives the component dimension. Since $[K_s : bb(F)_q] = m_s$, the global dimension is the weighted sum displayed above.])

#h(1.5em)The global selection space is therefore
#U[$ scr(C) = product_(s=1)^N \{J_s : J_s subset.eq cal(F)_s\}, wide abs(scr(C)) = 2^(sum_s abs(cal(F)_s)). $]
This is a labeled factor-selection count: no quotient by rotations, automorphisms, isometries, or code equivalence is taken.

The component twists assemble into the global tuple
#U[$ lambda = (lambda_s)_(s=1)^N in cal(A)^*. $]
The global constacyclic ambient module is
$ cal(M)_lambda = cal(A)[x] / \<x^n - lambda\> tilde.equiv product_(s=1)^N K_s[x] / \<x^n - lambda_s\> tilde.equiv product_(s=1)^N K_s^n, $ <eq:ambient>
where the last identification is the coefficient-vector identification. The global constacyclic shift is therefore componentwise, and the fixed CRT isomorphism embeds a global code in $cal(A)^n$ as a tuple of component codes.

#figure(kind: "lemma", supplement: [Lemma], placement: none, numbering: "1", [*~(Global CRT ambient module and factor-selection code).* _For $J = (J_s)_s in scr(C)$, define_
#U[$ C(J) = product_(s=1)^N C_s(J_s) subset.eq product_(s=1)^N K_s^n tilde.equiv cal(A)^n. $]
_Equivalently, $C(J)$ is the ideal of $cal(M)_lambda$ generated by the tuple $g_J = (g_(J_s))_s$. Different labeled tuples $J != J'$ give different global codes._]) <lem:global-code>

#Proof([The product and coefficient-vector identifications are the CRT isomorphisms #E(<eq:ambient>). If $J != J'$, choose a component $s$ with $J_s != J'_s$. #L(<lem:factor-selection>) gives $C_s(J_s) != C_s(J'_s)$, so their products have different $s$-components and are different global codes.])

== The code-first Galois pairing and the global code

For $x = (x_i)$ and $y = (y_i)$ in $K_s^n$, define
#U[$ sigma_(s,k)(a) = a^(p^k), quad rho_(s,k)(a) = a^(p^(d_s - k)) = sigma_(s,k)^(-1), quad 0 lt.eq k lt e, $]
When the component index is understood, we write the abbreviated maps
#U[$ sigma(a) = a^(p^k), quad rho(a) = a^(p^(d_s - k)). $]
The code-first second-slot pairing is
$ \<x, y\>_(s,k) = sum_(i=0)^(n-1) x_i sigma_(s,k)(y_i) = sum_(i=0)^(n-1) x_i y_i^(p^k). $ <eq:pairing>
Suppressing the component label, we write
#U[$ \<x, y\>_k = sum_i x_i y_i^(p^k). $]
The code-first dual is
#U[$ D_("code-first")(C) = \{y in K_s^n : \<c, y\>_(s,k) = 0 "for every" c in C\}, $]
and the code-first hull is
#U[$ "Hull"_k(C) = C inter D_("code-first")(C). $]
The pairing #E(<eq:pairing>) is $K_s$-linear in its first argument and $sigma_(s,k)$-semilinear in its second argument; the defining annihilator is nevertheless a $K_s$-linear subspace.

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(Code-first dual translation).* _For every $K_s$-linear code $C subset.eq K_s^n$,_
#U[$ D_("code-first")(C) = rho_(s,k)(C^(perp_E)), $]
_where $C^(perp_E)$ is the ordinary Euclidean dual and $rho_(s,k)$ acts coordinatewise._]) <prop:dual-translation>

#Proof([The code-first condition is $sum_i c_i sigma_(s,k)(y_i) = 0$ for every $c in C$. Setting $z = sigma_(s,k)(y)$ gives $z in C^(perp_E)$, and applying the inverse coordinatewise map gives $y = rho_(s,k)(z)$.])

#figure(kind: "lemma", supplement: [Lemma], placement: none, numbering: "1", [*~(Global Frobenius and code-first pairing).* _Define the componentwise maps on $cal(A)$ by_
#U[$ sigma_(cal(A), k)((a_s)_s) = (sigma_(s,k)(a_s))_s, wide rho_(cal(A), k)((a_s)_s) = (rho_(s,k)(a_s))_s. $]
_They are mutually inverse ring automorphisms and are semilinear over $bb(F)_q$ with respect to the base-field Frobenius. On $cal(A)^n$, define the $cal(A)$-valued global code-first pairing_
#U[$ \<x, y\>_(cal(A), k) = sum_(i=0)^(n-1) x_i sigma_(cal(A), k)(y_i) = lr((sum_(i=0)^(n-1) x_(s,i) y_(s,i)^(p^k)))_(s=1)^N. $]
_For a global code $C subset.eq cal(A)^n$, define_
#U[$ D_(cal(A), k)(C) = \{y in cal(A)^n : \<c, y\>_(cal(A), k) = 0_(cal(A)) "for every" c in C\}, wide "Hull"_(cal(A), k)(C) = C inter D_(cal(A), k)(C). $]]) <lem:global-pairing>

#Proof([Each $sigma_(s,k)$ is a field automorphism of $K_s$ with inverse $rho_(s,k)$, and the product of component automorphisms is a ring automorphism of $cal(A)$. The product idempotents are fixed because their coordinates are $0$ or $1$. The displayed pairing is the componentwise tuple of the already-defined component pairings; zero in $cal(A) tilde.equiv product_s K_s$ means zero in every component.])

#figure(kind: "lemma", supplement: [Lemma], placement: none, numbering: "1", [*~(Global code-first dual decomposition).* _For every labeled factor-selection code,_
#U[$ D_(cal(A), k)(C(J)) = product_(s=1)^N D_("code-first")(C_s(J_s)). $]]) <lem:global-dual>

#Proof([Let $y = (y_s)_s$. If $y in D_(cal(A), k)(C(J))$, fix $s$ and choose a global codeword whose $s$-component is an arbitrary $c_s in C_s(J_s)$ and whose other components are zero. The $s$-component of the global pairing is then $\<c_s, y_s\>_(s,k)$, so it is zero for every $c_s$; hence $y_s in D_("code-first")(C_s(J_s))$. This proves one inclusion. Conversely, if every $y_s$ belongs to its component dual, then every component of $\<c, y\>_(cal(A), k)$ is zero for every $c in C(J)$, so the tuple pairing is $0_(cal(A))$.])

#figure(kind: "lemma", supplement: [Lemma], placement: none, numbering: "1", [*~(Global hull decomposition).* _The global code-first hull decomposes as_
#U[$ "Hull"_(cal(A), k)(C(J)) = product_(s=1)^N "Hull"_k(C_s(J_s)). $]]) <lem:global-hull>

#Proof([Use the preceding dual decomposition and the elementary identity $(product_s U_s) inter (product_s V_s) = product_s (U_s inter V_s)$ for subspaces in a finite direct product.])

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(Global $bb(F)_q$-dimension additivity).* _For every $J in scr(C)$,_
#U[$ "dim"_(bb(F)_q) C(J) = sum_(s=1)^N m_s "dim"_(K_s) C_s(J_s), wide "dim"_(bb(F)_q) "Hull"_(cal(A), k)(C(J)) = sum_(s=1)^N m_s "dim"_(K_s) "Hull"_k(C_s(J_s)). $]
_In particular, an orbit factor of common $K_s$-degree $d_O$ contributes the global weight $w_O = m_s d_O$._]) <prop:global-dimensions>

#Proof([The $bb(F)_q$-dimension of a finite direct product is the sum of the component $bb(F)_q$-dimensions, and $[K_s : bb(F)_q] = m_s$. Apply the component-to-base-field conversion to the global code and to the global hull decomposition. A factor of $K_s$-degree $d_O$ contributes $m_s d_O$ over $bb(F)_q$.])

#h(1.5em)For a labeled selection define its generator-factor support and its surviving CRT support by
#U[$ "Supp"_("gen")(J) = \{(s, f) : f in J_s\}, wide "Supp"_("CRT")(C(J)) = \{(s, f) : f in cal(F)_s without J_s\}. $]
For any component or global ideal, $"Supp"_("CRT")$ denotes the set of factor components on which the ideal is nonzero. The global hull support is the union of the component hull supports of #L(<lem:global-hull>), and its $bb(F)_q$-dimension is the sum in #P(<prop:global-dimensions>).

#Tab(<tab:notation>) collects the notation and standing assumptions used in the component and global constructions.

#align(center)[
#show table.cell: set text(size: 10pt)
#show table.cell: set par(justify: false, first-line-indent: 0pt)
#figure(
table(columns: 3, stroke: 0.5pt, align: left,
[*Symbol*], [*Meaning*], [*Scope*],
[$bb(F)_q$], [base field of size $q = p^e$], [fixed],
[$K_s$], [component field $bb(F)_(q^(m_s))$], [component $s$],
[$d_s$], [absolute component degree $e m_s$], [$d_s = e m_s$],
[$sigma_(s,k)$], [Frobenius map], [$a mapsto a^(p^k)$],
[$rho_(s,k)$], [inverse Frobenius], [$a mapsto a^(p^(d_s - k))$],
[$\<x, y\>_(s,k)$], [code-first pairing], [second-slot $p^k$ map],
[$cal(A)$], [square-free affine algebra], [labeled product],
[$n$], [constacyclic length], [$"gcd"(n, p) = 1$],
[$lambda_s$], [component twist], [$lambda_s^(1+p^(d_s-k)) = 1$],
[$k$], [Frobenius iteration], [$0 lt.eq k lt e$],
[$cal(F)_s$], [irreducible factor set of $M_s$], [component $s$],
[$J_s$], [selected generator factors], [labeled selection],
[$tau_(s,k)$], [reciprocal factor permutation], [compatible case],
[$a_O, d_O$], [orbit length and factor degree], [orbit $O$],
[$epsilon_i$], [selected-factor indicator], [$epsilon_i = 1$ in $J_s$],
[$b_O$], [cyclic $1$-to-$0$ count], [orbit statistic],
[$T_w(u, z)$], [weighted transfer matrix], [rows source, columns destination],
[$w_O$], [$bb(F)_q$-weight $m_s d_O$], [orbit $O$],
[$scr(E)(u, z)$], [code/hull joint enumerator], [labeled codes],
),
caption: [Core notation and assumptions used in this paper.],
) <tab:notation>
]

// ---------- 3. Galois Duality and Hull Support ----------
= Galois Duality and Hull Support <sec:duality>

In this section, we determine the code-first duals and hull supports of component constacyclic codes. We introduce the inverse-Frobenius reciprocal and the compatibility condition, describe the dual generator together with the candidate-first comparison, and express the hull support as a cyclic boundary statistic on reciprocal orbits.

== The inverse-Frobenius reciprocal and the compatibility condition

Let $f(x) = sum_(i=0)^r f_i x^i$ be monic with $f_0 != 0$. Define the normalized inverse-Frobenius reciprocal
$ f^(\#_(s,k))(x) = rho_(s,k)(f_0)^(-1) sum_(i=0)^r rho_(s,k)(f_i) x^(r-i). $ <eq:reciprocal>

#figure(kind: "lemma", supplement: [Lemma], placement: none, numbering: "1", [*~(Normalized inverse-Frobenius reciprocal).* _The map $f mapsto f^(\#_(s,k))$ is monic, preserves degree and irreducibility, is multiplicative on monic polynomials with nonzero constant term, and is inverted by the corresponding normalized reciprocal using $sigma_(s,k)$._]) <lem:reciprocal>

#Proof([The leading coefficient after reversal is $rho_(s,k)(f_0) != 0$, so the displayed normalization makes the reciprocal monic and of degree $r$. Its constant coefficient is $rho_(s,k)(f_r) / rho_(s,k)(f_0) = rho_(s,k)(f_0)^(-1) != 0$. Reversal satisfies $"rev"(f g) = "rev"(f) "rev"(g)$, and the coefficient map $rho_(s,k)$ is multiplicative; the two normalization factors also multiply, proving multiplicativity on monic polynomials.

#h(1.5em)For the inverse, write $g = f^(\#_(s,k))$ and apply the corresponding normalized reciprocal using $sigma_(s,k)$. Since $g_0 = rho_(s,k)(f_0)^(-1)$, the inverse normalization is $sigma_(s,k)(g_0)^(-1) = f_0$, and coefficient reversal returns $f$. The coefficient automorphism preserves irreducible factorizations, while ordinary reciprocal reversal sends a nontrivial factorization of a polynomial with nonzero constant term to a nontrivial factorization of its reciprocal. Thus irreducibility is preserved.])

#figure(kind: "lemma", supplement: [Lemma], placement: none, numbering: "1", [*~(Root action).* _If $f(alpha) = 0$, then_
#U[$ f^(\#_(s,k))(alpha^(-p^(d_s - k))) = 0. $]
_Thus the induced root map is_
#U[$ alpha mapsto.long alpha^(-p^(d_s - k)). $]]) <lem:root-action>

#Proof([Substitute $alpha^(-p^(d_s - k))$ into the definition of $f^(\#_(s,k))$ and factor the inverse Frobenius through the coefficient sum. The resulting expression is a nonzero scalar multiple of
#U[$ rho_(s,k)(alpha^(-r) f(alpha)) = 0. $]])

#h(1.5em)If $alpha^n = lambda_s$, then
#U[$ (alpha^(-p^(d_s - k)))^n = lambda_s^(-p^(d_s - k)). $]
Consequently, the reciprocal preserves the same factor set precisely under
$ lambda_s^(1+p^(d_s - k)) = 1. $ <eq:compat>
Under this condition, define
#U[$ tau_(s,k) : cal(F)_s arrow.r.long cal(F)_s, quad tau_(s,k)(f) = f^(\#_(s,k)). $]
The map $tau_(s,k)$ is a permutation. It need not be an involution; fixed points and cycles of arbitrary admissible length are allowed.

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(Compatible factor permutation).* _Under $lambda_s^(1+p^(d_s-k)) = 1$, the map $tau_(s,k)$ is a permutation of $cal(F)_s$ and preserves factor degrees. Its cycles therefore partition the labeled factor set into orbits with a common degree on each orbit._]) <prop:compatible-permutation>

#Proof([The root action of #L(<lem:root-action>) sends roots of $M_s$ to roots of the same polynomial under the displayed compatibility condition. By #L(<lem:reciprocal>), the normalized reciprocal #E(<eq:reciprocal>) preserves monicity, irreducibility, and degree, and its inverse is obtained with $sigma_(s,k)$; hence it permutes $cal(F)_s$.])

#h(1.5em)The following ordinary Euclidean reciprocal fact will be used for the dual generator.

#figure(kind: "lemma", supplement: [Lemma], placement: none, numbering: "1", [*~(Ordinary constacyclic reciprocal).* _Let $M(x) = x^n - a$, let $G divides M$ be monic, and put $H = M / G$. If_
#U[$ H^*(x) = H(0)^(-1) sum_(i=0)^("deg" H) H_i x^("deg" H - i), $]
_then the Euclidean dual of the ideal $\<G\>$ in $K[x] / \<M\>$ is the ideal generated by $H^*$ in the $a^(-1)$-constacyclic quotient._]) <lem:ordinary-reciprocal>

#Proof([Write $r = "deg" G$ and $h = "deg" H$, so $r + h = n$. For the non-wrapped generator shifts $x^i G$ and $x^j H^*$, with $0 lt.eq i lt h$ and $0 lt.eq j lt r$, the coefficient pairing is, up to the nonzero scalar $H(0)^(-1)$, the coefficient of degree $h - i + j$ in $G H = x^n - a$. Indeed, reversal changes the index from $u$ in $H$ to $h - u$ in $H^*$, so the aligned terms satisfy $u + v = h - i + j$. Since $1 lt.eq h - i + j lt.eq n - 1$, that coefficient is zero. These shifts therefore span mutually orthogonal spaces.

#h(1.5em)The reciprocal identity
#U[$ H^*(x) = H(0)^(-1) x^h H(x^(-1)) $]
shows that $H^*$ divides the normalized reciprocal of $M = x^n - a$, namely $x^n - a^(-1)$. Hence its ideal is closed under the $a^(-1)$-constacyclic boundary shift; the non-wrapped shifts above form a basis of dimension $r$. This dimension equals the codimension of $\<G\>$, so the orthogonal space is exactly the $a^(-1)$-constacyclic ideal generated by $H^*$.])

== Code-first duals and the candidate-first comparison

We now determine the code-first dual of a component code.

#figure(kind: "theorem", supplement: [Theorem], placement: none, numbering: "1", [*~(Code-first dual generator).* _Let $C_s(J_s) = \<g_(J_s)\>$ be a component code and let $h_(J_s) = M_s / g_(J_s)$. Under the simple-root hypotheses, the code-first dual is generated by the normalized inverse-Frobenius reciprocal $h_(J_s)^(\#_(s,k))$ and is constacyclic with twist_
#U[$ lambda_s^(-p^(d_s - k)). $]
_If the compatibility condition holds, its factor support is_
#U[$ tau_(s,k)(cal(F)_s without J_s). $]]) <thm:dual-generator>

#Proof([First apply $rho_(s,k)$ to the defining equations of the code-first dual. This changes them into ordinary Euclidean annihilation equations for the coordinatewise $rho_(s,k)$-image of the code. By #L(<lem:ordinary-reciprocal>), the ordinary Euclidean dual of a simple-root $a$-constacyclic ideal generated by $g$ is generated by the normalized reciprocal of its check polynomial, with the inverse twist. Applying the coefficientwise inverse Frobenius and normalizing the leading coefficient yields $h_(J_s)^(\#_(s,k))$ and the twist $lambda_s^(-p^(d_s-k))$. #L(<lem:root-action>) gives the factor support.])

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(Same-twist compatibility criterion).* _The code-first dual twist equals the original twist precisely when_
#U[$ lambda_s^(-p^(d_s - k)) = lambda_s, wide "equivalently" wide lambda_s^(1+p^(d_s - k)) = 1. $]
_If this condition fails, the code-first dual belongs to the transformed modulus_
#U[$ x^n - lambda_s^(-p^(d_s - k)), $]
_so the same-factor-set orbit product is not asserted._]) <prop:same-twist>

#Proof([The first equality is the twist in #T(<thm:dual-generator>). Multiplying it by $lambda_s^(p^(d_s-k))$ gives the equivalent displayed power condition. If it fails, the root calculation places the dual in the transformed constacyclic modulus rather than the original same-factor-set quotient.])

#h(1.5em)We now compare the code-first dual with the candidate-first variant used for comparison.

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(Candidate-first/code-first convention transformation).* _For comparison, define_
#U[$ D_("candidate-first")(C) = lr(\{y : sum_i y_i sigma_(s,k)(c_i) = 0 "for every" c in C\}). $]
_For any $K_s$-linear code, without a constacyclic hypothesis,_
#U[$ D_("code-first")(C) = rho_(s,k)(C^(perp_E)), wide D_("candidate-first")(C) = sigma_(s,k)(C^(perp_E)), $]
_and therefore_
$ D_("candidate-first")(C) = sigma_(s,k)^2 (D_("code-first")(C)). $ <eq:convention>
_Suppressing the component index, the same transformation is stated as_
#U[$ D_("candidate-first")(C) = sigma_k^2 (D_("code-first")(C)). $]
_The two dual subspaces are not generally equal._]) <prop:convention>

#Proof([The first relation follows from #P(<prop:dual-translation>). For the candidate-first condition, setting $z = rho_(s,k)(y)$ gives $z in C^(perp_E)$ and hence $y = sigma_(s,k)(z)$. Applying $sigma_(s,k)$ twice to the first relation gives #E(<eq:convention>). No equality of the two subspaces follows unless the square of the Frobenius happens to act trivially on the relevant subspace.])

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(Same-code hull-dimension and LCD invariance).* _Let $B$ be a row basis of a finite-field-linear code $C$ and let_
#U[$ G = B thin sigma(B)^(sans(T)). $]
_Then both same-code hull dimensions are equal to_
#U[$ "dim"(C) - "rank"(G). $]
_In particular, the code-first and candidate-first pairings have the same same-code hull dimension and the same LCD decision. This does not identify the dual codes, hull subspaces, factor supports, or generator supports._]) <prop:gram-invariance>

#Proof([Writing a codeword as $v B$, the code-first hull equations become a homogeneous system with coefficient matrix $G$ after the invertible change of variables induced by $sigma$. The candidate-first equations give the corresponding left-nullspace description with the same matrix rank. Rank-nullity yields the displayed dimension in both cases. The LCD assertion is the special case in which this dimension is zero.])

== Hull support and the cyclic boundary statistic

#figure(kind: "theorem", supplement: [Theorem], placement: none, numbering: "1", [*~(Component hull support).* _Let $C_s(J_s)$ be selected by $J_s subset.eq cal(F)_s$. Under the compatible same-factor-set hypotheses, the code-first hull has factor support_
$ "Supp"_("CRT")("Hull"_k(C_s(J_s))) &= (cal(F)_s without J_s) inter tau_(s,k)(J_s) \ &= tau_(s,k)(J_s) without J_s. $ <eq:support>
_The first line is the direct lcm/intersection form, and the second uses that $tau_(s,k)$ is a permutation of $cal(F)_s$._]) <thm:hull-support>

#Proof([The code generator has support $J_s$, while the dual generator has support $tau_(s,k)(cal(F)_s without J_s)$. The intersection of the two principal ideals in the square-free quotient is generated by the least common multiple, so its surviving factors are the complement of the union of these two supports. This gives $(cal(F)_s without J_s) inter (cal(F)_s without tau_(s,k)(cal(F)_s without J_s))$. Since $tau_(s,k)$ is a permutation, the second complement is $tau_(s,k)(J_s)$, giving the two displayed forms.])

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(Weighted cyclic boundary statistic).* _For a labeled selection $J = (J_s)_s$ and its global code $C(J)$, let $O in cal(O)_s$ be a cycle of length $a_O$, indexed by_
#U[$ tau_(s,k)(f_i) = f_(i+1), quad i thin ("mod" a_O). $]
_All factors in $O$ have a common degree $d_O$. Put_
#U[$ w_O = m_s d_O, quad epsilon_i = cases(1 & f_i in J_s, 0 & f_i in.not J_s). $]
_Then_
$ b_O(epsilon) = sum_(i=0)^(a_O - 1) epsilon_i (1 - epsilon_(i+1)) $ <eq:boundary>
_and_
$ "dim"_(bb(F)_q) "Hull"_(cal(A), k)(C(J)) = sum_(s=1)^N sum_(O in cal(O)_s) w_O b_O(epsilon_O). $ <eq:hull-dim>]) <prop:boundary>

#Proof([The orbit positions have equal factor degree because the reciprocal permutation of #P(<prop:compatible-permutation>) preserves degree. The support formula #E(<eq:support>) identifies a hull factor at position $i + 1$ exactly when $f_i$ is selected and $f_(i+1)$ is not. Each such factor contributes $m_s d_O = w_O$ to the global $bb(F)_q$ dimension, and summing over the orbit partition gives the formula.])

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(Cyclic boundary interpretation).* _For a nonconstant cyclic binary word, the statistic $b_O$ of_ _#E(<eq:boundary>)_ _equals the number of one-runs and also the number of zero-runs. It is the number of directed $1$-to-$0$ transitions, with cyclic indexing modulo $a_O$._]) <prop:boundary-interpretation>

#Proof([Each summand is one exactly when the directed edge from $i$ to $i + 1$ is a $1$-to-$0$ transition. Every one-run has exactly one such exit and every zero-run has exactly one entry, so these counts agree. The two constant words have $b_O = 0$.])

// ---------- 4. Exact Joint Enumeration ----------
= Exact Joint Enumeration <sec:enumeration>

In this section, we enumerate the labeled selections. We determine the one-orbit polynomial, represent it by a weighted transfer matrix and cyclic trace, and multiply the local contributions into the global joint enumerator with its consequences.

== The one-orbit polynomial <sec:orbit>

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(One-orbit polynomial).* _For an orbit of length $a$ and weight $w$, let $P_(a,w)(z)$ be the sum of $z^(w b(epsilon))$ over all indexed cyclic binary words. Then_
#U[$ N(a, r) = 2 binom(a, 2r) = (a / r) binom(a - 1, 2r - 1) $]
_counts the words with $r$ one-runs, and_
$ P_(a,w)(z) = 2 + sum_(r=1)^(floor(a / 2)) 2 binom(a, 2r) z^(r w) = 2 + sum_(r=1)^(floor(a / 2)) (a / r) binom(a - 1, 2r - 1) z^(r w). $ <eq:orbit-poly>]) <prop:orbit-poly>

#Proof([The two constant words contribute $2$. By #P(<prop:boundary-interpretation>), a nonconstant word with $r$ one-runs has $2r$ transition edges. Choosing the $2r$ transition edges and one of the two starting values gives $2 binom(a, 2r)$. The equality with the composition form follows from $2 binom(a, 2r) = (a / r) binom(a - 1, 2r - 1)$, so the second expression is integral because it equals the first.])

#h(1.5em)The second form is integral because it equals the first form. In particular,
#U[$ P_(1,w)(z) = 2, quad P_(2,w)(z) = 2 + 2 z^w, quad P_(3,w)(z) = 2 + 6 z^w, $]
#U[$ P_(4,w)(z) = 2 + 12 z^w + 2 z^(2w), wide P_(5,w)(z) = 2 + 20 z^w + 10 z^(2w). $]
For example, at $a = 4$ there are two constant words, twelve words with one one-run, and two alternating words with two one-runs.

At $z = 1$, the binomial identity gives $P_(a,w)(1) = 2^a$, as required for the $2^a$ indexed factor selections in one orbit.

== The transfer-matrix representation <sec:transfer>

We now encode the one-orbit enumeration as a two-state transfer matrix.

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(Weighted transfer matrix).* _For a transition from source state $r = epsilon_i$ to destination state $t = epsilon_(i+1)$, assign_
#U[$ T_w(u, z)_(r,t) = u^(w(1-t)) z^(w r (1-t)). $]
_With states ordered as $0, 1$, this is_
$ T_w(u, z) = mat(u^w, 1; u^w z^w, 1). $ <eq:transfer>
_The destination weight is deliberate: each factor is counted once as the destination of the preceding edge. Thus $u$ records code dimension, because a factor with destination state $t = 0$ is not selected and contributes $w$ to the code dimension. The factor $z^w$ appears precisely on a $1$-to-$0$ edge._]) <prop:transfer-matrix>

#Proof([The four source/destination choices $(r, t) in \{0, 1\}^2$ receive the destination code-dimension weight $u^(w(1-t))$ and the boundary weight $z^(w r (1-t))$. This gives the displayed matrix in the state order $0, 1$.])

#figure(kind: "proposition", supplement: [Proposition], placement: none, numbering: "1", [*~(Local trace identity).* _With $T_w(u, z)$ as in Proposition_ _#Pn(<prop:transfer-matrix>)_, _for an orbit of length $a$ and weight $w$,_
$ "tr"(T_w(u, z)^a) = sum_(epsilon in \{0, 1\}^a) u^(w sum_i (1 - epsilon_i)) z^(w sum_i epsilon_i (1 - epsilon_(i+1))). $ <eq:trace>
_In particular,_
#U[$ "tr"(T_w(1, z)^a) = P_(a,w)(z). $]]) <prop:trace>

#Proof([Expand a diagonal entry of $T_w^a$ in #E(<eq:transfer>) as a sum over intermediate states. The diagonal condition identifies the terminal state with the initial state, thereby closing the cycle. Summing the two diagonal entries sums over every indexed binary word exactly once. The product of edge weights is
#U[$ product_i u^(w(1-epsilon_(i+1))) z^(w epsilon_i (1-epsilon_(i+1))), $]
which is the displayed monomial after cyclic reindexing. The closed-walk expansion is proved here directly; the hull-specific content is the preceding identification of the boundary statistic.])

== The global joint enumerator

#figure(kind: "theorem", supplement: [Theorem], placement: none, numbering: "1", [*~(Exact labeled joint enumerator).* _Under the standing hypotheses of Sections_ _#Sn(<sec:prelim>)_ _and_ _#Sn(<sec:duality>)_, _with the orbit notation of Sections_ _#Sn(<sec:orbit>)_ _and_ _#Sn(<sec:transfer>)_, _let_
#U[$ cal(A) tilde.equiv product_(s=1)^N K_s, quad K_s = bb(F)_(q^(m_s)), quad lambda = (lambda_s)_s in cal(A)^*, $]
_with $q = p^e$, $d_s = e m_s$, $"gcd"(n, p) = 1$, simple roots, fixed labels, finite-field-linear component codes, and_
#U[$ lambda_s^(1+p^(d_s - k)) = 1 quad (1 lt.eq s lt.eq N). $]
_For a labeled factor selection $J = (J_s)_s$, the global code is the CRT product_
#U[$ C(J) = product_(s=1)^N C_s(J_s) subset.eq cal(A)^n, $]
_and its global code-first dual and hull are defined by the $cal(A)$-valued pairing in_ _#L(<lem:global-pairing>)_:
#U[$ D_(cal(A), k)(C(J)) = \{y : \<c, y\>_(cal(A), k) = 0_(cal(A)) "for every" c in C(J)\}, wide "Hull"_(cal(A), k)(C(J)) = C(J) inter D_(cal(A), k)(C(J)). $]
_For every orbit $O in cal(O)_s$, let $a_O$ be its length, let $d_O$ be its common factor degree, and put $w_O = m_s d_O$. If $epsilon_(O,i) = 1$ exactly when the indexed factor $f_(O,i)$ is in $J_s$, set_
$ K(C(J)) := "dim"_(bb(F)_q) C(J) = sum_(s,O,i) w_O (1 - epsilon_(O,i)), \ H_k(C(J)) := "dim"_(bb(F)_q) "Hull"_(cal(A),k)(C(J)) = sum_(s,O,i) w_O epsilon_(O,i)(1 - epsilon_(O,i+1)). $ <eq:KH>
_With_
#U[$ T_w(u, z) = mat(u^w, 1; u^w z^w, 1), $]
_the exact joint generating polynomial is_
$ scr(E)(u, z) &= sum_(J in scr(C)) u^(K(C(J))) z^(H_k(C(J))) \ &= product_(s=1)^N product_(O in cal(O)_s) "tr"(T_(w_O)(u, z)^(a_O)). $ <eq:joint>
_For every pair $(K, H)$ of_ _#E(<eq:KH>),_
#U[$ [u^K z^H] scr(E)(u, z) $]
_is the number of distinct labeled factor-selection codes with global $bb(F)_q$-code dimension $K$ and global code-first $bb(F)_q$-hull dimension $H$._]) <thm:central>

#Proof([#L(<lem:global-code>) gives a Cartesian product of independent labeled component choices, while #L(<lem:global-dual>) and #L(<lem:global-hull>) identify the global hull with the product of the component hulls. #P(<prop:global-dimensions>) converts component dimensions to global $bb(F)_q$ dimensions and identifies the orbit weights. #T(<thm:hull-support>) and #P(<prop:boundary>) then give #E(<eq:hull-dim>). #P(<prop:trace>) enumerates each orbit choice with its code-dimension and hull-dimension weights. Since different orbits and components are independent coordinates and both dimensions are additive, multiplication of the local trace polynomials gives the product formula. The injectivity in #L(<lem:global-code>) and coefficient extraction give the stated distinct labeled-code interpretation.])

#h(1.5em)The result is a labeled enumeration. It does not quotient the selection space by rotations, automorphisms, isometries, or code equivalence.

== Consequences

We now record the principal specializations of the joint enumerator #E(<eq:joint>) in #T(<thm:central>).

#figure(kind: "corollary", supplement: [Corollary], placement: none, numbering: "1", [. _The total number of distinct labeled factor-selection codes is_
#U[$ scr(E)(1, 1) = 2^(sum_s abs(cal(F)_s)). $]]) <cor:total>

#Proof([At $u = z = 1$, every local trace #E(<eq:trace>) counts the $2^(a_O)$ indexed binary words on its orbit. Multiplying over the orbit partition gives $2^(sum_s abs(cal(F)_s))$, which also follows directly from the bijection of #L(<lem:factor-selection>).])

#figure(kind: "corollary", supplement: [Corollary], placement: none, numbering: "1", [*~(Code-dimension distribution).* _Setting $z = 1$ removes the hull marking and yields_
$ scr(E)(u, 1) = product_(s=1)^N product_(f in cal(F)_s) (1 + u^(m_s "deg"(f))). $ <eq:code-dist>
_Thus $[u^K] scr(E)(u, 1)$ counts labeled codes of global code dimension $K$. This is a marginal distribution and does not identify a dual convention._]) <cor:code-dist>

#Proof([Each factor is either unselected, contributing its full global dimension weight, or selected, contributing no code-dimension weight. The factor-selection bijection and independence give the product.])

#figure(kind: "corollary", supplement: [Corollary], placement: none, numbering: "1", [*~(Hull-dimension distribution).* _The exact hull polynomial is_
$ H_(cal(A), n, lambda, k)(z) = scr(E)(1, z) = product_(s=1)^N product_(O in cal(O)_s) P_(a_O, w_O)(z). $ <eq:hull-dist>
_Consequently,_
#U[$ [z^H] H_(cal(A), n, lambda, k)(z) $]
_counts labeled codes with code-first hull dimension $H$._]) <cor:hull-dist>

#Proof([Set $u = 1$ in #T(<thm:central>) and use Propositions~#Pn(<prop:orbit-poly>) and #Pn(<prop:trace>).])

#figure(kind: "corollary", supplement: [Corollary], placement: none, numbering: "1", [*~(LCD count).* _All orbit weights are positive. Hence the hull dimension is zero exactly when every orbit has $b_O = 0$. A cyclic binary word has no $1$-to-$0$ transition exactly when it is constant, so each orbit has two LCD selections. Therefore_
$ \#\{C : H_k(C) = 0\} = 2^(sum_s abs(cal(O)_s)). $ <eq:lcd>
_This is a labeled LCD count._]) <cor:lcd>

#Proof([The zero-boundary cyclic words are exactly the two constant words on each orbit. Independence over the orbit partition gives the displayed product.])

#h(1.5em)For the moment statements, equip the finite labeled selection space $scr(C)$ with the uniform probability measure
#U[$ bb(P)(C(J)) = 1 / scr(E)(1, 1) = 2^(-sum_s abs(cal(F)_s)) quad (J in scr(C)). $]
Thus every distinct labeled factor-selection code has equal probability.

#figure(kind: "corollary", supplement: [Corollary], placement: none, numbering: "1", [*~(Mean hull dimension).* _Under this uniform measure, for an orbit of length $a gt.eq 2$, the indicator $X_i = epsilon_i (1 - epsilon_(i+1))$ has expectation $1 / 4$, while a length-one orbit contributes zero. Independence across orbits gives_
$ bb(E)[H_k] = sum_(s, O : a_O gt.eq 2) (a_O w_O) / 4. $ <eq:mean>
_Equivalently, the same value is obtained by differentiating the normalized hull polynomial at $z = 1$._]) <cor:mean>

#Proof([Sum the expectations of the directed boundary indicators over every orbit and multiply by its weight. The length-one case has no directed boundary.])

#figure(kind: "corollary", supplement: [Corollary], placement: none, numbering: "1", [*~(Variance of hull dimension).* _Under the same uniform measure, for $a gt.eq 3$, neighboring directed-edge indicators have covariance $-1 / 16$ and nonneighboring indicators have covariance zero. Thus an orbit of length $a gt.eq 3$ contributes $a w^2 / 16$. For $a = 2$, the two directed boundary indicators are mutually exclusive and the orbit contribution is Bernoulli with variance $w^2 / 4$. A length-one orbit contributes zero. Therefore_
$ "Var"(H_k) = sum_(s, O : a_O = 2) (w_O^2) / 4 + sum_(s, O : a_O gt.eq 3) (a_O w_O^2) / 16. $ <eq:var>
_The separate $a = 2$ term is essential._]) <cor:variance>

#Proof([For $a gt.eq 3$, the covariance calculation for the cyclic indicators gives $a / 16$ after summing the variances and adjacent covariances. For $a = 2$, the two directed edges are mutually exclusive, so the boundary count is $0$ or $1$ with probability $1 / 2$ and the weighted variance is $w^2 / 4$. Independent orbits add their variances.])

// ---------- 5. Examples and Computational Validation ----------
= Examples and Computational Validation <sec:examples>

In this section, we illustrate #T(<thm:central>) with worked examples and record the computational validation. The computations below are independent checks of finite instances, not proofs of the general statements. The accompanying package separates direct construction, direct dual and hull calculation, Gram-matrix calculation, reciprocal and support calculation, local orbit enumeration, transfer-matrix evaluation, and global product comparison; the reproducible commands and complete outputs are retained there.

== Worked examples

#figure(kind: "example", supplement: [Example], placement: none, numbering: "1", [. Consider the case $q = 4$, $n = 5$, $lambda = 1$, $k = 1$ with four labeled $bb(F)_4$ components, giving $8^4 = 4096$ labeled selections. Writing $bb(F)_4 = bb(F)_2 (a)$, the recorded factorization is
#U[$ x^5 - 1 = (x + 1)(x^2 + a x + 1)(x^2 + (a + 1) x + 1), $]
and the recorded reciprocal action fixes the linear factor and interchanges the two quadratics. Each component hence has orbits of lengths $1$ and $2$ with weights $w = 1$ and $w = 2$. The one-component transfer-matrix traces of #P(<prop:trace>) give the joint enumerator
#U[$ (u + 1)(1 + u^4 + 2 u^2 z^2) = 1 + u + u^4 + u^5 + 2 u^2 z^2 + 2 u^3 z^2, $]
which is the recorded component joint histogram $\{(0, 0) : 1, (1, 0) : 1, (2, 2) : 2, (3, 2) : 2, (4, 0) : 1, (5, 0) : 1\}$. The hull polynomial of one component is $2 (2 + 2 z^2) = 4 + 4 z^2$, so the four-component ring hull polynomial is
#U[$ (4 + 4 z^2)^4 = 256 + 1024 z^2 + 1536 z^4 + 1024 z^6 + 256 z^8, $]
which is the recorded ring hull histogram $\{0 : 256, 2 : 1024, 4 : 1536, 6 : 1024, 8 : 256\}$; the recorded ring joint histogram has $65$ terms. In particular, each component contributes $4$ LCD selections and the ring contributes $256$, as given by #C(<cor:lcd>).]) <ex:pilot>

#figure(kind: "example", supplement: [Example], placement: none, numbering: "1", [. Consider the long-orbit case $q = 8$, $n = 7$, $lambda = 1$, $k = 1$, with $2^7 = 128$ labeled selections by #C(<cor:total>). Here $x^7 - 1$ splits into seven linear factors over $bb(F)_8$, and the recorded reciprocal action has orbit lengths $[1, 6]$, all of weight $w = 1$. By #E(<eq:orbit-poly>), the hull polynomial #E(<eq:hull-dist>) is therefore
#U[$ 2 P_(6,1)(z) = 2 (2 + 30 z + 30 z^2 + 2 z^3) = 4 + 60 z + 60 z^2 + 4 z^3, $]
which is the recorded hull histogram $\{0 : 4, 1 : 60, 2 : 60, 3 : 4\}$. The recorded joint histogram is
#U[$ & \{(0,0) : 1, (1,0) : 1, (1,1) : 6, (2,1) : 12, (2,2) : 9, \ & (3,1) : 12, (3,2) : 21, (3,3) : 2, (4,1) : 12, (4,2) : 21, \ & (4,3) : 2, (5,1) : 12, (5,2) : 9, (6,0) : 1, (6,1) : 6, (7,0) : 1\}, $]
in agreement with the transfer-matrix product of #P(<prop:trace>). In particular, there are $4$ LCD selections, as given by #C(<cor:lcd>).]) <ex:long-orbit>

== Validation record

#Tab(<tab:computations>) lists the validation cases with their parameters and scope; Examples~#Exn(<ex:pilot>) and #Exn(<ex:long-orbit>) work out the first two rows in detail.

#align(center)[
#show table.cell: set text(size: 8pt)
#show table.cell: set par(justify: false, first-line-indent: 0pt)
#figure(
table(columns: (15fr, 23fr, 11fr, 13fr, 23fr), stroke: 0.5pt, align: left,
[*Case*], [*Parameters*], [*Selections*], [*Scope*], [*Evidence*],
[F4 pilot], [$q = 4$, $n = 5$, $lambda = 1$, $k = 1$, four labeled $bb(F)_4$ components], [$8^4 = 4096$], [Direct dual, reciprocal, hull, and enumerator checks], [#text(font: "DejaVu Sans Mono")[validate\_#sym.zws pilot.py] and capture],
[F8 long orbit], [$q = 8$, $n = 7$, $lambda = 1$, $k = 1$; orbit lengths $[1, 6]$], [$2^7 = 128$], [Long-cycle support and generator checks], [#text(font: "DejaVu Sans Mono")[validate\_#sym.zws long\_#sym.zws orbit\_#sym.zws examples.py] and capture],
[F16 extension], [$K = bb(F)_16 = bb(F)_(4^2)$, $n = 5$, $lambda = 1$, $k = 1$; orbit lengths $[1, 4]$], [$2^5 = 32$], [Extension exponent and principal convention], [#text(font: "DejaVu Sans Mono")[validate\_#sym.zws long\_#sym.zws orbit\_#sym.zws examples.py] and capture],
[Compatible twist], [$q = 4$, $n = 5$, $lambda = omega$, $k = 1$; orbit lengths $[1, 2]$], [$2^3 = 8$], [Compatible nontrivial twist], [#text(font: "DejaVu Sans Mono")[validate\_#sym.zws nontrivial\_#sym.zws constacyclic.py] and capture],
[N2-A], [Extension-convention data fixed in the capture], [$32$], [Direct/principal convention comparison], [#text(font: "DejaVu Sans Mono")[validate\_#sym.zws n2\_#sym.zws extension\_#sym.zws convention.py] and capture],
[N2-B], [Incompatible extension diagnostic data fixed in the capture], [$8$], [Direct diagnostic only; no transfer enumeration], [#text(font: "DejaVu Sans Mono")[diagnose\_#sym.zws n2\_#sym.zws incompatible\_#sym.zws twist.py] and capture],
[Global product bridge], [$cal(A) = bb(F)_4 times bb(F)_16$ over $bb(F)_4$, $n = 5$, $lambda = (omega, 1)$, $k = 1$], [$2^3 dot 2^5 = 256$], [Direct product dual/hull, $bb(F)_4$-dimension additivity, orbit and transfer agreement], [#text(font: "DejaVu Sans Mono")[validate\_#sym.zws global\_#sym.zws product.py] and capture],
),
caption: [Fully specified or explicitly captured finite validation cases. These are validation records, not general proofs.],
) <tab:computations>
]

#h(1.5em)For the global-product case over $cal(A) = bb(F)_4 times bb(F)_16$, with contributing orbits of lengths $2$ and $4$ and weights $2$ and $2$, the recorded uniform mean and variance are $3.0$ and $2.0$, in agreement with Corollaries~#Cn(<cor:mean>) and #Cn(<cor:variance>). The independent end-to-end validator also checks the convention relation #E(<eq:convention>) of #P(<prop:convention>), reciprocal generators, support formulas, transfer products, injective selections, Gram-matrix and LCD calculations, and all $73$ rank-two planes in $bb(F)_8^3$ within its stated scope. The incompatible cases are diagnostics and are excluded from the compatible transfer theorem. One further validation artifact is underspecified and is not used as a computational case here.

// ---------- 6. Conclusion ----------
= Conclusion <sec:conclusion>

Under the stated square-free, simple-root, compatible-twist, fixed-component, and labeled-factor hypotheses, the component factor-selection model gives a self-contained route from code-first Galois duality to an exact joint generating polynomial. The inverse-Frobenius reciprocal determines the compatible factor action, the least-common-multiple intersection determines the hull support, and the support becomes a weighted cyclic boundary statistic on each reciprocal orbit. The local orbit polynomial and the two-state transfer matrix give equivalent descriptions of the same indexed selections, and their cyclic trace factors over independent labeled orbits into $scr(E)(u, z)$.

Coefficient extraction yields the joint code and hull distribution, while specializations give the total count of #C(<cor:total>), the code-dimension and hull-dimension distributions of Corollaries~#Cn(<cor:code-dist>) and #Cn(<cor:hull-dist>), the LCD count of #C(<cor:lcd>), and the mean and variance of Corollaries~#Cn(<cor:mean>) and #Cn(<cor:variance>), with the short-orbit variance case handled separately. The finite computations validate the stated $bb(F)_4$, $bb(F)_8$, $bb(F)_16$, compatible-twist, N2, and global-product instances through independent routes; they do not replace the conditional proofs.

The main enumerator is square-free and simple-root: repeated-root cases are excluded, and, by #P(<prop:same-twist>), when the compatibility condition #E(<eq:compat>) fails, the code-first dual is constacyclic over the transformed modulus $x^n - lambda_s^(-p^(d_s - k))$, to which the present orbit product does not apply. The enumeration counts distinct labeled factor selections, not equivalence, isometry, or automorphism classes. The code-first and candidate-first dual codes and hull subspaces are not generally equal: the Gram-matrix argument of #P(<prop:gram-invariance>) gives equality of same-code hull dimensions and LCD decisions only. No quantum distance, parameter, optimality, or fault-tolerance conclusion follows from the hull enumerator alone. #Tab(<tab:scope>) summarizes these scope boundaries.

#align(center)[
#show table.cell: set text(size: 10pt)
#show table.cell: set par(justify: false, first-line-indent: 0pt)
#figure(
table(columns: (25fr, 26fr, 39fr), stroke: 0.5pt, align: left,
[*Topic*], [*Status in this paper*], [*Boundary*],
[Repeated roots], [Excluded], [Requires multiplicity-sensitive ideals and a different enumeration.],
[Incompatible twists], [Diagnostic only], [Requires a two-modulus or bipartite theory.],
[Equivalence classes], [Not counted], [Main polynomial counts labeled selections only.],
[Burnside--Pólya], [Future work], [No group action or quotient count is proved.],
[Quantum parameters], [Conditional background only], [No distance or performance claim is made.],
[N1], [Excluded], [Specification and expected output are incomplete.],
[Final/corrected source transfer], [Incomplete], [Source-level comparison remains conditional.],
),
caption: [Scope boundaries required for interpreting the manuscript.],
) <tab:scope>
]

#h(1.5em)The literature comparison remains conservative: the accessible theorem-bearing version of the closest affine source and its final publisher record are distinct records \[12, 13\], and the complete corrected text of the finite-field constacyclic comparison remains to be checked before any stronger theorem-level attribution \[2, 3\]; we state no priority claim. One validation artifact (labeled N1 in the accompanying package) remains underspecified and is excluded. Future work includes Burnside--Pólya quotient counts under an explicitly defined group action with fixed-code calculations, repeated-root and multiplicity-sensitive ideals, and a two-modulus theory for incompatible twists.

// ---------- References ----------
#heading(level: 1, numbering: none)[References]
#[
#set par(first-line-indent: 0pt)
#grid(columns: (auto, 1fr), column-gutter: 0.7em, row-gutter: 0.45em,
[\[1\]], [E. Sangwisut, S. Jitman, S. Ling, and P. Udomkavanich. Hulls of cyclic and negacyclic codes over finite fields. _Finite Fields and Their Applications_, 33:232–257, 2015.],
[\[2\]], [I. Debnath, O. Prakash, and H. Islam. Galois hulls of constacyclic codes over finite fields. _Cryptography and Communications_, 15:111–127, 2023.],
[\[3\]], [I. Debnath, O. Prakash, and H. Islam. Correction to: galois hulls of constacyclic codes over finite fields. _Cryptography and Communications_, 15:129–130, 2023.],
[\[4\]], [I. Debnath and O. Prakash. Average dimensions of galois hulls of constacyclic codes. _Advances in Mathematics of Communications_, 19(6):1569–1604, 2025.],
[\[5\]], [I. Debnath, H. Islam, Yadav, and O. Prakash. Study of small galois hull dimensions of constacyclic codes. _Advances in Mathematics of Communications_, 22, 2026.],
[\[6\]], [Talbi, Batoul, Fotue Tabue, and E. Martínez-Moro. Galois hulls of cyclic serial codes over a finite chain ring. 2021.],
[\[7\]], [S. Jitman, S. Sangwisut, and P. Udomkavanich. Hulls of cyclic codes over Z4. _Discrete Mathematics_, 343, 2020. Article 111621.],
[\[8\]], [Pathak and Sharma. On the hulls of cyclic codes of oddly even length over Z4. _Discrete Mathematics_, 347, 2024. Article 113796.],
[\[9\]], [Gao, Wu, and Fu. Hulls of double cyclic codes. _Finite Fields and Their Applications_, 88, 2023. Article 102189.],
[\[10\]], [Aliabadi, Kalaycı, and Zadehdabbagh. Asymptotic performance of double circulant and four circulant codes with small hull dimension. _Cryptography and Communications_, 18:525–546, 2026.],
[\[11\]], [E. Zhang, B. Kong, and X. Zheng. Quantum codes from galois hulls of constacyclic codes over a finite non-chain ring. _Entropy_, 28, 2026. Article 407.],
[\[12\]], [I. Debnath, H. Islam, E. Martínez-Moro, and O. Prakash. Galois hulls of constacyclic codes over affine algebra rings. 2024. Version 1, 11 December 2024.],
[\[13\]], [I. Debnath, H. Islam, E. Martínez-Moro, and O. Prakash. Galois hulls of constacyclic codes over affine algebra rings. _Discrete Mathematics_, 349(2), 2026. Article 114750.],
)
]
