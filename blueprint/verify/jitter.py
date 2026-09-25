"""Compact jitter analysis: the (shift, jitter) parametrisation a + delta_i = theta_i is
degenerate: (a,delta) ~ (a - c, delta + c*1).  A GENUINE ambiguity needs a non-constant
epsilon with Delta + eps_i == 0 mod o_i.  Criterion: possible iff gcd(o_i,o_j) <= |eps_i-eps_j|."""
import itertools, math
def report(orders, jit):
    Th = math.lcm(*orders)
    gs = [math.gcd(orders[i], orders[j]) for i in range(len(orders)) for j in range(i+1, len(orders))]
    best = None
    for D in range(1, Th+1):
        for eps in itertools.product(range(-2*jit, 2*jit+1), repeat=len(orders)):
            if all(D+e == 0 or (D+e) % o == 0 for e, o in zip(eps, orders)):
                if len(set(eps)) > 1:          # non-constant => genuine ambiguity
                    best = (D, eps); break
        if best: break
    print(f"  orders={orders} jitter<= {jit}  gcds={gs}   Theta={Th}  "
          f"minimal genuine ambiguity Delta={best[0] if best else 'none within Theta'} "
          f"{'(eps=%s)'%str(best[1]) if best else ''}")
    if best is None:
        print("     => exact recovery of the symbol shift, robust to jitter of this size")
    else:
        print("     => a non-constant jitter vector can mimic a shift of that size "
              "(limit of the law at coordinate level)")
for orders in [(21,7),(3,7),(7,7),(5,7),(4,6),(5,7,3),(9,7),(21,35)]:
    for jit in (1,):
        report(orders, jit)
