# Mock Paper 2 — Accenture Style (Harder Variant)

**Format:** 40 questions (12 MS Office & Common Apps + 10 Network/Security/Cloud + 18 Pseudocode/DSA/DBMS)
**Time limit:** 40 minutes, closed book.
No negative marking — attempt every question.

This mock is intentionally harder than Mock 1 and includes trickier pseudocode, subnet math, bitwise ops, and conceptual DBMS questions that match recent Accenture candidate reports.

---

## Section A — MS Office & Common Applications (12)

**Q1.** In MS Excel, what is the result of `=LEFT("PROGRAMMING",3)&RIGHT("PROGRAMMING",3)`?
- A) "PROING"
- B) "GRMMIN"
- C) "PROGRA"
- D) "MING"

**Q2.** In MS Word, which formatting type is applied to an entire paragraph and controls alignment, line spacing, and indentation?
- A) Character formatting
- B) Paragraph formatting
- C) Section formatting
- D) Font formatting

**Q3.** The Excel formula `=IF(A1>=60,"PASS",IF(A1>=40,"RETOTAL","FAIL"))` returns what if A1 = 45?
- A) PASS
- B) RETOTAL
- C) FAIL
- D) #VALUE!

**Q4.** Which Windows shortcut opens Task Manager directly (without going through the security screen)?
- A) Ctrl + Alt + Del
- B) Ctrl + Shift + Esc
- C) Win + T
- D) Alt + F4

**Q5.** Pivot tables in Excel are primarily used to:
- A) Design web pages
- B) Summarize, group, and aggregate large datasets interactively
- C) Create slide animations
- D) Manage email

**Q6.** In MS PowerPoint, Presenter View shows the presenter:
- A) Exactly what the audience sees
- B) A blank screen
- C) Current slide, next slide preview, speaker notes, and a timer
- D) Only the slide master

**Q7.** A **.bat** file on Windows is:
- A) A binary executable compiled from C
- B) A text script containing command-line commands executed by cmd.exe
- C) A backup file automatically created by Word
- D) A Word macro

**Q8.** In Excel, `=SUMIF(A1:A5,">5",B1:B5)` does what?
- A) Sums all A1:A5 values greater than 5
- B) Sums values in B1:B5 where corresponding A1:A5 is greater than 5
- C) Counts cells greater than 5
- D) Sums B1:B5 if A1 is greater than 5

**Q9.** The difference between RAM and ROM is:
- A) RAM is non-volatile; ROM is volatile
- B) RAM is read-only; ROM is write-only
- C) RAM is read/write volatile working memory; ROM is non-volatile firmware storage
- D) RAM is a secondary storage device; ROM is a CPU register

**Q10.** Which of the following is a utility software?
- A) Microsoft Word
- B) Google Chrome
- C) Antivirus
- D) Minecraft

**Q11.** In Excel, conditional formatting is used to:
- A) Delete duplicate rows automatically
- B) Dynamically apply visual formatting based on cell values or rules
- C) Protect a worksheet with a password
- D) Mail merge

**Q12.** What does Ctrl+Z do in most Windows applications?
- A) Redo last action
- B) Undo last action
- C) Zoom
- D) Save

---

## Section B — Networking, Security & Cloud (10)

**Q13.** Which protocol provides reliable, connection-oriented delivery with retransmission and flow control?
- A) UDP
- B) IP
- C) TCP
- D) ICMP

**Q14.** DNS primarily uses which port and protocol for normal hostname-to-IP lookups?
- A) TCP 80
- B) UDP 53
- C) TCP 22
- D) UDP 67

**Q15.** You need to subnet a network so each subnet supports at least 50 usable hosts. Which subnet mask meets this requirement while wasting the fewest addresses?
- A) /24 (255.255.255.0 → 254 hosts)
- B) /25 (255.255.255.128 → 126 hosts)
- C) /26 (255.255.255.192 → 62 hosts)
- D) /27 (255.255.255.224 → 30 hosts)

**Q16.** Which of the following IP addresses belongs to the loopback range?
- A) 192.168.1.1
- B) 10.0.0.1
- C) 127.0.0.1
- D) 172.16.0.1

