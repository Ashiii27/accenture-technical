"""Networking, security and cloud diagrams (chapter 01 and chapter 07)."""
from _svgkit import (AMBER, AMBER_L, BG, BLUE, BLUE_L, GREEN, GREEN_L, INK, LINE, MONO,
                     MUTED, PURPLE, PURPLE_L, RED, RED_L, SLATE, SLATE_L, TEAL, TEAL_L,
                     arrow, box, canvas, elbow, line, note, pill, tag, title, txt, tw, wrap)


# ---------------------------------------------------------------- 1. OSI ----
def osi_layers():
    W, H = 780, 512
    p = [title(30, 34, 'OSI Model — 7 Layers, PDUs, Protocols & Devices',
               sub='Mnemonic (top→bottom): All People Seem To Need Data Processing')]
    cols = [(34, 40, '#'), (82, 172, 'Layer'), (262, 150, 'PDU'),
            (420, 250, 'Example protocols'), (676, 92, 'Device')]
    y = 74
    for cx, cw, lbl in cols:
        p.append(note(cx + (0 if lbl == '#' else 0), y, lbl, size=10.5, weight='bold'))
    y += 10
    p.append(line(30, y, 750, y, LINE, 1))
    rows = [
        ('7', 'Application', 'Data', 'HTTP, HTTPS, FTP, SMTP, DNS, DHCP', '—', PURPLE_L, PURPLE),
        ('6', 'Presentation', 'Data', 'TLS/SSL, JPEG, ASCII, encryption', '—', PURPLE_L, PURPLE),
        ('5', 'Session', 'Data', 'NetBIOS, RPC, SIP, sockets', '—', PURPLE_L, PURPLE),
        ('4', 'Transport', 'Segment / Datagram', 'TCP, UDP, port numbers', '—', BLUE_L, BLUE),
        ('3', 'Network', 'Packet', 'IP, ICMP, OSPF, BGP, ARP', 'Router', TEAL_L, TEAL),
        ('2', 'Data Link', 'Frame', 'Ethernet, MAC, VLAN 802.1Q, PPP', 'Switch', AMBER_L, AMBER),
        ('1', 'Physical', 'Bits', 'Cables, hubs, signals, 802.11', 'Hub', AMBER_L, AMBER),
    ]
    rh = 46
    for i, (num, name, pdu, prot, dev, fill, stroke) in enumerate(rows):
        yy = y + 6 + i * (rh + 4)
        p.append(box(30, yy, 720, rh, fill=fill, stroke=stroke, lw=1, rx=6))
        p.append(box(34, yy + 6, 40, rh - 12, label=num, fill='#ffffff', stroke=stroke,
                     rx=5, fs=13, weight='bold', tfill=stroke))
        p.append(note(82, yy + 20, name, size=12, weight='bold'))
        p.append(note(82, yy + 36, pdu, size=9.5, mono=True))
        p.append(note(262, yy + 27, 'PDU: ' + pdu.split(' / ')[0], size=10.5))
        p.append(note(420, yy + 20, prot, size=10, fill=SLATE))
        p.append(note(676, yy + 27, dev, size=11, weight='bold'))
    yb = y + 6 + 7 * (rh + 4) + 8
    p.append(note(30, yb + 16, 'Layer 1–2 = hardware/media layers  •  Layer 3–4 = addressing & delivery  '
                              '•  Layer 5–7 = application-facing', size=10, fill=MUTED))
    p.append(note(30, yb + 36, 'Trap: TLS is described as sitting BETWEEN the Transport and Application '
                              'layers (it protects L4–L7 traffic).', size=10, fill=MUTED))
    return canvas(W, H, p)


# ------------------------------------------------------- 2. Encapsulation ---
def encapsulation():
    W, H = 760, 352
    p = [title(30, 34, 'Encapsulation — What Each Layer Adds on the Way Down',
               sub='Sender adds headers going down; receiver strips them coming up')]
    seg = [('Ethernet header', SLATE_L, SLATE), ('IP header', TEAL_L, TEAL),
           ('TCP header', BLUE_L, BLUE), ('Application data', AMBER_L, AMBER),
           ('FCS (trailer)', SLATE_L, SLATE)]
    x, y, h = 40, 90, 78
    for name, fill, stroke in seg:
        w = 118 if name != 'Application data' else 190
        p.append(box(x, y, w, h, fill=fill, stroke=stroke))
        p.append(txt(x + w / 2, y + 44, name, size=10, anchor='middle', fill=INK))
        x += w
    p.append(note(40, 78, 'The frame that actually goes on the wire (Layer 2)', size=10, fill=MUTED))
    # arrows and PDU names below
    x = 40
    for name, fill, stroke in seg:
        w = 118 if name != 'Application data' else 190
        p.append(elbow(x + w / 2, y + h + 6, x + w / 2, y + h + 34, stroke=stroke, lw=1.2,
                       head=6, axis='v'))
        x += w
    names = [('L4: Segment', 40 + 118 * 2, BLUE), ('L3: Packet', 40 + 118, TEAL),
             ('L2: Frame', 40, SLATE), ('L1: Bits (0/1 on the wire)', 40, SLATE)]
    y2 = y + h + 50
    p.append(box(158, y2, 190, 30, label='L4: Segment (TCP hdr + data)', fill=BLUE_L,
                 stroke=BLUE, fs=10.5))
    p.append(box(40, y2 + 40, 308, 30, label='L3: Packet (IP hdr + segment)', fill=TEAL_L,
                 stroke=TEAL, fs=10.5))
    p.append(box(40, y2 + 80, 426, 30, label='L2: Frame (Eth hdr + packet + FCS)', fill=SLATE_L,
                 stroke=SLATE, fs=10.5))
    p.append(note(500, y2 + 20, 'Device view:', size=10.5, weight='bold'))
    p.append(note(500, y2 + 40, 'Switch reads L2 frame (MAC only)', size=10))
    p.append(note(500, y2 + 58, 'Router reads L3 packet (IP only)', size=10))
    p.append(note(500, y2 + 76, 'Firewall reads L3 + L4 (IP + port)', size=10))
    p.append(note(500, y2 + 100, 'A switch never rewrites the IP header;', size=10, fill=MUTED))
    p.append(note(500, y2 + 116, 'a router rewrites L2 per hop.', size=10, fill=MUTED))
    return canvas(W, H, p)


