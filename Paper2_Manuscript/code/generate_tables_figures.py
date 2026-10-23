#!/usr/bin/env python3
"""Generate all CSV tables and PNG/PDF figures quoted in the blueprint."""
import csv, json, math, os, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

from rr_enumerator import (
    enumerator_by_orbit_convolution, moments_from_enumerator,
    theoretical_moments, extremal_counts, one_orbit_bruteforce,
    _mu_edge, _a1_mean, _a1_variance,
)

TAB = os.path.join(ROOT, 'tables')
FIG = os.path.join(ROOT, 'figures')
os.makedirs(TAB, exist_ok=True); os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({'font.size': 10, 'axes.titlesize': 11, 'axes.labelsize': 10})

FAMILIES = [
    # slug, label, n', M, k, lambda0 label, lambda_n label, orbits
    ('F4_n10',       r'$\mathbb{F}_4$, $n=10$',        5, 2, 1, '1',      '1',        [(1,1),(2,2)]),
    ('F4_n10_omega', r'$\mathbb{F}_4$, $n=10$, $\lambda_0=\omega$', 5, 2, 1, 'omega', 'omega^2', [(1,1),(2,2)]),
    ('F8_n14',       r'$\mathbb{F}_8$, $n=14$',        7, 2, 1, '1',      '1',        [(1,1),(6,1)]),
    ('F3_n12',       r'$\mathbb{F}_3$, $n=12$',        4, 3, 0, '1',      '1',        [(1,1),(1,1),(1,2)]),
    ('F9_n12_i',     r'$\mathbb{F}_9$, $n=12$, $\lambda_0=i$', 4, 3, 1, 'i', '-i',     [(2,2)]),
    ('F9_n12_neg',   r'$\mathbb{F}_9$, $n=12$, $\lambda_0=-1$', 4, 3, 1, '-1','-1',    [(2,1),(2,1)]),
    ('F9_n24',       r'$\mathbb{F}_9$, $n=24$',        8, 3, 1, '1',      '1',        [(1,1)]*4+[(2,1)]*2),
    ('F25_n30',      r'$\mathbb{F}_{25}$, $n=30$',     6, 5, 1, '1',      '1',        [(1,1)]*6),
    ('F4xF16_n10',   r'$\mathbb{F}_4\times\mathbb{F}_{16}$, $n=10$', 5, 2, 1, '(1,1)','(1,1)', [(1,1),(2,2),(1,2),(4,2)]),
    ('F32_n62',      r'$\mathbb{F}_{32}$, $n=62$',     31,2, 1, '1',      '1',        [(1,1)]+[(10,1)]*3),
    ('F32_n124',     r'$\mathbb{F}_{32}$, $n=124$',    31,4, 1, '1',      '1',        [(1,1)]+[(10,1)]*3),
]

def frac(x):
    return str(x.numerator) if isinstance(x, Fraction) and x.denominator == 1 else str(x)

def save_joint_csv(slug, E):
    with open(os.path.join(TAB, f'joint_{slug}.csv'), 'w', newline='') as f:
        wr = csv.writer(f); wr.writerow(['kappa','eta_k','multiplicity'])
        for (k,e),v in sorted(E.items()): wr.writerow([k,e,v])

