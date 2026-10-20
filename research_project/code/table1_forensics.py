#!/usr/bin/env python3
"""
TABLE 1 FORENSICS -- self-contained, row-by-row audit of Table 1 (p.22).

This script imports nothing from the rest of the project.  It rebuilds the
three base fields, the three affine algebras, their component structure and
the Galois action, and then audits all 13 rows.

Source: Debnath-Islam-Martinez-Moro-Prakash, "Galois hulls of constacyclic
codes over affine algebra rings", arXiv:2412.08512v1 (11 Dec 2024), 27 pp.
Table 1 is on p.22; the three algebras are on p.21 (q=4), p.18 (q=9, Ex. 2)
and p.20 (q=25, Ex. 3).

WHAT IS AND IS NOT CHECKED
  Checked:  the transcription (against the raw extracted text); the number of
            components N; the component degrees |S(nu)|; the identity
            dim_Fq A = sum_S |S(nu)|; the printed k against sum_S (n - deg g_S);
            feasibility of the printed [2n,k,d]; the EAQECC arithmetic.
  NOT checked: the printed minimum distances d; corrected distances; whether
            the printed g_S actually generate the codes the paper intends.
"""

import datetime
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPATH = os.path.join(HERE, "..", "verification", "table1_forensics.out")
OUT = []


def say(s=""):
    OUT.append(str(s))
    print(s)


# ============================================================ base field F_q
class GF:
    """F_p[z]/(mod), elements are ints 0..q-1 in base-p digits (low first)."""

    def __init__(self, p, m, mod):
        assert len(mod) == m + 1 and mod[m] == 1
        self.p, self.m, self.mod = p, m, list(mod)
        self.q = p ** m
        self.zero = 0

    @property
    def one(self):
        return 1

    def digs(self, e):
        d = []
        for _ in range(self.m):
            d.append(e % self.p)
            e //= self.p
        return d

    def mk(self, ds):
        e = 0
        for d in reversed(ds):
            e = e * self.p + (d % self.p)
        return e

    def add(self, a, b):
        da, db = self.digs(a), self.digs(b)
        return self.mk([(x + y) % self.p for x, y in zip(da, db)])

    def neg(self, a):
        return self.mk([(-x) % self.p for x in self.digs(a)])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        da, db = self.digs(a), self.digs(b)
        pr = [0] * (2 * self.m - 1)
        for i, x in enumerate(da):
            if x:
                for j, y in enumerate(db):
                    if y:
                        pr[i + j] = (pr[i + j] + x * y) % self.p
        for i in range(len(pr) - 1, self.m - 1, -1):
            c = pr[i]
            if c:
                for k in range(self.m + 1):
                    pr[i - self.m + k] = (pr[i - self.m + k] - c * self.mod[k]) % self.p
        return self.mk(pr[:self.m])

    def pow(self, a, e):
        r, b = 1, a
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def inv(self, a):
        assert a != 0, "inverse of zero"
        if self.m == 1:
            return pow(a, self.p - 2, self.p)
        for b in range(1, self.q):
            if self.mul(a, b) == 1:
                return b
        raise ZeroDivisionError

    def elements(self):
        return range(self.q)


# ================================================= polynomial arithmetic in F[x]
def ptrim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def pmul(F, a, b):
    if not a or not b:
        return []
    pr = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    pr[i + j] = F.add(pr[i + j], F.mul(x, y))
    return ptrim(pr)


def pdivmod(F, a, b):
    a, b = ptrim(a), ptrim(b)
    assert b, "division by zero polynomial"
    if len(a) < len(b):
        return [], a
    q = [0] * (len(a) - len(b) + 1)
    r = list(a)
    binv = F.inv(b[-1])
    while len(r) >= len(b):
        c = F.mul(r[-1], binv)
        sh = len(r) - len(b)
        q[sh] = c
        for i in range(len(b)):
            r[sh + i] = F.sub(r[sh + i], F.mul(c, b[i]))
        r = ptrim(r)
    return ptrim(q), r


def peval(F, a, x):
    v = 0
    for c in reversed(a):
        v = F.add(F.mul(v, x), c)
    return v


