# Mock Paper 1 — Accenture Style Technical Assessment

**Format:** 40 questions (matching recent Accenture drives — 12 MS Office + 18 Pseudocode/DSA/DBMS + 10 Networking/Security/Cloud)
**Time limit:** Give yourself **40 minutes**, closed book.
**Marking:** 1 mark per correct answer, **no negative marking** (Accenture does not penalize wrong answers — so attempt every question).

---

## Section A — Common Applications & MS Office (12 Questions)

**Q1.** Which keyboard shortcut is used to open the **Find and Replace** dialog in MS Word?
- A) Ctrl + F
- B) Ctrl + H
- C) Ctrl + R
- D) Alt + F

**Q2.** In Excel, `=COUNT(A1:A10)` counts:
- A) All non-empty cells in A1:A10
- B) Only cells containing numbers in A1:A10
- C) Only cells containing text in A1:A10
- D) Empty cells in A1:A10

**Q3.** What is the output of `=MID("ACCENTURE",3,4)` in MS Excel?
- A) "ACCE"
- B) "CENT"
- C) "CEN"
- D) "ENTU"

**Q4.** In MS PowerPoint, visual effects applied when moving from one slide to the next are called:
- A) Animations
- B) Transitions
- C) Macros
- D) Masters

**Q5.** In Excel, an absolute cell reference looks like:
- A) A1
- B) $A$1
- C) A$1
- D) #A#1

**Q6.** Which feature in MS Word lets you create a batch of personalized letters from one template and a recipient list?
- A) Track Changes
- B) Mail Merge
- C) AutoCorrect
- D) Cross-reference

**Q7.** The `.pdf` file format is best described as:
- A) A proprietary Microsoft Word format
- B) An editable spreadsheet
- C) A fixed-layout document that appears the same across devices
- D) A Windows executable

**Q8.** Which chart type in Excel is most appropriate to show the **trend of monthly sales over 12 months**?
- A) Pie chart
- B) Line chart
- C) Scatter plot
- D) Donut chart

**Q9.** In Windows, which shortcut immediately shows the desktop?
- A) Alt + Tab
- B) Win + D
- C) Ctrl + Esc
- D) Alt + F4

**Q10.** In MS Word, to apply a company logo so it appears automatically on every slide of a PowerPoint deck, you should edit the:
- A) Handout Master
- B) Slide Master
- C) Notes Page
- D) Each slide individually

**Q11.** Which of the following is **volatile** memory (loses its contents when power is turned off)?
- A) ROM
- B) HDD
- C) SSD
- D) RAM

**Q12.** In Excel, which function would you use to combine text from two cells into one (e.g., first name in A1, last name in B1 → full name)?
- A) =MERGE(A1,B1)
- B) =COMBINE(A1,B1)
- C) =A1&" "&B1
- D) =JOIN(A1,B1)

---

## Section B — Networking, Security & Cloud (10 Questions)

**Q13.** At which OSI layer does a router operate?
- A) Layer 1 (Physical)
- B) Layer 2 (Data Link)
- C) Layer 3 (Network)
- D) Layer 4 (Transport)

**Q14.** Which port is used by HTTPS by default?
- A) 22
- B) 53
- C) 80
- D) 443

**Q15.** Which of the following is a **private IPv4 address**?
- A) 8.8.8.8
- B) 172.217.14.206
- C) 192.168.1.10
- D) 13.234.50.10

**Q16.** Which protocol is used to resolve an IP address to a MAC address on a local LAN?
- A) DNS
- B) DHCP
- C) ARP
- D) ICMP

**Q17.** Which cloud service model provides virtual machines on demand (like AWS EC2, Azure VMs)?
- A) SaaS
- B) PaaS
- C) IaaS
- D) FaaS

**Q18.** The TCP three-way handshake proceeds in which order?
- A) SYN, ACK, FIN
- B) SYN, SYN-ACK, ACK
- C) SYN-ACK, SYN, ACK
- D) ACK, SYN, SYN-ACK

**Q19.** Which of the following is an **asymmetric** encryption algorithm?
- A) AES
- B) DES
- C) RSA
- D) Blowfish

**Q20.** An attack that floods a target with traffic from thousands of compromised machines (a botnet) is called:
- A) Phishing
- B) DDoS
- C) SQL Injection
- D) XSS

**Q21.** How many usable host addresses are available on a /28 subnet?
- A) 16
- B) 14
- C) 30
- D) 2