summary = []
enum_cache = {}
for slug,label,np_,M,k,lam0,lamn,orbits in FAMILIES:
    E = enumerator_by_orbit_convolution(orbits, M)
    enum_cache[slug] = (E, orbits, M)
    mo = moments_from_enumerator(E); th = theoretical_moments(orbits, M)
    assert (mo['total'],mo['lcd'],mo['mean_eta'],mo['var_eta']) == (th['total'],th['lcd'],th['mean_eta'],th['var_eta'])
    ex = extremal_counts(orbits, M)['total']
    W = M*sum(a*w for a,w in orbits)
    cond = mo['conditional']; cmax = max(v['mean'] for v in cond.values())
    argmax = sorted(k for k,v in cond.items() if v['mean']==cmax)
    row = {
        'slug': slug, 'family': label.replace('$',''), 'n_prime': np_, 'M': M, 'n': np_*M, 'k': k,
        'lambda0': lam0, 'lambda_n': lamn, 'orbits': str(orbits),
        'num_factors': sum(a for a,_ in orbits), 'num_orbits': len(orbits), 'W_total': W,
        'total_codes': mo['total'], 'joint_terms': len(E), 'lcd': mo['lcd'],
        'self_orthogonal': ex['self_orthogonal'], 'dual_containing': ex['dual_containing'],
        'self_dual': ex['self_dual'], 'mean_eta': frac(mo['mean_eta']), 'var_eta': frac(mo['var_eta']),
        'mean_eta_float': float(mo['mean_eta']), 'var_eta_float': float(mo['var_eta']),
        'max_eta': max(e for _,e in E), 'max_cond_mean': frac(cmax),
        'max_cond_mean_float': float(cmax), 'argmax_kappa': str(argmax),
    }
    summary.append(row); save_joint_csv(slug, E)
    print(slug, 'terms=',len(E), 'total=',mo['total'], 'mean=',mo['mean_eta'], 'var=',mo['var_eta'],
          'LCD=',mo['lcd'], 'SO=',ex['self_orthogonal'], 'SD=',ex['self_dual'])

with open(os.path.join(TAB,'summary_families.csv'),'w',newline='') as f:
    wr = csv.DictWriter(f, fieldnames=list(summary[0])); wr.writeheader(); wr.writerows(summary)
with open(os.path.join(TAB,'summary_families.json'),'w') as f: json.dump(summary,f,indent=2)

# Conditional moments for the two F32 families
for slug in ('F32_n62','F32_n124'):
    E,_,_ = enum_cache[slug]; cond = moments_from_enumerator(E)['conditional']
    with open(os.path.join(TAB,f'conditional_{slug}.csv'),'w',newline='') as f:
        wr=csv.writer(f); wr.writerow(['kappa','Phi0','Phi1','Phi2','E[eta|kappa]','Var(eta|kappa)'])
        for k,v in sorted(cond.items()): wr.writerow([k,v['Phi0'],v['Phi1'],v['Phi2'],frac(v['mean']),frac(v['var'])])

# Moment coefficient table
with open(os.path.join(TAB,'moment_coefficients_by_M.csv'),'w',newline='') as f:
    wr=csv.writer(f); wr.writerow(['M','mu_edge(a>=2)','nu(a=1)','VarY','Cov_adjacent','Var_factor_a>=3','Var_total_a=2','Var_a=1'])
    for M in [1,2,3,4,5,8,9,16,25,27,32]:
        mu=_mu_edge(M); E2=Fraction(M*(M*M+M+1),6*(M+1))
        A=Fraction(M*(M-1)*(11*M*M+15*M+6),120*(M+1)**2)
        varY=E2-mu*mu; cov=A-mu*mu
        q3=Fraction(M*(M+2)*(M*M+2*M+2),60*(M+1)**2)
        v2=Fraction(M*(M+2)*(M*M+2*M+3),18*(M+1)**2)
        wr.writerow([M,frac(mu),frac(_a1_mean(M)),frac(varY),frac(cov),frac(q3),frac(v2),frac(_a1_variance(M))])

# One-orbit extremal table
with open(os.path.join(TAB,'one_orbit_extremal_counts.csv'),'w',newline='') as f:
    wr=csv.writer(f); wr.writerow(['a','M','total_words','lcd','self_orthogonal','dual_containing','self_dual'])
    for a in [1,2,3,4,5,6,10]:
        for M in [1,2,3,4,5]:
            ex=extremal_counts([(a,1)],M)['total']
            wr.writerow([a,M,(M+1)**a,ex['lcd'],ex['self_orthogonal'],ex['dual_containing'],ex['self_dual']])

# ---------------- Figures ----------------

