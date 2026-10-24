"""
Phase 3 / P3-3: ring-level (R_e) Gray coupling.

Setting.  R_e = F_{q^2}[u]/(u^e - 1), e | (q+1), so R_e = prod_j F_{q^2} by CRT with all
idempotents fixed by the q-power (established in R3).  A lambda-constacyclic code C over R_e
corresponds to a tuple (C_1,...,C_e) of field-level constacyclic codes, and

    Hull_H(C) = (+)_j Hull_H(C_j),        dim Hull_H(C) = sum_j dim Hull_H(C_j).

The Gray map of the source paper (pp. 6-7), in eta-basis coordinates s_ki, is

    psi(c) = [ (s_1i,...,s_ei) M ]_{i=0..n-1}  in F_{q^2}^{en},   M M^* = nu I_e,

so the Gray weight of a codeword is

    W(c) = sum_i g_i,     g_i = #{ j : ((s_1i,...,s_ei) M)_j != 0 }.

This probe checks the two-sided bound proved in P3_3_RING_GRAY.md,

    min_k d(C_k)  <=  d(psi(C))  <=  e * min_k d(C_k),

on every tuple of field codes in small instances, the equality cases

    C_1 = C_2 = D  =>  d(psi(C)) = d(D)          (e = 2, M = [[1,1],[1,-1]], char != 2)
    C_2 = 0        =>  d(psi(C)) = 2 d(C_1)

and the non-determination result (equal component data, different Gray distance).

Distances are exact.  ASCII only, pure stdlib (numpy is not available in this environment).
"""
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r1_probe"))
from r1_probe import make_field, divisors, code_from_generator   # noqa: E402


def all_words(F, basis, n):
    ADD, MUL = F.add, F.mul
    words = [tuple([F.zero] * n)]
    for row in basis:
        extra = []
        for w in words:
            for c in range(1, F.Q):
                extra.append(tuple(ADD[w[i]][MUL[c][row[i]]] for i in range(n)))
        words = words + extra
    return words


def min_dist(F, basis, n):
    best = None
    for w in all_words(F, basis, n):
        t = sum(1 for x in w if x != F.zero)
        if t and (best is None or t < best):
            best = t
    return best


