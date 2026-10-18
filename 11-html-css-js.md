# 11. Web Fundamentals — HTML, CSS, JavaScript (Frontend Section)

Per late-2025/2026 Accenture candidate reports, the coding round now includes a small **frontend task** alongside DSA and SQL. You're given a skeleton HTML/CSS/JS project and asked to make simple modifications (color changes, button clicks, DOM updates). This chapter covers exactly what you need — no advanced frameworks.

---

## 11.1 HTML — What You Need to Know

HTML (HyperText Markup Language) provides **structure** — headings, paragraphs, buttons, images, inputs, etc.

### Basic Document Skeleton
```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Hello Accenture</h1>
    <p>This is a paragraph.</p>
    <script src="script.js"></script>
</body>
</html>
```
- `<!DOCTYPE html>` declares HTML5.
- `<head>` contains metadata, title, CSS links.
- `<body>` contains visible content.
- Put `<script>` at the end of body (so DOM elements exist before JS runs) or use `defer`.

### Common Elements You MUST Know

| Tag | Purpose | Example |
|-----|---------|---------|
| `<h1> ... <h6>` | Headings (h1 largest, h6 smallest) | `<h1>Welcome</h1>` |
| `<p>` | Paragraph | `<p>Some text</p>` |
| `<a>` | Hyperlink (anchor) | `<a href="https://accenture.com">Click</a>` |
| `<img>` | Image (self-closing) | `<img src="logo.png" alt="Logo">` |
| `<button>` | Clickable button | `<button id="myBtn">Click me</button>` |
| `<div>` | Generic block container | `<div class="card">...</div>` |
| `<span>` | Generic inline container | `<span style="color:red">hi</span>` |
| `<ul>`, `<ol>`, `<li>` | Unordered/ordered lists | `<ul><li>Item</li></ul>` |
| `<input>` | Form input (self-closing) | `<input type="text" id="name">` |
| `<label>` | Label for input | `<label for="name">Name:</label>` |
| `<select>`, `<option>` | Dropdown | `<select><option>A</option></select>` |
| `<table>`, `<tr>`, `<td>`, `<th>` | Table rows/cells/headers | |
| `<br>` | Line break (self-closing) | |
| `<hr>` | Horizontal rule (self-closing) | |

### Key Attributes
- `id` — unique identifier for one element (used by JS `getElementById`).
- `class` — reusable class (multiple elements can share; used by CSS `.classname`).
- `style` — inline CSS (not best practice, but works).
- `src`, `href` — for images, links, scripts, stylesheets.
- `onclick` — inline JS handler (simple but not best practice): `<button onclick="doStuff()">Go</button>`.
- `value` — for form inputs/buttons.
- `placeholder` — hint text inside an input.

---

## 11.2 CSS — What You Need to Know

CSS (Cascading Style Sheets) provides **presentation** — colors, layout, fonts, spacing, animations.

### Three Ways to Apply CSS
1. **Inline** — `<p style="color: red;">Hi</p>` (highest specificity; avoid for large projects).
2. **Internal** — `<style>` block in `<head>`.
3. **External** — `<link rel="stylesheet" href="styles.css">` (best practice).

### Selectors (how you target elements)
```css
/* By element name */
p { color: blue; }

/* By id (use #) */
#myBtn { background-color: green; }

/* By class (use .) */
.card { border: 1px solid gray; padding: 10px; }

/* Descendant: <a> inside <li> */
li a { text-decoration: none; }

/* Hover pseudo-class */
button:hover { background-color: darkgreen; cursor: pointer; }
```

### Common Properties

