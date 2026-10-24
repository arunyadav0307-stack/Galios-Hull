"""
Phase 6/7 deliverable generator: QUANTUM_CODE_PARAMETER_TABLE.csv

Every row is produced by exact computation, not typed by hand:

  * field-level constacyclic codes over F_{q^2} are enumerated as monic divisors
    (bijection proved in CONSTITUENT_ENUMERATOR_FORMULA.md, Lemma 1);
  * dual-containing is decided on the field code by an independent basis test;
  * the ring code is the CRT tuple, and psi(C) is built explicitly in F_{q^2}^{en};
  * K = dim psi(C) is computed as the rank of psi(C), not from the formula;
  * d = d(psi(C)) is the exact minimum weight of psi(C), enumerated.

Columns are documented in QUANTUM_PARAMETER_VERIFICATION.md.  A row is emitted only
when every quantity could be computed exactly; nothing is filled in from a bound.

ASCII only, pure stdlib.
"""
import csv
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r1_probe"))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r3_probe"))
from r1_probe import make_field, divisors, code_from_generator        # noqa: E402
from r3_probe import field_is_dc, rref                               # noqa: E402
from p3_ring_gray import all_words, matrix_ok, find_matrix, enc      # noqa: E402


def psibasis(F, C, M, n, e):
    """psi applied to a basis of the CRT tuple, as vectors in F_{q^2}^{en}.

    The tuple is given as a list of `e` component bases; the product code has basis
    {(0,..,a_k,..,0) : a_k in basis_k}, which is what this builds.
    """
    rows = []
    for k, basis in enumerate(C):
        for a in basis:
            out = []
            for i in range(n):
                for j in range(e):
                    acc = F.zero
                    for kk in range(e):
                        if kk != k:
                            continue
                        if M[kk][j] % F.p:
                            acc = F.add[acc][F.mul[enc(F, M[kk][j])][a[i]]]
                    out.append(acc)
            rows.append(out)
    return rows


def code_params(F, C, M, n, e):
    basis = psibasis(F, C, M, n, e)
    basis = rref(F, basis, e * n)[0] if basis else []
    K = len(basis)
    if K == 0:
        return 0, None
    d = None
    for w in all_words(F, basis, e * n):
        t = sum(1 for x in w if x != F.zero)
        if t and (d is None or t < d):
            d = t
    return K, d


def rows_for(p, q, e, n, M, label, max_tuples=None):
    F = make_field(p, q)
    ok, nu = matrix_ok(F, M)
    if not ok:
        raise SystemExit(f"matrix not admissible over F_{F.Q}")
    pool = []
    for alpha in range(1, F.Q):
        for g in divisors(F, n, alpha):
            b = code_from_generator(F, g, n, alpha)
            pool.append((alpha, b))
    dc = [(a, b) for (a, b) in pool if b and field_is_dc(F, b, n)]
    out = []
    for idx, tup in enumerate(itertools.product(dc, repeat=e)):
        if max_tuples and idx >= max_tuples:
            break
        K, d = code_params(F, [t[1] for t in tup], M, n, e)
        if d is None:
            continue
        en = e * n
        kq = 2 * K - en
        if kq < 0:
            continue
        out.append({
            "instance": label, "q": q, "e": e, "n": n,
            "M": str(M).replace(" ", ""),
            "lambda_components": ";".join(str(t[0]) for t in tup),
            "component_dims": ";".join(str(len(t[1])) for t in tup),
            "en": en, "K": K, "quantum_k": kq, "d": d,
            "quantum_params": f"[[{en},{kq},>={d}]]_{p}" if q == p else
                              f"[[{en},{kq},>={d}]]_{q}",
            "quantum_singleton_slack": (kq + 2 * d) - (en + 2),
            "rank_eq_sum_of_dims": "yes" if K == sum(len(t[1]) for t in tup) else "no",
            "degenerate_zero_k": "yes" if kq == 0 else "no",
            "trivial_full_k": "yes" if K == en else "no",
            "distance_exact": "yes",
        })
    return out


def main():
    all_rows = []
    F3 = make_field(3, 3)
    all_rows += rows_for(3, 3, 2, 2, ((1, 1), (1, -1)), "R_2/F_9/n=2")
    all_rows += rows_for(3, 3, 2, 3, ((1, 1), (1, -1)), "R_2/F_9/n=3")
    F4 = make_field(2, 2)
    found = find_matrix(F4, 3)
    M3 = found[1]
    nz, M3, nu = found
    all_rows += rows_for(2, 2, 3, 2, M3, "R_3/F_4/n=2")

    path = os.path.join(HERE, "QUANTUM_CODE_PARAMETER_TABLE.csv")
    cols = ["instance", "q", "e", "n", "M", "lambda_components", "component_dims",
            "en", "K", "quantum_k", "d", "quantum_params",
            "quantum_singleton_slack", "rank_eq_sum_of_dims",
            "degenerate_zero_k", "trivial_full_k",
            "distance_exact"]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in all_rows:
            w.writerow(r)
    print(f"wrote {path}: {len(all_rows)} rows")
    # summary used by the accompanying documents
    for label in sorted({r["instance"] for r in all_rows}):
        rs = [r for r in all_rows if r["instance"] == label]
        params = {}
        for r in rs:
            params[r["quantum_params"]] = params.get(r["quantum_params"], 0) + 1
        mds = sum(1 for r in rs if r["quantum_singleton_slack"] == 0)
        nontrivial = [r for r in rs if 0 < r["quantum_k"] < r["en"]]
        nt_mds = sum(1 for r in nontrivial if r["quantum_singleton_slack"] == 0)
        bad_rank = sum(1 for r in rs if r["rank_eq_sum_of_dims"] != "yes")
        print(f"  {label}: {len(rs)} codes; quantum-MDS {mds} "
              f"(of which NON-TRIVIAL {nt_mds} of {len(nontrivial)}); "
              f"distinct params {len(params)}")
        print(f"      rank(psi(C)) == sum of component dims : "
              f"{len(rs)-bad_rank}/{len(rs)}")
        for k in sorted(params):
            print(f"      {k}  x{params[k]}")


if __name__ == "__main__":
    main()
