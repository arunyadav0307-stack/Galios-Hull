# Task Queue — Repeated-Root Galois Hull Enumeration
**Commander (ChatGPT) isi soochi se ek-ek command uthayega. Status: ⬜ baki · 🔄 chal raha · ✅ ho gaya · ⛔ gate**

## Phase 0 — Setup ✅
- ✅ P0-00 Idea lock, blueprint, audit v1, prototype (GF(4), 206 assignments verified)

## Phase 1 — Full-text literature audit ⛔ GATE G1
- ⬜ P1-01 Debnath–Islam–Yadav–Prakash (AMC 2026, small hull dims) ka theorem-extraction note:
  `p|n` par exact kya sabit hai? Hull ka pura exponent-formula hai ya sirf dim 1,2 ki shartein?
- ⬜ P1-02 Multi-twisted Galois hulls (FFA 2025) ki hypotheses extraction: kya repeated-root (`gcd(m_j,p)≠1`) shamil hai?
  Agar hai, to hamare T3/T4 ko uska darja (corollary/complement) saaf likho.
- ⬜ P1-03 Repeated-root LCD/self-dual enumerations (Dinh school + Pang–Zhu–Li 2018) ki soochi aur hamare corollaries se doori.
- ⬜ P1-04 Khoj-vakya audit: MathSciNet/zbMATH/Google Scholar par teen search — report me likho kya mila, kya nahi
  (jo access na mile use "NOT VERIFIED" likhna, andaz nahi).
- ⬜ P1-05 Audit v2 likho: novelty sentence ka antim roop + har padosi paper se farq ek table me. → **G1 band**

## Phase 2 — Prototype-2
- ⬜ P2-01 Samanya `F_{p^m}` prototype (`galois` pkg/Sage): `F₉, k=1` case brute-force jaanch.
- ⬜ P2-02 Do-component affine case `A = F₂ × F₄, k=0` — global product formula ki vector-level jaanch.
- ⬜ P2-03 Incompatible twist par chhota prayog (sirf samajhne ke liye; koi dawa nahi) → limitations note.

## Phase 3 — Proofs (ek component pehle)
- ⬜ P3-01 RR-1 + RR-2: divisor-jali lemma, `#` ki prime-power multiplicativity.
- ⬜ P3-02 RR-3 + RR-4: bina-separability Euclidean-dual lemma + code-first exponent formula (T3).
- ⬜ P3-03 RR-5 + T4: intersection=lcm lemma, hull dimension formula — adversarial chhote cases ke saath.
- ⬜ P3-04 T5 + T6: transfer trace aur global enumerator; **P=1 recovery har sutra par** → **GATE G3**

## Phase 4 — Moments / band sutra
- ⬜ P4-01 Variance ke `L=1, 2, ≥3` closed forms + computer se pehchan-jaanch (RR-8).
- ⬜ P4-02 (vaikalpik) Layer-decomposition se one-orbit polynomial ka band roop.

## Phase 5 — Manuscript
- ⬜ P5-01 LaTeX draft: khand 1–4 (intro, preliminaries, parametrization, dual).
- ⬜ P5-02 LaTeX draft: khand 5–7 (hull, enumerator, corollaries).
- ⬜ P5-03 Examples + validation khand; references publisher records se pakke.
- ⬜ P5-04 PDF build + visual jaanch.

## Phase 6 — Referee-yuddh aur samarpan (submission)
- ⬜ P6-01 Self-referee report: 5 sambhavit hamlo ke jawab manuscript ke andar.
- ⬜ P6-02 Sir (Dr. Habibul Islam) ke liye 2-page summary + mail draft (user ki manjuri ke baad hi bhejna).
- ⬜ P6-03 Journal chunaav (AMC / FFA / Cryptogr. Commun.) + submission package.

---
*Commander ke liye nirdesh: jis din koi kaam ✅ ho, Arena apni report me batayega — tum yahan status user se update karwa sakte ho ya Arena ko hi is file ko update karne ki command de sakte ho.*
