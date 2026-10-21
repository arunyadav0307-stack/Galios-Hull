# Arena Worklog — Repeated-Root Galois Hull Enumeration
*Har command, har badlaav, har galti — ek jagah. Kuch mitaaya nahi jayega; sudhaar nayi entry me aayega.*

---

## 2026-10-20 — Setup (user ke seedhe nirdesh par, koi COMMAND ID nahi)

- **Kiya:** Idea fix — *Exact Joint Enumeration of k-Galois Hull Dimensions of Repeated-Root Constacyclic Codes over Square-Free Affine Algebras*.
- **Files banayi:** `README.md`, `01_LITERATURE_AUDIT.md` (verdict: CONDITIONAL GO), `02_THEOREM_BLUEPRINT.md`
  (T1–T6, C1–C7, RR-1…RR-9), `03_RESEARCH_PLAN.md` (Phase 0–6, gates G1–G3), `NEW_PAPER_IDEAS.md` me "FIXED" update.
- **Prototype chalaya:** `code/validate_repeated_root.py` — GF(4), k=1, λ=1 par n=6,10,14 (P=2) aur n=20 (P=4);
  kul 206 exponent assignments me brute-force hull = exponent formula = transfer trace. LCD count har case `2^{#orbits}`.
  Output: `code/validation_output.txt`.
- **Ek galti pakdi aur sudhari (isi din):** Blueprint ke C5 me mean code-dimension `(P/2)·n·Σm_s` likha gaya tha —
  sahi hai `(n/2)·Σ_s m_s`. Sudhaar `02_THEOREM_BLUEPRINT.md` me ho gaya hai. (Yahi kaaran hai ki har formula
  P=1 recovery aur prototype se jaanchi jayegi.)
- **Workflow files banayi:** `CHATGPT_STARTER_PROMPT.md` (ChatGPT ko dene ke liye), `COMMAND_PROTOCOL.md`,
  `TASK_QUEUE.md`, ye `ARENA_WORKLOG.md`.
- **Agle sujhaye command:** `P1-01` — Debnath–Islam–Yadav–Prakash (AMC 2026) ka theorem-extraction note.
  Gate G1 (Phase 1 audit) band hue bagair manuscript drafting shuru nahi hogi.

---

## 2026-10-20 — BP-01 Paper Blueprint Preparation

- **Kiya:** `CHATGPT_STARTER_PROMPT.md`, project README, literature audit, theorem blueprint, research plan,
  command protocol, task queue, prototype script/output aur predecessor manuscript ke relevant dual/enumerator/moment
  sections dobara padhe. Paper structure, research gap, theorem dependencies, formula audits aur validation plan
  `04_PAPER_BLUEPRINT.md` me likha; saare suspected errors/risks `04_BLUEPRINT_GAP_REGISTER.md` me alag se rakhe.
  `02_THEOREM_BLUEPRINT.md` ki frozen statements **nahi badli** gayi; manuscript drafting bhi shuru nahi hui.
