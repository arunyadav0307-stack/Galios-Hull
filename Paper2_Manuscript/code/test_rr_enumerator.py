#!/usr/bin/env python3
"""Exhaustive internal tests for rr_enumerator.py (standard library only)."""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rr_enumerator import *

fails=[]
def check(cond,msg):
    print(('PASS ' if cond else 'FAIL ')+msg)
    if not cond: fails.append(msg)

# 1. Transfer DP = brute force = orbit convolution (small ranges)
ok=True
for M in range(1,6):
  for a in range(1,7):
    if (M+1)**a>30000: continue
    for w in (1,2):
      ok &= trace_dp_global([(a,w)],M)==one_orbit_bruteforce(a,w,M)
check(ok,'one-orbit transfer DP equals brute force for M<=5, a<=6')

ok=True
for M,orbits in [(1,[(1,1),(6,1)]),(2,[(1,1),(2,2)]),(3,[(1,1),(1,2),(2,1)]),(4,[(3,2)])]:
  ok &= trace_dp_global(orbits,M)==enumerator_by_orbit_convolution(orbits,M)
check(ok,'global transfer DP equals orbit-wise convolution')

# 2. M=1 simple-root specialisation check (F8 n=7 hull polynomial)
E=trace_dp_global([(1,1),(6,1)],1)
hull={}
for (k,e),v in E.items(): hull[e]=hull.get(e,0)+v
check(hull=={0:4,1:60,2:60,3:4},'M=1 recovers simple-root F8,n=7 hull histogram')

# 3. Theoretical mean/variance/LCD vs coefficient computation
ok=True
for M in range(1,9):
  for orbits in [[(1,1)],[(2,3)],[(3,2)],[(5,1)],[(1,2),(2,1),(4,3)],[(6,1)]]:
    E=trace_dp_global(orbits,M); em=moments_from_enumerator(E); th=theoretical_moments(orbits,M)
    ok &= em['total']==th['total'] and em['lcd']==th['lcd'] and em['mean_eta']==th['mean_eta'] and em['var_eta']==th['var_eta']
    ok &= em['cov_kappa_eta']==0
check(ok,'closed mean/variance/LCD formulas and Cov(kappa,eta)=0 for M<=8')

# 4. Symmetry c[k,e]=c[W-k,e]
ok=True
for M,orbits in [(2,[(1,1),(6,1)]),(3,[(2,2),(3,1)]),(5,[(4,2)])]:
  E=trace_dp_global(orbits,M); W=M*sum(a*w for a,w in orbits)
  ok &= all(E.get((W-k,e),0)==v for (k,e),v in E.items())
check(ok,'joint symmetry under kappa -> W-kappa')

# 5. Extremal classes: relation DP vs direct word checks, self-dual formula
ok=True
for M in range(1,7):
  for a in range(1,7):
    if (M+1)**a>30000: continue
    ec=extremal_counts([(a,1)],M)['total']
    words=list(itertools.product(range(M+1),repeat=a))
    direct={
      'lcd':sum(all(min(x,M-y)==0 for x,y in zip(w,w[1:]+w[:1])) for w in words),
      'self_orthogonal':sum(all(x+y>=M for x,y in zip(w,w[1:]+w[:1])) for w in words),
      'dual_containing':sum(all(x+y<=M for x,y in zip(w,w[1:]+w[:1])) for w in words),
      'self_dual':sum(all(x+y==M for x,y in zip(w,w[1:]+w[:1])) for w in words),
    }
    ok &= ec==direct and ec['lcd']==2 and ec['self_dual']==self_dual_count_formula(a,M)
    ok &= ec['self_orthogonal']==ec['dual_containing']
check(ok,'LCD/self-orthogonal/dual-containing/self-dual counts; LCD=2/orbit')

# 6. Target one-orbit support description
ok=True
for M in range(1,7):
  for a in range(1,7):
    if (M+1)**a>60000: continue
    ok &= one_orbit_support(a,1,M)==predicted_one_orbit_support(a,1,M)
check(ok,'target one-orbit support trapezoid holds in tested range M<=6,a<=6')

print('\nALL TESTS PASSED' if not fails else f'\n{len(fails)} FAILURES')
raise SystemExit(1 if fails else 0)