def savefig(name):
    plt.tight_layout(); plt.savefig(os.path.join(FIG,name+'.png'),dpi=300); plt.savefig(os.path.join(FIG,name+'.pdf')); plt.close()

# Fig 1 workflow
fig,ax=plt.subplots(figsize=(12.2,2.7)); ax.axis('off'); ax.set_xlim(0,12.2); ax.set_ylim(0,2.7)
stages=[('Affine algebra\n' + r'$\mathcal{A}\cong\prod_s K_s$',''),
        (r'$n=n^{\prime}p^t$, $M=p^t$' + '\n' + r'$x^n-\lambda_s=(x^{n^{\prime}}-\lambda_{s,0})^M$',''),
        ('Distinct factors\nreciprocal orbits\n' + r'$(a_O,w_O)$',''),
        ('Exponent words\n' + r'$e_i\in\{0,\ldots,M\}$' + '\nmin-edge statistic',''),
        ('Transfer matrix\n' + r'$\mathrm{tr}((T^{(M)}_w)^a)$' + '\njoint enumerator',''),
        ('LCD / SO / SD\nmoments, support\nverification','')]
for i,(txt,_) in enumerate(stages):
    x=.18+i*2.02
    box=FancyBboxPatch((x,.55),1.56,1.52,boxstyle='round,pad=0.03,rounding_size=0.08',fc='#eef4fb' if i<5 else '#fff3d6',ec='#24507d',lw=1.3)
    ax.add_patch(box); ax.text(x+.78,1.31,txt,ha='center',va='center',fontsize=8.3)
    if i<5: ax.annotate('',xy=(x+1.96,1.31),xytext=(x+1.64,1.31),arrowprops=dict(arrowstyle='-|>',color='#24507d',lw=1.5,mutation_scale=12))
ax.set_title('Repeated-root pipeline: from the affine algebra to the exact joint enumerator',pad=10)
savefig('fig1_workflow')

# Fig 2 orbit exponent word
fig,ax=plt.subplots(figsize=(7.2,6.4)); ax.axis('off'); ax.set_aspect('equal')
word=[2,0,3,1,2,0]; M=3; a=len(word); R=1.55
pts=[(R*math.cos(2*math.pi*i/a+math.pi/2),R*math.sin(2*math.pi*i/a+math.pi/2)) for i in range(a)]
for i,(x,y) in enumerate(pts):
    ax.add_patch(Circle((x,y),.43,fc='#eef4fb',ec='#24507d',lw=1.5,zorder=3))
    ax.text(x,y,f'$f_{i+1}$\n$e={word[i]}$',ha='center',va='center',fontsize=10,zorder=4)
for i in range(a):
    j=(i+1)%a; c=min(word[i],M-word[j])
    arr=FancyArrowPatch(pts[i],pts[j],connectionstyle='arc3,rad=0.22',arrowstyle='-|>',mutation_scale=13,
                        lw=2.4 if c>0 else 1.0,color='#b23a2f' if c>0 else '#777777',shrinkA=27,shrinkB=27)
    ax.add_patch(arr)
    mx,my=(pts[i][0]+pts[j][0])/2,(pts[i][1]+pts[j][1])/2
    norm=math.hypot(mx,my) or 1; mx*=1.24/norm if norm else 1; my*=1.24/norm if norm else 1
    # place contribution near the arc midpoint, pushed outward
    mx,my=(pts[i][0]+pts[j][0])/2,(pts[i][1]+pts[j][1])/2
    ax.text(mx*1.18,my*1.18,str(c),ha='center',va='center',fontsize=10,
            bbox=dict(boxstyle='circle,pad=0.18',fc='white',ec='none'))
ax.set_xlim(-2.6,2.6); ax.set_ylim(-2.7,2.7)
ax.set_title(r'One reciprocal orbit, $M=3$, word $e=(2,0,3,1,2,0)$'+'\nedge label $=\\min(e_i,M-e_{i+1})$; total hull contribution $=7w$')
savefig('fig2_orbit_exponent_word')

