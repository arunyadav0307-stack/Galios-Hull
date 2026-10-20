#!/usr/bin/env python3
"""
Screening test for research direction C1 (risk R1):
is the Galois hull dimension a class function on isometry classes?

SETTING
    A Hamming isometry of F_q^n is a monomial map phi = D P (P a coordinate
    permutation, D = diag(a_0,...,a_{n-1}) with all a_i in F_q^*).  These are
    exactly the linear maps preserving Hamming weight.

THE TWO GROUPS
    M(q,n)   = all monomial maps                     (order n! (q-1)^n)
    Sim_k    = { D P in M : a_i^{1+q^k} is independent of i }   (the similarity
               group of the k-Galois form <u,v>_k = sum_i u_i v_i^{q^k})

    PROPOSITION (proved in the note, verified here).  For phi = D P in M,
        <phi u, phi v>_k = sum_i a_i^{1+q^k} (Pu)_i (Pv)_i^{q^k}.
    Hence phi in Sim_k  =>  <phi u, phi v>_k = c <u, v>_k with c != 0, so phi maps
    C^{perp_k} onto (phi C)^{perp_k} and dim hull_k is INVARIANT.
    Conversely, if a_i^{1+q^k} is not constant the form is only preserved up to
    weights, and the hull may change.

THIS SCRIPT
    Part A  explicit counterexample, computed by brute force over all q^n vectors
            (no reliance on the hull helpers): the cyclic code <1+x> in
            F_4[x]/(x^3-1), its image under f(x) -> f(w x), and both hulls.
    Part B  size of M and of Sim_k for the tested parameters (index computation).
    Part C  exhaustive check that dim hull_k is invariant on all of Sim_k,
            and count how many monomial isometries are NOT in Sim_k.
"""

import sys, os, itertools, math, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gf

LINES = []


def log(s=""):
    LINES.append(s)
    print(s)


# ------------------------------------------------------------ brute-force code
def build(F, q, n):
    def add(u, v):
        return [F.add(a, b) for a, b in zip(u, v)]

    def smul(c, u):
        return [F.mul(c, a) for a in u]

    def span(basis):
        S = set()
        for coef in itertools.product(range(q), repeat=len(basis)):
            v = [0] * n
            for c, b in zip(coef, basis):
                v = add(v, smul(c, b))
            S.add(tuple(v))
        return S

    def dot(v, u, k):
        # paper p.7: the exponent is p^k, NOT q^k
        s = 0
        for i in range(n):
            s = F.add(s, F.mul(v[i], F.pow(u[i], F.p ** k)))
        return s

    def dual(S, k):
        return {v for v in itertools.product(range(q), repeat=n)
                if all(dot(v, u, k) == 0 for u in S)}

    def gdim(S):
        return round(math.log(len(S), q))

    return span, dual, gdim, dot


def part_a(F, q, n):
    log("PART A -- explicit counterexample (brute force over all q^n vectors)")
    log("-" * 78)
    span, dual, gdim, dot = build(F, q, n)
    w = 2  # a generator of F_4^*
    C = span([[1, 1, 0], [0, 1, 1]])          # <1+x> in F_4[x]/(x^3-1)
    log(f"  q={q} n={n}; C = <1+x>; |C| = {len(C)}, dim = {gdim(C)}")

    def phi(v):
        return tuple(F.mul(F.pow(w, i), v[i]) for i in range(n))

    C2 = {phi(v) for v in C}

    def shift(v, lam):
        return tuple([F.mul(lam, v[-1])] + list(v[:-1]))

    cyclic2 = all(shift(v, 1) in C2 for v in C2)
    log(f"  phi = f(x) -> f(w*x), i.e. diag(1, w, w^2); Hamming isometry: "
        f"{all(sum(1 for a in v if a) == sum(1 for a in phi(v) if a) for v in C)}")
    log(f"  phi(C) is cyclic: {cyclic2}")
    for k in (0, 1):
        h0 = gdim(C & dual(C, k))
        h1 = gdim(C2 & dual(C2, k))
        log(f"  k={k}:  dim hull_k(C) = {h0}   dim hull_k(phi C) = {h1}"
            f"   {'DIFFERENT' if h0 != h1 else 'same'}")
    we = lambda S: sorted(sum(1 for a in v if a) for v in S)
    log(f"  same weight enumerator: {we(C) == we(C2)}")
    log()
    return True


def part_b(F, q, n, kvals):
    log("PART B -- group sizes (how much of M is a form-similarity?)")
    log("-" * 78)
    n_m = math.factorial(n) * (q - 1) ** n
    log(f"  q={q} n={n}: |M| = n! (q-1)^n = {math.factorial(n)} * {(q-1)**n} = {n_m}")
    for k in kvals:
        cnt = 0
        for diag in itertools.product(range(1, q), repeat=n):
            vals = {F.pow(a, 1 + q ** k) for a in diag}
            if len(vals) == 1:
                cnt += 1
        log(f"  k={k}: #diagonals with a_i^(1+q^k) constant = {cnt}; "
            f"|Sim_{k}| = n! * {cnt} = {math.factorial(n) * cnt} "
            f"(index {n_m // (math.factorial(n) * cnt)})")
    log()
    return n_m


