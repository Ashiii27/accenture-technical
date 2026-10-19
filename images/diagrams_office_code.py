"""MS Office and pseudocode diagrams (chapters 02, 03 and 07)."""
from _svgkit import (AMBER, AMBER_L, BLUE, BLUE_L, GREEN, GREEN_L, INK, LINE, MUTED, PURPLE,
                     PURPLE_L, RED, RED_L, SLATE, SLATE_L, TEAL, TEAL_L, arrow, box, canvas,
                     line, note, title, txt, tw, wrap)


def _diamond(cx, cy, w, h, label, fill='#ffffff', stroke=SLATE, fs=9.5):
    pts = f'{cx:.1f},{cy - h/2:.1f} {cx + w/2:.1f},{cy:.1f} ' \
          f'{cx:.1f},{cy + h/2:.1f} {cx - w/2:.1f},{cy:.1f}'
    return ('<polygon points="%s" fill="%s" stroke="%s" stroke-width="1.2"/>' % (pts, fill, stroke)
            + '\n' + txt(cx, cy + fs * 0.35, label, size=fs, anchor='middle'))


# ------------------------------------------------- 15. Excel references ------
def excel_references():
    W, H = 760, 420
    p = [title(30, 34, 'Excel Cell References — What Happens When You Copy a Formula',
               sub='Formula typed in B2, then copied to C3 (one column right, one row down)')]
    heads = [('Reference type', 30, 180), ('Written in B2', 220, 130), ('After copy to C3', 360, 170),
             ('What is locked?', 540, 200)]
    y = 84
    for lbl, hx, hw in heads:
        p.append(box(hx, y, hw, 30, label=lbl, fill=SLATE_L, stroke=SLATE, fs=10.5, weight='bold'))
    rows = [
        ('Relative', '=A1', '=B2', 'nothing — both move', BLUE_L, BLUE),
        ('Absolute', '=$A$1', '=$A$1', 'column AND row', TEAL_L, TEAL),
        ('Mixed (col locked)', '=$A1', '=$A2', 'column only — row moves', AMBER_L, AMBER),
        ('Mixed (row locked)', '=A$1', '=B$1', 'row only — column moves', PURPLE_L, PURPLE),
    ]
    for i, (name, src, dst, locked, fill, stroke) in enumerate(rows):
        yy = y + 30 + i * 40
        p.append(box(30, yy, 180, 36, fill=fill, stroke=stroke))
        p.append(note(40, yy + 23, name, size=10.5, weight='bold'))
        p.append(box(220, yy, 130, 36, fill='#ffffff', stroke=LINE, lw=1, rx=4))
        p.append(txt(240, yy + 24, src, size=11.5, mono=True, weight='bold'))
        p.append(arrow(356, yy + 18, 400, yy + 18, stroke, 1.4, 6))
        p.append(box(400, yy, 130, 36, fill='#ffffff', stroke=LINE, lw=1, rx=4))
        p.append(txt(420, yy + 24, dst, size=11.5, mono=True, weight='bold'))
        p.append(box(540, yy, 200, 36, fill='#ffffff', stroke=LINE, lw=1, rx=4))
        p.append(note(550, yy + 23, locked, size=10))
    y2 = y + 30 + 4 * 40 + 18
    p.append(box(30, y2, 700, 74, fill=BLUE_L, stroke=BLUE, rx=6))
    p.append(wrap(46, y2 + 22, 'Rule: the $ sits in FRONT of the part you want to freeze — '
                               '$A1 freezes the column, A$1 freezes the row, $A$1 freezes both.',
                   size=10.5, weight='bold', maxw=660))
    p.append(note(46, y2 + 62, 'F4 cycles A1 → $A$1 → A$1 → $A1 → A1. Copy across copies the column '
                               'letter; copy down copies the row number.', size=10))
    y3 = y2 + 66
    p.append(box(30, y3, 700, 50, fill=RED_L, stroke=RED, rx=6))
    p.append(note(46, y3 + 20, 'Exam trap', size=10.5, weight='bold', fill=RED))
    p.append(wrap(46, y3 + 38, '=$A4+B$2 in C4 copied to D5 becomes =$A5+C$2 — the column-absolute '
                               'part keeps its letter, the row-absolute part keeps its number.',
                   size=10, maxw=660))
    return canvas(W, H, p)