# Fig 3 threshold layers
fig,ax=plt.subplots(figsize=(7.5,4.6)); word=[2,0,3,1]; M=3
for j,e in enumerate(word):
    for r in range(1,M+1):
        fc='#24507d' if e>=r else '#e8edf2'
        rect=plt.Rectangle((j,r-1),.86,.82,fc=fc,ec='white',lw=1.5); ax.add_patch(rect)
        if e>=r: ax.text(j+.43,r-.58,'1',color='white',ha='center',va='center',fontsize=11)
    ax.text(j+.43,-.45,f'$e_{j+1}={e}$\n$M-e={M-e}$',ha='center',va='top',fontsize=9)
for j in range(len(word)):
    jj=(j+1)%len(word); c=min(word[j],M-word[jj])
    if j<len(word)-1: ax.annotate(f'{c}',xy=(j+.93,3.18),ha='center',fontsize=10,color='#b23a2f')
ax.text(3.5,3.18,f'wrap: {min(word[-1],M-word[0])}',fontsize=9,color='#b23a2f')
ax.set_xlim(-.3,4.4); ax.set_ylim(-1.1,3.6); ax.set_xticks([]); ax.set_yticks([.4,1.4,2.4],['level 1','level 2','level 3'])
ax.set_title(r'Threshold-layer view: $e_i=\sum_{r=1}^{M}\mathbf{1}[e_i\geq r]$ (edge labels on top)')
savefig('fig3_threshold_layers')

# Fig 4 transfer matrix M=2 as annotated grid
fig,ax=plt.subplots(figsize=(6.8,5.4)); M=2
mat=np.zeros((3,3))
for alpha in range(3):
    for beta in range(3): mat[alpha,beta]=min(alpha,M-beta)
im=ax.imshow(mat,cmap='Blues',vmin=0,vmax=2)
def mono(alpha,beta):
    du=M-beta; dz=min(alpha,M-beta); s=''
    if du: s+=f'U^{{{du}w}}' if du>1 else 'U^{w}'
    if dz: s+=f'Z^{{{dz}w}}' if dz>1 else 'Z^{w}'
    return '$'+(s or '1')+'$'
for alpha in range(3):
    for beta in range(3):
        col = 'white' if mat[alpha, beta] >= 2 else '#111111'
        ax.text(beta,alpha,mono(alpha,beta),ha='center',va='center',fontsize=12,color=col,
                fontweight='bold' if mat[alpha,beta]>=2 else 'normal')
ax.set_xticks(range(3),[r'$\beta=0$',r'$\beta=1$',r'$\beta=2$']); ax.set_yticks(range(3),[r'$\alpha=0$',r'$\alpha=1$',r'$\alpha=2$'])
ax.set_xlabel('destination exponent'); ax.set_ylabel('source exponent')
ax.set_title(r'Transfer matrix $T^{(2)}_w(U,Z)$ (entries coloured by $\min(\alpha,M-\beta)$)')
fig.colorbar(im,ax=ax,ticks=[0,1,2],label=r'$\min(\alpha,M-\beta)$'); savefig('fig4_transfer_matrix_M2')

# Heatmap helper
def heatmap(slug,title,fname):
    E,orbits,M=enum_cache[slug]; W=M*sum(a*w for a,w in orbits); emax=max(e for _,e in E)
    A=np.full((W+1,emax+1),np.nan)
    for (k,e),v in E.items(): A[k,e]=math.log10(v)
    fig,ax=plt.subplots(figsize=(8.2,6.2))
    im=ax.imshow(A,origin='lower',aspect='auto',extent=[0,emax,0,W],cmap='viridis')
    cond=moments_from_enumerator(E)['conditional']
    xs=[float(cond[k]['mean']) for k in sorted(cond)]; ys=sorted(cond)
    ax.plot(xs,ys,color='#d9381e',linestyle='--',lw=2.0,label=r'$\mathbb{E}[\eta_k\mid\kappa]$')
    ax.set_xlabel(r'hull dimension $\eta_k$'); ax.set_ylabel(r'code dimension $\kappa$'); ax.set_title(title)
    ax.legend(loc='lower right',framealpha=0.95); fig.colorbar(im,ax=ax,label=r'$\log_{10}$ multiplicity'); savefig(fname)

