"""
fflib3.py -- distinct-degree factorisation over small finite fields.

fast_factor(F, g) -> list of monic irreducible factors of the square-free monic
polynomial g over F_q (q small).  Used to enumerate all monic divisors quickly.
"""
from fflib import GF, Poly, xpoly, const


def _powmod(F, base, e, mod):
    res = const(F, F.one)
    b = base.mod(mod)
    while e:
        if e & 1:
            res = res.mul(b).mod(mod)
        b = b.mul(b).mod(mod)
        e >>= 1
    return res


def _gcd(F, a, b):
    a, b = Poly(F, a.c), Poly(F, b.c)
    while not b.is_zero():
        a, b = b, a.mod(b)
    return a.monic() if not a.is_zero() else a


def ddf(F, g):
    """distinct-degree factorisation: returns list of (d, h_d) where h_d is the
    product of all monic irreducible factors of g of degree d."""
    out = []
    h = Poly(F, g.c).monic()
    d = 1
    x = xpoly(F)
    while h.deg() >= 2 * d:
        # x^{q^d} - x  mod h
        t = _powmod(F, x, F.q ** d, h)
        hd = _gcd(F, t.sub(x), h)
        if hd.deg() > 0:
            out.append((d, hd))
            h = h.divmod_(hd)[0]
        d += 1
    if h.deg() > 0:
        out.append((h.deg(), h))
    return out


def edf(F, hd, d):
    """split the product hd of distinct irreducible factors of degree d into
    the factors themselves (brute force over monic polynomials of degree d)."""
    from itertools import product
    facs = []
    rest = Poly(F, hd.c)
    from fflib2 import is_irreducible
    known = []
    n_tried = 0
    while rest.deg() > 0:
        found = False
        for coeffs in product(F.elements(), repeat=d):
            cand = list(coeffs) + [F.one]
            h = Poly(F, cand)
            if h.deg() != d:
                continue
            if not is_irreducible(F, h, known):
                continue
            known.append(h)
            if rest.mod(h).is_zero():
                facs.append(h)
                while rest.mod(h).is_zero():
                    rest = rest.divmod_(h)[0]
                found = True
                break
        if not found:
            raise RuntimeError("edf failed")
    return facs


def factor_fast(F, g):
    facs = []
    for d, hd in ddf(F, g):
        if hd.deg() == d and _is_irr_deg(F, hd, d):
            facs.append(hd)
        else:
            facs.extend(edf(F, hd, d))
    return facs


def _is_irr_deg(F, h, d):
    if h.deg() != d:
        return False
    if h.deg() == 1:
        return True
    return len(ddf(F, h)) == 1 and ddf(F, h)[0][1].deg() == d


def divisors_fast(F, g):
    facs = factor_fast(F, g)
    divs = [const(F, F.one)]
    for h in facs:
        divs = divs + [d.mul(h).monic() for d in divs]
    out = []
    for d in divs:
        if d not in out:
            out.append(d)
    out.sort(key=lambda p: p.deg())
    return out, facs
