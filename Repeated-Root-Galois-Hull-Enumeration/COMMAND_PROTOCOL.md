# Command Protocol — ChatGPT (Commander) → Arena (Worker) → ChatGPT

## Roles

| Kaun | Kaam |
|---|---|
| **Tum (User)** | Boss. Final decision, aur dono AI ke beech message le jaana (copy-paste). |
| **ChatGPT** | Commander: plan banana, ek-ek command dena, Arena ki report ki jaanch (review), agla command tay karna. Repo access NAHI hai. |
| **Arena AI (mai)** | Worker: repo me files banana/badlaav, code chalana, proof likhna, manuscript banana, har command par report dena. |

Dhyaan: ChatGPT aur Arena seedha baat **nahi** kar sakte. Har kadam tumhare copy-paste se chalega:
**ChatGPT command dega → tum Arena me paste karoge → Arena kaam karke report dega → tum woh report ChatGPT me paste karoge → ChatGPT agli command dega.**

---

## COMMAND format (ChatGPT is template me command dega)

```text
COMMAND ID: P<phase>-<number>        (jaise P1-01)
GOAL: ek line me kya hasil karna hai
CONTEXT: jo peeche ka kaam / jankari is command ke liye zaroori hai
TASKS:
  1. ...
  2. ...
FILES TO CREATE/EDIT: exact file naam/paths
ACCEPTANCE CRITERIA: kaam kab "ho gaya" mana jayega (ginati/sakshya ke saath)
RESTRICTIONS: kya NAHI karna (dawe, convention-change, scope se bahar, waghera)
REPORT BACK: filein badli, praman (output/theorem), rukawat, agla sujhaya command
```

Ek baar me **ek hi command**. Agar command bada ho to ChatGPT use chhote tukdo me todega.

## REPORT format (Arena, matlab mai, har command ke baad yahi dunga)

```text
REPORT FOR COMMAND P<phase>-<number>
STATUS: DONE / PARTIAL / BLOCKED
WHAT I DID: ...
FILES CHANGED: ...
RESULTS / EVIDENCE: (theorem statements, code output, audit findings — sakshya ke saath)
PROBLEMS FOUND: (koi galti, shanka, literature takkar — chhupana mana hai)
NEXT SUGGESTED COMMAND: ...
QUESTIONS FOR COMMANDER: (agar koi faisla chahiye)
```

Har report ke saath mai `ARENA_WORKLOG.md` me ek entry bhi jodunga, taaki poori kahani ek jagah rahe —
galti pakdi jaye to wahan "galti aur sudhaar" laal nishan ke saath likha jayega, mitaaya nahi jayega.

## Commander (ChatGPT) ke liye niyam

1. Bina report padhe agli command nahi. Acceptance criteria ek-ek karke jaanchna.
2. Koi bhi mathematical dawa bina sakshya (proof sketch / code check / citation) ke aage nahi badhana.
3. References, DOI, lekhak-naam — kabhi andaz se nahi; shanka ho to Arena ko "VERIFY" wali command dena.
4. Phase-gate todna mana: Phase 1 (audit) band hue bagair manuscript drafting ki command nahi (Gate G1);
   `P=1` recovery har formula ke liye jaanchi jayegi (Gate G3).
5. Har command se pehle user ko 2–3 line me Hinglish me samjhana ki ye command kya karegi.

## Worker (Arena) ke liye niyam

1. Command ke bahar scope nahi badhaunga; bada badlaav chahiye to pehle report me poochhunga.
2. Har badlaav file me hoga (chat me khoya hua kaam nahi), har file ka path report me dunga.
3. Code chalega to output file me save hoga; proof likhega to theorem-statement file me bhi update hoga.
4. Kuch galat mile (apni hi purani baat bhi) to report me saaf likhunga — "sara samajh gaya" wala jhootha bharosa nahi.
