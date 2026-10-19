# HARD Mock Set 3 — Accenture Technical (Above-Level)

**Level:** Harder than the 10 uploaded sets. Unique questions — nothing here repeats Sets 1, 2, 4 or 5.
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

**Q1.** A1:A5 = 5, 20, 10, 15, 8 and B1:B5 = 1, 2, 3, 4, 5. What does `=SUMPRODUCT((A1:A5>10) * B1:B5)` return?
- A) 15
- B) 8
- C) 6
- D) 3

**Q2.** What does `=TEXT(0.75, "0.0%")` display in Excel?
- A) `0.8%`
- B) `75.0%`
- C) `75%`
- D) `.75`

**Q3.** What does `=LEN(TRIM("  Hello  World  "))` return?
- A) 15
- B) 13
- C) 10
- D) 11

**Q4.** `=IF(A1 > 50, B1 * 0.1, B1 * 0.05)` with A1 = 50 and B1 = 200. Result?
- A) 10
- B) 20
- C) 5
- D) 0

**Q5.** In MS Word, what is a **section break** used for?
- A) Splitting one document into two files
- B) Inserting a page number
- C) Applying a different header, page numbering or page orientation **within** the same document
- D) Ending a paragraph

**Q6.** Which PowerPoint view shows all slides as thumbnails so you can reorder and set timings?
- A) Reading View
- B) Slide Sorter View
- C) Notes Page View
- D) Outline View

**Q7.** You must email 50 recipients without letting them see each other's addresses. Which field?
- A) To
- B) Cc
- C) Reply-To
- D) Bcc

**Q8.** Which Excel chart type best shows the **relationship/correlation between two numeric variables**?
- A) Scatter (XY) chart
- B) Pie chart
- C) Column chart
- D) Treemap

---

## Section B — Networking, Security & Cloud (12)

**Q9.** A subnet must support **100 hosts**. Smallest prefix?
- A) /24
- B) /25
- C) /26
- D) /27

**Q10.** `10.0.0.0/24` is divided into 4 equal subnets. Which is the **second** subnet?
- A) 10.0.0.0/26
- B) 10.0.0.128/26
- C) 10.0.0.64/26
- D) 10.0.0.32/26

**Q11.** Which is a **valid host address** in `192.168.1.0/28`?
- A) 192.168.1.0
- B) 192.168.1.15
- C) 192.168.1.16
- D) 192.168.1.14

**Q12.** The IPv6 **loopback** address is:
- A) `::1`
- B) `FE80::1`
- C) `FF02::1`
- D) `2001:db8::1`

**Q13.** Which prefix is reserved for IPv6 **link-local** addresses?
- A) `2000::/3`
- B) `FC00::/7`
- C) `FE80::/10`
- D) `FF00::/8`

**Q14.** Which protocol replaces ARP for address resolution in IPv6?
- A) RARP
- B) DHCPv6
- C) IGMP
- D) NDP (Neighbor Discovery, using ICMPv6)

**Q15.** Which file-transfer protocol runs **over SSH**?
- A) FTPS
- B) SFTP
- C) TFTP
- D) SMB

**Q16.** Which statement about TCP/UDP is **FALSE**?
- A) UDP is connection-oriented
- B) TCP delivers bytes in order
- C) TCP uses a three-way handshake
- D) UDP has no built-in congestion control

**Q17.** Which device can filter traffic using **IP addresses and port numbers** (Layers 3–4)?
- A) Hub
- B) Layer-2 switch
- C) Repeater
- D) Firewall

**Q18.** Automatically adding instances at peak load and removing them afterwards is called:
- A) Provisioning
- B) Orchestration
- C) Auto-scaling / elasticity
- D) Load-balancing

**Q19.** The most effective control against **credential stuffing** (replayed leaked passwords) is:
- A) Password complexity rules
- B) Multi-factor authentication (MFA)
- C) Longer session timeouts
- D) Antivirus

**Q20.** A **Type 1 (bare-metal) hypervisor**:
- A) Runs directly on the host hardware, with no host OS beneath it
- B) Runs as an application on top of a host OS
- C) Is another name for a container runtime
- D) Cannot run more than one VM

---

## Section C — CS Core: DSA / DBMS / OOP / HTML-CSS-JS (12)

