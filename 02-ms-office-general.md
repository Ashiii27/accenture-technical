# 2. MS Office & Common Applications

---

## 2.1 MS Word

### Essential Shortcut Keys

| Shortcut | Action |
|----------|--------|
| **Ctrl + Z** | Undo last action |
| **Ctrl + Y** | Redo (or repeat) last action |
| **Ctrl + F** | Find |
| **Ctrl + H** | Find and Replace |
| **Ctrl + B** | Bold toggle |
| **Ctrl + I** | Italic toggle |
| **Ctrl + U** | Underline toggle |
| Ctrl + C | Copy |
| Ctrl + V | Paste |
| Ctrl + X | Cut |
| Ctrl + A | Select all |
| Ctrl + S | Save |
| Ctrl + N | New document |
| Ctrl + O | Open |
| Ctrl + P | Print |
| Ctrl + Enter | Page break |
| Ctrl + Home/End | Go to start/end of document |
| F7 | Spell check |
| Shift + F3 | Change case (toggle UPPER/lower/Title) |
| Ctrl + Shift + >/< | Increase/decrease font size |

### Mail Merge
Used to create a batch of personalized documents (letters, envelopes, labels, emails) from a single template.
1. **Main document** — the template with placeholders (e.g., «Name», «Address»).
2. **Data source** — typically Excel, Access, or Outlook Contacts; each row = one recipient.
3. **Insert merge fields** — place field markers in the document.
4. **Preview results** — verify names/addresses appear correctly.
5. **Finish & Merge** — output to printer, new document, or email.

### Track Changes
- Found on the **Review** tab.
- Records every insertion, deletion, move, and format change with the reviewer's name/color.
- Changes can be **Accepted** or **Rejected** one by one or all at once.
- Use **Comments** for discussion without altering text.
- Useful for editing workflows where multiple people review a document.

### Table of Contents (TOC)
- Generated from **Heading styles** (Heading 1, Heading 2, Heading 3, etc.).
- Insert via **References → Table of Contents**.
- Automatically creates a hierarchical list with page numbers.
- **Update Table** after edits (right-click or References tab) to refresh page numbers and headings.
- To modify entries, edit the heading style applied to paragraphs — do not type directly in the TOC.

### Header, Footer, and Page Numbering
- **Header** = top margin area; **Footer** = bottom margin area (Insert tab).
- Often contains document title, company logo, page numbers, dates.
- **Page numbers** can be placed in header, footer, or margins; formats include 1,2,3 or i,ii,iii.
- **Different First Page** option hides header/footer on page 1 (useful for title pages).
- **Link to Previous** controls whether headers/footers carry over from the previous section — turn off to have different headers per section.
- Section breaks (not just page breaks) are needed to change headers/footers or page numbering within a document.

### Paragraph vs Character Formatting
- **Character formatting** applies to selected text/characters: font face, size, bold, italic, underline, color, superscript/subscript, highlight.
- **Paragraph formatting** applies to whole paragraphs: alignment (left/center/right/justify), indentation, line spacing, space before/after, bullets/numbering, tabs, borders/shading, paragraph styles.
- A paragraph is any text terminated by an ¶ (pilcrow) mark.
- Format Painter (paintbrush icon) copies character+paragraph formatting from one selection to another. Double-click to apply to multiple selections.

---

## 2.2 MS Excel

### Cell Referencing
- **Relative** (e.g., `=A1`) — adjusts when copied across rows/columns.
- **Absolute** (e.g., `=$A$1`) — stays fixed when copied (dollar signs lock both column and row).
- **Mixed** (e.g., `$A1` or `A$1`) — locks either the column or the row.
- Toggle reference types with **F4** while editing a formula.

### Basic Formulas

| Formula | Purpose | Example |
|---------|---------|---------|
| `=SUM(range)` | Adds numbers | `=SUM(A1:A10)` |
| `=AVERAGE(range)` | Arithmetic mean (ignores blanks, text) | `=AVERAGE(B1:B10)` |
| `=COUNT(range)` | Counts **numeric** cells | `=COUNT(C1:C20)` |
| `=COUNTA(range)` | Counts **non-empty** cells (includes text) | `=COUNTA(D1:D20)` |
| `=COUNTIF(range, criteria)` | Counts cells that meet a condition | `=COUNTIF(A1:A10,">50")` |
| `=SUMIF(range, criteria, sum_range)` | Sums cells meeting a condition | `=SUMIF(A1:A10,"Apple",B1:B10)` |

