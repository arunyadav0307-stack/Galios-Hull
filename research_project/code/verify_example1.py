"""Verify Example 1 of S1: the six displayed primitive idempotents of
A1 = F_2[x1,x2]/<x1^5+x1^4+1, x2^4+x2^2+x2> are idempotent, pairwise
orthogonal, and sum to 1."""
import re
# reductions: x1^5 = x1^4 + 1  (char 2);  x2^4 = x2^2 + x2
def norm(d):
    changed = True
    while changed:
        changed = False
        for (i, j) in list(d):
            if j >= 4:
                c = d.pop((i, j))
                d[(i, j-2)] = d.get((i, j-2), 0) ^ c
                d[(i, j-3)] = d.get((i, j-3), 0) ^ c
                changed = True
        for (i, j) in list(d):
            if i >= 5:
                c = d.pop((i, j))
                d[(i-1, j)] = d.get((i-1, j), 0) ^ c
                d[(i-5, j)] = d.get((i-5, j), 0) ^ c
                changed = True
    return {k: v for k, v in d.items() if v}
def dmul(A, B):
    r = {}
    for (i1, j1), c1 in A.items():
        for (i2, j2), c2 in B.items():
            k = (i1+i2, j1+j2); r[k] = r.get(k, 0) ^ (c1 & c2)
    return norm(r)
def padd(A, B):
    r = dict(A)
    for k, v in B.items(): r[k] = r.get(k, 0) ^ v
    return {k: v for k, v in r.items() if v}
def parse(s):
    d = {}
    for term in s.split('+'):
        i = j = 0
        m = re.search(r'x1(?:\^(\d+))?', term); i = int(m.group(1)) if m and m.group(1) else (1 if m else 0)
        m = re.search(r'x2(?:\^(\d+))?', term); j = int(m.group(1)) if m and m.group(1) else (1 if m else 0)
        d[(i, j)] = 1
    return norm(d)
S = [
 "x1^4x2^3+x1^3x2^3+x1^4x2+x1^2x2^3+x1^4+x1^3x2+x1^3+x1^2x2+x2^3+x1^2+x2+1",
 "x1^4x2^3+x1^3x2^3+x1^4x2+x1^2x2^3+x1^3x2+x1^2x2+x2^3+x2",
 "x1^4x2^3+x1^3x2^3+x1^4x2+x1^2x2^3+x1^4+x1^3x2+x1^3+x1^2x2+x1^2",
 "x1^4x2^3+x1^3x2^3+x1^3x2^2+x1^2x2^3+x1^3x2+x1^2x2+x1x2+x2^2",
 "x1^4x2^3+x1^4x2^2+x1^3x2^3+x1^2x2^3+x1^2x2+x1x2^2+x1x2+x2",
 "x1^4x2^3+x1^4x2^2+x1^3x2^3+x1^4x2+x1^3x2^2+x1^2x2^3+x1^2x2+x1x2^2+x2^2+x2",
]
E = [parse(s) for s in S]
print("parsed:", len(E))
print("e_i^2 == e_i       :", [dmul(e, e) == e for e in E])
print("e_i e_j == 0 (i!=j):", [all(dmul(E[i], E[j]) == {} for j in range(6) if j != i) for i in range(6)])
s = {}
for e in E: s = padd(s, e)
print("sum e_i == 1       :", s == {(0, 0): 1})
