# 6. Coding Assessment (3 questions, 60 minutes)

Difficulty is easy to medium. All solutions below are given in **Python** (which is also readable as pseudocode). Practice writing these out on paper, then typing them without looking.

**Strategy tips for the actual test:**
1. Read all three questions first and start with the easiest (builds confidence, unlocks points fast).
2. Get a working *naive* solution first, then optimize if you have time.
3. Test with sample inputs manually before submitting.
4. Watch edge cases: empty input, single element, negative numbers, zero, duplicates.

---

## 6.1 String Manipulation

### 1) Reverse a string
```python
def reverse_string(s):
    return s[::-1]

# Manual method
def reverse_string_manual(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)

print(reverse_string("hello"))        # "olleh"
```

### 2) Check palindrome
A string that reads the same forwards and backwards (ignoring case/non-alphanumerics if asked).
```python
def is_palindrome(s):
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("Racecar"))   # True
print(is_palindrome("hello"))     # False
```

### 3) Count vowels and consonants
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
    return v, c

print(count_vowels_consonants("Hello World"))   # (3, 7)
```

### 4) Frequency of each character
```python
from collections import Counter

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_frequency("apple"))   # {'a':1, 'p':2, 'l':1, 'e':1}
```

### 5) Anagram check
Two strings are anagrams if they contain the same characters with the same frequencies.
```python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Or with Counter:
from collections import Counter
def is_anagram2(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))   # True
```

### 6) Remove duplicates from a string (preserve order)
```python
def remove_duplicates(s):
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return ''.join(result)

print(remove_duplicates("programming"))   # "progamin"
```

### 7) First non-repeating character
```python
def first_non_repeating(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

print(first_non_repeating("aabbcde"))   # "c"
```

---

## 6.2 Array Problems

### 1) Find second largest element
```python
def second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None

print(second_largest([12, 35, 1, 10, 34, 1]))   # 34
```

### 2) Sum of elements / Running sum
```python
def sum_of_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total  # or just sum(arr)

def running_sum(arr):
    res = []
    total = 0
    for num in arr:
        total += num
        res.append(total)
    return res

print(running_sum([1,2,3,4]))   # [1,3,6,10]
```

### 3) Rotate array by k positions
```python
def rotate_right(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k] if k else arr

# In-place reversal method (O(1) extra space)
def reverse(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

def rotate_in_place(arr, k):
    n = len(arr)
    k = k % n
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)

arr = [1,2,3,4,5,6,7]
rotate_in_place(arr, 3)
print(arr)   # [5,6,7,1,2,3,4]
```

### 4) Check if array is sorted
```python
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

print(is_sorted([1,2,3,4]))   # True
print(is_sorted([1,3,2]))     # False
```

### 5) Two Sum — pair with given sum
```python
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

print(two_sum([2,7,11,15], 9))   # [0,1]
```

### 6) Maximum subarray sum (Kadane's Algorithm)
```python
def max_subarray(arr):
    max_sum = curr = arr[0]
    for num in arr[1:]:
        curr = max(num, curr + num)
        max_sum = max(max_sum, curr)
    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))   # 6 (subarray [4,-1,2,1])
```

### 7) Count occurrences of an element
```python
def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

print(count_occurrences([1,2,3,2,2,4], 2))   # 3
```

---

## 6.3 Number Problems

### 1) Check prime
```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

print(is_prime(17))   # True
print(is_prime(18))   # False
```

### 2) Generate Fibonacci up to N terms
```python
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq

