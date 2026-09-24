# Phase-9 Manuscript Notation Audit

**Audit date:** 2026-09-24
**Base commit:** `2be1c505c4d79741bc5378bc20de0cd2d17b05e8`

The proposed manuscript uses the notation below. First-use locations refer to the proposed section architecture, not final page numbers.

| Symbol | Meaning | First use | Consistency check |
|---|---|---:|---|
| `p` | prime characteristic | 2 | Never used as a polynomial or probability variable. |
| `e` | base-field extension degree in `q=p^e` | 2 | Distinct from orbit length and factor degree. |
| `q` | base field size `p^e` | 2 | Always the base field `F_q`. |
| `m_s` | component extension degree over `F_q` | 2 | Component index `s` is retained in every use. |
| `d_s` | absolute component degree `e m_s` | 2 | Recommended auxiliary symbol; never replaces `m_s`. |
| `K_s` | component field `F_(q^(m_s))=F_(p^(d_s))` | 2 | Used for component linear algebra and factorization. |
| `A` | fixed square-free affine algebra, `A ~= product_s K_s` | 2 | Preferred ambient-algebra symbol. |
| `R` | legacy/quoted ambient-ring alias | 2, warning box | Not used in the main theorem; never confused with `rho`. |
| `n` | constacyclic code length | 2 | Subject to `gcd(n,p)=1`. |
| `lambda_s` | nonzero component constacyclic twist | 2 | Lowercase lambda is never used for a relation polynomial. |
| `M_s` | modulus `x^n-lambda_s` | 3 | Square-free under the standing assumptions. |
| `mathcal F_s` | set of distinct monic irreducible factors of `M_s` | 3 | This is the factor-set symbol. |
| `F_s` | ambiguous legacy shorthand | 3, warning box | Prohibited in final prose; always write `mathcal F_s`. |
| `J_s` | selected subset of `mathcal F_s` | 3 | `epsilon=1` records membership in `J_s`. |
| `g_(J_s)` | product of selected factors, generator polynomial | 3 | Do not call it a check polynomial. |
| `h_(J_s)` | check polynomial `M_s/g_(J_s)` | 3 | Used in the dual-generator statement. |
| `k` | Galois/Frobenius iteration parameter, `0<=k<e` | 4 | Never used for code dimension; code dimension uses `K` or `r`. |
| `sigma_(s,k)` | `a -> a^(p^k)` on `K_s` | 4 | The second-slot map. |
| `rho_(s,k)` | `a -> a^(p^(d_s-k))` | 4 | The inverse-Frobenius map; `rho=sigma^(-1)`. |
| `<x,y>_(s,k)` | code-first second-slot pairing `sum_i x_i sigma(y_i)` | 4 | Codeword is first slot in the dual definition. |
| `C` | a component or global code, context labeled | 3/4 | State component/global level whenever ambiguous. |
| `C(J)` | global code indexed by the tuple of labeled selections | 8 | Never means an equivalence class. |
| `D_code-first(C)` | frozen code-first dual | 4 | Must not be shortened to `D` in comparison passages. |
| `D_candidate(C)` | candidate-first comparison dual | 4 | Always defined separately. |
| `tau_(s,k)` | reciprocal-induced permutation of `mathcal F_s` | 5 | Only a same-factor-set permutation under compatibility. |
| `alpha` | a root of `M_s` or a generic root in the root-action proof | 5 | Never used as a field component label. |
| `O` | one orbit of `tau_(s,k)` | 5 | Orbit index is uppercase `O`; component index remains `s`. |
| `a_O` | length of orbit `O` | 5 | Not confused with a scalar or field element. |
| `d_O` | common `K_s`-degree of factors in orbit `O` | 5 | Distinct from absolute component degree `d_s`. |
| `w_O` | global `F_q` weight `m_s d_O` | 5 | Same for every position in one orbit. |
| `epsilon_i` | binary selection indicator, `1` means selected generator factor | 5 | Cyclic index is modulo `a_O`. |
| `b_O` | cyclic `1-to-0` boundary statistic | 5 | It is a statistic, not a new algebraic object. |
| `P_(a,w)(z)` | one-orbit hull polynomial, `trace(T_w(1,z)^a)` | 6 | Uses `a,w` as arguments, not component labels. |
| `T_w(u,z)` | two-state weighted transfer matrix | 7 | Rows are source states and columns destination states. |
| `E(u,z)` | global joint generating polynomial | 8 | `u` is code dimension and `z` is hull dimension. |
| `K` | exponent/realized global code dimension in coefficient extraction | 8 | Never used for a component field; fields are `K_s`. |
| `H` | exponent/realized global hull dimension in coefficient extraction | 8 | Never used for a field or a code. |
| `H_k(C)` | code-first `k`-Galois hull `C intersection D_code-first(C)` | 4 | State the pairing when first introduced. |
| `sigma_k^2` | composition of two Frobenius automorphisms | 4 | Never interpreted as scalar exponent `2 p^k`. |
| `R`/`rho` | two visually similar symbols | 2/4 | `R` is retired from the main notation; `rho` is the inverse map. |

## Notation decisions

1. Use `A` for the affine algebra and reserve `R` for quotations from external ring literature. This removes the `R`/`rho` collision.
2. Use `mathcal F_s` exclusively for factor sets. The bare `F_s` is not permitted because it can be mistaken for a field.
3. Use `K_s` for component fields and `K,H` only as coefficient exponents in the global polynomial.
4. Use `d_s=e m_s` for absolute field degree and `d_O` for common factor degree; use `w_O=m_s d_O` for the global dimension weight.
5. Use `C` with a subscript or `C(J)` whenever a component code and a global product code appear in the same paragraph.
6. Introduce every symbol before its first equation. Do not reuse `alpha`, `k`, `R`, or `F_s` for a second meaning.

## Consistency checks

- No main-theorem symbol has two meanings after the decisions above.
- Component index `s`, orbit index `O`, and cyclic position index `i` are separate.
- Field notation `K_s` is not mixed with ring notation `A`.
- The code dimension is the `u` exponent, not its codimension; this follows from destination weighting `u^(w(1-epsilon_i))`.
- The hull dimension is the `z` exponent and is always an `F_q`-dimension in the global theorem.
- `P_(a,w)` is a specialization of the same `T_w` used in `E`; it is not a second independently defined polynomial.
