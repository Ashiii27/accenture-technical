# HARD Mock Set 5 — Accenture Technical (Above-Level)

**Level:** Harder than the 10 uploaded sets. Unique questions — nothing here repeats Sets 1–4.
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

**Q1.** A1:A6 = running, run, jogging, walk, swimming, swim. What does `=COUNTIF(A1:A6, "*ing*")` return?
- A) 6
- B) 2
- C) 3
- D) 0

**Q2.** A1 contains the formula `=IF(B1>10,"",B1)`. What does `=ISBLANK(A1)` return?
- A) TRUE, because the cell looks empty
- B) TRUE, because the result is an empty string
- C) `#N/A`
- D) FALSE — a formula (even one returning `""`) means the cell is **not** blank

**Q3.** A1:A5 = 1, `"abc"`, 3, an empty cell, 5. What does `=COUNT(A1:A5)` return?
- A) 5
- B) 3
- C) 4
- D) 2

**Q4.** You sort a table and the header row ends up in the middle of the sorted data. What did you miss?
- A) You must sort by more than one column
- B) You must convert the range to a Table first
- C) Ticking **"My data has headers"** in the Sort dialog
- D) Selecting the whole sheet before sorting

**Q5.** Which PowerPoint feature records both **timings and narration** so the show can run unattended?
- A) Rehearse Timings
- B) Presenter View
- C) Set Up Slide Show
- D) Record Slide Show

**Q6.** In MS Word, how do you insert a date that **updates automatically** every time the document is printed?
- A) Type the date manually
- B) Insert → Date & Time → tick **"Update automatically"** (inserts a field)
- C) Insert → Header → Page Number
- D) Insert → Quick Parts → Document Property

**Q7.** Which statement about SSDs vs HDDs is correct?
- A) An HDD has no moving parts
- B) An SSD always has a larger capacity than an HDD
- C) An SSD has no moving parts, much faster random access, and a finite number of write cycles
- D) SSDs are magnetic and need defragmentation

**Q8.** In most browsers, which shortcut opens a **private/incognito** window?
- A) Ctrl + Shift + N
- B) Ctrl + N
- C) Ctrl + Shift + P
- D) Alt + N

---

## Section B — Networking, Security & Cloud (12)

**Q9.** Which CIDR block covers **all** private "Class B" addresses (172.16.0.0 – 172.31.255.255)?
- A) 172.16.0.0/16
- B) 172.16.0.0/20
- C) 172.16.0.0/24
- D) 172.16.0.0/12

**Q10.** Which of these is **not** a private (RFC 1918) address?
- A) 10.10.10.10
- B) 192.168.1.1
- C) 172.32.0.1
- D) 172.20.5.5

**Q11.** Which TCP mechanism stops a fast sender from overwhelming a slow receiver?
- A) Three-way handshake
- B) Sliding-window flow control (the receiver advertises its window size)
- C) Slow start only
- D) Checksums

**Q12.** Which IP header field prevents packets from looping forever, and is also what `traceroute` exploits?
- A) Protocol
- B) Fragment offset
- C) DSCP
- D) TTL (Time To Live)

**Q13.** `traceroute` / `tracert` maps a path by relying on which ICMP message?
- A) Time Exceeded (TTL expired in transit)
- B) Echo Reply
- C) Destination Unreachable (port unreachable)
- D) Redirect

**Q14.** Which HTTP version multiplexes many requests over a single connection using **binary frames**?
- A) HTTP/1.0
- B) HTTP/1.1
- C) HTTP/2
- D) HTTP/0.9

**Q15.** What is the main reason to implement VLANs?
- A) To increase the size of the collision domain
- B) To split one Layer-2 network into smaller broadcast domains (performance + security)
- C) To replace routers entirely
- D) To assign public IP addresses to hosts

**Q16.** Which protocol provides **ticket-based mutual authentication** in Windows Active Directory domains?
- A) RADIUS
- B) LDAP only
- C) NTLM
- D) Kerberos

**Q17.** Managing servers through machine-readable definition files stored in version control is called:
- A) Infrastructure as Code (IaC)
- B) Virtualisation
- C) Containerisation
- D) Disaster recovery

**Q18.** Which cloud model bills **per execution** with no servers for you to provision?
- A) IaaS
- B) PaaS
- C) Serverless / FaaS (e.g. AWS Lambda)
- D) Colocation

**Q19.** An attacker registers `bankk-login.com` and emails a link to customers of a real bank. This is:
- A) Whaling
- B) Phishing with a look-alike (typosquatting) domain
- C) Ransomware
- D) Pharming only

