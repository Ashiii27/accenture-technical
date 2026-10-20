# Mock Paper 5 — OOPs, Java & OS Fundamentals (Accenture CS-Core)

**Why this paper exists:** recent drives (Oct-2025 batch reports) show a **dedicated "Pseudocode + OOPs" section (~10 questions)** in the technical MCQ round, plus Java output questions and OS fundamentals (scheduling, memory, threads) in interviews. Mock Papers 1–2 cover MS Office / Networking / Pseudocode / DSA / DBMS — this paper covers the **CS-core gap**: OOPs, Java basics and OS fundamentals.

**Format:** 40 questions — 15 OOPs + 15 Java Basics + 10 OS Fundamentals
**Time limit:** Give yourself **30 minutes**, closed book.
**Marking:** 1 mark per correct answer, **no negative marking** — attempt everything.
**Maps to:** chapters [14 (OOPs)](./14-oop-object-oriented-programming.md), [15 (OS)](./15-os-fundamentals.md), [16 (Java)](./16-java-basics.md).

---

## Section A — OOPs (15 Questions)

**Q1.** Which of the following is NOT one of the four pillars of OOP?
- A) Encapsulation  B) Inheritance  C) Polymorphism  D) Compilation

**Q2.** Which access modifier restricts a member to its own class only?
- A) public  B) protected  C) private  D) default

**Q3.** A method with the **same name as its class** and **no return type** is a:
- A) destructor  B) constructor  C) static method  D) factory

**Q4.** What is the output?
```
CLASS Box
    size ← 1
    METHOD grow()
        size ← size * 2
END CLASS
a ← NEW Box()
b ← NEW Box()
a.grow(); a.grow(); b.grow()
PRINT a.size + b.size
```
- A) 4  B) 5  C) 6  D) 8

**Q5.** `class Dog extends Animal` models which relationship?
- A) HAS-A  B) IS-A  C) USES-A  D) PART-OF-A

**Q6.** Method **overriding** requires:
- A) Different parameters  B) The same signature in parent and child  C) Two methods in one class  D) Static methods

**Q7.** Which methods can NEVER be overridden in Java?
- A) public  B) protected  C) private and static  D) final and abstract

**Q8.** Which statement about abstract classes is TRUE?
- A) They can be instantiated with `new`
- B) They cannot be instantiated, but may contain concrete methods
- C) They cannot have fields
- D) They cannot have constructors

**Q9.** The **diamond problem** arises with:
- A) Single inheritance  B) Multiple inheritance  C) Multilevel inheritance  D) Encapsulation

**Q10.** Composition models which relationship, and when should it be preferred?
- A) IS-A; always  B) HAS-A; when there is no genuine IS-A  C) IS-A; only for interfaces  D) USES-A; never

**Q11.** About classic Java interfaces (pre-Java-8), which is TRUE?
- A) They can be instantiated  B) They hold method bodies  C) A class can implement many of them  D) They have constructors

**Q12.** Encapsulation is best described as:
- A) Hiding how a feature is implemented
- B) Bundling data with methods and restricting direct access to the data
- C) One interface, many behaviours
- D) Reusing a parent's members in a child

**Q13.** `super()` inside a subclass constructor:
- A) Calls the parent class constructor  B) Creates a new parent object  C) Calls the parent's `main`  D) Deletes the parent

**Q14.** Given `Animal a = new Dog(); a.sound();` prints "woof". This is:
- A) Method overloading  B) Compile-time polymorphism  C) Runtime polymorphism (dynamic dispatch)  D) Encapsulation

**Q15.** Which is an example of **compile-time** polymorphism?
- A) Method overriding  B) Method overloading  C) Abstract methods  D) Interface implementation

---

## Section B — Java Basics (15 Questions)

**Q16.** What does `System.out.println(7 / 2);` print?
- A) 3.5  B) 3  C) 3.0  D) Compile error

**Q17.** What does `System.out.println(7.0 / 2);` print?
- A) 3  B) 3.0  C) 3.5  D) Compile error

**Q18.** `String s1 = "abc"; String s2 = new String("abc");` — `s1 == s2` is:
- A) true  B) false  C) compile error  D) runtime exception

**Q19.** The correct way to compare the **contents** of two Strings is:
- A) `==`  B) `=`  C) `.equals()`  D) `.compare()`

