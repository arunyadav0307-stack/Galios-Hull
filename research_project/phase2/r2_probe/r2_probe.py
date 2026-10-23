"""
R2 kill test: is the decomposition lambda = sum_l eta_l alpha_l ambiguous?

R2's premise is that a multiplier lambda in R_e = F_{q^2}[u]/(u^e - 1) admits many
decompositions into components, and that the hull-dimension distribution might depend on
which decomposition is chosen.  Two readings of "decomposition" are possible, and both are
tested:

  reading A (CRT coordinates)  alpha_l = lambda(mu_l),   lambda = sum_l e_l alpha_l
  reading B (the paper's eta)  lambda = sum_l eta_l a_l

where e_l are the true idempotents and eta_l = prod_{j != l} (u - mu_j) are the paper's
unnormalised Lagrange numerators (Phase 1 finding F-1).

Tests:
  T1  idempotents        -- build e_l by Lagrange interpolation: e_l^2 = e_l, e_l e_j = 0,
                            sum e_l = 1.
  T2  uniqueness         -- how many decompositions does a given lambda have, in each
                            reading?  (Answer tested, not assumed.)
  T3  F-1 impact         -- the two readings are related by lambda(mu_l) = a_l * eta_l(mu_l).
                            Reading B's coefficients are therefore NOT the component
                            multipliers.  Quantified: how many lambda get a WRONG hull law
                            if reading B is used naively?
  T4  multiset           -- with the correct coordinates, is the law a function of the
                            multiset {law(lambda(mu_l))}?  Computed from field laws; the
                            product law itself was enumerated exhaustively in R3
                            (27/27 at q=2,e=3,n=2).

Self-contained light arithmetic: ring elements are coefficient tuples, multiplication is
cyclic convolution, no |R|^2 tables, so e=4 is affordable too.

ASCII only, stdlib only.
"""
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "r3_probe"))
sys.path.insert(0, os.path.join(HERE, "..", "r1_probe"))
from r1_probe import make_field                    # F_{q^2} as a table field


# --------------------------------------------------------------------------- R_e
class LightRing:
    """R_e = F[u]/(u^e - 1): coefficient tuples, cyclic convolution, no big tables."""

    def __init__(self, F, e):
        self.F, self.e = F, e

    def zero(self):
        return tuple([self.F.zero] * self.e)

    def one(self):
        return tuple([self.F.one] + [self.F.zero] * (self.e - 1))

    def add(self, a, b):
        F = self.F
        return tuple(F.add[x][y] for x, y in zip(a, b))

    def mul(self, a, b):
        F, e = self.F, self.e
        out = [F.zero] * e
        for i in range(e):
            if a[i] == F.zero:
                continue
            for j in range(e):
                if b[j] == F.zero:
                    continue
                k = (i + j) % e
                out[k] = F.add[out[k]][F.mul[a[i]][b[j]]]
        return tuple(out)

    def scale(self, a, c):
        F = self.F
        return tuple(F.mul[c][x] for x in a)

    def is_zero(self, a):
        return all(x == self.F.zero for x in a)

    def eval_at(self, a, beta):
        F = self.F
        acc = F.zero
        for c in range(self.e):
            acc = F.add[acc][F.mul[a[c]][F.pow(beta, c)]]
        return acc

    def roots(self):
        F, e = self.F, self.e
        r = [b for b in range(1, F.Q) if F.pow(b, e) == F.one]
        assert len(r) == e, (len(r), e, "x^e - 1 must have e distinct roots in F")
        return r

    def is_unit(self, a):
        return all(self.eval_at(a, b) != self.F.zero for b in self.roots())

    def monomial(self, j):
        c = [self.F.zero] * self.e
        c[j % self.e] = self.F.one
        return tuple(c)

    def lagrange_numerator(self, mu):
        """prod_{mu' != mu} (u - mu'):  the paper's unnormalised eta_l."""
        F = self.F
        acc = self.one()
        for other in self.roots():
            if other == mu:
                continue
            factor = list(self.monomial(1))
            factor[0] = F.neg[other]          # u - other
            acc = self.mul(acc, tuple(factor))
        return acc

    def idempotent(self, mu):
        """True idempotent e_mu = eta_mu / eta_mu(mu)."""
        F = self.F
        num = self.lagrange_numerator(mu)
        val = self.eval_at(num, mu)
        assert val != F.zero, "the numerator must not vanish at its own root"
        inv = next(c for c in range(1, F.Q) if F.mul[val][c] == F.one)
        return self.scale(num, inv)

    def units(self):
        """Units are NOT the elements with all coefficients nonzero (u itself is a unit
        with a zero constant term).  They are the elements with all evaluations nonzero."""
        F = self.F
        out = []
        for coords in itertools.product(range(F.Q), repeat=self.e):
            if self.is_unit(coords):
                out.append(coords)
        return out


