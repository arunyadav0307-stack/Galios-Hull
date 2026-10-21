# Literature Audit v1 — Repeated-Root k-Galois Hull Enumeration
**Date:** 20 Oct 2026 · **Status:** PRELIMINARY (web/publisher-level). MathSciNet / zbMATH / Scopus ka exhaustive audit submission se pehle baki hai — is file ko "priority proof" mat samajhna.

**Audit question:** Kya kisi maujooda paper ne ye paanchon cheezein **ek saath** ki hain?
(1) repeated-root length `p | n`, (2) `k`-Galois (code-first ya koi bhi fixed convention) hull,
(3) square-free affine algebra / CRT field components, (4) **saare** labeled codes ki ginati,
(5) (code-dimension, hull-dimension) ka **joint** generating polynomial?

**Preliminary verdict: CONDITIONAL GO.** Paachon ka sangam kisi ek record me nahi mila.
Lekin 3 full-text checks (neeche §4) band kiye bagair koi novelty sentence manuscript me nahi jayega.

---

## 1. Sabse qareebi records (overlap matrix)

| # | Record | Setting | Kya deta hai | Hamse doori |
|---|---|---|---|---|
| L1 | Debnath–Prakash–Islam, *Galois hulls of constacyclic codes over finite fields*, Cryptogr. Commun. 15 (2023) 111–127 (+ Correction 129–130) | Ek finite field, **simple-root** | Ek code ke hull ka formula; kuch sharton par diye gaye hull-dimension wale codes ki ginati | Repeated-root nahi, affine nahi, joint (K,H) enumerator nahi |
| L2 | Debnath–Prakash, *Average dimensions of Galois hulls of constacyclic codes*, AMC 19 (2025) 1569–1604 | Field + ring `R_{m,q}`, simple-root | Hull dimensions ka **average** | Sirf average; puri distribution / repeated-root nahi |
| L3 | Debnath–Islam–Yadav–Prakash, *Study of small Galois hull dimensions of constacyclic codes*, AMC 22 (2026) 1–18 | Field, `p|n` **bhi shamil** | Hull-dimension **1 aur 2** hone ki existence conditions; EAQECC examples | ⭐ Sabse qareebi repeated-root padosi. Lekin: ginati nahi, joint enumerator nahi, affine nahi |
| L4 | Debnath–Islam–Martínez-Moro–Prakash, *Galois hulls of constacyclic codes over affine algebra rings*, Discrete Math. 349 (2026) 114750 (arXiv:2412.08512) | Square-free affine `A`, **simple-root** | Ek code ke hull ka formula, LCD condition, attainable dimensions ka set, EAQECC | Alphabet bilkul hamara, lekin simple-root. (Iske conclusion me "non-isometric codes ki ginati" future work kahi gayi hai — hamari ginati **labeled + repeated-root** hai, wohi nahi; phir bhi introduction me is line ka imaandar zikr hoga) |
| L5 | User ki predecessor manuscript (Phase 10F, is repo me) | Square-free affine `A`, simple-root | **Joint (K,H) enumerator**, transfer matrix, LCD count, mean/variance | Repeated-root nahi — yahi gap hamari paper band karti hai; `P=1` par ye recover honi chahiye |
| L6 | Talbi–Batoul–Fotue Tabue–Martínez-Moro, *Galois hulls of cyclic serial codes over a finite chain ring*, arXiv:2102.06995 | Chain ring, `gcd(n,p)=1` | Galois hull structure, Euclidean hull parameters ka algorithm, average | Chain ring ≠ affine product; repeated-root nahi |
| L7 | Zhang–Kong–Zheng, *Quantum Codes from Galois Hulls of Constacyclic Codes over a Finite Non-Chain Ring*, Entropy 28 (2026) 407 | Ek non-chain ring | Hull dimension formula + QMDS/QECC constructions | Ginati nahi, affine CRT nahi, repeated-root focus nahi |
| L8 | *Generator polynomial matrices of the Galois hulls of multi-twisted codes*, Finite Fields Appl. (2025), doi:10.1016/j.ffa.2025.102712 | Finite field, multi-twisted (constacyclic iski special case) | Hull ka **generator polynomial matrix** determinantal divisors se | ⚠️ Agar iske hypotheses repeated-root ko bhi lete hain, to hull-generator hamara headline nahi ban sakta — hamari pehchan **ginati** hogi. Full-text check mandatory (§4-B) |
| L9 | Repeated-root structure papers: length `3p^s`, `ℓ^t p^s`, `2ℓ^m p^n`, `k^s l^m p^n` aadi (Dinh aur anya; FFA/J. Algebra Appl. waghera) | Finite field, khaas lambaiyan | Saare codes ke generator polynomials, duals; kuch me LCD/self-dual **enumeration** (Euclidean, khaas cases) | Ye exponent/dual ki neev dete hain — reviewer bolega "structure to jani hui hai". Isliye hamara dawa structure par nahi, **k-Galois reciprocal-orbit joint enumerator + affine product + moments** par hoga |
| L10 | Pang–Zhu–Li, *On LCD repeated-root cyclic codes over finite fields*, J. Appl. Math. Comput. 56 (2018) 625–635 | Field, cyclic, Euclidean | LCD repeated-root codes ki shartein + ginati | Hamara LCD corollary iska Galois + affine + orbit roop hoga — akele LCD ko headline nahi banayenge |
| L11 | *Hulls of cyclic codes over a local ring*, Springer chapter (2026) | Local ring `Z_{p^3}` | Hull generators, types, fixed p-dimension ki ginati | Local/chain duniya; affine product aur Galois joint enumerator nahi |
| L12 | *Computable Derivative-Twisted Intersection Dimensions of Repeated-Root Cyclic Codes…*, Mathematics 14 (2026) 2866 | Field, repeated-root cyclic | Derivative-twisted intersections (hull jaisi par **alag** twist) | Alag sawaal; sirf watchlist — kabhi reviewer confuse kare to farq saaf rakhna |