### Lookup Functions
- **VLOOKUP(lookup_value, table_array, col_index, [range_lookup])**
  - Looks up a value in the **first column** of a table and returns a value from a specified column in the same row.
  - `range_lookup = FALSE` for exact match; `TRUE` (or omitted) for approximate match (first column must be sorted).
  - Can only look to the right (a major limitation).
  - Example: `=VLOOKUP(101, A2:D100, 3, FALSE)` finds 101 in column A and returns column C value.
- **HLOOKUP** — same but searches horizontally (first row instead of first column).
- **INDEX + MATCH** (more flexible than VLOOKUP):
  - `INDEX(range, row_num, col_num)` returns value at given position.
  - `MATCH(value, range, 0)` returns position of value (0 = exact match).
  - Combined: `=INDEX(C2:C100, MATCH(101, A2:A100, 0))` — looks left or right, more robust when columns are inserted.

### Logical Functions
- `=IF(condition, value_if_true, value_if_false)` — decision making.
  - Example: `=IF(A1>=40,"Pass","Fail")`
- `=AND(cond1, cond2,…)` — TRUE only if ALL conditions are true.
- `=OR(cond1, cond2,…)` — TRUE if ANY condition is true.
- `=NOT(cond)` — reverses TRUE/FALSE.
- **Nested IF** — multiple chained IFs:
  - `=IF(A1>=90,"A",IF(A1>=75,"B",IF(A1>=50,"C","F")))`

### Text Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `=CONCATENATE(...)` or `&` | Joins text | `=A1&" "&B1` → "John Doe" |
| `=LEFT(text, n)` | First n characters | `=LEFT("Excel",3)` → "Exc" |
| `=RIGHT(text, n)` | Last n characters | `=RIGHT("Excel",2)` → "el" |
| `=MID(text, start, n)` | Middle substring (start is 1-based) | `=MID("Excel",2,3)` → "xce" |
| `=LEN(text)` | Character count | `=LEN("Hello")` → 5 |
| `=TRIM(text)` | Removes extra spaces | `=TRIM("  hi  ")` → "hi" |
| `=UPPER(text)` | Uppercase | `=UPPER("hi")` → "HI" |
| `=LOWER(text)` | Lowercase | `=LOWER("HI")` → "hi" |
| `=PROPER(text)` | Capitalizes first letter of each word | `=PROPER("john doe")` → "John Doe" |

### Date Functions
- `=TODAY()` — current date (updates on open).
- `=NOW()` — current date and time (updates on open).
- `=DATEDIF(start, end, unit)` — difference between dates. Units: `"Y"` years, `"M"` months, `"D"` days.
  - Example: `=DATEDIF(A1,TODAY(),"Y")` gives age in years.

### Pivot Tables
- Interactive summary tables built from a data range/table.
- Used to **aggregate, group, and analyze** large datasets quickly without writing formulas.
- Drag fields into four areas: **Filters, Rows, Columns, Values**.
- Values area can SUM, COUNT, AVERAGE, MAX, MIN, etc.
- Ideal for: sales summaries by region/month, counting occurrences, cross-tabulations.
- Refresh after source data changes (Right-click → Refresh).

### Charts — Choosing the Right Type
| Chart | Best For |
|-------|----------|
| Column/Bar | Comparing categories (e.g., sales by region) |
| Line | Trends over time (e.g., monthly revenue) |
| Pie | Parts of a whole (one series only; avoid with > 5–6 slices) |
| Scatter (XY) | Relationship between two numeric variables |
| Area | Volume over time, emphasizing magnitude |
| Combo | Combining two measures with different scales (e.g., bars + line) |
| Histogram | Distribution/frequency of numerical data |

### Conditional Formatting
- Dynamically changes cell formatting (fill, font color, icons, data bars) based on rules/conditions.
- Common rules: Highlight Cells greater than/less than/equal to, Top/Bottom 10%, Color Scales (heat maps), Icon Sets, Data Bars.
- Found on the **Home** tab. Rules can be customized with formulas.

---

## 2.3 MS PowerPoint