**Q22.** Which of the following best describes a **stateful firewall**?
- A) Filters packets based only on individual IP/port headers
- B) Keeps track of active connections and allows replies automatically
- C) Inspects only Layer 1 signals
- D) Is the same as an IDS

---

## Section C — Pseudocode, DSA, DBMS (18 Questions)

**Q23.** What is the output?
```
x = 10
IF x < 5 THEN
    PRINT "A"
ELSE IF x < 15 THEN
    PRINT "B"
ELSE IF x < 20 THEN
    PRINT "C"
ELSE
    PRINT "D"
ENDIF
```
- A) A
- B) B
- C) C
- D) D

**Q24.** What is the output?
```
s = 0
FOR i = 1 TO 5
    s = s + i * 2
ENDFOR
PRINT s
```
- A) 15
- B) 30
- C) 20
- D) 25

**Q25.** What is the output?
```
n = 10
count = 0
WHILE n > 0
    n = n - 3
    count = count + 1
ENDWHILE
PRINT count
```
- A) 3
- B) 4
- C) 5
- D) -2

**Q26.** How many times does "X" get printed?
```
FOR i = 1 TO 3
    FOR j = 1 TO i
        PRINT "X"
    ENDFOR
ENDFOR
```
- A) 3
- B) 6
- C) 9
- D) 12

**Q27.**
```
FUNCTION weird(a, b)
    RETURN a * 2 + b
ENDFUNCTION

x = weird(3, 4)
PRINT x
```
What is printed?
- A) 7
- B) 10
- C) 14
- D) 24

**Q28.** What does the recursive function return for f(4)?
```
FUNCTION f(n)
    IF n <= 1 THEN RETURN 1
    RETURN n * f(n - 1)
ENDFUNCTION
```
- A) 4
- B) 12
- C) 24
- D) 64

**Q29.**
```
arr = [2, 7, 4, 9, 3]
n = 5
s = 0
FOR i = 0 TO n-1
    IF arr[i] % 2 == 0 THEN
        s = s + arr[i]
    ENDIF
ENDFOR
PRINT s
```
- A) 6
- B) 16
- C) 25
- D) 0

**Q30.** What is the output?
```
a = 8
b = 3
t = a
a = b
b = t
PRINT a + b
```
- A) 5
- B) 11
- C) 24
- D) -5

**Q31.** What is `5 & 3` in bitwise AND?
- A) 1
- B) 7
- C) 6
- D) 0

**Q32.**
```
a = 5
b = a++
c = ++a
PRINT b, c
```
- A) 5 7
- B) 6 6
- C) 5 6
- D) 6 7

**Q33.** Which data structure uses LIFO (Last-In, First-Out)?
- A) Queue
- B) Stack
- C) Linked List
- D) Tree

**Q34.** The time complexity of **binary search** on a sorted array is:
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n log n)

**Q35.** Which of the following sorting algorithms has **O(n log n) worst-case** time AND is stable?
- A) Quick sort
- B) Bubble sort
- C) Merge sort
- D) Selection sort

**Q36.** In a Binary Search Tree, an in-order traversal visits nodes in:
- A) Pre-order sequence
- B) Sorted ascending order
- C) Reverse sorted order
- D) Random order

**Q37.** Which normal form requires elimination of **transitive dependencies** (non-key columns depending on other non-key columns)?
- A) 1NF
- B) 2NF
- C) 3NF
- D) BCNF

**Q38.** In SQL, which JOIN returns **all rows from the left table** and matching rows from the right (filling NULLs where there is no match)?
- A) INNER JOIN
- B) LEFT OUTER JOIN
- C) RIGHT OUTER JOIN
- D) CROSS JOIN

**Q39.** Which SQL clause is used to filter groups **after** GROUP BY aggregation?
- A) WHERE
- B) HAVING
- C) ORDER BY
- D) FROM

**Q40.** Which of the following ACID properties guarantees that once a transaction is committed, its changes survive a system crash?
- A) Atomicity
- B) Consistency
- C) Isolation
- D) Durability

---

# Answer Key — Mock Paper 1

