"""
exp_dual.py -- determine the CORRECT structural facts about the sigma-Galois dual
of a lambda-constacyclic code over F_q, by exhaustive computation.

For each (q, n, lambda, k) and each monic divisor g | x^n - lambda we compute
  * C = <g>  (as an F_q-subspace of F_q^n),
  * D = C^{perp_sigma} for the pairing <u,v>_sigma = sum_i u_i v_i^{p^k},
  * the constacyclic parameter mu with tau_mu(D) = D  (search over F_q^*),
  * the monic "generator" polynomial h_D | x^n - mu whose roots match D,
  * whether D subseteq C,
  * candidate algebraic predictors:
      (P1) lambda^{p^k+1} = 1
      (P2) g has no sigma-self-reciprocal root pair  (gamma^{sigma} * gamma' = ... ),
  so that the blueprint states only verified theorems.
"""
from fflib import GF, Poly, xpoly, const, ord_of_poly, nullspace, mat_rank, in_span
from fflib3 import divisors_fast
from fflib2 import code_basis, sigma_dual_basis

FIELDS = {
    4: GF(2, 2, [1, 1, 1]),
    8: GF(2, 3, [1, 1, 0, 1]),
    16: GF(2, 4, [1, 1, 0, 0, 1]),
    9: GF(3, 2, [1, 0, 1]),
    3: GF(3, 1, [0, 1]),
    5: GF(5, 1, [0, 1]),
    7: GF(7, 1, [0, 1]),
    25: GF(5, 2, [2, 0, 1]),   # F_25 = F_5[x]/(x^2+2)
}


def xnf(F, n, lam):
    return Poly(F, [F.neg(lam)] + [F.zero] * (n - 1) + [F.one])


def tau(F, v, mu):
    return [F.mul(mu, v[-1])] + v[:-1]


def is_constacyclic_with(F, D, n, mu):
    return all(in_span(F, D, tau(F, v, mu)) for v in D)


def main():
    print("q  n  lam  k | adm  | #g  #(D subset C)  #(D constacyclic)  mu's        "
          "agree(adm<->allcontained)")
    print("----------------------------------------------------------------------------------")
    for q, F in FIELDS.items():
        ks = range(F.e) if F.e > 1 else [0]
        for n in range(2, 8):
            if n % F.p == 0:
                continue
            for lam in F.nonzero():
                divs = divisors_fast(F, xnf(F, n, lam))[0]
                nonconst = [g for g in divs if g.deg() > 0]
                for k in ks:
                    adm = (F.pow(lam, F.p ** k + 1) == F.one)
                    ncont = 0
                    mus = set()
                    noncstc = 0
                    for g in nonconst:
                        C = code_basis(F, g, n, lam)
                        D = sigma_dual_basis(F, C, n, k)
                        if all(in_span(F, C, v) for v in D):
                            ncont += 1
                        found = [mu for mu in F.nonzero()
                                 if is_constacyclic_with(F, D, n, mu)]
                        for mu in found:
                            mus.add(tuple(mu))
                        if not found:
                            noncstc += 1
                    agree = (adm == (ncont == len(nonconst)))
                    print(f"{q:2d} {n:2d} {str(lam):10s} {k} | {int(adm)}   | "
                          f"{len(nonconst):2d}  {ncont:2d}              {len(nonconst)-noncstc:2d}"
                          f"                {sorted(mus)}  {agree}")
    print()


if __name__ == "__main__":
    main()
