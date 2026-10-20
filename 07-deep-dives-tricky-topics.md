# 7. Deep Dives — Tricky Topics Explained Visually

This chapter walks through the concepts candidates most often get wrong. Use it if you missed questions on the mocks.

---

## 7.1 Subnet Math — Step-by-Step Worked Examples

### How to read CIDR and find the number of hosts
Given a CIDR like `192.168.10.0/26`:
1. Prefix length = 26 → 26 network bits, so **host bits = 32 − 26 = 6**.
2. Total addresses in subnet = 2⁶ = 64.
3. Usable hosts = 64 − 2 = **62** (subtract network address and broadcast address).

### How to find network, broadcast, and host range
Given `192.168.10.75/26`:
1. Block size in the last octet = 2⁶ = 64. So subnets increment by 64 in the 4th octet:
   - Subnet 0: 192.168.10.0 – 192.168.10.63
   - Subnet 1: 192.168.10.64 – 192.168.10.127
   - Subnet 2: 192.168.10.128 – 192.168.10.191
   - Subnet 3: 192.168.10.192 – 192.168.10.255
2. 75 falls in subnet 1 →
   - Network address: **192.168.10.64**
   - First usable host: **192.168.10.65**
   - Last usable host: **192.168.10.126**
   - Broadcast: **192.168.10.127**

### Quick reference table (often tested)
| CIDR | Mask | Hosts/Subnet | Block size |
|------|------|--------------|------------|
| /24 | 255.255.255.0 | 254 | 256 |
| /25 | 255.255.255.128 | 126 | 128 |
| /26 | 255.255.255.192 | 62 | 64 |
| /27 | 255.255.255.224 | 30 | 32 |
| /28 | 255.255.255.240 | 14 | 16 |
| /29 | 255.255.255.248 | 6 | 8 |
| /30 | 255.255.255.252 | 2 | 4 |

---

## 7.2 TCP Three-Way Handshake — Visualization

```
Client                                             Server
  |                                                  |
  | ------ SYN (seq=x) --------------------------->  |   Step 1: Client wants connection
  |                                                  |
  | <--- SYN (seq=y), ACK (ack=x+1) ---------------  |   Step 2: Server acknowledges, sends its own SYN
  |                                                  |
  | ------ ACK (ack=y+1) ------------------------->  |   Step 3: Client confirms
  |                                                  |
  | =========== CONNECTION ESTABLISHED ============= |
  |                                                  |
```

- **Why +1?** SYN and FIN flags *consume* one sequence number even though they carry no data. So the next data byte is x+1.
- The handshake ensures both sides know the other is alive and that initial sequence numbers are synchronized.

**Four-way termination (FIN):**
1. Client → FIN
2. Server → ACK
3. Server → FIN
4. Client → ACK (then enters TIME_WAIT)

---

## 7.3 DNS Resolution Walkthrough

When you type `www.example.com` into a browser:

1. **Browser cache** — check if recently looked up.
2. **OS cache / hosts file** — check local machine.
3. **Resolver (recursive DNS, usually ISP)** — if not cached locally, resolver queries on your behalf:
   4. **Root DNS server** (knows where TLDs are) → returns address of `.com` TLD server.
   5. **TLD server (.com)** → returns address of example.com's **Authoritative** server.
   6. **Authoritative server** → returns the IP for `www.example.com` (e.g., `93.184.216.34`).
7. Resolver caches the answer and sends IP back to your browser.
8. Browser opens TCP connection (SYN/SYN-ACK/ACK) to IP on port 443, performs TLS handshake, sends HTTP GET.

---

## 7.4 DHCP DORA — What Each Packet Actually Carries

| Stage | Who sends | Source IP | Destination IP | Purpose |
|-------|-----------|-----------|----------------|---------|
| Discover | Client | 0.0.0.0 (has no IP yet) | 255.255.255.255 (broadcast) | "Is there a DHCP server out there?" |
| Offer | Server | Server's IP | 255.255.255.255 | "I can give you IP x.y.z.w" |
| Request | Client | 0.0.0.0 | 255.255.255.255 | "I'll take x.y.z.w please" |
| Acknowledge | Server | Server's IP | 255.255.255.255 | "Confirmed. Here's your lease + gateway + DNS." |