# --------------------------------------------------------- 3. TCP vs UDP ----
def tcp_vs_udp():
    W, H = 740, 396
    p = [title(30, 34, 'TCP vs UDP — The Comparison Accenture Tests')]
    head = [('Feature', 30, 250), ('TCP', 290, 200), ('UDP', 500, 210)]
    y = 74
    for lbl, x, w in head:
        p.append(box(x, y, w, 30, label=lbl, fill=SLATE_L, stroke=SLATE, fs=11.5, weight='bold'))
    rows = [
        ('Connection', 'Connection-oriented (3-way handshake)', 'Connectionless — just send'),
        ('Reliability', 'Guaranteed: ACKs + retransmission', 'Best effort; packets may be lost'),
        ('Ordering', 'In-order delivery (sequence numbers)', 'No ordering guarantee'),
        ('Speed / overhead', 'Slower, more overhead', 'Faster, minimal overhead'),
        ('Header size', '20 bytes', '8 bytes'),
        ('Flow & congestion', 'Yes — sliding window, slow start', 'No'),
        ('Typical use', 'Web, email, file transfer, SSH', 'VoIP, video, DNS, gaming, NTP'),
    ]
    rh = 36
    for i, (f, t, u) in enumerate(rows):
        yy = y + 30 + i * rh
        p.append(box(30, yy, 250, rh - 3, fill='#ffffff', stroke=LINE, lw=1, rx=4))
        p.append(note(40, yy + 22, f, size=10.5, weight='bold'))
        p.append(box(290, yy, 200, rh - 3, fill=BLUE_L, stroke=BLUE, lw=1, rx=4))
        p.append(note(298, yy + 22, t, size=10))
        p.append(box(500, yy, 210, rh - 3, fill=AMBER_L, stroke=AMBER, lw=1, rx=4))
        p.append(note(508, yy + 22, u, size=10))
    p.append(wrap(30, H - 24, 'Trap: UDP is NOT "worse" — for live voice/video, lost packets are '
                              'preferable to the delay caused by retransmission (jitter).',
                   size=10, fill=MUTED, maxw=W - 60))
    return canvas(W, H, p)


# ------------------------------------------------- 4. TCP handshake / FIN ----
def tcp_handshake():
    W, H = 760, 520
    p = [title(30, 34, 'TCP Connection: Three-Way Handshake and Four-Way Teardown',
               sub='Flags that consume a sequence number: SYN and FIN')]
    # panel A
    y0 = 92
    p.append(box(30, y0, 700, 210, fill='#fafafa', stroke=LINE, lw=1, rx=8))
    p.append(note(44, y0 + 22, 'A. OPENING THE CONNECTION', size=10.5, weight='bold', fill=BLUE))
    cx, sx = 150, 560
    p.append(box(cx - 62, y0 + 34, 124, 34, label='CLIENT', fill=BLUE_L, stroke=BLUE, fs=12,
                 weight='bold'))
    p.append(box(sx - 62, y0 + 34, 124, 34, label='SERVER', fill=TEAL_L, stroke=TEAL, fs=12,
                 weight='bold'))
    p.append(line(cx, y0 + 72, cx, y0 + 196, BLUE, 1.2, '4 4'))
    p.append(line(sx, y0 + 72, sx, y0 + 196, TEAL, 1.2, '4 4'))
    steps = [
        ('1', 'SYN, seq=x', '→', 'Server moves LISTEN → SYN-RCVD'),
        ('2', 'SYN-ACK, seq=y, ack=x+1', '←', 'Client moves SYN-SENT → ESTABLISHED'),
        ('3', 'ACK, ack=y+1', '→', 'Server moves SYN-RCVD → ESTABLISHED'),
    ]
    for i, (n, msg, direction, state) in enumerate(steps):
        yy = y0 + 100 + i * 34
        if direction == '→':
            p.append(arrow(cx, yy, sx, yy, BLUE if i % 2 == 0 else BLUE, 1.6, 7))
        else:
            p.append(arrow(sx, yy, cx, yy, TEAL, 1.6, 7))
        p.append(txt((cx + sx) / 2, yy - 7, msg, size=10.5, anchor='middle', mono=True,
                     weight='bold'))
        p.append(note(sx + 14 if direction == '→' else 30, yy + 4, state, size=9, fill=MUTED))
    p.append(note(44, y0 + 202, 'Data can start flowing after step 3. Data bytes are numbered from '
                                'x+1 (client) and y+1 (server).', size=9.5, fill=MUTED))
    # panel B
    y1 = y0 + 230
    p.append(box(30, y1, 700, 190, fill='#fafafa', stroke=LINE, lw=1, rx=8))
    p.append(note(44, y1 + 22, 'B. CLOSING THE CONNECTION (four-way, either side can start)',
                   size=10.5, weight='bold', fill=RED))
    p.append(box(cx - 62, y1 + 34, 124, 30, label='ACTIVE CLOSE', fill=BLUE_L, stroke=BLUE,
                 fs=10.5, weight='bold'))
    p.append(box(sx - 62, y1 + 34, 124, 30, label='PASSIVE CLOSE', fill=TEAL_L, stroke=TEAL,
                 fs=10.5, weight='bold'))
    p.append(line(cx, y1 + 68, cx, y1 + 176, BLUE, 1.2, '4 4'))
    p.append(line(sx, y1 + 68, sx, y1 + 176, TEAL, 1.2, '4 4'))
    fin = [('1', 'FIN, seq=u', '→'), ('2', 'ACK, ack=u+1', '←'),
           ('3', 'FIN, seq=v', '←'), ('4', 'ACK, ack=v+1', '→')]
    for i, (n, msg, d) in enumerate(fin):
        yy = y1 + 96 + i * 28
        if d == '→':
            p.append(arrow(cx, yy, sx, yy, BLUE, 1.5, 6))
        else:
            p.append(arrow(sx, yy, cx, yy, TEAL, 1.5, 6))
        p.append(txt((cx + sx) / 2, yy - 6, msg, size=10, anchor='middle', mono=True))
    p.append(note(44, y1 + 182, 'The ACTIVE closer (first FIN) sends the last ACK and waits in '
                                'TIME_WAIT for 2 × MSL — that is where stray duplicate packets die.',
                   size=9.5, fill=MUTED))
    return canvas(W, H, p)


