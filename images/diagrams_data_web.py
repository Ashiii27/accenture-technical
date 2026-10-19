"""DSA, DBMS, SQL, coding and frontend diagrams (chapters 04, 05, 06, 11, 12 and 07)."""
from _svgkit import (AMBER, AMBER_L, BLUE, BLUE_L, GREEN, GREEN_L, INK, LINE, MUTED, PURPLE,
                     PURPLE_L, RED, RED_L, SLATE, SLATE_L, TEAL, TEAL_L, arrow, box, canvas,
                     elbow, line, note, tag, title, txt, tw, wrap)


# ------------------------------------------------------- 23. Big-O growth ----
def big_o_growth():
    W, H = 920, 430
    p = [title(30, 34, 'Big-O — How Fast the Work Grows With n')]
    x0, x1, y0, y1 = 70, 470, 80, 350
    p.append(line(x0, y0 - 10, x0, y1, SLATE, 1.2))
    p.append(line(x0, y1, x1 + 10, y1, SLATE, 1.2))
    p.append(note(x1 + 14, y1 + 4, 'n', size=10, fill=MUTED))
    p.append(note(20, y0 - 4, 'ops', size=10, fill=MUTED))
    ns = [1, 2, 4, 6, 8, 10, 12, 14, 16]
    xs = [x0 + i * (x1 - x0) / (len(ns) - 1) for i in range(len(ns))]

    def yv(v):
        return y1 - (min(v, 256) / 256.0) * (y1 - y0)

    import math
    curves = [
        ('O(1)', lambda n: 1, GREEN),
        ('O(log n)', lambda n: math.log2(n) if n > 1 else 0, TEAL),
        ('O(n)', lambda n: n, BLUE),
        ('O(n log n)', lambda n: n * math.log2(n) if n > 1 else 0, PURPLE),
        ('O(n²)', lambda n: n * n, RED),
    ]
    for name, fn, col in curves:
        pts = ' '.join(f'{xs[i]:.1f},{yv(fn(n)):.1f}' for i, n in enumerate(ns))
        p.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.2"/>')
    p.append(box(90, 88, 152, 108, fill='#ffffff', stroke=LINE, lw=1, rx=6))
    for i, (name, fn, col) in enumerate(curves):
        ly = 108 + i * 19
        p.append(line(100, ly - 4, 130, ly - 4, col, 2.4))
        p.append(note(138, ly, name, size=9.5, fill=col, weight='bold'))
    for n, xx in zip(ns, xs):
        p.append(note(xx - 4, y1 + 16, str(n), size=9, fill=MUTED))
    # right-hand table
    tx = 520
    p.append(note(tx, 88, 'What it means in practice', size=10.5, weight='bold'))
    heads = [('Complexity', tx, 110), ('n = 100', tx + 114, 80),
             ('Typical example', tx + 198, 190)]
    y = 98
    for lbl, hx, hw in heads:
        p.append(box(hx, y, hw, 26, label=lbl, fill=SLATE_L, stroke=SLATE, fs=9.5, weight='bold'))
    rows = [('O(1)', '1', 'array[i], hash lookup', GREEN),
            ('O(log n)', '7', 'binary search', TEAL),
            ('O(n)', '100', 'linear scan', BLUE),
            ('O(n log n)', '700', 'merge sort, heap sort', PURPLE),
            ('O(n²)', '10,000', 'bubble, selection sort', RED),
            ('O(2ⁿ)', '1.2e30', 'brute-force subsets', SLATE)]
    for i, (c, a, ex, col) in enumerate(rows):
        yy = y + 26 + i * 30
        p.append(box(tx, yy, 96, 28, fill=col + '1f', stroke=col))
        p.append(note(tx + 8, yy + 19, c, size=9.5, weight='bold', mono=True))
        for val, (hx, hw) in zip([a, ex], [(h[1], h[2]) for h in heads[1:]]):
            p.append(box(hx, yy, hw, 28, fill='#ffffff', stroke=LINE, lw=0.8, rx=3))
            p.append(note(hx + 6, yy + 19, val, size=9, mono=(val[0].isdigit())))
    p.append(wrap(tx, y + 26 + 6 * 30 + 26, 'Rules: drop constants (3n → O(n)), keep the dominant '
                                            'term (n² + n → O(n²)), and different inputs get '
                                            'different letters (O(a + b)).', size=10, maxw=380))
    p.append(wrap(30, H - 22, 'Exam favourite: a loop that halves the problem each pass is O(log n); '
                              'nested loops over the same data are O(n²); a loop whose inner work '
                              'halves each pass is O(n), not O(n log n).', size=10, maxw=860,
                   fill=MUTED))
    return canvas(W, H, p)


# ------------------------------------------- 24. Array vs linked list --------
def array_vs_linked_list():
    W, H = 800, 400
    p = [title(30, 34, 'Arrays vs Linked Lists — How Memory Is Actually Laid Out')]
    p.append(box(30, 76, 350, 30, label='ARRAY — one contiguous block', fill=BLUE_L, stroke=BLUE,
                 fs=11, weight='bold'))
    vals = [10, 20, 30, 40, 50]
    x = 40
    for i, v in enumerate(vals):
        p.append(box(x, 116, 58, 40, fill='#ffffff', stroke=BLUE))
        p.append(txt(x + 29, 142, str(v), size=12, anchor='middle', weight='bold'))
        p.append(txt(x + 29, 168, f'[{i}]', size=9, anchor='middle', fill=MUTED, mono=True))
        p.append(txt(x + 29, 182, f'{200 + i * 4}', size=8, anchor='middle', fill=SLATE, mono=True))
        x += 60
    p.append(note(40, 202, 'address: 200, 204, 208, 212, 216  (4 bytes each)', size=9, fill=MUTED,
                  mono=True))
    p.append(note(40, 222, 'Index i → address = base + i × size  ⇒  O(1) random access', size=10,
                  weight='bold'))
    p.append(box(420, 76, 350, 30, label='LINKED LIST — scattered nodes', fill=TEAL_L, stroke=TEAL,
                 fs=11, weight='bold'))
    nodes = [(440, '10', '312'), (530, '20', '188'), (620, '30', '704'), (710, '40', 'NULL')]
    prev = None
    for nx, val, nxt in nodes:
        p.append(box(nx, 116, 44, 40, fill='#ffffff', stroke=TEAL))
        p.append(txt(nx + 22, 142, val, size=12, anchor='middle', weight='bold'))
        p.append(box(nx + 44, 116, 44, 40, fill=TEAL_L, stroke=TEAL))
        p.append(txt(nx + 66, 142, nxt, size=9, anchor='middle', mono=True))
        p.append(txt(nx + 22, 168, 'data', size=8, anchor='middle', fill=MUTED))
        p.append(txt(nx + 66, 168, 'next', size=8, anchor='middle', fill=MUTED))
        if prev is not None:
            p.append(arrow(prev + 88, 136, nx, 136, TEAL, 1.4, 7))
        prev = nx
    p.append(note(440, 184, 'address', size=8, fill=SLATE))
    addrs = ['512', '308', '900', '164']
    for i, a in enumerate(addrs):
        p.append(txt(nodes[i][0] + 22, 196, a, size=8, anchor='middle', fill=SLATE, mono=True))
    p.append(note(420, 222, 'Nodes can sit anywhere — you must WALK the pointers  ⇒  O(n) access',
                   size=10, weight='bold'))
    # comparison strip
    heads = [('Operation', 30, 170), ('Array', 210, 170), ('Linked list', 390, 170),
             ('Why', 570, 210)]
    y = 246
    for lbl, hx, hw in heads:
        p.append(box(hx, y, hw, 26, label=lbl, fill=SLATE_L, stroke=SLATE, fs=10, weight='bold'))
    rows = [('Access i-th', 'O(1)', 'O(n)', 'array = arithmetic, list = walk'),
            ('Insert at front', 'O(n)', 'O(1)', 'array must shift everything right'),
            ('Insert in middle (given node)', 'O(n)', 'O(1)', 'list only relinks pointers'),
            ('Memory', 'contiguous, may waste/resize', 'extra pointer per node', 'cache locality: array wins')]
    for i, (op, arr, ll, why) in enumerate(rows):
        yy = y + 26 + i * 30
        p.append(box(30, yy, 170, 28, fill='#ffffff', stroke=LINE, lw=0.8, rx=3))
        p.append(note(38, yy + 19, op, size=9, weight='bold'))
        p.append(box(210, yy, 170, 28, fill=BLUE_L, stroke=BLUE, lw=0.8, rx=3))
        p.append(note(218, yy + 19, arr, size=9, mono=True))
        p.append(box(390, yy, 170, 28, fill=TEAL_L, stroke=TEAL, lw=0.8, rx=3))
        p.append(note(398, yy + 19, ll, size=9, mono=True))
        p.append(box(570, yy, 210, 28, fill='#ffffff', stroke=LINE, lw=0.8, rx=3))
        p.append(note(578, yy + 19, why, size=9))
    return canvas(W, H, p)


