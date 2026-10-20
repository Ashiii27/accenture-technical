"""OS fundamentals and Java basics diagrams (chapters 15 and 16)."""
from _svgkit import (AMBER, AMBER_L, BLUE, BLUE_L, GREEN, GREEN_L, INK,
                     LINE, MUTED, PURPLE, PURPLE_L, RED, RED_L, SLATE,
                     SLATE_L, TEAL, TEAL_L, arrow, box, canvas, elbow, line,
                     note, tag, title, txt, tw, wrap)


# ------------------------------------------- 46. Process states --------
def process_states():
    W, H = 920, 380
    p = [title(30, 34, 'Process States — the 5-State Model')]
    p.append(note(30, 53, 'The OS moves every process through these states; the scheduler only picks from Ready'))

    for name, x in (('New', 60), ('Ready', 280), ('Running', 500),
                    ('Waiting', 720)):
        p.append(box(x, 130, 120, 50, label=name, fill=BLUE_L, stroke=BLUE,
                     fs=12, weight='bold'))
    p.append(box(500, 290, 120, 50, label='Terminated', fill=SLATE_L,
                 stroke=SLATE, fs=11.5, weight='bold'))

    p.append(arrow(180, 155, 280, 155, BLUE, label='admitted'))
    p.append(arrow(400, 155, 500, 155, BLUE, label='scheduler'))
    p.append(arrow(620, 155, 720, 155, BLUE, label='I/O request'))
    p.append(arrow(560, 180, 560, 290, BLUE, label='exit'))

    # Running -> Ready (preemption), routed above the boxes
    p.append(line(560, 130, 560, 70, BLUE, 1.4))
    p.append(line(560, 70, 340, 70, BLUE, 1.4))
    p.append(arrow(340, 70, 340, 130, BLUE))
    p.append(note(450, 84, 'preempted', size=9.5, fill=MUTED, anchor='middle'))

    # Waiting -> Ready (I/O complete), routed below the boxes
    p.append(line(780, 180, 780, 240, BLUE, 1.4))
    p.append(line(780, 240, 340, 240, BLUE, 1.4))
    p.append(arrow(340, 240, 340, 180, BLUE))
    p.append(note(560, 226, 'I/O complete', size=9.5, fill=MUTED,
                  anchor='middle'))

    p.append(wrap(40, 368, 'Ready \u2194 Running is the scheduler\u2019s job; '
                           'Running \u2194 Waiting is driven by I/O events. '
                           'A process only reaches Terminated from Running.',
                  size=10, maxw=850, fill=INK))
    return canvas(W, H, p)


# --------------------------------------- 47. Memory layout -------------
def memory_layout():
    W, H = 920, 440
    p = [title(30, 34, 'A Process in Memory — Virtual Address Space')]
    p.append(note(30, 53, 'Each process gets its own virtual address space, mapped to physical RAM by the MMU'))

    rows = [
        ('STACK', 'locals, parameters, return addresses \u2014 grows down', BLUE_L, BLUE),
        ('HEAP', 'objects & dynamic memory (new / malloc) \u2014 grows up', TEAL_L, TEAL),
        ('DATA / BSS', 'global and static variables', AMBER_L, AMBER),
        ('TEXT (CODE)', 'executable instructions \u2014 read-only', SLATE_L, SLATE),
    ]
    y = 100
    for name, detail, fill, stroke in rows:
        p.append(box(200, y, 320, 60, fill=fill, stroke=stroke))
        p.append(note(360, y + 26, name, size=12, weight='bold',
                      fill=stroke, anchor='middle'))
        p.append(note(360, y + 46, detail, size=9, fill=MUTED,
                      anchor='middle'))
        y += 75

    # address-direction arrow
    p.append(arrow(600, 380, 600, 100, SLATE))
    p.append(note(600, 88, 'higher addresses', size=9, fill=MUTED,
                  anchor='middle'))
    p.append(note(612, 375, 'lower addresses', size=9, fill=MUTED))

    # side notes
    p.append(wrap(640, 120, 'Stack: auto cleanup on return \u2014 fast, '
                              'fixed-size frames.', size=9.5, maxw=250))
    p.append(wrap(640, 165, 'Heap: programmer-managed (or GC\u2019d); '
                              'shared across threads.', size=9.5, maxw=250))
    p.append(wrap(640, 225, 'Fragmentation: paging (fixed-size frames) '
                              'avoids external fragmentation.', size=9.5,
                  maxw=250))
    p.append(wrap(640, 285, 'Page fault: accessing a page not in RAM \u2014 '
                              'the OS fetches it from disk (swap).',
                  size=9.5, maxw=250))

    p.append(box(40, 400, 850, 30, fill=GREEN_L, stroke=GREEN, rx=6))
    p.append(note(54, 420, 'One process cannot read another process\u2019s '
                           'heap \u2014 the OS enforces the boundary.',
                  size=10, fill=INK))
    return canvas(W, H, p)


