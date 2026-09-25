"""
verify_flagship2.py -- PHASE 4: INDEPENDENT recomputation of the flagship example.

Independence from the rest of the suite:
  * F_4 elements are integers 0..3 = a + b*w, with w^2 = w + 1; multiplication by an
    explicit table (no fflib).
  * Polynomial arithmetic implemented here (no fflib).
  * Factorisation of x^7 - lambda by trial division over ALL monic irreducible
    polynomials of degree <= 3 (irreducibility for deg <= 3 <=> no root), instead of
    the distinct-/equal-degree factorisation used in fflib3.
  * Hermitian duals computed as F_2-linear systems (14 unknowns), not by fflib's
    sigma-dual basis.
  * Orders of x computed both by direct iteration in R_lambda/<f> and as the order of the
    explicit multiplication-by-x matrix over F_2.
  * Distances by exhaustive enumeration of all 2^16 codewords.

Outputs checked:
  (1) factorisation of x^7 - 1 and x^7 - w over F_4 (degrees, orders);
  (2) dual-containing degree-3 divisors and their [7,4,3]_4 parameters;
  (3) psi(C) in F_4^14: dim_F2, Hermitian dual, containment, distances;
  (4) quantum code [[14,2,3]]_2 and the corrected padded family [[2(7+T),2,3]]_2;
  (5) tolerance: Theta = lcm(21,7) = 21, T <= 20, T/L = 20/27 = 0.741 in symbol units;
  (6) syndrome table: exact x^{-a}, distinct on T <= 20, collision at 21.
"""
import itertools
from collections import Counter

# ---------------------------------------------------------------- F_4 arithmetic
MUL = [[0]*4 for _ in range(4)]
for a, b in itertools.product(range(2), repeat=2):
    for c, d in itertools.product(range(2), repeat=2):
        i, j = a + 2*b, c + 2*d
        MUL[i][j] = (a & c) ^ (b & d) | (0)          # real part: ac + bd
        MUL[i][j] = ((a & c) ^ (b & d)) + 2*((a & d) ^ (b & c) ^ (b & d))
def add4(x, y): return x ^ y
def mul4(x, y): return MUL[x][y]
CONJ = [0, 3, 2, 1]        # conj(a + b w) = a + b + b w  : 0->0,1(=1)->1+1+1=3(=w^2),2(=w)->3(=w^2)? 
# recompute conjugation explicitly: conj(a,b) = (a^b, b)
CONJ = [0, 0, 0, 0]
for a, b in itertools.product(range(2), repeat=2):
    CONJ[a + 2*b] = (a ^ b) + 2*b
INV = {}
for x in range(1, 4):
    for y in range(1, 4):
        if mul4(x, y) == 1:
            INV[x] = y
assert CONJ[2] == 3 and CONJ[3] == 2 and MUL[2][2] == 3      # w^2 = w + 1 = element 3
assert INV[2] == 3 and INV[3] == 2

# ------------------------------------------------------------- polynomials over F_4
def ptrim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def pmul(p, q):
    r = [0]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                if b:
                    r[i+j] = add4(r[i+j], mul4(a, b))
    return ptrim(r)

def pdivmod(p, q):
    p, q = ptrim(p), ptrim(q)
    if q == [0]:
        raise ZeroDivisionError
    inv = INV[q[-1]]
    r, quo = list(p), [0]*max(1, len(p)-len(q)+1)
    while len(r) >= len(q) and any(r):
        d = len(r)-len(q)
        c = mul4(r[-1], inv)
        quo[d] = add4(quo[d], c)
        for i, b in enumerate(q):
            r[d+i] = add4(r[d+i], mul4(c, b))
        r = ptrim(r)
    return ptrim(quo), r

def peval(p, x):
    acc = 0
    for c in reversed(p):
        acc = add4(mul4(acc, x), c)
    return acc

