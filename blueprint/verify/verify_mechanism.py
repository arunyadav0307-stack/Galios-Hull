"""
verify_mechanism.py -- verification of the synchronization mechanism with the
lambda-twisted padding.

Padding (new definition, reduces to the known cyclic padding for lambda = 1):
    transmitted block  =  the segment (s_v(j))_{j = -a_l}^{n + a_r - 1} of the
    bi-infinite lambda-periodic sequence   s_v(j) = lambda^{-floor(j/n)} v_{j mod n}.
The receiver's window for misalignment a in [-a_l, a_r] is (s_v(a),...,s_v(a+n-1)).

Verified here:
  (i)   the window is a scalar multiple of a lambda-constacyclic shift of v;
  (ii)  hence the window word lies in D whenever v in D;
  (iii) its synchronisation syndrome (divide by g_D in R_lambda, then reduce
        mod f) equals x^{-a} mod f, independently of the content word;
  (iv)  the syndromes are pairwise distinct  <=>  a_l + a_r < ord_f(x).
"""
import sys
from fflib import GF, Poly, const, xpoly, ord_of_poly, xpow_mod, in_span
from fflib3 import divisors_fast
from fflib2 import code_basis, sigma_dual_basis
from verify_all import xnf, divs, sigma_reciprocal, check_mechanism


def T_shift(F, lam, c):
    """multiplication by x in R_lambda = F_q[x]/(x^n - lambda)."""
    return [F.mul(lam, c[-1])] + list(c[:-1])


def x_pow_minus_a_in_R(F, n, lam, a, order):
    """x^{-a} in R_lambda, independent of xpow_mod: T^{(-a) mod order}(1)."""
    c = [F.zero] * n
    c[0] = F.one
    for _ in range((-a) % order):
        c = T_shift(F, lam, c)
    return Poly(F, c)

FIELDS = {
    2: GF(2, 1, [0, 1]),
    3: GF(3, 1, [0, 1]),
    4: GF(2, 2, [1, 1, 1]),
    5: GF(5, 1, [0, 1]),
    7: GF(7, 1, [0, 1]),
    8: GF(2, 3, [1, 1, 0, 1]),
    9: GF(3, 2, [1, 0, 1]),
}


def s_seq(F, v, n, lam, j):
    """lambda-periodic continuation: s_v(j) = lam^{-floor(j/n)} v_{j mod n}."""
    q, r = divmod(j, n)          # python floor division
    return F.mul(F.pow(F.inv(lam), q), v[r])


def window(F, v, n, lam, a):
    return [s_seq(F, v, n, lam, a + i) for i in range(n)]


def block(F, v, n, lam, al, ar):
    return [s_seq(F, v, n, lam, j) for j in range(-al, n + ar)]


def tau_pow(F, v, lam, s):
    n = len(v)
    res = v[:]
    for _ in range(s % n):
        res = [F.mul(lam, res[-1])] + res[:-1]
    return res


def mechanism(F, n, lam, al, ar, gC, gD, verbose=False):
    """full check on a single chain, with the general padding rule."""
    xr = xnf(F, n, lam)
    f = gC.divmod_(gD)[0]
    dord = ord_of_poly(F, f)
    # window words lie in D = <gD>, i.e. they are polynomials of degree < n
    # divisible by the monic polynomial gD (valid because gD | x^n - lambda);
    # the quotient in R_lambda is therefore computed by ordinary division.
    use_div = (gD.deg() > 0)
    Db, Cb = code_basis(F, gD, n, lam), code_basis(F, gC, n, lam)
    gvec = [F.zero] * n
    for i, c in enumerate(gD.c):
        gvec[i] = c
    contents = [[F.add(x, y) for x, y in zip(c, gvec)] for c in Cb] + [gvec]
    flags = dict(shift=True, inD=True, syndrome=True, content_free=True)
    syn = {}
    for a in range(-al, ar + 1):
        vals = set()
        for v in contents:
            W = window(F, v, n, lam, a)
            if not in_span(F, Db, W):
                flags["inD"] = False
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
                flags["shift"] = False
            if use_div:
                J = Poly(F, list(W)).divmod_(gD)[0]
            else:
                J = Poly(F, list(W))
            sp = J.mod(f)
            exp = x_pow_minus_a_in_R(F, n, lam, a, dord).mod(f)   # independent
            if not (sp == exp):
                flags["syndrome"] = False
                if verbose:
                    print(f"      syndrome mismatch a={a}: {sp} vs {exp}")
            vals.add(tuple(map(tuple, sp.c)))
        if len(vals) != 1:
            flags["content_free"] = False
        syn[a] = vals
    distinct = (len(syn) == al + ar + 1) and len(set().union(*syn.values())) == al + ar + 1
    return dict(flags=flags, distinct=distinct, ord_f=dord,
                tol_ok=(distinct == (al + ar < dord)), deg_f=f.deg(),
                n=n, lam=lam, q=F.q, dim=2 * (n - gC.deg()) - n, al=al, ar=ar)


