# HARD Mock Set 2 — Accenture Technical (Above-Level)

**Level:** Harder than the 10 uploaded sets. No question here is repeated in Sets 1, 3, 4 or 5 — the whole 250-question bank is unique.
**Format:** 50 questions · **Time: 50 minutes**, closed book · **No negative marking.**

| Section | Area | Qs |
|---|---|---|
| A | MS Office & Common Applications | 8 |
| B | Networking, Security & Cloud | 12 |
| C | CS Core — DSA / DBMS / OOP / HTML-CSS-JS | 12 |
| D | Pseudocode & Code Tracing | 14 |
| E | Applied — SQL & Code Output | 4 |

---

## Section A — MS Office & Common Applications (8)

**Q1.** A1:A6 = 10, 5, 20, 15, 30, 25 and B1:B6 = 1, 2, 3, 4, 5, 6. What does `=SUMIF(A1:A6, ">15", B1:B6)` return?
- A) 21
- B) 9
- C) 6
- D) 14

**Q2.** A1 contains `Amit Kumar Sharma`. What does `=MID(A1, FIND(" ", A1) + 1, 3)` return?
- A) `"Kum"`
- B) `"mit"`
- C) `"Ami"`
- D) `"Sha"`

**Q3.** What does `=ROUNDUP(-3.2, 0)` return in Excel?
- A) −3
- B) −3.2
- C) −4
- D) 0

**Q4.** You appended 50 new rows to the source data of a PivotTable, but it still shows the old totals. What must you do?
- A) Press F9 — it recalculates everything
- B) Nothing; PivotTables update automatically
- C) Click **Refresh** (and extend the source range if the new rows fall outside it)
- D) Delete and rebuild the PivotTable

**Q5.** `=IF(AND(A1>=50, B1<100), "OK", IF(OR(A1<20, B1>200), "ALERT", "REVIEW"))` with A1 = 60, B1 = 250. Output?
- A) OK
- B) REVIEW
- C) #VALUE!
- D) ALERT

**Q6.** You formatted chapter titles manually (bold, size 16) and inserted a Table of Contents — it comes out empty. Why?
- A) The document is too long
- B) The TOC field is broken
- C) Word builds a TOC from **built-in Heading styles**, not manual formatting
- D) You must enable Track Changes first

**Q7.** Which extension is a PowerPoint **template**?
- A) `.pptx`
- B) `.potx`
- C) `.ppsx`
- D) `.pptm`

**Q8.** Which Windows shortcut opens the **clipboard history** (multiple copied items)?
- A) Win + V
- B) Ctrl + V
- C) Win + C
- D) Ctrl + Shift + V

---

## Section B — Networking, Security & Cloud (12)

**Q9.** What is the subnet mask for `/19`?
- A) 255.255.192.0
- B) 255.255.240.0
- C) 255.255.224.0
- D) 255.255.248.0

**Q10.** How many `/27` subnets can be carved out of one `/24`?
- A) 4
- B) 6
- C) 8
- D) 16

**Q11.** A branch LAN must support **60 hosts**. Which is the smallest (most efficient) prefix?
- A) /25
- B) /27
- C) /28
- D) /26

**Q12.** An engineer statically assigns `192.168.5.255/24` to a PC. What is wrong?
- A) Nothing — it is a valid host address
- B) It is the **broadcast address** of the subnet and cannot be assigned to a host
- C) It is a Class B address
- D) It is an APIPA address

**Q13.** On an 802.1Q trunk, frames belonging to the **native VLAN** are:
- A) Dropped by default
- B) Always tagged with VLAN ID 4095
- C) Transmitted **untagged**
- D) Tagged with VLAN ID 1 only if tagged explicitly

**Q14.** Three switches run STP: SW-A priority 32768, SW-B priority 32768 (MAC higher than SW-A), SW-C priority 4096. Which becomes the **root bridge**?
- A) SW-A (lowest MAC)
- B) SW-B
- C) SW-C (lowest priority wins first)
- D) Cannot be determined

**Q15.** A router learns 10.0.0.0/8 from static config, OSPF, EIGRP and RIP. Which route is installed?
- A) OSPF (AD 110)
- B) EIGRP (AD 90)
- C) The static route (AD 1 — lowest administrative distance)
- D) RIP (AD 120)

**Q16.** Correct order of the DHCP address-acquisition exchange:
- A) Discover → Offer → Request → Acknowledge
- B) Request → Offer → Discover → Acknowledge
- C) Discover → Request → Offer → Acknowledge
- D) Offer → Discover → Request → Acknowledge