# ------------------------------------------------- 25. Linked list types -----
def linked_list_types():
    W, H = 780, 418
    p = [title(30, 34, 'Three Linked-List Flavours')]
    specs = [
        ('SINGLY LINKED LIST', BLUE, 90,
         'Each node: [ data | next ]. Traversal is one-way; the tail points to NULL.'),
        ('DOUBLY LINKED LIST', TEAL, 190,
         'Each node: [ prev | data | next ]. Walk both ways; deletion is O(1) if you have the node.'),
        ('CIRCULAR LINKED LIST', AMBER, 290,
         'Tail links back to the head — no NULL. Useful for round-robin scheduling / ring buffers.'),
    ]
    for name, col, y, desc in specs:
        p.append(box(30, y, 720, 88, fill=col + '12', stroke=col, lw=1.2, rx=6))
        p.append(note(44, y + 20, name, size=10.5, weight='bold', fill=col))
        p.append(wrap(44, y + 38, desc, size=9.5, maxw=690, fill=INK))
        x = 44
        if 'SINGLY' in name:
            for i, v in enumerate(['10', '20', '30']):
                p.append(box(x, y + 48, 34, 28, fill='#ffffff', stroke=col))
                p.append(txt(x + 17, y + 67, v, size=10, anchor='middle', weight='bold'))
                p.append(box(x + 34, y + 48, 34, 28, fill=col + '22', stroke=col))
                p.append(txt(x + 51, y + 67, '•→', size=10, anchor='middle', mono=True))
                if i < 2:
                    p.append(arrow(x + 68, y + 62, x + 78, y + 62, col, 1.3, 6))
                else:
                    p.append(arrow(x + 68, y + 62, x + 78, y + 62, col, 1.3, 6))
                    p.append(txt(x + 96, y + 67, 'NULL', size=9, mono=True, fill=MUTED))
                x += 100
        elif 'DOUBLY' in name:
            for i, v in enumerate(['10', '20', '30']):
                p.append(box(x, y + 48, 26, 28, fill=col + '22', stroke=col))
                p.append(txt(x + 13, y + 67, '←', size=10, anchor='middle', mono=True))
                p.append(box(x + 26, y + 48, 34, 28, fill='#ffffff', stroke=col))
                p.append(txt(x + 43, y + 67, v, size=10, anchor='middle', weight='bold'))
                p.append(box(x + 60, y + 48, 26, 28, fill=col + '22', stroke=col))
                p.append(txt(x + 73, y + 67, '→', size=10, anchor='middle', mono=True))
                if i < 2:
                    p.append(arrow(x + 86, y + 62, x + 96, y + 62, col, 1.3, 6))
                    p.append(arrow(x + 96, y + 70, x + 86, y + 70, col, 1.3, 6))
                x += 110
        else:
            pos = [(44, '10'), (144, '20'), (244, '30')]
            for i, (xx, v) in enumerate(pos):
                p.append(box(xx, y + 48, 34, 28, fill='#ffffff', stroke=col))
                p.append(txt(xx + 17, y + 67, v, size=10, anchor='middle', weight='bold'))
                p.append(box(xx + 34, y + 48, 34, 28, fill=col + '22', stroke=col))
                p.append(txt(xx + 51, y + 67, '•→', size=10, anchor='middle', mono=True))
                nxt = pos[(i + 1) % 3][0]
                if i < 2:
                    p.append(arrow(xx + 68, y + 62, nxt, y + 62, col, 1.3, 6))
            # tail back to head
            p.append(line(278, y + 76, 278, y + 92, col, 1.3, '4 3'))
            p.append(line(278, y + 92, 61, y + 92, col, 1.3, '4 3'))
            p.append(arrow(61, y + 92, 61, y + 78, col, 1.3, 6))
    p.append(wrap(30, 386, 'Head pointer must be updated when inserting/deleting at the front — the '
                           'classic place to lose marks (and the reason for a dummy/sentinel node).',
                   size=9.5, maxw=720, fill=MUTED))
    return canvas(W, H, p)


