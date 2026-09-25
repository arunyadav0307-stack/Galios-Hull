import time
from fflib import GF, Poly, const, xpoly, ord_of_poly, xpow_mod, in_span, mat_rank
from fflib3 import divisors_fast
from fflib2 import code_basis, sigma_dual_basis

F4 = GF(2,2,[1,1,1])
def xnf(F,n,lam): return Poly(F,[F.neg(lam)]+[F.zero]*(n-1)+[F.one])
# hand-checkable flagship: q=4, n=3, lambda=omega (order 3); is x^3-lam irreducible?
om = (0,1)
print("omega^3 =", F4.pow(om,3), " (should be 1)")
g = xnf(F4,3,om); print("g =", g)
divs, facs = divisors_fast(F4, g)
print("factors:", facs, "orders:", [ord_of_poly(F4,h) for h in facs])