**Q17.** Which DNS record type must be queried to find the **mail server** for a domain?
- A) A
- B) PTR
- C) MX
- D) CNAME

**Q18.** An attacker sends unsolicited ARP replies claiming the default gateway's IP maps to the attacker's MAC. This is:
- A) DHCP starvation
- B) ARP spoofing / poisoning (man-in-the-middle)
- C) DNS amplification
- D) SYN flood

**Q19.** "The vendor manages the runtime, middleware and operating system; you deploy and manage only your application and data." Which cloud model?
- A) IaaS
- B) SaaS
- C) On-premises
- D) PaaS

**Q20.** Which WPA3 feature protects against **offline dictionary attacks** even when a weak passphrase is used?
- A) TKIP
- B) SAE (Simultaneous Authentication of Equals)
- C) WEP shared-key authentication
- D) MAC filtering

---

## Section C — CS Core: DSA / DBMS / OOP / HTML-CSS-JS (12)

**Q21.** The recurrence `T(n) = 2T(n/2) + O(n)` solves to:
- A) O(n)
- B) O(log n)
- C) O(n log n)
- D) O(n²)

**Q22.** To maintain the **median of a continuously arriving stream** of numbers efficiently, you use:
- A) A single min-heap
- B) Two heaps — a max-heap for the lower half and a min-heap for the upper half
- C) A hash table
- D) A sorted array with binary search

**Q23.** Which statement about binary search is **FALSE**?
- A) It requires the data to be sorted
- B) It runs in O(log n) comparisons on an array
- C) It needs random access to the middle element
- D) It works efficiently on a **singly linked list** because it only needs sequential access

**Q24.** Keys 1, 2, 3, 4, 5, 6, 7 are inserted **in ascending order** into an initially empty BST. How many levels does the resulting tree have?
- A) 3
- B) 7
- C) 6
- D) 2

**Q25.** A relation has no partial or transitive dependencies but contains a non-trivial **multivalued dependency**. Which normal form is violated?
- A) 3NF
- B) 4NF
- C) BCNF
- D) 5NF

**Q26.** Using the table below, what is the **third row** returned by
`SELECT name, salary FROM Employees ORDER BY salary DESC, name ASC LIMIT 3;`?

| emp_id | name | salary |
|---|---|---|
| 1 | Amit | 50000 |
| 2 | Bala | 70000 |
| 3 | Chitra | 70000 |
| 4 | Dev | 45000 |
| 5 | Esha | 60000 |

- A) Esha, 60000
- B) Amit, 50000
- C) Chitra, 70000
- D) Dev, 45000

**Q27.** Which statement about database indexes is **FALSE**?
- A) An index can speed up `WHERE` and `JOIN` lookups
- B) An index on a column slows down `INSERT`/`UPDATE`/`DELETE` on that column
- C) A clustered index determines the physical order of rows
- D) Indexes improve every query and have **no** effect on write performance

**Q28.** Java:
```java
String a = "Hi";
String b = "Hi";
String c = new String("Hi");
System.out.print((a == b) + " " + (a == c) + " " + a.equals(c));
```
- A) `true true true`
- B) `false false true`
- C) `true false true`
- D) `true false false`

**Q29.** Which HTML5 element should wrap a **self-contained** blog post that makes sense on its own?
- A) `<section>`
- B) `<article>`
- C) `<div>`
- D) `<aside>`

**Q30.** How many of these print `true`?
```js
console.log([] == false);   // line 1
console.log(null == 0);     // line 2
console.log(NaN == NaN);    // line 3
```
- A) 0
- B) 2
- C) 1
- D) 3

**Q31.** What is `0x2F` in decimal?
- A) 45
- B) 57
- C) 62
- D) 47

**Q32.** Which HTTP method is **not** idempotent?
- A) GET
- B) PUT
- C) DELETE
- D) POST

---

## Section D — Pseudocode & Code Tracing (14)

**Q33.**
```
count ← 0
FOR i ← 1 TO 6 STEP 2
    FOR j ← 1 TO i
        count ← count + 1
    END FOR
END FOR
PRINT count
```
- A) 6
- B) 12
- C) 9
- D) 21

**Q34.**
```
FUNCTION P(b, e)
    IF e = 0
        RETURN 1
    IF e MOD 2 = 0
        half ← P(b, e DIV 2)
        RETURN half * half
    RETURN b * P(b, e - 1)
END FUNCTION
PRINT P(2, 10)
```
- A) 512
- B) 100
- C) 2048
- D) 1024