### Slide Layouts & Master Slides
- **Slide Layouts** (Home tab → Layout) are pre-built arrangements of placeholders (Title, Title and Content, Two Content, Blank, etc.).
- **Slide Master** (View tab → Slide Master) is the top-level template that controls the theme, fonts, colors, logos, and default layouts for **all slides** in the deck.
- Edit the Slide Master once to add a logo, change default font, or insert a footer across every slide instead of editing slides individually.
- Changes to the master propagate to layouts and slides based on it.

### Transitions vs Animations
- **Transitions** = visual effects when moving **between slides** (e.g., Fade, Push, Wipe, Morph). Controlled on the Transitions tab; applied per slide.
- **Animations** = motion effects applied **to objects on a single slide** (e.g., fly-in text, bullet points appearing one by one, image zoom). Controlled on the Animations tab; applied per object.
- Key rule: use sparingly in professional decks — too many effects distract from content.

### Presenter View
- Extends the presentation across two displays: the **audience sees the full slideshow** on the projector/screen, while you (on your laptop) see:
  - Current slide
  - Next slide preview
  - Speaker notes
  - Timer/clock
  - Pen/laser pointer tools
- Enable via Slide Show tab → Use Presenter View. Requires extended (not mirrored) desktop.

### Slide Numbers, Headers, Footers
- Insert → **Header & Footer** opens a dialog where you can:
  - Show/hide slide numbers.
  - Add footer text, date/time (fixed or auto-updating).
  - "Don't show on title slide" checkbox.
- Notes and Handouts have their own headers/footers separate from slides.

---

## 2.4 General Computer Knowledge

### Common Windows Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **Alt + Tab** | Switch between open windows/applications |
| **Alt + F4** | Close the active window (or show shutdown dialog if no window) |
| **Win + D** | Show/hide desktop instantly |
| Ctrl + C | Copy |
| Ctrl + V | Paste |
| Ctrl + X | Cut |
| Ctrl + Z | Undo |
| Ctrl + A | Select all |
| Win + E | Open File Explorer |
| Win + L | Lock computer |
| Win + R | Open Run dialog |
| Ctrl + Shift + Esc | Open Task Manager directly |
| Alt + Ctrl + Del | Security screen (lock, switch user, task mgr) |
| F2 | Rename selected file |
| F5 | Refresh |

### File Extensions

| Extension | File Type |
|-----------|-----------|
| `.docx` | Microsoft Word document (modern, XML-based) |
| `.doc` | Legacy Word document (binary) |
| `.xlsx` | Microsoft Excel workbook |
| `.pptx` | Microsoft PowerPoint presentation |
| `.pdf` | Portable Document Format (Adobe) |
| `.csv` | Comma-Separated Values (plain text tabular data) |
| `.txt` | Plain text file |
| `.exe` | Executable program (Windows) |
| `.dll` | Dynamic-Link Library — shared code used by .exe files |
| `.bat` | Batch file — script of Windows command-line commands |
| `.zip/.rar/.7z` | Compressed archives |
| `.html/.htm` | Web page |
| `.jpg/.png/.gif` | Image files |
| `.mp3/.wav/.mp4` | Audio/video files |

### Primary vs Secondary Storage
- **Primary Storage (Main Memory)** — directly accessible by the CPU; volatile or small/fast:
  - **RAM** (Random Access Memory) — volatile, working memory, fast, temporary.
  - **ROM** (Read-Only Memory) — non-volatile, contains BIOS/firmware, rarely written to.
  - Cache (L1/L2/L3) — fastest, on-CPU.
  - Registers — inside CPU, tiny.
- **Secondary Storage** — persistent, larger, slower, non-volatile:
  - HDD, SSD, USB flash drives, CD/DVD, optical drives, external drives.
- **Tertiary Storage** — archival (tape libraries, cloud cold storage).

### RAM vs ROM

| Feature | RAM | ROM |
|---------|-----|-----|
| Read/Write | Both read and write | Mostly read |
| Volatility | Volatile (lost on power off) | Non-volatile (retains data) |
| Purpose | Running programs / current data | Firmware/BIOS, boot instructions |
| Speed | Very fast | Slower than RAM |
| Size | Larger (GB) | Small (MB/KB) |
| Types | DRAM, SRAM, DDR4/5 | PROM, EPROM, EEPROM, Flash |

### Types of Software
- **System Software** — manages the computer itself.
  - Operating Systems (Windows, macOS, Linux, Android, iOS)
  - Device drivers, firmware, utilities (antivirus, disk defragmenter)