| Q# | Ans | Topic | Explanation |
|----|-----|-------|-------------|
| 1 | B | Word shortcuts | Ctrl+F is Find only; Ctrl+H opens Find & Replace. |
| 2 | B | Excel — COUNT | COUNT counts numeric cells only; COUNTA counts non-empty. |
| 3 | B | Excel — MID | MID is 1-indexed; starting at position 3, 4 chars of "ACCENTURE" → positions 3='C',4='E',5='N',6='T' → "CENT". |
| 4 | B | PowerPoint | Transitions = between slides; Animations = on-slide objects. |
| 5 | B | Excel references | $A$1 is fully absolute (both column and row locked). |
| 6 | B | Word — Mail Merge | Mail merge is specifically for personalized batches. |
| 7 | C | File extensions | PDF preserves layout across devices and is not easily edited. |
| 8 | B | Excel charts | Line charts are ideal for showing trends over time. |
| 9 | B | Windows shortcuts | Win+D shows desktop; Alt+Tab switches windows; Alt+F4 closes. |
| 10 | B | PowerPoint | Editing Slide Master propagates to all slides using that master. |
| 11 | D | Hardware | RAM is volatile; ROM/SSD/HDD retain data without power. |
| 12 | C | Excel text | `&` is the concatenation operator; CONCATENATE/CONCAT also work; MERGE/COMBINE/JOIN aren't the right functions. |
| 13 | C | OSI | Routers = Layer 3 (Network); switches L2, hubs L1. |
| 14 | D | Ports | HTTPS = 443; HTTP = 80; SSH = 22; DNS = 53. |
| 15 | C | IP addressing | 192.168.x.x is Class C private; 10.x and 172.16-31.x are also private. 8.8.8.8 is Google public DNS. |
| 16 | C | Protocols | ARP = IP→MAC; DNS = name→IP; DHCP = auto-IP; ICMP = ping. |
| 17 | C | Cloud | EC2/VMs = IaaS (raw infrastructure). PaaS = Azure App Service; SaaS = Gmail. |
| 18 | B | TCP | SYN, SYN-ACK, ACK is the correct order. |
| 19 | C | Cryptography | RSA is asymmetric (public/private key pair); AES/DES/Blowfish are symmetric. |
| 20 | B | Attacks | DDoS = Distributed Denial of Service (botnet of many sources). |
| 21 | B | Subnetting | /28 → 4 host bits → 2⁴ − 2 = 14 usable hosts (subtract network and broadcast). |
| 22 | B | Firewalls | Stateful firewalls track connection state; packet-filtering is stateless. |
| 23 | B | IF/ELSE | x=10: not <5, but <15 → prints B. |
| 24 | B | FOR loop | i=1→2, +4=6, +6=12, +8=20, +10=30. Sum of 2i for i=1..5 = 2*(15) = 30. |
| 25 | B | WHILE loop | n: 10→7→4→1→−2; count=4 iterations before −2 > 0 is false. |
| 26 | B | Nested loops | i=1: 1; i=2: 2; i=3: 3; total = 6. |
| 27 | B | Functions | 3*2 + 4 = 6+4 = 10. Watch operator precedence! |
| 28 | C | Recursion | f(4)=4*f(3)=4*3*f(2)=4*3*2*f(1)=4*3*2*1=24 (factorial). |
| 29 | A | Array | Evens: 2 + 4 = 6. (7,9,3 are odd.) |
| 30 | B | Swap | Swap exchanges a and b to a=3, b=8. a+b = 11. (The sum is unchanged by swapping!) |
| 31 | A | Bitwise | 5=101, 3=011, AND=001=1. |
| 32 | A | Increment | Post-increment `b = a++`: b=5, a becomes 6; pre-increment `c = ++a`: a becomes 7, c=7. |
| 33 | B | Stack | Stack = LIFO; Queue = FIFO. |
| 34 | C | Big-O | Binary search halves the space each step → O(log n). |
| 35 | C | Sorting | Merge sort is O(n log n) worst case AND stable. Quick sort is O(n²) worst and not stable. |
| 36 | B | BST | In-order (left→root→right) yields ascending order for a BST. |
| 37 | C | Normalization | 3NF removes transitive dependencies of non-keys on the PK. |
| 38 | B | SQL JOINs | LEFT JOIN keeps all left rows and fills NULLs for unmatched right rows. |
| 39 | B | SQL | HAVING filters groups; WHERE filters rows before grouping. |
| 40 | D | ACID | Durability ensures committed changes persist through crashes. |

**Score:** __ / 40

- **36+**: Excellent — you're ready for the real thing.
- **28–35**: Solid — review the topics you missed.
- **20–27**: Needs work — re-read the deep-dives and try Mock 2.
- **< 20**: Start over from chapters 1–5, especially pseudocode.
