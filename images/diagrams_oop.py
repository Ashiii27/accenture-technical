"""OOP diagrams for chapter 14 (Object-Oriented Programming)."""
from _svgkit import (AMBER, AMBER_L, BLUE, BLUE_L, GREEN, GREEN_L, INK, LINE,
                     MUTED, PURPLE, PURPLE_L, RED, RED_L, SLATE, SLATE_L, TEAL,
                     TEAL_L, arrow, box, canvas, elbow, line, note, tag, title,
                     txt, tw, wrap)


# ------------------------------------------- 42. Class vs object ----------
def class_vs_object():
    W, H = 920, 440
    p = [title(30, 34, 'Class vs Object — Blueprint vs Instance')]
    p.append(note(30, 53, 'A class defines the structure once; every object is a separate copy in memory'))

    # class blueprint (left)
    p.append(box(40, 95, 250, 32, label='class Car', fill=BLUE,
                 stroke=BLUE, tfill='#ffffff', fs=12, weight='bold'))
    p.append(box(40, 127, 250, 148, fill='#ffffff', stroke=BLUE))
    p.append(line(40, 173, 290, 173, LINE, 1))
    p.append(note(52, 150, '- brand : String', size=10.5, mono=True))
    p.append(note(52, 168, '- speed : int', size=10.5, mono=True))
    p.append(note(52, 196, '+ accelerate()', size=10.5, mono=True, fill=GREEN))
    p.append(note(52, 214, '+ brake()', size=10.5, mono=True, fill=GREEN))
    p.append(note(52, 232, '+ refuel(amt)', size=10.5, mono=True, fill=GREEN))
    p.append(note(52, 258, '- = private   + = public', size=9, fill=MUTED))

    # three objects (right)
    objs = [('car1 = new Car()', "brand='Swift'   speed=0", 95),
            ('car2 = new Car()', "brand='Civic'   speed=60", 187),
            ('car3 = new Car()', "brand='Fortuner' speed=35", 279)]
    for head, detail, y in objs:
        p.append(box(560, y, 300, 72, fill=TEAL_L, stroke=TEAL))
        p.append(note(574, y + 24, head, size=11, weight='bold', fill=TEAL))
        p.append(note(574, y + 48, detail, size=10.5, mono=True))

    # arrows class -> objects
    p.append(arrow(290, 150, 560, 131, TEAL, label='creates'))
    p.append(arrow(290, 201, 560, 223, TEAL, label='creates'))
    p.append(arrow(290, 252, 560, 315, TEAL, label='creates'))

    p.append(box(40, 372, 840, 48, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(wrap(54, 394, 'Each object holds its OWN copy of the fields — change car2.speed and car1/car3 are '
                           'untouched. The methods exist once, inside the class, shared by every object.',
                  size=10, maxw=810, fill=INK))
    return canvas(W, H, p)


# --------------------------------------- 43. Inheritance hierarchy --------
def inheritance_hierarchy():
    W, H = 920, 470
    p = [title(30, 34, 'Inheritance — the IS-A Relationship')]
    p.append(note(30, 53, 'A child class reuses the parent\u2019s fields and methods, then adds its own'))

    # parent
    p.append(box(250, 95, 220, 30, label='class Animal', fill=SLATE,
                 stroke=SLATE, tfill='#ffffff', fs=11.5, weight='bold'))
    p.append(box(250, 125, 220, 74, fill='#ffffff', stroke=SLATE))
    p.append(note(262, 148, '+ name : String', size=10.5, mono=True))
    p.append(note(262, 166, '+ eat()', size=10.5, mono=True, fill=GREEN))
    p.append(note(262, 184, '+ sleep()', size=10.5, mono=True, fill=GREEN))

    # children
    for name, member, x in (('class Dog', '+ bark()', 60), ('class Cat', '+ meow()', 400)):
        p.append(box(x, 260, 200, 30, label=name, fill=BLUE,
                     stroke=BLUE, tfill='#ffffff', fs=11.5, weight='bold'))
        p.append(box(x, 290, 200, 44, fill='#ffffff', stroke=BLUE))
        p.append(note(x + 12, 318, member + '   (added)', size=10.5, mono=True))

    # IS-A arrows (child -> parent)
    p.append(arrow(160, 260, 320, 199, BLUE, label='IS-A'))
    p.append(arrow(500, 260, 400, 199, BLUE, label='IS-A'))

    # right panel
    p.append(box(660, 95, 230, 299, fill=PURPLE_L, stroke=PURPLE, rx=7))
    p.append(note(674, 118, 'What a child class gets', size=10.5, weight='bold',
                  fill=PURPLE))
    items = ['\u2713 Inherits: parent fields',
             '\u2713   + methods (reuse)',
             '\u2713 Adds its own new',
             '\u2713   fields + methods',
             '\u2713 Overrides a parent',
             '\u2713   method with its own',
             '\u2717 Private members are',
             '\u2717   NOT directly reachable',
             '\u2717 Constructors are NOT',
             '\u2717   inherited']
    for i, it in enumerate(items):
        p.append(note(674, 146 + i * 24, it, size=9.5))

    p.append(box(40, 410, 850, 42, fill=GREEN_L, stroke=GREEN, rx=6))
    p.append(note(54, 436, 'Dog IS-A Animal  \u2022  Cat IS-A Animal — every Dog can eat() and sleep() '
                           'without rewriting that code.', size=10.5, fill=INK))
    return canvas(W, H, p)


# --------------------------------------- 44. Inheritance types ------------
def inheritance_types():
    W, H = 920, 430
    p = [title(30, 34, 'The Four Classic Inheritance Shapes')]
    p.append(note(30, 53, 'Single, multilevel, hierarchical and multiple — plus the diamond problem'))

    panels = [('SINGLE', 40), ('MULTILEVEL', 255), ('HIERARCHICAL', 470), ('MULTIPLE', 685)]
    for name, x in panels:
        p.append(box(x, 88, 195, 246, fill=SLATE_L, stroke=LINE, rx=7))
        p.append(box(x + 42, 100, 111, 24, label=name, fill=SLATE, stroke=SLATE,
                     tfill='#ffffff', fs=10, weight='bold'))

    def mini(x, y, label):
        p.append(box(x, y, 90, 40, label=label, fill='#ffffff', stroke=BLUE,
                     fs=11, weight='bold', mono=True))

    # single: A <- B
    mini(95, 150, 'A')
    mini(95, 260, 'B')
    p.append(arrow(140, 260, 140, 190, BLUE, label='IS-A'))

    # multilevel: A <- B <- C
    mini(310, 120, 'A')
    mini(310, 195, 'B')
    mini(310, 270, 'C')
    p.append(arrow(355, 195, 355, 160, BLUE))
    p.append(arrow(355, 270, 355, 235, BLUE))
    p.append(note(297, 330, 'each level adds more', size=9, fill=MUTED))

    # hierarchical: A -> B, C
    mini(545, 120, 'A')
    mini(485, 260, 'B')
    mini(575, 260, 'C')
    p.append(arrow(525, 260, 570, 160, BLUE))
    p.append(arrow(620, 260, 590, 160, BLUE))

    # multiple: B, C -> D
    mini(705, 120, 'B')
    mini(795, 120, 'C')
    mini(750, 260, 'D')
    p.append(arrow(750, 260, 750, 160, BLUE))
    p.append(arrow(772, 260, 820, 160, BLUE))
    p.append(note(700, 210, 'A (hidden base)', size=9, fill=MUTED))

    p.append(box(40, 352, 850, 56, fill=RED_L, stroke=RED, rx=6))
    p.append(wrap(54, 374, 'The diamond problem: with multiple inheritance D would inherit TWO copies of '
                           'A\u2019s members — which one wins is ambiguous. Java and C# ban class multiple '
                           'inheritance (use interfaces instead); Python resolves it with the MRO rule.',
                  size=10, maxw=820, fill=INK))
    return canvas(W, H, p)


# --------------------------------------- 45. Polymorphism -----------------
def polymorphism():
    W, H = 920, 470
    p = [title(30, 34, 'Polymorphism — One Interface, Many Behaviours')]
    p.append(note(30, 53, 'Compile-time (overloading) decides by signature; runtime (overriding) decides by object type'))

    # left panel: overloading
    p.append(box(40, 88, 400, 32, label='COMPILE-TIME — method overloading',
                 fill=BLUE_L, stroke=BLUE, fs=10.5, weight='bold'))
    p.append(box(60, 160, 150, 44, label='add(a, b)', fill='#ffffff', stroke=BLUE,
                 fs=11, weight='bold', mono=True))
    targets = [('add(int, int)', 140), ('add(double, double)', 196), ('add(String, String)', 252)]
    for lbl, y in targets:
        p.append(box(310, y, 120, 40, label=lbl, fill=BLUE_L, stroke=BLUE,
                     fs=9.5, mono=True))
    p.append(arrow(210, 172, 310, 160, BLUE, label='int, int'))
    p.append(arrow(210, 182, 310, 216, BLUE, label='double, double'))
    p.append(arrow(210, 192, 310, 272, BLUE, label='String, String'))
    p.append(wrap(50, 330, 'The compiler picks the matching version by the ARGUMENT TYPES — '
                           'decided before the program even runs.', size=9.5, maxw=370))

    # right panel: overriding
    p.append(box(480, 88, 400, 32, label='RUNTIME — method overriding',
                 fill=PURPLE_L, stroke=PURPLE, fs=10.5, weight='bold'))
    from _svgkit import pill
    p.append(pill(520, 150, 'Animal a = new Dog();', fill=PURPLE_L, stroke=PURPLE,
                  fs=10.5, mono=True)[0])
    p.append(box(520, 210, 150, 44, label='a.sound()', fill='#ffffff', stroke=PURPLE,
                 fs=11, weight='bold', mono=True))
    p.append(box(740, 210, 140, 44, label='which sound()?', fill=PURPLE_L, stroke=PURPLE,
                 fs=10, weight='bold'))
    p.append(box(500, 330, 180, 44, label='Dog.sound() \u2192 woof', fill=PURPLE_L,
                 stroke=PURPLE, fs=10, mono=True))
    p.append(box(700, 330, 180, 44, label='Cat.sound() \u2192 meow', fill=PURPLE_L,
                 stroke=PURPLE, fs=10, mono=True))
    p.append(arrow(740, 254, 590, 330, PURPLE, label='object is a Dog'))
    p.append(arrow(790, 254, 790, 330, PURPLE, label='object is a Cat'))
    p.append(wrap(490, 398, 'The runtime looks at the ACTUAL object type (Dog), not the '
                            'reference type (Animal).', size=9.5, maxw=380))

    p.append(box(40, 424, 840, 34, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(54, 445, 'Overloading = same name, DIFFERENT parameters, ONE class.   '
                           'Overriding = SAME signature, child redefines, TWO classes.',
                  size=10, fill=INK))
    return canvas(W, H, p)


OOP = [
    ('oop-class-object', class_vs_object),
    ('oop-inheritance-hierarchy', inheritance_hierarchy),
    ('oop-inheritance-types', inheritance_types),
    ('oop-polymorphism', polymorphism),
]
