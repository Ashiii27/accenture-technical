# Mock Paper 3 — Coding Assessment (Accenture Style)

**Format:** 3 coding problems (some drives also have 1 SQL question; 45–60 minutes total)
**Instructions:** Attempt in Python, Java, C++, or C#. Do not look at solutions until you've written and tested your code. Time yourself.

**Scoring:** In the real test, partial credit is given for passing some test cases — so submit whatever you have even if incomplete. Aim for **full correctness on at least 2 of 3 problems**.

---

## Problem 1 — String (Easy)

### Title: Count Vowels and Consonants

Write a function `count_vowels_consonants(s)` that takes a string `s` and returns a tuple `(vowels, consonants)` where:
- `vowels` is the number of vowels (a, e, i, o, u — case-insensitive)
- `consonants` is the number of alphabetic characters that are not vowels
- Ignore digits, spaces, and special characters (don't count them as either).

**Example 1:**
```
Input:  "Hello World!"
Output: (3, 7)
Explanation: vowels e, o, o = 3; consonants H,l,l,W,r,l,d = 7. Space and '!' are ignored.
```

**Example 2:**
```
Input:  "AEIOUaeiou"
Output: (10, 0)
```

**Example 3:**
```
Input:  "12345!@#$%"
Output: (0, 0)
```

**Constraints:** 0 ≤ len(s) ≤ 1000.

---

## Problem 2 — Array (Easy-Medium)

### Title: Second Largest Distinct Element

Write a function `second_largest(arr)` that returns the **second largest distinct** element in an array of integers. Return -1 if there is no second largest (e.g., all elements are the same, or fewer than 2 elements).

**Example 1:**
```
Input:  [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: Largest = 35, second largest distinct = 34.
```

**Example 2:**
```
Input:  [10, 10, 10]
Output: -1
Explanation: All elements same; no second largest distinct value.
```

**Example 3:**
```
Input:  [5, 1]
Output: 1
```

**Example 4:**
```
Input:  [-1, -2, -3, -4]
Output: -2
Explanation: Largest = -1, second largest = -2.
```

**Constraints:** 0 ≤ len(arr) ≤ 10⁵. Try O(n) time and O(1) space.

---

## Problem 3 — Number/Pattern (Medium)

### Title: Number Pyramid

Write a function `pyramid(n)` that **prints** an n-row number pyramid. Row i (1-indexed) contains the numbers 1 through i, separated by spaces, centered appropriately so the output forms a symmetric pyramid shape.

**Example n = 4:**
```
   1
  1 2
 1 2 3
1 2 3 4
```

(Use single spaces between numbers and leading spaces to center; exact centering can be approximate but the shape must be pyramidal — each row indented one fewer space than the row below and one more than the row above.)

---

## Bonus / Variant Problem — SQL (recent drives include this)

Given two tables:

**employees**
| emp_id | name     | dept_id | salary |
|--------|----------|---------|--------|
| 1      | Alice    | 10      | 60000  |
| 2      | Bob      | 20      | 75000  |
| 3      | Charlie  | 10      | 50000  |
| 4      | Diana    | 30      | 85000  |
| 5      | Eve      | 20      | 70000  |

**departments**
| dept_id | dept_name |
|---------|-----------|
| 10      | HR        |
| 20      | Engineering |
| 30      | Finance   |
| 40      | Marketing |

**Q (a):** Write a query that returns each employee's name alongside their department name. Include employees even if their department doesn't exist in the departments table.

**Q (b):** Write a query that returns the average salary per department (show dept_name and average salary), only for departments whose average salary is above 60000. Order by average salary descending.

---

# Solutions — Mock Paper 3

### Solution to Problem 1 — Count Vowels and Consonants
```python
def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return (v, c)

# Tests
assert count_vowels_consonants("Hello World!") == (3, 7)
assert count_vowels_consonants("AEIOUaeiou") == (10, 0)
assert count_vowels_consonants("12345!@#$%") == (0, 0)
assert count_vowels_consonants("") == (0, 0)
print("P1 OK")
```
**Key idea:** iterate once, use `isalpha()` to ignore non-letters, use a set for vowels for O(1) membership.

---

### Solution to Problem 2 — Second Largest Distinct
```python
def second_largest(arr):
    if len(arr) < 2:
        return -1
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else -1

# Tests
assert second_largest([12, 35, 1, 10, 34, 1]) == 34
assert second_largest([10, 10, 10]) == -1
assert second_largest([5, 1]) == 1
assert second_largest([-1, -2, -3, -4]) == -2
assert second_largest([1]) == -1
assert second_largest([]) == -1
print("P2 OK")
```
**Key idea:** one pass tracking `first` (largest) and `second` (second largest distinct). Initialize to −∞; if `second` never gets updated, all elements are equal → return −1.
**Common traps:**
- Sorting and taking index −2 fails on duplicates.
- Initializing `second` to 0 or -1 fails for arrays with all-negative values (use −∞).
- Forgetting `num != first` when updating second would cause duplicates to claim "second largest."

---

### Solution to Problem 3 — Number Pyramid
```python
def pyramid(n):
    for i in range(1, n+1):
        # numbers for this row
        nums = " ".join(str(k) for k in range(1, i+1))
        # center the row in width of last row (which has all n numbers)
        width = len(" ".join(str(k) for k in range(1, n+1)))
        print(nums.center(width))

# Try it:
pyramid(4)
# Expected (approximate):
#    1
#  1 2
# 1 2 3
#1 2 3 4
```
**Key idea:** Use Python's `.center(width)` to do the leading spaces automatically. The last row determines the width. If `.center()` isn't available, calculate leading spaces manually as `n - i` spaces before the row.

**Alternative without `.center()`:**
```python
def pyramid2(n):
    for i in range(1, n+1):
        spaces = " " * (n - i)
        nums = " ".join(str(k) for k in range(1, i+1))
        print(spaces + nums)
```

---

### Solutions to Bonus SQL

**(a) Employee name + department name, keep employees with no dept:**
```sql
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;
```
We use LEFT JOIN so employees without a matching department are kept (dept_name will be NULL for them).

**(b) Average salary per department, only those with avg > 60000, ordered desc:**
```sql
SELECT d.dept_name, AVG(e.salary) AS avg_salary
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING AVG(e.salary) > 60000
ORDER BY avg_salary DESC;
```
Expected result for the sample data:
```
Finance      85000
Engineering  72500
```
(HR: avg(60000, 50000) = 55000, excluded. Marketing has no employees, so INNER JOIN omits it — if Marketing should be shown with NULL avg, use RIGHT JOIN or LEFT JOIN starting from departments.)

---

## Self-Evaluation Checklist

After coding, ask yourself:

- [ ] Did my Problem 1 handle mixed case, empty string, and non-letter characters?
- [ ] Did my Problem 2 handle duplicates, negative numbers, single element, and all-same arrays?
- [ ] Does my Problem 3 actually print a pyramid shape (each row one wider than above)?
- [ ] Did I test with the sample inputs before declaring done?
- [ ] Did I use good variable names so I don't confuse myself mid-code?

**Time benchmark:** If you can solve all three problems correctly in under **30 minutes** with tests, you're well-placed for the real assessment. If you take the full 60 minutes but get 3/3 correct, that's still a very good score.

---

## Extra Practice Problems (same style, no solutions provided — solve for reps)

1. **String:** Write a function that returns `True` if a given string is a palindrome, ignoring case and non-alphanumeric characters. Example: `"A man, a plan, a canal: Panama"` → True.
2. **Array:** Given an array of integers, return indices of the two numbers that add up to a given target (assume exactly one solution).
3. **Number:** Write a function `is_prime(n)` that returns True if n is prime.
4. **Number:** Write a function that returns the factorial of n both iteratively and recursively.
5. **Array:** Rotate an array by k positions to the right (in-place with O(1) extra space).
6. **Matrix:** Compute the transpose of a matrix.
7. **Pattern:** Print an inverted triangle of n rows.
8. **Linked List:** Reverse a singly linked list iteratively.
9. **Number:** Check if a number is an Armstrong number (e.g., 153 = 1³+5³+3³).
10. **Array:** Implement bubble sort and selection sort from scratch.

All of these have full implementations in **Chapter 6** for when you want to compare your answer.
