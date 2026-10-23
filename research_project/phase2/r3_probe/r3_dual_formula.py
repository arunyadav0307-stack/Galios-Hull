"""
R3 probe, part 2 -- is the Hermitian dual over R_e componentwise, and under what conditions?

Claim under test (derived, then checked here):

  Let R_e = F_{q^2}[u]/(u^e - 1) and let e_j be the CRT idempotents, indexed by the e-th
  roots of unity beta_j in F_{q^2}.  Conjugation is the coefficientwise Frobenius x -> x^q.
  It need NOT fix the idempotents: it sends e_j to e_{sigma(j)}, where beta_{sigma(j)} = beta_j^q.

  Writing C = direct_sum_j e_j C_j one gets, for x, y in R_e^n,

      <x,y>_H = sum_j e_{sigma(j)} * <x^{(j)}, y^{(j)}>_F

  hence x lies in C^{perp_H} iff  <x^{(j)}, y^{(j)}>_F = 0  for every j and every y in C, i.e.

      C^{perp_H} = direct_sum_j e_j * ( C_{sigma^{-1}(j)} )^{perp_H}          (CROSSED FORMULA)

  and therefore

      C^{perp_H} <= C   <=>   for every j:  ( C_{sigma^{-1}(j)} )^{perp_H} <= C_j .

  When sigma = identity this is the naive componentwise product condition.  With e | q+1 one
  has beta^q = beta^{-1}, so sigma(j) = -j mod e; sigma is the identity only for e <= 2.

The script builds every lambda-constacyclic code over R_e as a CRT tuple (C_1..C_e), computes
its TRUE dual by linear algebra over F_{q^2} directly from the paper's ring-valued definition,
and compares with the crossed formula.  It then compares two counts:

    naive  : #{tuples with every C_j dual-containing}
    crossed: #{tuples satisfying (C_{sigma^{-1}(j)})^{perp} <= C_j for all j}

against the true number of dual-containing codes.

ASCII only, stdlib only.
"""

import itertools
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r3_probe import GF, find_irreducible, Ring, rref, nullspace, in_span, field_codes, ring_dual_basis


def setup(p, q, e, n):
    m, t = 0, q
    while t % p == 0:
        t //= p
        m += 1
    assert p ** m == q
    F = find_irreducible(p, 2 * m)
    F.conj_f = [F.pow(a, q) for a in range(F.Q)]
    R = Ring(F, e)
    R.set_frobenius(q)
    roots = R.roots
    # idempotents e_j: e_j(beta_m) = delta_jm,   e_j = (1/e) sum_t beta_j^{-t} u^t
    inv_e = None
    for x in range(1, F.Q):
        if F.mul[x][e % p] == F.one:      # e as an element of F_p, not e mod |F|
            inv_e = x
            break
    assert inv_e is not None
    idem = []
    for j, b in enumerate(roots):
        coords = []
        for t in range(e):
            bt = F.pow(b, (e - t) % e)          # beta^{-t}
            coords.append(F.mul[inv_e][bt])
        idem.append(R.elt(coords))
    for j in range(e):
        for m in range(e):
            assert R.eval_at(idem[j], roots[m]) == (F.one if j == m else F.zero), (j, m)

    # sigma: how the Hermitian involution permutes the idempotents
    sigma = {}
    for j in range(e):
        cj = R.conj[idem[j]]
        sigma[j] = next(m for m in range(e) if idem[m] == cj)
    return F, R, roots, sigma, idem


def build_code(R, F, idem, comps, n, e):
    """R-code from the tuple (C_1..C_e) of F-codes, as direct_sum_j e_j C_j."""
    vecs = []
    for j, Cj in enumerate(comps):
        for c in Cj:                       # c is a length-n vector over F
            v = []
            for i in range(n):
                scalar = R.elt([c[i]] + [F.zero] * (e - 1))   # embed the F-scalar into R
                v.extend(R.digits[R.mul[idem[j]][scalar]])
            vecs.append(v)
    return rref(F, vecs, n * e)[0]


def field_dual(F, C, n):
    return nullspace(F, [[F.conj_f[y[i]] for i in range(n)] for y in C], n)


def main():
    for (p, q, e, n, label) in [(3, 3, 2, 2, "q=3, e=2, n=2  (two components, e = 2)"),
                                (2, 2, 3, 2, "q=2, e=3, n=2  (three components, e = 3)")]:
        F, R, roots, sigma, idem = setup(p, q, e, n)
        print("=" * 78)
        print(label)
        print(f"  q={q}, e={e}, n={n}, F=F_{F.Q}, |R_e|={R.size}")
        print(f"  roots        : {roots}")
        print(f"  sigma        : { {j: sigma[j] for j in range(e)} }")
        print(f"  sigma == id  : {all(sigma[j] == j for j in range(e))}")

        lam = 1
        alphas = [R.eval_at(lam, b) for b in roots]
        codes = [field_codes(F, n, a) for a in alphas]

        true_dc = naive = crossed = tuples = 0
        formula_ok = 0
        naive_ok = 0
        for combo in itertools.product(*[range(len(c)) for c in codes]):
            comps = [codes[j][combo[j]] for j in range(e)]
            C = build_code(R, F, idem, comps, n, e)
            tuples += 1

            dual = ring_dual_basis(R, F, C, n, e)
            is_dc = all(in_span(F, C, v, n * e) for v in dual)
            true_dc += is_dc

            # crossed prediction of the dual
            pred_comps = [field_dual(F, comps[sigma_inv], n) for sigma_inv in
                          [next(k for k in range(e) if sigma[k] == j) for j in range(e)]]
            pred = build_code(R, F, idem, pred_comps, n, e)
            if (all(in_span(F, pred, v, n * e) for v in dual)
                    and all(in_span(F, dual, v, n * e) for v in pred)):
                formula_ok += 1

            if all(all(in_span(F, comps[j], v, n) for v in field_dual(F, comps[j], n))
                   for j in range(e)):
                naive += 1
            if all(in_span(F, comps[j], v, n) for j in range(e)
                   for v in field_dual(F, comps[next(k for k in range(e) if sigma[k] == j)], n)):
                crossed += 1

        print(f"  tuples (codes)                 : {tuples}")
        print(f"  true dual-containing           : {true_dc}")
        print(f"  crossed-formula exact match    : {formula_ok}/{tuples}")
        print(f"  naive product prediction       : {naive}   {'MATCHES' if naive == true_dc else 'WRONG'}")
        print(f"  crossed-condition prediction   : {crossed}   {'MATCHES' if crossed == true_dc else 'WRONG'}")


if __name__ == "__main__":
    main()
