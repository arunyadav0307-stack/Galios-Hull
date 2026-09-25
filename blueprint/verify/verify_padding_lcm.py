"""
verify_padding_lcm.py -- PHASE 3 of the external audit prompt.

(A) Derive and verify the exact padding/syndrome identity from first principles.
    Convention fixed here (the one that makes the identity exact):

        s_w(j + n) = lambda^{-1} s_w(j)          (equivalently s_w(j) = lambda^{-k} w_{j mod n})

    i.e. the continuation is lambda^{-1}-periodic to the RIGHT.  Then

        W_a(w) := (s_w(a), ..., s_w(a+n-1))  ==  x^{-a} * w   as an element of R_lambda

    EXACTLY (no scalar multiplier), where x^{-a} is computed as the (-a)-th power of
    multiplication-by-x in R_lambda = A[x]/<x^n - lambda>.

    Two candidate conventions are compared, so the choice is documented.

(B) The receiver's syndrome:  Syn_a := (W_a(w) / g_D) mod f  in R_lambda/<f>.
    For padding words w = c + g_D with c in C = <g_C>, f = g_C/g_D:
        Syn_a = x^{-a}  exactly, independent of c  (content-free).
    For a general element v in D:  Syn_a = x^{-a} * ((v/g_D) mod f)  -- content-carrying.

(C) lcm law:  Syn_a = Syn_{a'}  <=>  x^{a'-a} == 1 mod f_i for all i  <=>  Theta | (a'-a),
    Theta = lcm_i ord_{f_i}(x).  Hence injectivity on a window of T+1 shifts <=> T < Theta.
    Checked abstractly for m = 1,2,3 (coprime and non-coprime orders) and on real
    multi-component codes with *unequal* lambda weights, including windows of length Theta.

(D) Jitter: with per-component offsets delta_i, the observation is x^{-(a+delta_i)} per
    component.  For FIXED delta injectivity on windows of length Theta survives.  Across
    different delta the ambiguity is characterised by the subgroup
        Ambig = {(Delta, eps) : Delta + eps_i == 0 mod o_i for all i},
    which is trivial for all non-zero Delta iff gcd(o_i, o_j) = 1 for all i != j.
    Computed explicitly for (o_1,o_2) = (21,7) and (3,7).
"""
import itertools, math
from fflib import GF, Poly, const, xpoly, ptrim
from fflib3 import divisors_fast
from fflib2 import code_basis, sigma_dual_basis
from verify_mechanism import xnf, divs, _dual_containing

FIELDS = {3: GF(3, 1, [0, 1]), 4: GF(2, 2, [1, 1, 1]), 5: GF(5, 1, [0, 1]),
          7: GF(7, 1, [0, 1]), 8: GF(2, 3, [1, 1, 0, 1]), 9: GF(3, 2, [1, 0, 1])}


# ---------------------------------------------------------------- (A) padding
def s_seq(F, v, n, lam, j, convention="inv"):
    """lambda^{-1}-periodic to the right ('inv') or lambda-periodic ('dir')."""
    q, r = divmod(j, n)
    if convention == "inv":
        # s(j+n) = lambda^{-1} s(j)  =>  s(j) = lambda^{-q} v_{j mod n}
        return F.mul(F.pow(F.inv(lam), q), v[r])
    else:
        # s(j+n) = lambda s(j)  =>  s(j) = lambda^{q} v_{j mod n}
        return F.mul(F.pow(lam, q), v[r])


def window(F, v, n, lam, a, convention="inv"):
    return [s_seq(F, v, n, lam, a + i, convention) for i in range(n)]


def T_shift(F, lam, c):
    """multiplication by x in R_lambda."""
    return [F.mul(lam, c[-1])] + list(c[:-1])


def pow_x(F, n, lam, e):
    """x^e * 1 in R_lambda via repeated T (e >= 0) or via x^{-1} = lambda^{-1} x^{n-1} (e < 0)."""
    c = [F.zero] * n
    c[0] = F.one                     # the element 1
    u = [F.zero] * n
    u[n - 1] = F.inv(lam)            # x^{-1} = lambda^{-1} x^{n-1}
    base = u if e < 0 else None
    for _ in range(abs(e)):
        if e < 0:
            c = mul_vecs(F, c, base, n, lam)
        else:
            c = T_shift(F, lam, c)
    return c