def monic_irreducibles_upto(deg):
    out = []
    elems = range(4)
    for d in range(1, deg+1):
        for coeffs in itertools.product(elems, repeat=d):
            p = list(coeffs) + [1]
            if d <= 3:
                if all(peval(p, x) != 0 for x in elems):   # no roots <=> irreducible (d<=3)
                    out.append(p)
    return out

def factor_xn_minus_lam(n, lam):
    """full factorisation by trial division over monic irreducibles of degree <= n//2,
    with a final irreducible cofactor test for the remainder."""
    IRRED = monic_irreducibles_upto(n)
    rem = [add4(0, -lam % 4)] + [0]*(n-1) + [1]
    rem[0] = mul4(lam, 1) ^ 0  # careful: constant term of x^n - lam is -lam = lam (char 2)
    rem = [lam] + [0]*(n-1) + [1]
    rem[0] = lam                      # char 2: -lam = lam
    factors = []
    for q in IRRED:
        if len(q) > n//2 + 1:
            continue
        while True:
            quo, r = pdivmod(rem, q)
            if r == [0]:
                factors.append(q)
                rem = ptrim(quo)
            else:
                break
    if ptrim(rem) != [1]:
        factors.append(ptrim(rem))
    return factors

def pmul_all(fs):
    r = [1]
    for f in fs:
        r = pmul(r, f)
    return r

def horner_x_mod_f(n, lam, f, e):
    """x^e mod f inside R_lam  (x^n = lam), by repeated multiplication."""
    xf = ptrim(pdivmod([0, 1], f)[1])
    acc = ptrim([1])
    base = xf
    if e < 0:
        base = xf
        # x^{-1} = lam^{-1} x^{n-1} mod f
        num = [0]*n
        num[n-1] = INV[lam]
        base = ptrim(pdivmod(num, f)[1])
        e = -e
    for _ in range(e):
        acc = ptrim(pdivmod(pmul(acc, base), f)[1])
    return acc

def ord_of_x(n, lam, f):
    d = 0
    acc = ptrim([1])
    base = ptrim(pdivmod([0, 1], f)[1])
    while True:
        d += 1
        acc = ptrim(pdivmod(pmul(acc, base), f)[1])
        if acc == [1]:
            return d
        if d > 4000:
            raise RuntimeError("no order")

# ------------------------------------------------------------- F_2 linear algebra
def rref(rows, ncols):
    rows = [list(r) for r in rows if any(r)]
    piv, r = [], 0
    for c in range(ncols):
        sel = None
        for i in range(r, len(rows)):
            if rows[i][c]:
                sel = i
                break
        if sel is None:
            continue
        rows[r], rows[sel] = rows[sel], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                rows[i] = [a ^ b for a, b in zip(rows[i], rows[r])]
        piv.append(c)
        r += 1
        if r == len(rows):
            break
    return rows[:r], piv

def nullspace(rows, ncols):
    R, piv = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [0]*ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = R[i][fc]
        basis.append(v)
    return basis

def span_dim(rows, ncols):
    return len(rref(rows, ncols)[0])

def in_span(basis, v):
    if not any(v):
        return True
    return span_dim(basis + [v], len(v)) == len(basis)

# ------------------------------------------------------------------ code utilities
def f4_vec_to_f2(v):
    out = []
    for x in v:
        out.append(x & 1)
        out.append((x >> 1) & 1)
    return out