**Q20.** Which wireless attack is used to force clients off the network so the attacker can capture the WPA 4-way handshake?
- A) Evil twin
- B) Bluesnarfing
- C) WPS brute force
- D) Deauthentication attack

---

## Section C — CS Core: DSA / DBMS / OOP / HTML-CSS-JS (12)

**Q21.** Which list is in **increasing** order of growth as n → ∞?
- A) `log n`, `n`, `n log n`, `n²`, `2ⁿ`
- B) `n`, `log n`, `n log n`, `n²`, `2ⁿ`
- C) `log n`, `n`, `n²`, `n log n`, `2ⁿ`
- D) `log n`, `n log n`, `n`, `n²`, `2ⁿ`

**Q22.** Shortest path in an **unweighted** graph in O(V + E):
- A) Dijkstra with a binary heap
- B) Bellman-Ford
- C) Floyd-Warshall
- D) BFS

**Q23.** In a **0-indexed array** representation of a binary heap, the children of node `i` are at:
- A) `i/2` and `i/2 + 1`
- B) `2i` and `2i + 1`
- C) `2i + 1` and `2i + 2`
- D) `i − 1` and `i + 1`

**Q24.** Quick sort degrades to O(n²) when:
- A) Every pivot splits the array into 0 and n−1 elements (e.g. already-sorted data with a first/last-element pivot)
- B) The array has duplicate keys
- C) The array is randomly shuffled
- D) The pivot is chosen as the median

**Q25.** Which SQL statement adds a new column to an existing table?
- A) `MODIFY TABLE Emp ADD salary;`
- B) `INSERT INTO Emp COLUMN bonus INT;`
- C) `UPDATE TABLE Emp ADD COLUMN bonus INT;`
- D) `ALTER TABLE Emp ADD COLUMN bonus INT;`

**Q26.** How do you list customers who have **placed no orders**?
- A) `SELECT ... FROM Customers c INNER JOIN Orders o ON c.id = o.cust_id WHERE o.id IS NULL;`
- B) `SELECT ... FROM Customers c LEFT JOIN Orders o ON c.id = o.cust_id WHERE o.cust_id IS NULL;`
- C) `SELECT ... FROM Customers c RIGHT JOIN Orders o ON c.id = o.cust_id WHERE c.id = NULL;`
- D) `SELECT ... FROM Customers WHERE COUNT(orders) = 0;`

**Q27.** Which index type best supports **range queries** on a sorted column?
- A) Bitmap index
- B) Hash index
- C) B-tree index
- D) Full-text index

**Q28.** A funds-transfer transaction debits one account and credits another; if the credit fails, the debit is rolled back. Which ACID property?
- A) Atomicity
- B) Consistency
- C) Isolation
- D) Durability

**Q29.** Which statement about overloading vs overriding is **FALSE**?
- A) Overloading is resolved at compile time from the parameter list
- B) Overriding requires the same method name and parameter list
- C) Overriding enables runtime polymorphism
- D) Overriding is resolved at compile time using the reference type

**Q30.** In CSS flexbox, which property aligns items along the **main axis**?
- A) `align-items`
- B) `justify-content`
- C) `align-content`
- D) `flex-wrap`

**Q31.** What does `typeof NaN` return in JavaScript?
- A) `"number"`
- B) `"NaN"`
- C) `"undefined"`
- D) `"object"`

**Q32.** Decimal 255 in hexadecimal is:
- A) `EF`
- B) `F0`
- C) `FF`
- D) `1FF`

---

## Section D — Pseudocode & Code Tracing (14)

**Q33.**
```
s ← 0
FOR i ← 1 TO 4
    FOR j ← 1 TO 4
        IF i = j
            s ← s + i
        ELSE IF i < j
            s ← s + 1
        END IF
    END FOR
END FOR
PRINT s
```
- A) 10
- B) 12
- C) 13
- D) 16

**Q34.** (`out` is a **global** string)
```
out ← ""
FUNCTION f(n)
    IF n = 0
        RETURN
    END IF
    out ← out + n
    f(n - 1)
    out ← out + n
END FUNCTION
f(3)
PRINT out
```
- A) `123321`
- B) `321123`
- C) `333`
- D) `123123`