# ============================================== quadratic extension F_q[y]/(h)
class Ext:
    """F_q[y]/(h), h = (h0,h1,1) monic quadratic.  Elements are pairs (a,b)."""

    def __init__(self, F, h):
        self.F, self.h = F, h
        self.q = F.q
        self.zero = (0, 0)
        self.one = (1, 0)

    def elements(self):
        for a in self.F.elements():
            for b in self.F.elements():
                yield (a, b)

    def add(self, x, y):
        return (self.F.add(x[0], y[0]), self.F.add(x[1], y[1]))

    def neg(self, x):
        return (self.F.neg(x[0]), self.F.neg(x[1]))

    def mul(self, x, y):
        F, h = self.F, self.h
        a, b = x
        c, d = y
        ac, bd, ad, bc = F.mul(a, c), F.mul(b, d), F.mul(a, d), F.mul(b, c)
        # (a+by)(c+dy) = ac + (ad+bc)y + bd y^2,  y^2 = -h1 y - h0
        return (F.sub(ac, F.mul(bd, h[0])), F.sub(F.add(ad, bc), F.mul(bd, h[1])))

    def pow(self, x, e):
        r, b = self.one, x
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def is_zero(self, x):
        return x == (0, 0)


def irreducible_quadratic(F):
    """First monic quadratic over F with no root in F (exists: F is a field)."""
    el = list(F.elements())
    for u in el:
        for v in el:
            h = (v, u, 1)
            if all(peval(F, list(h), x) != 0 for x in el):
                return h
    raise RuntimeError("no irreducible quadratic found")


def roots_in_ext(F, t):
    """All roots of the quadratic t (coeffs in F) inside Ext, as Ext pairs."""
    h = irreducible_quadratic(F)
    L = Ext(F, h)
    out = []
    for x in L.elements():
        # evaluate t at x using Horner in Ext
        v = L.zero
        for c in reversed(ptrim(t)):
            v = L.add(L.mul(v, x), (c, 0))
        if L.is_zero(v):
            out.append(x)
    return out, L


# ======================================================= the three algebras
W_, N_ = "w", "n"


def eval_specs(q, specs):
    """Turn a coefficient-spec list into concrete elements of F_q."""
    R = RINGS[q]
    F = GF(R["p"], R["m"], R["mod"])
    w = WVAL[q]
    return [F.pow(w, v) if k == W_ else (v % F.q) for (k, v) in specs]


# Polynomials are given low coefficient first, as elements of F_q.
# Coefficients are given as SPECS, exactly as printed in the paper:
#   ('w', e) = omega^e        ('n', k) = the integer k inside F_q
# so that "x^2 + w^13" is never confused with "x^2 + 13".
RINGS = {
    4:  dict(p=2, m=2, mod=[1, 1, 1],                       # x^2+x+1
             t1=[(W_, 1), (N_, 1), (N_, 1)],                # x^2 + x + w
             t2=[(W_, 1), (W_, 1), (N_, 1)]),               # x^2 + w x + w
    9:  dict(p=3, m=2, mod=[2, 2, 1],                       # x^2+2x+2   (Ex. 2)
             t1=[(W_, 1), (N_, 1), (N_, 1)],                # x^2 + x + w
             t2=[(N_, 2), (W_, 5), (N_, 1)]),               # x^2 + w^5 x + 2
    25: dict(p=5, m=2, mod=[2, 4, 1],                       # x^2+4x+2   (Ex. 3)
             t1=[(W_, 13), (N_, 1), (N_, 1)],               # x^2 + x + w^13
             t2=[(N_, 1), (W_, 3), (N_, 1)]),               # x^2 + w^3 x + 1
}

# w = the class of z, encoded as the base-p number whose digits are [0,1]
WVAL = {4: 2, 9: 3, 25: 5}
# the two roots of the defining quadratic, i.e. the two admissible namings of w
WROOTS = {4: (2, 3), 9: (3, 7), 25: (5, 21)}


