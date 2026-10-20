"""
Phase 1B -- independent recomputation of Examples 2 and 3 of
Debnath, Islam, Martinez-Moro, Prakash, "Galois hulls of constacyclic codes
over affine algebra rings" (arXiv:2412.08512v1), Sections 4.2.

For each example we verify, from scratch:
  * the stated irreducible factorizations of x^n - lambda_S over F_q
  * the divisibility g_S | x^n - lambda_S
  * dim_{F_q} hull_k(C_S) for each constituent code
  * the total k-Galois hull dimension of C over A
  * the Gray-map matrix condition M (M^{(p^k)})^T = gamma I_N
  * the parameters [nN, K, d] of psi(C), with d computed EXACTLY
    (parity-check column dependence, not a random search)
  * the EAQECC parameters obtained from Theorem 10

Run: python3 verify_examples.py
"""
from itertools import combinations
from gf import *


def cyclic_basis(F, n, lam, g):
    k = n-(len(g)-1)
    rows = []
    for i in range(k):
        f = [0]*i + list(g)
        while len(f)-1 >= n:
            c = f[-1]; f = f[:-1]
            f[0] = F.add(f[0], F.mul(c, lam))
        rows.append([f[j] if j < len(f) else 0 for j in range(n)])
    return rows


def gray_basis(F, n, N, comps, M):
    rows = []
    for j, (lam, g) in enumerate(comps):
        for h in cyclic_basis(F, n, lam, g):
            vec = []
            for i in range(n):
                vec += [F.mul(h[i], M[j][r]) for r in range(N)]
            rows.append(vec)
    return rows


def exact_min_distance(F, G, length):
    """exact d of the row space of G, via parity-check column dependence"""
    K, Gr = span_rank(F, G, length)
    dual = nullspace(F, Gr, length)
    Hcols = [[dual[r][j] for r in range(len(dual))] for j in range(length)]
    m = len(dual)
    for w in range(1, length+1):
        for S in combinations(range(length), w):
            if span_rank(F, [list(Hcols[j]) for j in S], m)[0] < w:
                return K, w, S
    return K, None, None


def check_matrix_condition(F, M, N, k):
    Mt = [[F.pow(M[i][j], F.p**k) for j in range(N)] for i in range(N)]
    P = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            s = 0
            for r in range(N):
                s = F.add(s, F.mul(M[i][r], Mt[j][r]))
            P[i][j] = s
    gamma = P[0][0]
    ok = all(P[i][i] == gamma for i in range(N)) and all(
        P[i][j] == 0 for i in range(N) for j in range(N) if i != j)
    return ok, gamma, P