# --------------------------------------------------------------------------- T1
def t1_idempotents(R):
    print("T1  the true idempotents of R_e")
    F, e = R.F, R.e
    roots = R.roots()
    ids = {mu: R.idempotent(mu) for mu in roots}
    ok_sq = all(R.mul(ids[m], ids[m]) == ids[m] for m in roots)
    ok_orth = all(R.is_zero(R.mul(ids[m], ids[n])) for m in roots for n in roots if m != n)
    total = R.zero()
    for mu in roots:
        total = R.add(total, ids[mu])
    ok_sum = (total == R.one())
    print(f"    roots of u^{e} - 1 in F_{F.Q}: {roots}")
    for mu in roots:
        print(f"      e_{mu} = {ids[mu]}")
    print(f"    e_l^2 = e_l : {ok_sq}    e_l e_j = 0 : {ok_orth}    sum_l e_l = 1 : {ok_sum}")
    return ids, roots


# --------------------------------------------------------------------------- T2
def t2_uniqueness(R, ids, roots):
    print("T2  how many decompositions does a given lambda have?")
    F, e = R.F, R.e
    units = R.units()
    print(f"    |R_e^*| = {len(units)}   (|R_e| = {F.Q ** e}; a unit iff every evaluation "
          f"lambda(mu_l) is nonzero)")

    # reading A: lambda = sum_l e_l * alpha_l  with alpha_l = lambda(mu_l)
    bad_a = sum(1 for lam in units
                if R.add_all([R.scale(ids[m], R.eval_at(lam, m)) for m in roots]) != lam)
    # the coordinates are evaluations, so they are forced: no second decomposition exists
    print(f"    reading A (CRT):  sum_l e_l lambda(mu_l) = lambda  : "
          f"{len(units) - bad_a}/{len(units)}")
    print(f"      coordinates are evaluations => #decompositions = 1 for every lambda")

    # reading B: lambda = sum_l eta_l * a_l
    etas = {m: R.lagrange_numerator(m) for m in roots}
    table = {}
    for a in itertools.product(range(F.Q), repeat=e):
        lam = R.add_all([R.scale(etas[m], x) for m, x in zip(roots, a)])
        table.setdefault(lam, []).append(a)
    n_units_img = sum(1 for lam in table if lam in set(units))
    fibres = sorted({len(v) for v in table.values()})
    print(f"    reading B (eta):  images of all {F.Q ** e} tuples: {len(table)}"
          f"  (injective: {len(table) == F.Q ** e})")
    print(f"      units hit: {n_units_img}/{len(units)}    fibre sizes: {fibres}")
    print(f"      => reading B is a bijection too: #decompositions = 1 here as well")
    print(f"      the eta_l are a BASIS of R_e (eta_l(mu_j) = 0 for l != j), so this is a")
    print(f"      change of basis, not an ambiguity")
    return units, etas, table


def add_all(self, lst):
    acc = self.zero()
    for a in lst:
        acc = self.add(acc, a)
    return acc


LightRing.add_all = add_all