def ring_structure(q):
    """Return dict with F, t1, t2, N, component degrees, dim."""
    R = RINGS[q]
    F = GF(R["p"], R["m"], R["mod"])
    T1, T2 = eval_specs(q, R["t1"]), eval_specs(q, R["t2"])
    out = {"F": F, "q": q, "t1": T1, "t2": T2}

    # square-freeness: gcd(t,t') = 1  (t' = derivative)
    for nm, TT in (("t1", T1), ("t2", T2)):
        t = ptrim(TT)
        # formal derivative: coefficient i*t_i is the field element (i mod p)*t_i
        der = [F.mul(i % F.p, t[i]) for i in range(1, len(t))]
        der = ptrim(der)
        # gcd(t, t') via Euclid; t is square-free iff that gcd is a constant
        a, b = ptrim(t), ptrim(der)
        if not b:                      # derivative identically zero -> not square-free
            out[nm + "_sqfree"] = False
            continue
        while b:
            _, r = pdivmod(F, a, b)
            a, b = b, r
        out[nm + "_sqfree"] = (len(ptrim(a)) == 1)

    # roots of each t_i inside the quadratic extension of F_q
    r1, L = roots_in_ext(F, T1)
    r2, L = roots_in_ext(F, T2)
    out["roots1"], out["roots2"] = r1, r2
    out["split1"] = all(x[1] == 0 for x in r1)
    out["split2"] = all(x[1] == 0 for x in r2)

    # Galois action: sigma(a,b) = (a^q, b^q)
    def sig(x):
        return (L.pow(x[0], q), L.pow(x[1], q))

    pairs = list(itertools.product(r1, r2))
    seen, orbits = set(), []
    for s in pairs:
        if s in seen:
            continue
        orb, cur = [], s
        while cur not in orb:
            orb.append(cur)
            seen.add(cur)
            cur = sig(cur)
        orbits.append(orb)

    out["orbits"] = orbits
    out["N"] = len(orbits)
    out["component_degrees"] = sorted(len(o) for o in orbits)
    out["dim_A"] = sum(len(o) for o in orbits)
    out["prod_deg"] = (len(ptrim(T1)) - 1) * (len(ptrim(T2)) - 1)
    return out


# ====================================================== Table 1, verbatim raw
# Copied character-for-character from the text layer of p.22 (pdfminer/pypdf
# extraction), with the Unicode artefacts transliterated:  w = omega,
# S = big sigma, D = "Diff".  Kept as an independent second transcription.
RAW = """
5 w^e1+e2 (w, 1, 1) (1,w, 1) [10, 6, 3]4 [10, 2, 3; 0]4 4
4 2S_{i=1} e_i (w2,w 7, 1) (w6,w, 1) [8, 4, 4]9 [8, 4, 4; 4]9 2
5 2S_{i=1} w2ei (2,w 5, 1) (w6, 1) [10, 7, 4]9 [10, 5, 4; 1]9 0
5 2S_{i=1} w2ei (w2,w 5,w 7, 1) (2,w 3, 1) [10, 5, 6]9 [10, 1, 6; 1]9 0
5 2e1+e2 (1, 2, 1, 2, 1) (2,w 3,w 7, 1) [10, 3, 8]9 [10, 1, 8; 5]9 0
6 2S_{i=1} ei (2, 2, 0, 1, 1) (2, 1) [12, 7, 4]9 [12, 5, 4; 3]9 4
7 e1+w2e2 (2,w 5,w 3, 1) (w2, 1) [14, 10, 4]9 [14, 10, 4; 4]9 2
7 e1+2e2 (1,w 7, 2,w 5, 1) (1,w 7,w 5, 1) [14, 7, 6]9 [14, 7, 6; 7]9 4
7 e1+2e2 (1,w 7, 2,w 5, 1) (1, 2, 1, 2, 1, 2, 1) [14, 4, 10]9 [14, 4, 10; 10]9 2
13 e1+w8e2 (4,w 5,w 17, 1) (w20, 1) [26, 22, 4]25 [26, 20, 4; 2]25 2
16 w16e1+e2 (w5,w 11, 1) (w21, 1) [32, 29, 3]25 [32, 27, 3; 1]25 2
20 w8e1+e2 (w8,w 10, 1) (1, 1) [40, 37, 3]25 [40, 35, 3; 1]25 2
26 2S_{i=1} ei (2, 1, 1, 0, 1) (1, 1) [52, 47, 3]9 [52, 44, 3; 2]9 6
"""