| Property | Purpose | Examples |
|----------|---------|----------|
| `color` | Text color | `red`, `#ff0000`, `rgb(255,0,0)`, `rgba(255,0,0,0.5)` |
| `background-color` | Background fill | same values as color |
| `font-size` | Text size | `16px`, `1.2em`, `1rem`, `120%` |
| `font-weight` | Boldness | `normal`, `bold`, `400`, `700` |
| `text-align` | Horizontal alignment | `left`, `center`, `right`, `justify` |
| `padding` | Space INSIDE border | `10px`, `5px 10px` (vertical horizontal), `1px 2px 3px 4px` (TRBL) |
| `margin` | Space OUTSIDE border | same shorthand as padding; `margin: 0 auto;` centers block element |
| `border` | Border | `1px solid black`; `border-radius: 8px;` for rounded corners |
| `width`, `height` | Dimensions | `200px`, `50%`, `100vw` |
| `display` | Layout behavior | `block`, `inline`, `inline-block`, `none` (hides), `flex`, `grid` |
| `position` | Positioning | `static` (default), `relative`, `absolute`, `fixed`, `sticky` |
| `display: flex` | Flexbox (centering, rows) | use with `justify-content` (horizontal) and `align-items` (vertical) |
| `cursor` | Mouse pointer | `pointer`, `default`, `not-allowed` |
| `box-shadow` | Shadow effect | `2px 2px 5px gray` |

### The Box Model
Every element is a box with four layers (inside to outside):
**Content → Padding → Border → Margin.**

Total element width = content-width + 2×padding + 2×border (unless `box-sizing: border-box`, in which case width INCLUDES padding/border).

### Color Formats
- Named: `red`, `blue`, `white`, `black`, `gray`, etc.
- Hex: `#FF0000` (red), `#00FF00` (green), `#0000FF` (blue), `#000000` (black), `#FFFFFF` (white). 3-digit shorthand `#F00` = `#FF0000`.
- RGB: `rgb(255, 0, 0)` = red.
- RGBA: `rgba(255, 0, 0, 0.5)` = red with 50% transparency.

### Centering an element (common task)
```css
/* Center horizontally */
.center {
    margin: 0 auto;
    width: 300px;
}

/* Center both ways using flexbox on parent */
.parent {
    display: flex;
    justify-content: center;   /* horizontal */
    align-items: center;       /* vertical */
    height: 100vh;             /* full viewport height */
}
```

### Making colored boxes (common in Accenture frontend tasks)
```css
.box {
    width: 100px;
    height: 100px;
    background-color: blue;
    margin: 5px;
    display: inline-block;
}
```
```html
<div class="box"></div>
<div class="box"></div>
<div class="box"></div>
```

---

## 11.3 JavaScript — What You Need to Know

JavaScript provides **behavior** — handling clicks, updating content, form validation, dynamic styling.

### Where to put it
- In a separate file (best): `<script src="script.js"></script>` at end of `<body>`.
- Inline in HTML: `<button onclick="myFunction()">Click</button>`.
- In a `<script>` tag.

### Variables
```javascript
// Modern: let (can change) and const (cannot reassign)
let name = "Alice";
const PI = 3.14;
var oldStyle = "avoid var";   // old style, function-scoped
```

### Basic Data Types
- **String:** `"hello"`, `'hello'`, `` `hello ${name}` `` (template literals with backticks)
- **Number:** `42`, `3.14`
- **Boolean:** `true`, `false`
- **Array:** `[1, 2, 3]`
- **Object:** `{name: "Alice", age: 25}`
- `null`, `undefined`

### Functions
```javascript
// Traditional function
function add(a, b) {
    return a + b;
}

// Arrow function (modern)
const multiply = (a, b) => a * b;

// Calling
console.log(add(2, 3));   // 5
```

### DOM Manipulation (THE MOST IMPORTANT PART FOR THE TEST)

The DOM (Document Object Model) is how JS sees the HTML page — a tree of elements you can read and modify.

#### Selecting elements
```javascript
// By id (returns one element)
const btn = document.getElementById("myBtn");

// By class (returns HTMLCollection - array-like)
const cards = document.getElementsByClassName("card");

// By tag name
const paras = document.getElementsByTagName("p");

// By CSS selector (returns first match)
const el = document.querySelector("#myBtn");
const firstCard = document.querySelector(".card");

// By CSS selector (returns ALL matches as NodeList)
const allButtons = document.querySelectorAll("button");
```

#### Changing content
```javascript
element.textContent = "New text";          // plain text (safe)
element.innerHTML = "<b>Bold</b> text";    // parsed as HTML (watch for XSS)
```

#### Changing styles
```javascript
element.style.color = "red";
element.style.backgroundColor = "yellow";    // note camelCase, not "background-color"
element.style.fontSize = "20px";
element.style.display = "none";              // hide
element.style.display = "block";             // show
```