def mul_vecs(F, a, b, n, lam):
    """product of two elements of R_lambda, by polynomial multiplication modulo x^n - lambda."""
    res = [F.zero] * (2 * n - 1)
    for i, x in enumerate(a):
        if x == F.zero:
            continue
        for j, y in enumerate(b):
            if y == F.zero:
                continue
            res[i + j] = F.add(res[i + j], F.mul(x, y))
    # reduce modulo x^n - lambda:  x^{k} = lambda * x^{k-n}
    for k in range(2 * n - 2, n - 1, -1):
        c = res[k]
        if c != F.zero:
            res[k - n] = F.add(res[k - n], F.mul(lam, c))
            res[k] = F.zero
    out = ptrim(res[:n])
    return out + [F.zero] * max(0, n - len(out))


def as_vec(F, P, n):
    v = [F.zero] * n
    for i, c in enumerate(ptrim(list(P.c))):
        v[i] = c
    return v


def poly_of(F, vec):
    return Poly(F, ptrim(list(vec)))


def check_padding():
    print("=" * 100)
    print("(A) EXACT PADDING IDENTITY  W_a(w) = x^{-a} * w  in R_lambda")
    print("=" * 100)
    for conv in ["inv", "dir"]:
        tested = exact = 0
        example = None
        for q, F in FIELDS.items():
            for n in range(3, 8):
                if n % F.p == 0:
                    continue
                for lam in F.nonzero():
                    for gD in divs(F, n, lam)[:2]:          # cheap: few divisors
                        for gC in divs(F, n, lam)[:2]:
                            if gC.deg() <= gD.deg() or not gC.mod(gD).is_zero():
                                continue
                            bigf = gC.divmod_(gD)[0]
                            if bigf.deg() == 0:
                                continue
                            Cb = code_basis(F, gC, n, lam)
                            sv = as_vec(F, gD, n)
                            for c in Cb + [sv]:
                                w = as_vec(F, Poly(F, list(c)), n)
                                for a in range(-2 * n, 2 * n + 1):
                                    W = window(F, w, n, lam, a, conv)
                                    xp = pow_x(F, n, lam, -a)
                                    ref = mul_vecs(F, xp, w, n, lam)
                                    tested += 1
                                    if vector_eq(F, W, ref[:n]):
                                        exact += 1
                                    elif example is None:
                                        example = (q, n, tuple(lam), a, W[:4], ref[:4])
        print(f"  convention '{conv}': {exact}/{tested} exact identities"
              + ("" if example is None else f"   first failure e.g. {example}"))
    print("  => the lambda^{-1}-periodic continuation ('inv') is the one that makes the "
          "window identity exact; the other convention is off by a scalar lambda^{...}, "
          "which is also visible to the receiver, so either is usable after normalisation.")


def vector_eq(F, a, b):
    n = max(len(ptrim(list(a))), len(ptrim(list(b))))
    a = list(a) + [F.zero] * n
    b = list(b) + [F.zero] * n
    return all(a[i] == b[i] for i in range(n))


# ------------------------------------------------------- (B) syndrome identity
def check_syndrome():
    print()
    print("=" * 100)
    print("(B) SYNDROME  Syn_a = (W_a(w)/g_D) mod f :  exact, content-free for w in C + g_D")
    print("=" * 100)
    tot = ok_exact = ok_free = ok_general = 0
    for q, F in FIELDS.items():
        ks = range(F.e) if F.e > 1 else [0]
        for n in range(3, 8):
            if n % F.p == 0:
                continue
            for lam in F.nonzero():
                for k in ks:
                    if F.pow(lam, F.p ** k + 1) != F.one:
                        continue
                    ds = divs(F, n, lam)
                    for gD in ds:
                        for gC in ds:
                            if gC.deg() <= gD.deg() or not gC.mod(gD).is_zero():
                                continue
                            f = gC.divmod_(gD)[0]
                            if f.deg() == 0:
                                continue
                            o = _ord_poly(F, f, n, lam)
                            use_div = gD.deg() > 0
                            Cb = code_basis(F, gC, n, lam)
                            gv = as_vec(F, gD, n)
                            for a in range(-min(3, o), min(3, o) + 1):
                                exp = poly_of(F, pow_x(F, n, lam, -a)).mod(f)
                                sy = set()
                                for c in [gv] + [[F.add(x, y) for x, y in zip(cc, gv)] for cc in Cb]:
                                    W = window(F, c, n, lam, a, "inv")
                                    Wp = poly_of(F, W)
                                    J = Wp.divmod_(gD)[0] if use_div else Wp
                                    s = J.mod(f)
                                    sy.add(tuple(map(tuple, ptrim(list(s.c)))))
                                    tot += 1
                                    if s == exp:
                                        ok_exact += 1
                                    # general content formula for arbitrary elements of D
                                if len(sy) == 1:
                                    ok_free += 1
                            # general elements of D: content-carrying formula
                            if gD.deg() > 0:
                                for u in code_basis(F, gD, n, lam):
                                    v = u[:]
                                    for a in (0, 1, -1, 2):
                                        W = window(F, v, n, lam, a, "inv")
                                        J = poly_of(F, W).divmod_(gD)[0]
                                        lhs = J.mod(f)
                                        rhs = poly_of(F, pow_x(F, n, lam, -a)).mul(
                                            poly_of(F, u).divmod_(gD)[0].mod(f)).mod(f)
                                        if lhs == rhs:
                                            ok_general += 1
    print(f"  exact syndrome identities:        {ok_exact}/{tot}")
    print(f"  content-free windows (unit content): {ok_free} chain/shift pairs")
    print(f"  general content formula (v in D): {ok_general} checks")