- **Application Software** — end-user programs to perform tasks.
  - Word processors, spreadsheets, browsers, games, email clients, Photoshop.
- **Utility Software** — subset of system software for maintenance: antivirus, backup tools, disk cleaners, compression tools, file managers.
- **Programming/Development Software** — IDEs, compilers, interpreters, debuggers.

### Operating System Functions
1. **Process Management** — CPU scheduling, process creation/termination, multitasking, deadlock handling.
2. **Memory Management** — RAM allocation, virtual memory (paging/segmentation), memory protection.
3. **File Management** — file/directory organization, permissions, access, storage allocation on disk.
4. **Device Management** — drivers, I/O control, buffering, spooling.
5. **Security & Access Control** — user accounts, authentication, permissions.
6. **User Interface** — CLI or GUI (shell, desktop, windows).
7. **Networking** — protocol stacks, network resource sharing.

---

# Practice Questions — MS Office & General Computer Knowledge

**(Answers at the end)**

### MS Word
1. Which shortcut opens Find & Replace?
   a) Ctrl+F  b) Ctrl+H  c) Ctrl+R  d) Ctrl+S
2. To create a batch of personalized letters, you would use:
   a) Mail Merge  b) Track Changes  c) TOC  d) Macros
3. A Table of Contents is built primarily from:
   a) Comments  b) Footnotes  c) Heading styles  d) Bookmarks
4. Bold, italic, and underline are examples of:
   a) Paragraph formatting  b) Character formatting  c) Section formatting  d) Page formatting
5. To have different headers on odd and even pages you must first:
   a) Insert a page break  b) Use mail merge  c) Enable "Different odd & even" and potentially use section breaks  d) Restart Word

### MS Excel
6. Which formula counts only numeric entries in a range?
   a) COUNTA  b) COUNT  c) COUNTIF  d) SUM
7. `=MID("HELLO",2,3)` returns:
   a) "HEL"  b) "ELL"  c) "LLO"  d) "HE"
8. Which cell reference stays fixed when copied?
   a) A1  b) $A$1  c) A$1  d) $A1
9. To look up a value anywhere in a table (not just the first column), the best combination is:
   a) VLOOKUP alone  b) HLOOKUP alone  c) INDEX + MATCH  d) SUMIF
10. `=IF(A1>=50,"PASS","FAIL")` when A1=49 returns:
    a) PASS  b) FAIL  c) ERROR  d) 50
11. Pivot tables are best used for:
    a) Writing long documents  b) Summarizing and aggregating large datasets  c) Editing images  d) Sending email
12. Which function joins text strings together?
    a) JOIN  b) CONCATENATE or &  c) MERGE  d) BIND

### MS PowerPoint
13. Motion effects applied to objects on a single slide are called:
    a) Transitions  b) Animations  c) Masters  d) Macros
14. To apply a logo to every slide in the deck efficiently, edit:
    a) Each slide individually  b) Slide Master  c) Handout Master  d) Notes Page
15. Presenter View shows the audience the full slideshow while showing you:
    a) The same view exactly  b) Current slide, next slide, notes, timer  c) Only the desktop  d) A blank screen

### General Computer Knowledge
16. Which shortcut shows the desktop immediately?
    a) Alt+Tab  b) Win+D  c) Ctrl+Esc  d) Alt+F4
17. `.dll` files are:
    a) Word documents  b) Shared code libraries on Windows  c) Web pages  d) Image files
18. Which of the following is VOLATILE memory?
    a) ROM  b) SSD  c) RAM  d) HDD
19. An operating system does NOT directly manage:
    a) Process scheduling  b) Memory allocation  c) Word processing  d) File systems
20. `.csv` files are:
    a) Encrypted Excel files  b) Plain text with values separated by commas  c) Compressed archives  d) Executables
21. Which type of software is an antivirus program?
    a) Application  b) Utility  c) Gaming  d) Firmware
22. Which file type is most suitable for a document meant to look identical across devices and not easily editable?
    a) .docx  b) .txt  c) .pdf  d) .bat

---

## Answer Key — MS Office & General

1. b | 2. a | 3. c | 4. b | 5. c
6. b | 7. b | 8. b | 9. c | 10. b
11. b | 12. b | 13. b | 14. b | 15. b
16. b | 17. b | 18. c | 19. c | 20. b
21. b | 22. c