**Q21.** Which operation is **O(1) amortised** but O(n) in the worst case?
- A) Search in a balanced BST
- B) Deletion from a hash table
- C) Push onto a linked-list stack
- D) Appending to a dynamically-resizing array

**Q22.** Which sort is optimal for an **almost-sorted** array?
- A) Heap sort
- B) Insertion sort
- C) Selection sort
- D) Quick sort with last-element pivot

**Q23.** Which structure checks whether parentheses in an expression are **balanced**?
- A) Stack
- B) Queue
- C) Binary tree
- D) Graph

**Q24.** A **complete** binary tree has 31 nodes. How many leaves does it have?
- A) 15
- B) 31
- C) 16
- D) 8

**Q25.** Which statement about 3NF and BCNF is TRUE?
- A) Every 3NF relation is in BCNF
- B) BCNF and 3NF are identical
- C) BCNF allows transitive dependencies
- D) Every BCNF relation is in 3NF, but a 3NF relation need not be in BCNF

**Q26.** `R(A,B,C,D)` with FDs `A→B`, `B→C`, `C→D`. What is the candidate key?
- A) `{A,B}`
- B) `{A}`
- C) `{A,B,C}`
- D) `{D}`

**Q27.** Table `Orders(id, cust, amount)` → (1,A,100), (2,B,250), (3,A,300), (4,C,50), (5,B,200). Which customer appears **first**?
```sql
SELECT cust, COUNT(*) c, SUM(amount) s
FROM Orders
GROUP BY cust
HAVING SUM(amount) >= 300
ORDER BY c DESC, s DESC;
```
- A) C
- B) A
- C) No rows returned
- D) B

**Q28.** Which ACID property guarantees concurrent transactions behave as if executed **serially**?
- A) Atomicity
- B) Isolation
- C) Durability
- D) Consistency

**Q29.** Java — what is printed by `new B();`?
```java
class A { A() { show(); } void show() { System.out.print("A"); } }
class B extends A { void show() { System.out.print("B"); } }
```
- A) `A`
- B) `AB`
- C) `B`
- D) Compile-time error

**Q30.** Which HTML5 element is meant to contain the **primary navigation links** of a page?
- A) `<header>`
- B) `<menu>`
- C) `<div id="nav">`
- D) `<nav>`

**Q31.** JavaScript:
```js
const arr = [1, 2, 3];
console.log(arr.map(x => x * 2).filter(x => x > 2));
```
- A) `[2, 4, 6]`
- B) `[4, 6]`
- C) `[6]`
- D) `[2, 4]`

**Q32.** Minimum number of bits required to represent **500 distinct values**?
- A) 9
- B) 8
- C) 10
- D) 16

---

## Section D — Pseudocode & Code Tracing (14)

**Q33.**
```
a ← 0; b ← 0
FOR i ← 1 TO 5
    IF i MOD 2 = 0
        a ← a + i
    ELSE
        b ← b + i
    END IF
END FOR
PRINT a, b
```
- A) 15 0
- B) 5 10
- C) 6 9
- D) 9 6

**Q34.**
```
FUNCTION SD(n)
    IF n < 10
        RETURN n
    RETURN n MOD 10 + SD(n DIV 10)
END FUNCTION
PRINT SD(4567)
```
- A) 4
- B) 10
- C) 4567
- D) 22

**Q35.** (`x` is a **global** variable)
```
x ← 10
FUNCTION f(n)
    x ← x + n
    RETURN x
END FUNCTION
r1 ← f(3)
r2 ← f(5)
PRINT r1 + r2
```
- A) 23
- B) 31
- C) 18
- D) 26

**Q36.** How many times does a character repeat consecutively in `"mississippi"`?
```
s ← "mississippi"
count ← 0
FOR i ← 0 TO LENGTH(s) - 2
    IF s[i] = s[i + 1]
        count ← count + 1
    END IF
END FOR
PRINT count
```
- A) 3
- B) 4
- C) 2
- D) 5

**Q37.**
```
i ← 1; j ← 10; c ← 0
WHILE i < j
    i ← i + 2
    j ← j - 1
    c ← c + 1
END WHILE
PRINT c, i, j
```
- A) 2 5 8
- B) 4 9 6
- C) 5 11 5
- D) 3 7 7

