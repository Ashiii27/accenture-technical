#!/usr/bin/env python3
"""Parse the repo's markdown question banks into website/questions.js.

Handles the repo's house formats:
  A) chapters 01/02/04/05 : "N. question" + "a) .. b) .. c) .. d) .." (inline)
  B) chapters 14/15/16    : "N. question" + one "a) .." option per line
  C) chapter 11 / mocks   : "**QN.** question" + "- A) .." option lines
  D) hard-mocks           : "**QN.** question" + "- A) .." + "**QN — A.** expl"
Answer keys: compact "N. x |", bold "N. **x)** — expl", or markdown tables.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TOPIC_BY_FILE = {
    "01-networking-security-cloud.md": "Networking / Security / Cloud",
    "02-ms-office-general.md": "MS Office & General",
    "04-dsa.md": "DSA",
    "05-dbms.md": "DBMS / SQL",
    "11-html-css-js.md": "HTML / CSS / JS",
    "14-oop-object-oriented-programming.md": "OOPs",
    "15-os-fundamentals.md": "OS Fundamentals",
    "16-java-basics.md": "Java Basics",
}

LETTERS = ("a", "b", "c", "d")


def clean(s):
    return re.sub(r"\s+", " ", s).strip()


def split_inline_options(text):
    """'... a) x  b) y  c) z  d) w' -> (question, [x, y, z, w])."""
    m = re.search(r"\ba\)\s", text)
    if not m:
        return text, []
    q = text[: m.start()].strip()
    rest = text[m.start():]
    parts = re.split(r"\s+(?=[a-dA-D]\)\s)", rest)
    opts = []
    for p in parts:
        mm = re.match(r"^([a-dA-D])\)\s*(.*)$", p.strip(), re.S)
        if mm:
            opts.append(clean(mm.group(2)))
    return q, opts


def consume_option(cur, letter, rest):
    """Append the first option plus any inline options on the same line."""
    parts = re.split(r"\s+(?=[a-dA-D]\)\s)", rest)
    cur["options"].append(clean(parts[0]))
    for p in parts[1:]:
        mm = re.match(r"^([a-dA-D])\)\s*(.*)$", p.strip(), re.S)
        if mm:
            cur["options"].append(clean(mm.group(2)))


# ------------------------------------------------------------ chapter (A/B/C) -
def parse_chapter(path, topic):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^#{1,2}\s+Practice Questions", text, re.M)
    if not m:
        return []
    body = text[m.end():]
    m2 = re.search(r"^#{1,2}\s+Answer Key", body, re.M)
    key_text = text[m2.start():] if m2 else ""
    if m2:
        body = body[: m2.start()]

    q_re = re.compile(r"^(?:\*\*Q(\d+)\.\*\*|(\d+)\.)\s*(.*)$")
    opt_re = re.compile(r"^(?:-\s*)?([a-d])\)\s+(.*)$")

    questions, cur = [], None
    for ln in body.splitlines():
        s = ln.strip()
        if s.startswith("###") or s == "**(Answers at the end)**":
            continue
        qm = q_re.match(ln)
        if qm and not opt_re.match(s):
            num = qm.group(1) or qm.group(2)
            if cur:
                questions.append(cur)
            cur = {"num": int(num), "text": clean(qm.group(3)), "options": []}
            continue
        om = opt_re.match(s)
        if cur is not None and om:
            consume_option(cur, om.group(1), om.group(2))
            continue
        if cur is not None and s and s not in ("---", "***"):
            if re.search(r"\b[a-d]\)\s", s) and not cur["options"]:
                q2, inline = split_inline_options(cur["text"] + " " + s)
                cur["text"], cur["options"] = q2, inline
            else:
                cur["text"] = clean(cur["text"] + " " + s)
    if cur:
        questions.append(cur)

    answers, expls = {}, {}
    for ln in key_text.splitlines():
        for num, letter in re.findall(r"(\d+)\.\s*\*\*([a-d])", ln):
            answers[int(num)] = letter
        for num, letter in re.findall(r"(?:^|\s)(\d+)\.\s*([a-d])\s*(?:\||$)", ln):
            answers.setdefault(int(num), letter)
        em = re.match(r"^(\d+)\.\s*\*\*([a-d])\)?\*\*\s*[—-]\s*(.+)$", ln)
        if em:
            expls[int(em.group(1))] = clean(em.group(3))

    out = []
    for q in questions:
        if len(q["options"]) < 2:
            continue
        ans = answers.get(q["num"])
        if not ans:
            continue
        out.append({
            "topic": topic, "source": path.name, "q": q["text"],
            "options": q["options"], "answer": ans,
            "explanation": expls.get(q["num"], ""),
        })
    return out

# ------------------------------------------------------------------- mock (C) -
def parse_mock(path):
    text = path.read_text(encoding="utf-8")
    q_re = re.compile(r"^\*\*Q(\d+)\.\*\*\s*(.*)$")
    opt_re = re.compile(r"^- ([A-D])\)\s+(.*)$")

    questions, cur = [], None
    for ln in text.splitlines():
        qm = q_re.match(ln)
        om = opt_re.match(ln)
        if qm:
            if cur:
                questions.append(cur)
            cur = {"num": int(qm.group(1)), "text": clean(qm.group(2)),
                   "options": []}
        elif cur is not None and om:
            consume_option(cur, om.group(1), om.group(2))
        elif (cur is not None and ln.strip()
              and not ln.startswith("#") and ln.strip() not in ("---", "***")):
            cur["text"] = clean(cur["text"] + " " + ln.strip())
    if cur:
        questions.append(cur)

    answers, expls, topics = {}, {}, {}
    for row in text.splitlines():
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) == 4 and re.match(r"^\d+$", cells[0]) \
                and re.match(r"^[A-D]$", cells[1]):
            n = int(cells[0])
            answers[n], topics[n], expls[n] = (
                cells[1].lower(), clean(cells[2]), clean(cells[3]))
        elif len(cells) == 3 and re.match(r"^\d+$", cells[0]) \
                and re.match(r"^[A-D]$", cells[1]):
            n = int(cells[0])
            answers[n], expls[n] = cells[1].lower(), clean(cells[2])

    out = []
    for q in questions:
        ans = answers.get(q["num"])
        if not ans or len(q["options"]) != 4:
            continue
        out.append({
            "topic": topic_from_keyword(topics.get(q["num"], "")),
            "source": path.name, "q": q["text"], "options": q["options"],
            "answer": ans, "explanation": expls.get(q["num"], ""),
        })
    return out


MOCK_TOPIC_MAP = [
    (r"word|excel|powerpoint|office|shortcut|vlookup|pivot", "MS Office & General"),
    (r"tcp|udp|osi|subnet|dns|dhcp|arp|nat|firewall|crypt|ssl|tls|attack|network|ping|port|ip ",
     "Networking / Security / Cloud"),
    (r"loop|bitwise|increment|recursion|array|swap|nested|function|if/else|trace|pseudocode|while|for |output",
     "Pseudocode"),
    (r"stack|queue|big-o|bst|sort|linked|tree|binary|search|complexity|dsa", "DSA"),
    (r"normali[sz]|sql|join|having|acid|index|key|er |dbms|trigger|view|query", "DBMS / SQL"),
    (r"class|inherit|polymorph|encapsulat|abstract|interface|override|oop|constructor", "OOPs"),
    (r"html|css|javascript|dom|selector|tag|frontend", "HTML / CSS / JS"),
    (r"thread|schedul|deadlock|memory|process|page|mutex|kernel|virtual", "OS Fundamentals"),
    (r"java|jvm|jdk|jre|string|arraylist|hashmap", "Java Basics"),
]


def topic_from_keyword(s):
    s = s.lower()
    for pat, topic in MOCK_TOPIC_MAP:
        if re.search(pat, s):
            return topic
    return "General"

# --------------------------------------------------------------- hard mocks (D) -
def parse_hardmock(path):
    text = path.read_text(encoding="utf-8")
    section, questions, cur = "General", [], None
    q_re = re.compile(r"^\*\*Q(\d+)\.\*\*\s*(.*)$")
    opt_re = re.compile(r"^- ([A-D])\)\s+(.*)$")
    sec_re = re.compile(r"^##\s+Section [A-E] — (.+?) \((\d+)\)")
    for ln in text.splitlines():
        sm = sec_re.match(ln)
        if sm:
            section = sm.group(1).strip()
            continue
        qm = q_re.match(ln)
        om = opt_re.match(ln)
        if qm:
            if cur:
                questions.append(cur)
            cur = {"num": int(qm.group(1)), "text": clean(qm.group(2)),
                   "options": [], "topic": hard_topic(section)}
        elif cur is not None and om:
            consume_option(cur, om.group(1), om.group(2))
        elif (cur is not None and ln.strip()
              and not ln.startswith("#") and ln.strip() not in ("---", "***")):
            cur["text"] = clean(cur["text"] + " " + ln.strip())
    if cur:
        questions.append(cur)

    answers, expls = {}, {}
    for m in re.finditer(r"^\*\*Q(\d+) — ([A-D])\.\*\*\s*(.*)$", text, re.M):
        answers[int(m.group(1))] = m.group(2).lower()
        expls[int(m.group(1))] = clean(m.group(3))

    out = []
    for q in questions:
        ans = answers.get(q["num"])
        if not ans or len(q["options"]) != 4:
            continue
        out.append({
            "topic": q["topic"], "source": path.name, "q": q["text"],
            "options": q["options"], "answer": ans,
            "explanation": expls.get(q["num"], ""),
        })
    return out


def hard_topic(section):
    s = section.lower()
    if "office" in s:
        return "MS Office & General"
    if "network" in s:
        return "Networking / Security / Cloud"
    if "cs core" in s:
        return "DSA / DBMS / OOP / Web"
    if "pseudocode" in s:
        return "Pseudocode"
    if "applied" in s:
        return "Applied SQL / Code"
    return "General"


# --------------------------------------------------------------------- main --
def main():
    bank, stats = [], {}

    for fname, topic in TOPIC_BY_FILE.items():
        qs = parse_chapter(ROOT / fname, topic)
        stats[fname] = len(qs)
        bank.extend(qs)

    for fname in ("08-mock-paper-1.md", "09-mock-paper-2.md",
                  "17-mock-paper-5-oop-java-os.md"):
        qs = parse_mock(ROOT / fname)
        stats[fname] = len(qs)
        bank.extend(qs)

    for f in sorted((ROOT / "hard-mocks").glob("Set-*.md")):
        qs = parse_hardmock(f)
        stats[f.name] = len(qs)
        bank.extend(qs)

    for i, q in enumerate(bank, 1):
        q["id"] = i

    js = ("// AUTO-GENERATED by build_bank.py — do not edit by hand.\n"
          "const QUESTION_BANK = " + json.dumps(bank, ensure_ascii=False)
          + ";\n")
    (Path(__file__).parent / "questions.js").write_text(js, encoding="utf-8")

    print(f"total questions: {len(bank)}")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    topics = {}
    for q in bank:
        topics[q["topic"]] = topics.get(q["topic"], 0) + 1
    print("by topic:")
    for t, n in sorted(topics.items(), key=lambda x: -x[1]):
        print(f"  {t}: {n}")
    no_expl = sum(1 for q in bank if not q["explanation"])
    print(f"without explanation: {no_expl}")


if __name__ == "__main__":
    sys.exit(main())