heatmap('F8_n14',r'Joint distribution over $\mathbb{F}_8$, $n=14$ ($n^\prime=7$, $M=2$): $3^7$ codes','fig5_joint_F8_n14')
heatmap('F32_n62',r'Joint distribution over $\mathbb{F}_{32}$, $n=62$ ($n^\prime=31$, $M=2$): $3^{31}$ codes','fig6_joint_F32_n62')

# Fig 7 hull marginal comparison, same orbit skeleton, M=1,2,4
fig,ax=plt.subplots(figsize=(8,5.2))
for M,marker in [(1,'o'),(2,'s'),(4,'^')]:
    E=enumerator_by_orbit_convolution([(1,1),(6,1)],M); tot=sum(E.values()); W=7*M
    hull={}
    for (k,e),v in E.items(): hull[e]=hull.get(e,0)+v/tot
    xs=sorted(hull); ax.plot([x/W for x in xs],[hull[x] for x in xs],marker=marker,ms=4,lw=1.4,label=f'$M={M}$ ($n={7*M}$)')
ax.set_xlabel(r'normalised hull dimension $\eta_k/n$'); ax.set_ylabel('probability (uniform exponent word)')
ax.set_title(r'Hull marginal for the $\mathbb{F}_8$ orbit skeleton $(1,1),(6,1)$ as $M$ grows'); ax.legend(); ax.grid(alpha=.25); savefig('fig7_hull_marginals')

# Fig 8 support trapezoid one orbit a=6,M=3
fig,ax=plt.subplots(figsize=(7.6,5.6)); a,M=6,3; E=one_orbit_bruteforce(a,1,M); pts=np.array(list(E))
ax.scatter(pts[:,0],pts[:,1],s=28,color='#24507d',label='attainable $(\\kappa,\\eta)$')
R=np.arange(0,a*M+1); lo=[min(r,M,a*M-r) for r in R]; hi=[min(r,a*M-r) for r in R]
ax.plot(R,hi,'--',color='#b23a2f',label=r'upper: $\min(R,aM-R)$'); ax.plot(R,lo,'--',color='#2e7d32',label=r'lower: $\min(R,M,aM-R)$')
ax.set_xlabel(r'$R=\sum_i(M-e_i)$ (unweighted code dimension)'); ax.set_ylabel(r'$H=\sum_i\min(e_i,M-e_{i+1})$')
ax.set_title('One-orbit support trapezoid ($a=6$, $M=3$, $w=1$)'); ax.legend(); ax.grid(alpha=.25); savefig('fig8_support_trapezoid')

# Fig 9 conditional means F32
fig,ax=plt.subplots(figsize=(8,5.2))
for slug in ('F32_n62','F32_n124'):
    E,orbits,M=enum_cache[slug]; W=M*sum(a*w for a,w in orbits); cond=moments_from_enumerator(E)['conditional']
    xs=sorted(cond); ax.plot([x/W for x in xs],[float(cond[x]['mean'])/W for x in xs],lw=1.6,label=f'$M={M}$, $n={31*M}$')
ax.set_xlabel(r'normalised code dimension $\kappa/W$'); ax.set_ylabel(r'$\mathbb{E}[\eta_k\mid\kappa]/W$')
ax.set_title(r'Conditional mean hull dimension, $\mathbb{F}_{32}$ repeated-root families'); ax.legend(); ax.grid(alpha=.25); savefig('fig9_conditional_F32')

print('Wrote',len(os.listdir(TAB)),'table files and',len(os.listdir(FIG)),'figure files')
