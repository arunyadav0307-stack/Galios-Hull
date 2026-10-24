"""
P3-7b: two structural facts about repeated-root codes C_a = <(x-1)^a> in F_q[x]/(x^n-1), n = p^s.

(A) FIELD INDEPENDENCE.  d(C_a) does not depend on the field F_q (q = p^m), because the parity
    check matrix H_a[i][j] = C(j,i) mod p has entries in F_p, and the rank of a matrix with entries
    in F_p is the same over every extension field (rank = largest non-zero minor).  Hence

        d(C_a over F_q) = d(C_a over F_p)   for every q = p^m.

    Tested here by computing d(C_a) for n = 9 over F_9 (t^2 = -1) and comparing with the F_3 values
    of the P3-7 run.

(B) WEIGHT-2 CLASSIFICATION (Lemma W2).  For a >= 1, C_a contains a word of weight 2 iff
    a <= p^(s-1); weight 1 never occurs for a >= 1.  Consequently d(C_a) >= 3 for a > p^(s-1),
    which together with the word y^(2e) = (x^e - 1)^2 gives

        d(C_a) = 3     for   p^(s-1) < a <= 2 p^(s-1),  p >= 3        (Theorem C).

    Tested here by exhaustive search for codewords of weight <= 2 in every C_a.

METHOD.  A word supported on a set S of exponents lies in C_a iff the columns of H_a indexed by S
are linearly dependent (Lemma C of P3_7_POWER_ATTAINMENT.md).  So "is there a word of weight <= w"
is a rank test on an a x |S| matrix -- exact, and it needs no codeword enumeration, which is what
lets the F_9 comparison run at all.

An earlier version of this script tested the wrong side (it asked for combinations vanishing *on* S
instead of *outside* S) and reported weight-1 words for every code; that is why the rank test is now
stated as column dependence of H_a, where the direction is unambiguous.

Pure stdlib, ASCII only.
"""
import itertools
import sys


def binom_mod_p(j, i, p):
    """C(j,i) mod p by Lucas' theorem."""
    if i < 0 or i > j:
        return 0
    out = 1
    while i:
        jt, it = j % p, i % p
        if it > jt:
            return 0
        num, den = 1, 1
        for k in range(it):
            num = num * (jt - k) % p
            den = den * (k + 1) % p
        out = out * num % p * pow(den, p - 2, p) % p
        j //= p
        i //= p
    return out


# ---------------------------------------------------------------- fields
class Fp:
    """F_p as residues mod p."""
    name = "F_p"

    def __init__(self, p):
        self.p = p
        self.q = p

    def add(self, x, y):
        return (x + y) % self.p

    def sub(self, x, y):
        return (x - y) % self.p

    def mul(self, x, y):
        return x * y % self.p

    def inv(self, x):
        return pow(x % self.p, self.p - 2, self.p)

    def zero(self, x):
        return x % self.p == 0