# ----------------------------------------------------------- 5. Subnetting ---
def subnet_math():
    W, H = 780, 460
    p = [title(30, 34, 'Subnet Math — Reading 192.168.10.75/26 Bit by Bit',
               sub='Prefix /26 = 26 network bits (N) + 6 host bits (H)')]
    y = 92
    octets = ['11000000', '10101000', '00001010', '01001011']
    labels = ['192', '168', '10', '75']
    x = 60
    p.append(note(30, y - 10, 'IP address in binary', size=10, weight='bold'))
    for i, (lab, bits) in enumerate(zip(labels, octets)):
        p.append(txt(x, y + 6, lab, size=11, anchor='middle', mono=True, weight='bold'))
        x0 = x - len(bits) * 6.2
        for j, b in enumerate(bits):
            fill = BLUE_L if (i * 8 + j) < 26 else AMBER_L
            stroke = BLUE if (i * 8 + j) < 26 else AMBER
            p.append(box(x0 + j * 12.4, y + 12, 11.4, 22, fill=fill, stroke=stroke, lw=0.8, rx=2))
            p.append(txt(x0 + j * 12.4 + 5.7, y + 27, b, size=9, anchor='middle', mono=True))
        x += 175
    # boundary
    bx = 60 - 32 * 6.2 + 26 * 12.4
    p.append(line(bx, y + 8, bx, y + 40, RED, 1.6))
    p.append(txt(bx, y + 50, '/26', size=9.5, anchor='middle', fill=RED, weight='bold'))
    p.append(txt(bx - 10, y + 50, '← network bits (26)', size=9, anchor='end', fill=BLUE))
    p.append(txt(bx + 10, y + 50, 'host bits (6) →', size=9, anchor='start', fill=AMBER))
    # mask row
    y += 76
    p.append(note(30, y - 4, 'Subnet mask 255.255.255.192  (26 ones, then six zeros)', size=10,
                  weight='bold'))
    mask = ['11111111', '11111111', '11111111', '11000000']
    x = 60
    for i, bits in enumerate(mask):
        x0 = x - len(bits) * 6.2
        for j, b in enumerate(bits):
            fill = BLUE_L if b == '1' else '#ffffff'
            stroke = BLUE if b == '1' else LINE
            p.append(box(x0 + j * 12.4, y + 4, 11.4, 22, fill=fill, stroke=stroke, lw=0.8, rx=2))
            p.append(txt(x0 + j * 12.4 + 5.7, y + 19, b, size=9, anchor='middle', mono=True))
        x += 175
    # maths
    y += 44
    maths = [('Host bits', '32 − 26 = 6', BLUE_L, BLUE),
             ('Total addresses', '2⁶ = 64', BLUE_L, BLUE),
             ('Usable hosts', '64 − 2 = 62', GREEN_L, GREEN),
             ('Block size', '2⁶ = 64  (step 64)', AMBER_L, AMBER)]
    x = 30
    for name, val, fill, stroke in maths:
        p.append(box(x, y, 172, 52, fill=fill, stroke=stroke))
        p.append(note(x + 10, y + 20, name, size=9.5, weight='bold'))
        p.append(txt(x + 10, y + 40, val, size=11.5, mono=True, fill=INK))
        x += 184
    # range strip
    y += 76
    p.append(note(30, y, 'Where .75 lands:', size=10.5, weight='bold'))
    blocks = [('0 – 63', 'subnet 0', '#ffffff'), ('64 – 127', 'subnet 1  ← 75 is here', GREEN_L),
              ('128 – 191', 'subnet 2', '#ffffff'), ('192 – 255', 'subnet 3', '#ffffff')]
    x = 30
    for rng, lab, fill in blocks:
        p.append(box(x, y + 8, 175, 40, fill=fill, stroke=GREEN if 'here' in lab else LINE))
        p.append(txt(x + 87, y + 26, rng, size=10.5, anchor='middle', mono=True))
        p.append(txt(x + 87, y + 40, lab, size=9, anchor='middle', fill=MUTED))
        x += 179
    y += 68
    res = [('Network', '192.168.10.64', BLUE), ('First host', '192.168.10.65', TEAL),
           ('Last host', '192.168.10.126', TEAL), ('Broadcast', '192.168.10.127', RED)]
    x = 30
    for name, val, stroke in res:
        p.append(box(x, y, 175, 44, fill='#ffffff', stroke=stroke, lw=1.4))
        p.append(note(x + 10, y + 18, name, size=9.5, weight='bold'))
        p.append(txt(x + 10, y + 36, val, size=11.5, mono=True, fill=stroke))
        x += 179
    return canvas(W, H, p)


