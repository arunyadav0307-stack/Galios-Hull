"""
Phase 3 / P3-4: the ring-level distribution.

For R_e = F_{q^2}[u]/(u^e - 1) with e | (q+1) and a FIXED admissible Gray matrix M, count the
dual-containing lambda-constacyclic codes C = (+)_l e_l C_l by their quantum parameters

    [[en, 2K - en, >=d]],      K = dim psi(C) = sum_l dim C_l,   d = d(psi(C)) exact.

Ingredients, all proved earlier in this phase:
  * Thm 1 (P3_3): C^perp_H <= C  iff  C_l^perp_H <= C_l for every l.  So the dual-containing
    tuples are exactly the tuples of dual-containing field codes.
  * psi is a bijective F_{q^2}-linear map, so dim psi(C) = dim C = sum_l k_l.
  * d(psi(C)) is computed exactly, never bounded, using the Gray matrix M.

The point of the table: by Thm 5 (P3_3) d(psi) is not a function of the constituent data, so this
distribution is NOT a product of field-level laws.  The table exhibits that.

Every row records lambda's component tuple, so the dependence on lambda is visible.

ASCII only, pure stdlib.
"""
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r1_probe"))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r3_probe"))
from r1_probe import make_field, divisors, code_from_generator      # noqa: E402
from r3_probe import field_is_dc                                     # noqa: E402
from p3_ring_gray import all_words, matrix_ok, gray_e2, gray_e, find_matrix   # noqa: E402


def field_data(p, q, n):
    """All nonzero field-level constacyclic codes, with k, d, dual-containing flag."""
    F = make_field(p, q)
    out = []
    for alpha in range(1, F.Q):
        for g in divisors(F, n, alpha):
            b = code_from_generator(F, g, n, alpha)
            if not b:
                continue
            W = all_words(F, b, n)
            d = min(sum(1 for x in w if x != F.zero) for w in W if any(w))
            out.append({"alpha": alpha, "g": g, "k": len(b), "d": d,
                        "dc": field_is_dc(F, b, n), "W": W})
    return F, out


def distribution(F, codes, e, n, M):
    """Exact quantum-parameter distribution over dual-containing tuples."""
    dc = [c for c in codes if c["dc"]]
    rows = []
    for tup in itertools.product(dc, repeat=e):
        K = sum(c["k"] for c in tup)
        L = e * n
        if 2 * K - L < 0:
            continue                     # cannot happen for DC codes, but guard
        if e == 2:
            d = gray_e2(F, tup[0]["W"], tup[1]["W"], M)
        else:
            d = gray_e(F, [c["W"] for c in tup], M, e)
        rows.append((tuple(c["alpha"] for c in tup), tuple(c["k"] for c in tup),
                     tuple(c["d"] for c in tup), K, d))
    return rows


def summarise(name, F, e, n, M, rows):
    print("=" * 88)
    print(f"{name}:  q field F_{F.Q}, e={e}, n={n}, M={M}")
    print(f"  dual-containing tuples with 2K - en >= 0 : {len(rows)}")
    dist = {}
    for (_, _, _, K, d) in rows:
        key = (2 * K - e * n, d)
        dist[key] = dist.get(key, 0) + 1
    print("  quantum-parameter distribution  [[en, 2K-en, >=d]],  en =", e * n)
    for key in sorted(dist):
        print(f"    [[{e*n}, {key[0]}, >={key[1]}]]  :  {dist[key]}")
    # does the parameter depend only on the constituent multiset of (k,d)?
    groups = {}
    for (al, ks, ds, K, d) in rows:
        groups.setdefault(tuple(sorted(zip(ks, ds))), set()).add((K, d))
    multi = {g: v for g, v in groups.items() if len(v) > 1}
    print(f"  constituent-data groups: {len(groups)};  giving more than one quantum "
          f"parameter: {len(multi)}")
    for g in sorted(multi)[:3]:
        print(f"    {(g)} -> {sorted(multi[g])}")
    return dist, multi


def main():
    # ---- e = 2, q = 3, n = 2 and n = 3, the paper's matrix
    F = make_field(3, 3)
    M = ((1, 1), (1, -1))
    ok, nu = matrix_ok(F, M)
    print(f"e=2 matrix {M}: admissible={ok}, nu={nu}")
    for n in (2, 3):
        codes = field_data(3, 3, n)[1]
        rows = distribution(F, codes, 2, n, M)
        summarise(f"R_2 over F_9, n={n}", F, 2, n, M, rows)

    # ---- e = 3, q = 2, n = 2, dense admissible matrix
    F4 = make_field(2, 2)
    found = find_matrix(F4, 3)
    nz, M3, nu3 = found
    print("=" * 88)
    print(f"e=3 matrix {M3}: nu={nu3}, nonzero entries={nz}")
    codes = field_data(2, 2, 2)[1]
    rows = distribution(F4, codes, 3, 2, M3)
    summarise("R_3 over F_4, n=2", F4, 3, 2, M3, rows)


if __name__ == "__main__":
    main()