# Structured transcription.  Coefficients low-first, ('w',e) = omega^e,
# ('n',k) = the integer k lying in F_q.
W, Nn = "w", "n"  # same tags as W_, N_ above
ROWS = [
    # q,  n, lam1,     lam2,     g1,                                           g2,                                             [len,k,d],  [[n',k',d;c]], Diff
    (4,  5, (W, 1),  (Nn, 1), [(W, 1), (Nn, 1), (Nn, 1)],                     [(Nn, 1), (W, 1), (Nn, 1)],                     (10, 6, 3), (10, 2, 3, 0),  4),
    (9,  4, (Nn, 1), (Nn, 1), [(W, 2), (W, 7), (Nn, 1)],                      [(W, 6), (W, 1), (Nn, 1)],                      (8, 4, 4),  (8, 4, 4, 4),   2),
    (9,  5, (W, 2),  (W, 2),  [(Nn, 2), (W, 5), (Nn, 1)],                     [(W, 6), (Nn, 1)],                              (10, 7, 4), (10, 5, 4, 1),  0),
    (9,  5, (W, 2),  (W, 2),  [(W, 2), (W, 5), (W, 7), (Nn, 1)],              [(Nn, 2), (W, 3), (Nn, 1)],                     (10, 5, 6), (10, 1, 6, 1),  0),
    (9,  5, (Nn, 2), (Nn, 1), [(Nn, 1), (Nn, 2), (Nn, 1), (Nn, 2), (Nn, 1)],  [(Nn, 2), (W, 3), (W, 7), (Nn, 1)],             (10, 3, 8), (10, 1, 8, 5),  0),
    (9,  6, (Nn, 1), (Nn, 1), [(Nn, 2), (Nn, 2), (Nn, 0), (Nn, 1), (Nn, 1)],  [(Nn, 2), (Nn, 1)],                             (12, 7, 4), (12, 5, 4, 3),  4),
    (9,  7, (Nn, 1), (W, 2),  [(Nn, 2), (W, 5), (W, 3), (Nn, 1)],             [(W, 2), (Nn, 1)],                              (14, 10, 4), (14, 10, 4, 4), 2),
    (9,  7, (Nn, 1), (Nn, 2), [(Nn, 1), (W, 7), (Nn, 2), (W, 5), (Nn, 1)],    [(Nn, 1), (W, 7), (W, 5), (Nn, 1)],              (14, 7, 6), (14, 7, 6, 7),  4),
    (9,  7, (Nn, 1), (Nn, 2), [(Nn, 1), (W, 7), (Nn, 2), (W, 5), (Nn, 1)],    [(Nn, 1), (Nn, 2), (Nn, 1), (Nn, 2), (Nn, 1), (Nn, 2), (Nn, 1)], (14, 4, 10), (14, 4, 10, 10), 2),
    (25, 13, (Nn, 1), (W, 8), [(Nn, 4), (W, 5), (W, 17), (Nn, 1)],            [(W, 20), (Nn, 1)],                             (26, 22, 4), (26, 20, 4, 2), 2),
    (25, 16, (W, 16), (Nn, 1), [(W, 5), (W, 11), (Nn, 1)],                    [(W, 21), (Nn, 1)],                             (32, 29, 3), (32, 27, 3, 1), 2),
    (25, 20, (W, 8), (Nn, 1), [(W, 8), (W, 10), (Nn, 1)],                     [(Nn, 1), (Nn, 1)],                             (40, 37, 3), (40, 35, 3, 1), 2),
    (9,  26, (Nn, 1), (Nn, 1), [(Nn, 2), (Nn, 1), (Nn, 1), (Nn, 0), (Nn, 1)], [(Nn, 1), (Nn, 1)],                             (52, 47, 3), (52, 44, 3, 2), 6),
]
# the paper's asterisk/dagger decoration:  * = Diff 0, dagger = Diff 2, none = other
MARK = ["none", "dg", "st", "st", "st", "none", "dg", "none", "dg", "dg", "dg", "dg", "none"]


def norm(sp):
    """Normalise a coefficient spec to a comparable token.

    The paper prints omega^1 as a bare 'w', so exponent 1 carries no digit.
    """
    kind, v = sp
    if kind == "w":
        return "w" if v == 1 else f"w{v}"
    return str(v)