**Q20.** After `int[] a = new int[3];` the value of `a[0]` is:
- A) null  B) 1  C) 0  D) undefined

**Q21.** The default value of an instance `boolean` field is:
- A) true  B) false  C) null  D) 0

**Q22.** Which of these is a **checked** exception?
- A) NullPointerException  B) IOException  C) ArrayIndexOutOfBoundsException  D) ArithmeticException

**Q23.** Why does `float f = 3.14;` fail to compile?
- A) `float` is not a valid type
- B) `3.14` is a `double` literal — use `3.14f` or a cast
- C) Floats cannot hold decimals
- D) Missing semicolon

**Q24.** Which keyword prevents a method from being overridden?
- A) static  B) final  C) abstract  D) volatile

**Q25.** What does `System.out.println("10" + 5);` print?
- A) 15  B) "105"  C) "15"  D) Compile error

**Q26.** Which collection does **not** allow duplicate elements?
- A) ArrayList  B) LinkedList  C) HashSet  D) HashMap

**Q27.** For fast random access by index, prefer:
- A) ArrayList  B) LinkedList  C) HashSet  D) Stack

**Q28.** What does `javac App.java` do?
- A) Runs the program  B) Compiles source into bytecode (`App.class`)  C) Packages a JAR  D) Starts the JVM

**Q29.** Java passes method arguments:
- A) By reference  B) By value — including object references (the reference is copied)  C) By pointer  D) By name

**Q30.** What does this print?
```java
char c = 'A';
c = (char) (c + 1);
System.out.println(c);
```
- A) A  B) B  C) 66  D) Compile error

---

## Section C — OS Fundamentals (10 Questions)

**Q31.** Which is a core function of an operating system?
- A) Process management  B) Memory management  C) File management  D) All of the above

**Q32.** Threads within the same process:
- A) Have separate heaps  B) Share the process's memory space  C) Cannot run concurrently  D) Are heavier than processes

**Q33.** Which CPU scheduling algorithm is **preemptive**?
- A) FCFS  B) SJF (classic)  C) Round Robin  D) FCFS with priority

**Q34.** Which algorithm gives the **minimum average waiting time** (non-preemptive)?
- A) FCFS  B) SJF  C) Round Robin  D) Priority

**Q35.** A page fault occurs when:
- A) A program divides by zero  B) A referenced page is not in RAM  C) The disk is full  D) Two processes collide

**Q36.** Requesting **all** resources at once (instead of one-by-one) breaks which deadlock condition?
- A) Mutual exclusion  B) Hold and wait  C) No preemption  D) Circular wait

**Q37.** Virtual memory primarily allows:
- A) Faster CPU execution  B) Programs larger than physical RAM to run  C) Removing the need for disk  D) Unlimited processes

**Q38.** A mutex guarantees:
- A) Only one thread accesses a shared resource at a time  B) All threads run in parallel  C) No deadlocks ever  D) Priority inheritance

**Q39.** The OS kernel executes in:
- A) User mode  B) Kernel mode  C) Guest mode  D) Real mode

**Q40.** FCFS scheduling is known to suffer from:
- A) Starvation  B) The convoy effect  C) Thrashing  D) Fragmentation

---

# Answer Key — Mock Paper 5