After DORA the client configures its NIC with the assigned IP, and subsequent traffic uses unicast.

---

## 7.5 ARP — Step-by-Step

When PC-A (192.168.1.2, MAC-AA) wants to send to PC-B (192.168.1.3, MAC-BB) on the **same subnet**:

1. PC-A checks its **ARP cache** (table). If 192.168.1.3 → MAC-BB is cached, skip to step 4.
2. PC-A sends a **broadcast frame** (destination MAC = FF:FF:FF:FF:FF:FF) saying "Who has 192.168.1.3? Tell 192.168.1.2."
3. Every host on the LAN reads it; PC-B replies **unicast** "192.168.1.3 is at MAC-BB". (Other hosts ignore.)
4. PC-A stores MAC-BB in its ARP cache and sends the IP packet inside an Ethernet frame addressed to MAC-BB.

If the destination is on a **different subnet**, ARP is used not for the final destination but for the **default gateway** (router's LAN MAC). The frame goes to the router's MAC, but the IP packet stays addressed to the final IP (routing).

---

## 7.6 Switch vs Router — The Exact Difference in Behavior

### Switch receiving a frame (Layer 2)
1. Learn the source MAC → ingress port mapping (update MAC table).
2. Look up destination MAC in the MAC table.
3. If known → forward out that port only (unicast).
4. If unknown (or broadcast/multicast) → **flood** out all ports except the one it came from.
5. Never examine IP addresses. Never cross subnet boundaries.

### Router receiving a packet (Layer 3)
1. Decapsulate the frame (strip Layer 2 header/trailer).
2. Look up destination **IP** in the routing table (longest prefix match).
3. Decrement TTL, recompute IP header checksum.
4. Choose exit interface and next-hop.
5. Re-encapsulate in a new Layer 2 frame appropriate for the outgoing interface (new source/dest MACs, possibly different link type).
6. Routers do **not forward broadcasts** by default — that's what defines broadcast domain boundaries.

### Summary
- **Collision domain** = set of devices whose frames can collide. Each switch port is its own collision domain; hub is one big collision domain.
- **Broadcast domain** = set of devices that receive each other's broadcasts. Router separates broadcast domains; switch (without VLANs) is one broadcast domain.

---

## 7.7 SSL/TLS Handshake — Simplified but Complete

```
Client                                                  Server
  |                                                       |
  | ClientHello (cipher suites, random #1) ---------->    |  1
  |                                                       |
  | <----- ServerHello (chosen cipher, random #2)         |  2
  | <----- Certificate (server public key inside)         |  3
  | <----- ServerHelloDone                                |  4
  |                                                       |
  | ClientKeyExchange                                      |
  | (encrypt premaster secret with server's public key)    |
  | ------------------------------------------------->     |  5
  |                                                       |
  | Both sides: derive session key from two randoms + PMS  |
  |                                                       |
  | ChangeCipherSpec (future msgs encrypted) --------->    |  6
  | Finished (verify handshake) ----------->              |  7
  | <------- ChangeCipherSpec                             |  8
  | <------- Finished                                     |  9
  |                                                       |
  | ========== ENCRYPTED APPLICATION DATA =============== |
```
Key points:
- **Asymmetric crypto (RSA/ECDHE)** is used only to exchange/agree on the premaster secret — slow.
- **Symmetric crypto (AES)** is used for all subsequent data — fast.
- The server must present a certificate signed by a trusted CA so the client knows it's talking to the real server (prevents MITM).

---

## 7.8 How VLOOKUP Actually Works (with Traps)

```
=VLOOKUP( lookup_value, table_array, col_index_num, [range_lookup] )
```

| Argument | Meaning |
|----------|---------|
| lookup_value | The value to find; **must be in the FIRST column** of `table_array` |
| table_array | The range containing data |
| col_index_num | Which column to return (1 = first column of the table) |
| range_lookup | `FALSE` = exact match (most common); `TRUE` or omitted = approximate match (first column MUST be sorted ascending) |

**Trap 1:** If you forget `FALSE` and the first column isn't sorted, you'll get wrong answers (or #N/A).
**Trap 2:** If you drag the formula and the table reference is relative (no `$`), the table shifts and you get garbage. Always use `$A$2:$D$100` absolute references for the table.
**Trap 3:** VLOOKUP can only return columns to the RIGHT of the lookup column. To look left, use INDEX/MATCH or XLOOKUP.

### INDEX/MATCH breakdown
```
=INDEX( return_column, MATCH( lookup_value, lookup_column, 0 ) )
```
- `MATCH` returns the **row position** where the value is found.
- `INDEX` returns the value at that position in the return column.
- Works in any direction; more robust when columns are inserted.

### IFERROR wrapping
```
=IFERROR(VLOOKUP(A2, $A$2:$D$100, 3, FALSE), "Not found")
```
Hides `#N/A` errors with a friendly message.

---

## 7.9 Recursion Tracing — A Worked Template

Whenever you see recursion:
1. Write the function signature with base cases.
2. Draw the call tree top-down until you hit base cases.
3. Fill in return values bottom-up.

**Example:** What does `g(4)` return?
```
FUNCTION g(n):
    IF n == 0: RETURN 2
    IF n == 1: RETURN 1
    RETURN g(n-1) + g(n-2)
ENDFUNCTION
```
Expand:
```
g(4) = g(3) + g(2)
     = (g(2) + g(1)) + (g(1) + g(0))
     = ((g(1)+g(0)) + 1) + (1 + 2)
     = ((1 + 2) + 1) + 3
     = (3 + 1) + 3
     = 7
```
Sequence: g(0)=2, g(1)=1, g(2)=3, g(3)=4, g(4)=7.

**Common pseudocode recursion patterns you'll see:**
- Factorial: `n * fact(n-1)` base `fact(0)=1`.
- Fibonacci: `fib(n-1)+fib(n-2)` base `fib(0)=0, fib(1)=1`.
- Sum of digits: `(n%10) + sum_digits(n/10)` base `n==0 → 0`.
- GCD (Euclidean): `gcd(b, a%b)` base `b==0 → a`.
- Power: `power(x, n-1) * x` base `n==0 → 1`.
- Binary search recursive: split based on comparison, return index.

---

## 7.10 Bitwise Operators (newer Accenture pseudocode favorite)

Bitwise ops operate on binary representations. Know this table:

| Operator | Name | Example (binary → result) | Rule |
|----------|------|----------------------------|------|
| `&` | AND | `5 & 3` = `101 & 011` = `001` = 1 | Bit is 1 only where BOTH bits are 1 |
| `\|` | OR | `5 \| 3` = `101 \| 011` = `111` = 7 | Bit is 1 where EITHER bit is 1 |
| `^` | XOR | `5 ^ 3` = `101 ^ 011` = `110` = 6 | Bit is 1 where bits DIFFER |
| `~` | NOT (complement) | `~5` = −6 (in two's complement) | Flips all bits |
| `<<` | Left shift | `5 << 1` = `1010` = 10 | Multiply by 2^k |
| `>>` | Right shift | `5 >> 1` = `10` = 2 | Divide by 2^k (integer division) |

**Key identities / tricks:**
- `x & 1` returns 1 if x is odd, 0 if even.
- `x ^ x = 0`, `x ^ 0 = x`.
- `x << 1 = 2*x`, `x >> 1 = x/2` (integer).
- Swapping without temp: `a = a^b; b = a^b; a = a^b;`
- Power of two check: `x > 0 && (x & (x-1)) == 0`.
- Setting the k-th bit to 1: `x | (1 << k)`.
- Clearing the k-th bit: `x & ~(1 << k)`.

### Increment/Decrement Operators
Pseudocode may use C-style:
- `++i` (pre-increment): increment first, then use the new value.
- `i++` (post-increment): use the current value, then increment.
- Same with `--`.

**Example:**
```
a = 5
b = a++      // b=5, a=6 (post: use old value then increment)
c = ++a      // c=7, a=7 (pre: increment then use new value)
```
This single topic trips up more people than anything else in pseudocode. Trace carefully!

---

## 7.11 Pass by Value vs Reference — Memory Diagram

Imagine:
```
FUNCTION f(x)
    x = x + 1
ENDFUNCTION

a = 5
f(a)
PRINT a        // still 5
```

Memory:
- Variable `a` lives at address 100 with value 5.
- When `f(a)` is called, a NEW variable `x` (parameter) is created at address 200, copied with value 5.
- `x = x+1` changes address 200 to 6. Address 100 (a) is never touched.

**But with arrays/objects (reference):**
```
FUNCTION g(arr)
    arr[0] = 99
ENDFUNCTION

nums = [1,2,3]
g(nums)
PRINT nums[0]   // 99
```
Memory:
- `nums` at 100 holds a pointer (e.g. 500) to the array data.
- Parameter `arr` at 200 is created copying the pointer 500.
- Both point to the SAME array data, so modifying `arr[0]` modifies the underlying data.

**Quick rule of thumb** for Accenture pseudocode:
- Numbers, booleans, characters → pass by value (original unchanged).
- Arrays, lists, objects, strings (in some languages) → effectively pass by reference (changes visible to caller).
- If the pseudocode reassigns the parameter itself (`arr = [1,2,3]` inside the function), that breaks the reference link and doesn't affect the caller.

---

## 7.12 Normalization Worked Example — From Messy Table to BCNF

**Bad table** (one big unnormalized table):
```
STUDENT(student_id, student_name, course_id, course_name, instructor_id, instructor_name, grade)
```
Sample data shows problems:
- `course_name` repeats for every student taking it (redundancy).
- If instructor "Smith" changes her name, we have to update many rows (update anomaly).
- If a new course has no students yet, we can't record it (insert anomaly).
- If the last student drops a course, the course/instructor info disappears (delete anomaly).

**Step 1: 1NF** — atomic columns only. Our columns are already atomic, so already 1NF.

**Step 2: 2NF** — remove partial dependencies (assuming PK is (student_id, course_id)).
- `student_name` depends only on `student_id` (partial).
- `course_name, instructor_id, instructor_name` depend only on `course_id` (partial).
- `grade` depends on the whole PK.

Decompose:
- STUDENT(student_id, student_name)
- COURSE(course_id, course_name, instructor_id, instructor_name)
- ENROLL(student_id, course_id, grade)  PK = (student_id, course_id)

**Step 3: 3NF** — remove transitive dependencies.
- In COURSE: `instructor_name` depends on `instructor_id`, which is not a key.

Decompose further:
- STUDENT(student_id, student_name)
- INSTRUCTOR(instructor_id, instructor_name)
- COURSE(course_id, course_name, instructor_id)  FK → INSTRUCTOR
- ENROLL(student_id, course_id, grade)  FKs → STUDENT, COURSE

**Step 4: BCNF** — every determinant is a superkey.
- All non-trivial FDs are now:
  - student_id → student_name (student_id is key of STUDENT ✓)
  - instructor_id → instructor_name (instructor_id is key of INSTRUCTOR ✓)
  - course_id → course_name, instructor_id (course_id is key of COURSE ✓)
  - (student_id, course_id) → grade (the composite is key of ENROLL ✓)
- BCNF satisfied.

---

## 7.13 SQL JOINs — Venn-Diagram Style Explanation

Imagine:
- `employees` table: (emp_id, name, dept_id) — 5 rows
- `departments` table: (dept_id, dept_name) — 3 rows (say dept 10,20,30)
- Suppose emp "Tom" has dept_id = NULL (no department assigned).
- Dept 30 "Security" currently has no employees.

| JOIN type | Rows returned | Which employees? | Which departments? |
|-----------|---------------|------------------|--------------------|
| INNER JOIN employees e ON e.dept_id = d.dept_id | Rows where BOTH exist | Only employees WITH a department | Only departments that HAVE an employee |
| LEFT JOIN | All rows from LEFT (employees) + matching right | All employees (including Tom, dept columns NULL for him) | Only matching depts (dept 30 missing) |
| RIGHT JOIN | All rows from RIGHT (departments) + matching left | Only employees matching a dept (Tom missing) | All departments (incl. empty Security; emp columns NULL) |
| FULL OUTER JOIN | All rows from both sides | All employees (incl. Tom) | All departments (incl. empty Security); NULLs fill the gaps |

**Classic question:** "Which SQL clause lists employees who have NO department?"
```sql
SELECT e.name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;
```
Because LEFT JOIN keeps Tom with NULLs for all department columns. The WHERE picks exactly those.

---

## 7.14 Kadane's Algorithm — Why It Works

Problem: find the maximum sum of any contiguous subarray.

Naive O(n²): check every start and end, compute sum. Too slow for large n.

**Kadane's insight (O(n)):** As you walk through the array, keep track of the best sum ending at the current position. For each element, you have two choices:
- Extend the previous best subarray by adding this element, or
- Start a new subarray at this element.

```
max_ending_here = max( a[i], max_ending_here + a[i] )
max_so_far = max( max_so_far, max_ending_here )
```

Walkthrough on `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:
```
i=0 (num=-2): meh=max(-2,-2)=-2            msf=-2
i=1 (num=1):  meh=max(1,-2+1=−1)=1         msf=1
i=2 (num=-3): meh=max(-3,1−3=−2)=−2        msf=1
i=3 (num=4):  meh=max(4,-2+4=2)=4          msf=4
i=4 (num=-1): meh=max(-1,4-1=3)=3          msf=4
i=5 (num=2):  meh=max(2,3+2=5)=5           msf=5
i=6 (num=1):  meh=max(1,5+1=6)=6           msf=6   ← subarray [4,-1,2,1]
i=7 (num=-5): meh=max(-5,6-5=1)=1          msf=6
i=8 (num=4):  meh=max(4,1+4=5)=5           msf=6
```
Answer = **6** (from indices 3 to 6: 4 + −1 + 2 + 1 = 6).

**Edge case:** if all numbers are negative, Kadane's picks the single least-negative number (the best you can do).

---

## 7.15 Slow & Fast Pointer (Tortoise & Hare) — Middle of Linked List

To find the middle in one pass without counting first:
- `slow` starts at head, moves **1 step** at a time.
- `fast` starts at head, moves **2 steps** at a time.
- When fast reaches the end (fast == null or fast.next == null), slow is at the middle.

Walkthrough on `1 → 2 → 3 → 4 → 5 → None`:
```
slow=1, fast=1 → step: slow=2, fast=3
             → step: slow=3, fast=5
             → fast.next is None, stop. slow=3 (middle).
```
For even-length lists (e.g., 1→2→3→4→None), this gives the **second middle** (3). Adjust by starting fast at head.next for first middle.

**Cycle detection (Floyd's algorithm):** Same pattern, but if fast ever equals slow, there's a cycle. If fast hits null, no cycle.

---

## 7.16 Binary Search — Why the Loop Condition Matters

```
low = 0
high = n - 1
WHILE low <= high                 # <= (not <) because we need to check the final one-element range
    mid = (low + high) // 2
    IF arr[mid] == target: RETURN mid
    ELSE IF arr[mid] < target: low = mid + 1    # +1 because mid already checked
    ELSE: high = mid - 1                         # -1 because mid already checked
RETURN -1
```

- Use `low <= high` when you're searching an **inclusive** range [low, high] (the standard binary search).
- If you use `low < high`, the loop exits with `low == high`, which you must still check once.
- The `+1` / `-1` adjustments are critical; forgetting them can cause infinite loops or missed elements.
- To avoid integer overflow in languages like Java: `mid = low + (high - low) / 2` instead of `(low + high) / 2`.

---

## 7.17 OOP Concepts Quick Reference (sometimes tested in pseudocode section)

> **Full chapter:** all OOPs notes, 30 MCQs with explanations and coding practice live in [chapter 14 — OOPs](./14-oop-object-oriented-programming.md). This section is just the summary.

- **Class**: blueprint defining attributes (fields) and methods (functions).
- **Object**: instance of a class.
- **Encapsulation**: bundling data + methods; hiding internal state (private/protected/public access).
- **Abstraction**: hiding complexity, exposing only essential features (abstract classes, interfaces).
- **Inheritance**: a class (child/sub) derives from another (parent/super), reusing and extending behavior.
- **Polymorphism**: same interface, different behavior.
  - *Compile-time* (overloading): multiple methods with same name but different parameters.
  - *Runtime* (overriding): subclass redefines a method from the parent; the right version is chosen at runtime based on object type.
- **Constructor**: special method called when an object is created; initializes state; same name as class; no return type.
- **Access modifiers (Java/C#)**: private (same class) < default (same package) < protected (same package + subclasses) < public (everywhere).
- **Abstract class**: cannot be instantiated; can have abstract methods (no body) which subclasses must implement.
- **Interface**: a contract of method signatures; a class can implement multiple interfaces.


---

## 7.18 Exam Traps & Common Accenture Trick Questions

Accenture question writers use specific traps year after year.

### "All of the above" / "None of the above"
- If **two** options are definitely true, "All of the above" is usually correct.
- If you can disprove **even one** option, eliminate "All of the above."
- "None of the above" is a distractor more often than it's correct — pick it only if you can rule out every other option.

### Networking Traps
- **"A Layer 3 switch"** is a switch that also routes (Layer 3). Don't automatically assume "switch = Layer 2" — read the wording.
- A generic **firewall** question usually expects Layer 3/4, but "next-gen firewall" is Layer 7.
- **Ping uses ICMP** (not TCP/UDP).
- **DNS primarily uses UDP/53** for queries but **TCP/53** for zone transfers and responses larger than 512 bytes.
- `127.0.0.1` is loopback, not private (private ranges are 10/8, 172.16/12, 192.168/16).
- **Default gateway** is the router used when the destination is on a different subnet. ARP is used to find the gateway's MAC, not the destination's MAC.
- VLANs separate broadcast domains on a single switch. Trunk ports (802.1Q) carry multiple VLANs.

### IP/Subnet Traps
- "Usable hosts" always means 2^h − 2 (subtract network and broadcast). The question won't always say "usable" — but it almost always means it.
- /0 = default route; /32 = single host; /31 is used for point-to-point links (special case, no broadcast).
- IPv6 does NOT use broadcast; it uses multicast (including "all nodes" multicast as a replacement).
- NAT (basic) maps one-to-one; PAT (overload) maps many-to-one using ports. Home routers almost always use PAT.

### Security Traps
- **HTTPS does NOT mean a website is safe** — it only means the connection is encrypted. A phishing site can perfectly well have a valid certificate.
- **IDS** detects and alerts (passive); **IPS** detects and blocks (in-line).
- **HTTPS = HTTP over TLS**; TLS is the successor to SSL (SSL 2.0/3.0 are deprecated and insecure).
- **MFA requires factors from multiple categories** (knowledge + possession + inherence). Two passwords is NOT MFA.
- DoS = one source; DDoS = many sources (botnet). Phishing = social engineering, not a technical attack on infrastructure.

### Excel Traps
- **VLOOKUP without `FALSE`** does approximate match and requires a sorted first column — this is the #1 reason VLOOKUP appears to "give wrong answers."
- **COUNT counts numbers only.** To count non-empty cells use COUNTA. To count non-empty cells meeting a condition use COUNTIF.
- When copying a formula, references without `$` shift. If you're looking up against a fixed table, lock it with `$A$1:$Z$100`-style references.
- IFERROR is your friend — wrap lookups with `=IFERROR(..., "Not found")` to avoid ugly #N/A.
- `TODAY()` updates every time the workbook opens (volatile). If you want a static date, type it.

### Pseudocode Traps
- **0-based vs 1-based arrays:** check how the loop is written. If it's `FOR i = 0 TO n-1` it's 0-based; `FOR i = 1 TO n` is 1-based.
- **Post- vs pre-increment:** `b = a++` assigns the old value then increments; `b = ++a` increments first.
- **Off-by-one in loops:** `TO n` usually includes n; `WHILE i < n` excludes n.
- **Loop-variable reuse:** if a loop uses `i` and the code modifies `i` inside the loop body, it changes the iteration count (common bug-in-pseudocode question).
- **Pass-by-value vs reference:** reassigning a parameter name inside a function (`arr = [1,2,3]`) does NOT affect the caller; mutating the object (arr[0]=99) does.
- **Division:** some pseudocode uses `/` as integer division when both operands are integers (like C/Java); others give floating point. Read context.
- **Return exits the function immediately.** Any code after RETURN in the same block is dead code and does not run.
- **Nested loops:** inner loop runs to completion for EACH iteration of the outer loop. Multiply bounds for total iterations only when bounds are fixed.

### DSA Traps
- Binary search requires a **SORTED** array.
- Bubble sort's first pass moves the LARGEST element to the end; Selection sort's first pass moves the SMALLEST to the front. Don't mix them up.
- Stack = LIFO; Queue = FIFO. "Which data structure for BFS?" = Queue. "Which for DFS / function calls / balanced brackets?" = Stack.
- In a BST, **in-order = sorted ascending**. Pre-order is root-left-right; post-order is left-right-root.
- Big O: worst-case Quick Sort is O(n²); worst-case Merge Sort is O(n log n).
- Linked-list head insertion is O(1); tail insertion (without a tail pointer) is O(n).

### DBMS Traps
- **WHERE filters rows BEFORE grouping; HAVING filters groups AFTER grouping.** You cannot use aggregates (SUM, COUNT) in WHERE.
- **INNER JOIN** drops rows without matches on both sides. Use LEFT JOIN to keep all left-side rows.
- **Primary key ≠ single column.** Primary keys can be composite (multi-column).
- **Foreign keys can be NULL** (indicating an optional relationship).
- A table can have only ONE clustered index (because data can only be physically ordered one way), but many non-clustered indexes.
- **DELETE** removes rows (can be rolled back in a transaction, logs each row). **TRUNCATE** deallocates pages (faster, fewer logs, usually cannot be rolled back). **DROP** removes the entire table.
- A **view** does NOT store data (except materialized views); it's a stored query.
- **Triggers** fire automatically on INSERT/UPDATE/DELETE — they do not take explicit parameters but reference OLD and NEW row values.

### Cloud Traps
- IaaS = you rent infrastructure (VMs); PaaS = you deploy applications onto a managed platform; SaaS = you use a finished application.
- Type 1 hypervisor = bare-metal (ESXi, Hyper-V, KVM); Type 2 = hosted on an OS (VirtualBox, VMware Workstation).
- Containers share the host kernel (lightweight); VMs each have their own guest OS (heavier isolation).
- Elasticity = automatically scaling up/down with load; Scalability = the ability to grow. "Pay-as-you-go" is a pricing model.

### General Strategy
- **Read the question twice.** Many wrong answers come from selecting what sounded right for a different question.
- **Time is shared across sections.** Pseudocode takes the longest per question; prioritize it and do quick/known MS Office & cloud questions first to bank time.
- **No negative marking** — answer every question even if you must guess.
- For pseudocode output questions, **actually trace on scratch paper** with a variable table. Trying to do it in your head is the #1 cause of wrong pseudocode answers.