# ------------------------------------------------------ 16. VLOOKUP ----------
def vlookup_anatomy():
    W, H = 770, 510
    p = [title(30, 34, 'VLOOKUP — Argument by Argument (and the #N/A traps)')]
    # table
    p.append(note(30, 74, 'Lookup table A2:C6', size=10.5, weight='bold'))
    data = [('', 'A', 'B', 'C'), ('1', 'EmpID', 'Name', 'Salary'),
            ('2', '101', 'Amit', '50000'), ('3', '102', 'Bala', '70000'),
            ('4', '103', 'Chitra', '60000')]
    y = 82
    for i, row in enumerate(data):
        x = 30
        for j, cell in enumerate(row):
            w = 34 if j == 0 else 120
            is_head = i == 1
            p.append(box(x, y, w, 26, fill=SLATE_L if is_head else '#ffffff', stroke=LINE, lw=0.9,
                         rx=2))
            p.append(txt(x + 8, y + 18, cell, size=10, mono=True,
                         weight='bold' if is_head else 'normal'))
            x += w
        y += 26
    # formula
    fy = y + 26
    p.append(txt(30, fy + 14, '=VLOOKUP( 102 , A2:C6 , 3 , FALSE )', size=15, mono=True,
                 weight='bold'))
    parts = [(148, 'lookup_value', 'What you are looking for (102)', BLUE),
             (232, 'table_array', 'Whole table; the key MUST be the LEFTMOST column', TEAL),
             (322, 'col_index_num', 'Which column to return (3 = Salary)', AMBER),
             (400, 'range_lookup', 'FALSE = exact • TRUE/omitted = approximate', RED)]
    for x, name, desc, col in parts:
        p.append(arrow(x, fy - 2, x, fy - 16, col, 1.2, 5))
        p.append(txt(x, fy - 22, name, size=9.5, anchor='middle', mono=True, weight='bold',
                     fill=col))
    yy = fy + 44
    for x, name, desc, col in parts:
        p.append(note(30, yy, '•', size=10, fill=col))
        p.append(wrap(46, yy, f'{name}: {desc}', size=10, maxw=700))
        yy += 28
    # traps
    p.append(box(30, yy + 6, 710, 122, fill=RED_L, stroke=RED, rx=6))
    p.append(note(46, yy + 26, 'Traps that cost marks', size=10.5, weight='bold', fill=RED))
    p.append(wrap(46, yy + 46, '1. TRUE (or omitted) needs the first column sorted ASCENDING — '
                               'otherwise you silently get a wrong row, not an error.',
                   size=10, maxw=670))
    p.append(wrap(46, yy + 64, '2. col_index counts from the left edge of table_array, NOT from '
                               'column A.', size=10, maxw=670))
    p.append(wrap(46, yy + 84, '3. VLOOKUP cannot look LEFT — use INDEX + MATCH for that.',
                   size=10, maxw=670))
    p.append(wrap(46, yy + 104, '4. Wrap it: =IFERROR(VLOOKUP(...), "Not Found") turns #N/A into '
                                'something readable.', size=10, maxw=670))
    return canvas(W, H, p)


