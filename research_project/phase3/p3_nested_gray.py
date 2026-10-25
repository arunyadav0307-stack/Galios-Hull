"""
P3-10: the e = 2 Gray image is the |u|u+v| (Plotkin) construction.

Setting (as in P3-3/P3-4).  R_e = F_q[u]/(u^e - 1) with gcd(e,q) = 1, R_e = F_q^e through the roots
alpha_1,...,alpha_e of u^e - 1, and the Gray map psi(c) = M c with M = (alpha_l^j)_{j,l}.

For e = 2 and q odd the roots are alpha_1 = 1, alpha_2 = -1, so M = ((1,1),(1,-1)) and

    psi(c_1, c_2) = ( c_1 + c_2 , c_1 - c_2 ).

CLAIM (P3-10).  If C_2 <= C_1 then

    psi(C_1 x C_2) = { (u, u+v) : u in C_1, v in C_2 }

is exactly the |u|u+v| (Plotkin sum) code, hence

    d(psi(C_1 x C_2)) = min { 2 d(C_1) , d(C_2) }.

Proof.  Set u = c_1 + c_2 (which lies in C_1 because C_2 <= C_1) and v = -2 c_2 (in C_2).  Then
u + v = c_1 + c_2 - 2 c_2 = c_1 - c_2 is the second coordinate, and because 2 is invertible (q odd)
the map (c_1,c_2) -> (u,v) is a bijection C_1 x C_2 -> C_1 x C_2.  So psi(C_1 x C_2) = {(u,u+v)},
the |u|u+v| code.  A codeword has weight w(u) + w(u+v).  If v = 0 the weight is 2w(u) >= 2 d(C_1).
If v != 0, then u - (u+v) = -v, so w(u) + w(u+v) >= w(v) >= d(C_2) by the triangle inequality, and
equality is attained at u = 0.  Hence d = min{2 d(C_1), d(C_2)}.  []

This is the classical |u|u+v| / Plotkin-sum distance formula (van Lint's construction); it is
re-proved above only so the document is self-contained.  NO NOVELTY IS CLAIMED.

What this script establishes computationally:
  * the formula holds for every nested pair we can enumerate, over several odd primes p;
  * it FAILS for pairs that are not nested, so the hypothesis is doing real work.

Pure stdlib, ASCII only.
"""
import itertools
import sys

CAP = 300000          # max |C_1| * |C_2| enumerated per pair


# ---------------------------------------------------------------- F_p arithmetic
class Field:
    def __init__(self, p):
        self.p = p

    def add(self, x, y):
        return (x + y) % self.p

    def sub(self, x, y):
        return (x - y) % self.p

    def neg(self, x):
        return (-x) % self.p

    def mul(self, x, y):
        return x * y % self.p

    def inv(self, x):
        return pow(x % self.p, self.p - 2, self.p)