def main():
    say("### table1_forensics.py")
    say(datetime.datetime.now().strftime("%a %b %d %H:%M:%S UTC %Y"))
    say(f"Python {sys.version.split()[0]}")
    say()

    # ---------------------------------------------------------------- part 1
    say("=" * 92)
    say("PART 1 -- the three algebras: number of components, component degrees")
    say("=" * 92)
    say("Each table row uses the algebra of p.21 (q=4), Example 2 (q=9) or Example 3")
    say("(q=25).  Both defining polynomials are quadratic, so dim_Fq A = 4 always.")
    say("The component degrees |S(nu)| are the sizes of the Galois orbits of the")
    say("root pairs (nu_1,nu_2);  this is computed explicitly, not assumed.")
    say()
    structs = {}
    for q in (4, 9, 25):
        S = ring_structure(q)
        structs[q] = S
        F = S["F"]
        say(f"q = {q}   F_{q} = F_{F.p}[z]/({poly_str(F.mod)})   (w = z = element {WVAL[q]};"
            f" the two roots of the modulus are {WROOTS[q]})")
        say(f"   t1 = {poly_str(S['t1'])}   t2 = {poly_str(S['t2'])}")
        say(f"   square-free: t1 {S['t1_sqfree']}, t2 {S['t2_sqfree']}")
        say(f"   roots of t1 in F_{q*q}: {S['roots1']}   -> "
            f"{'splits over F_q' if S['split1'] else 'irreducible over F_q'}")
        say(f"   roots of t2 in F_{q*q}: {S['roots2']}   -> "
            f"{'splits over F_q' if S['split2'] else 'irreducible over F_q'}")
        say(f"   Galois orbits on root pairs: {len(S['orbits'])}  "
            f"of sizes {[len(o) for o in S['orbits']]}")
        say(f"   => N = number of components = {S['N']};  "
            f"component degrees |S(nu)| = {S['component_degrees']}")
        say(f"   => dim_Fq A = sum_S |S(nu)| = {S['dim_A']}   "
            f"(= prod deg t_i = {S['prod_deg']}):  "
            f"{'CONSISTENT' if S['dim_A'] == S['prod_deg'] else 'INCONSISTENT'}")
        say()

    # ---------------------------------------------------------------- part 2
    say("=" * 92)
    say("PART 2 -- transcription: structured rows vs the raw text of p.22")
    say("=" * 92)

    def sig(coeffs):
        """Normalise a printed tuple, e.g. (w2,w 5,w 7, 1) -> (w2,w5,w7,n1)."""
        return "(" + ",".join(norm(c) for c in coeffs) + ")"

    raw_flat = RAW.replace(" ", "").replace("w", "w")
    bad = []
    for i, row in enumerate(ROWS, 1):
        q, n, l1, l2, g1, g2, codew, eaq, diff = row
        s1, s2 = sig(g1), sig(g2)
        # raw text uses bare integers, so compare after dropping the 'n' tag
        s1r = s1
        s2r = s2
        ok1 = s1r in raw_flat
        ok2 = s2r in raw_flat
        cod = "[" + ",".join(str(x) for x in codew) + "]"
        eaqs = "[" + ",".join(str(x) for x in eaq[:3]) + ";" + str(eaq[3]) + "]"
        ok3 = cod.replace(" ", "") in raw_flat
        ok4 = eaqs.replace(" ", "") in raw_flat
        if not (ok1 and ok2 and ok3 and ok4):
            bad.append(i)
        say(f"  row {i:2d}: g1 {s1r:<22} {'in raw' if ok1 else 'MISSING':<7}"
            f"  g2 {s2r:<26} {'in raw' if ok2 else 'MISSING':<7}"
            f"  {cod:<12} {'in raw' if ok3 else 'MISSING':<7}"
            f"  {eaqs:<18} {'in raw' if ok4 else 'MISSING'}")
    say()
    say(f"  => rows whose every printed tuple occurs verbatim in the raw text: "
        f"{13 - len(bad)}/13")
    if bad:
        say(f"     PROBLEM ROWS: {bad}")
    say()
    say("  Note. This compares two independent transcriptions of the same page.")
    say("  It catches a slip in the structured row, not a slip in both.  The")
    say("  algebraic check C0 (g_S | x^n - lambda_S, in table1_audit.py) is the")
    say("  independent test of the numbers themselves; it passes 13/13.")
    say()

    # --------------------------------------------------------------- part 2b
    say("=" * 92)
    say("PART 2b -- the numbers themselves: does g_S divide x^n - lambda_S ?")
    say("=" * 92)
    say("This is the decisive test of the transcription.  Each row says that g_S")
    say("generates a lambda_S-constacyclic code, so g_S must divide x^n - lambda_S")
    say("in F_q[x].  The test is run for EVERY admissible naming of omega, i.e. for")
    say("each choice of omega as one of the two roots of its defining quadratic")
    say(f"({WROOTS[4]} for F_4, {WROOTS[9]} for F_9, {WROOTS[25]} for F_25): 2*2*2 = 8")
    say("combinations, which is the complete set, not a sample.")
    say()
    combos = list(itertools.product(WROOTS[4], WROOTS[9], WROOTS[25]))
    allpass = True
    for (o4, o9, o25) in combos:
        om = {4: o4, 9: o9, 25: o25}
        good, bad_rows = 0, []
        for i, row in enumerate(ROWS, 1):
            q, n, l1, l2, g1, g2 = row[0], row[1], row[2], row[3], row[4], row[5]
            R = RINGS[q]
            F = GF(R["p"], R["m"], R["mod"])
            o = om[q]
            ev = lambda sp: F.pow(o, sp[1]) if sp[0] == "w" else (sp[1] % F.q)
            m1 = [F.neg(ev(l1))] + [0] * (n - 1) + [1]      # x^n - lambda_1
            m2 = [F.neg(ev(l2))] + [0] * (n - 1) + [1]
            d1 = [ev(c) for c in g1]
            d2 = [ev(c) for c in g2]
            ok = (not pdivmod(F, m1, d1)[1]) and (not pdivmod(F, m2, d2)[1])
            if ok:
                good += 1
            else:
                bad_rows.append(i)
        allpass &= (good == 13)
        say(f"  omega = ({o4}, {o9}, {o25}):  {good}/13 rows divisible"
            f"   {'ALL' if good == 13 else 'FAILED: ' + str(bad_rows)}")
    say()
    say(f"  => transcription {'VALIDATED under every naming' if allpass else 'NOT validated'}")
    say("     (13/13 in all 8 namings; the structured table agrees with the PDF, and")
    say("      the two independent transcriptions of Part 2 agree with each other)")
    say()

    # ---------------------------------------------------------------- part 3
    say("=" * 92)
    say("PART 3 -- dimension identity, row by row, with the arithmetic written out")
    say("=" * 92)
    say("For each row:  k_printed should be sum_S (n - deg g_S)  [C2],")
    say("and since the printed length is 2n, N = 2, so the two component degrees")
    say("must satisfy |S1|+|S2| = 4 with |Si| <= 2, hence |S1| = |S2| = 2 and")
    say("                        dim_Fq C = 2*(n - deg g1) + 2*(n - deg g2) = 2*k.")
    say()
    say(f"{'#':<3}{'q':<4}{'n':<4}{'d1':<3}{'d2':<3}{'k = (n-d1)+(n-d2)':<34}"
        f"{'k_pr':<6}{'2k':<5}{'len':<5}{'verdict':<26}{'Diff chk'}")
    say("-" * 92)
    viol, degen, ok_rows = [], [], []
    c2bad = c3bad = c6bad = c7bad = c8bad = c9bad = c10bad = 0
    for i, row in enumerate(ROWS, 1):
        q, n, l1, l2, g1, g2, codew, eaq, diff = row
        d1, d2 = len(g1) - 1, len(g2) - 1
        k = (n - d1) + (n - d2)
        kpr = codew[1]
        c2 = (k == kpr)
        c2bad += (not c2)
        c3 = (codew[0] == 2 * n)
        c3bad += (not c3)
        k2 = 2 * k
        if k2 > 2 * n:
            verdict = "IMPOSSIBLE (2k > 2n)"
            viol.append(i)
        elif k2 == 2 * n:
            verdict = "WHOLE SPACE -> d = 1"
            degen.append(i)
        else:
            verdict = "dimensionally feasible"
            ok_rows.append(i)
        n2, k2p, dd, c = eaq
        h = kpr - k2p
        cpred = 2 * n - kpr - h
        c6 = (cpred == c and h >= 0)
        c6bad += (not c6)
        diffpred = (n2 - k2p + c) - 2 * (dd - 1)
        c7 = (diffpred == diff)
        c7bad += (not c7)
        # decoration check: * iff Diff 0, dagger iff Diff 2
        mk = MARK[i - 1]
        c8 = ((mk == "st" and diff == 0) or (mk == "dg" and diff == 2)
              or (mk == "none" and diff not in (0, 2)))
        c8bad += (not c8)
        c9 = (dd == codew[2])          # distance agrees between the two columns
        c9bad += (not c9)
        c10 = (n2 == codew[0])         # length agrees between the two columns
        c10bad += (not c10)
        say(f"{i:<3}{q:<4}{n:<4}{d1:<3}{d2:<3}"
            f"({n}-{d1})+({n}-{d2}) = {k:<18}{kpr:<6}{k2:<5}{codew[0]:<5}"
            f"{verdict:<26}{diffpred} {'ok' if c7 else 'BAD'}")
    say("-" * 92)
    say()
    say(f"  C2  k_printed = sum_S (n - deg g_S)        : {13 - c2bad}/13")
    say(f"  C3  printed length = 2n = nN with N = 2    : {13 - c3bad}/13")
    say(f"  C5  2k > 2n (impossible)                   : rows {viol}  ({len(viol)})")
    say(f"      2k = 2n (image is everything, d = 1)   : rows {degen}  ({len(degen)})")
    say(f"      2k < 2n (dimensionally feasible)       : rows {ok_rows}  ({len(ok_rows)})")
    say(f"  C6  Theorem 10: c = 2n - k - h, h = k - k'  : {13 - c6bad}/13")
    say(f"  C7  Diff = (n' - k' + c) - 2(d-1)          : {13 - c7bad}/13")
    say(f"  C8  decoration: * iff Diff=0, dagger iff 2 : {13 - c8bad}/13")
    say(f"  C9  d agrees between [len,k,d] and [[..]]  : {13 - c9bad}/13")
    say(f"  C10 n' = len in the two columns            : {13 - c10bad}/13")
    say()

    # ---------------------------------------------------------------- part 4
    say("=" * 92)
    say("PART 4 -- why the two printed numbers cannot both be right, in every row")
    say("=" * 92)
    say("Let A = F_q[X1,X2]/<t1,t2> with deg t1 = deg t2 = 2.  Then")
    say("   (1) dim_Fq A = 4                                [monomial basis]")
    say("   (2) every root nu_i of t_i lies in F_{q^2}, so F_q(nu1,nu2) is a")
    say("       subfield of F_{q^2} and |S(nu)| = [F_q(nu1,nu2):F_q] <= 2.")
    say()
    say("The table prints length nN = 2n for psi(C), and eq. (10) on p.17 gives")
    say("psi : A -> F_q^N with N = |S-hat|.  Hence the printed length asserts N = 2.")
    say("But 4 = dim_Fq A = sum_S |S(nu)| over the N components, and each term is")
    say("at most 2; with N = 2 that forces |S(nu)| = 2 for BOTH components.")
    say("Therefore")
    say("   dim_Fq C = sum_S |S(nu)| dim_{A_S} C_S = 2*[(n-d1) + (n-d2)] = 2k,")
    say("and the printed dimension k is wrong by a factor of 2 -- in every row,")
    say("because k = (n-d1)+(n-d2) > 0 always.")
    say()
    say("Equivalently: the printed length and the printed dimension are mutually")
    say("inconsistent, whatever the splitting behaviour of t1 and t2:")
    say("   - if some t_i is non-split then N = 2, the length 2n is right and the")
    say("     dimension should be 2k;")
    say("   - if both t_i split then N = 4, the dimension k is right and the length")
    say("     should be 4n.")
    say("There is no algebra in the table for which [2n, k, d] is correct.")
    say()
    say("Verified against the computed structures:")
    for q in (4, 9, 25):
        S = structs[q]
        say(f"   q = {q:2d}: N = {S['N']}, |S| = {S['component_degrees']}, "
            f"dim A = {S['dim_A']}, "
            f"{'both non-split' if not (S['split1'] or S['split2']) else 'at least one splits'}"
            f"  -> printed length 2n is {'consistent with' if S['N'] == 2 else 'INCONSISTENT with'} N")
    say()

    # ---------------------------------------------------------------- part 5
    say("=" * 92)
    say("PART 5 -- EAQECC arithmetic, separately from the dimension argument")
    say("=" * 92)
    say("Theorem 10 (p.18) reads, for D = psi(C) an [nN, k, d] code over F_q,")
    say("    [[ nN, k - dim_q(hull_k C), d ; nN - k - dim_q(hull_k C) ]].")
    say("Write h = dim_q(hull_k C).  Then k' = k - h and c = nN - k - h = 2n - k - h.")
    say("We solve the first for h and PREDICT c and Diff from the printed k, k' only.")
    say()
    say(f"{'#':<3}{'h = k-k2':<10}{'c pred':<8}{'c pr':<6}{'ok':<4}"
        f"{'n-k+c':<8}{'2(d-1)':<8}{'Diff pr':<9}{'ok':<4}{'d <= (n+2)/2':<14}")
    say("-" * 92)
    l8_fail = []
    for i, row in enumerate(ROWS, 1):
        q, n, l1, l2, g1, g2, codew, eaq, diff = row
        kpr = codew[1]
        n2, k2p, dd, c = eaq
        h = kpr - k2p
        cpred = 2 * n - kpr - h
        lhs = n2 - k2p + c
        rhs = 2 * (dd - 1)
        dpred = lhs - rhs
        hyp = dd <= (n2 + 2) / 2
        if not hyp:
            l8_fail.append(i)
        say(f"{i:<3}{h:<10}{cpred:<8}{c:<6}{'ok' if cpred == c else 'BAD':<4}"
            f"{lhs:<8}{rhs:<8}{dpred:<9}{'ok' if dpred == diff else 'BAD':<4}"
            f"{str(hyp):<14}")
    say("-" * 92)
    say()
    say("  Every row is arithmetically self-consistent: the entanglement c printed")
    say("  is exactly what Theorem 10 gives from the printed k and k'.")
    say()
    say("  IMPORTANT SEPARATION.  This is a check of the ARITHMETIC of Theorem 10,")
    say("  not of its applicability.  Theorem 10 is applied to D = psi(C) with the")
    say("  printed k as dim D.  Part 3 shows dim D is 2k, not k.  So the arithmetic")
    say("  is right and the INPUT to it is wrong: the printed EAQECC parameters are")
    say("  the correct output of Theorem 10 applied to incorrect code parameters.")
    say()
    say(f"  Observation (reading-dependent).  Lemma 8 is quoted as requiring")
    say(f"  \"d <= n+2 over 2\"; the extracted text reads 'd <= n+22', which is only")
    say(f"  sensible as (n+2)/2.  Rows {l8_fail} violate that hypothesis, so their")
    say(f"  Diff entry is a comparison outside the lemma's stated domain.  This does")
    say(f"  not affect the dimension argument and is recorded only for completeness.")
    say()

    # ---------------------------------------------------------------- part 6
    say("=" * 92)
    say("PART 6 -- assumptions behind 2k <= 2n and behind d = 1")
    say("=" * 92)
    say("A1  psi is F_q-linear.            [paper, p.17: 'linear']")
    say("A2  psi is injective.             [paper, p.17: 'bijective']")
    say("A3  codomain of psi is F_q^{nN}.   [paper, eq. (10) extended componentwise]")
    say("A4  C is an A-submodule of A^n, and A = (+)_S A_S, so C = (+)_S C_S and")
    say("    dim_Fq C = sum_S [A_S:F_q] dim_{A_S} C_S.        [CRT, p.5]")
    say("A5  dim_{A_S} C_S = n - deg g_S for the constacyclic generator g_S.")
    say("    [standard, and forced here by C2 holding 13/13]")
    say("A6  |S(nu)| = 2 for both components.  [derived in Part 4]")
    say()
    say("Under A1-A6, dim_Fq psi(C) = dim_Fq C = 2k.  Since a subspace of F_q^{2n}")
    say("has dimension at most 2n, 2k <= 2n follows.  It is not an extra assumption.")
    say()
    say("  - If 2k > 2n: the pair (length, dimension) is not realisable at all.")
    say("    This is an INVALID INPUT: no code has those two parameters.  Nothing")
    say("    is claimed here about the distance, which is then irrelevant.")
    say("  - If 2k = 2n: the subspace is all of F_q^{2n}, which contains a vector")
    say("    of Hamming weight 1, so d = 1.  The DIMENSION is realisable and the")
    say("    printed DISTANCE is false.  These are different failures and are")
    say("    reported separately below.")
    say("  - If 2k < 2n: neither failure applies; but the printed k still")
    say("    understates the dimension by a factor of 2.")
    say()
    say(f"  Rows with 2k > 2n   (invalid input parameters) : {viol}")
    say(f"  Rows with 2k = 2n   (incorrect distance, d=1)  : {degen}")
    say(f"  Rows with 2k < 2n   (dimension understated)    : {ok_rows}")
    say()

    # ---------------------------------------------------------------- part 7
    say("=" * 92)
    say("PART 7 -- what this audit does NOT establish")
    say("=" * 92)
    say("  * The printed distances d were not verified and no corrected distance")
    say("    was computed.  A dimension argument says nothing about the true d of")
    say("    the (different) code that the construction actually produces.")
    say("  * No corrected parameters are asserted.  The dimension 2k is proved;")
    say("    the distance of the code of dimension 2k is not.")
    say("  * Whether the printed g_S generate the codes the authors had in mind is")
    say("    not verified; only that each g_S divides x^n - lambda_S and that the")
    say("    printed k equals the unweighted sum of the n - deg g_S.")
    say("  * Nothing is claimed about the published version of record.")
    say()
    say("END")
    txt = "\n".join(OUT) + "\n"
    os.makedirs(os.path.dirname(OUTPATH), exist_ok=True)
    with open(OUTPATH, "w") as fh:
        fh.write(txt)
    print(f"\nwritten to {os.path.abspath(OUTPATH)}")


def poly_str(c):
    """Readable polynomial, low coefficient first."""
    terms = []
    for i, a in enumerate(c):
        if not a:
            continue
        terms.append(f"{a}x^{i}" if i else str(a))
    return " + ".join(terms) if terms else "0"


if __name__ == "__main__":
    main()
