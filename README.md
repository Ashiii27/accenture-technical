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
| [14 - OOPs (Object-Oriented Programming)](./14-oop-object-oriented-programming.md) | **NEW — dedicated OOPs chapter**: classes vs objects, the four pillars (encapsulation, abstraction, inheritance, polymorphism) with Java/Python/pseudocode examples, constructors & destructors, access modifiers, static vs instance, overloading vs overriding, abstract class vs interface, IS-A vs HAS-A, object memory & lifecycle, pseudocode tracing, exam traps, cheat sheet + **30 MCQs with full explanations** and 5 coding-style practice problems |
| [15 - OS Fundamentals](./15-os-fundamentals.md) | **NEW — OS chapter**: processes vs threads, the 5-state model, CPU scheduling (FCFS/SJF/priority/RR with a worked Gantt-chart example), memory management (virtual memory, paging, page faults, TLB, fragmentation), file systems (inodes, rwx permissions), concurrency (mutex/semaphore, deadlock's 4 conditions), interrupts/DMA, kernel types + **25 MCQs with explanations** |
| [16 - Java Basics](./16-java-basics.md) | **NEW — Java chapter**: JDK/JRE/JVM, bytecode & "write once run anywhere", 8 primitive types, operators (incl. ++ pitfalls), control flow, arrays, Strings (pool, immutability, `.equals()` vs `==`), OOP-in-Java map, exceptions (checked vs unchecked), collections essentials, 10 Java-specific exam traps + **25 MCQs with explanations** and 5 coding drills |

### Diagrams

The notes chapters embed **51 hand-built SVG diagrams** wherever a picture explains the topic faster than prose — OSI layers and encapsulation, the TCP/TLS handshakes, subnet math, IP classes, NAT, DNS, DHCP, ARP, devices & domains, crypto, cloud shared responsibility, Excel references and VLOOKUP, PowerPoint master, loop flowcharts, recursion, pass-by-value memory, bubble sort, nested-loop grids, Big-O curves, arrays vs linked lists, list types, stack vs queue, binary search, sorting cheat sheet, BST traversals, ER cardinality, normalization steps, keys hierarchy, SQL joins, clause order, B-tree index, Kadane's, array rotation, the CSS box model, the DOM tree, CSS specificity, the chapter-12 practice schema, the chapter-14 OOP set (class vs object, inheritance hierarchy, the four inheritance shapes, compile-time vs runtime polymorphism), and the chapter-15/16 set (process states, process memory layout, FCFS/SJF/RR Gantt charts, JVM architecture, the Java String pool, the Java exception hierarchy).

They live in [`images/`](./images/) as **self-contained SVG files** — no external fonts, scripts or images, so they render anywhere (GitHub, VS Code, any offline viewer).

### Mock Papers

| File | Format | Questions |
|------|--------|-----------|
| [08 - Mock Paper 1 (MCQ Standard)](./08-mock-paper-1.md) | 12 MS Office + 10 Network/Cloud + 18 Pseudocode/DSA/DBMS | 40 MCQs with detailed answers + score guide |
| [09 - Mock Paper 2 (MCQ Harder)](./09-mock-paper-2.md) | Same distribution, harder questions (subnet math, Collatz, bitwise, superkeys) | 40 MCQs with detailed answers |
| [10 - Mock Paper 3 (Coding — old pattern)](./10-mock-paper-3-coding.md) | 3 easy-medium DSA coding problems + bonus SQL | Worked solutions, checklist, extra problems |
| [13 - Mock Paper 4 (Coding — NEW 2025/2026 pattern)](./13-mock-paper-4-full-coding-round.md) | Part A DSA + Part B SQL (3 queries) + Part C Frontend (Tip Calculator with buttons/DOM) — exactly matching recent 3-part coding drives | Full solutions with explanations |
| [**hard-mocks/** — 5 HARD sets](./hard-mocks/) | **250 unique questions, 50 per set**, pitched slightly **above** Accenture level: 8 MS Office + 12 Networking/Security/Cloud + 12 DSA/DBMS/OOP/HTML-CSS-JS + 14 Pseudocode + 4 Applied SQL/code per set. Every computational answer machine-verified. | Answer keys with explanations + printable PDFs |
| [17 - Mock Paper 5 (OOPs, Java & OS)](./17-mock-paper-5-oop-java-os.md) | **NEW — CS-core gap filler**: 15 OOPs + 15 Java basics + 10 OS fundamentals MCQs, matching the "Pseudocode + OOPs" section reported in recent (Oct-2025+) drives | Answer key with explanations + score guide |

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

1. **Days 1–3:** Read chapters 01–06, **14 (OOPs)**, **15 (OS)** and **16 (Java basics)**, answering all in-chapter questions on paper.
2. **Day 4:** Read chapter 11 (HTML/CSS/JS) — type out the counter example into a file and run it in your browser to see it work.
3. **Day 5:** Read chapter 12 (SQL) — write each query in a text editor before revealing the answer.
4. **Day 6:** Take Mock Paper 1 (08) closed-book with a 40-minute timer. Review explanations. Then take Mock Paper 5 (17) — the OOPs/Java/OS CS-core paper — in 30 minutes.
5. **Day 7:** Take Mock Paper 2 (09) with timer, then Mock Paper 3 (Coding) in 60 minutes, writing actual code and running it.
6. **Day 8:** Take Mock Paper 4 (13) as a full 60-minute simulated coding round — create the HTML file and actually open it in a browser to test button clicks. Review weak spots from chapter 07 deep-dives.
7. **Final hours before exam:** Skim port numbers / OSI layers / VLOOKUP syntax / `addEventListener` syntax / JOIN + GROUP BY + HAVING template.

## How to use this guide

- **Pseudocode** must be traced **on paper**, not in your head. Build the variable table.
- **Coding** problems: type them out yourself — reading solutions does not build muscle memory.
- **Frontend practice:** actually create `.html` files and open them in your browser; click the buttons and verify behavior — don't just read the code.
- **SQL practice:** write queries freehand before revealing the hidden solutions.
- **Use the explanations** — every mock question answer includes a "why," not just a letter.