# -------------------------------------------------------- 6. IP classes ------
def ip_classes():
    W, H = 800, 372
    p = [title(30, 34, 'IPv4 Address Classes & Private (RFC 1918) Ranges')]
    heads = [('Class', 30, 90), ('First octet', 124, 110), ('Leading bits', 238, 110),
             ('Default mask', 352, 130), ('Hosts / network', 486, 140), ('Private range', 630, 140)]
    y = 72
    for lbl, x, w in heads:
        p.append(box(x, y, w, 28, label=lbl, fill=SLATE_L, stroke=SLATE, fs=10, weight='bold'))
    rows = [
        ('A', '1 – 126', '0', '255.0.0.0  (/8)', '16,777,214', '10.0.0.0/8', BLUE_L, BLUE),
        ('B', '128 – 191', '10', '255.255.0.0  (/16)', '65,534', '172.16.0.0/12', TEAL_L, TEAL),
        ('C', '192 – 223', '110', '255.255.255.0  (/24)', '254', '192.168.0.0/16', AMBER_L, AMBER),
        ('D', '224 – 239', '1110', '— multicast —', '—', '224.0.0.0/4 (multicast)', SLATE_L, SLATE),
        ('E', '240 – 255', '1111', '— experimental —', '—', '—', SLATE_L, SLATE),
    ]
    rh = 34
    for i, (c, r, lead, mask, hosts, priv, fill, stroke) in enumerate(rows):
        yy = y + 28 + i * rh
        p.append(box(30, yy, 90, rh - 3, fill=fill, stroke=stroke))
        p.append(txt(75, yy + 22, c, size=12, anchor='middle', weight='bold', fill=stroke))
        for val, (x, w) in zip([r, lead, mask, hosts, priv],
                               [(h[1], h[2]) for h in heads[1:]]):
            p.append(box(x, yy, w, rh - 3, fill='#ffffff', stroke=LINE, lw=1, rx=3))
            p.append(note(x + 8, yy + 21, val, size=9.5, mono=True))
    y2 = y + 28 + 5 * rh + 16
    p.append(box(30, y2, 740, 68, fill=RED_L, stroke=RED, rx=6))
    p.append(note(44, y2 + 22, 'Special-purpose addresses to memorise', size=10.5, weight='bold',
                  fill=RED))
    p.append(note(44, y2 + 40, '127.0.0.0/8 = loopback (::1 in IPv6)   •   169.254.0.0/16 = APIPA '
                               '(DHCP failed)', size=9.5))
    p.append(note(44, y2 + 54, '0.0.0.0 = default route / "any"   •   255.255.255.255 = local '
                               'broadcast   •   FE80::/10 = IPv6 link-local', size=9.5))
    p.append(note(30, H - 16, 'Trap: 172.32.x.x is NOT private — the private block is 172.16.0.0/12 '
                              '(172.16 – 172.31 only).', size=10, fill=MUTED))
    return canvas(W, H, p)


# -------------------------------------------------------------- 7. NAT -------
def nat_pat():
    W, H = 770, 404
    p = [title(30, 34, 'NAT / PAT — How One Public IP Serves a Whole LAN')]
    hosts = [('PC-A', '192.168.1.10', 3001), ('PC-B', '192.168.1.11', 3002),
             ('PC-C', '192.168.1.12', 3003)]
    x = 36
    for name, ip, port in hosts:
        p.append(box(x, 80, 130, 40, fill=BLUE_L, stroke=BLUE))
        p.append(txt(x + 65, 98, name, size=10.5, anchor='middle', weight='bold'))
        p.append(txt(x + 65, 113, f'{ip}:{port}', size=9.5, anchor='middle', mono=True))
        p.append(arrow(x + 130, 100, 300, 112, BLUE, 1.4, 7))
        x += 150
    p.append(box(300, 78, 170, 46, label='Switch', fill=SLATE_L, stroke=SLATE, fs=11))
    # router + table
    p.append(box(300, 150, 170, 44, label='NAT Router', fill=TEAL_L, stroke=TEAL, fs=12,
                 weight='bold'))
    p.append(txt(385, 212, 'public IP 203.0.113.5', size=10, anchor='middle', mono=True, fill=TEAL))
    p.append(arrow(470, 172, 620, 172, TEAL, 1.6, 8, label='translated packets', lsize=9.5))
    p.append(box(620, 150, 120, 44, label='Internet', fill=AMBER_L, stroke=AMBER, fs=12,
                 weight='bold'))
    # translation table
    p.append(note(30, 244, 'PAT translation table inside the router', size=10.5, weight='bold'))
    heads = [('Inside (private)', 30, 200), ('Outside (public)', 240, 210),
             ('Remote server', 460, 260)]
    y = 258
    for lbl, hx, hw in heads:
        p.append(box(hx, y, hw, 26, label=lbl, fill=SLATE_L, stroke=SLATE, fs=10, weight='bold'))
    rows = [('192.168.1.10:3001', '203.0.113.5:40001', '93.184.216.34:80'),
            ('192.168.1.11:3002', '203.0.113.5:40002', '93.184.216.34:80'),
            ('192.168.1.12:3003', '203.0.113.5:40003', '93.184.216.34:443')]
    for i, (a, b, c) in enumerate(rows):
        yy = y + 26 + i * 24
        for val, (hx, hw) in zip([a, b, c], [(h[1], h[2]) for h in heads]):
            p.append(box(hx, yy, hw, 22, fill='#ffffff', stroke=LINE, lw=0.8, rx=3))
            p.append(note(hx + 8, yy + 15, val, size=9.5, mono=True))
    p.append(wrap(30, H - 34, 'NAT hides internal hosts (they are not reachable from outside until '
                              'they speak first) and delays IPv4 exhaustion — it is not a firewall, '
                              'but it behaves like one.', size=10, fill=MUTED, maxw=W - 60))
    return canvas(W, H, p)


