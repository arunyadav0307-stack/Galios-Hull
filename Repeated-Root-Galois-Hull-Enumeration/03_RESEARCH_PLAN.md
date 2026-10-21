# Research Plan — Repeated-Root k-Galois Hull Enumeration
**Idea locked:** 20 Oct 2026 · **Andaz se kul samay:** 12–16 hafte (part-time) / 6–8 hafte (lagatar)

---

## Phase 0 — Idea lock + prototype ✅ (ho gaya)
- [x] Idea fix, title fix
- [x] Preliminary literature audit v1 (`01_LITERATURE_AUDIT.md`)
- [x] Theorem blueprint: statements + proof obligations (`02_THEOREM_BLUEPRINT.md`)
- [x] Brute-force prototype: GF(4) par 206 assignments, teeno hisaab barabar (`code/`)

## Phase 1 — Full-text literature audit (1–2 hafte) ⛔ GATE
- Audit file ke **Check A–D** band karo: Debnath-small (2026) ke pure theorems, multi-twisted (2025) ki hypotheses,
  repeated-root LCD enumerations ki soochi, MathSciNet/zbMATH khoj (library/sir ki madad).
- Har qareebi paper ke liye ek "theorem-extraction note": usne *exactly* kya sabit kiya, kis dayre me.
- **Gate G1:** Agar kisi paper me repeated-root Galois **joint enumerator** pehle se mil gaya →
  paper turant pivotegi: (a) sirf affine + moments wala hissa bachega, ya (b) idea badalna padega.
  Milne ki ummeed kam hai (audit v1), par ye gate manuscript likhne se **pehle** hai.

## Phase 2 — Prototype-2: dayra badhaao (1 hafta)
- `galois` (Python) ya Sage se samanya `F_{p^m}` implementation: ek `p=3` case (jaise `F₉, k=1, n=12`)
  aur do-component affine case (`A = F₂ × F₄`, `k=0`, `n=6`) brute-force se jaancho.
- Incompatible twist (`λ^{1+p^{d−k}} ≠ 1`) par chhota prayog: hull vyavhaar dekho (daave ke liye nahi, samajhne ke liye) —
  taaki "limitations" khand sach par tika ho.
- **Gate G2:** Koi bhi mismatch → formula/proof yojana wahi ruk kar theek hogi, aage nahi badhegi.

## Phase 3 — Proofs, pehle ek component (2–3 hafte)
- RR-1…RR-5: parametrization, reciprocal multiplicities, **bina-separability dual lemma**, hull formula.
- Adversarial jaanch (purani aadat): chhote counter-example khud dhundho — `P=2, n₀=1` jaise kinare wale cases,
  `L=1` orbit, trivial codes (`g=1`, `g=M`), `ϱ > d_s` wala mamla.
- Phir T5–T6 (transfer + global), C1–C5.
- **Gate G3:** `P=1` par purani theorem ki **har** corollary (LCD count, mean, variance-exception) naye sutro se wapas aani chahiye. Ek bhi na aaye → galti yahi pakdi jayegi.

## Phase 4 — Moments aur band sutra (1–2 hafte)
- RR-8: variance ke `L=1, 2, ≥3` cases ke closed forms (`P` me rational polynomials), layer-decomposition (blueprint §2) se ya seedhe ginti se.
- Sambhav ho to one-orbit polynomial ka parat-dar-parat (layered) band roop.
- Saari pehchane (identities) chhote `P, L` par computer se jaanch (prototype me jodkar).

## Phase 5 — Manuscript (2–3 hafte)
- Blueprint §4 wali 10-khand rachna; purani manuscript ka hi LaTeX ishtail (style) aur imaandari wali bhasha
  ("no priority claim", hypotheses ek jagah, labeled ≠ equivalence).
- Examples table: prototype ke 4 cases + affine do-component case; EAQECC sirf jana-hua distance wale example par (RR-9).
- References: granth-soochi publisher records se pakki — koi lekhak/DOI andaz se nahi.

## Phase 6 — Internal referee + submission taiyari (1–2 hafte)
- Khud par referee report: reviewer ke 5 sambhavit hamle —
  (1) "dual lemma non-separable me?" (2) "multi-twisted 2025 se farq?" (3) "structure to Dinh jante the?"
  (4) "LCD ginati Pang se aage kya?" (5) "affine me naya kya hai jo ek field par nahi?"
  Har ka jawab manuscript ke andar pehle se.
- Reproducibility: `code/` saaf karke, README se chalakar, output jodkar.
- **Target journals (prathmikta kram):** (1) *Advances in Mathematics of Communications* — sir ki team ka apna akhada, hull+EAQECC dayra;
  (2) *Finite Fields and Their Applications* — enumerative/finite-field pehchan sabse majboot ho to;
  (3) *Cryptography and Communications* — 2023 wali predecessor yahi chhapi thi;
  (4) *Discrete Mathematics* — affine-wali paper yahi hai, par kram (sequence) lamba chal sakta hai.

## Sir (Dr. Habibul Islam) se sampark ki ran-neeti
- Pehle mail **Phase 3 ke baad** bhejna behtar hai: saath me 2-page summary (main theorem + `P=1` recovery + prototype table)
  aur ek saaf vaakya — *"aapki 2026 affine paper aur hamari simple-root enumerator ki jo seema thi (`p∤n`), use band karne ka prayas hai."*
- Mail se pehle unki *Study of small Galois hull dimensions* (AMC 2026) poori padhi honi chahiye — wahi is paper ki sabse qareebi padosi hai,
  aur baat-cheet wahi se shuru hogi.
- Co-authorship ka koi dawa/apeksha pehle se nahi; pehle kaam dikhao, salah maango.

## Risk register (sabse bade teen)
| Risk | Sambhavna | Bachav |
|---|---|---|
| Full-text audit me qareebi enumerator mil jaye | Kam | Gate G1 manuscript se pehle; pivot yojana taiyar |
| Dual/hull proof non-separable modulus me atak jaye | Madhyam | Proof ki disha annihilator/PID par hai, prototype vector-level par saath hai; atakne par dayra `λ^{…}=1` wale khaas twists tak seemit karke bhi paper banti hai |
| Reviewer "sirf P=1 ka vistaar" kahe | Madhyam | Jawab pehle se: `(P+1)`-state statistic nayi hai, LCD ki `P`-swatantrata aur variance ke naye cases jaise **gunatmak** naye tathya aage rakhne hain, sirf "matrix bada ho gaya" nahi |
