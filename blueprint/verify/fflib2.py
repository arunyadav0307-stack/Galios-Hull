"""
fflib2.py -- divisor enumeration by factorisation (fast enough for the sweep),
plus helpers reused by the verification scripts.
"""
from itertools import product, combinations
from fflib import GF, Poly, xpoly, const, vec_scale, vec_add, mat_rank


def is_irreducible(F, h, known_irreducibles):
    """h monic, deg h >= 1; test using the list of irreducibles of smaller degree."""
    d = h.deg()
    if d == 1:
        return True
    if any((h.eval(a)).__eq__(F.zero) for a in F.elements()):
        return False  # has a linear factor
    for ir in known_irreducibles:
        if ir.deg() * 2 > d:
            break
        if h.mod(ir).is_zero():
            return False
    return True


def factorise(F, g, cap_deg=None):
    """monic square-free-ish factorisation of the monic polynomial g over F_q.
    Returns list of monic irreducible factors (distinct, assuming square-free)."""
    rest = Poly(F, g.c)
    facs = []
    known = []          # irreducibles found so far, increasing degree
    d = 1
    while rest.deg() >= 2 * d and rest.deg() > 0:
        for coeffs in product(F.elements(), repeat=d):
            cand = list(coeffs) + [F.one]
            h = Poly(F, cand)
            if h.deg() != d:
                continue
            if h in known:
                continue
            if not is_irreducible(F, h, known):
                continue
            known.append(h)
            if rest.mod(h).is_zero():
                facs.append(h)
                while rest.mod(h).is_zero():
                    rest = rest.divmod_(h)[0]
        d += 1
    if rest.deg() >= 1:
        # remaining part: irreducible of degree >= rest.deg()/2+... just append
        # (find its irreducible factors among degree <= deg(rest)//2 first)
        for coeffs in product(F.elements(), repeat=rest.deg() // 2) if rest.deg() // 2 > 0 else []:
            pass
        facs.append(rest)
    return facs


def all_monic_divisors(F, g):
    """all monic divisors of g from its factorisation (assumes square-free)."""
    facs = factorise(F, g)
    divs = [const(F, F.one)]
    for h in facs:
        divs = divs + [d.mul(h).monic() for d in divs]
    # dedupe
    out = []
    for d in divs:
        if d not in out:
            out.append(d)
    out.sort(key=lambda p: p.deg())
    return out


def code_basis(F, gen, n, lam):
    """basis (as vectors in F_q^n) of the lambda-constacyclic code <gen>."""
    basis = []
    for j in range(n - gen.deg()):
        v = [F.zero] * n
        for i, c in enumerate(gen.c):
            idx = (i + j) % n
            v[idx] = F.add(v[idx], F.mul(c, F.pow(lam, (i + j) // n)))
        basis.append(v)
    return basis


def sigma_dual_basis(F, basis, n, k):
    from fflib import nullspace
    rows = [[F.pow(u[i], F.p ** k) for i in range(n)] for u in basis]
    return nullspace(F, rows, n)


def spans_equal(F, A, B):
    from fflib import in_span
    RA = mat_rank(F, A)
    return mat_rank(F, A + B) == RA and all(in_span(F, A, b) for b in B) and \
        all(in_span(F, B, a) for a in A)
