"""
verify_core.py -- verification of the mathematical core of the blueprint.

 (A) ADMISSIBILITY:  lambda^(p^k+1) = 1   <=>  every lambda-constacyclic code
     C = <g> of length n over F_q satisfies C^{perp_sigma} subseteq C,
     where the sigma-Galois dual uses sigma = Frobenius^k.
 (B) ORDER STRUCTURE: for every monic divisor f | x^n - lambda,
     ord_f(x) = r*h  with h | n,  r = ord(lambda),  gcd(r, n/h) = 1.
 (C) TOLERANCE MECHANISM (the lambda-twisted padding):
     block B(v) = ( lambda*tail_{a_l}(v), v, lambda^{-1}*head_{a_r}(v) );
     for every a in [-a_l, a_r]:
        (i)  the middle n-window  W(a,B) = mu * tau_lambda^s(v),
        (ii) W(a,B) in D  whenever v in D,
        (iii) the sync syndrome (quotient by g_D in R_lambda, then mod f)
              equals x^{-a} mod f,
        (iv) syndromes pairwise distinct  <=>  a_l + a_r < ord_f(x).
"""
import math, time, sys
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

DIV_CACHE = {}


def xnf(F, n, lam):
    return Poly(F, [F.neg(lam)] + [F.zero] * (n - 1) + [F.one])


def divisors(F, n, lam):
    key = (F.q, n, tuple(lam))
    if key not in DIV_CACHE:
        DIV_CACHE[key] = divisors_fast(F, xnf(F, n, lam))[0]
    return DIV_CACHE[key]


def claim_A(verbose=True):
    print("=" * 78, flush=True)
    print("CLAIM (A): lam^(p^k+1)=1  <=>  every lam-constacyclic code is sigma-dual-containing")
    print("=" * 78, flush=True)
    tested = fails = 0
    for q, F in FIELDS.items():
        ks = range(F.e) if F.e > 1 else [0]
        for n in range(2, 8):
            if n % F.p == 0:
                continue
            for lam in F.nonzero():
                divs = divisors(F, n, lam)
                for k in ks:
                    adm = (F.pow(lam, F.p ** k + 1) == F.one)
                    for g in divs:
                        if g.deg() == 0:
                            continue
                        basis = code_basis(F, g, n, lam)
                        dual = sigma_dual_basis(F, basis, n, k)
                        contained = all(in_span(F, basis, v) for v in dual)
                        tested += 1
                        if contained != adm:
                            fails += 1
                            print(f"  FAIL q={q} n={n} lam={lam} k={k} deg g={g.deg()} "
                                  f"adm={adm} contained={contained}", flush=True)
    print(f"  -> {tested} lambda-constacyclic codes tested, {fails} counterexamples", flush=True)
    return fails


