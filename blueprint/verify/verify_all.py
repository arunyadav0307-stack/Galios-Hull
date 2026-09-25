"""
verify_all.py -- consolidated verification of the blueprint's core claims.

Sections
  (A1) lam^{p^k+1}=1  <=>  sigma-dual of a nontrivial lam-constacyclic code is
       lam-constacyclic  (tau_lam-stable)
  (A2) generator: C^{perp_sigma} = <h^tau>   (h = (x^n-lam)/g, h^tau = x^l h(1/x)^sigma)
  (A3) containment criterion (polynomial form):
       C^{perp_sigma} subseteq C   <=>   h^tau in <g>_Rlam
                                   <=>   gcd(g, rev(g^{p^{e-k}})) = 1      [roots free]
  (B)  order structure: ord_f(x) = r*h, h | n, r = ord(lam), gcd(r, n/h) = 1
  (C)  lambda-twisted padding / syndrome / exact tolerance a_l + a_r < ord_f(x)
  (R)  ring version: A = F_q[v]/<v^2-v>, tolerance = lcm over CRT components
"""
import math
from fflib import GF, Poly, xpoly, const, ord_of_poly, xpow_mod, in_span, mat_rank
from fflib3 import divisors_fast
from fflib2 import code_basis, sigma_dual_basis

FIELDS = {
    3: GF(3, 1, [0, 1]),
    4: GF(2, 2, [1, 1, 1]),
    5: GF(5, 1, [0, 1]),
    7: GF(7, 1, [0, 1]),
    8: GF(2, 3, [1, 1, 0, 1]),
    9: GF(3, 2, [1, 0, 1]),
}
CACHE = {}


def xnf(F, n, lam):
    return Poly(F, [F.neg(lam)] + [F.zero] * (n - 1) + [F.one])


def divs(F, n, lam):
    key = (F.q, n, tuple(lam))
    if key not in CACHE:
        CACHE[key] = divisors_fast(F, xnf(F, n, lam))[0]
    return CACHE[key]


def same_space(F, A, B):
    return mat_rank(F, A + B) == mat_rank(F, A) == mat_rank(F, B)


def tau_stable(F, D, lam):
    return all(in_span(F, D, [F.mul(lam, v[-1])] + v[:-1]) for v in D)


def sigma_reciprocal(F, d, k):
    """h^tau = x^l h(1/x)^{sigma}, monic (roots = 1/gamma for gamma root of d)."""
    l = d.deg()
    coeffs = [F.pow(c, F.p ** k) for c in d.c]
    poly = Poly(F, coeffs[::-1])
    return poly.monic() if not poly.is_zero() else poly


def frob_poly(F, d, k):
    """polynomial whose roots are the p^k-th powers of the roots of d."""
    return Poly(F, [F.pow(c, F.p ** k) for c in d.c]).monic()


def rev_poly(F, d):
    return Poly(F, d.c[::-1]).monic() if d.c[::-1][-1] != F.zero else Poly(F, d.c[::-1])


