# Accenture Technical Assessment — Study Guide

This repository contains detailed notes, deep-dive explanations, and **four full-length mock papers (with answer keys)** for the Accenture technical assessment, including the **2025/2026 new pattern** (DSA + SQL + Frontend HTML/CSS/JS in the coding round).

## Repository Contents

### Notes & Deep Explanations

| File | Topics Covered |
|------|----------------|
| [01 - Networking, Security & Cloud](./01-networking-security-cloud.md) | OSI, TCP/IP, IP addressing, protocols, devices, security, crypto, cloud + 40 MCQs |
| [02 - MS Office & Common Applications](./02-ms-office-general.md) | Word, Excel, PowerPoint, Windows/general PC knowledge + 22 MCQs |
| [03 - Pseudocode](./03-pseudocode.md) | IF/ELSE, FOR/WHILE, nested loops, functions, recursion, arrays, strings, pass-by-value/reference, bubble sort + 15 trace-by-hand problems |
| [04 - DSA (MCQ)](./04-dsa.md) | Arrays, Linked Lists, Stacks, Queues, Binary Search, Sorting, Trees/BST, Big-O + 20 MCQs |
| [05 - DBMS (MCQ)](./05-dbms.md) | ER diagrams, normalization, keys, SQL JOINs, ACID, indexing, triggers/views/procs + 21 MCQs |
| [06 - Coding Assessment](./06-coding-practice.md) | Worked solutions: strings, arrays, numbers, patterns, sorting, linked lists, matrices + challenge problems |
| [07 - Deep Dives — Tricky Topics](./07-deep-dives-tricky-topics.md) | **Visual walkthroughs**: subnet math, TCP handshake, DNS, DHCP, ARP, switches vs routers, TLS handshake, VLOOKUP traps, recursion template, bitwise operators, increment/decrement, pass-by-value memory diagrams, normalization worked example, JOIN Venn diagrams, Kadane's, slow-fast pointer, binary-search loop conditions, OOPs, **exam traps & trick questions catalog** |
| [11 - HTML, CSS & JavaScript](./11-html-css-js.md) | **NEW — frontend section**: HTML tags/attributes, CSS selectors/properties/flexbox/box model, JS variables/functions, **DOM manipulation** (getElementById, querySelector, textContent, style, classList, addEventListener, createElement, input values) + a worked counter-app example + 12 practice questions with solutions |
| [12 - SQL Practice Queries](./12-sql-practice.md) | **NEW — SQL coding section**: 15 graduated SQL problems (SELECT/WHERE/JOIN/GROUP BY/HAVING/ORDER BY/LIMIT/LIKE/IN/self-join/CASE/dates) using a 4-table schema with hidden solutions + a timed 3-question mock SQL round |

### Mock Papers

| File | Format | Questions |
|------|--------|-----------|
| [08 - Mock Paper 1 (MCQ Standard)](./08-mock-paper-1.md) | 12 MS Office + 10 Network/Cloud + 18 Pseudocode/DSA/DBMS | 40 MCQs with detailed answers + score guide |
| [09 - Mock Paper 2 (MCQ Harder)](./09-mock-paper-2.md) | Same distribution, harder questions (subnet math, Collatz, bitwise, superkeys) | 40 MCQs with detailed answers |
| [10 - Mock Paper 3 (Coding — old pattern)](./10-mock-paper-3-coding.md) | 3 easy-medium DSA coding problems + bonus SQL | Worked solutions, checklist, extra problems |
| [13 - Mock Paper 4 (Coding — NEW 2025/2026 pattern)](./13-mock-paper-4-full-coding-round.md) | Part A DSA + Part B SQL (3 queries) + Part C Frontend (Tip Calculator with buttons/DOM) — exactly matching recent 3-part coding drives | Full solutions with explanations |
| [**hard-mocks/** — 5 HARD sets](./hard-mocks/) | **250 unique questions, 50 per set**, pitched slightly **above** Accenture level: 8 MS Office + 12 Networking/Security/Cloud + 12 DSA/DBMS/OOP/HTML-CSS-JS + 14 Pseudocode + 4 Applied SQL/code per set. Every computational answer machine-verified. | Answer keys with explanations + printable PDFs |

## Accenture Exam Pattern (2025–2026 drives)

| Round | Section | Questions | Time |
|-------|---------|-----------|------|
| 1 | Behavioral + Cognitive (Gamified) | Varies | ~40 min |
| 2 | **Technical MCQs** | ~40–45 | ~40–50 min shared |
|   | └ Common Apps & MS Office | ~12 | |
|   | └ Pseudocode (incl. DSA/DBMS/OOPs/bitwise) | ~18 | |
|   | └ Networking, Security & Cloud | ~10 | |
| 3 | **Coding Assessment** (3 parts) | 3 problems | 45–60 min |
|   | └ Part 1: DSA (easy-medium array/string) | 1 | |
|   | └ Part 2: SQL query (JOINs + GROUP BY + HAVING) | 1 | |
|   | └ Part 3: Frontend (HTML/CSS/JS with DOM click handler) | 1 | |
| 4 | Communication Assessment | ~20 spoken tasks | ~30 min |

**Sectional cutoffs apply. No negative marking — guess if you must.**
Pseudocode is the highest-weighted MCQ section and the most common reason for rejection. The frontend/SQL parts are new in late-2025/2026 drives — do NOT skip chapters 11 and 12.

## Recommended 8-Day Study Plan

1. **Days 1–3:** Read chapters 01–06, answering all in-chapter questions on paper.
2. **Day 4:** Read chapter 11 (HTML/CSS/JS) — type out the counter example into a file and run it in your browser to see it work.
3. **Day 5:** Read chapter 12 (SQL) — write each query in a text editor before revealing the answer.
4. **Day 6:** Take Mock Paper 1 (08) closed-book with a 40-minute timer. Review explanations.
5. **Day 7:** Take Mock Paper 2 (09) with timer, then Mock Paper 3 (Coding) in 60 minutes, writing actual code and running it.
6. **Day 8:** Take Mock Paper 4 (13) as a full 60-minute simulated coding round — create the HTML file and actually open it in a browser to test button clicks. Review weak spots from chapter 07 deep-dives.
7. **Final hours before exam:** Skim port numbers / OSI layers / VLOOKUP syntax / `addEventListener` syntax / JOIN + GROUP BY + HAVING template.

## How to use this guide

- **Pseudocode** must be traced **on paper**, not in your head. Build the variable table.
- **Coding** problems: type them out yourself — reading solutions does not build muscle memory.
- **Frontend practice:** actually create `.html` files and open them in your browser; click the buttons and verify behavior — don't just read the code.
- **SQL practice:** write queries freehand before revealing the hidden solutions.
- **Use the explanations** — every mock question answer includes a "why," not just a letter.
