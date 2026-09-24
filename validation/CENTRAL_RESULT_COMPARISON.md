# Phase-8 Central Result Comparison

**Audit date:** 2026-09-24
**Branch:** `arena/01a0c9d2-galios-hull`
**Mandatory base commit:** `703260d610b4980df25610694bbe6a04f937abbc`
**Purpose:** compare the frozen central theorem package with the strongest accessible theorem-level and publisher-level records without identifying different dual conventions or different code families.

## 1. The frozen target

The target is not the statement that hulls or fixed-dimension counts have never been studied. The target is the following conditional package.

Let

- `A ~= prod_s K_s` be a fixed **labeled** product of finite fields obtained from a square-free affine algebra;
- `K_s=F_{q^{m_s}}=F_{p^{d_s}}`, with `d_s=e m_s`;
- `gcd(n,p)=1`, so every `x^n-lambda_s` is simple-root;
- `J_s` be a selected subset of the monic irreducible factor set `F_s` of `x^n-lambda_s`;
- `C(J_s)` be the corresponding component ideal, and the global code be the labeled product of the component choices;
- `sigma(a)=a^(p^k)` and `rho(a)=a^(p^(d_s-k))` be the frozen second-slot/code-first maps;
- `lambda_s^(1+p^(d_s-k))=1` be the same-factor-set compatibility condition.

The code-first hull support on a factor orbit `O=(f_0,...,f_{a-1})`, with `tau(f_i)=f_{i+1}` and `epsilon_i=1` for a selected generator factor, is

```text
b_O(epsilon) = sum_i epsilon_i (1-epsilon_(i+1)).
```

The orbit weight is `w_O=m_s deg(f_i)`. The target joint polynomial is

```text
E(u,z) = product_s product_O trace(T_(w_O)(u,z)^(a_O)),
T_w(u,z) = [[u^w, 1], [u^w z^w, 1]],
```

where `u` records global `F_q`-code dimension and `z` records global code-first `F_q`-hull dimension. This is a count of distinct labeled factor-selection codes. It is not a count of equivalence classes, necklaces, or Burnside/Pólya orbits.

The frozen package also includes the separate convention identity

```text
D_candidate(C) = sigma_k^2(D_code-first(C)),
```

and the separate Gram-matrix result that same-code hull dimensions and LCD decisions agree under the two pairings. Neither result identifies the two dual subspaces, hull subspaces, factor supports, or generators.

## 2. Evidence rule

The comparison uses the following order of trust:

1. original publisher or open full text;
2. accepted/preprint theorem text when the publisher version is inaccessible;
3. publisher abstract, section snippets, and bibliographic records for discovery and scope only;
4. search snippets or aggregators only to locate a source, never as proof of an exact overlap.

A source can therefore be strong evidence for a narrower result while remaining `PARTIAL` or `UNVERIFIED` for transfer to the frozen target. The statuses below are the permitted transfer vocabulary:

`DIRECT`, `DIRECT AFTER CONVENTION TRANSFORMATION`, `PARTIAL`, `NOT TRANSFERABLE`, and `UNVERIFIED`.

## 3. Central comparison table