**Q35.**
```
A ← [1, 2, 3, 4, 5]
n ← 5; k ← 2
FOR r ← 1 TO k
    temp ← A[0]
    FOR i ← 0 TO n - 2
        A[i] ← A[i + 1]
    END FOR
    A[n - 1] ← temp
END FOR
PRINT A[0], A[4]
```
- A) 2 3
- B) 3 5
- C) 3 2
- D) 5 1

**Q36.**
```
A ← [3, 1, 3, 2, 1, 3]
maxc ← 0; mode ← 0
FOR i ← 0 TO 5
    c ← 0
    FOR j ← 0 TO 5
        IF A[i] = A[j]
            c ← c + 1
        END IF
    END FOR
    IF c > maxc
        maxc ← c
        mode ← A[i]
    END IF
END FOR
PRINT mode, maxc
```
- A) 1 3
- B) 3 2
- C) 2 1
- D) 3 3

**Q37.**
```
i ← 10
DO
    i ← i + 2
WHILE i < 5
PRINT i
```
- A) 10
- B) 0
- C) 12
- D) Infinite loop

**Q38.**
```
s ← "  data  structures  "
count ← 0
prev ← ' '
FOR each ch IN s
    IF ch <> ' ' AND prev = ' '
        count ← count + 1
    END IF
    prev ← ch
END FOR
PRINT count
```
- A) 3
- B) 4
- C) 1
- D) 2

**Q39.**
```
n ← 29; i ← 2; flag ← TRUE
WHILE i * i <= n
    IF n MOD i = 0
        flag ← FALSE
        BREAK
    END IF
    i ← i + 1
END WHILE
PRINT flag, i
```
- A) TRUE 5
- B) TRUE 6
- C) FALSE 29
- D) TRUE 29

**Q40.** (Arrays are passed **by reference**)
```
FUNCTION bump(arr)
    FOR i ← 0 TO LENGTH(arr) - 1
        arr[i] ← arr[i] * 2
    END FOR
END FUNCTION
A ← [1, 2, 3]
bump(A)
PRINT A[0], A[2]
```
- A) 1 3
- B) 2 3
- C) 2 6
- D) Runtime error

**Q41.**
```
A ← [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxEnding ← A[0]; maxSoFar ← A[0]
FOR i ← 1 TO 8
    maxEnding ← MAX(A[i], maxEnding + A[i])
    maxSoFar ← MAX(maxSoFar, maxEnding)
END FOR
PRINT maxSoFar
```
- A) 7
- B) 4
- C) 11
- D) 6

**Q42.**
```
a ← 0; b ← 1
FOR i ← 1 TO 8
    t ← a + b
    a ← b
    b ← t
END FOR
PRINT a
```
- A) 13
- B) 21
- C) 34
- D) 55

**Q43.**
```
m ← 84; att ← 68
IF att < 75
    g ← "F"
ELSE IF m >= 90
    g ← "A"
ELSE IF m >= 80
    g ← "B"
ELSE
    g ← "C"
END IF
PRINT g
```
- A) F
- B) A
- C) B
- D) C

**Q44.**
```
n ← 29; c ← 0
WHILE n > 0
    n ← n AND (n - 1)
    c ← c + 1
END WHILE
PRINT c
```
- A) 3
- B) 5
- C) 4
- D) 29

**Q45.**
```
n ← 9875
WHILE n > 9
    s ← 0
    WHILE n > 0
        s ← s + n MOD 10
        n ← n DIV 10
    END WHILE
    n ← s
END WHILE
PRINT n
```
- A) 9
- B) 11
- C) 29
- D) 2

**Q46.**
```
count ← 0
FOR i ← 1 TO 3
    FOR j ← 1 TO 3
        IF j > i
            BREAK
        END IF
        count ← count + 1
    END FOR
END FOR
PRINT count
```
- A) 9
- B) 6
- C) 3
- D) 7

---

## Section E — Applied: SQL & Code Output (4)

Tables for Q47–Q48:

`Departments(dept_id, dept_name)` → (1, HR), (2, IT), (3, FIN)
`Employees(emp_id, name, dept_id)` → (1, Amit, 1), (2, Bala, 2), (3, Chitra, 2), (4, Dev, NULL)

**Q47.** How many rows does this return?
```sql
SELECT d.dept_name, e.name
FROM Departments d
INNER JOIN Employees e ON d.dept_id = e.dept_id;
```
- A) 4
- B) 2
- C) 3
- D) 5