print(fibonacci(10))   # [0,1,1,2,3,5,8,13,21,34]
```

### 3) Factorial
```python
def factorial_iter(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

print(factorial_iter(5))   # 120
```

### 4) Reverse digits of a number
```python
def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return sign * rev

print(reverse_number(-1234))   # -4321
```

### 5) Armstrong number
A number equal to the sum of its own digits each raised to the power of the number of digits (e.g., 153 = 1³ + 5³ + 3³ = 153).
```python
def is_armstrong(n):
    s = str(n)
    power = len(s)
    total = sum(int(d) ** power for d in s)
    return total == n

print(is_armstrong(153))   # True
print(is_armstrong(9474))  # True (4-digit)
```

### 6) Sum of digits
```python
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(sum_of_digits(1234))   # 10
```

### 7) GCD and LCM
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(12, 18))   # 6
print(lcm(12, 18))   # 36
```

---

## 6.4 Pattern Printing

When asked to print patterns: **outer loop = rows, inner loop = columns per row**. Print a new line after each row.

### 1) Right triangle (stars)
```python
def right_triangle(n):
    for i in range(1, n+1):
        print('*' * i)

right_triangle(4)
# *
# **
# ***
# ****
```

### 2) Pyramid (centered)
```python
def pyramid(n):
    for i in range(1, n+1):
        print(' ' * (n - i) + '*' * (2*i - 1))

pyramid(4)
#    *
#   ***
#  *****
# *******
```

### 3) Inverted triangle
```python
def inverted_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

inverted_triangle(4)
# ****
# ***
# **
# *
```

### 4) Number pattern
```python
def number_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end='')
        print()

number_pattern(4)
# 1
# 12
# 123
# 1234
```

### 5) Alphabet pattern
```python
def alpha_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('A') + j), end='')
        print()

alpha_pattern(4)
# A
# AB
# ABC
# ABCD
```

---

## 6.5 Sorting and Searching

### 1) Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break   # already sorted
    return arr

print(bubble_sort([5,2,8,1,3]))   # [1,2,3,5,8]
```

### 2) Selection Sort
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### 3) Binary Search
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1,3,5,7,9,11], 7))   # 3
```

---

## 6.6 Linked List Basics

Simple singly linked list node:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### 1) Traverse and print
```python
def traverse(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")
```

### 2) Find middle element (slow & fast pointer)
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data
```

### 3) Insert at head/tail
```python
def insert_head(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node

def insert_tail(head, val):
    new_node = Node(val)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head
```

---

## 6.7 Matrix Operations

### 1) Transpose of a matrix
```python
def transpose(mat):
    rows = len(mat)
    cols = len(mat[0])
    res = [[mat[j][i] for j in range(rows)] for i in range(cols)]
    return res

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
# [[1,4,7],[2,5,8],[3,6,9]]
```

### 2) Diagonal sum (square matrix)
```python
def diagonal_sum(mat):
    n = len(mat)
    total = 0
    for i in range(n):
        total += mat[i][i]               # main diagonal
        if i != n - 1 - i:               # anti-diagonal (avoid double-counting center)
            total += mat[i][n-1-i]
    return total

print(diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))   # 1+5+9 + 3+7 = 25
```

### 3) Spiral traversal
```python
def spiral_order(mat):
    res = []
    if not mat:
        return res
    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):   # top row
            res.append(mat[top][i])
        top += 1
        for i in range(top, bottom + 1):   # right column
            res.append(mat[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):   # bottom row
                res.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):   # left column
                res.append(mat[i][left])
            left += 1
    return res

print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))   # [1,2,3,6,9,8,7,4,5]
```

---

# Practice Set — Try These Before Looking at Solutions

### Problem 1 — String
Write a function that takes a sentence and returns the longest word.
```
Input : "The quick brown fox jumps over the lazy dog"
Output: "quick"  (or "jumps" / "brown" — same length; return the first)
```

### Problem 2 — Array
Given an array `nums` and an integer `target`, return **indices** of the two numbers such that they add up to target. You may assume exactly one solution exists and you may not use the same element twice.

### Problem 3 — Number
Write a function that returns `True` if a given integer is a palindrome (without converting to string). E.g., 121 → True, -121 → False (reads -121-).

### Problem 4 — Pattern
Print this pattern for n=5:
```
A
BB
CCC
DDDD
EEEEE
```

### Problem 5 — Matrix
Rotate a square matrix **90 degrees clockwise** in-place.
```
Input:  [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

### Problem 6 — Linked List
Reverse a singly linked list and return the new head.

---

## Solutions to Practice Set

### Solution 1
```python
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest
```

### Solution 2
```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return []
```

### Solution 3
```python
def is_num_palindrome(n):
    if n < 0:
        return False
    original, rev = n, 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return original == rev
```

### Solution 4
```python
def alpha_count_pattern(n):
    for i in range(n):
        ch = chr(ord('A') + i)
        print(ch * (i + 1))
```

### Solution 5
```python
def rotate_90(mat):
    n = len(mat)
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # Reverse each row
    for i in range(n):
        mat[i].reverse()
    return mat
```

### Solution 6
```python
def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

---

# Quick-Reference Checklist for Exam Day

Before you start coding, scan this list:
- [ ] Did I read the problem carefully? (Return value? Print or return? 0-based or 1-based?)
- [ ] Did I consider edge cases (empty input, 1 element, negatives, duplicates, zero)?
- [ ] Do my loops terminate correctly (off-by-one)?
- [ ] For string problems: am I handling case/spaces/punctuation as specified?
- [ ] For array/number problems: should I sort first, or use a hash set/map to avoid O(n²)?
- [ ] Did I test with the sample input on paper mentally?
- [ ] Can I get a simpler solution by using Python built-ins (slicing, `sorted`, `Counter`, `set`)? Go with the readable, correct one.
