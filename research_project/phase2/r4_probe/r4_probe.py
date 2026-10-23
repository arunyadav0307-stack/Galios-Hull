"""
R4 feasibility probe: does the Gray distance factor over the CRT components?

The question R4 would ask: count lambda-constacyclic codes over R_e with C^perp_H <= C by
their QUANTUM parameters [[en, 2k-en, >=d]], i.e. by (hull dimension, Gray distance).
Every other count in this project collapsed because the quantity was a sum over the CRT
components.  The point of this probe is to test whether the Gray distance behaves the same
way -- and it does NOT, for a structural reason that is checked here, not assumed.

Definitions taken from the source paper (verified text, pages 5-7 and 15):

  R_e = F_{q^2}[u]/(u^e - 1),  r_i = sum_k eta_k s_{ki},   {eta_k} the paper's basis
  psi(r_0..r_{n-1}) = [ (s_10..s_e0)M, ..., (s_1,n-1..s_e,n-1)M ]   in F_{q^2}^{en}
  M M^* = nu I_e,   psi(C^perp_H) = psi(C)^perp_H

so the Gray weight of a codeword is a sum over POSITIONS of a joint function of all e
component symbols at that position.  It is not the sum of the component Hamming weights.

For e = 2 with M = [[1,1],[1,-1]] (the paper's matrix for e=2) and s_k = alpha-coordinate/2:

  psi(c) = ( a+b , a-b )   over F_{q^2},   weight = w(a+b) + w(a-b)

with a in C_1, b in C_2 the two component codewords.  Hence

  w = 1  <=>  a = b = c*e_i for some position i, c != 0

i.e. a weight-1 Gray word exists exactly when C_1 and C_2 share a weight-1 word.  The Gray
distance therefore depends on C_1 INTERSECT C_2, which is a joint invariant of the pair and
not a function of (d(C_1), d(C_2)).

TEST: group all (C_1, C_2) pairs by the quadruple (k_1, d_1, k_2, d_2) and check whether the
Gray distance is constant on each group.  If it is not, no product law can reproduce the
quantum-parameter distribution, and R4 has content that R1/R2/R3 do not.

ASCII only, stdlib only.
"""
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "r3_probe"))
sys.path.insert(0, os.path.join(HERE, "..", "r1_probe"))
from r1_probe import make_field, Pol, divisors, code_from_generator, hull_dim   # noqa: E402
from r3_probe import field_is_dc                                               # noqa: E402


def words(F, basis, n):
    """All codewords of the span of `basis` (rows of length n), as tuples."""
    out = []
    k = len(basis)
    if k == 0:
        return [tuple([F.zero] * n)]
    for coeffs in itertools.product(range(F.Q), repeat=k):
        v = [F.zero] * n
        for c, row in zip(coeffs, basis):
            if c:
                for i in range(n):
                    v[i] = F.add[v[i]][F.mul[c][row[i]]]
        out.append(tuple(v))
    return out


def wts(F, v):
    return sum(1 for x in v if x != F.zero)


