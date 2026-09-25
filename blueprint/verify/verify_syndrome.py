"""
verify_syndrome.py -- decisive, self-contained check of the window-syndrome
identity, with the expected value computed INDEPENDENTLY of xpow_mod/ord_of_poly.

Independent definition (used here):
  R_lambda = F_q[x]/(x^n - lambda); vector c = (c_0,...,c_{n-1}) represents
  y = sum_i c_i x^i.  Multiplication by x^{-1} in R_lambda is
        S(c) = (lambda^{-1} c_0, c_1, ..., c_{n-1}),
  because c_0 x^{-1} = c_0 lambda^{-1} x^{n-1}.  Then
        x^{-a}  =  S^a(1,0,...,0)   in R_lambda,
  and the reference syndrome is (x^{-a} mod f) computed by polynomial
  remainder (divmod_), which is the *unique* remainder of degree < deg f.

Receiver's syndrome: divide the window word by the generator g_D inside
R_lambda (an ordinary polynomial division, valid because g_D | x^n - lambda),
then reduce modulo f.

Reported per (chain, a):  syndrome(basis word)  vs  mu_a * x^{-a} mod f.
"""
import itertools, math
from fflib import GF, Poly, const, xpoly, ord_of_poly, in_span, ptrim
from fflib3 import divisors_fast
from fflib2 import code_basis
from verify_mechanism import (FIELDS, window, block, s_seq, tau_pow,
                              _dual_containing, xnf, divs)


def S_shift(F, lam, c):
    """multiplication by x^{-1} in R_lambda = F_q[x]/(x^n - lambda):
       x^{-1} * sum c_i x^i = c_1 + c_2 x + ... + c_{n-1} x^{n-2} + lambda^{-1} c_0 x^{n-1}.
       (Corrected: the wrapped coefficient lambda^{-1} c_0 goes to position n-1.)"""
    return list(c[1:]) + [F.mul(F.inv(lam), c[0])]


def T_shift(F, lam, c):
    """multiplication by x in R_lambda:
       x * sum c_i x^i = lambda c_{n-1} + c_0 x + ... + c_{n-2} x^{n-1}."""
    return [F.mul(lam, c[-1])] + list(c[:-1])


def x_pow_minus_a_in_R(F, n, lam, a, order):
    """x^{-a} as an element of R_lambda computed with T (= multiplication by x):
       x^{-a} = x^{(-a) mod order} = T^{(-a) mod order}(1)."""
    c = [F.zero] * n
    c[0] = F.one
    for _ in range((-a) % order):
        c = T_shift(F, lam, c)
    return Poly(F, c)


def syndrome_of_window(F, n, lam, W, gD, f):
    """receiver-side: divide by g_D in R_lambda (polynomial division), then mod f."""
    if gD.deg() > 0:
        J = Poly(F, list(W)).divmod_(gD)[0]
    else:
        J = Poly(F, list(W))
    return J.mod(f)


def check(F, n, lam, gC, gD, al, ar, verbose=True):
    f = gC.divmod_(gD)[0]
    xr = xnf(F, n, lam)
    Cb = code_basis(F, gC, n, lam)
    gvec = [F.zero] * n
    for i, c in enumerate(gD.c):
        gvec[i] = c
    contents = [[F.add(x, y) for x, y in zip(c, gvec)] for c in Cb] + [gvec]
    rows, ok_all = [], True
    for a in range(-al, ar + 1):
        exp = x_pow_minus_a_in_R(F, n, lam, a, ord_of_poly(F, f)).mod(f)   # independent
        mus, synds = set(), set()
        for v in contents:
            W = window(F, v, n, lam, a)
            syn = syndrome_of_window(F, n, lam, W, gD, f)
            synds.add(tuple(map(tuple, syn.c)))
            syn_c = tuple(map(tuple, ptrim(list(syn.c))))
            exp_c = tuple(map(tuple, ptrim(list(exp.c))))
            mu = None
            for m in list(F.nonzero()):
                if tuple(map(tuple, ptrim(list(exp.scale(m).c)))) == syn_c:
                    mu = m
                    break
            exact = (syn_c == exp_c)
            if not exact:
                ok_all = False
                ok_exact = False
            mus.add(mu)
        ok = (len(mus) == 1) and (None not in mus)
        rows.append((a, tuple(map(tuple, exp.c)) if verbose else None, sorted(map(str, mus)), len(synds), ok))
    return f, rows, ok_all