**Q38.**
```
A ← [1, 2, 3, 4, 5, 6]
i ← 0; j ← 5
WHILE i < j
    temp ← A[i]
    A[i] ← A[j]
    A[j] ← temp
    i ← i + 1
    j ← j - 1
END WHILE
PRINT A[1], A[4]
```
- A) 2 5
- B) 5 2
- C) 6 1
- D) 1 6

**Q39.**
```
FUNCTION F(n)
    IF n = 0 RETURN 0
    IF n = 1 RETURN 1
    RETURN 2 * F(n-1) + F(n-2)
END FUNCTION
PRINT F(4)
```
- A) 5
- B) 24
- C) 12
- D) 8

**Q40.** Selection sort on `A ← [64, 25, 12, 22, 11]`, counting only executed swaps. How many swaps?
- A) 3
- B) 5
- C) 4
- D) 2

**Q41.**
```
n ← 100; c ← 0
WHILE n > 1
    n ← n DIV 3
    c ← c + 1
END WHILE
PRINT c, n
```
- A) 5 0
- B) 3 3
- C) 4 3
- D) 4 1

**Q42.**
```
FUNCTION firstUpper(s)
    FOR i ← 0 TO LENGTH(s) - 1
        IF s[i] is an uppercase letter
            RETURN i
        END IF
    END FOR
    RETURN -1
END FUNCTION
PRINT firstUpper("acCenture")
```
- A) 0
- B) 2
- C) 3
- D) -1

**Q43.** 2×2 matrix multiplication:
```
M ← [[1,2],[3,4]]
N ← [[5,6],[7,8]]
FOR i ← 0 TO 1
    FOR j ← 0 TO 1
        C[i][j] ← M[i][0] * N[0][j] + M[i][1] * N[1][j]
    END FOR
END FOR
PRINT C[0][0], C[1][1]
```
- A) 19 23
- B) 17 50
- C) 19 50
- D) 23 50

**Q44.**
```
i ← 0; s ← 0
WHILE i < 10
    i ← i + 1
    IF i MOD 4 = 0
        CONTINUE
    END IF
    s ← s + i
END WHILE
PRINT s
```
- A) 43
- B) 55
- C) 47
- D) 31

**Q45.**
```
s ← "abxcba"
n ← LENGTH(s)
ok ← TRUE
FOR i ← 0 TO (n DIV 2) - 1
    IF s[i] <> s[n - 1 - i]
        ok ← FALSE
        BREAK
    END IF
END FOR
PRINT ok
```
- A) TRUE (loop never runs)
- B) TRUE (all compared pairs match)
- C) FALSE at i = 0
- D) FALSE (mismatch detected at i = 2)

**Q46.** Tower of Hanoi move count:
```
FUNCTION moves(n)
    IF n = 1 RETURN 1
    RETURN 2 * moves(n-1) + 1
END FUNCTION
PRINT moves(5)
```
- A) 15
- B) 31
- C) 16
- D) 63

---

## Section E — Applied: SQL & Code Output (4)

Salaries table for Q47: `Emp(id, salary)` → (1, 70000), (2, 70000), (3, 60000), (4, 50000), (5, 45000)

**Q47.** What does this return?
```sql
SELECT MAX(salary) FROM Emp
WHERE salary < (SELECT MAX(salary) FROM Emp);
```
- A) 70000
- B) NULL
- C) 60000
- D) 50000

**Q48.** Which statement about `DELETE`, `TRUNCATE` and `DROP` is TRUE?
- A) `TRUNCATE TABLE` removes all rows, is minimally logged, and **cannot** take a `WHERE` clause
- B) `DELETE` without `WHERE` is always faster than `TRUNCATE`
- C) `DROP TABLE` deletes rows but keeps the table structure
- D) `TRUNCATE` is DML and can be rolled back in every DBMS

**Q49.** Java:
```java
int[] arr = {1, 2, 3};
for (int i = 0; i < arr.length; i++) {
    arr[i] = arr[arr.length - 1 - i];
}
System.out.print(arr[0] + "" + arr[1] + "" + arr[2]);
```
- A) `123`
- B) `321`
- C) `111`
- D) `323`