# --------------------------------------- 48. Scheduling Gantt ----------
def scheduling_gantt():
    W, H = 920, 430
    p = [title(30, 34, 'CPU Scheduling \u2014 Three Policies, Same Jobs')]
    p.append(note(30, 53, 'P1 (arrive 0, burst 6) \u00b7 P2 (1, 4) \u00b7 P3 (2, 2) \u00b7 P4 (3, 3) \u2014 timeline in time units'))

    x0, scale, bh = 110, 50, 34
    rows = [
        ('FCFS', 100, [('P1', 0, 6, BLUE_L, BLUE), ('P2', 6, 10, TEAL_L, TEAL),
                       ('P3', 10, 12, AMBER_L, AMBER), ('P4', 12, 15, PURPLE_L, PURPLE)],
         '5.5'),
        ('SJF', 185, [('P1', 0, 6, BLUE_L, BLUE), ('P3', 6, 8, AMBER_L, AMBER),
                      ('P4', 8, 11, PURPLE_L, PURPLE), ('P2', 11, 15, TEAL_L, TEAL)],
         '4.75'),
        ('RR (q=2)', 270, [('P1', 0, 2, BLUE_L, BLUE), ('P2', 2, 4, TEAL_L, TEAL),
                           ('P3', 4, 6, AMBER_L, AMBER), ('P1', 6, 8, BLUE_L, BLUE),
                           ('P4', 8, 10, PURPLE_L, PURPLE), ('P2', 10, 12, TEAL_L, TEAL),
                           ('P1', 12, 14, BLUE_L, BLUE), ('P4', 14, 15, PURPLE_L, PURPLE)],
         '6.5'),
    ]
    for name, y, segs, avg in rows:
        p.append(note(40, y + 24, name, size=11, weight='bold', fill=INK))
        for lbl, s, e, fill, stroke in segs:
            bx, bw = x0 + s * scale, (e - s) * scale
            p.append(box(bx, y, bw, bh, fill=fill, stroke=stroke))
            p.append(note(bx + bw / 2, y + 23, lbl, size=10, weight='bold',
                          fill=INK, anchor='middle', mono=True))
        p.append(note(860, y + 50, f'avg waiting time = {avg}', size=9.5,
                      fill=MUTED, anchor='end'))

    # time axis
    p.append(line(x0, 350, 860, 350, SLATE, 1.2))
    for t in (0, 3, 6, 9, 12, 15):
        p.append(line(x0 + t * scale, 346, x0 + t * scale, 354, SLATE, 1.2))
        p.append(note(x0 + t * scale, 368, str(t), size=9, fill=MUTED,
                      anchor='middle'))

    p.append(box(40, 392, 850, 30, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(54, 412, 'SJF gives the lowest average waiting time; '
                           'Round Robin gives the best responsiveness '
                           '(every job runs within 2 units).',
                  size=10, fill=INK))
    return canvas(W, H, p)


# --------------------------------------- 49. JVM architecture ----------
def jvm_architecture():
    W, H = 920, 440
    p = [title(30, 34, 'Java Platform \u2014 JDK, JRE and the JVM')]
    p.append(note(30, 53, 'JDK \u2283 JRE \u2283 JVM \u2014 and what lives inside the JVM'))

    p.append(box(40, 95, 270, 220, fill=BLUE_L, stroke=BLUE))
    p.append(note(55, 118, 'JDK \u2014 development kit', size=11, weight='bold',
                  fill=BLUE))
    p.append(box(60, 135, 230, 165, fill=TEAL_L, stroke=TEAL))
    p.append(note(75, 158, 'JRE \u2014 runtime', size=10.5, weight='bold',
                  fill=TEAL))
    p.append(box(80, 175, 190, 110, fill=PURPLE_L, stroke=PURPLE))
    p.append(note(95, 198, 'JVM \u2014 runs bytecode', size=10, weight='bold',
                  fill=PURPLE))
    p.append(wrap(95, 215, 'class loader + execution engine', size=8.5,
                  maxw=160))

    p.append(arrow(310, 205, 378, 205, SLATE))

    p.append(note(380, 118, 'Inside the JVM', size=11, weight='bold',
                  fill=INK))
    subs = [
        ('Class Loader', 'loads .class files into memory'),
        ('Runtime Data Areas', 'heap, thread stacks, method area, PC registers'),
        ('Execution Engine', 'interpreter + JIT compiler (hot code \u2192 native)'),
        ('Native Method Interface', 'calls into OS / C libraries'),
    ]
    y = 135
    for name, detail in subs:
        p.append(box(380, y, 510, 52, fill='#ffffff', stroke=PURPLE))
        p.append(note(394, y + 21, name, size=10.5, weight='bold',
                      fill=PURPLE))
        p.append(note(394, y + 40, detail, size=9.5, fill=MUTED))
        y += 64

    p.append(box(40, 400, 850, 30, fill=GREEN_L, stroke=GREEN, rx=6))
    p.append(note(54, 420, 'Java compiles to bytecode (.class), not machine '
                           'code \u2014 any JVM on any OS can run it: '
                           '\u201cwrite once, run anywhere\u201d.',
                  size=10, fill=INK))
    return canvas(W, H, p)


# --------------------------------------- 50. String pool ---------------
def string_pool():
    W, H = 920, 400
    p = [title(30, 34, 'Java Strings \u2014 the Pool vs the Heap')]
    p.append(note(30, 53, 'Literals are pooled; new String() always makes a fresh object'))

    p.append(box(40, 95, 420, 250, fill=SLATE_L, stroke=LINE, rx=7))
    code = [
        'String a = "abc";   // pooled',
        'String b = "abc";   // reuses pool',
        'String c = new String("abc"); // heap',
        '',
        'a == b      \u2192 true',
        'a == c      \u2192 false',
        'a.equals(c) \u2192 true',
        'c.equals(a) \u2192 true',
    ]
    for i, ln in enumerate(code):
        p.append(note(56, 125 + i * 26, ln if ln else ' ', size=10, mono=True,
                      fill=INK))

    p.append(box(560, 100, 320, 100, fill=GREEN_L, stroke=GREEN))
    p.append(note(575, 122, 'STRING POOL', size=10.5, weight='bold',
                  fill=GREEN))
    p.append(box(640, 145, 160, 36, label='"abc"', fill='#ffffff',
                 stroke=GREEN, fs=11, mono=True, weight='bold'))

    p.append(box(560, 240, 320, 100, fill=BLUE_L, stroke=BLUE))
    p.append(note(575, 262, 'HEAP (regular objects)', size=10.5,
                  weight='bold', fill=BLUE))
    p.append(box(640, 285, 160, 36, label='"abc" (c)', fill='#ffffff',
                 stroke=BLUE, fs=11, mono=True, weight='bold'))

    p.append(arrow(460, 180, 636, 163, GREEN, label='a, b'))
    p.append(arrow(460, 240, 636, 303, BLUE, label='c'))

    p.append(box(40, 360, 850, 30, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(54, 380, 'Use .equals() to compare String CONTENTS; '
                           '== compares REFERENCES. Pooling saves memory '
                           'for repeated literals.', size=10, fill=INK))
    return canvas(W, H, p)


# --------------------------------------- 51. Exception hierarchy -------
def exception_hierarchy():
    W, H = 920, 430
    p = [title(30, 34, 'Java Exception Hierarchy')]
    p.append(note(30, 53, 'What you must catch, what you may ignore, and what you should never catch'))

    p.append(box(370, 95, 180, 44, label='Throwable', fill=SLATE,
                 stroke=SLATE, tfill='#ffffff', fs=11.5, weight='bold'))
    p.append(box(150, 210, 200, 44, label='Error', fill=RED_L, stroke=RED,
                 fs=11.5, weight='bold'))
    p.append(note(165, 268, 'StackOverflowError, OutOfMemoryError', size=9,
                  fill=MUTED))
    p.append(box(570, 210, 200, 44, label='Exception', fill=BLUE_L,
                 stroke=BLUE, fs=11.5, weight='bold'))

    p.append(box(380, 315, 240, 60, fill=AMBER_L, stroke=AMBER))
    p.append(note(395, 335, 'RuntimeException \u2014 UNCHECKED', size=9.5,
                  weight='bold', fill=AMBER))
    p.append(note(395, 351, 'NPE, ArrayIndexOutOfBounds,', size=8.5,
                  fill=MUTED))
    p.append(note(395, 363, 'ArithmeticException \u2014 no throws needed',
                  size=8.5, fill=MUTED))

    p.append(box(660, 315, 220, 60, fill=TEAL_L, stroke=TEAL))
    p.append(note(675, 335, 'Checked exceptions', size=9.5, weight='bold',
                  fill=TEAL))
    p.append(note(675, 351, 'IOException, SQLException \u2014', size=8.5,
                  fill=MUTED))
    p.append(note(675, 363, 'must be caught or declared', size=8.5,
                  fill=MUTED))

    p.append(arrow(420, 139, 250, 210, SLATE))
    p.append(arrow(500, 139, 670, 210, SLATE))
    p.append(arrow(620, 254, 500, 315, BLUE))
    p.append(arrow(720, 254, 770, 315, TEAL))

    p.append(wrap(40, 100, 'Errors are JVM-level catastrophes \u2014 '
                             'never catch them.', size=9.5, maxw=250))

    p.append(box(40, 395, 850, 30, fill=SLATE_L, stroke=SLATE, rx=6))
    p.append(note(54, 415, 'catch (Exception e) handles everything under '
                           'Exception; throws declares it; finally always '
                           'runs.', size=10, fill=INK))
    return canvas(W, H, p)


OS_JAVA = [
    ('os-process-states', process_states),
    ('os-memory-layout', memory_layout),
    ('os-scheduling-gantt', scheduling_gantt),
    ('java-jvm-architecture', jvm_architecture),
    ('java-string-pool', string_pool),
    ('java-exception-hierarchy', exception_hierarchy),
]