**Q17.** Which attack intercepts communications between two parties without their knowledge (e.g., via ARP spoofing on an open Wi-Fi)?
- A) Phishing
- B) DDoS
- C) MITM (Man-in-the-Middle)
- D) Brute force

**Q18.** VPN tunneling commonly uses which protocol suite for site-to-site VPNs?
- A) HTTP
- B) FTP
- C) IPsec
- D) SMTP

**Q19.** In which cloud deployment model are resources shared among multiple organizations (e.g., government community) but isolated from the general public?
- A) Public cloud
- B) Private cloud
- C) Community cloud
- D) Personal cloud

**Q20.** PAT (Port Address Translation / NAT overload) is primarily used to:
- A) Encrypt traffic between browser and server
- B) Map many private IPs to one public IP using different source ports
- C) Provide load balancing across servers
- D) Resolve domain names to IPs

**Q21.** Which of the following correctly orders cloud service models from MOST customer-managed to LEAST customer-managed?
- A) SaaS → PaaS → IaaS
- B) IaaS → PaaS → SaaS
- C) PaaS → IaaS → SaaS
- D) IaaS → SaaS → PaaS

**Q22.** A hypervisor that runs directly on top of bare-metal hardware (e.g., VMware ESXi, Microsoft Hyper-V) is a:
- A) Type 2 hypervisor
- B) Type 1 hypervisor
- C) Virtual box
- D) Container engine

---

## Section C — Pseudocode, DSA, DBMS (18)

**Q23.**
```
x = 0
FOR i = 1 TO 4
    FOR j = i TO 4
        x = x + 1
    ENDFOR
ENDFOR
PRINT x
```
- A) 4
- B) 10
- C) 16
- D) 20

**Q24.**
```
n = 7
WHILE n > 1
    IF n % 2 == 0 THEN
        n = n / 2
    ELSE
        n = 3*n + 1
    ENDIF
ENDWHILE
PRINT n
```
- A) 0
- B) 1
- C) 2
- D) infinite loop (no correct answer)

**Q25.** What does this function return when called as `mystery(4)`?
```
FUNCTION mystery(n)
    IF n == 0 THEN RETURN 0
    IF n == 1 THEN RETURN 1
    RETURN mystery(n-1) + mystery(n-2)
ENDFUNCTION
```
- A) 3
- B) 4
- C) 5
- D) 24

**Q26.**
```
s = "HELLO"
t = ""
FOR i = LENGTH(s)-1 DOWNTO 0
    t = t + s[i]
ENDFOR
PRINT t
```
- A) HELLO
- B) OLLEH
- C) HLO
- D) LLO

**Q27.**
```
arr = [10, 20, 30, 40, 50]
k = 2
n = 5
// rotate right by k using reversal method
reverse arr[0..n-1]
reverse arr[0..k-1]
reverse arr[k..n-1]
PRINT arr
```
What is printed? (Assume reverse(start,end) reverses elements inclusive.)
- A) [10,20,30,40,50]
- B) [40,50,10,20,30]
- C) [30,40,50,10,20]
- D) [50,40,30,20,10]

**Q28.**
```
FUNCTION addOne(x)
    x = x + 1
    RETURN x
ENDFUNCTION

a = 5
b = addOne(a)
PRINT a, b
```
- A) 5 5
- B) 5 6
- C) 6 6
- D) 6 5

**Q29.** What is printed?
```
i = 0
WHILE i < 5
    i = i + 1
    IF i == 3 THEN CONTINUE
    PRINT i
ENDWHILE
```
(Assume CONTINUE skips the rest of this iteration and goes back to the loop condition.)
- A) 1 2 3 4 5
- B) 1 2 4 5
- C) 1 2 4
- D) 0 1 2 4

**Q30.** What is the output of `6 << 1` (bitwise left shift)?
- A) 3
- B) 6
- C) 12
- D) 7

**Q31.**
```
x = 10
y = x % 3   // modulus (remainder)
z = x / 3   // integer division
PRINT y, z
```
- A) 1 3
- B) 3 1
- C) 0 3
- D) 1 4