**Q50.** HTML/JS — what is rendered on the page?
```html
<p id="demo">Hello</p>
<script>
  document.getElementById('demo').innerHTML = '<b>Hi</b>';
</script>
```
- A) The literal text `<b>Hi</b>`
- B) The word **Hi** in bold
- C) Nothing — you must use `textContent`
- D) `Hello` unchanged, because the script runs before the element exists

---

---

# ⛔ STOP — Answer Key for Set 3

## Quick grid

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | C | B | D | A | C | B | D | A | B | C |

| Q | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | D | A | C | D | B | A | D | C | B | A |

| Q | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | D | B | A | C | D | B | D | B | C | D |

| Q | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | B | A | C | D | B | A | D | B | C | A |

| Q | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | D | B | C | A | D | B | C | A | D | B |

## Explanations

**Q1 — C.** `(A1:A5>10)` → {0,1,0,1,0}; multiplied by B → {0,2,0,4,0} → sum **6**. Note `10 > 10` is FALSE — strictly greater.

**Q2 — B.** 0.75 formatted as `"0.0%"` → **75.0%** (the format string controls the display, not the stored value).

**Q3 — D.** TRIM removes leading/trailing spaces **and collapses internal runs to a single space** → "Hello World" → **11**.

**Q4 — A.** 50 is **not** > 50, so the FALSE branch runs: 200 × 0.05 = **10**.

**Q5 — C.** Section breaks let one document have different headers, page numbering (e.g. roman then arabic) and orientation/ margins per section.

**Q6 — B.** Slide Sorter shows thumbnails for reordering, transitions and timings. Normal/Outline view is for editing content.

**Q7 — D.** Bcc recipients are hidden from all other recipients. Cc is visible to everyone.

**Q8 — A.** A scatter (XY) plot shows the relationship between two numeric variables; column/bar compares categories, pie shows parts of a whole.

**Q9 — B.** Need 2^h − 2 ≥ 100 → h = 7 → 32 − 7 = **/25** (126 usable hosts). /26 gives only 62.

**Q10 — C.** 4 subnets = 2 extra bits → /26 (block 64) → 10.0.0.0/26, **10.0.0.64/26**, .128/26, .192/26.

**Q11 — D.** /28 = block 16 → 192.168.1.0–.15; `.0` is the network address, `.15` the broadcast → usable `.1`–`.14`.

**Q12 — A.** `::1/128` is loopback. `FE80::/10` link-local, `FF02::1` all-nodes multicast, `2001:db8::/32` documentation.

**Q13 — C.** Link-local = **FE80::/10** (auto-configured, never routed).

**Q14 — D.** NDP (ICMPv6) handles address resolution, router discovery and duplicate-address detection; ARP does not exist in IPv6.

**Q15 — B.** **SFTP** = SSH File Transfer Protocol (port 22). FTPS = FTP over TLS (990/989); TFTP is trivial/unauthenticated UDP.

**Q16 — A.** UDP is **connectionless** — that is the false statement. All the others are true.

**Q17 — D.** A firewall filters on L3/L4 (IP, protocol, port) — and an NGFW/application firewall also inspects L7. A L2 switch only sees MAC addresses.

**Q18 — C.** Auto-scaling (horizontal elasticity) adds/removes instances by policy. Load balancing only distributes existing traffic.

**Q19 — B.** MFA defeats replay of a stolen password. Complexity rules and timeouts do not stop a valid leaked credential being replayed.

**Q20 — A.** Type 1 = bare metal (ESXi, Hyper-V, KVM) directly on hardware. Type 2 = hosted (VirtualBox, VMware Workstation) on top of an OS.

**Q21 — D.** A dynamic array's `append`/`push` is O(1) amortised; the occasional resize costs O(n).

**Q22 — B.** Insertion sort is O(n) on nearly sorted data (adaptive) — it only shifts each element a short distance. Quick sort with a bad pivot degrades to O(n²).

**Q23 — A.** Push opens, pop closes, and a mismatch/leftover stack means unbalanced.

**Q24 — C.** 31 = 2⁵ − 1 → a perfect tree with levels 0–4; leaves live on level 4 → 2⁴ = **16**. (General rule: leaves = ⌈n/2⌉ for a complete tree.)