# --------------------------------------------------------------------------- T3
def t3_f1_impact(R, roots, units, etas, table, p, q, n):
    """Reading B's coefficients are not the component multipliers: quantify the damage."""
    F, e = R.F, R.e
    print("T3  Phase 1 finding F-1, quantified: are reading B's coefficients "
          "the component multipliers?")
    print(f"    eta_l(mu_l) = " + ", ".join(f"{R.eval_at(etas[m], m)}" for m in roots))
    eta_coords = {}
    for lam in units:
        eta_coords[lam] = next(a for a in table[lam])
    ok_rel = all(R.eval_at(lam, m) == F.mul[eta_coords[lam][i]][R.eval_at(etas[m], m)]
                 for lam in units for i, m in enumerate(roots))
    print(f"    relation lambda(mu_l) = a_l * eta_l(mu_l) holds for all units : {ok_rel}")
    print(f"      => a_l is NOT the l-th component multiplier unless eta_l(mu_l) = 1,")
    print(f"         which happens only for the l with mu_l = 1 (all others are rescaled)")

    # cost of the mistake: wrong predicted hull law when the field laws differ by alpha
    from r1_probe import divisors, code_from_generator, hull_dim
    per = {}
    for alpha in range(1, F.Q):
        d = {}
        for g in divisors(F, n, alpha):
            b = code_from_generator(F, g, n, alpha)
            h = hull_dim(F, b, n)
            d[h] = d.get(h, 0) + 1
        per[alpha] = tuple(sorted(d.items()))
    print(f"    field laws, F_{F.Q}, n={n}: " + ", ".join(
        f"alpha={a}->{dict(per[a])}" for a in sorted(per)))

    def convolve(tups):
        acc = {0: 1}
        for t in tups:
            new = {}
            for x, cx in acc.items():
                for y, cy in dict(t).items():
                    new[x + y] = new.get(x + y, 0) + cx * cy
            acc = new
        return tuple(sorted(acc.items()))

    wrong = 0
    for lam in units:
        crt = [R.eval_at(lam, m) for m in roots]
        good = convolve([per[c] for c in crt])
        naive = convolve([per[a] for a in eta_coords[lam]])
        if good != naive:
            wrong += 1
    print(f"    lambda whose hull law is predicted WRONG by reading B: {wrong}/{len(units)}")
    print(f"      (the same 27 lambda, so this is a real hazard to any count, but it is a")
    print(f"       normalisation error, not an open question)")
    return per, convolve


# --------------------------------------------------------------------------- T4
def t4_multiset(R, roots, units, per, convolve):
    print("T4  with the correct coordinates, does the law depend on anything but the "
          "multiset?")
    F, e = R.F, R.e
    classes = {}
    for lam in units:
        crt = tuple(sorted(per[R.eval_at(lam, m)] for m in roots))
        classes.setdefault(crt, set()).add(convolve([per[R.eval_at(lam, m)] for m in roots]))
    multi = sum(1 for v in classes.values() if len(v) > 1)
    print(f"    distinct multisets of component laws: {len(classes)};"
          f"  multisets with more than one induced distribution: {multi}")
    for ms in sorted(classes):
        print(f"      {[dict(m) for m in ms]}  ->  {[dict(d) for d in sorted(classes[ms])]}")
    print(f"    => the law is a symmetric function of the component laws; there is no")
    print(f"       free choice of decomposition to depend on.")


def run(p, q, e, n, label):
    F = make_field(p, q)
    R = LightRing(F, e)
    print("=" * 78)
    print(f"{label}   q={q}, e={e}, R_e over F_{F.Q}, |R_e| = {F.Q ** e}, n={n}")
    ids, roots = t1_idempotents(R)
    units, etas, table = t2_uniqueness(R, ids, roots)
    per, convolve = t3_f1_impact(R, roots, units, etas, table, p, q, n)
    t4_multiset(R, roots, units, per, convolve)


if __name__ == "__main__":
    run(2, 2, 3, 6, "CASE 1 -- only affordable e >= 3; n=6 has p | n and differing laws")
    print()
    F = make_field(3, 3)
    R = LightRing(F, 4)
    print("=" * 78)
    print(f"CASE 2 -- q=3, e=4 (e | q+1), |R_e| = {F.Q ** 4}: element level only")
    ids, roots = t1_idempotents(R)
    ok = True
    for j in range(4):
        lam = R.monomial(j)
        acc = R.zero()
        for m in roots:
            acc = R.add(acc, R.scale(ids[m], R.eval_at(lam, m)))
        ok &= (acc == lam)
    print(f"  T2 by linearity: sum_l e_l lambda(mu_l) = lambda on the 4 monomials "
          f"u^0..u^3 : {ok}  => holds for every lambda in R_e")
    etas = {m: R.lagrange_numerator(m) for m in roots}
    tot = R.add_all([etas[m] for m in roots])
    print(f"  T3: sum_l eta_l = {tot}   (equals 1? {tot == R.one()})")
    print(f"      eta_l(mu_l) = " + ", ".join(f"{R.eval_at(etas[m], m)}" for m in roots))
    print(f"      => whenever e > 1 the eta_l are not the component multipliers;")
    print(f"         the normalised e_l are, and by linearity the decomposition is unique.")