## 2. Novelty boundary (manuscript me surakshit bhasha)

**Keh sakte hain (audit band hone ke baad):**
> "Under the compatible-twist hypothesis, we derive an exact bivariate generating polynomial for the joint distribution of code dimension and k-Galois hull dimension over all labeled multiplicity selections of repeated-root constacyclic codes over a square-free affine algebra. The polynomial factors over reciprocal-factor orbits as a product of traces of a (P+1)-state transfer matrix, and specializes to the labeled simple-root enumerator at P = 1."

**Bilkul NAHI keh sakte:**
- "Pehli baar repeated-root codes ke hulls ginne gaye" (L3, L9, L10 iske tukde pehle de chuke hain)
- "Hull generator pehli baar mila" (L8 ka dayra check kiye bagair to hargiz nahi)
- "LCD codes ki ginati nayi hai" (L10) — nayi baat **joint enumerator** hai, usi ke corollaries hain baaki
- "Quantum codes naye parameters ke saath" — jab tak distance alag se sabit na ho

## 3. Is paper ki asli pehchan (ek vaakya, jo har draft me rahega)

> **Simple-root me factor ek binary switch tha; repeated-root me woh ek (P+1)-danu wala dial hai —
> aur is paper me hum us dial ke saare ghumaon ko code- aur hull-dimension ke saath ek saath ginte hain,
> poore affine algebra par, ek hi transfer-matrix trace wale formula se.**

## 4. Mandatory full-text checks (Phase 1 — ye band hue bagair draft final nahi)

- **Check A (L3):** *Study of small Galois hull dimensions* ke pure theorems padho: kya wahan `p|n` ke liye
  generator-exponenton me hull ka **pura formula** hai? Agar hai, to hamari paper usi formula ko
  "known lemma" kehkar credit degi aur apni pehchan sirf enumerator/affine/moments par rakhegi.
- **Check B (L8):** Multi-twisted paper ki hypotheses: kya block lengths par `gcd(m_j, p) = 1` hai?
  Agar repeated-root bhi shamil hai, to hamare Theorem (dual/hull generator) ko uska corollary kehna padega —
  enumerator phir bhi hamara rahega.
- **Check C (L9/L10):** Khaas-lambai repeated-root LCD/self-dual enumerations ki list banao, taaki
  hamare LCD/self-orthogonal corollaries ka dayra (general `n = P·n₀`, Galois, affine) saaf dikhe.
- **Check D:** Sir se milne / mail karne se pehle MathSciNet + zbMATH par teen khoj-vakya chalao:
  "Galois hull" + "repeated-root", "hull enumeration" + "constacyclic" + "affine",
  "hull" + "multiplicity" + "transfer matrix". (Library access chahiye hoga.)

## 5. Kaam ke references (working list)

1. Debnath, Prakash, Islam — Cryptogr. Commun. 15 (2023), doi:10.1007/s12095-022-00591-6 (+ Correction doi:10.1007/s12095-022-00602-6)
2. Debnath, Prakash — Adv. Math. Commun. 19 (2025), doi:10.3934/amc.2025010
3. Debnath, Islam, Yadav, Prakash — Adv. Math. Commun. 22 (2026), doi:10.3934/amc.2025054
4. Debnath, Islam, Martínez-Moro, Prakash — Discrete Math. 349 (2026) 114750, doi:10.1016/j.disc.2025.114750; arXiv:2412.08512
5. Sangwisut, Jitman, Ling, Udomkavanich — Finite Fields Appl. 33 (2015), doi:10.1016/j.ffa.2014.12.008
6. Talbi et al. — arXiv:2102.06995 (chain ring Galois hulls)
7. Zhang, Kong, Zheng — Entropy 28 (2026), doi:10.3390/e28040407
8. Multi-twisted Galois hulls — Finite Fields Appl. (2025), doi:10.1016/j.ffa.2025.102712
9. Fan, Zhang — Galois inner product ki neev (2017); Liu, Pan — Des. Codes Cryptogr. 88 (2020) (Galois hulls of linear codes)
10. Repeated-root structure: length `k^s l^m p^n` (Finite Fields Appl. 2024, S1071579724001813), length `2ℓ^m p^n` (S1071579714001282), length `3p^s` (Discrete Math. 2013, S0012365X13000526) — poori granth-soochi Phase 1 me pakki hogi, koi lekhak-naam andaz se nahi likha jayega.