**Q25 — D.** BCNF is stricter: it forbids *every* non-trivial dependency whose determinant is not a superkey, so BCNF ⊂ 3NF.

**Q26 — B.** A⁺ = {A,B,C,D} (A→B→C→D) → **{A}** is the (minimal) candidate key.

**Q27 — D.** A: 2 orders / 400; B: 2 orders / 450; C: 1 / 50 (fails HAVING). Ties on `c` → `s DESC` → **B (450)** first, then A.

**Q28 — B.** Isolation = concurrent transactions appear to run serially (serialisable). Atomicity = all-or-nothing; Durability = survives crashes; Consistency = valid states.

**Q29 — C.** The base constructor runs first and calls `show()`, which dispatches **virtually** to `B.show()` → prints **B**. (This is why calling overridable methods from a constructor is dangerous: B's fields are not initialised yet.)

**Q30 — D.** `<nav>` is the semantic element for primary navigation. `<menu>` is for toolbars/context menus.

**Q31 — B.** `map` → [2,4,6]; `filter(x > 2)` → **[4, 6]**. Neither method mutates the original array.

**Q32 — A.** 2⁸ = 256 < 500 ≤ 512 = 2⁹ → **9 bits**.

**Q33 — C.** Evens 2 + 4 = 6; odds 1 + 3 + 5 = 9 → `6 9`.

**Q34 — D.** 7 + 6 + 5 + 4 = **22** (recursion peels the last digit off each time).

**Q35 — B.** `f(3)` → x = 13, returns 13. `f(5)` → x = 18, returns 18. 13 + 18 = **31**. The global persists between calls.

**Q36 — A.** Consecutive equal pairs: "ss" (2–3), "ss" (5–6), "pp" (8–9) → **3**.

**Q37 — D.** (1,10)→(3,9)→(5,8)→(7,7); at (7,7) the condition fails → `c = 3, i = 7, j = 7`.

**Q38 — B.** Reversed array = [6,5,4,3,2,1]; `A[1] = 5`, `A[4] = 2` → `5 2`.

**Q39 — C.** F(0)=0, F(1)=1, F(2)=2, F(3)=5, F(4)=2×5+2 = **12**.

**Q40 — A.** Minima: 11 (swap 1), 12 (swap 2), 22 (swap 3), then 25 is already in place → **3** swaps. Selection sort is O(n²) comparisons but only O(n) swaps.

**Q41 — D.** 100 → 33 → 11 → 3 → 1 = **4** divisions, ending with `n = 1`.

**Q42 — B.** "acCenture": a(0) c(1) **C(2)** → returns **2** (the first uppercase letter, 0-based).

**Q43 — C.** C[0][0] = 1×5 + 2×7 = 19; C[1][1] = 3×6 + 4×8 = 50 → `19 50`.

**Q44 — A.** Sum 1…10 = 55, minus 4 and 8 → **43**. The `CONTINUE` skips only the addition.

**Q45 — D.** i = 0: a vs a ✓; i = 1: b vs b ✓; i = 2: **x vs c ✗** → FALSE and BREAK. The loop runs to `n DIV 2 − 1` = 2.

**Q46 — B.** moves(n) = 2ⁿ − 1 → 2⁵ − 1 = **31**.

**Q47 — C.** Inner query gives 70000; the outer max of salaries **strictly less** than 70000 = **60000** (the classic "second highest" pattern).

**Q48 — A.** TRUNCATE is DDL, deallocates pages, is minimally logged and takes no WHERE clause. DELETE is DML, logged row-by-row and supports WHERE; DROP removes the table definition itself.

**Q49 — D.** Not a reverse! i = 0 → arr[0] = arr[2] = 3; i = 1 → arr[1] = arr[1] = 2; i = 2 → arr[2] = arr[0] = **3** → `323`.

**Q50 — B.** `innerHTML` parses the string as HTML → **Hi** in bold. `textContent` would display the literal `<b>Hi</b>`. The script sits *after* the element, so the element exists.

---

### Score guide (Set 3)

| Score | Verdict |
|---|---|
| 43–50 | Excellent — safely above Accenture level |
| 34–42 | Good — revise the missed areas |
| 25–33 | Needs work — revisit the notes, retry after 3 days |
| < 25 | Return to chapters 01–06 before Set 4 |
