"""
Closing L-2: the power-attainment conjecture for single-orbit repeated-root codes.

Setting.  F = F_q, char p, n = p^s.  Then x^n - 1 = (x-1)^n, and for 0 <= a <= n

    C_a = <(x-1)^a> = { f in F[x] : deg f < n, (x-1)^a | f } <= F^n,

because x^n - 1 = (x-1)^n, so the quotient loses nothing:
f = (x-1)^a h + (x-1)^n k = (x-1)^a (h + (x-1)^{n-a} k).

CONJECTURE (L-2, generalised from n=9).
    d(C_a) = min { w((x-1)^j) : a <= j <= n-1 },     and  d(C_n) is undefined (zero code).

Two tools make this decidable at larger n than the earlier brute force:

 (1) WEIGHT LEMMA (proved in the write-up).  w((x-1)^j) = prod_i (d_i + 1), where j = sum_i d_i p^i
     is the base-p expansion.  Proof: (x-1)^j = prod_i (x^{p^i} - 1)^{d_i} in characteristic p, each
     factor has all d_i + 1 coefficients nonzero since d_i < p, and the exponents from different
     factors lie in distinct residue classes, so no cancellation occurs.

 (2) CIRCUIT REDUCTION.  Substitute x = 1 + (x-1) in f(x) = sum_j f_j x^j; the coefficient
     of (x-1)^i is c_i = sum_{j >= i} f_j C(j,i).  So f is divisible by (x-1)^a iff c_i = 0 for
     i = 0..a-1, i.e. C_a = ker H_a with

         H_a[i][j] = C(j,i) mod p     (binomial, i = 0..a-1, j = 0..n-1; Lucas).

     Caution (bug found and fixed while running this script): the falling factorial
     j(j-1)...(j-i+1) is NOT the right matrix.  In characteristic p the ordinary derivative test
     cannot see multiplicity beyond p -- over F_3, (x-1)^3 = x^3 - 1 has every ordinary
     derivative vanishing at 1 although the root has multiplicity 3.  Using falling factorials
     produced d = 2 for every a >= 3 at n = 9, contradicting the committed table.

     A nonzero codeword of weight w is exactly a set of w columns of H_a that is linearly
     dependent.  Hence

         d(C_a) = minimum circuit size of the column matroid of H_a.

     This is exact, needs no enumeration of codewords, and lets n grow to 27 / 25 where the
     earlier weight-by-weight brute force could not reach.

ASCII only, pure stdlib.
"""
import itertools
import time
import sys


# ------------------------------------------------------------------ field (only char p matters)
class PField:
    """F_p as integers mod p; enough because the codes here are defined over any F_q of char p."""

    def __init__(self, p):
        self.p = p

    def sub(self, a, b):
        return (a - b) % self.p


def binom_mod_p(j, i, p):
    """C(j,i) mod p, by Lucas' theorem.  NOT the falling factorial.

    Writing f(x) = sum_j f_j x^j = sum_i c_i (x-1)^i using x = 1 + (x-1) gives
    c_i = sum_{j >= i} f_j * C(j,i), so C_a = ker H with H[i][j] = C(j,i) mod p.
    The ordinary-derivative test (falling factorials) is WRONG in characteristic p
    once a > p: it cannot see multiplicity beyond p, e.g. (x-1)^3 = x^3 - 1 has all
    ordinary derivatives vanishing at 1 although its root multiplicity is 3.
    """
    if i < 0 or i > j:
        return 0
    result = 1
    while i:
        jt, it = j % p, i % p
        if it > jt:
            return 0
        num, den = 1, 1
        for k in range(it):
            num = num * (jt - k) % p
            den = den * (k + 1) % p
        if den % p == 0:
            return 0
        result = result * num % p * pow(den, p - 2, p) % p
        j //= p
        i //= p
    return result


def rank_mod_p(rows, p):
    rows = [list(r) for r in rows]
    if not rows:
        return 0
    ncols = len(rows[0])
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][c] % p:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c], p - 2, p)
        rows[r] = [(x * inv) % p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % p:
                f = rows[i][c]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[r])]
        r += 1
    return r


def weight_of_power(j, p):
    """w((x-1)^j) = prod over base-p digits (d_i + 1)."""
    if j == 0:
        return 1
    w = 1
    while j:
        w *= (j % p) + 1
        j //= p
    return w


def predicted_table(n, p):
    """Suffix minima of the power weights: the value conjectured to be d(C_a)."""
    ws = [weight_of_power(j, p) for j in range(n)]
    out = []
    for a in range(n + 1):
        if a == n:
            out.append(None)                      # zero code
        else:
            out.append(min(ws[a:]))
    return out, ws


def min_circuit(n, a, p, cap=7):
    """Smallest dependent set of columns of H_a, by increasing size; None if above cap."""
    cols = [[binom_mod_p(j, i, p) for i in range(a)] for j in range(n)]
    # a set of size 1 is dependent iff the column is zero
    for j in range(n):
        if all(x == 0 for x in cols[j]):
            return 1
    for w in range(2, min(cap, n) + 1):
        for S in itertools.combinations(range(n), w):
            sub = [cols[j] for j in S]
            if rank_mod_p(sub, p) < w:
                return w
    return None