class F9:
    """F_9 = F_3[t]/(t^2 + 1); a + b t is stored as a + 3b."""
    name = "F_9"
    p = 3
    q = 9

    def add(self, x, y):
        return self.sub(x, self.neg(y))

    def sub(self, x, y):
        return (x % 3 - y % 3) % 3 + 3 * ((x // 3 - y // 3) % 3)

    def neg(self, x):
        return (-x % 3) + 3 * (-(x // 3) % 3)

    def mul(self, x, y):
        a, b = x % 3, x // 3
        c, d = y % 3, y // 3
        return (a * c + 2 * b * d) % 3 + 3 * ((a * d + b * c) % 3)

    def inv(self, x):
        for y in range(1, 9):
            if self.mul(x, y) == 1:
                return y
        raise ZeroDivisionError

    def zero(self, x):
        return x == 0


# ---------------------------------------------------------------- linear algebra over a field
def rank(matrix, F):
    """Rank of a list of rows over the field F."""
    m = [list(r) for r in matrix]
    rows = len(m)
    if rows == 0:
        return 0
    cols = len(m[0])
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if not F.zero(m[i][c]):
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        inv = F.inv(m[r][c])
        m[r] = [F.mul(inv, x) for x in m[r]]
        for i in range(rows):
            if i != r and not F.zero(m[i][c]):
                f = m[i][c]
                m[i] = [F.sub(x, F.mul(f, y)) for x, y in zip(m[i], m[r])]
        r += 1
        if r == rows:
            break
    return r


def has_codeword_of_weight(n, a, p, F, w):
    """True iff C_a has a non-zero word with weight <= w (support search on H_a columns)."""
    if a == 0:
        return w >= 1
    cols = [[binom_mod_p(j, i, p) for i in range(a)] for j in range(n)]   # n columns of length a
    if w == 1:
        return any(all(F.zero(x) for x in c) for c in cols)
    for S in itertools.combinations(range(n), w):
        sub = [cols[j] for j in S]                                        # |S| vectors of length a
        if rank(sub, F) < w:
            return True
    return False


def min_weight_capped(n, a, p, F, cap):
    """Smallest weight <= cap of a non-zero word of C_a, else None."""
    for w in range(1, cap + 1):
        if has_codeword_of_weight(n, a, p, F, w):
            return w
    return None


def main():
    ok = True

    print("=" * 78)
    print("(A) Field independence:  d(C_a) over F_9  vs  d(C_a) over F_3,  n = 9")
    print("    H_a has entries in F_p; rank over F_q = rank over F_p (minors), so d cannot depend on q.")
    f3 = {0: 1, 1: 2, 2: 2, 3: 2, 4: 3, 5: 3, 6: 3, 7: 6, 8: 9}    # from p3_power_attainment_log.txt
    print("     a   d over F_3 (P3-7)   d over F_9 (cap 4)   agree")
    mism = 0
    for a in range(0, 9):
        d9 = min_weight_capped(9, a, 3, F9(), 4)
        exp = f3[a]
        if exp > 4:
            agree = (d9 is None)          # cap: only "no word of weight <= 4" is testable
            shown = ">4" if d9 is None else d9
        else:
            agree = (d9 == exp)
            shown = d9
        mism += (not agree)
        print(f"    {a:2d}   {exp:6d}              {shown!s:>6}             {'yes' if agree else 'NO'}")
    print(f"    mismatches: {mism}")
    ok = ok and mism == 0

    print()
    print("=" * 78)
    print("(B) Weight-2 classification:  weight<=2 word exists  <=>  a = 0 (w=1) or 1 <= a <= p^(s-1) (w=2)")
    tot = bad = 0
    for p, s in [(2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (5, 1), (5, 2), (7, 1), (11, 1)]:
        n, e = p ** s, p ** (s - 1)
        row = []
        for a in range(n):
            got = min_weight_capped(n, a, p, Fp(p), 2)
            pred = 1 if a == 0 else (2 if a <= e else None)
            good = (got == pred)
            tot += 1
            bad += (not good)
            row.append(f"{a}:{got}" + ("" if good else f"[exp {pred}]"))
        print(f"    p={p:2d}, n={n:2d}, e={e:2d}  " + " ".join(row))
    print(f"    total {tot} values, {bad} disagreements with Lemma W2")
    ok = ok and bad == 0

    print()
    print("=" * 78)
    print("(C) Theorem C:  d(C_a) = 3 exactly for e < a <= 2e when p >= 3")
    for p, s in [(3, 2), (5, 2), (3, 3)]:
        n, e = p ** s, p ** (s - 1)
        out = []
        for a in range(1, n):
            mw = min_weight_capped(n, a, p, Fp(p), 4)
            out.append((a, mw))
        band = [a for a, mw in out if mw == 3]
        print(f"    p={p}, n={n}, e={e}:  a with d = 3 (cap 4): {band}")
        print(f"      expected band e < a <= 2e: {list(range(e + 1, 2 * e + 1))}")
        if p == 3 and s == 3:
            # exhaustive subset search to 4 on n=27 with a up to 18 is expensive; report only shape
            pass
    print()
    print("Overall:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
