"""
verify_ceiling.py -- evidence for the *ceiling theorem* (Thm 7 of the final blueprint):

    ord_f(x) = r*h with h | n,  r = ord(lambda) | p^kappa + 1
    =>  Theta | (p^kappa + 1) * n   =>  T/L < (p^kappa + 1)/(p^kappa + 2)
    and the bound is ATTAINED: lambda of maximal order r = p^kappa + 1 with h = n.

Instance verified here (Flagship B of the blueprint):
    q = 16 = 2^4, kappa = 2 (Hermitian over F_16 / F_4), n = 7,
    lambda of order 5 = p^kappa + 1, dual-containing degree-3 divisor f of x^7 - lambda
    with ord_f(x) = 35 = 5*7  ->  Theta = 35, T_max = 34 > n = 7, T/L = 34/41 = 0.829.
Also re-derives the cyclic ceiling (lambda = 1 => ord_f | n => T/L < 1/2) on the same field.
"""
import itertools
from fflib import GF, Poly, const, ord_of_poly, ptrim, in_span
from fflib2 import code_basis, sigma_dual_basis
from verify_mechanism import xnf, divs, _dual_containing

Q, MOD, E, KAP, N = 16, [1, 1, 0, 0, 1], 4, 2, 7     # F_16 = F_2[x]/(x^4+x+1)


def all_words(F, basis):
    elems = F.elements()
    for coeffs in itertools.product(range(len(elems)), repeat=len(basis)):
        v = [F.zero] * len(basis[0])
        for i, ci in enumerate(coeffs):
            if ci:
                a = elems[ci]
                v = [F.add(x, F.mul(a, y)) for x, y in zip(v, basis[i])]
        yield v


def min_dist(F, basis, exclude=None, cap=1):
    best = None
    for v in all_words(F, basis):
        if all(c == F.zero for c in v):
            continue
        if exclude is not None and in_span(F, exclude, v):
            continue
        w = sum(1 for c in v if c != F.zero)
        if best is None or w < best:
            best = w
        if best <= cap:
            break
    return best


def main():
    F = GF(2, E, MOD)
    print(f"F_{Q} = F_2[x]/(x^4+x+1); kappa = {KAP}; Hermitian twist sigma(a) = a^(2^{KAP}) = a^4")
    print(f"admissible weights: lambda^(p^kappa+1) = lambda^5 = 1, i.e. r = ord(lambda) | 5")
    lams = [a for a in F.nonzero() if F.pow(a, 2 ** KAP + 1) == F.one]
    byorder = {}
    for a in lams:
        byorder.setdefault(F.order(a), []).append(a)
    print("  weights by order:", {k: len(v) for k, v in sorted(byorder.items())})
    print()
    print("== (1) attainability of Theta = (p^kappa+1)*n = 5*7 = 35 ==")
    for r, lams_r in sorted(byorder.items(), reverse=True):
        lam = lams_r[0]
        best = []
        for g in divs(F, N, lam):
            if g.deg() == 0 or g.deg() >= N:
                continue
            o = ord_of_poly(F, g)
            dc = _dual_containing(F, N, lam, g, KAP)
            best.append((o, g.deg(), dc))
        best.sort(reverse=True)
        print(f"  lambda with r = {r}: max ord_f = {best[0][0]}, dual-containing top entries: "
              f"{[b for b in best if b[2]][:3]}")
    lam5 = byorder[5][0]
    g = None
    for cand in divs(F, N, lam5):
        if 0 < cand.deg() < N and ord_of_poly(F, cand) == 35 and _dual_containing(F, N, lam5, cand, KAP):
            g = cand
            break
    k = N - g.deg()
    print(f"  chosen chain: C = <g>, deg g = {g.deg()}, ord_f = {ord_of_poly(F, g)} = 5*7 = (p^kappa+1)*n")
    print()
    print("== (2) the quantum component and its exact parameters ==")
    C = code_basis(F, g, N, lam5)
    D = sigma_dual_basis(F, C, N, KAP)
    Kq = N - 2 * len(D)                      # in F_16-units? no: logical units in F_4-units
    kF = N - g.deg()
    print(f"  C = <g>: [{N},{kF}]_{Q};  Hermitian dual dim = {len(D)};  containment: "
          f"{all(in_span(F, C, v) for v in D)}")
    dC, dD, dQ = min_dist(F, C), min_dist(F, D), min_dist(F, C, exclude=D)
    print(f"  d(C) = {dC}, d(C^perp_H) = {dD}, d(C \\ C^perp_H) = {dQ}  ->  [[7,{2*kF-N},{dQ}]]_4")
    print()
    print("== (3) the padded family and the ceiling ==")
    Th = 35
    for T in (0, 2, 6, 20, 34):
        print(f"  T = {T:2d}: L = {N+T:2d} F_16-symbols = {4*(N+T):3d} F_4-symbols "
              f"({8*(N+T):3d} qubits if decomposed);  T/L = {T/(N+T):.3f}")
    print(f"  Theta = lcm(ord_f) = {Th};  T_max = {Th-1} > n = {N};  "
          f"T/L = {(Th-1)/(N+Th-1):.3f};  bound (p^kappa+1)/(p^kappa+2) = 5/6 = 0.833")
    print()
    print("== (4) cyclic control (lambda = 1): the ceiling T/L < 1/2 ==")
    for g in divs(F, N, F.one):
        if 0 < g.deg() < N:
            o = ord_of_poly(F, g)
            assert N % o == 0, (o, N)
            print(f"  divisor deg {g.deg()}: ord_f = {o} divides n = {N}  ->  T <= {o-1} < n; "
                  f"T/L <= {(o-1)/(N+o-1):.3f}")
    print("  => for lambda = 1 the tolerance never exceeds the block length; the ceiling")
    print("     statement of the blueprint is corroborated on this field.")


if __name__ == "__main__":
    main()