| ID | Source and accessible record | Verified source result | Exact overlap with the frozen target | Principal mismatch or limit | Transfer status | Safe use |
|---|---|---|---|---|---|---|
| C8-01 | Debnath–Islam–Martínez-Moro–Prakash, *Galois hulls of constacyclic codes over affine algebra rings*, arXiv:2412.08512v1, [readable HTML](https://arxiv.org/html/2412.08512); final *Discrete Mathematics* record, DOI [10.1016/j.disc.2025.114750](https://doi.org/10.1016/j.disc.2025.114750) | The accessible source decomposes a square-free affine algebra into field components, gives component dual/hull generators, hull-dimension formulas, LCD conditions, and conditional quantum applications. Its conclusion explicitly says that enumeration of non-isometric constacyclic codes with a prescribed Galois hull dimension over the affine algebra remains an open future problem. | Highest structural overlap: affine product, constacyclic components, Galois hulls, and lcm/hull support. | The readable source uses the candidate-first dual; its displayed reciprocal/twist is rho-based. The final publisher full text is access-controlled. It does not provide the frozen all-selection bivariate transfer product. | `PARTIAL` for structural background; `DIRECT AFTER CONVENTION TRANSFORMATION` only for the slot relation; `NOT TRANSFERABLE` for its displayed dual formula as a literal candidate-first theorem. | Cite for scope and for the independently verified open enumeration statement, with the convention warning. Do not cite it as proof of `E(u,z)`. |
| C8-02 | Sangwisut–Jitman–Ling–Udomkavanich, *Hulls of cyclic and negacyclic codes over finite fields*, *Finite Fields and Their Applications* 33 (2015), 232–257, DOI [10.1016/j.ffa.2014.12.008](https://doi.org/10.1016/j.ffa.2014.12.008), [publisher record](https://www.sciencedirect.com/science/article/pii/S107157971400166X) | The open publisher record gives Euclidean/Hermitian hull dimensions for cyclic and negacyclic finite-field codes and enumerates codes having a fixed hull dimension. The factor description separates self-reciprocal factors and reciprocal pairs. | It verifies exact fixed-dimension enumeration and the reciprocal/lcm mechanism in a simple-root finite-field subfamily. | No arbitrary square-free affine product, extension-component weight assembly, frozen code-first `k` convention, or bivariate code/hull transfer product is supplied as the present target. | `PARTIAL` | Use as confirmed counterevidence to any broad claim that exact hull-dimension enumeration is new; use only for its finite-field cyclic/negacyclic scope. |
| C8-03 | Debnath–Prakash–Islam, *Galois hulls of constacyclic codes over finite fields*, *Cryptography and Communications* 15 (2023), 111–127, DOI [10.1007/s12095-022-00591-6](https://doi.org/10.1007/s12095-022-00591-6), with correction [10.1007/s12095-022-00602-6](https://doi.org/10.1007/s12095-022-00602-6) | The publisher abstract states a Galois-hull dimension formula and counts constacyclic codes with a prescribed hull dimension under restrictions on `q`; a correction record is linked. | Exact finite-field constacyclic prescribed-dimension counting is directly adjacent. | The corrected theorem text and exact hypotheses were not fully accessible here; the result is over one finite field, not the labeled affine product, and no exact joint transfer product was verified. | `UNVERIFIED` for theorem-level import; `PARTIAL` for background scope | Cite only with the correction and only for abstract-level related scope until the corrected full text is read. |
| C8-04 | Talbi–Batoul–Fotue Tabue–Martínez-Moro, *Galois hulls of cyclic serial codes over a finite chain ring*, arXiv:2102.06995, [readable HTML](https://arxiv.org/html/2102.06995), published in *Finite Fields and Their Applications* 77 (2022), Article 101950 | The readable theorem text treats cyclic serial codes over a finite chain ring with `gcd(n,p)=1`. It gives the Galois/Euclidean hull parameters and Proposition 8 gives the number of cyclic serial codes with a fixed `q`-dimension of the Euclidean hull through the functions `psi_s` and `rho_s`. | This is an exact fixed-hull-dimension enumeration over a non-field finite ring and uses factor/cyclotomic data plus additive dimension contributions. | A chain ring is non-reduced and has nilpotent layers; the paper uses ordered `q`-partitions and chain-ring parameters, not a square-free product of labeled fields, and not the frozen weighted binary orbit transfer. | `PARTIAL` | Use as strong adjacent counterevidence and as a method comparison. Do not call its chain-ring count a theorem over the present algebra. |
| C8-05 | Jitman–Sangwisut–Udomkavanich, *Hulls of cyclic codes over Z4*, *Discrete Mathematics* 343 (2020), Article 111621, DOI [10.1016/j.disc.2019.111621](https://doi.org/10.1016/j.disc.2019.111621), [publisher record](https://www.sciencedirect.com/science/article/pii/S0012365X19302833) | The open archive abstract and outline state an algorithm for hull types and exact counts of cyclic `Z4` codes with each prescribed 2-dimension, together with averages. | Exact fixed-dimension enumeration over a finite ring is verified. | `Z4` is a chain ring with nilpotents; the result is Euclidean and cyclic, not the reduced affine product or the code-first extension-component product. | `PARTIAL` | Background/counterevidence only. |
| C8-06 | Pathak–Sharma, *On the hulls of cyclic codes of oddly even length over Z4*, *Discrete Mathematics* 347 (2024), Article 113796, DOI [10.1016/j.disc.2023.113796](https://doi.org/10.1016/j.disc.2023.113796), [publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0012365X2300482X) | The publisher abstract reports generator descriptions, fixed 2-dimension enumeration, and average 2-dimension for cyclic codes of length `2n` over `Z4` with `n` odd. | Further exact ring-code hull enumeration is verified. | Same chain-ring/non-reduced and Euclidean limitations; no arbitrary affine CRT product or bivariate orbit transfer. | `PARTIAL` | Background/counterevidence only. |
| C8-07 | Zhang–Kong–Zheng, *Quantum Codes from Galois Hulls of Constacyclic Codes over a Finite Non-Chain Ring*, *Entropy* 28 (2026), Article 407, DOI [10.3390/e28040407](https://doi.org/10.3390/e28040407), [full MDPI text](https://www.mdpi.com/1099-4300/28/4/407) | The full article defines a finite non-chain ring that CRT-decomposes as `e_1 F_{p^m} direct-sum ... direct-sum e_t F_{p^m}`, uses the code-first definition `{x:<y,x>_l=0 for all y in C}`, proves componentwise Galois dual/hull decomposition, and gives an lcm hull generator and Gram-rank dimension formula. | Direct structural overlap with reduced direct-product component hull decomposition and code-first pairing. | The ring is a restricted direct product with all components `F_{p^m}` and the paper targets quantum constructions; no exact enumeration of all labeled factor selections or weighted `trace(T^a)` product is given. Its notation uses `l` and `p^{m-l}`, which must be mapped componentwise. | `PARTIAL` | Cite for adjacent non-chain/direct-product structure and code-first component decomposition; do not import its quantum or counting conclusions. |
| C8-08 | Debnath–Prakash, *Average dimensions of Galois hulls of constacyclic codes*, *Advances in Mathematics of Communications* 19 (2025), 1569–1604, DOI [10.3934/amc.2025010](https://doi.org/10.3934/amc.2025010), [publisher record](https://www.aimsciences.org/article/doi/10.3934/amc.2025010) | The publisher abstract states formulas for Galois hull dimensions and average dimensions of constacyclic codes over finite fields and over `R_{m,q}=F_q[u]/<u^m-u>`, plus Galois LCD constructions. | It is adjacent in both Galois-hull and affine/ring direction and confirms that averages/LCD constructions are established outputs. | It is an average-dimension and construction paper, not an exact all-code bivariate distribution over an arbitrary labeled square-free product. Full text is access-restricted. | `PARTIAL` | Average/LCD background only. |
| C8-09 | Debnath–Islam–Yadav–Prakash, *Study of small Galois hull dimensions of constacyclic codes*, *Advances in Mathematics of Communications* 22 (2026), DOI [10.3934/amc.2025054](https://doi.org/10.3934/amc.2025054), [publisher record](https://www.aimsciences.org/article/doi/10.3934/amc.2025054) | The publisher abstract states conditions for Galois hull dimensions 1 and 2; the accessible record gives examples and a summary of parameter conditions. | It is current counterevidence against claiming that prescribed small Galois hull dimensions are unstudied. | It concerns existence/small dimensions and conditional quantum examples, not the full labeled distribution or the present transfer product. Full text is access-restricted. | `PARTIAL` | Cite only for narrow small-dimension context. |
| C8-10 | Gao–Wu–Fu, *Hulls of double cyclic codes*, *Finite Fields and Their Applications* 88 (2023), Article 102189, DOI [10.1016/j.ffa.2023.102189](https://doi.org/10.1016/j.ffa.2023.102189), [publisher record](https://www.sciencedirect.com/science/article/abs/pii/S107157972300031X) | The publisher abstract and section theorem preview state generators, hull dimensions, and enumeration of double cyclic codes over `Z_2` with fixed hull dimension. | It is a structurally adjacent multi-component cyclic enumeration using generating-function ideas. | Double cyclic codes are a different generalized quasi-cyclic family over `Z_2`, with separable/non-separable cases; no arbitrary affine product, Galois parameter, or factor-orbit product match was verified. | `PARTIAL` | Counterevidence and adjacent method only. |
| C8-11 | Aliabadi–Kalaycı–Zadehdabbagh, *Asymptotic performance of double circulant and four circulant codes with small hull dimension*, *Cryptography and Communications* 18 (2026), 525–546, DOI [10.1007/s12095-025-00861-z](https://doi.org/10.1007/s12095-025-00861-z), [open article](https://link.springer.com/article/10.1007/s12095-025-00861-z) | The open article gives explicit enumeration formulas for double circulant and four circulant codes over `F_q` with prescribed Euclidean hull dimension, including reciprocal-pair constituents. | It is theorem-level counterevidence to any generic assertion that prescribed-hull enumeration plus CRT/reciprocal constituents is new. | The code family is DC/FC quasi-cyclic, not the labeled factor-selection constacyclic family over a square-free affine algebra; its constituent choices and counting weights differ. | `PARTIAL` | Cite as adjacent exact enumeration, not as a transfer to the target. |
| C8-12 | Standard transfer-matrix sources: [Combinatorics Notes, Theorem 24.1 and 24.2](https://seragunn.github.io/combinatorics-notes/regular-languages/transfer-matrix.html) and the standard closed-walk identity `tr(A^a)` | Matrix powers count walks, and the trace sums closed walks. Marking transitions by commuting weight variables gives the corresponding weighted generating polynomial. | This directly supports the combinatorial device used after the algebraic reduction. | It is general combinatorics, not a hull theorem; the source does not establish the application-specific hull statistic. | `DIRECT` as a standard combinatorial tool only | Do not present the transfer matrix or trace mechanism alone as a novelty claim. |

## 3.1 Required 19-result theorem-architecture comparison

The rows below are the required result-level comparison. “Internal evidence” identifies the frozen theorem result and its proof/audit record; “adjacent evidence” identifies the strongest checked external record from the source table. A transfer label never means that a different source theorem has been silently imported.

| Result | Frozen result being compared | Internal evidence | Adjacent evidence checked | Exact overlap / limit | Transfer status |
|---|---|---|---|---|---|
| R8-01 | Square-free affine decomposition into labeled finite-field components. | Blueprint Theorem 1 and preserved Phase-2 proof audit. | C8-01 affine source; C8-07 restricted CRT/non-chain ring. | Same reduced-product idea is present, but the external rings and component hypotheses are source-specific. | `PARTIAL` |
| R8-02 | Simple-root component ideals are classified by binary selections of irreducible factors. | Blueprint Theorem 2 and factor-selection proof. | C8-01 component generator descriptions; C8-04 cyclic serial factor data. | Factor descriptions are adjacent, but no source was verified to state the exact arbitrary labeled selection bijection used here. | `PARTIAL` |
| R8-03 | The code-first second-slot `k`-Galois pairing and dual are fixed explicitly. | Blueprint Theorem 3; Phase-4/5 convention audits. | C8-01 candidate-first source dual; C8-07 Definition 4 code-first-looking pairing. | The primary source uses the opposite slot, while the adjacent non-chain source uses a code-first-looking definition with different notation. | `DIRECT AFTER CONVENTION TRANSFORMATION` |
| R8-04 | The normalized code-first reciprocal uses `rho(a)=a^(p^(e*m_s-k))`. | Blueprint Theorem 4 and reciprocal validator. | C8-01 displayed rho-based reciprocal/twist; C8-07 Corollary 1 uses `sigma^(m-l)` on reciprocals. | Reciprocal/Frobenius machinery is present, but exponent and slot conventions must be mapped componentwise. | `DIRECT AFTER CONVENTION TRANSFORMATION` |
| R8-05 | The inverse-Frobenius root action on irreducible factors is identified. | Blueprint Theorem 5 and root-action diagnostics. | C8-01 source factor action; C8-04 cyclic serial reciprocal/cyclotomic framework. | Reciprocal factor action is adjacent, but the frozen inverse-Frobenius orientation is not transferred literally from every source. | `PARTIAL` |
| R8-06 | Compatibility makes the twist preserve the same factor set and yields a permutation of factors. | Blueprint Theorem 6 and compatible-twist validator. | C8-01 source same-factor/hull conditions; C8-07 constacyclic dual multiplier transformation. | Related same-family conditions occur, but the frozen arbitrary labeled compatibility condition is not an external theorem match. | `PARTIAL` |
| R8-07 | The code-first dual generator/check-polynomial formula is obtained. | Blueprint Theorem 7 and direct dual checks. | C8-01 component dual generators; C8-07 Corollary 1 and Theorem 2. | Generator/reciprocal formulas are directly adjacent; the exact frozen convention and arbitrary affine product remain distinct. | `PARTIAL` |
| R8-08 | The same-factor-set compatibility and dual-twist criterion are separated from convention transformation. | Blueprint Theorem 8 and incompatible-twist diagnostics. | C8-01 source compatibility restrictions; C8-07 Theorem 2 multiplier change. | Sources give related multiplier restrictions, but incompatible two-modulus transfer is explicitly outside the frozen theorem. | `PARTIAL` |
| R8-09 | The hull support is the lcm/intersection support `tau(J) minus J` under the frozen orientation. | Blueprint Theorem 9 and support checks. | C8-01 affine hull/lcm formulas; C8-07 Theorem 6 lcm hull generator. | Lcm/intersection hull formulas are known in adjacent families; the exact forward support orientation is convention-sensitive. | `PARTIAL` |
| R8-10 | `b_O(epsilon)=sum_i epsilon_i(1-epsilon_(i+1))` counts the cyclic `1-to-0` boundary. | Blueprint Theorem 10 and the elementary proof in this audit. | C8-12 standard cyclic walk/trace source plus standard run identity. | The transition/run identity is standard combinatorics; only its hull-support application is family-specific. | `DIRECT` |
| R8-11 | A factor orbit contributes the weighted orbit polynomial before global multiplication. | Blueprint Theorem 11 and exhaustive orbit checks. | C8-12 weighted walk-generating mechanism; C8-02/C8-04 factor-orbit enumeration contexts. | Weighted cyclic-word enumeration is standard, but no checked source states this exact hull-weighted orbit polynomial. | `UNVERIFIED` |
| R8-12 | The two-state matrix `T_w(u,z)=[[u^w,1],[u^w z^w,1]]` encodes selected source bits and boundary weights. | Blueprint Theorem 12 and transfer validator. | C8-12 matrix-power walk-counting theorem. | The matrix construction is a direct standard transfer device; the weight interpretation follows the frozen support reduction. | `DIRECT` |
| R8-13 | `trace(T_w(u,z)^a)` closes an indexed orbit and counts its weighted cyclic selections. | Blueprint Theorem 13 and closed-walk checks. | C8-12 closed-walk trace identity. | The trace identity transfers directly as combinatorial machinery, not as an external hull theorem. | `DIRECT` |
| R8-14 | The global product over labeled factor orbits is the exact joint enumerator `E(u,z)`. | Blueprint Theorem 14 and Phase-3/6 independent enumerator checks. | C8-01, C8-04, C8-07, C8-10, and C8-11 provide narrower component/counting settings. | No checked source states the complete labeled square-free affine/code-first weighted product. | `UNVERIFIED` |
| R8-15 | Specializing `E(1,1)` gives the total number of distinct labeled factor-selection codes. | Blueprint Theorem 15 and finite count checks. | C8-02, C8-04, C8-10, and C8-11 give exact counts in different families. | Exact counting is known in narrower families; the frozen labeled affine specialization has no verified external identical theorem. | `PARTIAL` |
| R8-16 | Coefficients of `E(1,z)` give the exact labeled hull-dimension distribution. | Blueprint Theorem 16 and exhaustive finite distributions. | C8-02, C8-03, C8-04, C8-05, C8-06, C8-10, and C8-11 give prescribed/fixed-dimension counts in narrower families. | Broad fixed-hull enumeration is known, but the exact frozen distribution is not transferred from those different families. | `PARTIAL` |
| R8-17 | The `z=0` specialization gives the labeled LCD count. | Blueprint Theorem 17 and LCD validator. | C8-01, C8-07, and C8-08 report LCD conditions/constructions in restricted settings. | LCD conditions are established elsewhere, but no exact target-family `z=0` product was verified externally. | `PARTIAL` |
| R8-18 | Logarithmic derivatives/specializations give the mean hull dimension. | Blueprint Theorem 18 and moment checks. | C8-08 explicitly studies average Galois-hull dimensions; C8-04 gives average-related chain-ring formulas. | Average dimensions are known in adjacent families; the target labeled affine expectation follows internally from `E` and is not imported. | `PARTIAL` |
| R8-19 | The second derivative and two-cycle treatment give the exact variance. | Blueprint Theorem 19 and the separate variance case check. | No checked source was verified to state this exact variance for the frozen labeled product; C8-08 is average-only at accessible scope. | The variance corollary is conditional on the internal product; no exact external match was established. | `UNVERIFIED` |

This 19-row architecture is the required central result comparison. The three `DIRECT` entries concern standard combinatorial identities only; they do not convert the complete algebraic enumerator into a known external theorem. The `PARTIAL` entries acknowledge narrower hull, reciprocal, CRT, LCD, and average results without transferring their hypotheses. The `UNVERIFIED` entries are deliberately not presented as absent from the literature.

## 4. What is and is not already present

### 4.1 Already present in checked literature

The checked records establish, in their respective hypotheses:

- finite-field cyclic/negacyclic exact hull dimensions and fixed-dimension counts;
- finite-field constacyclic hull formulas and restricted prescribed-dimension counts;
- chain-ring cyclic serial fixed-hull-dimension counts;
- `Z4` cyclic fixed-2-dimension counts and averages;
- direct-product/non-chain componentwise hull decomposition and lcm formulas;
- average Galois hull dimensions and Galois LCD constructions;
- exact fixed-hull-dimension counts for several generalized cyclic/circulant families;
- the transfer-matrix/closed-walk mechanism and the elementary binary transition/run identity.

Accordingly, the following broad claims are **not safe**: “exact hull enumeration is new,” “CRT hull decomposition is new,” “reciprocal-pair counts are new,” or “the transfer matrix is a new combinatorial method.”

### 4.2 Not verified as an exact prior match

No accessible source in this audit was verified to state the complete product

```text
product_s product_O trace(T_(w_O)(u,z)^(a_O))
```

for the exact combination of:

1. arbitrary labeled square-free affine products of finite fields;
2. simple-root constacyclic factor selections;
3. the frozen code-first second-slot `k`-Galois convention and inverse-Frobenius action on extension components;
4. compatible same-factor-set twists;
5. weighted cyclic boundary support;
6. a joint code-dimension/hull-dimension polynomial for all distinct labeled selections.

This is a **comparison result**, not a proof that no such theorem exists. The final publisher text of the primary 2026 affine article and the corrected full text of the 2023 finite-field article remain inaccessible in this environment.

### 4.3 The primary affine source's explicit gap

The accessible arXiv theorem-bearing source states in its conclusion that enumeration of non-isometric constacyclic codes with a given Galois hull dimension over its affine algebra is an open future problem. This is strong source-level support that the source itself does not supply the present enumeration. It does not establish a field-wide priority claim, and it does not remove the need to compare the adjacent chain-ring, non-chain, finite-field, and generalized cyclic literature.

## 5. Comparison conclusion

The central mathematical formula is internally proved with the existing conditional 19-result audit and independent finite checks. The literature comparison yields:

- **exact fixed-hull enumeration:** known in multiple narrower families;
- **affine/non-chain component hull decomposition:** known in several restricted forms;
- **cyclic binary transition statistic and trace transfer:** standard tools;
- **the exact weighted joint labeled product in the frozen square-free affine/code-first framework:** no exact prior theorem established in the checked records;
- **priority/novelty of that product:** not established.

The defensible publication position is therefore a narrowed, self-contained theorem claim with no firstness or absence claim. The detailed contribution boundary is in `validation/CONTRIBUTION_BOUNDARY.md`.