# ----------------------------------------------------- 8. DNS resolution ----
def dns_resolution():
    W, H = 790, 430
    p = [title(30, 34, 'DNS Resolution — Iterative Query for www.example.com',
               sub='The local resolver does the walking; your machine makes one query and gets one '
                   'answer')]
    lanes = [('Your PC\n(browser / stub resolver)', 36, 150, BLUE),
             ('Local DNS resolver\n(ISP or 8.8.8.8) — caches', 250, 180, TEAL),
             ('Root server  (.)', 520, 230, SLATE),
             ('TLD server  (.com)', 520, 230, SLATE),
             ('Authoritative\nns1.example.com', 520, 230, AMBER)]
    # lane 1 and 2 boxes
    p.append(box(36, 84, 150, 60, fill=BLUE_L, stroke=BLUE))
    p.append(txt(111, 108, 'Your PC', size=11, anchor='middle', weight='bold'))
    p.append(txt(111, 124, 'stub resolver', size=9.5, anchor='middle', mono=True))
    p.append(box(250, 84, 190, 60, fill=TEAL_L, stroke=TEAL))
    p.append(txt(345, 106, 'Local DNS resolver', size=11, anchor='middle', weight='bold'))
    p.append(txt(345, 122, 'recursive + caching', size=9.5, anchor='middle', mono=True))
    servers = [('Root server  (.)', 96, SLATE_L, SLATE), ('TLD server  (.com)', 168, SLATE_L, SLATE),
               ('Authoritative  ns1.example.com', 240, AMBER_L, AMBER)]
    for lbl, sy, fill, stroke in servers:
        p.append(box(520, sy, 240, 56, fill=fill, stroke=stroke))
        p.append(txt(640, sy + 26, lbl, size=10.5, anchor='middle', weight='bold', mono=True))
        p.append(txt(640, sy + 44, {'Root server  (.)': '13 clusters worldwide',
                                    'TLD server  (.com)': 'knows every .com name server',
                                    'Authoritative  ns1.example.com': 'HAS the A record'}
        [lbl], size=9, anchor='middle', fill=MUTED))
    p.append(arrow(186, 106, 250, 106, BLUE, 1.5, 7, label='1  query', lsize=9.5))
    p.append(arrow(440, 108, 520, 120, TEAL, 1.5, 7, label='2  "where is .com?"', lsize=9.5))
    p.append(arrow(520, 140, 440, 128, SLATE, 1.4, 7, label='3  ask .com TLD', lsize=9.5))
    p.append(arrow(440, 160, 520, 168, TEAL, 1.4, 7, label='4  "where is example.com?"', lsize=9.5))
    p.append(arrow(520, 196, 440, 184, SLATE, 1.4, 7, label='5  ask ns1.example.com', lsize=9.5))
    p.append(arrow(440, 216, 520, 252, TEAL, 1.4, 7, label='6  "A = 93.184.216.34"', lsize=9.5))
    p.append(arrow(520, 284, 440, 272, AMBER, 1.5, 7, label='7  answer + TTL', lsize=9.5))
    p.append(arrow(250, 128, 186, 128, GREEN, 1.6, 8, label='8  answer (cached)', lsize=9.5))
    p.append(box(36, 320, 724, 82, fill='#fafafa', stroke=LINE, rx=6))
    p.append(note(50, 340, 'Record types you must know', size=10.5, weight='bold'))
    recs = [('A / AAAA', 'name → IPv4 / IPv6'), ('CNAME', 'alias → canonical name'),
            ('MX', 'mail server for the domain'), ('NS', 'authoritative name server'),
            ('PTR', 'IP → name (reverse)'), ('SOA', 'zone start-of-authority'),
            ('TXT', 'SPF, DKIM, verification')]
    x = 50
    for i, (r, d) in enumerate(recs):
        cx = 50 + (i % 4) * 180
        cy = 358 + (i // 4) * 20
        p.append(txt(cx, cy, f'{r}  — {d}', size=9.5, mono=False))
    return canvas(W, H, p)


# ---------------------------------------------------------- 9. DHCP DORA ----
def dhcp_dora():
    W, H = 750, 400
    p = [title(30, 34, 'DHCP — The DORA Exchange (UDP 67 server / 68 client)')]
    p.append(box(60, 80, 160, 44, label='Client  (0.0.0.0)', fill=BLUE_L, stroke=BLUE, fs=11.5,
                 weight='bold'))
    p.append(box(500, 80, 180, 44, label='DHCP Server', fill=TEAL_L, stroke=TEAL, fs=11.5,
                 weight='bold'))
    p.append(line(140, 124, 140, 300, BLUE, 1.2, '4 4'))
    p.append(line(590, 124, 590, 300, TEAL, 1.2, '4 4'))
    steps = [
        ('1', 'DISCOVER', 'broadcast →', 'Client has no IP yet: "Is there a DHCP server?"',
         BLUE),
        ('2', 'OFFER', '← unicast/broadcast', 'Server offers an IP + mask + lease', TEAL),
        ('3', 'REQUEST', 'broadcast →', 'Client formally asks for the offered IP', BLUE),
        ('4', 'ACKNOWLEDGE', '← unicast/broadcast', 'Server confirms; client configures itself', TEAL),
    ]
    for i, (n, name, direction, desc, col) in enumerate(steps):
        y = 150 + i * 42
        if direction.startswith('broadcast') or direction == 'broadcast →':
            p.append(arrow(140, y, 590, y, col, 1.5, 7))
        else:
            p.append(arrow(590, y, 140, y, col, 1.5, 7))
        p.append(txt(365, y - 7, f'{n}. {name}   ({direction})', size=10.5, anchor='middle',
                     weight='bold', mono=True, fill=col))
        p.append(txt(365, y + 12, desc, size=9.5, anchor='middle', fill=MUTED))
    p.append(box(30, 322, 690, 62, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(46, 342, 'What the ACK carries', size=10.5, weight='bold', fill=AMBER))
    p.append(wrap(46, 362, 'IP address  •  subnet mask  •  default gateway  •  DNS server(s)  '
                           '•  lease time  •  (optionally NTP, domain name)', size=10, maxw=650))
    p.append(wrap(46, 380, 'No DHCP server reachable? Windows/Linux self-assign an APIPA address '
                           'from 169.254.0.0/16 — you get link-local connectivity only.',
                   size=9.5, fill=MUTED, maxw=650))
    return canvas(W, H, p)


# ---------------------------------------------------------------- 10. ARP ----
def arp_resolution():
    W, H = 750, 380
    p = [title(30, 34, 'ARP — Resolving an IP Address to a MAC Address',
               sub='"I know the IP, who owns it? Tell me your MAC."')]
    hosts = [('Host A', '192.168.1.10', 'AA:AA:AA:AA:AA:AA', 40, BLUE),
             ('Host B', '192.168.1.20', 'BB:BB:BB:BB:BB:BB', 290, GREEN),
             ('Host C', '192.168.1.30', 'CC:CC:CC:CC:CC:CC', 540, SLATE)]
    for name, ip, mac, x, col in hosts:
        p.append(box(x, 90, 170, 64, fill={'#4f46e5': BLUE_L, '#16a34a': GREEN_L,
                                           '#475569': SLATE_L}[col], stroke=col))
        p.append(txt(x + 85, 112, name, size=11, anchor='middle', weight='bold'))
        p.append(txt(x + 85, 128, ip, size=9.5, anchor='middle', mono=True))
        p.append(txt(x + 85, 144, mac, size=9, anchor='middle', mono=True, fill=MUTED))
    p.append(line(40, 154, 710, 154, LINE, 1.2, '6 4'))
    p.append(txt(375, 172, 'Switch — floods unknown/broadcast frames to every port',
                 size=9.5, anchor='middle', fill=MUTED))
    # step 1 - broadcast
    p.append(box(40, 190, 170, 40, fill='#ffffff', stroke=BLUE, lw=1.4))
    p.append(txt(125, 206, '1. ARP Request', size=10, anchor='middle', weight='bold'))
    p.append(txt(125, 221, 'Who has .20?', size=9.5, anchor='middle', mono=True))
    p.append(arrow(210, 210, 290, 210, BLUE, 1.5, 7, label='broadcast', lsize=9))
    p.append(arrow(210, 210, 540, 210, BLUE, 1.5, 7, dash='4 3'))
    p.append(txt(375, 244, 'Destination MAC = FF:FF:FF:FF:FF:FF  (everyone listens)',
                 size=9.5, anchor='middle', fill=MUTED))
    # step 2 - reply
    p.append(arrow(460, 272, 210, 272, GREEN, 1.6, 8, label='2. ARP Reply (unicast)', lsize=9.5))
    p.append(txt(375, 292, '"192.168.1.20 is at BB:BB:BB:BB:BB:BB"', size=10, anchor='middle',
                 mono=True))
    p.append(box(30, 310, 690, 54, fill=GREEN_L, stroke=GREEN, rx=6))
    p.append(wrap(46, 328, 'Result: Host A stores the mapping in its ARP cache (TTL ~2-20 min) and '
                           'can now build the Layer-2 frame.', size=10, maxw=650))
    p.append(wrap(46, 346, 'Off-subnet? Host A never ARPs for the far-away host — it ARPs for its '
                           'DEFAULT GATEWAY. IPv6 replaces ARP with NDP (ICMPv6).',
                   size=9.5, fill=MUTED, maxw=650))
    return canvas(W, H, p)


# ------------------------------------------------ 11. Devices & domains ------
def devices_domains():
    W, H = 790, 400
    p = [title(30, 34, 'Hub vs Switch vs Router — Collision & Broadcast Domains')]
    panels = [
        ('HUB (Layer 1)', BLUE, 'Repeats every bit to every port',
         '1 collision domain, 1 broadcast domain', 'Half-duplex, slowest, obsolete'),
        ('SWITCH (Layer 2)', TEAL, 'Forwards by MAC address table',
         'Collision domain per port, 1 broadcast domain', 'Full-duplex; VLANs split broadcast domains'),
        ('ROUTER (Layer 3)', AMBER, 'Forwards by IP / routing table',
         'Separate broadcast domain per interface', 'Does NOT forward broadcasts — that is the point'),
    ]
    x = 30
    for name, col, how, domains, extra in panels:
        p.append(box(x, 78, 240, 70, fill=col + '1a', stroke=col))
        p.append(txt(x + 120, 100, name, size=11, anchor='middle', weight='bold', fill=col))
        p.append(txt(x + 120, 118, how, size=9.5, anchor='middle'))
        p.append(box(x, 158, 240, 96, fill='#fafafa', stroke=LINE, lw=1, rx=6))
        # tiny topology
        p.append(box(x + 96, 172, 48, 26, label='dev', fill=col + '22', stroke=col, fs=10))
        for dx in (-72, -20, 32):
            p.append(box(x + 108 + dx, 218, 36, 22, fill='#ffffff', stroke=LINE, fs=8.5))
            p.append(line(x + 120, 198, x + 126 + dx, 218, LINE, 1))
        p.append(txt(x + 8, 246, 'PC1', size=8, fill=MUTED))
        p.append(txt(x + 60, 246, 'PC2', size=8, fill=MUTED))
        p.append(txt(x + 112, 246, 'PC3', size=8, fill=MUTED))
        p.append(txt(x + 164, 246, 'PC4', size=8, fill=MUTED))
        # domains
        p.append(box(x, 266, 240, 50, fill='#ffffff', stroke=col, lw=1.2, rx=6))
        p.append(txt(x + 120, 286, domains, size=9.5, anchor='middle', weight='bold'))
        p.append(txt(x + 120, 302, extra, size=9, anchor='middle', fill=MUTED))
        x += 250
    p.append(box(30, 332, 730, 56, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(46, 352, 'Memory hook', size=10.5, weight='bold', fill=AMBER))
    p.append(wrap(46, 368, 'Hub: everyone hears everything.  Switch: learns who is where (MAC table).  '
                           'Router: separates networks and stops broadcasts.  Firewall: filters by IP + '
                           'port (and, for NGFW, by application).', size=10, maxw=690))
    return canvas(W, H, p)


# ----------------------------------------------------- 12. TLS handshake -----
def tls_handshake():
    W, H = 790, 470
    p = [title(30, 34, 'TLS Handshake — Simplified but Complete',
               sub='Goal: authenticate the server, then agree on a SYMMETRIC session key')]
    cx, sx = 140, 560
    p.append(box(cx - 66, 80, 132, 38, label='CLIENT (browser)', fill=BLUE_L, stroke=BLUE, fs=11,
                 weight='bold'))
    p.append(box(sx - 76, 80, 152, 38, label='SERVER (website)', fill=TEAL_L, stroke=TEAL, fs=11,
                 weight='bold'))
    p.append(line(cx, 122, cx, 400, BLUE, 1.2, '4 4'))
    p.append(line(sx, 122, sx, 400, TEAL, 1.2, '4 4'))
    steps = [
        ('1', '→', 'ClientHello', 'TLS versions, cipher suites, client random', BLUE),
        ('2', '←', 'ServerHello', 'chosen version + cipher, server random', TEAL),
        ('3', '←', 'Certificate', "server's X.509 cert (public key + identity)", TEAL),
        ('4', '←', 'ServerKeyExchange / HelloDone', 'ECDHE parameters, signed by the CA-backed key', TEAL),
        ('5', '→', 'ClientKeyExchange', 'client ECDHE public value (RSA: premaster, encrypted)', BLUE),
        ('6', '↔', 'ChangeCipherSpec + Finished', 'both sides switch to the derived session key', PURPLE),
        ('7', '↔', 'Application Data', 'encrypted with the fast SYMMETRIC key (AES / ChaCha20)', GREEN),
    ]
    y = 152
    for n, d, name, desc, col in steps:
        if d == '→':
            p.append(arrow(cx, y, sx, y, col, 1.5, 7))
        elif d == '←':
            p.append(arrow(sx, y, cx, y, col, 1.5, 7))
        else:
            p.append(arrow(cx, y, sx, y, col, 1.5, 7))
            p.append(arrow(sx, y + 8, cx, y + 8, col, 1.5, 7))
        p.append(txt((cx + sx) / 2, y - 6, f'{n}. {name}', size=10.5, anchor='middle',
                     weight='bold', fill=col))
        p.append(txt((cx + sx) / 2, y + 12, desc, size=9.5, anchor='middle', fill=MUTED))
        y += 36
    p.append(box(30, 412, 730, 46, fill=PURPLE_L, stroke=PURPLE, rx=6))
    p.append(wrap(46, 430, 'Key point: the browser validates the certificate (issuer, hostname, '
                           'expiry, revocation). The session key is DERIVED by both sides — it is '
                           'never sent over the wire.', size=10, weight='bold', maxw=700))
    p.append(wrap(46, 452, 'ECDHE gives forward secrecy: stealing the server key later does not '
                           'decrypt captured sessions. TLS 1.3 does the exchange in 1 round trip. '
                           'HTTPS = HTTP over TLS on port 443.', size=9.5, fill=MUTED, maxw=700))
    return canvas(W, H, p)


# ---------------------------------------------------------- 13. Crypto -------
def crypto_compare():
    W, H = 780, 380
    p = [title(30, 34, 'Encryption & Hashing — Three Different Tools')]
    panels = [
        ('SYMMETRIC', BLUE, ['Plaintext ──[ same secret key ]──▶ Ciphertext',
                             'Ciphertext ──[ same secret key ]──▶ Plaintext',
                             'Fast • one shared key • key distribution is the problem',
                             'AES, DES/3DES, RC4, ChaCha20']),
        ('ASYMMETRIC', TEAL, ['Plaintext ──[ PUBLIC key ]──▶ Ciphertext',
                              'Ciphertext ──[ PRIVATE key ]──▶ Plaintext',
                              'Slow • solves key exchange • ~100–1000× slower',
                              'RSA, ECC, Diffie–Hellman']),
        ('HASHING', AMBER, ['Message ──[ hash function ]──▶ fixed-length digest',
                            'One-way only — there is NO key that reverses it',
                            'Integrity • password storage (salted!) • signatures',
                            'MD5 (broken), SHA-1 (broken), SHA-256, bcrypt']),
    ]
    x = 30
    for name, col, lines in panels:
        p.append(box(x, 76, 240, 250, fill=col + '14', stroke=col, lw=1.4))
        pill_w, _ = 0, 0
        p.append(box(x + 55, 88, 130, 28, label=name, fill='#ffffff', stroke=col, fs=11.5,
                     weight='bold'))
        yy = 148
        for ln in lines:
            # simple word wrap
            words, cur, out = ln.split(' '), '', []
            for wd in words:
                if tw(cur + ' ' + wd, 9.5) > 212:
                    out.append(cur)
                    cur = wd
                else:
                    cur = (cur + ' ' + wd).strip()
            out.append(cur)
            for o in out:
                p.append(note(x + 14, yy, o, size=9.5, mono=('──' in ln)))
                yy += 15
            yy += 12
        x += 250
    p.append(box(30, 336, 720, 34, fill=RED_L, stroke=RED, rx=6))
    p.append(wrap(46, 352, 'Digital signature = hash the message, encrypt the hash with the signer '
                           'private key — gives integrity + authenticity + non-repudiation (anyone can '
                           'verify with the public key).', size=10, maxw=690))
    return canvas(W, H, p)


# ------------------------------------------------- 14. Shared responsibility -
def cloud_shared_responsibility():
    W, H = 780, 500
    p = [title(30, 34, 'Cloud Shared Responsibility — Who Manages What?',
               sub='Blue = you (customer)    Teal = cloud provider    Grey = shared')]
    rows = [('Applications', 'YOU', 'YOU', 'PROVIDER'),
            ('Data & access control', 'YOU', 'YOU', 'PROVIDER (hosts it)'),
            ('Runtime', 'YOU', 'YOU', 'PROVIDER'),
            ('Middleware', 'YOU', 'YOU', 'PROVIDER'),
            ('Operating system', 'YOU', 'YOU', 'PROVIDER'),
            ('Virtualization', 'YOU', 'PROVIDER', 'PROVIDER'),
            ('Servers', 'YOU', 'PROVIDER', 'PROVIDER'),
            ('Storage', 'YOU', 'PROVIDER', 'PROVIDER'),
            ('Networking', 'YOU', 'PROVIDER', 'PROVIDER')]
    heads = [('Layer', 30, 210), ('On-premises', 250, 130), ('IaaS', 390, 130),
             ('PaaS', 530, 130), ('SaaS', 670, 90)]
    y = 88
    for lbl, hx, hw in heads:
        p.append(box(hx, y, hw, 30, label=lbl, fill=SLATE_L, stroke=SLATE, fs=11, weight='bold'))
    for i, (layer, onprem, iaas, paas) in enumerate(rows):
        yy = y + 30 + i * 30
        p.append(box(30, yy, 210, 28, fill='#ffffff', stroke=LINE, lw=0.8, rx=3))
        p.append(note(40, yy + 19, layer, size=10, weight='bold'))
        for val, (hx, hw) in zip([onprem, iaas, paas], [(h[1], h[2]) for h in heads[1:]]):
            if 'YOU' in val and 'PROVIDER' not in val:
                fill, stroke = BLUE_L, BLUE
            elif 'PROVIDER' in val and 'YOU' not in val:
                fill, stroke = TEAL_L, TEAL
            else:
                fill, stroke = SLATE_L, SLATE
            p.append(box(hx, yy, hw, 28, fill=fill, stroke=stroke, lw=0.8, rx=3))
            p.append(note(hx + 8, yy + 19, val, size=9.5,
                          fill=BLUE if stroke == BLUE else (TEAL if stroke == TEAL else SLATE)))
    y2 = y + 30 + len(rows) * 30 + 16
    p.append(box(30, y2, 730, 76, fill=AMBER_L, stroke=AMBER, rx=6))
    p.append(note(46, y2 + 22, 'Exam lines to remember', size=10.5, weight='bold', fill=AMBER))
    p.append(wrap(46, y2 + 40, 'IaaS = VMs / networks / storage (EC2, Azure VM) — YOU patch the guest '
                               'OS.  PaaS = runtime + middleware managed (App Service, RDS) — you '
                               'deploy code only.', size=10, maxw=690))
    p.append(wrap(46, y2 + 72, 'SaaS = ready-to-use software (Gmail, Salesforce). Serverless/FaaS = '
                               'pay per execution. Never shared: your DATA and who may access it.',
                   size=9.5, fill=MUTED, maxw=690))
    return canvas(W, H, p)


NETWORKING = [
    ('osi-layers', osi_layers),
    ('encapsulation', encapsulation),
    ('tcp-vs-udp', tcp_vs_udp),
    ('tcp-handshake', tcp_handshake),
    ('subnet-math', subnet_math),
    ('ipv4-classes', ip_classes),
    ('nat-pat', nat_pat),
    ('dns-resolution', dns_resolution),
    ('dhcp-dora', dhcp_dora),
    ('arp-resolution', arp_resolution),
    ('devices-domains', devices_domains),
    ('tls-handshake', tls_handshake),
    ('crypto-compare', crypto_compare),
    ('cloud-shared-responsibility', cloud_shared_responsibility),
]