def code_distance_direct(n, a, p, max_words=200000):
    """Enumerate the code directly when the dimension is small.

    Basis rows are (x-1)^j for j = a..n-1, expanded in x using C(j,k) via Lucas.
    A first version divided the falling factorial by k! mod p, which is invalid
    whenever k >= p (k! = 0 mod p) and under-reported weights -- it gave d = 3 for
    (x-1)^8 over F_3 instead of 9.  Fixed to use binom_mod_p.
    """
    dim = n - a
    if p ** dim > max_words:
        return None
    basis = []
    for j in range(a, n):
        row = []
        for k in range(n):
            c = binom_mod_p(j, k, p)
            if c and (j - k) % 2:
                c = (-c) % p
            row.append(c)
        basis.append(row)
    best = None
    for coeffs in itertools.product(range(p), repeat=dim):
        if not any(coeffs):
            continue
        v = [0] * n
        for c, row in zip(coeffs, basis):
            if c:
                v = [(x + c * y) % p for x, y in zip(v, row)]
        w = sum(1 for x in v if x)
        if best is None or w < best:
            best = w
            if best == 1:
                return 1
    return best


def cross_check(n, p, cap=7, max_words=50000):
    """Compare the two independent tools wherever both are affordable."""
    both = mism = 0
    for a in range(n):
        if p ** (n - a) > max_words:
            continue
        c = min_circuit(n, a, p, cap=cap)
        e = code_distance_direct(n, a, p, max_words=max_words)
        if e is None:
            continue
        both += 1
        if c is not None and c != e:
            mism += 1
            print(f"    CROSS-CHECK MISMATCH a={a}: circuit {c} vs enumerate {e}")
    return both, mism


def run(p, s, cap=7, max_words=2000000, verbose=True):
    n = p ** s
    if verbose:
        print("=" * 78)
        print(f"p={p}, s={s}, n={n}:  x^{n} - 1 = (x-1)^{n}")
    pred, ws = predicted_table(n, p)
    if verbose:
        print(f"  w((x-1)^j) for j=0..{min(n,15)-1}: {ws[:15]}")
        print("   a   dim   d(computed)   d(conjecture)   agree   method")
    agree = bad = unknown = 0
    for a in range(n + 1):
        dim = n - a
        if dim == 0:
            if verbose:
                print(f"  {a:3d}  {dim:4d}   {'--':>10}   {str(pred[a]):>12}   {'n/a':>5}   zero code")
            continue
        d = min_circuit(n, a, p, cap=cap)
        method = "circuit"
        if d is None and p ** dim <= max_words:
            # Nothing dependent of size <= cap, so either the true distance exceeds
            # cap (normal) or the circuit search missed something (a tool bug: f lagged).
            d = code_distance_direct(n, a, p, max_words=max_words)
            method = "enumerate"
        if d is None:
            unknown += 1
            if verbose:
                print(f"  {a:3d}  {dim:4d}   {'?':>10}   {str(pred[a]):>12}   {'?':>5}   above cap")
            continue
        ok = (d == pred[a])
        agree += ok
        bad += (not ok)
        if verbose:
            print(f"  {a:3d}  {dim:4d}   {d:10d}   {str(pred[a]):>12}   "
                  f"{'yes' if ok else 'NO':>5}   {method}")
    if verbose:
        print(f"  agree {agree}, disagree {bad}, undetermined {unknown}")
    return agree, bad, unknown


# (p, s, cap).  n = p^s.  cap=7 keeps the subset search affordable up to n=27;
# when nothing of size <= 7 exists the direct enumeration (dimension small there)
# decides, and both regimes are logged separately.
def mbound(cases):
    """Check m(a) <= a + 1 (Singleton-consistent) for every a, using Lemma W only.

    No code is built: this is a statement about the weights of powers.  Run with
    `python3 p3_power_attainment.py --mbound`.
    """
    allok = True
    for p_, s_ in cases:
        n_ = p_ ** s_
        ws = [weight_of_power(j, p_) for j in range(n_)]
        bad = [a for a in range(n_) if min(ws[a:]) > a + 1]
        allok = allok and not bad
        print(f"  p={p_:2d}, n={n_:3d}: m(a) <= a+1 for all a? {not bad}"
              + (f"   VIOLATIONS {bad[:6]}" if bad else ""))
    print(f"  all cases satisfy m(a) <= a+1: {allok}")
    return allok


CASES = [(2, 1, 7), (2, 2, 7), (2, 3, 7), (2, 4, 7),
         (3, 1, 7), (3, 2, 7), (3, 3, 7),
         (5, 1, 7), (5, 2, 7),
         (7, 1, 7), (11, 1, 7)]

MBOUND_CASES = [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4),
                (5, 1), (5, 2), (5, 3), (7, 1), (7, 2), (11, 1), (13, 1)]

if __name__ == "__main__":
    if "--mbound" in sys.argv:
        print("Lemma-W check: m(a) = min_{j>=a} w((x-1)^j) <= a+1 (Singleton-consistent)")
        print("No code is constructed; only powers of (x-1) are weighed.")
        ok = mbound(MBOUND_CASES)
        sys.exit(0 if ok else 1)
    t0 = time.time()
    tot = [0, 0, 0]
    print("L-2 power-attainment check: d(C_a) = min_{j>=a} w((x-1)^j), n = p^s")
    print("d(C_a) computed exactly in two independent ways (circuit matroid / enumeration).")
    for p_, s_, cap_ in CASES:
        tot = [x + y for x, y in zip(tot, run(p_, s_, cap=cap_))]
        print(f"  [elapsed {time.time() - t0:.1f}s]")
    print("=" * 78)
    print(f"TOTAL agree {tot[0]}, disagree {tot[1]}, undetermined {tot[2]}")
    print()
    print("Cross-check of the two tools (where both are affordable):")
    for p_, s_, cap_ in CASES:
        n_ = p_ ** s_
        both, mism = cross_check(n_, p_, cap=cap_)
        print(f"  p={p_}, n={n_}: {both} values compared, {mism} mismatches")
    print(f"  [elapsed {time.time() - t0:.1f}s]")
    sys.exit(0)
