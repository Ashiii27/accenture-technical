#!/usr/bin/env python3
"""Regenerate the PDF versions of the HARD mock sets from the markdown sources.

    pip install reportlab
    python3 generate_pdfs.py

Reads Set-1.md ... Set-5.md in this folder and writes Set-1.pdf ... Set-5.pdf
(questions first, answer key after a clear STOP divider, exactly like the .md).
"""
import glob
import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageBreak,
                                PageTemplate, Paragraph, Preformatted, Spacer,
                                Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
ACCENT = colors.HexColor('#7b1fa2')
GREY = colors.HexColor('#555555')


def styles():
    ss = getSampleStyleSheet()
    s = {}
    s['title'] = ParagraphStyle('title', parent=ss['Title'], fontSize=19, leading=23,
                                textColor=ACCENT, spaceAfter=2)
    s['sub'] = ParagraphStyle('sub', parent=ss['Normal'], fontSize=9.5, leading=13,
                              alignment=TA_CENTER, textColor=GREY, spaceAfter=4)
    s['h1'] = ParagraphStyle('h1', parent=ss['Heading1'], fontSize=13.5, leading=17,
                             textColor=ACCENT, spaceBefore=12, spaceAfter=6)
    s['h2'] = ParagraphStyle('h2', parent=ss['Heading2'], fontSize=11.5, leading=14,
                             textColor=colors.black, spaceBefore=8, spaceAfter=4)
    s['q'] = ParagraphStyle('q', parent=ss['BodyText'], fontSize=9.6, leading=12.6,
                            spaceBefore=7, spaceAfter=2)
    s['opt'] = ParagraphStyle('opt', parent=ss['BodyText'], fontSize=9.4, leading=12.2,
                              leftIndent=10, spaceAfter=0.5)
    s['code'] = ParagraphStyle('code', parent=ss['Code'], fontName='Courier', fontSize=8.3,
                               leading=10.4, leftIndent=8, backColor=colors.HexColor('#f4f4f7'),
                               borderPadding=3, spaceBefore=3, spaceAfter=3)
    s['note'] = ParagraphStyle('note', parent=ss['BodyText'], fontSize=9.4, leading=12.4,
                               textColor=GREY, spaceBefore=2)
    s['ans'] = ParagraphStyle('ans', parent=ss['BodyText'], fontSize=9.2, leading=12,
                              spaceBefore=3, spaceAfter=0)
    s['stop'] = ParagraphStyle('stop', parent=ss['Title'], fontSize=16, leading=20,
                               textColor=colors.HexColor('#b00020'), spaceBefore=10)
    return s