def claim_B():
    print("=" * 78, flush=True)
    print("CLAIM (B): ord_f(x) = r*h, h|n, r=ord(lam), gcd(r,n/h)=1")
    print("=" * 78, flush=True)
    tested = fails = 0
    for q, F in FIELDS.items():
        for n in range(2, 10):
            if n % F.p == 0:
                continue
            for lam in F.nonzero():
                r = F.order(lam)
                for h in divisors(F, n, lam):
                    if h.deg() == 0:
                        continue
                    d = ord_of_poly(F, h)
                    tested += 1
                    errs = []
                    if (n * r) % d:
                        errs.append("d|n*r fails")
                    elif d % r:
                        errs.append("r|d fails")
                    elif n % (d // r):
                        errs.append("(d/r)|n fails")
                    elif math.gcd(r, n // (d // r)) != 1:
                        errs.append("gcd(r,n/(d/r))=1 fails")
                    if errs:
                        fails += 1
                        print(f"  FAIL q={q} n={n} lam={lam} r={r} f={h.c} d={d} {errs}", flush=True)
    print(f"  -> {tested} divisors tested, {fails} violations", flush=True)
    return fails


def inv_in_R(F, n, lam, g):
    """inverse of the polynomial g in R_lambda (g must be coprime to x^n - lambda)."""
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
    assert len(old_r) == 1, "gcd(g, x^n-lam) != 1"
    return Poly(F, old_s).divmod_(xr)[1]


def tau_pow(F, v, lam, s):
    n = len(v)
    res = v[:]
    for _ in range(s % n):
        res = [F.mul(lam, res[-1])] + res[:-1]
    return res


def check_config(F, n, lam, al, ar, gC, gD, verbose=False):
    """returns dict with the four mechanism assertions."""
    xr = xnf(F, n, lam)
    assert xr.mod(gD).is_zero() and gC.mod(gD).is_zero()
    f = gC.divmod_(gD)[0]
    dord = ord_of_poly(F, f)
    ginv = inv_in_R(F, n, lam, gD)
    Dbasis = code_basis(F, gD, n, lam)
    Cbasis = code_basis(F, gC, n, lam)
    gvec = [F.zero] * n
    for i, c in enumerate(gD.c):
        gvec[i] = c
    contents = [[F.add(x, y) for x, y in zip(c, gvec)] for c in Cbasis] + [gvec]
    out = dict(shift=True, inD=True, syndrome=True, distinct=False, ord_f=dord,
               dim_quantum=2 * (n - gC.deg()) - n, deg_f=f.deg(), n=n, q=F.q, lam=lam)
    syn = {}
    for a in range(-al, ar + 1):
        for v in contents:
            B = ([F.mul(lam, v[n - al + j]) for j in range(al)] + v +
                 [F.mul(F.inv(lam), v[j]) for j in range(ar)])
            W = B[al + a: al + a + n]
            if not in_span(F, Dbasis, W):
                out["inD"] = False
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
                out["shift"] = False
            J = Poly(F, list(W)).mul(ginv).divmod_(xr)[1]
            s_poly = J.mod(f)
            exp = xpow_mod(F, (-a) % dord, f)
            if not (s_poly == exp):
                out["syndrome"] = False
                if verbose:
                    print(f"     a={a} syn={s_poly} exp={exp}")
            syn[a] = tuple(map(tuple, s_poly.c))
    out["distinct"] = (len(set(syn.values())) == al + ar + 1)
    out["tolerance_ok"] = (out["distinct"] == (al + ar < dord))
    return out


def claim_C(maxn=8, shifts=((1, 1), (2, 1), (2, 2), (3, 2))):
    print("=" * 78, flush=True)
    print("CLAIM (C): lambda-twisted padding, window shift, syndrome, exact tolerance")
    print("=" * 78, flush=True)
    cfg = fails = 0
    for q, F in FIELDS.items():
        for n in range(3, maxn + 1):
            if n % F.p == 0:
                continue
            for lam in F.nonzero():
                divs = [d for d in divisors(F, n, lam) if d.deg() <= n // 2]
                for gD in divs:
                    for gC in divs:
                        if gC.deg() <= gD.deg() or not gC.mod(gD).is_zero():
                            continue
                        if 2 * (n - gC.deg()) - n <= 0:
                            continue
                        for (al, ar) in shifts:
                            cfg += 1
                            R = check_config(F, n, lam, al, ar, gC, gD)
                            if not (R["shift"] and R["inD"] and R["syndrome"]
                                    and R["tolerance_ok"]) or R["dim_quantum"] <= 0:
                                fails += 1
                                print(f"  FAIL q={q} n={n} lam={lam} deg f={R['deg_f']} "
                                      f"ord_f={R['ord_f']} a=({al},{ar}) {R}", flush=True)
    print(f"  -> {cfg} configurations tested, {fails} failures", flush=True)
    return fails


if __name__ == "__main__":
    t0 = time.time()
    fA = claim_A()
    fB = claim_B()
    fC = claim_C()
    print(f"\nTOTAL: claim A fails={fA}, B fails={fB}, C fails={fC}  "
          f"({time.time()-t0:.1f}s)", flush=True)