#### Changing attributes
```javascript
element.setAttribute("src", "newimage.jpg");
element.getAttribute("href");
element.id = "newId";
element.classList.add("highlight");
element.classList.remove("hidden");
element.classList.toggle("active");
```

#### Creating & inserting elements
```javascript
const newDiv = document.createElement("div");
newDiv.textContent = "Hello";
newDiv.className = "box";
document.body.appendChild(newDiv);             // add at end

// Or insert before a specific element
parent.insertBefore(newDiv, existingChild);
```

#### Event listeners (handling button clicks — ESSENTIAL)
```javascript
const btn = document.getElementById("myBtn");

btn.addEventListener("click", function() {
    alert("Button clicked!");
    // Or update something on the page:
    document.getElementById("message").textContent = "You clicked!";
});

// Arrow shorthand
btn.addEventListener("click", () => {
    console.log("clicked");
});
```

#### Getting input values
```javascript
const input = document.getElementById("nameInput");
const value = input.value;              // read
input.value = "";                       // clear

// Example: show an alert with the typed name
document.getElementById("greetBtn").addEventListener("click", () => {
    const name = document.getElementById("nameInput").value;
    alert("Hello " + name + "!");
});
```

### Common Patterns You'll Be Asked to Do
1. **Change box color on click**: toggle between two colors, or change to a random color.
2. **Button click counter**: click a button, increment a number on screen.
3. **Show/hide elements**: toggle `display: none` / `display: block`.
4. **Form validation**: check if an input is not empty / is a valid email before showing a message.
5. **Add items to a list**: type in a text box, click Add, item appears in `<ul>`.
6. **Todo list**: add + delete items.
7. **Change text/background color based on a dropdown selection**.

### Conditionals & Loops (same logic as pseudocode)
```javascript
if (score >= 50) {
    console.log("Pass");
} else {
    console.log("Fail");
}

for (let i = 0; i < 5; i++) {
    console.log(i);
}

const arr = [10, 20, 30];
arr.forEach(num => console.log(num));
```

---

## 11.4 Worked Example — A Complete Mini Task

**Task:** Create a page with a button and a counter. Each button click increments the counter display. Add a second button that resets to 0. The counter is red when ≥10, green otherwise.

**HTML (index.html):**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Counter</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Click Counter</h1>
    <p id="counterDisplay">0</p>
    <button id="incrementBtn">Click me!</button>
    <button id="resetBtn">Reset</button>
    <script src="script.js"></script>
</body>
</html>
```

**CSS (styles.css):**
```css
body {
    text-align: center;
    font-family: Arial, sans-serif;
    padding-top: 40px;
}

#counterDisplay {
    font-size: 64px;
    font-weight: bold;
    color: green;
}

button {
    font-size: 18px;
    padding: 10px 20px;
    margin: 5px;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    background-color: #2196F3;
    color: white;
}

button:hover {
    background-color: #0b7dda;
}

.red { color: red; }
.green { color: green; }
```

**JavaScript (script.js):**
```javascript
let count = 0;
const display = document.getElementById("counterDisplay");
const incBtn = document.getElementById("incrementBtn");
const resetBtn = document.getElementById("resetBtn");

incBtn.addEventListener("click", () => {
    count++;
    updateDisplay();
});

resetBtn.addEventListener("click", () => {
    count = 0;
    updateDisplay();
});

function updateDisplay() {
    display.textContent = count;
    if (count >= 10) {
        display.classList.remove("green");
        display.classList.add("red");
    } else {
        display.classList.remove("red");
        display.classList.add("green");
    }
}
```

**Key points demonstrated:**
- `getElementById` to grab elements.
- `addEventListener("click", ...)` to respond to clicks.
- `.textContent` to update what's shown.
- `.classList.add/remove` to change styling dynamically.
- A helper function (`updateDisplay`) to keep code DRY.

---

## Practice Questions — HTML/CSS/JS

**Q1.** Which HTML tag creates a clickable button?
- a) `<btn>`
- b) `<button>`
- c) `<click>`
- d) `<press>`

**Q2.** Which CSS selector targets an element with `id="box1"`?
- a) `.box1`
- b) `#box1`
- c) `box1`
- d) `*box1`

**Q3.** To make an element's text red in CSS:
- a) `text-color: red;`
- b) `font-color: red;`
- c) `color: red;`
- d) `bgcolor: red;`