def sweep():
    print("=" * 100)
    print("MECHANISM SWEEP: all chains (C,D), admissible lambda, dual-containing C and D")
    print("=" * 100)
    tested = fails = 0
    for q, F in FIELDS.items():
        ks = range(F.e) if F.e > 1 else [0]
        for n in range(3, 8):
            if n % F.p == 0:
                continue
            for lam in F.nonzero():
                for k in ks:
                    if F.pow(lam, F.p ** k + 1) != F.one:
                        continue
                    ds = divs(F, n, lam)
                    for gD in ds:
                        for gC in ds:
                            if gC.deg() <= gD.deg() or not gC.mod(gD).is_zero():
                                continue
                            if 2 * (n - gC.deg()) - n <= 0:
                                continue
                            # dual-containment via the verified criterion
                            okC = _dual_containing(F, n, lam, gC, k)
                            okD = _dual_containing(F, n, lam, gD, k)
                            if not (okC and okD):
                                continue
                            for (al, ar) in [(0, 0), (1, 1), (2, 2), (3, 3), (5, 2)]:
                                if al >= n or ar >= n:
                                    continue
                                R = mechanism(F, n, lam, al, ar, gC, gD)
                                tested += 1
                                if not (all(R["flags"].values()) and R["tol_ok"]):
                                    fails += 1
                                    print(f"  FAIL q={q} n={n} lam={lam} k={k} deg f={R['deg_f']} "
                                          f"ord_f={R['ord_f']} ({al},{ar}) {R}")
    print(f"  -> {tested} configurations: {fails} failures")


def _dual_containing(F, n, lam, g, k, exhaustive=False):
    """verified criterion: C^{perp_sigma} subseteq C  <=>  h^tau in <g>_R(lambda)."""
    if g.deg() == 0:
        return True
    C = code_basis(F, g, n, lam)
    if exhaustive:
        D = sigma_dual_basis(F, C, n, k)
        return all(in_span(F, C, v) for v in D)
    h = xnf(F, n, lam).divmod_(g)[0]
    ht = sigma_reciprocal(F, h, k)
    vh = [F.zero] * n
    for i, c in enumerate(ht.c):
        vh[i] = c
    return in_span(F, C, vh)


def flagship():
    print("=" * 100)
    print("FLAGSHIP EXAMPLE  q = 4, n = 7, lambda = omega (ord 3), k = 1 (Hermitian twist)")
    print("=" * 100)
    F = GF(2, 2, [1, 1, 1])
    om = [a for a in F.nonzero() if F.order(a) == 3][0]
    n, k, lam = 7, 1, om
    ds = divs(F, n, lam)
    best = None
    for gC in ds:
        if gC.deg() == 0 or gC.deg() >= n:
            continue
        if _dual_containing(F, n, lam, gC, k):
            d = ord_of_poly(F, gC)
            if best is None or d > best[0]:
                best = (d, gC)
    print(f"  best dual-containing C = <f> with deg f = {best[1].deg()}, ord_f(x) = {best[0]}")
    gD = const(F, F.one)                       # D = R_lambda (whole space)
    print(f"  chain: C = <f> subset D = R_lambda ; quantum dimension 2(7-{best[1].deg()}) - 7 "
          f"= {2*(n-best[1].deg())-n}")
    for (al, ar) in [(0, 0), (1, 1), (3, 3), (5, 5), (10, 10), (9, 11)]:
        if al + ar >= best[0]:
            continue
        R = mechanism(F, n, lam, al, ar, best[1], gD, verbose=True)
        L = n + al + ar
        print(f"  (a_l,a_r)=({al},{ar}): T = {al+ar:2d}, code length L = {L:2d}, "
              f"flags={R['flags']} distinct={R['distinct']} tol_ok={R['tol_ok']} "
              f"-> T/L = {(al+ar)/L:.3f}")
    print(f"  NOTE: for cyclic QSCs T < n = L - T, i.e. T < L/2 always.  Here T/L can exceed 1/2.")


if __name__ == "__main__":
    sweep()
    flagship()
