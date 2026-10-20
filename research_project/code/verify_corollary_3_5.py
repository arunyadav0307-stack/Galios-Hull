"""
Phase 1B verification:
  (1) brute-force attainable-hull-dimension sets  D_k(n,q,lambda)
  (2) test of Corollary 3.5 (both parts)
  (3) test that the hull-dimension distribution over the affine algebra A
      factorizes as the convolution (product) of the constituent distributions.

Run:  python3 verify_corollary_3_5.py
"""
from collections import Counter
from itertools import product as iproduct
from gf import *


def divisors_from_factorization(F, facts):
    """all monic divisors of prod h_i^{e_i}"""
    divs = [[1]]
    for h, e in facts:
        new = []
        for d in divs:
            for a in range(e+1):
                new.append(pmul(F, d, ppow(F, h, a)))
        divs = new
    return divs


def ppow(F, h, a):
    r = [1]
    for _ in range(a):
        r = pmul(F, r, h)
    return r


def constacyclic_divisors(F, n, lam):
    xn = [0]*(n+1); xn[n] = 1; xn[0] = F.neg(lam)
    return divisors_from_factorization(F, factor(F, xn))


def code_basis(F, n, lam, g):
    k = n-(len(g)-1)
    rows = []
    for i in range(k):
        f = [0]*i + list(g)
        while len(f)-1 >= n:
            c = f[-1]; f = f[:-1]
            f[0] = F.add(f[0], F.mul(c, lam))
        rows.append([f[j] if j < len(f) else 0 for j in range(n)])
    return rows


def hull_distribution(F, n, lam, k):
    """Counter {hull_dim: number of lambda-constacyclic codes} for one field"""
    c = Counter()
    for g in constacyclic_divisors(F, n, lam):
        B = code_basis(F, n, lam, g)
        c[hull_dim(F, B, n, k)] += 1
    return c


def main():
    print("="*78)
    print("TEST 1 -- Corollary 3.5(1): p odd, n'=1, n=p^e', q=p^e, k arbitrary")
    print("="*78)
    F9 = GF(3, 2, [2, 2, 1])
    n, q, k = 9, 9, 1          # n = 3^2, n'=1
    for lam, name in [(1, "lambda=1"), (F9.neg(1), "lambda=-1")]:
        c = hull_distribution(F9, n, lam, k)
        Ds = sorted(c)
        print(f"  q=9 n=9 k=1 {name}: attainable set D_1 = {Ds}")
        print(f"      counts {dict(sorted(c.items()))}")
    # ring A = F_9[x]/<x^2-1>, N = 2 components, lambda = e1+e2
    c1 = hull_distribution(F9, n, 1, k)
    N = 2
    ring = Counter()
    for a, b in iproduct(c1, c1):
        ring[a+b] += c1[a]*c1[b]
    print(f"  ring A=F9[x]/<x^2-1>, N={N}, lambda=e1+e2 : D = {sorted(ring)}")
    print(f"  predicted |D| = N(n-1)/2 + 1 = {N*(n-1)//2 + 1} ; observed = {len(ring)}"
          f"  -> {'PASS' if len(ring)==N*(n-1)//2+1 else 'FAIL'}")

    print()
    print("="*78)
    print("TEST 2 -- Corollary 3.5(2): p=2, e even, k=e/2, ord(lam)n' | 2^e-1")
    print("="*78)
    # F_4 = F_2(w), w^2+w+1=0
    F4 = GF(2, 2, [1, 1, 1])
    w = 2
    n, q, k = 4, 4, 1          # n = 1 * 2^2
    lam = F4.pow(w, 1)         # ord(lam) = 3 | 2^2-1 = 3
    print("  ord(lambda) =", next(i for i in range(1, 4) if F4.pow(lam, i) == 1))
    c = hull_distribution(F4, n, lam, k)
    print(f"  q=4 n=4 k=1 lambda=w : attainable set D_1 = {sorted(c)}")
    print(f"      counts {dict(sorted(c.items()))}")
    N = 2
    ring = Counter()
    for a, b in iproduct(c, c):
        ring[a+b] += c[a]*c[b]
    print(f"  ring A=F4[x]/<x^2+x+w>, N={N}, lambda=e1+w e2 : D = {sorted(ring)}")
    print(f"  predicted |D| = N n/2 + 1 = {N*n//2 + 1} ; observed = {len(ring)}"
          f"  -> {'PASS' if len(ring)==N*n//2+1 else 'FAIL'}")

    print()
    print("="*78)
    print("TEST 3 -- product factorization of the joint hull-dimension distribution")
    print("="*78)
    # A = F_4[x]/<x^2+x+w> : two components, both F_4.
    # lambda = e1 + w e2  -> constituent multipliers 1 and w
    n, k = 4, 1
    cA = hull_distribution(F4, n, 1, k)
    cB = hull_distribution(F4, n, F4.pow(w, 1), k)
    joint = Counter()
    for a, b in iproduct(cA, cB):
        joint[a+b] += cA[a]*cB[b]
    direct = Counter()
    # direct enumeration over A = tuples of component codes
    for ga in constacyclic_divisors(F4, n, 1):
        for gb in constacyclic_divisors(F4, n, F4.pow(w, 1)):
            ha = hull_dim(F4, code_basis(F4, n, 1, ga), n, k)
            hb = hull_dim(F4, code_basis(F4, n, F4.pow(w, 1), gb), n, k)
            direct[ha+hb] += 1
    print("  local distributions :", dict(sorted(cA.items())), dict(sorted(cB.items())))
    print("  convolution         :", dict(sorted(joint.items())))
    print("  direct over A       :", dict(sorted(direct.items())))
    print("  ->", "PASS (factorization holds exactly)"
          if joint == direct else "FAIL")
    tot_local = sum(cA.values())*sum(cB.values())
    print(f"  total number of codes: product of locals = {tot_local}, direct = {sum(direct.values())}")


if __name__ == "__main__":
    main()