- **Prototype praman:** `code/validate_repeated_root.py` dobara chalaya; output saved
  `code/validation_output.txt` se exactly match hua aur `ALL PROTOTYPE CHECKS PASSED` par khatm hua.
  Temporary BP-01 audit checks me GF(4), `(n0,P)=(5,2)` ke saare 27 assignments par
  \(\langle h^\#\rangle=D_{\mathrm{CF}}(C)\) vector-space dual se match hua; LCD/self-orthogonal word criteria aur
  \(P=1\) orbit polynomial ki finite checks bhi pass hui. Ye finite evidence hai, general proof nahi.
- **RR-3 nishkarsh:** Euclidean dual generator \(h^*\) ka coefficient-pairing proof separability use nahi karta;
  non-wrapped shifts + dimension count se repeated-root modulus par bhi route sound hai. Phir
  \(D_{\mathrm{CF}}(C)=\rho(C^{\perp E})\) se \(h^\#\) milta hai. Formal proof abhi likhna baki hai (RR-3 open),
  par ye ab sabse bada mathematical blocker nahi hai.
- **Galti mili — sudhaar NAHI kiya (protocol ke mutabiq alag register me rakhi):** Frozen C5 ki hull-mean formula
  \(L_O=1\) orbits par galat hai, kyunki wahan statistic \(\min(P-A,A)\) hai, do independent uniforms ka min nahi.
  Prototype counterexamples: \((n_0,P)=(3,2)\) par brute mean \(1\) vs frozen \(5/3\); \((5,2)\) par
  \(23/9\) vs \(25/9\). Proposed corrected formula sirf `04_BLUEPRINT_GAP_REGISTER.md` GAP-01 me hai;
  Commander/Boss ki approval ke bagair `02_THEOREM_BLUEPRINT.md` nahi badla jayega.
- **Literature chetaavni:** Accessible L4 affine paper ko “simple-root only” kehna unsafe hai — uske text me
  \(n=n'p^{e'}\), exponent \(0\ldots p^{e'}\) aur hull-dimension formula dikhta hai. L8 multi-twisted arXiv text me bhi
  general \(\gcd(m_j,p)=1\) restriction nahi dikhi. Isliye paper ki pehchan individual hull formula par nahi,
  joint labeled \((K,H)\) enumerator + transfer trace par rahegi. Gate G1 ab bhi khula hai.
- **Files banayi:** `04_PAPER_BLUEPRINT.md`, `04_BLUEPRINT_GAP_REGISTER.md`. **File update:** ye worklog.
  Koi aur project file edit nahi hui.
- **Agle sujhaye command:** `P1-01` — L1/L4 ka full-text theorem-extraction aur overlap audit,
  saath me L3 extraction aur L8 publisher-version closure. Gate G1 band hue bagair manuscript drafting nahi hogi.

---

## 2026-10-20 — P1-01 Full-Text Theorem Extraction and Overlap Audit

- **Kiya:** Command labels aur repo labels ka label-map file me saaf likhkar (command “L1” = repo L4 affine,
  command “L4” = repo L8 multi-twisted, command “L3” = repo L1 finite-field, command “L8” = ambiguous →
  publisher/scope closure) theorem-level extraction ki gayi. Deliverable:
  `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md`. `04_BLUEPRINT_GAP_REGISTER.md` me GAP-01–GAP-04, GAP-09,
  GAP-10, GAP-12, GAP-15 par P1-01 updates aur naya GAP-16 joda gaya. `02_THEOREM_BLUEPRINT.md` ki frozen
  statements aur prototype code **nahi badli** gayi; manuscript drafting shuru nahi hui.
- **Repo L4 (affine, arXiv:2412.08512; DOI `10.1016/j.disc.2025.114750`):** candidate-first pairing
  \(\langle\alpha,\beta\rangle_k=\sum_i\alpha_i\beta_i^{p^k}\) verify hua. Theorem 5 (dual generator
  \(\tilde h=\sum e_{S(\nu)}h_{S(\nu)}^\#\)), Theorem 7 (hull generator \(\sum e_{S(\nu)}\mathrm{lcm}(g_{S(\nu)},h_{S(\nu)}^\#)\)),
  Theorem 8 (\(n=n'p^{e'}\), \(\gcd(\mathrm{ord}\,\lambda,n')=1\), \(\mathrm{ord}(\lambda)\mid1+p^{e-k}\) par
  exponent-level hull-dimension formula, \(0\le u\le p^{e'}\)) aur Corollary 3.5 (attainable dimension
  **values** ki ginati, codes ki nahi) extract hue. Conclusion me codes-by-hull-dimension ginati khuli
  (open) kahi gayi hai. Joint \((K,H)\) enumerator, \((P+1)\)-state transfer trace, code-count ya
  mean/variance inspected text me nahi mila. Publisher version sirf abstract/introduction/snippet level
  par verify hua; repo-root PDF arXiv v1 hai, publisher PDF nahi. §2.1 field-components aur §2.3
  \(\mathbb F_q\)-projection codes ka model frozen \(K_s\)-model se abhi reconcile nahi hua.
- **Repo L8 (multi-twisted, arXiv:2305.15237; DOI `10.1016/j.ffa.2025.102712`, FFA 109 (2026) Art. 102712):**
  Theorems 21/25/28 aur Corollaries 22/26/29 se hull-dimension/GPM machinery verify hui; block lengths
  par general \(\gcd(m_j,p)=1\) restriction nahi mili; index-1 constacyclic specialization
  \(\Lambda^{-p^{-\kappa}}=\Lambda\) ke under aata hai. Labeled joint enumerator, transfer trace ya
  moments inspected text me nahi mile. Publisher theorem numbering alag se verify nahi hua.
- **Repo L1 (finite-field, DOI `10.1007/s12095-022-00591-6`):** Publisher abstract se hull-dimension
  formula aur restrictions on \(q\) ke saath “given Galois hull dimension” par codes ki ginati verify
  hui; correction DOI `10.1007/s12095-022-00602-6` se \(B_i\)/\(f^{i_1\#}\ne f^{i_2\#}\) repeated-root
  machinery verify hui. Lekin lawful open full text nahi mila, isliye exact theorem numbers/hypotheses/
  counting scope **unresolved** hai — absence ka praman nahi. “L1 simple-root only” wali baat unsafe hai.
- **Repo L3/L2/L9/L10 scope:** L3 (DOI `10.3934/amc.2025054`) Table 1 se sirf hull-dimension 1–2 ki
  existence (Thm. 3.1/3.9/3.18/3.20) verify hui; theorem bodies expose nahi hue. L2
  (DOI `10.3934/amc.2025010`) se finite fields + \(R_{m,q}\) par average formulas verify hue — mean
  headline nahi ban sakta. L9/L10 publisher-scope table (FFA 2025 \(k^s\ell^mp^n\), FFA 2015
  \(2\ell^mp^n\), Cryptogr. Commun. 2015 \(\ell^tp^s\), AMC 2023 \(6\ell^mp^n\), Pang–Zhu–Li 2018
  general cyclic LCD enumeration) se Euclidean structure/LCD-type overlap verify hua; koi bhi inspected
  record \(k\)-Galois affine joint enumerator nahi deta.
- **GAP-01 dobara jaanch (sudhaar NAHI kiya):** \(L=1\) statistic \(\min(P-A,A)\) se
  \(\mathbb E=\lfloor P^2/4\rfloor/(P+1)=\nu_P\) derive hua aur exact `fractions` computation se
  \(P=1\ldots20\) tak brute-force match hua; \((P,L)\in\{1,2,3,4\}\times\{1,2,3\}\) par split formula
  match hua, frozen formula sirf \(L=1\) par fail hua. Counterexamples phir se exact mile:
  \((3,2)\): \(1\) vs \(5/3\); \((5,2)\): \(23/9\) vs \(25/9\). Script `/tmp/p1_01_gap01_check.py`
  temporary evidence hai, repo artifact nahi. Frozen C5 abhi bhi **unapproved/unapplied** hai.
- **Files banayi:** `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md`. **Files update:**
  `04_BLUEPRINT_GAP_REGISTER.md` (P1-01 updates + GAP-16), ye worklog. Koi aur project file edit nahi hui.
- **Overall verdict:** **CONDITIONAL GO.** Gate G1 ab bhi khula hai (L1 unresolved, publisher/model
  verification baki, Check D baki). Koi novelty/priority claim authorized nahi hai.
- **Agle sujhaye command (sirf ek):** `P1-02` — repo L1 ke liye lawful full-text closure aur
  L1/L4/L8 publisher-version comparison, saath me Check-D database-search record. Gate G1 band hue
  bagair manuscript drafting nahi hogi.

## 2026-10-21 — P1-02 Literature Closure and Novelty Gate G1

- **Repo L1 (DOI `10.1007/s12095-022-00591-6`) lawful full-text try:** Springer/ACM sirf metadata+abstract; zbMATH Zbl 1518.94136 me "Full Text: DOI" hi hai, open version nahi; koi arXiv/preprint ya IIT Patna/IIIT Bhopal repository copy nahi mila; ILL workspace se execute nahi ho sakta. ResearchGate "Full-text available" snippet verify nahi hua (fetch dusri papers par gaya) aur Academia.edu correction copy ki licence verify nahi hui — dono evidence ke roop me use nahi hue. Search commanded stopping rule par roki gayi; exact unresolved sawal **L1-Q1...L1-Q8** `P1_02_LITERATURE_CLOSURE.md` section 1.3 me likhe hain. **Status (a): Unresolved / partial overlap (potentially critical).**
- **Publisher verification:** Repo L4 — *Discrete Math.* 349(2), Feb 2026, Art. 114750, zbMATH Zbl 1582.94185 (18 p.); abstract/intro arXiv-scope se match, Theorem 4/Lemma 7 snippets spot-consistent, lekin Theorem 8/Corollary 3.5 ki publisher numbering verify nahi hui. Repo L8 — *Finite Fields Appl.* 109, Jan 2026, Art. 102712, zbMATH Zbl 1576.94064 (25 p.); **numbering arXiv se alag hai** (publisher main result "Theorem 18" vs arXiv Theorem 28; "Theorem 4"/"Corollary 7" vs arXiv Theorem 8/Corollary 11) — arXiv numbers ko publisher numbers kehna mana hai. **Statuses (b) Partial overlap (strong); (c) metadata verified, full equivalence unresolved.**
- **Check D (21 Oct 2026):** web discovery, SpringerLink/ScienceDirect/AIMS/ACM records, arXiv search (3 phrase queries — sab "produced no results"), zbMATH Open (5 known documents; baaki do fielded queries "No Documents Found"). MathSciNet/Scopus/Web of Science **NOT VERIFIED** (searched hi nahi) — coverage documented par non-exhaustive. T5/T6 ka exact duplicate kahin nahi mila, par **novelty approved nahi** hai. **Statuses (d) no counterpart found, novelty not approved; (e) documented but non-exhaustive.**
- **C5 record (sudhaar NAHI kiya):** `E[min(P-A,A)] = floor(P^2/4)/(P+1) = nu_P` exact derivation ke saath record hua. `L=1` first moment poori tarah resolved; `L>=2` par edge mean `mu_P = P(2P+1)/(6(P+1))` confirmed (linearity se orbit mean). Candidate split formula ab bhi **unapproved/unapplied** hai; variance (C6), T1-T4 par nirbharta aur Boss ka correction decision baki hai. **Status (f).**
- **Files banayi:** `P1_02_LITERATURE_CLOSURE.md`. **Files update:** `04_BLUEPRINT_GAP_REGISTER.md` (GAP-01/02/03/04/09/10/12 P1-02 updates + GAP-16 status/outcome), ye worklog. `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md` aur frozen `02_THEOREM_BLUEPRINT.md` untouched hain.
- **Overall verdict:** **CONDITIONAL GO.** Gate G1 ab bhi khula hai (L1 unresolved, publisher equivalence baki, Check D non-exhaustive). Koi novelty/priority claim authorized nahi hai.
- **Agle sujhaye command (sirf ek):** `P1-03` — Boss-enabled repo L1 full-text closure (institutional/library/ILL/author-supplied lawful copy) aur Gate-G1 re-vote; saath me C5 correction par Boss ka alag decision. Us se pehle manuscript drafting nahi hogi.