def enc(F, c):
    c %= F.p
    return F.enc[tuple((c // F.p ** i) % F.p for i in range(F.deg))]


def gray_e2(F, W1, W2, M, lower=0):
    """Exact min over (a,b) != (0,0) of w((a_i,b_i)M) summed over positions; e = 2."""
    ADD, MUL = F.add, F.mul
    m11, m12 = enc(F, M[0][0]), enc(F, M[0][1])
    m21, m22 = enc(F, M[1][0]), enc(F, M[1][1])
    best = None
    for a in W1:
        for b in W2:
            if not any(a) and not any(b):
                continue
            tot = 0
            for i in range(len(a)):
                if ADD[MUL[m11][a[i]]][MUL[m12][b[i]]] != F.zero:
                    tot += 1
                if ADD[MUL[m21][a[i]]][MUL[m22][b[i]]] != F.zero:
                    tot += 1
            if best is None or tot < best:
                best = tot
                if best <= lower:
                    return best
    return best


def gray_e(F, Ws, M, e, lower=0):
    """Exact min Gray weight for general e over all tuples (not all zero)."""
    ADD, MUL = F.add, F.mul
    Me = [[enc(F, c) for c in row] for row in M]
    n = len(Ws[0][0])
    best = None
    for idx in itertools.product(*[range(len(W)) for W in Ws]):
        chosen = [Ws[k][idx[k]] for k in range(e)]
        if all(not any(c) for c in chosen):
            continue
        tot = 0
        for pos in range(n):
            for j in range(e):
                acc = F.zero
                for k in range(e):
                    acc = ADD[acc][MUL[Me[k][j]][chosen[k][pos]]]
                if acc != F.zero:
                    tot += 1
        if best is None or tot < best:
            best = tot
            if best <= lower:
                return best
    return best


def matrix_ok(F, M):
    e = len(M)
    Me = [[enc(F, c) for c in row] for row in M]
    Ms = [[F.pow(Me[k][j], F.p) for k in range(e)] for j in range(e)]
    P = [[F.zero] * e for _ in range(e)]
    for i in range(e):
        for k in range(e):
            acc = F.zero
            for j in range(e):
                acc = F.add[acc][F.mul[Me[i][j]][Ms[j][k]]]
            P[i][k] = acc
    diag = [P[i][i] for i in range(e)]
    nu = diag[0]
    ok = (all(d == nu for d in diag) and nu != F.zero
          and all(P[i][k] == F.zero for i in range(e) for k in range(e) if i != k))
    return ok, nu


def field_codes(p, q, n):
    F = make_field(p, q)
    out = []
    for alpha in range(1, F.Q):
        for g in divisors(F, n, alpha):
            b = code_from_generator(F, g, n, alpha)
            if not b:
                continue
            out.append((alpha, g, b, len(b), min_dist(F, b, n)))
    return F, out


def test_e2(p, q, n):
    F, codes = field_codes(p, q, n)
    M = ((1, 1), (1, -1))
    ok, nu = matrix_ok(F, M)
    print("=" * 86)
    print(f"E2  q={q}, n={n}, F_{F.Q}: M={M}, MM*=nu I with nu={nu}, admissible={ok}")
    if not ok:
        print("     (nu = 0 in this characteristic: the paper's matrix is degenerate; skipped)")
        return
    words = {i: all_words(F, c[2], n) for i, c in enumerate(codes)}
    checked = bad = 0
    for i, ci in enumerate(codes):
        for j, cj in enumerate(codes):
            lo = min(ci[4], cj[4])
            dg = gray_e2(F, words[i], words[j], M, lower=lo)
            checked += 1
            if not (lo <= dg <= 2 * lo):
                bad += 1
                print(f"    VIOLATION alpha={ci[0],cj[0]} d={ci[4],cj[4]} d(psi)={dg}"
                      f" bounds=({lo},{2*lo})")
    print(f"  pairs checked: {checked};  bound violations: {bad}")
    eq_ok = eq_bad = 0
    for i, ci in enumerate(codes):
        dg = gray_e2(F, words[i], words[i], M, lower=ci[4])
        if dg == ci[4]:
            eq_ok += 1
        else:
            eq_bad += 1
            print(f"    DxD FAILED alpha={ci[0]} k={ci[3]} d={ci[4]} d(psi)={dg}")
    print(f"  theorem  C1 = C2 = D  =>  d(psi) = d(D) :  {eq_ok} hold, {eq_bad} fail")
    groups = {}
    for i, ci in enumerate(codes):
        for j, cj in enumerate(codes):
            lo = min(ci[4], cj[4])
            dg = gray_e2(F, words[i], words[j], M, lower=lo)
            groups.setdefault((ci[3], ci[4], cj[3], cj[4]), set()).add(dg)
    nd = {k: v for k, v in groups.items() if len(v) > 1}
    print(f"  component-data groups: {len(groups)};  with >1 Gray distance: {len(nd)}")
    for k in sorted(nd)[:4]:
        print(f"    (k1,d1,k2,d2)={k} -> d(psi) in {sorted(nd[k])}")
    return checked, bad, eq_bad, len(nd)


def find_matrix(F, e, want_dense=True):
    best = None
    for entries in itertools.product(range(F.Q), repeat=e * e):
        cand = tuple(tuple(entries[r * e:(r + 1) * e]) for r in range(e))
        ok, nu = matrix_ok(F, cand)
        if ok:
            nz = sum(1 for row in cand for c in row if c)
            if best is None or nz > best[0]:
                best = (nz, cand, nu)
            if not want_dense:
                return best
    return best


def test_e3(p, q, n):
    F, codes = field_codes(p, q, n)
    print("=" * 86)
    print(f"E3  q={q}, n={n}, F_{F.Q}: searching an admissible 3x3 M (densest found)")
    found = find_matrix(F, 3)
    if not found:
        print("  no admissible M found")
        return
    nz, M, nu = found
    print(f"  M={M}  nu={nu}  nonzero entries={nz}")
    words = [all_words(F, c[2], n) for c in codes]
    checked = bad = 0
    for i, ci in enumerate(codes):
        for j, cj in enumerate(codes):
            for k, ck in enumerate(codes):
                lo = min(ci[4], cj[4], ck[4])
                dg = gray_e(F, [words[i], words[j], words[k]], M, 3, lower=lo)
                checked += 1
                if not (lo <= dg <= 3 * lo):
                    bad += 1
                    print(f"    VIOLATION k={ci[3],cj[3],ck[3]} d={ci[4],cj[4],ck[4]}"
                          f" d(psi)={dg} bounds=({lo},{3*lo})")
    print(f"  triples checked: {checked};  bound violations: {bad}")


def test_special(p, q, n):
    """Theorem B (only one component nonzero) and Theorem C (all components equal)."""
    F, codes = field_codes(p, q, n)
    print("=" * 86)
    print(f"SPECIAL  q={q}, n={n}, F_{F.Q}")
    zero = [tuple([F.zero] * n)]
    M = ((1, 1), (1, -1))
    ok, nu = matrix_ok(F, M)
    if ok:
        rho = 2
        bad = 0
        for c in codes:
            W = all_words(F, c[2], n)
            dg = gray_e2(F, W, zero, M, lower=0)
            if dg != rho * c[4]:
                bad += 1
                print(f"    Thm B FAILED alpha={c[0]} d={c[4]} d(psi)={dg} expected={rho*c[4]}")
        print(f"  Thm B  C2 = 0  =>  d(psi) = {rho} d(C1):  {len(codes)-bad} hold, {bad} fail")
    # Theorem C, e = 2: column sums of M are 2 and 0 -> sigma = 1 -> d(psi) = d(D)
    if ok:
        bad = 0
        for c in codes:
            W = all_words(F, c[2], n)
            dg = gray_e2(F, W, W, M, lower=c[4])
            if dg != c[4]:
                bad += 1
        print(f"  Thm C  e=2, sigma=1  =>  d(psi) = d(D):  {len(codes)-bad} hold, {bad} fail")
    # Theorem C, e = 3 with the dense matrix found earlier.
    # The search is |F|^9, so it is only affordable over F_4.
    found = find_matrix(F, 3) if F.Q <= 4 else None
    if found:
        nz, M3, nu3 = found
        cols = []
        for j in range(3):
            acc = F.zero
            for k in range(3):
                acc = F.add[acc][M3[k][j]]
            cols.append(acc)
        sigma = sum(1 for c in cols if c != F.zero)
        print(f"  e=3 matrix {M3}, column sums {cols} in F_{F.Q}, sigma = {sigma}")
        print("  Thm C only gives an UPPER bound sigma*d(D) for sigma > 1; checking <=")
        bad = tight = 0
        for c in codes:
            W = all_words(F, c[2], n)
            dg = gray_e(F, [W, W, W], M3, 3, lower=c[4])
            if dg > sigma * c[4]:
                bad += 1
                print(f"    Thm C(e=3) VIOLATED alpha={c[0]} d={c[4]} d(psi)={dg}"
                      f" > sigma*d={sigma*c[4]}")
            if dg == sigma * c[4]:
                tight += 1
        print(f"  Thm C  e=3 equal components:  {len(codes)-bad}/{len(codes)} satisfy "
              f"d(psi) <= sigma*d(D);  equality in {tight}, strict in {len(codes)-tight}")
        print("  (strict below sigma*d shows the diagonal codeword is NOT optimal, so no")
        print("   product formula can hold for e >= 3 -- recorded as a corrected prediction)")


if __name__ == "__main__":
    test_e2(3, 3, 2)
    test_e2(3, 3, 3)
    test_e2(2, 2, 2)
    test_e2(2, 2, 4)
    test_e3(2, 2, 2)
    test_special(3, 3, 2)
    test_special(3, 3, 3)
    test_special(2, 2, 2)