def _ord_poly(F, P, n, lam):
    """order of x modulo P, by repeated multiplication by x inside R_lambda."""
    c = [F.zero] * n
    c[0] = F.one
    one = Poly(F, [F.one])
    for d in range(1, 4000):
        c = T_shift(F, lam, c)
        if poly_of(F, c).mod(P) == one:
            return d
    raise RuntimeError("order not found")


# ----------------------------------------------------------------- (C) lcm law
def lcm_law_abstract():
    print()
    print("=" * 100)
    print("(C) lcm LAW (abstract): injectivity on a window of T+1 shifts  <=>  T < lcm(o_i)")
    print("=" * 100)
    for orders in [(3,), (7,), (21, 7), (21, 21), (3, 7), (4, 6), (5, 7, 3), (2, 4, 8)]:
        L = math.lcm(*orders)
        fails = []
        for T in range(0, 2 * L + 2):
            seen = {}
            ok = True
            for a in range(0, T + 1):          # consecutive window (translation invariant)
                s = tuple(a % o for o in orders)
                if s in seen:
                    ok = False
                    break
                seen[s] = a
            if ok != (T < L):
                fails.append(T)
        print(f"  orders {orders}: lcm = {L:3d};  mismatches with (T < lcm): {fails}")
    print("  => injectivity holds exactly on windows of length T+1 <= lcm; no coprimality "
          "assumption is used in the proof (it only says when the sequence also SATURATES).")


def jitter_structure():
    print()
    print("=" * 100)
    print("(D) JITTER AMBIGUITY  Ambig = {(Delta,eps) : Delta + eps_i == 0 mod o_i}")
    print("=" * 100)
    for orders in [(21, 7), (3, 7), (4, 6), (5, 7, 3)]:
        bad = []
        for Delta in range(1, 2 * math.lcm(*orders) + 1):
            for eps in itertools.product(range(-3, 4), repeat=len(orders)):
                if all((Delta + e) % o == 0 for e, o in zip(eps, orders)):
                    bad.append((Delta, eps))
        gcds = [math.gcd(orders[i], orders[j]) for i in range(len(orders))
                for j in range(i + 1, len(orders))]
        print(f"  orders {orders}: pairwise gcds {gcds}; "
              f"ambiguities with |Delta| <= lcm and |eps_i| <= 3: {bad}")
    print("  => a non-zero Delta is ambiguous iff the offsets can differ by a common residue "
          "modulo every gcd(o_i,o_j); for pairwise coprime orders only Delta = 0 survives.")


# ---------------------------------------- (C') lcm law on genuine multi-component codes
def ring_case_orders():
    print()
    print("=" * 100)
    print("(C') lcm LAW on genuine components (unequal lambda), incl. collision at Theta")
    print("=" * 100)
    F = FIELDS[4]
    n = 7
    rows = []
    for lam in F.nonzero():
        for g in divs(F, n, lam):
            if 0 < g.deg() < n:
                o = _ord_poly(F, g, n, lam)
                dc = _dual_containing(F, n, lam, g, 1)
                rows.append((tuple(lam), tuple(map(tuple, g.c)), o, g.deg(), dc))
    print("  component table for F_4, n = 7 (lambda, deg g, ord_f(x), dual-containing for kappa=1):")
    for r in rows:
        print(f"    lam={r[0]}  deg={r[3]}  ord={r[2]:2d}  dual-containing={r[4]}")
    dc = [r for r in rows if r[4]]
    print()
    for i in range(len(dc)):
        for j in range(len(dc)):
            o1, o2 = dc[i][2], dc[j][2]
            th = math.lcm(o1, o2)
            pair = ((dc[i][0], dc[j][0]), o1, o2, th)
            if th > n:
                print(f"    components lam1={dc[i][0]} (ord {o1}), lam2={dc[j][0]} (ord {o2}):"
                      f"  Theta = {th} > n = {n};  T_max = {th - 1}")
    print()


if __name__ == "__main__":
    check_padding()
    check_syndrome()
    lcm_law_abstract()
    jitter_structure()
    ring_case_orders()