def main():
    print("="*78)
    print("EXAMPLE 2  (paper: Section 4.2)   q=9, p=3, e=2, k=1 (Hermitian), n=7, N=2")
    print("="*78)
    F9 = GF(3, 2, [2, 2, 1])          # w^2 + 2w + 2 = 0
    w = 3
    print("  w^2 =", F9.mul(w, w), "  ord(w) =",
          next(i for i in range(1, 9) if F9.pow(w, i) == 1))
    # stated factorizations
    x7m1 = [0]*8; x7m1[7] = 1; x7m1[0] = F9.neg(1)
    x7mw2 = [0]*8; x7mw2[7] = 1; x7mw2[0] = F9.neg(F9.pow(w, 2))
    f1 = factor(F9, x7m1); f2 = factor(F9, x7mw2)
    print("  x^7-1   irreducible factor degrees:",
          sorted([(len(h)-1, e) for h, e in f1]))
    print("  x^7-w^2 irreducible factor degrees:",
          sorted([(len(h)-1, e) for h, e in f2]))
    g1 = [2, 6, 7, 1]                  # x^3 + w^3 x^2 + w^5 x + 2
    g2 = [4, 1]                        # x + w^2
    print("  g1 | x^7-1  :", pdivmod(F9, x7m1, g1)[1] == [0])
    print("  g2 | x^7-w^2:", pdivmod(F9, x7mw2, g2)[1] == [0])
    B1 = cyclic_basis(F9, 7, 1, g1); B2 = cyclic_basis(F9, 7, F9.pow(w, 2), g2)
    print("  dim C1 =", span_rank(F9, B1, 7)[0], " dim C2 =", span_rank(F9, B2, 7)[0])
    h1 = hull_dim(F9, B1, 7, 1); h2 = hull_dim(F9, B2, 7, 1)
    print("  dim hull_1(C1) =", h1, " dim hull_1(C2) =", h2,
          "  TOTAL =", h1+h2, "  (paper: 0)")
    M2 = [[F9.pow(w, 1), F9.pow(w, 3)], [F9.pow(w, 7), F9.pow(w, 5)]]
    ok, gamma, _ = check_matrix_condition(F9, M2, 2, 1)
    print("  M (M^(3))^T = gamma I :", ok, " gamma =", gamma)
    G = gray_basis(F9, 7, 2, [(1, g1), (F9.pow(w, 2), g2)], M2)
    K, d, wit = exact_min_distance(F9, G, 14)
    print(f"  psi(C) = [14, {K}, {d}]_9   (paper: [14,10,4])")
    print(f"  EAQECC = [[14, {K}-{h1+h2}, {d}; {14-K-(h1+h2)}]]_9"
          f"   (paper: [[14,10,4;4]]_9)")

    print()
    print("="*78)
    print("EXAMPLE 3  (paper: Section 4.2)   q=25, p=5, e=2, k=1 (Hermitian), n=13, N=2")
    print("="*78)
    F25 = GF(5, 2, [2, 4, 1])         # w^2 + 4w + 2 = 0
    w = 5
    print("  w^2 =", F25.mul(w, w), "  ord(w) =",
          next(i for i in range(1, 25) if F25.pow(w, i) == 1))
    x13m1 = [0]*14; x13m1[13] = 1; x13m1[0] = F25.neg(1)
    x13mw8 = [0]*14; x13mw8[13] = 1; x13mw8[0] = F25.neg(F25.pow(w, 8))
    print("  x^13-1   irreducible factor degrees:",
          sorted([(len(h)-1, e) for h, e in factor(F25, x13m1)]))
    print("  x^13-w^8 irreducible factor degrees:",
          sorted([(len(h)-1, e) for h, e in factor(F25, x13mw8)]))
    g1 = pmul(F25, [4, 1], [1, F25.pow(w, 1), 1])
    g2 = [F25.pow(w, 20), 1]
    print("  g1 | x^13-1   :", pdivmod(F25, x13m1, g1)[1] == [0])
    print("  g2 | x^13-w^8 :", pdivmod(F25, x13mw8, g2)[1] == [0])
    B1 = cyclic_basis(F25, 13, 1, g1); B2 = cyclic_basis(F25, 13, F25.pow(w, 8), g2)
    print("  dim C1 =", span_rank(F25, B1, 13)[0],
          " dim C2 =", span_rank(F25, B2, 13)[0])
    h1 = hull_dim(F25, B1, 13, 1); h2 = hull_dim(F25, B2, 13, 1)
    print("  dim hull_1(C1) =", h1, " dim hull_1(C2) =", h2,
          "  TOTAL =", h1+h2, "  (paper: 2)")
    M3 = [[F25.pow(w, 1), F25.pow(w, 2)], [2, F25.pow(w, 13)]]
    ok, gamma, _ = check_matrix_condition(F25, M3, 2, 1)
    print("  M (M^(5))^T = gamma I :", ok, " gamma =", gamma)
    G = gray_basis(F25, 13, 2, [(1, g1), (F25.pow(w, 8), g2)], M3)
    K, d, wit = exact_min_distance(F25, G, 26)
    print(f"  psi(C) = [26, {K}, {d}]_25   (paper: [26,22,4])")
    print(f"  EAQECC = [[26, {K}-{h1+h2}, {d}; {26-K-(h1+h2)}]]_25"
          f"   (paper: [[26,20,4;2]]_25)")


if __name__ == "__main__":
    main()