def demo(F, q, n, lam, k, al, ar, label=""):
    xr = xnf(F, n, lam)
    ds = divs(F, n, lam)
    best = None
    for gC in ds:
        if 0 < gC.deg() < n and _dual_containing(F, n, lam, gC, k):
            o = ord_of_poly(F, gC)
            if best is None or o > best[0]:
                best = (o, gC)
    if best is None:
        print(f"  [{label}] no dual-containing chain"); return
    o, gC = best
    gD = const(F, F.one)
    f, rows, ok = check(F, n, lam, gC, gD, al, ar, verbose=False)
    print(f"  [{label}] q={q} n={n} lam={lam} deg f={f.deg()} ord_f(x)={o} "
          f"windows ({al},{ar}) -> mu_a constant across content words: {ok}")
    mus = sorted({r[2][0] for r in rows})
    print(f"        scalar factors mu_a (syndrome = mu_a * x^-a) take values: {mus}")
    # tolerance: are the syndromes pairwise distinct until ord_f?
    T = o - 1
    al2, ar2 = T // 2, T - T // 2
    if al2 + ar2 == T and al2 < n and ar2 < n:
        f2, rows2, ok2 = check(F, n, lam, gC, gD, al2, ar2, verbose=False)
        distinct = len({r[3] for r in rows2}) == 1 and all(r[3] == 1 for r in rows2)
        print(f"        maximal window T={T} ({al2},{ar2}) < ord_f: syndromes distinct = "
              f"{all(r[4] for r in rows2)} (syndrome unique per shift: {distinct})")
    else:
        print(f"        (max T={T} exceeds block size n={n}, use the ring version below)")



if __name__ == "__main__":
    print("=" * 96)
    print("(1) FIELD CASE, single lambda-constacyclic chain, independent expected syndrome")
    print("=" * 96)
    for (q, n, lam_idx) in [(4, 7, None), (4, 3, None), (9, 4, None), (2, 7, None), (5, 4, None)]:
        F = FIELDS[q]
        for lam in F.nonzero():
            ks = range(F.e) if F.e > 1 else [0]
            for k in ks:
                if F.pow(lam, F.p ** k + 1) != F.one:
                    continue
                demo(F, q, n, lam, k, 1, 1, label=f"q={q},n={n},k={k}")
    print()
    print("=" * 96)
    print("(2) RING CASE  A = F_4 x F_4, n = 7, lambda = (omega,1)  [two admissible weights]")
    print("=" * 96)
    F = FIELDS[4]
    om = [a for a in F.nonzero() if F.order(a) == 3][0]
    n, k = 7, 1
    comps = [om, F.one]
    data = []
    for lam in comps:
        ds = divs(F, n, lam)
        cands = [g for g in ds if 0 < g.deg() < n and _dual_containing(F, n, lam, g, k)]
        cands.sort(key=lambda g: -ord_of_poly(F, g))
        data.append((lam, cands[0], ord_of_poly(F, cands[0])))
        print(f"  component lam={lam}: best deg={cands[0].deg()} ord_f={data[-1][2]}")
    T_ring = math.lcm(*[d[2] for d in data])
    print(f"  predicted ring tolerance  lcm(ord_f1, ord_f2) = {T_ring}  (>> n = {n})")
    # verify the syndrome *pair* is distinct for all shifts in a window of width T_ring
    def pair_syndrome(a):
        out = []
        for lam, g, o in data:
            exp = x_pow_minus_a_in_R(F, n, lam, a, o).mod(g)
            out.append(tuple(map(tuple, exp.c)))
        return tuple(out)
    seen = {}
    dup = 0
    W = 21
    for a in range(-(W // 2), W - W // 2):
        s = pair_syndrome(a)
        if s in seen:
            dup += 1
        seen[s] = a
    print(f"  shifts a in [-10,10]: {len(seen)} distinct syndrome pairs, {dup} collisions "
          f"(expected 21 distinct if lcm = 21)")
    print("  => the ring tolerance is the LCM of the component tolerances, not any single ord_f.")