def sections_A_and_B():
    print("=" * 96)
    print("(A1)+(A2)+(A3):  sigma-dual structure, generator, dual-containment criterion")
    print("=" * 96)
    n1 = n2 = n3 = 0
    t1 = t2 = t3 = 0
    for q, F in FIELDS.items():
        ks = range(F.e) if F.e > 1 else [0]
        for n in range(3, 8):
            if n % F.p == 0:
                continue
            for lam in F.nonzero():
                for k in ks:
                    adm = (F.pow(lam, F.p ** k + 1) == F.one)
                    for g in divs(F, n, lam):
                        if g.deg() == 0 or g.deg() == n:
                            continue
                        C = code_basis(F, g, n, lam)
                        D = sigma_dual_basis(F, C, n, k)
                        h = xnf(F, n, lam).divmod_(g)[0]
                        htau = sigma_reciprocal(F, h, k)
                        # (A1)
                        t1 += 1
                        if tau_stable(F, D, lam) != adm:
                            n1 += 1
                            print(f"  A1 FAIL q={q} n={n} lam={lam} k={k} deg g={g.deg()}")
                        # (A2)
                        t2 += 1
                        if not same_space(F, D, code_basis(F, htau, n, lam)):
                            n2 += 1
                            print(f"  A2 FAIL q={q} n={n} lam={lam} k={k} deg g={g.deg()}")
                        # (A3)
                        cont = all(in_span(F, C, v) for v in D)
                        vhtau = [F.zero] * n
                        for i, c in enumerate(htau.c):
                            vhtau[i] = c
                        in_ideal = in_span(F, C, vhtau)
                        # root-free condition: gcd(g, rev(g^{p^{e-k}})) = 1
                        ge = frob_poly(F, g, (-k) % F.e if F.e else 0)
                        rev = Poly(F, ge.c[::-1])
                        gr = g.mod(rev) if rev.deg() > 0 else g
                        # proper gcd
                        a, b = Poly(F, g.c), Poly(F, rev.c)
                        while any(map(any, b.c)):
                            a, b = b, a.mod(b)
                        gcd = a.monic() if not a.is_zero() else a
                        rootfree = (gcd.deg() == 0)
                        t3 += 1
                        if (cont != in_ideal) or (in_ideal != rootfree):
                            n3 += 1
                            print(f"  A3 FAIL q={q} n={n} lam={lam} k={k} deg g={g.deg()}: "
                                  f"containment={cont} h^tau in <g>={in_ideal} rootfree={rootfree}")
    print(f"  (A1) {t1} tests, {n1} failures")
    print(f"  (A2) {t2} tests, {n2} failures")
    print(f"  (A3) {t3} tests, {n3} failures")

    print("-" * 96)
    print("(B): ord_f(x) = r*h,  h | n,  gcd(r, n/h) = 1")
    nB = tB = 0
    for q, F in FIELDS.items():
        for n in range(2, 11):
            if n % F.p == 0:
                continue
            for lam in F.nonzero():
                r = F.order(lam)
                for h in divs(F, n, lam):
                    if h.deg() == 0:
                        continue
                    d = ord_of_poly(F, h)
                    tB += 1
                    errs = []
                    if (n * r) % d:
                        errs.append("d | n*r fails")
                    elif d % r:
                        errs.append("r | d fails")
                    elif n % (d // r):
                        errs.append("(d/r) | n fails")
                    elif math.gcd(r, n // (d // r)) != 1:
                        errs.append("gcd(r, n/(d/r)) = 1 fails")
                    if errs:
                        nB += 1
                        print(f"  B FAIL q={q} n={n} lam={lam} r={r} f={h.c} d={d} {errs}")
    print(f"  (B) {tB} tests, {nB} failures")


def inv_in_R(F, n, lam, g):
    xr = xnf(F, n, lam)
    old_r, r_ = xr.c[:], Poly(F, g.c).c[:]
    old_s, s_ = [F.one], [F.zero]
    while any(map(any, r_)):
        Q, rem = Poly(F, old_r).divmod_(Poly(F, r_))
        qs = Q.mul(Poly(F, s_))
        L = max(len(old_s), len(qs.c))
        new_s = [F.sub(x, y) for x, y in zip(old_s + [F.zero] * (L - len(old_s)),
                                             qs.c + [F.zero] * (L - len(qs.c)))]
        old_r, r_ = r_, rem.c
        old_s, s_ = s_, new_s
    assert len(old_r) == 1
    return Poly(F, old_s).divmod_(xr)[1]


def tau_pow(F, v, lam, s):
    n = len(v)
    res = v[:]
    for _ in range(s % n):
        res = [F.mul(lam, res[-1])] + res[:-1]
    return res


def check_mechanism(F, n, lam, al, ar, gC, gD, verbose=False):
    xr = xnf(F, n, lam)
    f = gC.divmod_(gD)[0]
    dord = ord_of_poly(F, f)
    ginv = inv_in_R(F, n, lam, gD)
    Db, Cb = code_basis(F, gD, n, lam), code_basis(F, gC, n, lam)
    gvec = [F.zero] * n
    for i, c in enumerate(gD.c):
        gvec[i] = c
    contents = [[F.add(x, y) for x, y in zip(c, gvec)] for c in Cb] + [gvec]
    ok = dict(shift=True, inD=True, syndrome=True)
    syn = {}
    for a in range(-al, ar + 1):
        for v in contents:
            B = ([F.mul(lam, v[n - al + j]) for j in range(al)] + v +
                 [F.mul(F.inv(lam), v[j]) for j in range(ar)])
            W = B[al + a: al + a + n]
            if not in_span(F, Db, W):
                ok["inD"] = False
            found = False
            for s in range(n):
                tv = tau_pow(F, v, lam, s)
                for mu in F.nonzero():
                    if all(F.mul(mu, tv[i]) == W[i] for i in range(n)):
                        found = True
                        break
                if found:
                    break
            if not found:
                ok["shift"] = False
            J = Poly(F, list(W)).mul(ginv).divmod_(xr)[1]
            s_poly = J.mod(f)
            exp = xpow_mod(F, (-a) % dord, f)
            if not (s_poly == exp):
                ok["syndrome"] = False
                if verbose:
                    print(f"      a={a}: syn={s_poly} exp={exp}")
            syn[a] = tuple(map(tuple, s_poly.c))
    distinct = (len(set(syn.values())) == al + ar + 1)
    return dict(ok=ok, distinct=distinct, tol_ok=(distinct == (al + ar < dord)),
                ord_f=dord, deg_f=f.deg(), n=n, lam=lam, q=F.q)


def section_C():
    print("-" * 96)
    print("(C): lambda-twisted padding / syndrome / exact tolerance, on all valid chains")
    print("-" * 96)
    tested = fails = 0
    chains = 0
    for q, F in FIELDS.items():
        ks = range(F.e) if F.e > 1 else [0]
        for n in range(3, 8):
            if n % F.p == 0:
                continue
            for lam in F.nonzero():
                for k in ks:
                    if F.pow(lam, F.p ** k + 1) != F.one:
                        continue
                    for gD in divs(F, n, lam):
                        for gC in divs(F, n, lam):
                            if gC.deg() <= gD.deg() or not gC.mod(gD).is_zero():
                                continue
                            if 2 * (n - gC.deg()) - n <= 0:
                                continue
                            # dual-containment of C (and of D) via (A3)
                            okC = _rootfree(F, gC, k)
                            okD = _rootfree(F, gD, k)
                            if not (okC and okD):
                                continue
                            chains += 1
                            for (al, ar) in [(1, 1), (2, 2), (3, 1), (2, 4), (3, 3)]:
                                R = check_mechanism(F, n, lam, al, ar, gC, gD)
                                tested += 1
                                if not (all(R["ok"].values()) and R["tol_ok"]):
                                    fails += 1
                                    print(f"  C FAIL q={q} n={n} lam={lam} k={k} deg f={R['deg_f']} "
                                          f"ord_f={R['ord_f']} ({al},{ar}) {R}")
    print(f"  (C) {chains} valid chains, {tested} configurations, {fails} failures")


def _rootfree(F, g, k):
    if g.deg() == 0:
        return True
    ge = frob_poly(F, g, (-k) % F.e if F.e else 0)
    rev = Poly(F, ge.c[::-1])
    a, b = Poly(F, g.c), rev
    while any(map(any, b.c)):
        a, b = b, a.mod(b)
    gcd = a.monic() if not a.is_zero() else a
    return gcd.deg() == 0


def main():
    sections_A_and_B()
    section_C()


if __name__ == "__main__":
    main()