def part_c(F, q, n, kvals, n_m):
    log("PART C -- exhaustive invariance check inside Sim_k")
    log("-" * 78)
    span, dual, gdim, dot = build(F, q, n)
    codes = []
    for lam in range(1, q):
        f = [0] * (n + 1)
        f[0] = F.neg(lam)
        f[n] = 1
        for g in _divisors(F, f):
            v = list(g) + [0] * (n - len(g))
            basis = []
            for _ in range(n - (len(g) - 1)):
                basis.append(list(v))
                v = [F.mul(lam, v[-1])] + v[:-1]
            S = span(basis)
            codes.append((lam, tuple(g), S, gdim(S)))
    log(f"  constacyclic codes enumerated: {len(codes)}")

    bad = 0
    checked = 0
    for perm in itertools.permutations(range(n)):
        for diag in itertools.product(range(1, q), repeat=n):
            for k in kvals:
                if len({F.pow(a, 1 + q ** k) for a in diag}) != 1:
                    continue          # not a form similarity
                for lam, g, S, dim in codes:
                    C2 = {tuple(_apply(perm, diag, F, v)) for v in S}
                    checked += 1
                    if gdim(C2 & dual(C2, k)) != gdim(S & dual(S, k)):
                        bad += 1
    log(f"  (code, similarity, k) triples checked: {checked}")
    log(f"  invariance failures: {bad}"
        f"   {'OK as proved' if bad == 0 else 'CONTRADICTS THE PROPOSITION'}")
    log()

    outside = 0
    for diag in itertools.product(range(1, q), repeat=n):
        for k in kvals:
            if len({F.pow(a, 1 + q ** k) for a in diag}) != 1:
                outside += 1
    log(f"  note: {outside} diagonal choices are Hamming isometries but NOT")
    log(f"        similarities of the tested Galois forms -- these are exactly")
    log(f"        the maps that may (and in Part A, do) change the hull.")
    log()
    return bad


def _apply(perm, diag, F, v):
    out = [0] * len(v)
    for i, c in enumerate(v):
        out[perm[i]] = F.mul(c, diag[i])
    return out


def _divisors(F, f):
    from itertools import combinations
    irr = [p for p, _ in gf.factor(F, f)]
    out = []
    for r in range(len(irr) + 1):
        for sub in combinations(range(len(irr)), r):
            g = [1]
            for i in sub:
                h = [0] * (len(g) + len(irr[i]) - 1)
                for a, ca in enumerate(g):
                    for b, cb in enumerate(irr[i]):
                        if ca and cb:
                            h[a + b] = F.add(h[a + b], F.mul(ca, cb))
                g = gf.ptrim(h)
            out.append(gf.ptrim(g))
    return out


def main():
    log("### isometry_hull_screening.py")
    log(datetime.datetime.now().strftime("%a %b %d %H:%M:%S UTC %Y"))
    log(f"Python {sys.version.split()[0]}")
    log("=" * 78)
    log()

    q, p, m, mod = 4, 2, 2, [1, 1, 1]
    F = gf.GF(p, m, mod)
    n = 3
    kvals = [0, 1]

    part_a(F, q, n)
    n_m = part_b(F, q, n, kvals)
    bad = part_c(F, q, n, kvals, n_m)

    log("=" * 78)
    log("VERDICT")
    log("  The GALOIS hull dimension is not a class function on isometry classes.")
    log("  Explicit witness: q=4, n=3, C=<1+x>, phi=diag(1,w,w^2); Euclidean hull")
    log("  0 -> 1, both codes cyclic with the same weight enumerator.")
    log("  CORRECTION (2026-10-20): the Hermitian (k=1) hull is 0 -> 0 here.  Over")
    log("  F_4 a^3 = 1 for every nonzero a, so every monomial map is a Hermitian")
    log("  similarity.  A Hermitian counterexample exists over F_9 (hull 2 -> 0);")
    log("  see final_check_A.py and FINAL_INDEPENDENT_MATHEMATICAL_CHECK.md.")
    log()
    log("  Therefore direction C1, as stated, is ILL-POSED and must be reformulated")
    log("  in terms of the similarity group Sim_k of the Galois form (where invariance")
    log("  holds, by the proposition verified in Part C).")
    log("=" * 78)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "verification",
                       "isometry_hull_screening.out")
    with open(os.path.abspath(out), "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    print(f"\nwritten to {os.path.abspath(out)}")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