def gray_dist(F, C1, C2, n, M=((1, 1), (1, -1))):
    """min over (a,b) != (0,0) of w(component 1 of (s1,s2)M) + w(component 2).

    (s1, s2) are the eta-basis coordinates; for e=2 they are (a,b)/2 up to a global
    scalar, which does not affect the weight.  M entries are integers reduced mod p.
    """
    m11, m12 = M[0]
    m21, m22 = M[1]
    m11, m12 = m11 % F.p, m12 % F.p
    m21, m22 = m21 % F.p, m22 % F.p

    def enc(c):
        return F.enc[tuple((c // F.p ** i) % F.p for i in range(F.deg))]

    m11, m12, m21, m22 = enc(m11), enc(m12), enc(m21), enc(m22)

    def lin(u, v, m1, m2):
        return F.add[F.mul[m1][u]][F.mul[m2][v]]

    best = None
    W1 = words(F, C1, n)
    W2 = words(F, C2, n)
    for a in W1:
        for b in W2:
            if all(x == F.zero for x in a) and all(x == F.zero for x in b):
                continue
            s = 0
            for i in range(n):
                if lin(a[i], b[i], m11, m12) != F.zero:
                    s += 1
                if lin(a[i], b[i], m21, m22) != F.zero:
                    s += 1
            if best is None or s < best:
                best = s
                if best == 1:
                    return 1
    return best


def matrix_check(F, M):
    """Numerically verify M M* = nu I_e for the Hermitian transpose, return (ok, nu)."""
    def elt(c):
        c %= F.p
        return F.enc[tuple((c // F.p ** i) % F.p for i in range(F.deg))]
    Me = [[elt(c) for c in row] for row in M]
    e = len(M)
    # Hermitian transpose: (M*)[i][j] = conj(M[j][i]) = M[j][i]^q
    Ms = [[F.pow(Me[j][i], F.p if F.deg == 2 else 1) for j in range(e)] for i in range(e)]
    P = [[None] * e for _ in range(e)]
    for i in range(e):
        for k in range(e):
            acc = F.zero
            for j in range(e):
                acc = F.add[acc][F.mul[Me[i][j]][Ms[j][k]]]
            P[i][k] = acc
    diag = [P[i][i] for i in range(e)]
    nu = diag[0]
    ok = all(d == nu for d in diag) and all(P[i][k] == F.zero for i in range(e) for k in range(e) if i != k) and nu != F.zero
    return ok, nu


def check_matrix(F, M=((1, 1), (1, -1))):
    """MM* = nu I: for M = [[1,1],[1,-1]] we get nu = 2, which must be nonzero in F."""
    nu = F.add[F.one][F.one]
    ok = (nu != F.zero)
    print(f"  matrix check: M=[[1,1],[1,-1]], MM* = nu I with nu = {nu}"
          f"  -> admissible: {ok}")
    if not ok:
        print(f"     q={F.p} even: nu = 0, so M does not satisfy the paper's hypothesis")
        print(f"     nu in F*_{F.Q}. The Gray map degenerates (psi is not injective);")
        print(f"     a different M would be needed. Probe skipped for this field.")
    return ok


def run(p, q, n):
    F = make_field(p, q)
    print("=" * 78)
    print(f"e=2, q={q}, n={n}, F_{F.Q}, M=[[1,1],[1,-1]]")
    if not check_matrix(F):
        return None
    # field-level codes for every multiplier
    field = {}
    for alpha in range(1, F.Q):
        cs = []
        for g in divisors(F, n, alpha):
            b = code_from_generator(F, g, n, alpha)
            d = None
            for w in words(F, b, n):
                if any(x != F.zero for x in w):
                    ww = wts(F, w)
                    d = ww if d is None else min(d, ww)
            cs.append((alpha, g, b, len(b), d))
        field[alpha] = cs
    print("  field-level codes (alpha, k, d):")
    for alpha in sorted(field):
        print(f"    alpha={alpha}: " + ", ".join(f"({k},{d})" for (_, _, _, k, d) in field[alpha]))

    # all pairs -> Gray distance, grouped by the component invariants
    groups = {}
    dc_pairs = 0
    examples = []
    for a1 in sorted(field):
        for a2 in sorted(field):
            for (_, g1, b1, k1, d1) in field[a1]:
                for (_, g2, b2, k2, d2) in field[a2]:
                    dg = gray_dist(F, b1, b2, n)
                    key = (k1, d1, k2, d2)
                    groups.setdefault(key, set()).add(dg)
                    dc = field_is_dc(F, b1, n) and field_is_dc(F, b2, n)
                    if dc:
                        dc_pairs += 1
                        examples.append((a1, a2, g1, g2, k1 + k2, dg))
    print(f"  {len(groups)} distinct component-invariant groups (k1,d1,k2,d2)")
    bad = {k: v for k, v in groups.items() if len(v) > 1}
    print(f"  groups on which the Gray distance is NOT determined by (k1,d1,k2,d2): {len(bad)}")
    for k in sorted(bad):
        print(f"      (k1,d1,k2,d2)={k} -> Gray distances {sorted(bad[k])}")
    if bad:
        print("  => the Gray distance is NOT a function of the component data alone")
        print("     (so no product over components can reproduce the quantum-parameter count)")
    else:
        print("  => the Gray distance IS a function of the component data alone in this case")
    print(f"  dual-containing pairs: {dc_pairs}; distinct quantum parameters "
          f"(k1+k2, d): {sorted({(k, d) for (_, _, _, _, k, d) in examples})}")
    return bad


if __name__ == "__main__":
    run(3, 3, 2)
    print()
    print("=" * 78)
    print("the same instance with a SECOND admissible matrix M2 = [[1,1],[t,-t]],")
    print("t = 2 in F_9 (norm 1, so M2 M2* = 2 I).  The paper leaves M free subject to")
    print("MM* = nu I, so this tests whether the parameters depend on that choice.")
    F = make_field(3, 3)
    for M in (((1, 1), (1, -1)), ((1, 1), (2, -2))):
        ok, nu = matrix_check(F, M)
        print(f"  M={M}:  MM* = nu I with nu={nu}, admissible={ok}")
    C = [code_from_generator(F, g, 2, 1) for g in divisors(F, 2, 1)]
    diffs = 0
    for i, b1 in enumerate(C):
        for j, b2 in enumerate(C):
            d1 = gray_dist(F, b1, b2, 2, ((1, 1), (1, -1)))
            d2 = gray_dist(F, b1, b2, 2, ((1, 1), (2, -2)))
            if d1 != d2:
                diffs += 1
                print(f"    alpha=1 codes ({i},{j}): M -> d={d1},  M2 -> d={d2}   DIFFERS")
    print(f"  pairs of alpha=1 codes whose Gray distance depends on the choice of M: "
          f"{diffs}/{len(C) ** 2}")
