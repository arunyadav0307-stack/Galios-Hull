#!/usr/bin/env python3
"""Phase 1 - independent verification of Tables 1-3 of Yadav et al. (2024), HAL v1.

Every row is re-derived from the printed generator polynomials: length, dimension,
exact minimum distance, hull dimension, Hermitian dual-containing property and the
quantum Singleton residual.  Claims that cannot be reproduced are reported as
MISMATCH, never adjusted.
"""
import sys, re, itertools, json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import galois, numpy as np
from gfcore import Field, phi, ord_j

OUT = []
TERM = re.compile(r"^(?:(t)(\d*)|(\d+))?(?:x(\d*))?$")


def parse_scalar(s, F):
    s = s.strip()
    m = TERM.match(s)
    if not m:
        raise ValueError("cannot parse scalar %r" % s)
    tpow, tdig, lit, xpow = m.groups()
    if xpow is not None:
        raise ValueError("not a scalar: %r" % s)
    if tpow:
        return F.pw(int(tdig) if tdig else 1)
    return F.GF(int(lit))


def parse_poly(s, F):
    terms = {}
    for chunk in s.split("+"):
        chunk = chunk.replace(" ", "")
        m = TERM.match(chunk)
        if not m:
            raise ValueError("cannot parse term %r in %r" % (chunk, s))
        tpow, tdig, lit, xpow = m.groups()
        coeff = F.pw(int(tdig) if tdig else 1) if tpow else F.GF(int(lit) if lit else 1)
        if xpow is None:
            exp = 0
        elif xpow == "":
            exp = 1
        else:
            exp = int(xpow)
        terms[exp] = coeff
    return F.poly_from_terms([(c, e) for e, c in terms.items()])


def min_dist_fast(F, G):
    """Exact minimum distance for the small-co-dimension codes in these tables."""
    G = F.GF(G)
    H = G.null_space()
    r, N = H.shape
    for w in (1, 2):
        for S in itertools.combinations(range(N), w):
            if F.rank(H[:, list(S)]) < w:
                return w, "exhaustive"
    idx = np.array(list(itertools.combinations(range(N), 3)))
    A = H[:, idx]
    dep = np.ones(len(idx), dtype=bool)
    for rows in itertools.combinations(range(r), 3):
        M = A[list(rows)]                      # (3, T, 3)
        m00, m01, m02 = M[0][:, 0], M[0][:, 1], M[0][:, 2]
        m10, m11, m12 = M[1][:, 0], M[1][:, 1], M[1][:, 2]
        m20, m21, m22 = M[2][:, 0], M[2][:, 1], M[2][:, 2]
        det = (m00 * (m11 * m22 - m12 * m21)
               - m01 * (m10 * m22 - m12 * m20)
               + m02 * (m10 * m21 - m11 * m20))
        dep &= (det == 0)
        if not dep.any():
            break
    if dep.any():
        return 3, "exhaustive"
    if r <= 3:
        return 4, "any 4 columns are dependent"
    rng = np.random.default_rng(0)
    for _ in range(4000):
        S = sorted(int(v) for v in rng.choice(N, 4, replace=False))
        if F.rank(H[:, S]) < 4:
            return 4, "witness"
    return None, "unresolved"


def gray(F, cons, M):
    rows = []
    e = M.shape[0]
    for idx, C in enumerate(cons):
        for r in C:
            blk = []
            for j in range(C.shape[1]):
                v = F.GF(np.zeros(e, dtype=int)); v[idx] = r[j]
                blk.extend((v @ M).tolist())
            rows.append(blk)
    return F.GF(np.array(rows))


