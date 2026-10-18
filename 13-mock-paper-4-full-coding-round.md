# Mock Paper 4 — Full Coding Round (New 2025/2026 Pattern)

**Format:** 3 parts — (A) DSA, (B) SQL, (C) Frontend (HTML/CSS/JS)
**Time:** 60 minutes total (split ~25/15/20, but manage your own time)
**Languages:** Python / Java / C# for DSA; SQL for B; HTML+CSS+JS for C
**Partial marking applies** — submit whatever you have working; do NOT leave any question totally blank.

---

## Part A — DSA (String/Array) (≈25 min)

### Problem — Character Frequency Sorter

Write a function `frequencySort(s)` that takes a string `s` and returns a string containing the characters of `s` ordered by **frequency** from most frequent to least frequent. If two characters have the same frequency, order them by their first appearance in `s` (stable). Case-sensitive. Ignore spaces (i.e., do NOT include spaces in the output, and do NOT count them).

**Example 1:**
```
Input:  "apple"
Output: "ppale"
Explanation: 'p' appears 2 times, 'a' 1, 'l' 1, 'e' 1.
              'p' first. Then a,l,e in order of first appearance.
```

**Example 2:**
```
Input:  "hello world"
Output: "llloohewrd"
Explanation: After removing space → "helloworld". 'l' appears 3 times; 'o' appears 2;
             h,e,w,r,d each appear once in order of first appearance.
```

**Example 3:**
```
Input:  "aabbcc"
Output: "aabbcc"
Explanation: all have frequency 2; keep original order of first appearance: a,b,c.
```

**Constraints:** `s` can be empty and up to length 1000. Characters may be letters, digits, or symbols.

---

## Part B — SQL Query (≈15 min)

Given three tables:

**students**
| student_id | name     |
|------------|----------|
| 1          | Arjun    |
| 2          | Bhavna   |
| 3          | Chirag   |
| 4          | Divya    |
| 5          | Esha     |

**courses**
| course_id | course_name | instructor |
|-----------|-------------|------------|
| 101       | Math        | Mr. Gupta  |
| 102       | Physics     | Ms. Iyer   |
| 103       | Chemistry   | Dr. Khan   |
| 104       | Biology     | Mrs. Rao   |

**enrollments** (junction table: which student is in which course + marks)
| enrollment_id | student_id | course_id | marks |
|---------------|------------|-----------|-------|
| 1             | 1          | 101       | 85    |
| 2             | 1          | 102       | 78    |
| 3             | 2          | 101       | 92    |
| 4             | 2          | 103       | 67    |
| 5             | 3          | 102       | 55    |
| 6             | 3          | 103       | 72    |
| 7             | 4          | 101       | 88    |
| 8             | 4          | 104       | 91    |
| 9             | 5          | 104       | 74    |

Write **one SQL query** for each of the following:

**(a)** List every student's name alongside the **number of courses** they are enrolled in. Include all students (even those not enrolled in any course, showing 0). Columns: `name`, `course_count`.

**(b)** Show each course_name and the **average marks** of students in that course. Only include courses with an average of 75 or higher. Order by average marks descending.