# ------------------------------------------------------ 26. Stack & queue ----
def stack_queue():
    W, H = 780, 380
    p = [title(30, 34, 'Stack (LIFO) vs Queue (FIFO)')]
    # stack
    p.append(box(40, 78, 320, 250, fill=BLUE_L, stroke=BLUE, lw=1.4, rx=8))
    p.append(txt(200, 100, 'STACK — Last In, First Out', size=11, anchor='middle', weight='bold',
                 fill=BLUE))
    items = ['30  ← top', '20', '10'] if False else ['30', '20', '10']
    for i, v in enumerate(items):
        y = 250 - i * 42
        p.append(box(110, y, 130, 38, fill='#ffffff', stroke=BLUE))
        p.append(txt(175, y + 25, v, size=12, anchor='middle', weight='bold'))
    p.append(note(250, 268, 'top', size=10, weight='bold', fill=BLUE))
    p.append(arrow(250, 262, 250, 252, BLUE, 1.2, 6))
    p.append(note(60, 268, 'bottom', size=9, fill=MUTED))
    p.append(box(60, 130, 90, 30, label='push()', fill='#ffffff', stroke=BLUE, fs=10))
    p.append(arrow(150, 145, 240, 145, BLUE, 1.3, 6))
    p.append(box(60, 170, 90, 30, label='pop()', fill='#ffffff', stroke=BLUE, fs=10))
    p.append(arrow(240, 185, 150, 185, BLUE, 1.3, 6))
    p.append(wrap(60, 300, 'One opening: both push and pop happen at the TOP.  Uses: undo/redo, '
                           'function call stack, expression evaluation, browser back button.',
                   size=9.5, maxw=280))
    # queue
    p.append(box(400, 78, 350, 250, fill=TEAL_L, stroke=TEAL, lw=1.4, rx=8))
    p.append(txt(575, 100, 'QUEUE — First In, First Out', size=11, anchor='middle', weight='bold',
                 fill=TEAL))
    for i, v in enumerate(['10', '20', '30']):
        p.append(box(430 + i * 62, 190, 56, 38, fill='#ffffff', stroke=TEAL))
        p.append(txt(458 + i * 62, 215, v, size=12, anchor='middle', weight='bold'))
    p.append(note(430, 182, 'front', size=9.5, weight='bold', fill=TEAL))
    p.append(note(540, 182, 'rear', size=9.5, weight='bold', fill=TEAL))
    p.append(arrow(458, 250, 458, 236, TEAL, 1.2, 6))
    p.append(txt(458, 268, 'dequeue', size=9, anchor='middle', fill=TEAL))
    p.append(arrow(600, 160, 616, 160, TEAL, 1.3, 6))
    p.append(txt(700, 164, 'enqueue', size=9, fill=TEAL))
    p.append(wrap(420, 300, 'Two ends: insert at the REAR, remove from the FRONT.  Uses: printer '
                            'queues, BFS, task scheduling, request buffering in web servers.',
                   size=9.5, maxw=320))
    p.append(box(30, 340, 720, 30, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(46, 359, 'Trap: a stack implemented with an array must check for overflow/underflow; '
                           'a naive queue wastes space — real ones are circular.', size=10))
    return canvas(W, H, p)


# ------------------------------------------------------ 27. Binary search ----
def binary_search():
    W, H = 800, 450
    p = [title(30, 34, 'Binary Search — Three Steps to Find 45 in a Sorted Array',
               sub='Each comparison throws away HALF of the remaining range → O(log n)')]
    arr = [2, 5, 8, 12, 16, 23, 38, 45, 67]
    steps = [(0, 8, 4, 'A[4] = 16 < 45  →  search RIGHT'),
             (5, 8, 6, 'A[6] = 38 < 45  →  search RIGHT'),
             (7, 8, 7, 'A[7] = 45  →  FOUND at index 7')]
    y = 96
    for i, (lo, hi, mid, msg) in enumerate(steps):
        p.append(note(30, y + 4, f'Step {i + 1}', size=10, weight='bold'))
        x = 110
        for j, v in enumerate(arr):
            inside = lo <= j <= hi
            ismid = j == mid
            col = GREEN if ismid and i == 2 else (AMBER if ismid else (BLUE if inside else SLATE))
            p.append(box(x, y - 14, 62, 38, fill=(GREEN_L if ismid and i == 2 else
                                                  (AMBER_L if ismid else
                                                   (BLUE_L if inside else '#f2f2f2'))),
                         stroke=col, lw=1.4))
            p.append(txt(x + 31, y + 12, str(v), size=12, anchor='middle', weight='bold'))
            idx_y = y - 20
            p.append(txt(x + 31, idx_y, str(j), size=8.5, anchor='middle', fill=MUTED, mono=True))
            if j == lo:
                p.append(txt(x + 31, y + 36, 'low', size=8.5, anchor='middle', fill=BLUE,
                             weight='bold'))
            if j == hi:
                p.append(txt(x + 31, y + 36, 'high', size=8.5, anchor='middle', fill=BLUE,
                             weight='bold'))
            if ismid:
                p.append(txt(x + 31, y + 50, 'mid', size=8.5, anchor='middle', fill=AMBER,
                             weight='bold'))
            x += 66
        p.append(note(30, y + 70, msg, size=9.5, fill=SLATE))
        y += 100
    p.append(box(30, y - 16, 740, 40, fill=GREEN_L, stroke=GREEN, rx=6))
    p.append(note(46, y + 2, 'Comparisons: 3 for 9 elements. For 1,000,000 elements binary search '
                             'needs ~20; a linear scan needs up to 1,000,000.', size=10))
    p.append(note(46, y + 18, 'Preconditions: SORTED data + RANDOM ACCESS (arrays yes, linked lists '
                              'no).', size=10, fill=MUTED))
    return canvas(W, H, p)


# ------------------------------------------------- 28. Sorting cheat sheet ---
def sorting_cheatsheet():
    W, H = 800, 456
    p = [title(30, 34, 'Sorting Algorithms — The Whole Cheat Sheet on One Page')]
    heads = [('Algorithm', 30, 130), ('Best', 164, 78), ('Average', 246, 88), ('Worst', 338, 88),
             ('Space', 430, 78), ('Stable?', 512, 78), ('Idea', 594, 180)]
    y = 80
    for lbl, hx, hw in heads:
        p.append(box(hx, y, hw, 28, label=lbl, fill=SLATE_L, stroke=SLATE, fs=10, weight='bold'))
    rows = [('Bubble sort', 'O(n)', 'O(n²)', 'O(n²)', 'O(1)', 'Yes', 'swap adjacent if out of order', GREEN),
            ('Selection sort', 'O(n²)', 'O(n²)', 'O(n²)', 'O(1)', 'No', 'pick the min, swap to front', GREEN),
            ('Insertion sort', 'O(n)', 'O(n²)', 'O(n²)', 'O(1)', 'Yes', 'insert into the sorted prefix', GREEN),
            ('Merge sort', 'O(n log n)', 'O(n log n)', 'O(n log n)', 'O(n)', 'Yes', 'split, sort, merge', TEAL),
            ('Quick sort', 'O(n log n)', 'O(n log n)', 'O(n²)', 'O(log n)', 'No', 'partition around a pivot', TEAL),
            ('Heap sort', 'O(n log n)', 'O(n log n)', 'O(n log n)', 'O(1)', 'No', 'build heap, extract max', TEAL),
            ('Counting sort', 'O(n + k)', 'O(n + k)', 'O(n + k)', 'O(k)', 'Yes', 'count occurrences (integers)', PURPLE)]
    for i, (name, b, a, w, sp, st, idea, col) in enumerate(rows):
        yy = y + 28 + i * 32
        p.append(box(30, yy, 130, 30, fill=col + '18', stroke=col))
        p.append(note(38, yy + 20, name, size=9.5, weight='bold'))
        for val, (hx, hw) in zip([b, a, w, sp, st, idea], [(h[1], h[2]) for h in heads[1:]]):
            p.append(box(hx, yy, hw, 30, fill='#ffffff', stroke=LINE, lw=0.8, rx=3))
            p.append(note(hx + 6, yy + 20, val, size=8.8, mono=('O(' in val)))
    y2 = y + 28 + len(rows) * 32 + 16
    p.append(box(30, y2, 740, 92, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(46, y2 + 22, 'What examiners actually ask', size=10.5, weight='bold', fill=AMBER))
    p.append(wrap(46, y2 + 42, '• Stable = equal keys keep their original order (merge, insertion, '
                               'bubble, counting are stable; quick, heap, selection are not).',
                   size=10, maxw=700))
    p.append(wrap(46, y2 + 70, '• Worst-case O(n log n) guarantees: merge sort and heap sort. Quick '
                               'sort is O(n²) on already-sorted data with a first/last pivot — and '
                               'it is the fastest in practice because of cache locality.',
                   size=10, maxw=700))
    return canvas(W, H, p)


# ---------------------------------------------------- 29. BST traversals -----
def bst_traversals():
    W, H = 800, 470
    p = [title(30, 34, 'Tree Traversals — Same Nodes, Four Different Orders',
               sub='Left subtree always comes before the right one; only the ROOT moves')]
    # nodes: (x, y, label)
    nodes = {'50': (400, 130), '30': (240, 220), '70': (560, 220), '20': (150, 310),
             '40': (330, 310), '60': (470, 310), '80': (650, 310)}
    edges = [('50', '30'), ('50', '70'), ('30', '20'), ('30', '40'), ('70', '60'), ('70', '80')]
    for a, b in edges:
        xa, ya = nodes[a]
        xb, yb = nodes[b]
        p.append(line(xa, ya + 22, xb, yb - 22, SLATE, 1.3))
    for lbl, (nx, ny) in nodes.items():
        p.append(f'<circle cx="{nx}" cy="{ny}" r="22" fill="{BLUE_L}" stroke="{BLUE}" '
                 f'stroke-width="1.6"/>')
        p.append(txt(nx, ny + 5, lbl, size=12, anchor='middle', weight='bold'))
    # results
    res = [('In-order  (left-root-right)', '20  30  40  50  60  70  80',
            'sorted output for a BST', GREEN),
           ('Pre-order  (root-left-right)', '50  30  20  40  70  60  80',
            'copy / serialize a tree', BLUE),
           ('Post-order  (left-right-root)', '20  40  30  60  80  70  50',
            'delete/free: children first', PURPLE),
           ('Level-order  (BFS + queue)', '50  30  70  20  40  60  80',
            'breadth-first, needs a QUEUE', AMBER)]
    y = 356
    for i, (name, out, use, col) in enumerate(res):
        yy = y + i * 22
        p.append(note(30, yy, name, size=9.5, weight='bold', fill=col))
        p.append(txt(330, yy, out, size=9.5, mono=True, weight='bold'))
        p.append(note(560, yy, use, size=9, fill=MUTED))
    p.append(wrap(30, H - 26, 'BST property: every value in the left subtree is smaller than the '
                              'node; every value in the right subtree is larger. Inserting sorted '
                              'data into an unbalanced BST degenerates it into a linked list (O(n) '
                              'search).', size=10, maxw=740, fill=MUTED))
    return canvas(W, H, p)


# -------------------------------------------------- 30. ER & cardinality -----
def er_cardinality():
    W, H = 800, 430
    p = [title(30, 34, 'ER Diagrams — Entities, Attributes, Relationships & Cardinality')]
    # legend
    p.append(box(30, 80, 180, 26, label='Entity', fill=TEAL_L, stroke=TEAL, fs=10.5, weight='bold'))
    p.append(box(230, 80, 180, 26, label='Relationship', fill=AMBER_L, stroke=AMBER, fs=10.5,
                 weight='bold'))
    p.append(note(430, 97, '◯  attribute   ◇  relationship   ▭  entity', size=10))
    # example
    p.append(box(60, 150, 160, 46, label='EMPLOYEE', fill=TEAL_L, stroke=TEAL, fs=11, weight='bold'))
    p.append(box(420, 150, 160, 46, label='DEPARTMENT', fill=TEAL_L, stroke=TEAL, fs=11,
                 weight='bold'))
    poly = '260,160 300,173 260,186 220,173'
    p.append(f'<polygon points="{poly}" fill="{AMBER_L}" stroke="{AMBER}" stroke-width="1.4"/>')
    p.append(txt(260, 177, 'works for', size=9, anchor='middle'))
    p.append(line(220, 173, 220, 173, SLATE, 1.4))
    p.append(line(220, 173, 220, 173, SLATE, 1.4))
    p.append(arrow(220, 173, 220, 173, SLATE, 1.4, 0))
    p.append(line(220, 173, 240, 173, SLATE, 1.4))
    p.append(line(300, 173, 420, 173, SLATE, 1.4))
    p.append(note(236, 166, 'N', size=10, weight='bold', fill=AMBER))
    p.append(note(396, 166, '1', size=10, weight='bold', fill=AMBER))
    # attributes
    attrs = [(70, 220, 'emp_id'), (140, 220, 'name'), (210, 220, 'salary')]
    for ax, ay, lbl in attrs:
        is_key = lbl == 'emp_id'
        stroke_col = PURPLE if is_key else LINE
        sw = 1.6 if is_key else 1
        dash = ' stroke-dasharray="4 3"' if is_key else ''
        rx = max(28, tw(lbl, 9) / 2 + 10)
        p.append('<ellipse cx="%.0f" cy="%d" rx="%.0f" ry="18" fill="#ffffff" stroke="%s" '
                 'stroke-width="%.1f"%s/>' % (ax + 30, ay, rx, stroke_col, sw, dash))
        p.append(txt(ax + 30, ay + 4, lbl, size=9, anchor='middle', mono=True))
        p.append(line(ax + 30, ay - 18, 140, 196, LINE, 1))
    p.append(note(70, 262, 'dashed/underlined ellipse = key attribute', size=9, fill=MUTED))
    # cardinality mini examples
    p.append(note(30, 292, 'Cardinality ratios', size=10.5, weight='bold'))
    cards = [('1 : 1', 'one employee ↔ one company car', BLUE),
             ('1 : N', 'one department ↔ many employees', TEAL),
             ('M : N', 'many employees ↔ many projects', AMBER)]
    x = 30
    for c, desc, col in cards:
        p.append(box(x, 304, 240, 70, fill=col + '12', stroke=col, rx=6))
        p.append(txt(x + 120, 326, c, size=13, anchor='middle', weight='bold', fill=col))
        p.append(wrap(x + 14, 346, desc, size=9.5, maxw=212))
        p.append(note(x + 14, 366, 'M:N needs a junction table in SQL', size=8.8, fill=MUTED)
                 if c == 'M : N' else note(x + 14, 366, 'FK sits on the "many" side', size=8.8,
                                           fill=MUTED))
        x += 250
    return canvas(W, H, p)


# --------------------------------------------------- 31. Normalization -------
def normalization_steps():
    W, H = 800, 460
    p = [title(30, 34, 'Normalization — Fixing One Anomaly at a Time (1NF → 2NF → 3NF)')]
    # UNF
    p.append(box(30, 78, 340, 150, fill=RED_L, stroke=RED, rx=6))
    p.append(note(44, 98, 'UNF — repeating groups', size=10, weight='bold', fill=RED))
    p.append(txt(44, 120, 'Order | Customer | Items', size=9.5, mono=True, weight='bold'))
    p.append(txt(44, 138, '1001 | Ravi     | Pen, Book', size=9.5, mono=True))
    p.append(txt(44, 156, '1002 | Anu      | Pen', size=9.5, mono=True))
    p.append(wrap(44, 182, 'Problem: one cell holds many values → cannot query or index an item.',
                   size=9.5, maxw=310))
    p.append(arrow(378, 152, 428, 152, RED, 1.6, 8, label='1NF', lsize=10))
    # 1NF
    p.append(box(430, 78, 340, 150, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(444, 98, '1NF — atomic values', size=10, weight='bold', fill=AMBER))
    p.append(txt(444, 120, 'Order | Customer | Item', size=9.5, mono=True, weight='bold'))
    p.append(txt(444, 138, '1001 | Ravi     | Pen', size=9.5, mono=True))
    p.append(txt(444, 156, '1001 | Ravi     | Book', size=9.5, mono=True))
    p.append(wrap(444, 182, 'Still bad: Customer depends only on Order (part of the key) → partial '
                            'dependency.', size=9.5, maxw=310))
    p.append(arrow(378, 216, 428, 240, RED, 1.6, 8))
    # 2NF
    p.append(box(30, 250, 340, 130, fill=BLUE_L, stroke=BLUE, rx=6))
    p.append(note(44, 270, '2NF — no partial dependencies', size=10, weight='bold', fill=BLUE))
    p.append(txt(44, 292, 'Orders:  Order | Customer', size=9.5, mono=True, weight='bold'))
    p.append(txt(44, 310, '1001   | Ravi', size=9.5, mono=True))
    p.append(txt(44, 328, 'Items:   Order | Item', size=9.5, mono=True, weight='bold'))
    p.append(txt(44, 346, '1001   | Pen', size=9.5, mono=True))
    # 3NF
    p.append(box(430, 250, 340, 130, fill=GREEN_L, stroke=GREEN, rx=6))
    p.append(note(444, 270, '3NF — no transitive dependencies', size=10, weight='bold', fill=GREEN))
    p.append(txt(444, 292, 'Orders:  Order | CustID', size=9.5, mono=True, weight='bold'))
    p.append(txt(444, 310, 'Customers: CustID | City', size=9.5, mono=True, weight='bold'))
    p.append(wrap(444, 336, 'City depended on Customer, not on the order key — move it out.',
                   size=9.5, maxw=310))
    p.append(arrow(378, 316, 428, 316, GREEN, 1.6, 8, label='3NF', lsize=10))
    p.append(wrap(30, 404, '1NF = atomic cells.  2NF = 1NF + every non-key attribute depends on the '
                           'WHOLE key.  3NF = 2NF + no non-key attribute depends on another non-key '
                           'attribute.  BCNF = every determinant is a candidate key.',
                   size=10, maxw=740))
    p.append(wrap(30, 434, 'Why bother? Normalization kills the insert / update / delete anomalies '
                           '(e.g. changing a customer city in one row but not another).',
                   size=9.5, maxw=740, fill=MUTED))
    return canvas(W, H, p)


# ------------------------------------------------------ 32. Keys hierarchy ---
def keys_hierarchy():
    W, H = 780, 400
    p = [title(30, 34, 'DBMS Keys — How They Nest Inside Each Other')]
    cx, cy = 220, 200
    p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="170" ry="130" fill="{SLATE_L}" stroke="{SLATE}"/>')
    p.append(note(cx - 152, cy - 104, 'SUPERKEY', size=10.5, weight='bold'))
    p.append(note(cx - 152, cy - 88, 'any set of columns that uniquely identifies a row',
                  size=9))
    p.append(f'<ellipse cx="{cx}" cy="{cy + 16}" rx="130" ry="92" fill="{BLUE_L}" stroke="{BLUE}"/>')
    p.append(note(cx - 116, cy - 60, 'CANDIDATE KEY', size=10.5, weight='bold', fill=BLUE))
    p.append(note(cx - 116, cy - 44, 'minimal superkey — no subset of it is unique', size=9))
    p.append(f'<ellipse cx="{cx}" cy="{cy + 36}" rx="88" ry="56" fill="{TEAL_L}" stroke="{TEAL}"/>')
    p.append(txt(cx, cy + 28, 'PRIMARY KEY', size=10, anchor='middle', weight='bold', fill=TEAL))
    p.append(txt(cx, cy + 44, 'the one you chose', size=9, anchor='middle'))
    p.append(txt(cx, cy + 58, 'NOT NULL + UNIQUE', size=9, anchor='middle', mono=True))
    # side notes
    notes = [('ALTERNATE KEY', 'candidate keys not chosen as PK', PURPLE),
             ('COMPOSITE KEY', 'two or more columns together', AMBER),
             ('SURROGATE KEY', 'artificial id (auto-increment)', SLATE)]
    y = 120
    for name, desc, col in notes:
        p.append(box(470, y, 280, 44, fill=col + '14', stroke=col, rx=6))
        p.append(note(486, y + 20, name, size=10, weight='bold', fill=col))
        p.append(note(486, y + 36, desc, size=9.5))
        y += 58
    # FK panel
    p.append(box(30, 320, 720, 66, fill=GREEN_L, stroke=GREEN, rx=6))
    p.append(note(46, 340, 'FOREIGN KEY', size=10.5, weight='bold', fill=GREEN))
    p.append(wrap(46, 358, 'A column (or set) in the CHILD table that points at the PRIMARY KEY '
                           'of the PARENT table.', size=10, maxw=690))
    p.append(wrap(46, 376, 'employees.dept_id → departments.dept_id. NULL is allowed when the '
                           'column is nullable, but any non-NULL value MUST exist in the parent.',
                   size=9.5, fill=MUTED, maxw=690))
    return canvas(W, H, p)


# -------------------------------------------------------- 33. SQL JOINs ------
def sql_joins_venn():
    W, H = 820, 512
    p = [title(30, 34, 'SQL JOINs — Venn View + What Actually Comes Back',
               sub='A = left table (employees)   •   B = right table (departments)')]
    panels = [
        ('INNER JOIN', 'int', 'Only rows that match in BOTH tables.', BLUE,
         'SELECT ... FROM employees e\nINNER JOIN departments d ON e.dept_id = d.dept_id'),
        ('LEFT JOIN', 'left', 'All of A; NULLs where B has no match.', TEAL,
         'SELECT ... FROM employees e\nLEFT JOIN departments d ON e.dept_id = d.dept_id'),
        ('RIGHT JOIN', 'right', 'All of B; NULLs where A has no match.', AMBER,
         'SELECT ... FROM employees e\nRIGHT JOIN departments d ON e.dept_id = d.dept_id'),
        ('FULL OUTER JOIN', 'full', 'Everything from both sides; NULLs fill the gaps.', PURPLE,
         'SELECT ... FROM employees e\nFULL OUTER JOIN departments d ON e.dept_id = d.dept_id'),
    ]
    positions = [(30, 78), (420, 78), (30, 274), (420, 274)]
    for i, ((name, mode, desc, col, sql), (px, py)) in enumerate(zip(panels, positions)):
        p.append(box(px, py, 370, 182, fill='#fafafa', stroke=col, lw=1.2, rx=8))
        p.append(note(px + 14, py + 22, name, size=11, weight='bold', fill=col))
        cx1, cx2, cy, r = px + 84, px + 146, py + 88, 52
        cid = f'clip{i}'
        p.append(f'<defs><clipPath id="{cid}"><circle cx="{cx1}" cy="{cy}" r="{r}"/></clipPath></defs>')
        if mode == 'int':
            p.append(f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{LINE}"/>')
            p.append(f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{LINE}"/>')
            p.append(f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="{col}" fill-opacity="0.55" '
                     f'stroke="{col}" clip-path="url(#{cid})"/>')
        elif mode == 'left':
            p.append(f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="{col}" fill-opacity="0.55" '
                     f'stroke="{col}"/>')
            p.append(f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{LINE}"/>')
        elif mode == 'right':
            p.append(f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{LINE}"/>')
            p.append(f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="{col}" fill-opacity="0.55" '
                     f'stroke="{col}"/>')
        else:
            p.append(f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="{col}" fill-opacity="0.55" '
                     f'stroke="{col}"/>')
            p.append(f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="{col}" fill-opacity="0.55" '
                     f'stroke="{col}"/>')
        p.append(txt(cx1 - 22, cy + 5, 'A', size=12, anchor='middle', weight='bold'))
        p.append(txt(cx2 + 22, cy + 5, 'B', size=12, anchor='middle', weight='bold'))
        p.append(wrap(px + 212, py + 70, desc, size=9.5, maxw=148))
        for k, ln in enumerate(sql.split('\n')):
            p.append(txt(px + 14, py + 136 + k * 14, ln, size=8.4, mono=True))
    p.append(box(30, 466, 760, 34, fill=RED_L, stroke=RED, rx=6))
    p.append(note(46, 486, 'Trap: LEFT JOIN + WHERE on the RIGHT table = INNER JOIN.  '
                           'LEFT JOIN + WHERE right.key IS NULL = anti-join.', size=10,
               weight='bold', fill=RED))
    return canvas(W, H, p)


# ------------------------------------------------ 34. SQL clause order -------
def sql_clause_order():
    W, H = 790, 522
    p = [title(30, 34, 'SQL — The Order You WRITE It vs the Order the Engine RUNS It')]
    write = ['SELECT  name, COUNT(*) AS n', 'FROM  employees', 'WHERE  salary > 40000',
             'GROUP BY  dept_id', 'HAVING  COUNT(*) > 1', 'ORDER BY  n DESC', 'LIMIT  5']
    run = ['FROM  employees', 'WHERE  salary > 40000', 'GROUP BY  dept_id', 'HAVING  COUNT(*) > 1',
           'SELECT  name, COUNT(*) AS n', 'ORDER BY  n DESC', 'LIMIT  5']
    heads = [('① How you WRITE the query', 30, 330), ('② How the engine EXECUTES it', 430, 330)]
    y = 78
    for lbl, hx, hw in heads:
        p.append(box(hx, y, hw, 30, label=lbl, fill=SLATE_L, stroke=SLATE, fs=11, weight='bold'))
    colors = {'SELECT': BLUE, 'FROM': TEAL, 'WHERE': AMBER, 'GROUP BY': PURPLE, 'HAVING': RED,
              'ORDER BY': GREEN, 'LIMIT': SLATE}

    def col_of(line):
        for k, v in colors.items():
            if line.startswith(k):
                return v
        return SLATE

    for i, (lw_, lr_) in enumerate(zip(write, run)):
        yy = y + 30 + i * 42
        p.append(box(30, yy, 330, 38, fill=col_of(lw_) + '18', stroke=col_of(lw_), rx=5))
        p.append(txt(44, yy + 25, lw_, size=10.5, mono=True))
        p.append(box(430, yy, 330, 38, fill=col_of(lr_) + '18', stroke=col_of(lr_), rx=5))
        p.append(txt(444, yy + 25, lr_, size=10.5, mono=True))
        p.append(txt(392, yy + 25, str(i + 1), size=11, anchor='middle', weight='bold', fill=MUTED))
    y2 = y + 30 + 7 * 42 + 14
    p.append(box(30, y2, 730, 88, fill=GREEN_L, stroke=GREEN, rx=6))
    p.append(note(46, y2 + 22, 'Why this ordering matters in the exam', size=10.5, weight='bold',
                  fill=GREEN))
    p.append(wrap(46, y2 + 42, '• WHERE filters ROWS before grouping, so it cannot contain '
                               'aggregates (COUNT/SUM/AVG) — that is what HAVING is for.',
                   size=10, maxw=690))
    p.append(wrap(46, y2 + 60, '• You can use a SELECT alias in ORDER BY (it runs later) but NOT in '
                               'WHERE (it runs earlier) in standard SQL.', size=10, maxw=690))
    p.append(wrap(46, y2 + 78, '• COUNT(*) counts rows; COUNT(col) counts non-NULL values; '
                               'SUM of an empty set is NULL, COUNT of an empty set is 0.',
                   size=10, maxw=690))
    return canvas(W, H, p)


# ------------------------------------------------------- 35. Indexing --------
def index_btree():
    W, H = 800, 400
    p = [title(30, 34, 'Indexes — B-Tree Lookups and Clustered vs Non-Clustered')]
    p.append(box(30, 78, 360, 150, fill='#fafafa', stroke=LINE, rx=6))
    p.append(note(46, 98, 'B-tree index on salary', size=10.5, weight='bold'))
    p.append(box(150, 112, 120, 30, label='root: [ 30 | 60 ]', fill=BLUE_L, stroke=BLUE, fs=9.5,
                 mono=False))
    p.append(arrow(180, 142, 90, 168, SLATE, 1.2, 6))
    p.append(arrow(210, 142, 210, 168, SLATE, 1.2, 6))
    p.append(arrow(240, 142, 330, 168, SLATE, 1.2, 6))
    for i, lbl in enumerate(['[10 20]', '[30 40 50]', '[60 70 80]']):
        x = 50 + i * 110
        p.append(box(x, 170, 96, 30, label=lbl, fill='#ffffff', stroke=BLUE, fs=9.5, mono=True))
    p.append(line(50, 200, 356, 200, LINE, 1))
    p.append(wrap(46, 216, 'Balanced tree → lookups, ranges and sorts are O(log n) instead of a '
                           'full O(n) table scan.', size=9.5, maxw=330))
    # clustered vs non clustered
    p.append(box(410, 78, 360, 150, fill=TEAL_L, stroke=TEAL, rx=6))
    p.append(note(426, 98, 'CLUSTERED index (one per table)', size=10.5, weight='bold', fill=TEAL))
    rows = ['id 10  Ravi', 'id 20  Anu', 'id 30  Kabir']
    for i, r in enumerate(rows):
        p.append(box(426, 112 + i * 26, 250, 22, fill='#ffffff', stroke=TEAL, lw=0.8, rx=3))
        p.append(note(434, 128 + i * 26, r, size=9, mono=True))
    p.append(wrap(426, 200, 'The ROWS themselves are stored in key order — that is why there can '
                            'be only one.', size=9.5, maxw=330))
    p.append(box(410, 244, 360, 122, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(426, 264, 'NON-CLUSTERED index (many allowed)', size=10.5, weight='bold',
                  fill=AMBER))
    idx = [('Anu', 'row 2'), ('Kabir', 'row 3'), ('Ravi', 'row 1')]
    for i, (k, ptr) in enumerate(idx):
        p.append(box(426, 280 + i * 24, 120, 20, fill='#ffffff', stroke=AMBER, lw=0.8, rx=3))
        p.append(note(434, 294 + i * 24, f'{k} → {ptr}', size=9, mono=True))
    p.append(wrap(426, 356, 'A separate sorted structure that points back at the rows; the engine '
                            'does one extra lookup.', size=9.5, maxw=330))
    p.append(box(30, 244, 360, 122, fill=RED_L, stroke=RED, rx=6))
    p.append(note(46, 264, 'The trade-off examiners love', size=10.5, weight='bold', fill=RED))
    p.append(wrap(46, 284, 'Indexes speed up reads (WHERE, JOIN, ORDER BY) but slow down writes: '
                           'every INSERT/UPDATE/DELETE must also update the index.',
                   size=10, maxw=330))
    p.append(wrap(46, 330, 'They also do not help when a query must read most of the table — the '
                           'planner then prefers a full scan.', size=9.5, maxw=330, fill=MUTED))
    return canvas(W, H, p)


# ----------------------------------------------------------- 36. Kadane ------
def kadane():
    W, H = 800, 400
    p = [title(30, 34, "Kadane's Algorithm — Maximum Subarray Sum, Step by Step",
               sub='At each element: extend the old subarray, or start a new one here')]
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    meh = [-2, 1, -2, 4, 3, 5, 6, 1, 5]
    msf = [-2, 1, 1, 4, 4, 5, 6, 6, 6]
    p.append(note(30, 84, 'index', size=9, fill=MUTED))
    x = 110
    for i, v in enumerate(arr):
        best = 3 <= i <= 6
        p.append(box(x, 70, 58, 34, fill=(GREEN_L if best else '#ffffff'),
                     stroke=(GREEN if best else LINE), lw=1.3))
        p.append(txt(x + 29, 92, str(v), size=12, anchor='middle', weight='bold'))
        p.append(txt(x + 29, 64, str(i), size=8.5, anchor='middle', fill=MUTED, mono=True))
        x += 62
    rows = [('max_ending_here', meh, BLUE), ('max_so_far', msf, TEAL)]
    y = 120
    for name, vals, col in rows:
        p.append(note(30, y + 24, name, size=9.5, mono=True, weight='bold', fill=col))
        x = 110
        for i, v in enumerate(vals):
            best = 3 <= i <= 6
            p.append(box(x, y, 58, 34, fill=(col + '22' if best else '#ffffff'), stroke=col, lw=1))
            p.append(txt(x + 29, y + 22, str(v), size=11, anchor='middle', mono=True, weight='bold'))
            x += 62
        y += 42
    p.append(txt(110, 214, 'max_ending_here = max(a[i], max_ending_here + a[i])', size=9,
                  fill=MUTED, mono=True))
    p.append(txt(110, 232, 'max_so_far = max(max_so_far, max_ending_here)', size=9, fill=MUTED,
                  mono=True))
    y = 250
    p.append(box(30, y, 740, 122, fill='#fafafa', stroke=LINE, rx=6))
    p.append(note(46, y + 22, 'Why it works', size=10.5, weight='bold'))
    p.append(wrap(46, y + 42, 'Any maximum subarray ending at i either (a) is just a[i], or '
                              '(b) is the best subarray ending at i-1 plus a[i]. Keeping both '
                              'running values gives the answer in ONE pass: O(n) time, O(1) space.',
                   size=10, maxw=700))
    p.append(wrap(46, y + 82, 'Here the best window is indices 3..6 → 4 + (−1) + 2 + 1 = 6. '
                              'With all-negative input, the answer is the single largest element — '
                              'never 0 unless you decide an empty subarray is allowed.',
                   size=10, maxw=700, fill=MUTED))
    return canvas(W, H, p)


# ----------------------------------------------------- 37. Rotate array ------
def rotate_array():
    W, H = 780, 380
    p = [title(30, 34, 'Rotate an Array Right by k — The Reversal Trick (O(1) extra space)',
               sub='Example: [1,2,3,4,5,6,7], k = 3')]

    def strip(y, values, hi=None, label=''):
        x = 60
        p.append(note(30, y - 8, label, size=9.5, weight='bold'))
        for i, v in enumerate(values):
            hot = hi and i in hi
            p.append(box(x, y, 52, 38, fill=(AMBER_L if hot and hi == range(0, 3) else
                                             (TEAL_L if hot else '#ffffff')),
                         stroke=(AMBER if hot and hi == range(0, 3) else
                                 (TEAL if hot else LINE)), lw=1.3))
            p.append(txt(x + 26, y + 25, str(v), size=12, anchor='middle', weight='bold'))
            x += 56
    strip(84, [1, 2, 3, 4, 5, 6, 7], None, 'start   [1, 2, 3, 4, 5, 6 7]   with k = 3')
    p.append(arrow(462, 130, 462, 148, SLATE, 1.3, 7))
    strip(152, [7, 6, 5, 4, 3, 2, 1], None, '1. reverse the whole array')
    p.append(arrow(462, 198, 462, 216, SLATE, 1.3, 7))
    strip(220, [5, 6, 7, 4, 3, 2, 1], range(0, 3), '2. reverse the first k = 3')
    p.append(arrow(462, 266, 462, 284, SLATE, 1.3, 7))
    strip(296, [5, 6, 7, 1, 2, 3, 4], range(3, 7),
          '3. reverse the rest  →  [5, 6, 7, 1, 2, 3, 4]  done')
    p.append(box(470, 84, 280, 250, fill='#fafafa', stroke=LINE, rx=6))
    p.append(note(486, 104, 'Python', size=10, weight='bold'))
    code = ['def rotate(a, k):',
            '    k %= len(a)          # k may be > n',
            '    a.reverse()',
            '    a[:k] = reversed(a[:k])',
            '    a[k:] = reversed(a[k:])']
    for i, ln in enumerate(code):
        p.append(txt(486, 126 + i * 18, ln, size=9.5, mono=True))
    p.append(note(486, 236, 'Alternative: slicing', size=10, weight='bold'))
    p.append(txt(486, 258, 'a[:] = a[-k:] + a[:-k]', size=9.5, mono=True))
    p.append(wrap(486, 284, 'Left rotation is the mirror image: reverse the first k, then the rest, '
                            'then everything.', size=9.5, maxw=250))
    return canvas(W, H, p)


# --------------------------------------------------- 38. CSS box model -------
def css_box_model_full():
    W, H = 800, 470
    p = [title(30, 34, 'The CSS Box Model — Four Layers and the Width Maths')]
    layers = [('MARGIN', 40, 84, 700, 250, '#fef3c7', AMBER,
               'transparent space OUTSIDE the border — margin does NOT count in the width'),
              ('BORDER', 90, 124, 600, 170, '#fde68a', AMBER,
               'border: 5px solid  →  adds 2 × 5 = 10px'),
              ('PADDING', 140, 160, 500, 98, '#bfdbfe', BLUE,
               'padding: 20px  →  adds 2 × 20 = 40px, inside the border'),
              ('CONTENT', 230, 194, 320, 44, '#93c5fd', BLUE, 'the text / image itself')]
    for name, x, y, w, h, fill, stroke, desc in layers:
        p.append(box(x, y, w, h, fill=fill, stroke=stroke, lw=1.4, rx=4))
        p.append(note(x + 8, y + 18, name, size=10, weight='bold', fill=stroke))
        if name == 'CONTENT':
            p.append(note(x + 8, y + h - 9, desc, size=9, fill=SLATE))
        else:
            p.append(note(x + 8, y + h - 9, desc, size=9, fill=SLATE))
    # width maths
    y = 352
    p.append(box(30, y, 380, 90, fill=RED_L, stroke=RED, rx=6))
    p.append(note(46, y + 22, 'box-sizing: content-box  (DEFAULT)', size=10, weight='bold', fill=RED))
    p.append(note(46, y + 42, 'total width = 200 + 40 + 10 = 250px', size=10, mono=True))
    p.append(note(46, y + 60, 'the declared width is only the CONTENT', size=9.5, fill=MUTED))
    p.append(box(430, y, 340, 90, fill=GREEN_L, stroke=GREEN, rx=6))
    p.append(note(446, y + 22, 'box-sizing: border-box', size=10, weight='bold', fill=GREEN))
    p.append(note(446, y + 42, 'content = 200 − 40 − 10 = 150px', size=10, mono=True))
    p.append(note(446, y + 60, 'width INCLUDES padding + border', size=9.5, fill=MUTED))
    p.append(wrap(30, H - 18, 'Centering: margin: 0 auto; + a fixed width centers a block element '
                              'horizontally; flexbox (justify-content / align-items) centers both '
                              'ways. text-align: center only centers inline content.',
                   size=9.5, maxw=740, fill=MUTED))
    return canvas(W, H, p)


# -------------------------------------------------------- 39. DOM tree -------
def dom_tree():
    W, H = 800, 430
    p = [title(30, 34, 'The DOM — How the Browser Sees Your HTML',
               sub='A tree of nodes you can find, read and change with JavaScript')]
    # html snippet
    p.append(box(30, 78, 300, 190, fill=SLATE_L, stroke=SLATE, rx=6))
    p.append(note(44, 98, 'index.html', size=10, weight='bold'))
    code = ['<html>', '  <body>', '    <h1 id="title">Hi</h1>', '    <p class="msg">Text</p>',
            '    <button id="btn">Click</button>', '  </body>', '</html>']
    for i, ln in enumerate(code):
        p.append(txt(44, 122 + i * 19, ln, size=9.5, mono=True))
    p.append(arrow(340, 170, 400, 170, SLATE, 1.6, 8, label='parsed into', lsize=9.5))
    # tree
    tree = [('document', 470, 100, SLATE), ('<html>', 470, 150, BLUE),
            ('<head>', 380, 210, TEAL), ('<body>', 600, 210, TEAL),
            ('<h1 id="title">', 480, 270, AMBER), ('<p class="msg">', 610, 270, AMBER),
            ('<button id="btn">', 740, 270, AMBER)]
    edges = [(0, 1), (1, 2), (1, 3), (3, 4), (3, 5), (3, 6)]
    for a, b in edges:
        xa, ya = tree[a][1], tree[a][2]
        xb, yb = tree[b][1], tree[b][2]
        p.append(elbow(xa, ya + 18, xb, yb - 18, SLATE, 1.2, 6, axis='v'))
    for lbl, tx, ty, col in tree:
        w = max(60, tw(lbl, 9.5, mono=True) + 18)
        p.append(box(tx - w / 2, ty, w, 34, fill=col + '1e', stroke=col))
        p.append(txt(tx, ty + 22, lbl, size=9.5, anchor='middle', mono=True, weight='bold'))
    # js panel
    p.append(box(30, 300, 740, 112, fill=GREEN_L, stroke=GREEN, rx=6))
    p.append(note(46, 322, 'The five DOM moves you must know for the coding round', size=10.5,
                  weight='bold', fill=GREEN))
    moves = [("document.getElementById('btn')", 'find ONE element by id'),
             ("document.querySelector('.msg')", 'first match for ANY CSS selector'),
             ("document.querySelectorAll('.msg')", 'ALL matches (NodeList — has forEach)'),
             ("el.textContent = 'New text'", 'change the visible text (safe)'),
             ("el.addEventListener('click', fn)", 'run fn when the element is clicked'),
             ("el.classList.toggle('active')", 'add/remove a CSS class')]
    for i, (code_, desc) in enumerate(moves):
        xx = 46 + (i % 3) * 250
        yy = 344 + (i // 3) * 30
        p.append(txt(xx, yy, code_, size=9, mono=True, weight='bold'))
        p.append(txt(xx, yy + 13, desc, size=8.8, fill=MUTED))
    return canvas(W, H, p)


# ------------------------------------------------- 40. CSS specificity -------
def css_specificity():
    W, H = 800, 428
    p = [title(30, 34, 'CSS Specificity — Which Rule Actually Wins',
               sub='Score = (inline, IDs, classes/attributes/pseudo-classes, elements)')]
    heads = [('Selector', 30, 250), ('Score', 290, 130), ('Wins over', 430, 340)]
    y = 82
    for lbl, hx, hw in heads:
        p.append(box(hx, y, hw, 28, label=lbl, fill=SLATE_L, stroke=SLATE, fs=10, weight='bold'))
    rows = [('p', '0-0-0-1', 'nothing (weakest)', SLATE),
            ('.note p', '0-0-1-1', 'p', SLATE),
            ('#main p', '0-1-0-1', '.note p  (IDs beat any number of classes)', BLUE),
            ('#main .note p:hover', '0-1-2-1', '#main p', BLUE),
            ('style="..." (inline)', '1-0-0-0', 'everything except !important', PURPLE),
            ('!important', '∞', 'everything (avoid it)', RED)]
    for i, (sel, score, beats, col) in enumerate(rows):
        yy = y + 28 + i * 32
        p.append(box(30, yy, 250, 30, fill=col + '14', stroke=col))
        p.append(note(38, yy + 20, sel, size=9.5, mono=True, weight='bold'))
        p.append(box(290, yy, 130, 30, fill='#ffffff', stroke=LINE, lw=0.8, rx=3))
        p.append(note(298, yy + 20, score, size=9.5, mono=True))
        p.append(box(430, yy, 340, 30, fill='#ffffff', stroke=LINE, lw=0.8, rx=3))
        p.append(note(438, yy + 20, beats, size=9.5))
    y2 = y + 28 + 6 * 32 + 14
    p.append(box(30, y2, 740, 94, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(46, y2 + 22, 'Worked example', size=10.5, weight='bold', fill=AMBER))
    p.append(txt(46, y2 + 42, 'p { color: green }  →  0-0-0-1', size=9.5, mono=True))
    p.append(txt(340, y2 + 42, '.content p { color: blue }  →  0-0-1-1', size=9.5, mono=True))
    p.append(txt(46, y2 + 62, '#main p { color: red }  →  0-1-0-1   WINS', size=9.5, mono=True,
                 weight='bold'))
    p.append(note(46, y2 + 82, 'Compare left to right: the first position that differs decides. '
                               'If two rules tie, the LAST one in the source wins.', size=10,
               fill=MUTED))
    return canvas(W, H, p)


# ---------------------------------------------------- 41. Practice schema ----
def practice_schema():
    W, H = 820, 470
    p = [title(30, 34, 'Chapter 12 Practice Schema — Four Tables, Three Relationships',
               sub='Every SQL question in chapter 12 uses this schema')]
    tables = [
        ('departments', 30, 86, [('PK', 'dept_id'), ('', 'dept_name'), ('', 'location')], TEAL),
        ('employees', 30, 236, [('PK', 'emp_id'), ('', 'name'), ('FK', 'dept_id'), ('', 'salary'),
                                ('', 'hire_date'), ('FK', 'manager_id')], BLUE),
        ('projects', 470, 86, [('PK', 'project_id'), ('', 'project_name'), ('FK', 'dept_id'),
                               ('', 'budget')], AMBER),
        ('employee_projects', 470, 236, [('FK', 'emp_id'), ('FK', 'project_id'),
                                         ('', 'hours_worked')], PURPLE),
    ]
    boxes = {}
    for name, x, y, cols, col in tables:
        h = 26 + len(cols) * 24
        boxes[name] = (x, y, 250, h)
        p.append(box(x, y, 250, h, fill=col + '12', stroke=col, lw=1.4))
        p.append(box(x, y, 250, 26, fill=col, stroke=col))
        p.append(txt(x + 125, y + 18, name, size=10.5, anchor='middle', weight='bold',
                     fill='#ffffff'))
        for i, (kind, cname) in enumerate(cols):
            yy = y + 26 + i * 24
            p.append(note(x + 10, yy + 17, cname, size=9.5, mono=True))
            if kind:
                p.append(tag(x + 180, yy + 3, 56, 18, kind, fill=col + '2a', stroke=col,
                             tfill=col, fs=9, mono=False))
                boxes.setdefault(name + ':' + cname, (x + 180, yy + 3))
    # relationships
    p.append(elbow(280, 140, 280, 280, TEAL, 1.5, 8, axis='h'))
    p.append(note(300, 214, 'dept_id  1 : N', size=9.5, fill=TEAL, weight='bold'))
    p.append(arrow(470, 130, 280, 130, AMBER, 1.5, 8, label='dept_id', lsize=9.5))
    p.append(arrow(470, 260, 280, 260, PURPLE, 1.5, 8, label='emp_id', lsize=9.5))
    p.append(arrow(595, 236, 595, 208, AMBER, 1.5, 8))
    p.append(note(602, 226, 'project_id', size=9.5, fill=AMBER, weight='bold'))
    p.append(box(30, 400, 760, 56, fill=RED_L, stroke=RED, rx=6))
    p.append(note(46, 420, 'Two traps in this data', size=10.5, weight='bold', fill=RED))
    p.append(note(46, 438, 'Frank (emp 6) has dept_id = NULL, and Marketing (dept 40) has no '
                           'employees — so INNER JOIN loses both while LEFT/RIGHT JOIN keep them.',
                   size=10))
    return canvas(W, H, p)


DATA_WEB = [
    ('big-o-growth', big_o_growth),
    ('array-vs-linked-list', array_vs_linked_list),
    ('linked-list-types', linked_list_types),
    ('stack-queue', stack_queue),
    ('binary-search', binary_search),
    ('sorting-cheatsheet', sorting_cheatsheet),
    ('bst-traversals', bst_traversals),
    ('er-cardinality', er_cardinality),
    ('normalization-steps', normalization_steps),
    ('keys-hierarchy', keys_hierarchy),
    ('sql-joins-venn', sql_joins_venn),
    ('sql-clause-order', sql_clause_order),
    ('index-btree', index_btree),
    ('kadane', kadane),
    ('rotate-array', rotate_array),
    ('css-box-model', css_box_model_full),
    ('dom-tree', dom_tree),
    ('css-specificity', css_specificity),
    ('practice-schema', practice_schema),
]