def inline(text):
    """Escape XML, turn `backticks` into Courier spans and **bold** into <b>."""
    parts = []
    for i, chunk in enumerate(re.split(r'`([^`]+)`', text)):
        esc = (chunk.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
        esc = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', esc)
        parts.append(f'<font face="Courier" color="#1a4d7a">{esc}</font>' if i % 2 else esc)
    return ''.join(parts)


def build_table(rows, S):
    data = [[Paragraph(inline(c.strip()), ParagraphStyle('c', parent=S['opt'], fontSize=8.6,
                                                         leading=11, leftIndent=0))
             for c in r] for r in rows]
    t = Table(data, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f0eaf6')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    return t


def render_block(lines, S):
    """Render a chunk of markdown lines (no page-crossing logic)."""
    flow = []
    buf, code, table = [], None, []
    for raw in lines:
        line = raw.rstrip()
        if line.startswith('```'):
            if code is None:
                if buf:
                    flow.append(Paragraph(inline(' '.join(buf)), S['q']))
                    buf = []
                code = []
            else:
                flow.append(Preformatted('\n'.join(code), S['code']))
                code = None
            continue
        if code is not None:
            code.append(line)
            continue
        if line.strip().startswith('|') and line.strip().endswith('|'):
            if buf:
                flow.append(Paragraph(inline(' '.join(buf)), S['q']))
                buf = []
            table.append([c for c in line.strip().strip('|').split('|')])
            continue
        if table:
            rows = [r for r in table if not all(set(c) <= set('-: ') for c in r)]
            flow.append(build_table(rows, S))
            table = []
        if not line.strip() or re.fullmatch(r'-{3,}', line.strip()):
            if buf:
                flow.append(Paragraph(inline(' '.join(buf)), S['q']))
                buf = []
            continue
        if line.startswith('## '):
            if buf:
                flow.append(Paragraph(inline(' '.join(buf)), S['q']))
                buf = []
            flow.append(Paragraph(inline(line[3:]), S['h1']))
        elif line.startswith('# '):
            if buf:
                flow.append(Paragraph(inline(' '.join(buf)), S['q']))
                buf = []
            flow.append(Paragraph(inline(line[2:]), S['title']))
        elif re.match(r'^- [A-D]\)', line):
            if buf:
                flow.append(Paragraph(inline(' '.join(buf)), S['q']))
                buf = []
            flow.append(Paragraph('<b>' + line[2:4] + '</b>' + inline(line[4:]), S['opt']))
        elif line.startswith('**Q'):
            if buf:
                flow.append(Paragraph(inline(' '.join(buf)), S['q']))
                buf = []
            m = re.match(r'^\*\*(Q\d+)\.?\*\*\s*(.*)$', line)
            flow.append(Paragraph('<b>%s.</b> %s' % (inline(m.group(1)), inline(m.group(2))),
                                  S['q']))
        else:
            buf.append(line.lstrip('> '))
    if buf:
        flow.append(Paragraph(inline(' '.join(buf)), S['q']))
    if table:
        rows = [r for r in table if not all(set(c) <= set('-: ') for c in r)]
        flow.append(build_table(rows, S))
    return flow


def build_pdf(md_path, out_path):
    S = styles()
    text = open(md_path, encoding='utf-8').read()
    q_part, key_part = re.split(r'# ⛔ STOP', text)
    meta, q_part = q_part.split('---', 1)

    doc = BaseDocTemplate(out_path, pagesize=A4, topMargin=15 * mm, bottomMargin=15 * mm,
                          leftMargin=16 * mm, rightMargin=14 * mm,
                          title=os.path.basename(out_path)[:-4], author='Accenture prep')
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='n')

    def decorate(canvas, doc_):
        canvas.saveState()
        canvas.setFont('Helvetica', 7.5)
        canvas.setFillColor(GREY)
        canvas.drawString(doc.leftMargin, A4[1] - 10 * mm,
                          os.path.basename(out_path)[:-4] + '  |  ACCENTURE HARD MOCK')
        canvas.drawRightString(A4[0] - doc.rightMargin, 10 * mm, 'Page %d' % doc_.page)
        canvas.restoreState()

    doc.addPageTemplates([PageTemplate(id='all', frames=[frame], onPage=decorate)])

    story = []
    meta_lines = [l for l in meta.strip().split('\n') if l.strip()]
    story.append(Paragraph(inline(meta_lines[0].lstrip('# ')), S['title']))
    for l in meta_lines[1:]:
        story.append(Paragraph(inline(l.strip('- ').replace('**', '')), S['sub']))
    story.append(Spacer(1, 4))

    for item in render_block(q_part.split('\n'), S):
        if isinstance(item, Preformatted):
            story.append(KeepTogether(item))
        else:
            story.append(item)

    story.append(PageBreak())
    story.append(Paragraph('ANSWER KEY', S['stop']))
    story.append(Paragraph('Do not look here until you have finished all 50 questions.',
                           S['note']))
    key_lines = key_part.split('\n')
    ans_para = []
    in_table = False
    table_buf = []
    for line in key_lines:
        if line.strip().startswith('|') and line.strip().endswith('|'):
            if ans_para:
                story.append(Paragraph(inline(' '.join(ans_para)), S['ans']))
                ans_para = []
            table_buf.append([c for c in line.strip().strip('|').split('|')])
            in_table = True
            continue
        if in_table:
            rows = [r for r in table_buf if not all(set(c) <= set('-: ') for c in r)]
            story.append(build_table(rows, S))
            story.append(Spacer(1, 4))
            table_buf, in_table = [], False
        if not line.strip() or line.startswith('---'):
            continue
        if line.startswith('## '):
            if ans_para:
                story.append(Paragraph(inline(' '.join(ans_para)), S['ans']))
                ans_para = []
            story.append(Paragraph(inline(line[3:]), S['h2']))
            continue
        if re.match(r'^\*\*Q\d+', line):
            if ans_para:
                story.append(Paragraph(inline(' '.join(ans_para)), S['ans']))
                ans_para = []
            story.append(Paragraph('<b>' + inline(line.split('**')[1]) + '</b>'
                                   + inline(line.split('**', 2)[2]), S['ans']))
            continue
        ans_para.append(line)
    if ans_para:
        story.append(Paragraph(inline(' '.join(ans_para)), S['ans']))
    if table_buf:
        rows = [r for r in table_buf if not all(set(c) <= set('-: ') for c in r)]
        story.append(build_table(rows, S))

    doc.build(story)


if __name__ == '__main__':
    for md in sorted(glob.glob(os.path.join(HERE, 'Set-*.md'))):
        out = md[:-3] + '.pdf'
        build_pdf(md, out)
        print('wrote', out, os.path.getsize(out), 'bytes')
