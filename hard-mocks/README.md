# HARD Mocks — 5 sets, above Accenture level

A companion to `Mocks/` (the 10 uploaded sets). **Same syllabus, harder questions.**

- **250 questions**, 50 per set — **every question is unique across all five sets** (verified: no duplicate or near-duplicate item).
- Every computational answer was **machine-verified** (subnet math with Python's `ipaddress`, every pseudocode trace executed, every SQL query run on SQLite, every JS/Java/Python snippet executed).
- Each set ends with a **⛔ STOP** divider before the answer key, and every answer includes *why* — not just the letter.

## What changed compared with the 10 uploaded sets

| | Uploaded sets (1–10) | These HARD sets |
|---|---|---|
| Questions | 45 | 50 |
| Sections | 3 (CS, Networking, Pseudocode) | 5 (MS Office / Networking / CS Core / Pseudocode / Applied SQL+code) |
| MS Office & Common Apps | not covered | 8 per set (a real Accenture section) |
| Applied SQL / frontend code | not covered | 4 per set (output prediction, query choice) |
| Networking depth | "which port / which protocol" | subnet math (network, broadcast, usable hosts, summarisation, wildcard masks), TCP states, TLS key exchange, VLAN/STP/AD, cloud models, attacks |
| Pseudocode depth | single loops — sum, factorial, reverse, palindrome, max | nested loops with `BREAK`/`CONTINUE`, pass-by-value vs by-reference, global vs local, recursion call counts, Kadane, digital root, in-place reversal/rotation, two-pointer merge, bit tricks |
| Distractors | random numbers | built from the classic traps (off-by-one, `COUNT(col)` vs `COUNT(*)`, `= NULL`, var hoisting, `this` in arrow functions, `VAR` vs `LET`, LEFT JOIN + WHERE, LIMIT offset) |

## Files

| File | Contents |
|---|---|
| [Set-1.md](./Set-1.md) | 50 questions + key — VLOOKUP traps, subnet math, TLS/ECDHE, CSRF, LRU cache, 3NF, Collatz, Kadane-style traces, HTMLCollection |
| [Set-2.md](./Set-2.md) | 50 questions + key — SUMIF/ROUNDUP, /19–/27 sizing, STP/AD/DHCP/WPA3, merge-sort recurrence, BST degeneration, String pool, mutable default args, TDZ |
| [Set-3.md](./Set-3.md) | 50 questions + key — TEXTJOIN/TRIM, IPv6 + SFTP + firewalls, amortised O(1), BCNF vs 3NF, virtual dispatch from a constructor, matrix multiply, Hanoi |
| [Set-4.md](./Set-4.md) | 50 questions + key — INDEX/MATCH, freeze panes, wildcard masks, IPsec, SPF/DKIM, stack permutations, non-repeatable read, closures, `border-box`, mutual recursion |
| [Set-5.md](./Set-5.md) | 50 questions + key — COUNTIF wildcards, ISBLANK trap, VLAN/Kerberos/IaC/serverless, BFS shortest path, anti-join, heap indexing, stack simulation, `LIMIT offset` trap |

Each set also has a matching **PDF** (`Set-1.pdf` … `Set-5.pdf`) for printing / phone practice.

## Section pattern (identical in every set)

| Section | Area | Qs | Topics rotated across the 5 sets |
|---|---|---|---|
| A | MS Office & Common Applications | 8 | Excel formulas & references, Word, PowerPoint, Windows/shortcuts, hardware & file formats |
| B | Networking, Security & Cloud | 12 | Subnetting, OSI, TCP/UDP, routing, DNS/DHCP, switching, security, crypto, cloud models & shared responsibility |
| C | CS Core | 12 | Complexity, arrays/LL/stack/queue/trees/hashing, sorting & searching, DBMS (normal forms, keys, SQL, indexes, transactions), OOP, HTML/CSS, JavaScript, number systems |
| D | Pseudocode & Code Tracing | 14 | Loops, nested loops, recursion, parameter passing, strings, arrays, matrices, bitwise, stacks |
| E | Applied | 4 | SQL output prediction / query choice, code output in Java, Python, JavaScript + DOM |

## How to use them

1. **Sit one set at a time**, closed book, **50 minutes on the clock** (1 min/question — Accenture's real MCQ pace).
2. Trace section D **on paper** with a variable table. Mental arithmetic is the #1 cause of wrong answers here.
3. Stop at the ⛔ divider. Score yourself with the grid below, then read the explanations for everything you got wrong **or guessed**.
4. Anything below ~70 % in a section → re-read the matching chapter in the repo root (`01`–`07`, `11`, `12`), then re-sit that section three days later.
5. Because the questions are unique, you can use all five as a progression: Set 1 → Set 5, one per day, then re-sit your weakest set in the final week.

### Master answer grid (all 250)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Set 1** | C | A | D | C | D | B | B | C | C | D |
| **Set 2** | D | A | C | C | D | C | B | A | C | C |
| **Set 3** | C | B | D | A | C | B | D | A | B | C |
| **Set 4** | B | D | A | C | B | D | C | A | D | B |
| **Set 5** | C | D | B | C | D | B | C | A | D | C |

| Q | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Set 1** | A | C | A | B | B | D | B | B | B | A |
| **Set 2** | D | B | C | C | C | A | C | B | D | B |
| **Set 3** | D | A | C | D | B | A | D | C | B | A |
| **Set 4** | C | A | D | B | C | A | D | B | C | A |
| **Set 5** | B | D | A | C | B | D | A | C | B | D |

| Q | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Set 1** | C | B | B | C | C | C | D | D | B | B |
| **Set 2** | C | B | D | B | B | A | D | C | B | C |
| **Set 3** | D | B | A | C | D | B | D | B | C | D |
| **Set 4** | D | B | A | C | D | B | A | C | D | B |
| **Set 5** | A | D | C | A | D | B | C | A | D | B |

| Q | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Set 1** | A | C | C | D | B | C | D | C | D | C |
| **Set 2** | D | D | C | D | C | D | C | D | B | C |
| **Set 3** | B | A | C | D | B | A | D | B | C | A |
| **Set 4** | A | C | D | A | C | D | B | A | C | D |
| **Set 5** | A | C | D | B | C | A | D | B | C | D |

| Q | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Set 1** | B | C | D | B | C | D | C | C | D | C |
| **Set 2** | D | B | A | C | D | B | C | D | C | D |
| **Set 3** | D | B | C | A | D | B | C | A | D | B |
| **Set 4** | B | A | C | D | B | C | B | A | D | C |
| **Set 5** | A | B | C | D | A | B | C | A | D | B |

### Scoring (per set, out of 50)

| Score | Verdict |
|---|---|
| 43–50 | Comfortably above Accenture level |
| 34–42 | On track — revise the topics you dropped |
| 25–33 | At risk — re-read the notes, re-sit in 3 days |
| < 25 | Rebuild the fundamentals (chapters 01–07) first |