**Q48.** What value does this aggregate query return?
```sql
SELECT COUNT(*) FROM Employees WHERE dept_id <> 2;
```
- A) 2
- B) 3
- C) 4
- D) 1

**Q49.** Python:
```python
def add(x, lst=[]):
    lst.append(x)
    return lst

print(add(1), add(2))
```
- A) `[1] [2]`
- B) `[1] [1]`
- C) `[1] [1, 2]`
- D) `TypeError`

**Q50.** JavaScript:
```js
let x = 5;
function f() { console.log(x); let x = 3; }
f();
```
- A) 5
- B) 3
- C) `undefined`
- D) `ReferenceError: Cannot access 'x' before initialization`

---

---

# ⛔ STOP — Answer Key for Set 2

## Quick grid

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | D | A | C | C | D | C | B | A | C | C |

| Q | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | D | B | C | C | C | A | C | B | D | B |

| Q | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | C | B | D | B | B | A | D | C | B | C |

| Q | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | D | D | C | D | C | D | C | D | B | C |

| Q | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | D | B | A | C | D | B | C | D | C | D |

## Explanations

**Q1 — D.** Rows where A > 15: 20 (B3 = 3), 30 (B5 = 5), 25 (B6 = 6) → 3 + 5 + 6 = **14**. SUMIF sums the *third* argument, not the tested range.

**Q2 — A.** `FIND(" ")` = 5 → `MID(A1, 6, 3)` = characters 6–8 of "Amit Kumar Sharma" = **"Kum"**.

**Q3 — C.** ROUNDUP rounds **away from zero**, so −3.2 → **−4** (not −3). `ROUND(-3.2,0)` would give −3.

**Q4 — C.** PivotTables do **not** auto-refresh; press Refresh (or Refresh All). F9 recalculates worksheet formulas, which is not the same thing. Also extend the source range / use a Table if new rows sit outside it.

**Q5 — D.** `AND(60>=50, 250<100)` → FALSE, so we fall to the second IF: `OR(60<20, 250>200)` → TRUE → **ALERT**.

**Q6 — C.** The TOC is generated from paragraphs using built-in Heading 1/2/3 styles. Manual bold + size 16 looks identical on screen but is invisible to the TOC field.

**Q7 — B.** `.potx` = template, `.pptx` = presentation, `.ppsx` = slide show, `.pptm` = macro-enabled presentation.

**Q8 — A.** Win + V opens clipboard history (once enabled); Ctrl + V is a normal paste of the last item only.

**Q9 — C.** /19 = 8 + 8 + 3 network bits → third octet 224 → **255.255.224.0**.

**Q10 — C.** /27 vs /24 = 3 extra network bits → 2³ = **8** subnets.

**Q11 — D.** Need 2^h − 2 ≥ 60 → h = 6 (62 hosts) → prefix = 32 − 6 = **/26**.

**Q12 — B.** In 192.168.5.0/24 the last address (`.255`) is the **directed broadcast** address and is not assignable to a host.

**Q13 — C.** Native-VLAN frames cross an 802.1Q trunk **untagged**; a mismatch of native VLAN on the two ends causes VLAN hopping/leakage.

**Q14 — C.** Bridge ID = priority first, then MAC. SW-C (4096) beats the default 32768 regardless of MAC.

**Q15 — C.** Lowest administrative distance wins: static = 1 < EIGRP 90 < OSPF 110 < RIP 120.

**Q16 — A.** **DORA**: Discover → Offer → Request → Acknowledge. The client broadcasts Discover; the server offers; the client requests; the server acknowledges.

**Q17 — C.** `MX` = mail exchanger. `A`/`AAAA` = name→address, `PTR` = address→name (reverse), `CNAME` = alias→canonical name.

**Q18 — B.** ARP spoofing/poisoning — poisoning the ARP caches of hosts and the gateway to become a man-in-the-middle.

**Q19 — D.** PaaS (e.g. Azure App Service, Heroku). IaaS = you manage the OS too; SaaS = you only use the software.

**Q20 — B.** WPA3-Personal replaces the PSK 4-way handshake with **SAE** (dragonfly), so an offline dictionary attack on captured frames is not possible.

**Q21 — C.** Master theorem: a = 2, b = 2, f(n) = O(n) = Θ(n^{log_b a}) → **O(n log n)** (merge sort).

**Q22 — B.** Two heaps: max-heap for the lower half, min-heap for the upper half, rebalanced so their sizes differ by ≤ 1 → median in O(1), insert O(log n).