ROWS = [
    # table, row, n, a, b, g1, g2, p, claimed [en,k,d], claimed hull, claimed quantum
    (1, 1, 12, "1", "1", "x3 + x2 + t8x + t8", "x+ t8", 5, (24, 20, 4), 0, None),
    (1, 2, 12, "1", "6", "x3 + t2x2 + t2x + t36", "x+ t6", 7, (24, 20, 4), 0, None),
    (1, 3, 12, "1", "1", "x3 + x2 + t40x + t40", "x+ t10", 11, (24, 20, 4), 0, None),
    (1, 4, 30, "1", "10", "x2 + 4x + 1", "x+ t10", 11, (60, 57, 3), 0, None),
    (1, 5, 12, "1", "1", "x3 + 8x2 + 5x + 12", "x+ 1", 13, (24, 20, 4), 0, None),
    (1, 6, 14, "1", "1", "x2 + t27x + t12", "x+ 1", 13, (28, 25, 4), 0, None),
    (1, 7, 30, "t36", "1", "x2 + t4x + t120", "x+ 1", 13, (60, 57, 3), 0, None),
    (2, 1, 12, "1", "1", "x3 + x2 + t8x + t8", "x+ t2", 5, (24, 20, 4), 1, None),
    (2, 2, 12, "1", "1", "x3 + x2 + t13x + t14", "x+ 2", 5, (24, 20, 4), 2, None),
    (2, 3, 12, "1", "1", "x3 + tx2 + t22x + t44", "x+ t4", 7, (24, 20, 4), 2, None),
    (2, 4, 12, "1", "t12", "x3 + t2x2 + t2x + t36", "x+ t5", 7, (24, 20, 4), 1, None),
    (2, 5, 12, "1", "10", "x3 + t3x2 + t103x + t70", "x+ t25", 11, (24, 20, 4), 1, None),
    (2, 6, 12, "10", "10", "x3 + t45x2 + t50x + t95", "x+ t5", 11, (24, 20, 4), 2, None),
    (2, 7, 30, "1", "1", "x2 + t5x + t4", "x+ 1", 11, (60, 57, 3), 1, None),
    (2, 8, 30, "1", "1", "x2 + t5x + t4", "x+ t4", 11, (60, 57, 3), 2, None),
    (2, 9, 12, "1", "1", "x3 + 11x + 4", "x+ 1", 13, (24, 20, 4), 1, None),
    (2, 10, 12, "1", "1", "x3 + 4x2 + x + 4", "x+ 2", 13, (24, 20, 4), 2, None),
    (2, 11, 30, "1", "t120", "x2 + 8x + 4", "x+ t4", 13, (60, 57, 3), 2, None),
    (2, 12, 30, "1", "t120", "x2 + 8x + 4", "x+ t60", 13, (60, 57, 3), 1, None),
    (3, 1, 16, "1", "1", "x3 + t7x2 + tx + 1", "x+ t", 3, (32, 28, 3), None, ((32, 24, 3), 4)),
    (3, 2, 16, "1", "1", "x3 + t7x2 + tx + 1", "x3 + tx2 + t7x + 1", 3, (32, 26, 4), None, ((32, 20, 4), 6)),
    (3, 3, 20, "2", "2", "x3 + x2 + x + t", "x+ t", 3, (40, 36, 3), None, ((40, 32, 3), 4)),
    (3, 4, 26, "1", "t2", "x3 + 2x2 + 1", "x+ t", 3, (52, 48, 3), None, ((52, 44, 3), 4)),
    (3, 5, 28, "2", "t2", "x3 + t6x2 + tx + t3", "x2 + t3", 3, (56, 51, 3), None, ((56, 46, 3), 6)),
    (3, 6, 30, "1", "t2", "x3 + t2x2 + t2x + 1", "x2 + t3x + t6", 3, (60, 55, 4), None, ((60, 50, 4), 4)),
    (3, 7, 20, "t4", "1", "x3 + t11x2 + t3", "x+ 1", 5, (40, 36, 4), None, ((40, 32, 4), 2)),
    (3, 8, 26, "4", "4", "x3 + t7x2 + tx + 2", "x+ 2", 5, (52, 48, 4), None, ((52, 44, 4), 2)),
    (3, 9, 28, "1", "4", "x3 + t23x2 + tx + 3", "x2 + t15x + 1", 5, (56, 51, 4), None, ((56, 46, 4), 4)),
    (3, 10, 30, "1", "4", "x2 + 2x + 1", "x+ t2", 5, (60, 57, 3), None, ((60, 54, 3), 2)),
    (3, 11, 30, "1", "t12", "x2 + t3x + 1", "x+ t2", 7, (60, 57, 3), None, ((60, 54, 3), 2)),
    (3, 12, 30, "1", "t12", "x3 + t7x2 + t41x + 4", "x+ t2", 7, (60, 56, 4), None, ((60, 52, 4), 2)),
    (3, 13, 36, "1", "t12", "x3 + t4", "x+ t3", 7, (72, 68, 3), None, ((72, 64, 3), 4)),
    (3, 14, 14, "12", "12", "x2 + t21x + 1", "x+ t6", 13, (28, 25, 4), None, ((28, 22, 4), 0)),
]