# ------------------------------------------------- 17. PowerPoint master -----
def ppt_master():
    W, H = 740, 330
    p = [title(30, 34, 'PowerPoint — Slide Master → Layouts → Slides',
               sub='Edit the master once; every slide using that layout updates')]
    p.append(box(250, 84, 240, 46, label='SLIDE MASTER (theme, logo, fonts)', fill=PURPLE_L,
                 stroke=PURPLE, fs=11, weight='bold'))
    layouts = ['Title Slide', 'Title + Content', 'Two Content']
    x = 70
    lys = []
    for i, l in enumerate(layouts):
        lys.append(x)
        p.append(box(x, 158, 180, 38, label=l, fill=BLUE_L, stroke=BLUE, fs=10.5))
        p.append(arrow(370, 130, x + 90, 158, SLATE, 1.3, 6))
        x += 215
    for i, lx in enumerate(lys):
        for k in range(2):
            p.append(box(lx + 10 + k * 84, 220, 72, 44, fill='#ffffff', stroke=LINE, lw=1, rx=4))
            p.append(txt(lx + 46 + k * 84, 248, f'Slide {i*2 + k + 1}', size=9, anchor='middle'))
        p.append(arrow(lx + 90, 196, lx + 90, 220, SLATE, 1.2, 5))
    p.append(box(30, 282, 680, 40, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(wrap(46, 300, 'Logo must be hidden on the title slide? Select that slide → Format '
                           'Background → Hide Background Graphics (keeps the design, drops the '
                           'master artwork).', size=10, maxw=660))
    return canvas(W, H, p)


# --------------------------------------------------- 18. Loop flowcharts -----
def loop_flowcharts():
    W, H = 800, 476
    p = [title(30, 34, 'FOR vs WHILE vs DO-WHILE — How Many Times Does the Body Run?')]
    panels = [('FOR', 30, BLUE), ('WHILE', 285, TEAL), ('REPEAT / DO-WHILE', 540, AMBER)]
    code = {
        'FOR': 'FOR i = 1 TO 5\n    body\nEND FOR',
        'WHILE': 'WHILE cond\n    body\nEND WHILE',
        'REPEAT / DO-WHILE': 'REPEAT\n    body\nUNTIL cond',
    }
    for name, x, col in panels:
        p.append(box(x, 74, 230, 366, fill='#fafafa', stroke=col, lw=1.3, rx=8))
        p.append(box(x + 60, 84, 110, 26, label=name, fill=col + '22', stroke=col, fs=11,
                     weight='bold'))
        cy = 126
        p.append(box(x + 60, cy, 110, 28, label='start', fill='#ffffff', stroke=col, fs=10, rx=14))
        if name == 'FOR':
            p.append(box(x + 50, cy + 40, 130, 30, label='i = 1 (init once)', fill='#ffffff',
                         stroke=col, fs=9.5))
            p.append(_diamond(x + 115, cy + 100, 130, 44, 'i <= 5 ?', '#ffffff', col))
            p.append(box(x + 50, cy + 140, 130, 30, label='body', fill=col + '22', stroke=col,
                         fs=10))
            p.append(box(x + 50, cy + 192, 130, 30, label='i = i + 1', fill='#ffffff', stroke=col,
                         fs=10))
        elif name == 'WHILE':
            p.append(_diamond(x + 115, cy + 48, 140, 44, 'condition?', '#ffffff', col))
            p.append(box(x + 50, cy + 92, 130, 30, label='body', fill=col + '22', stroke=col,
                         fs=10))
        else:
            p.append(box(x + 50, cy + 40, 130, 30, label='body', fill=col + '22', stroke=col,
                         fs=10))
            p.append(_diamond(x + 115, cy + 108, 140, 44, 'until true?', '#ffffff', col))
        p.append(box(x + 60, cy + 240, 110, 26, label='done', fill='#ffffff', stroke=col, fs=10,
                     rx=13))
        p.append(note(x + 12, cy + 282, 'Body runs', size=9.5, weight='bold'))
    p.append(note(42, 428, 'known number of iterations', size=9))
    p.append(note(42, 442, '(exactly n times)', size=9))
    p.append(note(297, 428, '0 or more times — the', size=9))
    p.append(note(297, 442, 'condition is checked FIRST', size=9))
    p.append(note(552, 428, '1 or more times — the', size=9))
    p.append(note(552, 442, 'condition is checked AFTER', size=9))
    return canvas(W, H, p)


# -------------------------------------------------- 19. Recursion tree -------
def recursion_tree():
    W, H = 780, 448
    p = [title(30, 34, 'Recursion — Call Tree and Unwinding (factorial 4)',
               sub='Two phases: wind down to the base case, then unwind back up returning values')]
    # tree rows
    rows = [
        ('fact(4)', '4 * fact(3)', 80),
        ('fact(3)', '3 * fact(2)', 140),
        ('fact(2)', '2 * fact(1)', 200),
        ('fact(1)', 'BASE CASE → return 1', 260),
    ]
    for i, (label, action, y) in enumerate(rows):
        x = 40 + i * 60
        base = 'BASE' in action
        p.append(box(x, y, 110, 42, fill=GREEN_L if base else BLUE_L,
                     stroke=GREEN if base else BLUE))
        p.append(txt(x + 55, y + 19, label, size=10.5, anchor='middle', weight='bold'))
        p.append(txt(x + 55, y + 34, action, size=9, anchor='middle', mono=True))
        if i < len(rows) - 1:
            p.append(arrow(x + 30, y + 42, x + 70, y + 60, SLATE, 1.3, 6,
                           label='call', lsize=8.5))
    # unwinding
    y = 330
    p.append(note(40, y - 16, 'Unwinding — return values bubble back up', size=10.5, weight='bold',
                  fill=GREEN))
    vals = [('fact(1) = 1', BLUE), ('fact(2) = 2 × 1 = 2', BLUE), ('fact(3) = 3 × 2 = 6', BLUE),
            ('fact(4) = 4 × 6 = 24', GREEN)]
    x = 40
    for lab, col in vals:
        p.append(box(x, y, 160, 38, fill=col + '18' if col != GREEN else GREEN_L, stroke=col))
        p.append(txt(x + 80, y + 24, lab, size=10, anchor='middle', mono=True, weight='bold'))
        if x < 600:
            p.append(arrow(x + 160, y + 19, x + 186, y + 19, GREEN, 1.4, 6))
        x += 186
    # stack panel
    p.append(box(500, 84, 250, 176, fill='#fafafa', stroke=LINE, rx=6))
    p.append(note(516, 104, 'Call stack at the deepest point', size=10, weight='bold'))
    stack = ['fact(1)  ← executing', 'fact(2)', 'fact(3)', 'fact(4)', 'main()']
    for i, s in enumerate(stack):
        yy = 220 - i * 26
        p.append(box(516, yy, 218, 22, fill=GREEN_L if i == 0 else '#ffffff', stroke=LINE, lw=0.9,
                     rx=3))
        p.append(note(524, yy + 15, s, size=9.5, mono=True))
    p.append(note(516, 246, 'Stack is LIFO — the last call finishes first.', size=9, fill=MUTED))
    p.append(wrap(40, 400, 'Always ask: (1) what is the base case? (2) does every recursive call move '
                           'closer to it? (3) what does each frame return? No base case = stack '
                           'overflow.', size=10, maxw=700, fill=MUTED))
    return canvas(W, H, p)


# ------------------------------------------ 20. Pass by value vs reference ---
def pass_by_value_reference():
    W, H = 780, 400
    p = [title(30, 34, 'Pass by Value vs Pass by Reference — What the Callee Can Change')]
    # left: by value
    p.append(box(30, 78, 350, 250, fill=BLUE_L, stroke=BLUE, lw=1.4, rx=8))
    p.append(txt(205, 102, 'PASS BY VALUE', size=12, anchor='middle', weight='bold', fill=BLUE))
    p.append(note(50, 126, 'main():  x = 5', size=10.5, mono=True))
    p.append(box(50, 138, 120, 44, fill='#ffffff', stroke=BLUE))
    p.append(txt(110, 156, 'x', size=11, anchor='middle', weight='bold', mono=True))
    p.append(txt(110, 172, '5', size=11, anchor='middle', mono=True))
    p.append(arrow(170, 160, 250, 160, BLUE, 1.4, 7, label='copy of the value', lsize=9))
    p.append(box(250, 138, 110, 44, fill='#ffffff', stroke=BLUE, dashed=True))
    p.append(txt(305, 156, 'param a', size=10, anchor='middle', weight='bold', mono=True))
    p.append(txt(305, 172, '5 → 15', size=10, anchor='middle', mono=True))
    p.append(wrap(50, 208, 'Inside the function a = a + 10 changes only the COPY. Back in main, x is '
                           'still 5.', size=10, maxw=310))
    p.append(note(50, 306, 'Result: PRINT x  →  5', size=11, weight='bold', mono=True, fill=BLUE))
    # right: by reference
    p.append(box(400, 78, 350, 250, fill=TEAL_L, stroke=TEAL, lw=1.4, rx=8))
    p.append(txt(575, 102, 'PASS BY REFERENCE', size=12, anchor='middle', weight='bold', fill=TEAL))
    p.append(note(420, 126, 'main():  y = 5', size=10.5, mono=True))
    p.append(box(420, 138, 120, 44, fill='#ffffff', stroke=TEAL))
    p.append(txt(480, 156, 'y', size=11, anchor='middle', weight='bold', mono=True))
    p.append(txt(480, 172, '5 → 15', size=10, anchor='middle', mono=True))
    p.append(arrow(540, 160, 620, 160, TEAL, 1.4, 7, label='same memory', lsize=9))
    p.append(box(620, 138, 110, 44, fill='#ffffff', stroke=TEAL, dashed=True))
    p.append(txt(675, 156, 'param b', size=10, anchor='middle', weight='bold', mono=True))
    p.append(txt(675, 172, 'alias of y', size=9, anchor='middle', mono=True))
    p.append(wrap(420, 208, 'The parameter is another name for the SAME box. b = b + 10 writes '
                            'straight into the caller variable.', size=10, maxw=310))
    p.append(note(420, 306, 'Result: PRINT y  →  15', size=11, weight='bold', mono=True, fill=TEAL))
    p.append(box(30, 342, 720, 46, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(46, 362, 'In most exam pseudocode, plain variables are passed BY VALUE and ARRAYS '
                           'are passed BY REFERENCE.', size=10.5, weight='bold'))
    p.append(note(46, 380, 'So a function that edits arr[i] does change the caller array — a '
                           'function that swaps two plain variables does nothing.', size=10))
    return canvas(W, H, p)


# ---------------------------------------------- 21. Bubble sort first pass ---
def bubble_sort_pass():
    W, H = 780, 480
    p = [title(30, 34, 'Bubble Sort — One Pass, Swap by Swap',
               sub='Each pass bubbles the largest remaining element to its final place')]
    arr = [5, 1, 4, 2, 8]
    labels = ['Pass 0 (start)', 'compare 5,1 → swap', 'compare 5,4 → swap', 'compare 5,2 → swap',
              'compare 5,8 → no swap']
    states = [[5, 1, 4, 2, 8], [1, 5, 4, 2, 8], [1, 4, 5, 2, 8], [1, 2, 5, 4, 8], [1, 2, 4, 5, 8]]
    swaps = [None, (0, 1), (1, 2), (2, 3), (3, 4)]
    y = 96
    for i, (state, lab, sw) in enumerate(zip(states, labels, swaps)):
        p.append(note(30, y + 18, lab, size=10, fill=MUTED))
        x = 210
        for j, v in enumerate(state):
            hot = sw and j in sw
            p.append(box(x, y, 60, 40, fill=(RED_L if hot else '#ffffff'),
                         stroke=(RED if hot else LINE), lw=1.4))
            p.append(txt(x + 30, y + 26, str(v), size=13, anchor='middle', weight='bold'))
            x += 66
        if sw:
            a, b = sw
            xa, xb = 210 + a * 66, 210 + b * 66
            p.append(arrow(xa + 30, y - 6, xb + 30, y - 6, RED, 1.4, 6))
            p.append(arrow(xb + 30, y + 46, xa + 30, y + 46, RED, 1.4, 6))
        y += 62
    p.append(box(30, y + 4, 720, 44, fill=GREEN_L, stroke=GREEN, rx=6))
    p.append(note(46, y + 24, 'Pass 1 result: [1, 2, 4, 5, 8] — the largest value (8) is now at the '
                              'end and never moves again.', size=10.5))
    p.append(note(46, y + 40, 'Swaps in this pass = 4. Total swaps over the whole sort = number of '
                              'INVERSIONS in the original array.', size=10, fill=MUTED))
    return canvas(W, H, p)


# ------------------------------------------------- 22. Nested loop grid ------
def nested_loop_grid():
    W, H = 720, 400
    p = [title(30, 34, 'Nested Loops — Building the (i, j) Table Instead of Guessing')]
    p.append(box(30, 74, 320, 34, fill=SLATE_L, stroke=SLATE, rx=4))
    p.append(txt(44, 96, 'FOR i = 1 TO 3', size=11, mono=True, weight='bold'))
    p.append(txt(190, 96, 'FOR j = 1 TO i', size=11, mono=True, weight='bold'))
    p.append(txt(320, 96, 'PRINT j', size=11, mono=True, weight='bold'))
    # grid
    gx, gy = 60, 130
    p.append(note(gx, gy - 8, 'j →', size=9.5, fill=MUTED))
    p.append(note(30, gy + 26, 'i', size=9.5, fill=MUTED))
    p.append(note(30, gy + 40, '↓', size=9.5, fill=MUTED))
    for jj in range(1, 4):
        p.append(box(gx + (jj - 1) * 60, gy, 58, 26, fill='#ffffff', stroke=LINE, lw=0.8, rx=3))
        p.append(txt(gx + (jj - 1) * 60 + 29, gy + 18, f'j={jj}', size=9, anchor='middle',
                     mono=True))
    for ii in range(1, 4):
        yy = gy + 26 + (ii - 1) * 30
        p.append(box(gx - 60, yy, 58, 28, fill=SLATE_L, stroke=SLATE, lw=0.8, rx=3))
        p.append(txt(gx - 31, yy + 19, f'i={ii}', size=9, anchor='middle', mono=True))
        for jj in range(1, 4):
            inside = jj <= ii
            p.append(box(gx + (jj - 1) * 60, yy, 58, 28,
                         fill=(BLUE_L if inside else '#f7f7f7'),
                         stroke=(BLUE if inside else '#e5e7eb'), lw=0.8, rx=3))
            if inside:
                p.append(txt(gx + (jj - 1) * 60 + 29, yy + 19, f'prints {jj}', size=8.5,
                             anchor='middle'))
    p.append(note(gx, gy + 26 + 3 * 30 + 22, 'Only the cells where j <= i execute — the inner loop '
                                             'runs 1 + 2 + 3 = 6 times.', size=10, fill=MUTED))
    p.append(note(gx, gy + 26 + 3 * 30 + 40, 'Output: 1   1 2   1 2 3', size=11, mono=True,
                  weight='bold'))
    # right side: counting rule
    p.append(box(400, 118, 290, 240, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(416, 140, 'Counting shortcuts', size=10.5, weight='bold', fill=AMBER))
    rules = ['FOR i = 1..n, inner j = 1..n   →  n × n',
             'FOR i = 1..n, inner j = 1..i   →  n(n+1)/2',
             'FOR i = 1..n, inner j = i..n   →  n(n+1)/2',
             'Outer halves each time, inner n →  O(n)',
             'Three nested loops of n        →  O(n³)']
    yy = 164
    for r in rules:
        p.append(wrap(416, yy, r, size=9.5, maxw=260, mono=True))
        yy += 40
    p.append(wrap(30, H - 26, 'Exam habit: write the iteration table (i, j, output) on paper. Most '
                              'wrong answers come from an off-by-one in the inner bound, not from '
                              'the maths.', size=10, maxw=680, fill=MUTED))
    return canvas(W, H, p)


OFFICE_CODE = [
    ('excel-references', excel_references),
    ('vlookup-anatomy', vlookup_anatomy),
    ('ppt-master', ppt_master),
    ('loop-flowcharts', loop_flowcharts),
    ('recursion-tree', recursion_tree),
    ('pass-by-value-reference', pass_by_value_reference),
    ('bubble-sort-pass', bubble_sort_pass),
    ('nested-loop-grid', nested_loop_grid),
]