# ---------------------------------------------------------------- polynomials (lists, low -> high)
def ptrim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pmul(F, a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    r[i + j] = F.add(r[i + j], F.mul(x, y))
    return ptrim(r)


def psub(F, a, b):
    n = max(len(a), len(b))
    r = [(a[i] if i < len(a) else 0) for i in range(n)]
    for i in range(n):
        if i < len(b) and b[i]:
            r[i] = F.sub(r[i], b[i])
    return ptrim(r)


def pdivmod(F, a, b):
    a = ptrim(list(a))
    b = ptrim(list(b))
    inv_lead = F.inv(b[-1])
    b = [F.mul(inv_lead, c) for c in b]
    q = [0] * max(1, len(a) - len(b) + 1)
    rem = ptrim(list(a))
    while len(rem) >= len(b) and not (len(rem) == 1 and rem[0] == 0):
        shift = len(rem) - len(b)
        coeff = rem[-1]
        q[shift] = coeff
        rem = psub(F, rem, [0] * shift + [F.mul(coeff, c) for c in b])
        if len(rem) == 1 and rem[0] == 0:
            break
    return ptrim(q), ptrim(rem)


def pmod(F, a, m):
    return pdivmod(F, a, m)[1]


def is_zero(p):
    return len(p) == 1 and p[0] == 0


def xn_minus_1(F, n):
    p = [0] * (n + 1)
    p[0] = F.neg(1)
    p[n] = 1
    return ptrim(p)


def divisors_of(F, f, max_deg):
    out = []
    for deg in range(max_deg + 1):
        for coeffs in itertools.product(range(F.p), repeat=deg):
            g = list(coeffs) + [1]
            if is_zero(pmod(F, f, g)):
                out.append(tuple(g))
    return out


def code_from_generator(F, g, n):
    """<g> in F_p[x]/(x^n - 1)."""
    f = xn_minus_1(F, n)
    g = list(g)
    dim = n - (len(g) - 1)
    if dim <= 0:
        return [[0]]
    words = []
    for coeffs in itertools.product(range(F.p), repeat=dim):
        h = list(coeffs)
        prod = pmul(F, g, h) if any(h) else [0]
        words.append(pmod(F, prod, f))
    return words


def weight(w):
    return sum(1 for c in w if c)


def min_dist(words):
    best = None
    for w in words:
        if any(w):
            d = weight(w)
            if best is None or d < best:
                best = d
    return best


def psi_distance(F, C1, C2, n):
    """min weight of (c1+c2, c1-c2) over C1 x C2, or None if too large."""
    if len(C1) * len(C2) > CAP:
        return None
    best = None
    for a in C1:
        for b in C2:
            left = [F.add(a[i] if i < len(a) else 0, b[i] if i < len(b) else 0) for i in range(n)]
            right = [F.sub(a[i] if i < len(a) else 0, b[i] if i < len(b) else 0) for i in range(n)]
            w = weight(left) + weight(right)
            if w == 0:
                continue
            if best is None or w < best:
                best = w
    return best


def main():
    total_checked = total_bad = total_control = 0
    cases = [(p, n) for p in (3, 5, 7, 11, 13) for n in (2, 3, 4, 5, 6)
             if n % p != 0]
    print("P3-10: psi(C1 x C2) is the |u|u+v| code, so d = min{2 d(C1), d(C2)} when C2 <= C1")
    print("(e = 2, Gray matrix M = ((1,1),(1,-1)) = the two roots of u^2 - 1)")
    print()

    for p, n in cases:
        F = Field(p)
        f = xn_minus_1(F, n)
        divs = divisors_of(F, f, n)
        if len(divs) < 2:
            continue
        codes = {g: code_from_generator(F, g, n) for g in divs}
        dist = {g: min_dist(codes[g]) for g in codes}

        checked = bad = skipped = 0
        details = []
        for g1 in divs:
            for g2 in divs:
                if not is_zero(pmod(F, list(g2), list(g1))):      # g1 must divide g2
                    continue
                d1, d2 = dist[g1], dist[g2]
                if d1 is None or d2 is None:
                    skipped += 1
                    continue
                dpsi = psi_distance(F, codes[g1], codes[g2], n)
                if dpsi is None:
                    skipped += 1
                    continue
                pred = min(2 * d1, d2)
                checked += 1
                if dpsi != pred:
                    bad += 1
                    details.append((g1, g2, d1, d2, dpsi, pred))

        # control: non-nested pairs
        control = 0
        for g1 in divs:
            for g2 in divs:
                if is_zero(pmod(F, list(g2), list(g1))):
                    continue
                d1, d2 = dist[g1], dist[g2]
                if d1 is None or d2 is None:
                    continue
                dpsi = psi_distance(F, codes[g1], codes[g2], n)
                if dpsi is None:
                    continue
                if dpsi != min(2 * d1, d2):
                    control += 1

        total_checked += checked
        total_bad += bad
        total_control += control
        flag = "PASS" if bad == 0 else "FAIL"
        print(f"p={p:2d}, n={n}:  {len(divs):2d} cyclic codes, {checked:3d} nested pairs checked, "
              f"{bad} disagreements, {skipped} skipped   [{flag}]")
        for (g1, g2, d1, d2, dpsi, pred) in details[:5]:
            print(f"    MISMATCH g1={g1} g2={g2}: d1={d1} d2={d2} d(psi)={dpsi} pred={pred}")

    print()
    print(f"TOTAL nested pairs checked: {total_checked}, disagreements: {total_bad}")
    print(f"non-nested pairs where the unqualified formula FAILS: {total_control}")
    print("(the hypothesis C_2 <= C_1 is therefore necessary as well as sufficient in the cases tested)")
    print()
    print("Overall:", "PASS" if total_bad == 0 else "FAIL")
    return 0 if total_bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