| Q# | Ans | Topic | Explanation |
|----|-----|-------|-------------|
| 1 | D | OOP pillars | The four pillars are encapsulation, abstraction, inheritance, polymorphism — compilation is a build step, not a pillar. |
| 2 | C | Access modifiers | private = same class only. Order: private < default < protected < public. |
| 3 | B | Constructor | Same name as class, no return type, auto-called by `new`. |
| 4 | C | Pseudocode OOP trace | Each object has its own `size`: a → 2 → 4, b → 2. 4 + 2 = **6** (common wrong answer: 8 — sharing one counter). |
| 5 | B | Inheritance | `extends` models IS-A; composition models HAS-A. |
| 6 | B | Overriding | Same name + same signature, child redefines the body. Different parameters = overloading, not overriding. |
| 7 | C | Override rules | private members aren't visible to subclasses; static methods belong to the class (they're hidden, not overridden). |
| 8 | B | Abstract classes | Incomplete — can't instantiate; but they may hold fields, constructors and concrete methods. |
| 9 | B | Diamond problem | Multiple inheritance gives D two copies of A's members; Java/C# ban it for classes (use interfaces). |
| 10 | B | Composition | HAS-A (a field referencing another object); preferred unless the relationship is genuinely IS-A. |
| 11 | C | Interfaces | A contract of signatures; Java allows multiple interface implementation (single class inheritance only). |
| 12 | B | Encapsulation | Bundle data + methods, hide the data behind a controlled public surface. (a) is abstraction. |
| 13 | A | super() | Invokes the parent constructor; must be the first statement in the child constructor. |
| 14 | C | Dynamic dispatch | Reference type is Animal but the OBJECT is Dog — the runtime calls Dog's version. |
| 15 | B | Overloading | Same name, different parameters, one class — resolved by the compiler. |
| 16 | B | Integer division | Both operands are int → result truncates to 3. `7 / 2.0` would be 3.5. |
| 17 | C | Floating division | A double operand forces floating-point division → 3.5. |
| 18 | B | String pool | `new` always creates a fresh heap object; the literal lives in the pool → different references. |
| 19 | C | String equality | `.equals()` compares contents; `==` compares references. |
| 20 | C | Array defaults | Numeric arrays initialise to 0; reference arrays to null. |
| 21 | B | Primitive defaults | Instance primitives default to 0 / false; locals must be initialised explicitly. |
| 22 | B | Checked exceptions | IOException must be caught or declared. NPE/AIOOBE/ArithmeticException are unchecked RuntimeExceptions. |
| 23 | B | Literals | Floating literals are double by default; `3.14f` or `(float) 3.14` fixes it. |
| 24 | B | final | final class = no subclasses; final method = no override; final variable = constant. |
| 25 | B | Concatenation | `"10" + 5` → String "105" (left-to-right: String + int concatenates). |
| 26 | C | Set | Sets enforce uniqueness; ArrayList/LinkedList allow duplicates. |
| 27 | A | List performance | ArrayList = array-backed O(1) index access; LinkedList = O(n) traversal but cheap inserts. |
| 28 | B | javac | Compiles `.java` → `.class` bytecode; `java App` runs it (no extension). |
| 29 | B | Pass-by-value | Java is always pass-by-value; for objects the *reference* is copied, so field changes persist but reassignment doesn't. |
| 30 | B | char arithmetic | 'A' (65) + 1 = 66 → cast back to char → 'B'. |
| 31 | D | OS roles | The OS manages processes, memory, files and I/O. |
| 32 | B | Threads | Threads share code/data/heap; each has its own stack and registers — which is why locks are needed. |
| 33 | C | Preemption | RR cuts the CPU after each quantum; FCFS and classic SJF run jobs to completion/blocking. |
| 34 | B | SJF | Shortest Job First is provably optimal for average waiting time. |
| 35 | B | Page faults | A normal event: the page is fetched from swap/disk into RAM by the OS. |
| 36 | B | Deadlock prevention | Asking for everything up front removes "hold and wait". |
| 37 | B | Virtual memory | Extends the effective address space using disk; slower if it thrashes. |
| 38 | A | Mutex | Binary lock with a single owner — the basis of mutual exclusion. |
| 39 | B | CPU modes | Kernel mode = full hardware access; apps run in user mode and trap via system calls. |
| 40 | B | Convoy effect | Short jobs queue behind one long job in FCFS, dragging average waiting time up. |

**Score:** __ / 40

- **34+**: Excellent — CS-core is locked down.
- **26–33**: Solid — re-read the sections you missed in chapters 14–16.
- **18–25**: Needs work — redo the chapter MCQs, then retake this paper.
- **< 18**: Start with chapters 14 (OOPs) and 16 (Java) — the highest-yield topics here.

---

> **Previous:** [14 - OOPs](./14-oop-object-oriented-programming.md) · [15 - OS Fundamentals](./15-os-fundamentals.md) · [16 - Java Basics](./16-java-basics.md) · **Mock Papers:** [1](./08-mock-paper-1.md) [2](./09-mock-paper-2.md) [3-coding](./10-mock-paper-3-coding.md) [4-coding](./13-mock-paper-4-full-coding-round.md) [hard-mocks](./hard-mocks/)