**Q32.** After one full pass of bubble sort on `[7,3,9,2,5]` (the outermost loop's first iteration), the array becomes:
- A) [2,3,5,7,9]
- B) [3,7,2,5,9]
- C) [3,7,9,2,5]
- D) [9,7,5,3,2]

**Q33.** In a singly linked list, inserting a new node at the head takes:
- A) O(1) time
- B) O(n) time
- C) O(log n) time
- D) O(n²) time

**Q34.** A **circular queue** implemented in an array solves which problem that arises with a simple linear-array queue?
- A) The inability to enqueue integers
- B) Wasted space as the front pointer advances (only able to enqueue until the end, even though space exists at the front)
- C) The need for a dequeue operation
- D) Eliminating the need for pointers/indices

**Q35.** A node that has no children in a tree is called a:
- A) Root
- B) Branch
- C) Leaf
- D) Parent

**Q36.** In the ER model, a many-to-many (M:N) relationship is mapped to a relational database as:
- A) A single table with a single-column primary key
- B) A junction/associative table with two foreign keys forming a composite primary key
- C) Two foreign keys added to either of the participating tables
- D) A trigger

**Q37.** Given a table `orders (order_id, customer_id, order_date, amount)`, which query returns the total `amount` per `customer_id` only for customers whose total exceeds 1000?
- A) `SELECT customer_id, SUM(amount) FROM orders WHERE SUM(amount) > 1000 GROUP BY customer_id`
- B) `SELECT customer_id, SUM(amount) FROM orders GROUP BY customer_id HAVING SUM(amount) > 1000`
- C) `SELECT customer_id, SUM(amount) FROM orders GROUP BY customer_id WHERE SUM(amount) > 1000`
- D) `SELECT customer_id, SUM(amount) FROM orders HAVING SUM(amount) > 1000`

**Q38.** A primary key must satisfy:
- A) Unique and may be NULL
- B) Unique and NOT NULL
- C) Can be duplicated as long as it's an integer
- D) Must always be a single column (cannot be composite)

**Q39.** Which of the following is true of a non-clustered index?
- A) It physically orders the rows of the table
- B) A table can have at most one
- C) It is a separate structure that points to rows; it does not change the physical order of data
- D) It cannot be used to speed up queries

**Q40.** Which of the following is a superkey of a table with columns (A,B,C,D) where the only candidate key is {A}?
- A) {B}
- B) {C,D}
- C) {A,B}
- D) {}

---

# Answer Key — Mock Paper 2