**Q23 — D.** Binary search on a singly linked list costs O(n) because reaching the middle needs traversal — no random access.

**Q24 — B.** Sorted insertion into an unbalanced BST degenerates into a chain of **7 levels** (height 6, search O(n)).

**Q25 — B.** Multivalued dependencies are removed by **4NF**. The relation can already be in BCNF and still violate 4NF.

**Q26 — A.** Order: Bala 70000, Chitra 70000 (tie broken by name ascending), then **Esha 60000** → third row = Esha.

**Q27 — D.** Indexes cost disk space and slow down writes (the index must be updated). They also do not help queries that must scan most rows.

**Q28 — C.** `a` and `b` are both string-literal interned references → `==` true. `new String(...)` forces a fresh object → `==` false, but `equals` compares content → true.

**Q29 — B.** `<article>` = self-contained, independently distributable content. `<section>` = a thematic grouping; `<aside>` = tangentially related.

**Q30 — C.** Only line 1: `[] == false` → `[]` coerces to `""` → `0`, `false` → `0` → **true**. `null == 0` → false (null only == null/undefined). `NaN == NaN` → always false.

**Q31 — D.** 0x2F = 2×16 + 15 = **47**.

**Q32 — D.** GET, PUT, DELETE, HEAD, OPTIONS are idempotent (repeating has the same effect). **POST** creates a new resource each time.

**Q33 — C.** i = 1, 3, 5 → inner runs 1 + 3 + 5 = **9**.

**Q34 — D.** Exponentiation by squaring: 2¹⁰ = **1024** (with only ~4 multiplications, not 10).

**Q35 — C.** Two left rotations: [1,2,3,4,5] → [2,3,4,5,1] → [3,4,5,1,2] → `A[0] = 3`, `A[4] = 2`.

**Q36 — D.** Counts: 3 → 3, 1 → 2, 2 → 1. i = 0 gives c = 3 > 0 → mode 3, maxc 3. i = 2 (value 3) gives c = 3, **not > 3**, so nothing changes (strict `>`). → `3 3`.

**Q37 — C.** A DO…WHILE always executes the body once, so `i` becomes 12 and only then is the condition tested → prints **12**.

**Q38 — D.** Count space→non-space transitions: "data" (1) and "structures" (2). Leading/trailing runs don't count because `prev` starts as a space and the trailing spaces never transition to non-space → **2**.

**Q39 — B.** i runs 2,3,4,5 (25 ≤ 29), then 6 makes `i*i = 36 > 29` and the loop exits with **i = 6**, flag still TRUE (29 is prime).

**Q40 — C.** Arrays are reference types: `bump` mutates the caller's array → [2,4,6] → `2 6`.

**Q41 — D.** Kadane's algorithm: best subarray 4, −1, 2, 1 → **6**.

**Q42 — B.** After 8 iterations: (a,b) = (1,1), (1,2), (2,3), (3,5), (5,8), (8,13), (13,21), (21,34) → `a = 21` (b = 34 = F₉).

**Q43 — A.** The attendance test comes **first**, so 68 < 75 short-circuits to **F** even though 84 marks would be a B.

**Q44 — C.** Brian Kernighan: `n & (n-1)` clears the lowest set bit. 29 = `11101` has **4** set bits → 4 iterations.

**Q45 — D.** Digital root: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = **2**.

**Q46 — B.** Triangular count: i = 1 → 1, i = 2 → 2, i = 3 → 3 → **6**. The BREAK only skips the tail of each inner loop.

**Q47 — C.** Matches: HR–Amit, IT–Bala, IT–Chitra = **3**. Dev (NULL dept_id) never matches; FIN has no employees.

**Q48 — D.** `dept_id <> 2` is UNKNOWN for Dev's NULL → excluded. Only Amit (dept 1) qualifies → **1**. Use `WHERE dept_id <> 2 OR dept_id IS NULL` to keep NULLs.

**Q49 — C.** The default list is created **once** at function definition, so both calls share it → `[1] [1, 2]`. Use `lst=None` and create a new list inside.

**Q50 — D.** `let` is hoisted but stays in the **temporal dead zone** until initialisation, so the inner `x` shadows the outer one and logging before `let x = 3` throws a ReferenceError.

---

### Score guide (Set 2)

| Score | Verdict |
|---|---|
| 43–50 | Excellent — you are safely above Accenture level |
| 34–42 | Good — revise the missed topics and re-sit |
| 25–33 | Needs work — return to the notes, then retry this set after 3 days |
| < 25 | Go back to chapters 01–06 before Set 3 |
