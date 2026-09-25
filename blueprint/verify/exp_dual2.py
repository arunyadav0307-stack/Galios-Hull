"""
exp_dual2.py -- pin down (by exhaustive computation) the exact structural facts
about the sigma-Galois dual of a lambda-constacyclic code.  Only verified
statements will be promoted to theorems in the blueprint.

Definitions used
  R_lam   = F_q[x]/<x^n - lam>,  lam in F_q^*
  C       = <g>  (monic g | x^n - lam), h = (x^n - lam)/g
  sigma   = Frobenius^k  (k in {0,...,e-1})
  b(u,v)  = sum_i u_i sigma(v_i)        ("sigma-Galois inner product")
  D       = C^{perp_sigma} = {u : b(u,v)=0 for all v in C}   (computed by linear algebra)
  d^tau   = x^{deg d} d(1/x)^sigma      ("sigma-twisted reciprocal": roots 1/gamma)

Conjectures tested
  (A1) lam^{p^k+1} = 1  <=>  D is lam-constacyclic  (nontrivial C)
  (A2) D = <h^tau>   and   D subseteq C  <=>  g | h^tau
  (A3) D subseteq C  <=>  Z(C) ∩ Z(C)^{-sigma^{-1}} = empty
"""
from fflib import GF, Poly, xpoly, const, in_span, mat_rank, nullspace
from fflib3 import divisors_fast
from fflib2 import code_basis, sigma_dual_basis

FIELDS = {
    4: GF(2, 2, [1, 1, 1]),
    8: GF(2, 3, [1, 1, 0, 1]),
    9: GF(3, 2, [1, 0, 1]),
    3: GF(3, 1, [0, 1]),
    5: GF(5, 1, [0, 1]),
    7: GF(7, 1, [0, 1]),
}


def xnf(F, n, lam):
    return Poly(F, [F.neg(lam)] + [F.zero] * (n - 1) + [F.one])


def ideal_basis(F, d, n, lam):
    return code_basis(F, d, n, lam)


def same_space(F, A, B):
    return mat_rank(F, A) == mat_rank(F, B) and mat_rank(F, A + B) == mat_rank(F, A)


def tau_invariant(F, D, n, lam):
    return all(in_span(F, D, [F.mul(lam, v[-1])] + v[:-1]) for v in D)


def sigma_reciprocal(F, d, k, n, lam):
    """monic polynomial with roots {1/gamma : gamma root of d}, coefficients twisted
    by sigma (Frobenius^k).  Computed as x^l * d(1/x)^{sigma}, normalised."""
    l = d.deg()
    coeffs = [F.pow(c, F.p ** k) for c in d.c]
    poly = Poly(F, coeffs[::-1])          # x^l * d(1/x)^{sigma}
    return poly.monic() if not poly.is_zero() else poly


def divisors_of(F, n, lam, cache={}):
    key = (F.q, n, tuple(lam))
    if key not in cache:
        cache[key] = divisors_fast(F, xnf(F, n, lam))[0]
    return cache[key]


def main():
    print("=" * 100)
    print("(A1) lam^{p^k+1}=1  <=>  sigma-dual of every nontrivial lam-constacyclic code is lam-constacyclic")
    print("=" * 100)
    bad = 0
    for q, F in FIELDS.items():
        ks = range(F.e) if F.e > 1 else [0]
        for n in range(3, 7):
            if n % F.p == 0:
                continue
            for lam in F.nonzero():
                adm = None
                for k in ks:
                    adm = (F.pow(lam, F.p ** k + 1) == F.one)
                    for g in divisors_of(F, n, lam):
                        if g.deg() == 0 or g.deg() == n:
                            continue
                        C = ideal_basis(F, g, n, lam)
                        D = sigma_dual_basis(F, C, n, k)
                        ti = tau_invariant(F, D, n, lam)
                        if ti != adm:
                            bad += 1
                            print(f"  MISMATCH q={q} n={n} lam={lam} k={k} deg g={g.deg()} "
                                  f"adm={adm} tau-invariant={ti}")
    print(f"  -> {bad} mismatches\n")

    print("=" * 100)
    print("(A2) D = <h^tau>  and  (D subset C  <=>  g | h^tau)")
    print("=" * 100)
    bad_gen = bad_cont = 0
    tested = 0
    for q, F in FIELDS.items():
        ks = range(F.e) if F.e > 1 else [0]
        for n in range(3, 7):
            if n % F.p == 0:
                continue
            for lam in F.nonzero():
                for k in ks:
                    for g in divisors_of(F, n, lam):
                        if g.deg() == 0 or g.deg() == n:
                            continue
                        C = ideal_basis(F, g, n, lam)
                        D = sigma_dual_basis(F, C, n, k)
                        h = xnf(F, n, lam).divmod_(g)[0]
                        htau = sigma_reciprocal(F, h, k, n, lam)
                        tested += 1
                        # generator identity: is D the ideal <htau> (as a subspace)?
                        htau_basis = ideal_basis(F, htau, n, lam)
                        if not same_space(F, D, htau_basis):
                            bad_gen += 1
                            print(f"  GEN MISMATCH q={q} n={n} lam={lam} k={k} deg g={g.deg()}")
                        cont = all(in_span(F, C, v) for v in D)
                        pred = xnf(F, n, lam).mod(htau).is_zero() and g.mod(htau).is_zero()
                        if cont != pred:
                            bad_cont += 1
                            print(f"  CONT MISMATCH q={q} n={n} lam={lam} k={k} deg g={g.deg()} "
                                  f"containment={cont} g|h^tau={pred}")
    print(f"  -> {tested} codes tested: {bad_gen} generator mismatches, "
          f"{bad_cont} containment mismatches\n")


if __name__ == "__main__":
    main()