| Q# | Ans | Explanation |
|----|-----|-------------|
| 1 | A | LEFT 3 of "PROGRAMMING" = "PRO"; RIGHT 3 = "ING"; concatenated = "PROING". |
| 2 | B | Alignment/spacing/indent = paragraph formatting; bold/font = character. |
| 3 | B | 45 is not >=60, so first IF false; 45 >=40 true → RETOTAL. |
| 4 | B | Ctrl+Shift+Esc opens Task Manager directly; Ctrl+Alt+Del opens security screen. |
| 5 | B | Pivot tables = interactive aggregation summaries. |
| 6 | C | Presenter view shows current/next slides, notes, timer. |
| 7 | B | .bat = Windows batch script, run by cmd.exe. |
| 8 | B | SUMIF(criteria_range, criteria, sum_range): sums sum_range where criteria_range meets criteria. |
| 9 | C | RAM is volatile read/write; ROM is non-volatile and stores firmware. |
| 10 | C | Antivirus is a system utility; Word/Chrome/Minecraft are applications. |
| 11 | B | Conditional formatting visually highlights based on rules. |
| 12 | B | Ctrl+Z = Undo; Ctrl+Y = Redo. |
| 13 | C | TCP is connection-oriented, reliable, with retransmission. UDP is connectionless. |
| 14 | B | DNS lookups = UDP port 53; zone transfers use TCP 53. |
| 15 | C | Need ≥50 hosts → host bits must satisfy 2^h − 2 ≥ 50 → h≥6 (since 2^5−2=30 too small, 2^6−2=62 works). /26 = 32−6 = 26 bits prefix. /26 is right answer. |
| 16 | C | 127.0.0.0/8 is loopback; 127.0.0.1 is the standard localhost address. |
| 17 | C | MITM (Man-in-the-Middle) intercepts/relays traffic secretly. |
| 18 | C | IPsec is the standard for site-to-site VPNs (sometimes SSL/TLS VPNs for remote access). |
| 19 | C | Community cloud is shared by several organizations with shared concerns (e.g., government). |
| 20 | B | PAT/NAT overload maps many private IPs to one public IP by tracking source ports. |
| 21 | B | IaaS (you manage most) → PaaS → SaaS (provider manages most). |
| 22 | B | Type 1 = bare-metal hypervisor. Type 2 runs as an app on a host OS (VirtualBox). |
| 23 | B | i=1→4; i=2→3; i=3→2; i=4→1; total = 4+3+2+1 = 10. |
| 24 | B | This is the Collatz sequence starting at 7: 7→22→11→34→17→52→26→13→40→20→10→5→16→8→4→2→1. It ends at 1 (loop exits because n>1 is false). Answer = 1. |
| 25 | A | Fibonacci: fib(0)=0, fib(1)=1, fib(2)=1, fib(3)=2, fib(4)=3. |
| 26 | B | Loop iterates from last index (4) down to 0, appending each char to t → "OLLEH". |
| 27 | B | Rotating right by k using reversal: reverse all → [50,40,30,20,10]; reverse first k=2 → [40,50,30,20,10]; reverse remaining 3 → [40,50,10,20,30]. |
| 28 | B | Integer argument is pass-by-value; a remains 5, addOne returns 6 to b. |
| 29 | B | i increments to 1,2,3,4,5; when i=3 CONTINUE skips the PRINT, so output is 1 2 4 5. |
| 30 | C | Left shift by 1 = multiply by 2: 6 * 2 = 12. |
| 31 | A | 10 / 3 = 3 remainder 1 (integer division gives 3, modulus gives 1). |
| 32 | B | First bubble pass: 7↔3 swap → [3,7,9,2,5]; 7<9 no swap; 9↔2 swap → [3,7,2,9,5]; 9↔5 swap → [3,7,2,5,9]. **Correction:** answer is [3,7,2,5,9]. Wait — that's not one of the options. Re-examining options: only B is [3,7,2,5,9]? Option B says [3,7,2,5,9]. Yes! |
| 33 | A | Head insert in a singly linked list is just pointer reassignment: newNode.next=head; head=newNode. O(1). |
| 34 | B | Circular queue wraps indices around via modulo so freed space at the front can be reused. |
| 35 | C | A leaf has zero children. |
| 36 | B | M:N relationships become a junction/link table (e.g., Enroll(student_id, course_id)). |
| 37 | B | WHERE can't use aggregates, GROUP BY comes before HAVING. Option B is the correct structure. |
| 38 | B | PK must be unique AND non-null; it CAN be composite (multiple columns). |
| 39 | C | Non-clustered index is a separate B-tree structure; clustered physically sorts the data; there can be many non-clustered indexes. |
| 40 | C | A superkey is any set that uniquely determines rows; it must contain a candidate key. {A,B} contains candidate key A, so it is a superkey. {B}, {C,D}, and {} are not. |

**Note on Q32:** After carefully retracing:
```
Initial: [7,3,9,2,5]
j=0: 7>3 swap → [3,7,9,2,5]
j=1: 7<9 no swap
j=2: 9>2 swap → [3,7,2,9,5]
j=3: 9>5 swap → [3,7,2,5,9]
```
Result is [3,7,2,5,9] — option **B** matches.

**Score:** __ / 40

- 36+ : Mock 1 level was too easy for you; you're ahead of the curve.
- 28–35 : Solid. Review any explanations you missed.
- 20–27 : Review Deep Dives chapter (07) for the topics you missed; re-attempt in 2 days.
- Below 20 : Go back to chapters 1–7 and restudy.