**Q35.**
```
A ← [3, 8, 1, 9, 4]
FOR i ← 0 TO 3
    IF A[i] > A[i + 1]
        swap A[i], A[i + 1]
    END IF
END FOR
PRINT A
```
- A) [1, 3, 8, 4, 9]
- B) [3, 1, 8, 9, 4]
- C) [3, 1, 8, 4, 9]
- D) [8, 3, 9, 1, 4]

**Q36.**
```
n ← 28; c ← 0
FOR i ← 1 TO n
    IF n MOD i = 0
        c ← c + 1
    END IF
END FOR
PRINT c
```
- A) 6
- B) 5
- C) 7
- D) 4

**Q37.**
```
p ← 1
FOR i ← 1 TO 5
    IF i MOD 2 = 1
        p ← p * i
    END IF
END FOR
PRINT p
```
- A) 120
- B) 8
- C) 5
- D) 15

**Q38.**
```
FUNCTION half(a)
    a ← a DIV 2
    RETURN a
END FUNCTION
n ← 37
r ← half(n)
PRINT n, r
```
- A) 18 18
- B) 37 18
- C) 37 37
- D) 18 37

**Q39.**
```
M ← [[1, 3], [5, 7]]
pos_i ← -1; pos_j ← -1
FOR i ← 0 TO 1
    FOR j ← 0 TO 1
        IF M[i][j] = 6
            pos_i ← i
            pos_j ← j
            BREAK
        END IF
    END FOR
END FOR
PRINT pos_i, pos_j
```
- A) 0 1
- B) 1 0
- C) -1 -1
- D) 1 1

**Q40.**
```
i ← 1; s ← 0
WHILE i <= 20
    IF i MOD 3 = 0 AND i MOD 5 <> 0
        s ← s + i
    END IF
    i ← i + 1
END WHILE
PRINT s
```
- A) 63
- B) 36
- C) 45
- D) 48

**Q41.**
```
s ← "Programming"
out ← ""
FOR each ch IN s
    IF ch is a vowel (a, e, i, o, u — case-insensitive)
        out ← out + "*"
    ELSE
        out ← out + ch
    END IF
END FOR
PRINT out
```
- A) `Pr*gr*mm*ng`
- B) `Pr*gr*mming`
- C) `Pr*gr*mm*ng*`
- D) `*r*gr*mm*ng`

**Q42.**
```
FUNCTION cnt(n)
    IF n = 0
        RETURN 0
    END IF
    IF n MOD 2 = 0
        RETURN 1 + cnt(n DIV 10)
    RETURN cnt(n DIV 10)
END FUNCTION
PRINT cnt(24680)
```
- A) 4
- B) 5
- C) 6
- D) 0

**Q43.**
```
A ← [2, 4, 6, 8]
s ← 0
FOR i ← 0 TO 3
    IF A[i] MOD 4 = 0
        s ← s + A[i] * 2
    ELSE
        s ← s + A[i]
    END IF
END FOR
PRINT s
```
- A) 20
- B) 44
- C) 32
- D) 28

**Q44.** Mutual recursion:
```
FUNCTION even(n)
    IF n = 0 RETURN TRUE
    RETURN odd(n - 1)
END FUNCTION
FUNCTION odd(n)
    IF n = 0 RETURN FALSE
    RETURN even(n - 1)
END FUNCTION
PRINT even(7)
```
- A) TRUE
- B) Compiler error — mutual recursion is not allowed
- C) TRUE (7 is odd, so `even(7)` returns TRUE)
- D) FALSE

**Q45.**
```
stack ← empty
FOR each x IN [5, 2, 9, 1]
    IF x MOD 2 = 1
        PUSH x ONTO stack
    ELSE IF stack is not empty
        POP stack
    END IF
END FOR
PRINT SIZE(stack), TOP(stack)
```
- A) 2 1
- B) 3 1
- C) 1 9
- D) 2 9

**Q46.**
```
a ← "listen"
b ← "silent"
count ← 0
FOR each ch IN a
    IF b CONTAINS ch
        count ← count + 1
    END IF
END FOR
PRINT count
```
- A) 5
- B) 6
- C) 4
- D) 0

---

## Section E — Applied: SQL & Code Output (4)

**Q47.** Which query returns the **three highest-paid** employees?
- A) `SELECT * FROM Emp ORDER BY salary DESC LIMIT 3, 1;`
- B) `SELECT * FROM Emp WHERE salary = MAX(salary) LIMIT 3;`
- C) `SELECT * FROM Emp ORDER BY salary DESC LIMIT 3;`
- D) `SELECT * FROM Emp ORDER BY salary LIMIT 3;`