**(c)** Find the name of the student(s) who scored the **highest marks** in each course. Columns: `course_name`, `name`, `marks`. (It's fine if multiple students tie.)

---

## Part C — Frontend (HTML/CSS/JS) (≈20 min)

Create a single HTML file that builds a **Tip Calculator** with the following behavior:

**UI Requirements:**
- A heading: "Tip Calculator"
- An input box labeled "Bill amount ($)" that accepts a number (id=`billInput`)
- Three buttons for tip percentage: "10%", "15%", "20%" (ids `tip10`, `tip15`, `tip20`)
- A div/area (id=`result`) where results appear. Initially empty / hidden.

**Behavior:**
- When the user types a bill amount and clicks one of the tip buttons:
  - Calculate the tip = bill × tip%
  - Calculate the total = bill + tip
  - Display three lines in `result`:
    - "Bill amount: $X.XX"
    - "Tip (Y%): $X.XX"
    - "Total: $X.XX"
  - Amounts should be shown with exactly 2 decimal places.
- If the bill input is empty, non-numeric, or ≤ 0 when a button is clicked, show the message "Please enter a valid bill amount" in `result`.
- Make the buttons look like buttons (background color, padding, pointer cursor, hover effect).
- Add some basic centering/styling (the page doesn't need to be beautiful — just functional and clean).

You may put CSS and JS inline (in `<style>` and `<script>` tags) or in separate blocks — whatever is fastest. The evaluator will run it in a browser and click the buttons; make sure it works.

---

# Solutions — Mock Paper 4

---

## Part A Solution — Character Frequency Sorter

```python
from collections import Counter

def frequencySort(s):
    # Remove spaces
    s = s.replace(" ", "")
    if not s:
        return ""

    # Count frequencies, BUT track first-appearance order so we can preserve it on ties
    freq = {}
    order = []
    for ch in s:
        if ch not in freq:
            freq[ch] = 0
            order.append(ch)
        freq[ch] += 1

    # Build result: highest frequency first; for ties, first-appearance order
    # We sort unique characters by (-freq, first_appearance_index)
    chars_sorted = sorted(order, key=lambda ch: (-freq[ch], order.index(ch)))

    result = ""
    for ch in chars_sorted:
        result += ch * freq[ch]
    return result


# Tests
assert frequencySort("apple") == "ppale"
assert frequencySort("hello world") == "llloohewrd"
assert frequencySort("aabbcc") == "aabbcc"
assert frequencySort("") == ""
assert frequencySort("   ") == ""
assert frequencySort("abracadabra") == "aaaaabbrrcd"
print("Part A: all tests passed")
```
**How it works:**
1. Strip spaces.
2. Single pass to compute frequencies AND record first-appearance order.
3. Sort unique characters by `(-frequency, first-appearance index)` — negative frequency so higher frequency comes first; first-appearance index breaks ties stably.
4. Build output by repeating each character its frequency number of times.

---

## Part B Solutions — SQL

### (a) Student course counts including zeros
```sql
SELECT
    s.name,
    COUNT(e.course_id) AS course_count
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.name
ORDER BY s.name;
```
Key points:
- LEFT JOIN so students with no enrollments are kept.
- `COUNT(e.course_id)` not `COUNT(*)` because COUNT(*) would count the NULL row produced for non-enrolled students as 1, giving wrong counts for zero-enrollment students.

### (b) Courses with avg marks ≥ 75, ordered
```sql
SELECT
    c.course_name,
    AVG(e.marks) AS avg_marks
FROM courses c
INNER JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
HAVING AVG(e.marks) >= 75
ORDER BY avg_marks DESC;
```
Key points:
- INNER JOIN because we only want courses that have enrollments.
- HAVING (not WHERE) to filter on an aggregate.
- Result:
  - Biology | 82.5
  - Math | 88.33  — wait let's compute: (85+92+88)/3 = 88.33.
  - (Physics avg: (78+55)/2 = 66.5 <75 → excluded.)
  - (Chemistry avg: (67+72)/2 = 69.5 <75 → excluded.)

So output:
```
Math      88.3333
Biology   82.5
```

### (c) Top student per course
```sql
SELECT c.course_name, s.name, e.marks
FROM enrollments e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses  c ON e.course_id = c.course_id
WHERE e.marks = (
    SELECT MAX(e2.marks)
    FROM enrollments e2
    WHERE e2.course_id = e.course_id
)
ORDER BY c.course_name;
```
The correlated subquery returns, for each course, the highest marks; the outer query picks the enrollment row(s) matching that max. If there is a tie, both students are returned.

Result for our data:
```
Math      Bhavna   92
Physics   Arjun    78
Chemistry Chirag   72
Biology   Divya    91
```

---

## Part C Solution — Tip Calculator

Save this as `tip.html` and open it in a browser. Everything is in one file for easy submission on platforms that ask you to modify a skeleton.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Tip Calculator</title>
<style>
  body {
    font-family: Arial, sans-serif;
    max-width: 420px;
    margin: 40px auto;
    padding: 20px;
    text-align: center;
    background: #f5f5f5;
  }
  h1 { color: #333; }
  label { display: block; margin-top: 15px; font-weight: bold; }
  input[type="number"] {
    padding: 8px;
    font-size: 16px;
    width: 180px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .tip-buttons { margin-top: 15px; }
  button {
    padding: 10px 18px;
    margin: 5px;
    font-size: 16px;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    background-color: #2196F3;
    color: white;
    transition: background-color 0.2s;
  }
  button:hover { background-color: #0b7dda; }
  #result {
    margin-top: 25px;
    padding: 15px;
    background: white;
    border: 1px solid #ddd;
    border-radius: 6px;
    min-height: 40px;
    text-align: left;
    font-size: 16px;
    white-space: pre-line;
  }
  .error { color: #d32f2f; font-weight: bold; }
</style>
</head>
<body>
  <h1>Tip Calculator</h1>

  <label for="billInput">Bill amount ($)</label>
  <input type="number" id="billInput" placeholder="e.g. 50.00" min="0" step="0.01">

  <div class="tip-buttons">
    <button id="tip10">10%</button>
    <button id="tip15">15%</button>
    <button id="tip20">20%</button>
  </div>

  <div id="result"></div>

<script>
  const billInput = document.getElementById("billInput");
  const result    = document.getElementById("result");

  function calculateTip(percent) {
    const bill = parseFloat(billInput.value);
    if (isNaN(bill) || bill <= 0) {
      result.className = "error";
      result.textContent = "Please enter a valid bill amount";
      return;
    }
    const tip   = bill * (percent / 100);
    const total = bill + tip;
    result.className = "";
    result.textContent =
      "Bill amount: $" + bill.toFixed(2)   + "\n" +
      "Tip (" + percent + "%): $" + tip.toFixed(2)   + "\n" +
      "Total: $"        + total.toFixed(2);
  }

  document.getElementById("tip10").addEventListener("click", () => calculateTip(10));
  document.getElementById("tip15").addEventListener("click", () => calculateTip(15));
  document.getElementById("tip20").addEventListener("click", () => calculateTip(20));
</script>
</body>
</html>
```

**Key points demonstrated that the evaluator will look for:**
1. Correct IDs on the input, buttons, and result div.
2. `parseFloat` to read the numeric input; `isNaN` / `≤ 0` validation.
3. `.toFixed(2)` for exactly two decimal places.
4. Attaching click listeners with `addEventListener("click", ...)`.
5. DOM update via `.textContent` (using `\n` for newlines and `white-space: pre-line` in CSS to render them).
6. Visual styling (button hover, centering, error coloring) — not strictly required but makes a polished impression.

---

## Self-Assessment

| Task | Full marks if... |
|------|------------------|
| Part A | Handles spaces, single-char case, empty string, ties correctly (preserves first-appearance order). |
| Part B (a) | Uses LEFT JOIN and COUNT on a right-side column; zeros appear for students with no courses. |
| Part B (b) | Uses INNER JOIN, GROUP BY, HAVING (not WHERE) for the aggregate filter, ORDER BY DESC. |
| Part B (c) | Uses a subquery/window function to pick the max per course and returns all tied students. |
| Part C | All three buttons trigger the math, invalid input shows the error message, numbers formatted to 2 decimals. |

If you can finish all three parts correctly in **under 50 minutes**, you're in very good shape for Accenture's coding round. If one part stumps you, move to the next — partial credit on the other two is usually enough to clear the cutoff.