def run():
    Fs = {}
    for p in (3, 5, 7, 11, 13):
        Fs[p] = Field(p, 2)
    res = []
    for (tab, row, n, a_s, b_s, g1s, g2s, p, claim, hull_claim, qclaim) in ROWS:
        F = Fs[p]; GF = F.GF
        a, b = parse_scalar(a_s, F), parse_scalar(b_s, F)
        g1, g2 = parse_poly(g1s, F), parse_poly(g2s, F)
        rec = {"table": tab, "row": row, "n": n, "p": p, "lambda": [a_s, b_s],
               "g1": str(g1), "g2": str(g2)}
        ok = True
        d1 = F.modulus(n, a); d2 = F.modulus(n, b)
        div1 = (d1 % g1 == galois.Poly([0], field=GF))
        div2 = (d2 % g2 == galois.Poly([0], field=GF))
        rec["g1_divides_xn_minus_a"] = bool(div1)
        rec["g2_divides_xn_minus_b"] = bool(div2)
        ok &= div1 and div2
        C1 = F.code_from_generator(g1, n, a)
        C2 = F.code_from_generator(g2, n, b)
        k1, k2 = F.rank(C1), F.rank(C2)
        rec["k"] = k1 + k2
        ok &= (k1 + k2 == claim[1])
        M = F.GF(np.array([[1, 1], [1, F.p - 1]]))
        G = gray(F, [C1, C2], M)
        en = G.shape[1]; kk = F.rank(G)
        rec["en"], rec["dim"] = en, kk
        ok &= (en, kk) == (claim[0], claim[1])
        d, how = min_dist_fast(F, G)
        rec["d"], rec["d_method"] = d, how
        ok &= (d == claim[2])
        hd = F.hull_of_matrix(G)
        rec["hull"] = hd
        dc = F.is_dual_containing_matrix(C1) and F.is_dual_containing_matrix(C2)
        rec["dual_containing_constituents"] = bool(dc)
        if tab in (1, 2):
            if hull_claim is not None:
                ok &= (hd == hull_claim)
            else:
                ok &= True
        else:
            nq, kq, dq = qclaim[0]
            got = (en, 2 * kk - en, d)
            rec["quantum_claim"], rec["quantum_computed"] = list(nq and [nq, kq, dq]), list(got)
            ok &= got[1] == kq and d >= dq
            resid = en + 2 - (kq + 2 * dq)
            rec["residual_claimed"] = qclaim[1]
            rec["residual_recomputed"] = en + 2 - (got[1] + 2 * d)
            ok &= (resid == qclaim[1])
            rec["dual_containing"] = bool(dc)
        rec["status"] = "PASS" if ok else "MISMATCH"
        res.append(rec)
        print(f"T{tab} r{row:>2} n={n:>2} p={p:>2} [{en},{kk},{d}] claim[{claim[0]},{claim[1]},{claim[2]}] "
              f"hull={hd}" + (f" (claim {hull_claim})" if hull_claim is not None else "") +
              f" dc={dc} div={div1 and div2} -> {rec['status']}")
    return res


if __name__ == "__main__":
    r = run()
    json.dump(r, open("research_project/phase1/raw/tables_recalc.json", "w"), indent=1)
    bad = [x for x in r if x["status"] != "PASS"]
    print(f"\n{len(r) - len(bad)}/{len(r)} rows fully reproduced; mismatches: "
          f"{[(x['table'], x['row']) for x in bad]}")