**Q4.** Which JavaScript method selects ONE element by its id?
- a) `document.querySelector(".foo")`
- b) `document.getElementById("foo")`
- c) `document.getElementsByClassName("foo")`
- d) `document.find("foo")`

**Q5.** To change the text inside `<p id="msg">Hello</p>` to "Goodbye" using JS:
- a) `document.getElementById("msg").textContent = "Goodbye"`
- b) `document.getElementById("msg") = "Goodbye"`
- c) `document.getElementById("msg").value = "Goodbye"`
- d) `#msg.setText("Goodbye")`

**Q6.** Which CSS property controls space INSIDE an element (between content and border)?
- a) margin
- b) padding
- c) border
- d) spacing

**Q7.** In CSS, `#abc .xyz` selects:
- a) Element with id `xyz` inside element with class `abc`
- b) Element with class `xyz` inside element with id `abc`
- c) Element with both id `abc` and class `xyz`
- d) Two separate elements

**Q8.** What does `element.style.display = "none"` do?
- a) Makes element visible
- b) Removes element from layout (hidden)
- c) Changes text to "none"
- d) Sets color to black

**Q9.** Which HTML attribute specifies the URL when clicking a link?
- a) `src`
- b) `link`
- c) `href`
- d) `url`

**Q10.** How do you attach a click handler in JS?
- a) `element.onClick = fn`
- b) `element.click(fn)`
- c) `element.addEventListener("click", fn)`
- d) `element.listen("click", fn)`

**Q11 (Practical).** Write HTML for a page with:
- A heading "Color Changer"
- A div 200×200px with id "box" initially blue, centered
- Two buttons under it: "Red" and "Green"
- When "Red" is clicked, box becomes red; "Green" makes it green.

**Q12 (Practical).** Write a simple to-do app:
- Text input with id "todoInput" and a button "Add"
- An empty `<ul id="todoList">`
- When "Add" is clicked, take the input text, add a new `<li>` to the list with that text, and clear the input.

---

## Answer Key — HTML/CSS/JS

1. **b** — `<button>` is the correct tag.
2. **b** — `#` for id, `.` for class.
3. **c** — The property is `color`, not `text-color` or `font-color`.
4. **b** — `getElementById` returns one element by id. `querySelector(".foo")` selects by class, not id.
5. **a** — `.textContent` is the correct property for text. `.value` is for form inputs.
6. **b** — padding is inside; margin is outside.
7. **b** — Descendant selector: elements with class `xyz` inside an element with id `abc`.
8. **b** — `display: none` hides the element completely from layout.
9. **c** — `<a>` uses `href`; images/scripts use `src`.
10. **c** — `addEventListener("click", handler)` is the standard way.

**Solution to Q11 (Color Changer):**

*index.html:*
```html
<!DOCTYPE html>
<html>
<head>
<style>
  #box {
    width: 200px;
    height: 200px;
    background-color: blue;
    margin: 20px auto;
  }
  body { text-align: center; }
  button { padding: 8px 16px; margin: 5px; cursor: pointer; }
</style>
</head>
<body>
  <h1>Color Changer</h1>
  <div id="box"></div>
  <button id="redBtn">Red</button>
  <button id="greenBtn">Green</button>
  <script>
    const box = document.getElementById("box");
    document.getElementById("redBtn").addEventListener("click", () => {
      box.style.backgroundColor = "red";
    });
    document.getElementById("greenBtn").addEventListener("click", () => {
      box.style.backgroundColor = "green";
    });
  </script>
</body>
</html>
```

**Solution to Q12 (To-do):**

*index.html:*
```html
<h1>Todo List</h1>
<input type="text" id="todoInput" placeholder="Add a task...">
<button id="addBtn">Add</button>
<ul id="todoList"></ul>
<script>
  const input = document.getElementById("todoInput");
  const list  = document.getElementById("todoList");
  document.getElementById("addBtn").addEventListener("click", () => {
    const text = input.value.trim();
    if (text === "") return;
    const li = document.createElement("li");
    li.textContent = text;
    list.appendChild(li);
    input.value = "";
  });
  // Allow Enter key to add too
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") document.getElementById("addBtn").click();
  });
</script>
```