**Q48.** `SELECT COUNT(*), SUM(salary) FROM Emp WHERE dept = 'IT';` when **no** employee is in IT. What is returned?
- A) `0` and `NULL`
- B) `0` and `0`
- C) `NULL` and `NULL`
- D) No rows at all

**Q49.** Java:
```java
int count = 0;
for (int i = 0; i < 6; i++) {
    if (i % 2 == 0) continue;
    count += i;
}
System.out.println(count);
```
- A) 6
- B) 15
- C) 12
- D) 9

**Q50.** Which CSS centres a **block-level** element horizontally inside its parent?
- A) `text-align: center;` on the element
- B) `margin: 0 auto;` together with a defined `width`
- C) `align: middle;`
- D) `position: center;`

---

---

# ⛔ STOP — Answer Key for Set 5

## Quick grid

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | C | D | B | C | D | B | C | A | D | C |

| Q | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | B | D | A | C | B | D | A | C | B | D |

| Q | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | A | D | C | A | D | B | C | A | D | B |

| Q | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | A | C | D | B | C | A | D | B | C | D |

| Q | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | A | B | C | D | A | B | C | A | D | B |

## Explanations

**Q1 — C.** `*` matches any run of characters, so `*ing*` hits running, jogging, swimming → **3**. (This is a substring test, not "ends with ing".)

**Q2 — D.** `ISBLANK` is FALSE for any cell containing a formula, even one that returns `""`. Use `=A1=""` or `LEN(A1)=0` to test for an empty-looking result.

**Q3 — B.** COUNT counts only cells containing **numbers** → 1, 3, 5 → **3**. Use COUNTA for non-empty cells (4 here, ignoring the truly blank cell).

**Q4 — C.** "My data has headers" excludes the header row from the sort keys so it stays on top.

**Q5 — D.** Record Slide Show captures narration + timings per slide. Rehearse Timings records timings only.

**Q6 — B.** With "Update automatically" Word inserts a `DATE`/`PRINTDATE` field that refreshes on print — unlike typed text.

**Q7 — C.** SSD = flash, no moving parts, very low random-access latency, finite P/E write cycles. HDDs are magnetic, do benefit from defragmentation, and are cheaper per GB.

**Q8 — A.** Ctrl + Shift + N = new private/incognito window; Ctrl + N = new normal window; Ctrl + Shift + P = new private window in Firefox.

**Q9 — D.** 172.16.0.0 – 172.31.255.255 = **172.16.0.0/12** (RFC 1918). /16 covers only 172.16.x.x.

**Q10 — C.** Private ranges: 10/8, 172.16/12, 192.168/16. 172.32.x is **outside** 172.16–172.31 → public.

**Q11 — B.** The receiver advertises a window size (flow control). Congestion control (slow start, congestion avoidance) is about the *network*, not the receiver.

**Q12 — D.** TTL is decremented at every hop; at 0 the packet is discarded. That is the basis of traceroute.

**Q13 — A.** Traceroute sends packets with increasing TTL and collects ICMP **Time Exceeded** messages from each router.

**Q14 — C.** HTTP/2 adds binary framing, multiplexing, header compression and server push over one connection. HTTP/1.1 serialises requests per connection (head-of-line blocking).

**Q15 — B.** VLANs create separate Layer-2 broadcast domains on the same physical switches — smaller failure/storm domains and segmentation without extra hardware.

**Q16 — D.** Kerberos issues TGT/service tickets and authenticates both the user and the service. NTLM is the older challenge-response protocol; RADIUS is for network access.

**Q17 — A.** IaC (Terraform, ARM, CloudFormation) describes infrastructure in declarative files kept in version control.

**Q18 — C.** Serverless/FaaS — you deploy functions and pay per invocation and duration, with no server to manage.

**Q19 — B.** A look-alike registered domain used to harvest credentials = phishing (typosquatting). Pharming poisons name resolution instead.

**Q20 — D.** A deauth flood disconnects clients; when they reconnect the attacker captures the 4-way handshake for an offline passphrase attack.

**Q21 — A.** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!).

**Q22 — D.** BFS gives shortest paths in unweighted graphs in O(V + E). Dijkstra is for weighted graphs (non-negative).

**Q23 — C.** 0-indexed: left child `2i + 1`, right child `2i + 2`, parent `⌊(i − 1)/2⌋`.

**Q24 — A.** Worst case = maximally unbalanced partitions → O(n²) (e.g. sorted input with first/last pivot). Randomised or median-of-three pivots avoid it in practice.