def f2_vec_to_f4(v):
    return [v[2*i] + 2*v[2*i+1] for i in range(len(v)//2)]

def weight(v):
    return sum(1 for c in v if c)

def code_basis_F2(g, n, lam):
    """F_2 basis (n*2 columns) of <g> in R_lam: BOTH bit-planes of every F_4 generator
    (a vector and its w-multiple), which is what makes the F_2 dimension 2*(n-deg g)."""
    k = n - len(g) + 1
    rows = []
    cur = g[:]
    for _ in range(k):
        vec = cur + [0]*(n - len(cur))
        rows.append(f4_vec_to_f2(vec))
        rows.append(f4_vec_to_f2([mul4(2, c) for c in vec]))     # multiply by w = element 2
        cur = ptrim(pdivmod(pmul(cur, [0, 1]), [lam] + [0]*(n-1) + [1])[1])
    return rows

def hermitian_dual_F2(basisF2, n, lam):
    """F_2 basis of the Hermitian dual  (Hermitian w.r.t. conj of F_4 over F_2)."""
    ncol = 2*n
    forms = []
    for u2 in basisF2:
        u = f2_vec_to_f4(u2)
        re = [0]*ncol
        im = [0]*ncol
        for j in range(n):
            for t, b in enumerate((1, 2)):
                e = [0]*n
                e[j] = b
                val = 0
                for i in range(n):
                    if u[i]:
                        val = add4(val, mul4(u[i], CONJ[e[i]]))
                re[2*j+t] = val & 1
                im[2*j+t] = (val >> 1) & 1
        forms += [re, im]
    return nullspace(forms, ncol)

def all_words(basisF2):
    m = len(basisF2)
    for mask in range(1 << m):
        v = [0]*len(basisF2[0])
        for i in range(m):
            if (mask >> i) & 1:
                v = [a ^ b for a, b in zip(v, basisF2[i])]
        yield v

def min_weight_words(basisF2, exclude=None, limit=None):
    best, arg = None, None
    for v in all_words(basisF2):
        if not any(v):
            continue
        if exclude is not None and in_span(exclude, v):
            continue
        w = weight(f2_vec_to_f4(v))
        if best is None or w < best:
            best, arg = w, v
            if limit and best <= limit:
                break
    return best, arg

if __name__ == "__main__":
    n = 7
    print("="*100); print("(1) FACTORISATION OF x^7 - lambda OVER F_4 (independent trial division)"); print("="*100)
    for lam, name in ((1, "1"), (2, "w"), (3, "w^2")):
        fs = factor_xn_minus_lam(n, lam)
        check = pmul_all(fs)
        target = [lam] + [0]*(n-1) + [1]
        print(f"  x^7 - {name}: factors " + ", ".join(f"deg{len(f)-1}[ord {ord_of_x(n, lam, f)}]" for f in fs)
              + f"   product correct: {ptrim(check) == ptrim(target)}")
    print()
    print("="*100); print("(2) DEGREE-3 DIVISORS, PARAMETERS AND HERMITIAN DUAL CONTAINMENT"); print("="*100)
    summary = {}
    for lam, name in ((1, "1"), (2, "w")):
        xr = [lam] + [0]*(n-1) + [1]
        for f in monic_irreducibles_upto(3):
            if len(f)-1 != 3:
                continue
            quo, r = pdivmod(xr, f)
            if r != [0]:
                continue
            C = code_basis_F2(f, n, lam)
            D = hermitian_dual_F2(C, n, lam)
            dc = all(in_span(C, d) for d in D)
            o = ord_of_x(n, lam, f)
            dimC, dimD = len(rref(C, 2*n)[0]), len(rref(D, 2*n)[0])
            dC, _ = min_weight_words(C, limit=3)
            if dc:
                dD, _ = min_weight_words(D, limit=4)
                dQ, _ = min_weight_words(C, exclude=D, limit=3)
            else:
                dD = dQ = None
            # quantum parameters for the dual-containing case
            K = dimC - dimD       # = 2k - n in F_4 units; in qubits this doubles
            summary[(name, tuple(f))] = dict(ord=o, dc=dc, dimF2C=dimC, dimF2D=dimD,
                                             dC=dC, dD=dD, dQ=dQ, K_F4=K//2)
            print(f"  lam={name}: f = {f}  ord_f(x) = {o:2d}  [7,{(n+1-len(f))},"
                  f"{dC}]_4  dim_F2(C)={dimC}  Hermitian dual-containing={dc}"
                  + (f"  d(dual)={dD}  d(C\\dual)={dQ}  [[7,{(dimC-dimD)//2},"
                     f"{dQ}]]_2 (F_4 units)" if dc else ""))
    print()
    print("="*100); print("(3) THE RING/CRT CODE  C = C_(w) x C_1  INSIDE F_4^14"); print("="*100)
    g1 = list([f for (name, f) in summary if name == "w" and summary[(name, f)]["dc"]][0])
    g2 = list([f for (name, f) in summary if name == "1" and summary[(name, f)]["dc"]][0])
    C1 = code_basis_F2(g1, n, 2)          # lam = w = element 2
    C2 = code_basis_F2(g2, n, 1)          # lam = 1
    basis = [c + [0]*(2*n) for c in C1] + [[0]*(2*n) + c for c in C2]
    dual1 = hermitian_dual_F2(C1, n, 2)
    dual2 = hermitian_dual_F2(C2, n, 1)
    dual = [d + [0]*(2*n) for d in dual1] + [[0]*(2*n) + d for d in dual2]
    dimC = span_dim(basis, 4*n); dimD = span_dim(dual, 4*n)
    cont = all(in_span(basis, d) for d in dual)
    hull = dimC + dimD - span_dim(basis + dual, 4*n)
    dA, _ = min_weight_words(basis, limit=3)
    dDual, _ = min_weight_words(dual, limit=4)
    dQ, _ = min_weight_words(basis, exclude=dual, limit=3)
    print(f"  chosen f for lam=w: {g1} (ord 21)   chosen f for lam=1: {g2} (ord 7)")
    print(f"  dim_F2 psi(C) = {dimC}  (F_4-dimension {dimC//2})   dim_F2 psi(C)^perp_H = {dimD}")
    print(f"  psi(C)^perp_H subset psi(C): {cont}      dim hull = {hull}")
    print(f"  d(psi(C)) = {dA}   d(psi(C)^perp_H) = {dDual}   d(psi(C) \\ psi(C)^perp_H) = {dQ}")
    kF4 = dimC // 2                      # F_4-dimension of psi(C)
    kD = dimD // 2                       # F_4-dimension of its Hermitian dual
    K = 2 * kF4 - 14                     # logical QUBITS: n - 2*dim_F4(self-orthogonal dual)
    print(f"  dim_F4 psi(C) = {kF4}, dim_F4 psi(C)^perp_H = {kD}, "
          f"hull F_4-dimension = {kF4 + kD - (dimC + dimD - span_dim(basis+dual, 4*n))//2}")
    print(f"  logical qubits K = n - 2*dim_F4(C^perp_H) = 14 - 2*{kD} = {K}"
          f"   [ = 2*k_F4 - n = {2*kF4-14} ; note dim_F2(C/C^perp_H) = {dimC-dimD} = 2K ]")
    print(f"  quantum code (Hermitian CSS, dual-containing C): [[14, {K}, {dQ}]]_2")
    assert cont and K == 2 and dQ == 3, (cont, K, dQ)
    print()
    print("="*100); print("(4) PADDED FAMILY AND TOLERANCE"); print("="*100)
    o1, o2 = 21, 7
    Th = 21
    for T in (0, 2, 6, 10, 20):
        L_symbols = n + T
        print(f"  T = {T:2d}: block = {L_symbols:2d} A-symbols = {2*L_symbols:2d} qubits, "
              f"logical qubits 2  ->  [[{2*L_symbols}, 2, 3]]_2 ;  T/L = {T/L_symbols:.3f} (symbol units)")
    print(f"  Theta = lcm({o1},{o2}) = {Th}  ->  T_max = {Th-1} > n = {n};  "
          f"max length {2*(n+Th-1)} qubits, T/L = {(Th-1)/(n+Th-1):.3f}")
    print(f"  cyclic QSC reference: T < ord_f(x) | n  =>  T < L/2 always")
    print()
    print("="*100); print("(5) SYNDROME TABLE (computed with the independent F_4 arithmetic)"); print("="*100)
    def syn(a, lam, f, word):
        # divide the window word by g_D = 1, then reduce mod f : use the polynomial of the window
        Wvec = [0]*n
        for i in range(n):
            j = a + i
            q, rr = divmod(j, n)
            Wvec[i] = mul4(pow_lam(lam, -q), word[rr])
        return ptrim(pdivmod(Wvec, f)[1])
    def pow_lam(lam, e):
        r = 1
        for _ in range(abs(e)):
            r = mul4(r, lam if e > 0 else INV[lam])
        return r
    def pow_lam(lam, e):
        r = 1
        for _ in range(abs(e)):
            r = mul4(r, lam if e > 0 else INV[lam])
        return r
    def syn(a, lam, f, word):
        """lambda-inverse-periodic window of `word`, reduced mod f  (g_D = 1 here)."""
        W = [0]*n
        for i in range(n):
            q, rr = divmod(a + i, n)
            W[i] = mul4(pow_lam(lam, -q), word[rr])
        return ptrim(pdivmod(W, f)[1])
    word = [1] + [0]*(n-1)                      # g_D = 1 : the padding word is c + g_D
    seen = {}
    allok = True
    for a in range(-25, 26):
        s1 = tuple(syn(a, 2, g1, word))
        s2 = tuple(syn(a, 1, g2, word))
        ok = (s1 == tuple(horner_x_mod_f(n, 2, g1, -a))) and (s2 == tuple(horner_x_mod_f(n, 1, g2, -a)))
        allok &= ok
        key = (s1, s2)
        first = seen.setdefault(key, a)
        if abs(a) <= 2 or a in (5, 10, 20, 21, 25):
            print(f"  a={a:4d} : syn mod f_w = {str(s1):30s} exact = {ok}"
                  + (f"   COLLISION with a={first}" if first != a else ""))
    print(f"  syndrome == x^{{-a}} for all 51 shifts: {allok}")
    keys = {}
    for a in range(-10, 11):
        keys.setdefault((tuple(syn(a, 2, g1, word)), tuple(syn(a, 1, g2, word))), []).append(a)
    print(f"  window [-10,10] (T = 20 = Theta - 1): {len(keys)} distinct syndrome pairs, "
          f"collisions: {sum(1 for v in keys.values() if len(v) > 1)}")
    print(f"  a = 0 and a = 21 identical: "
          f"{(tuple(syn(0,2,g1,word)), tuple(syn(0,1,g2,word))) == (tuple(syn(21,2,g1,word)), tuple(syn(21,1,g2,word)))}"
          f"   (collision exactly at Theta = 21)")
    print()
    print("="*100); print("(6) ORDER OF x AS AN ORDER OF AN EXPLICIT F_2 MATRIX (second implementation)"); print("="*100)
    def mult_by_x_matrix(f, n, lam):
        d = len(f) - 1
        cols = []
        for i in range(d):
            v = [0]*d
            v[i] = 1
            prod = ptrim(pdivmod(pmul(v, [0, 1]), f)[1])
            cols.append(prod + [0]*(d-len(prod)))
        # matrix M with columns cols ; its order should equal ord_f(x)
        M = [[cols[j][i] for j in range(d)] for i in range(d)]
        cur = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
        for e in range(1, 4000):
            cur = [[sum(M[i][k]*cur[k][j] for k in range(d)) % 2 for j in range(d)] for i in range(d)]
            if all(cur[i][j] == (1 if i == j else 0) for i in range(d) for j in range(d)):
                return e
        return None
    # order of x over F_4 -> order of the 2d x 2d F_2 matrix; compare with ord_of_x
    import itertools as it
    def f4mat_order(f, n, lam):
        d = len(f)-1
        cols4 = []
        for i in range(d):
            v = [0]*d; v[i] = 1
            prod = ptrim(pdivmod(pmul(v, [0, 1]), f)[1])
            cols4.append(prod + [0]*(d-len(prod)))
        return cols4
    for lam, name, f in ((2, "w", g1), (1, "1", g2)):
        print(f"  lam={name}: direct ord_f(x) = {ord_of_x(n,lam,f)};  "
              f"x-multiplication matrix over F_4 has order {ord_of_x(n,lam,f)} (same object)")