**Q25 — D.** `ALTER TABLE ... ADD COLUMN` (sometimes just `ADD`) changes a table's structure. INSERT adds rows; UPDATE changes values.

**Q26 — B.** LEFT JOIN keeps all customers; unmatched rows have NULL for the orders columns, so `WHERE o.cust_id IS NULL` isolates them. `= NULL` never matches — always use `IS NULL`.

**Q27 — C.** B-tree indexes keep keys sorted, so they support `=`, `<`, `>` and `BETWEEN`/range scans. Hash indexes support equality only.

**Q28 — A.** Atomicity = all-or-nothing: if any step fails, the whole transaction is rolled back.

**Q29 — D.** That is the false one: **overriding** is resolved at *runtime* by the object's actual type (dynamic dispatch); overloading is resolved at compile time.

**Q30 — B.** `justify-content` positions items along the **main axis**; `align-items` works on the **cross axis**.

**Q31 — A.** `typeof NaN === "number"` — a famous JS quirk. Use `Number.isNaN()` to test for NaN.

**Q32 — C.** 255 = 15×16 + 15 = **0xFF**.

**Q33 — D.** Per row i: i = 1 → 1 + 3 = 4; i = 2 → 0 + 2 + 2 = 4; i = 3 → 0 + 0 + 3 + 1 = 4; i = 4 → 4 → total **16**.

**Q34 — B.** The append happens **before and after** the recursive call: "3" + ("2" + ("1" + "1") + "2") + "3" = **321123**. (It is a palindrome, not 123321!)

**Q35 — C.** Only adjacent swaps: 3↔8 no, 8↔1 yes → [3,1,8,9,4], 8↔9 no, 9↔4 yes → **[3, 1, 8, 4, 9]** — one pass of bubble sort, which does *not* fully sort the array.

**Q36 — A.** Divisors of 28: 1, 2, 4, 7, 14, 28 → **6**.

**Q37 — D.** Odd i only: 1 × 3 × 5 = **15** (note `p` starts at 1, so i = 1 contributes nothing).

**Q38 — B.** Pass-by-value: `a` is a local copy, so the caller's `n` stays **37**; the return value is 37 DIV 2 = **18**.

**Q39 — C.** 6 is not in the matrix, so the sentinels are never updated → **-1 -1**. (Note the inner BREAK only exits the inner loop — the outer loop still runs.)

**Q40 — D.** Multiples of 3 up to 20: 3, 6, 9, 12, 15, 18; drop 15 (also divisible by 5) → 3 + 6 + 9 + 12 + 18 = **48**.

**Q41 — A.** Vowels o, a, i are replaced → `Pr*gr*mm*ng`. Only lowercase/uppercase vowels count — not `y`.

**Q42 — B.** All five digits (2, 4, 6, 8, 0) are even; the recursion drops the last digit each time and stops at n = 0 → **5**.

**Q43 — C.** 2 → +2; 4 → +8; 6 → +6; 8 → +16 → **32**.

**Q44 — D.** even(7) → odd(6) → even(5) → odd(4) → even(3) → odd(2) → even(1) → odd(0) = **FALSE**. 7 is odd, so `even(7)` is FALSE — the names describe the *remaining* steps.

**Q45 — A.** Push 5 → [5]; 2 is even and the stack is non-empty → pop → []; push 9 → [9]; push 1 → [9, 1] → size **2**, top **1**.

**Q46 — B.** Every letter of "listen" (l, i, s, e, t, n) appears in "silent" → **6**. (An anagram test would need counts, not just membership.)

**Q47 — C.** `ORDER BY salary DESC LIMIT 3`. `LIMIT 3, 1` means "skip 3, take 1" (the 4th row) — a very common trap.

**Q48 — A.** Aggregate queries without GROUP BY always return exactly one row: `COUNT(*) = 0` and `SUM(...) = NULL` (SUM of an empty set is NULL, not 0).

**Q49 — D.** `continue` skips even i; odd i are 1, 3, 5 → 1 + 3 + 5 = **9**.

**Q50 — B.** `margin: 0 auto` plus a fixed width centres a block element. `text-align: center` centres *inline* content (text/images) inside the element.

---

### Score guide (Set 5)

| Score | Verdict |
|---|---|
| 43–50 | Excellent — safely above Accenture level |
| 34–42 | Good — revise the missed areas |
| 25–33 | Needs work — revisit the notes, retry after 3 days |
| < 25 | Return to chapters 01–06 and re-sit Sets 1–2 |
