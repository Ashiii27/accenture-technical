# 1. Networking, Security & Cloud

---

## 1.1 OSI Model

The OSI (Open Systems Interconnection) model has **7 layers** that describe how data moves from one computer to another over a network. Memorize from Layer 7 (top) to Layer 1 (bottom). A common mnemonic: **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing (Layer 7 → 1: Application, Presentation, Session, Transport, Network, Data Link, Physical).

### Layers, PDUs, and Functions

| # | Layer | PDU | Key Function | Protocols/Devices |
|---|-------|-----|--------------|-------------------|
| 7 | Application | **Data** | User-facing services, end-user applications | HTTP, HTTPS, FTP, SMTP, DNS, DHCP, SSH, Telnet |
| 6 | Presentation | **Data** | Translation, encryption, compression, encoding (JPEG, ASCII, SSL/TLS) | SSL/TLS, JPEG, PNG, MPEG, ASCII |
| 5 | Session | **Data** | Establishes, manages, terminates sessions between apps | NetBIOS, RPC, PPTP |
| 4 | Transport | **Segment** (TCP) / **Datagram** (UDP) | End-to-end reliability, flow control, port addressing | TCP, UDP |
| 3 | Network | **Packet** | Logical addressing (IP), routing between networks | IP (IPv4/IPv6), ICMP, ARP, OSPF, BGP; **Routers**, Layer-3 switches |
| 2 | Data Link | **Frame** | Physical addressing (MAC), error detection (CRC), access to media | Ethernet, PPP, MAC; **Switches**, Bridges, NICs |
| 1 | Physical | **Bit** | Raw bit transmission over physical medium (voltage, radio, light) | Cables (CAT5/6), fiber, Wi-Fi radio, hubs, repeaters |

### Key Memory Hooks
- **PDUs**: "Please Do Not Throw Sausage Pizza Away" → Physical=Bit, Data Link=Frame, Network=Packet, Transport=Segment/Datagram, Session/Presentation/Application=Data.
- **Routers** work at Layer 3, **Switches** at Layer 2, **Hubs** at Layer 1.
- Encryption (SSL/TLS) is technically Presentation layer, though many modern models treat it as part of Application.

---

## 1.2 TCP/IP

### TCP vs UDP

| Feature | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
|---------|-------------------------------------|------------------------------|
| Connection | **Connection-oriented** (must establish connection first) | **Connectionless** |
| Reliability | Reliable — guaranteed delivery, retransmits lost packets | Unreliable — best-effort, no retransmission |
| Ordering | In-order delivery (sequence numbers) | No ordering guarantee |
| Speed | Slower (overhead from handshakes, ACKs) | Faster, low latency |
| Flow/Congestion control | Yes | No |
| Header size | 20–60 bytes | 8 bytes |
| Use cases | Web (HTTP/HTTPS), email (SMTP), file transfer (FTP), SSH | DNS queries, streaming, VoIP, video calls, online gaming, DHCP |

### TCP Three-Way Handshake
1. **SYN**: Client sends `SYN` (synchronize) with sequence number `x` to server.
2. **SYN-ACK**: Server replies with `SYN` (its own seq `y`) and `ACK` of `x+1`.
3. **ACK**: Client sends `ACK` of `y+1`. Connection is now ESTABLISHED.

After this, data transfer begins. Connection teardown uses a 4-way FIN/ACK exchange.

### Common Port Numbers

| Port | Protocol | Transport |
|------|----------|-----------|
| 20 | FTP (data) | TCP |
| 21 | FTP (control) | TCP |
| 22 | SSH (Secure Shell) | TCP |
| 23 | Telnet | TCP |
| 25 | SMTP (sending email) | TCP |
| 53 | DNS | UDP (queries) / TCP (zone transfers) |
| 67 | DHCP server | UDP |
| 68 | DHCP client | UDP |
| 69 | TFTP | UDP |
| 80 | HTTP | TCP |
| 110 | POP3 (receiving email) | TCP |
| 143 | IMAP (receiving email) | TCP |
| 443 | HTTPS (HTTP over TLS) | TCP |
| 3306 | MySQL | TCP |
| 3389 | RDP | TCP |

Mnemonic for exam: "**H**ere's **T**o **N**ever **F**inding **S**anta's **D**irty **D**ogs **H**iding" — 80 HTTP, 23 Telnet, 20/21 FTP, 25 SMTP, 22 SSH, 53 DNS, 67/68 DHCP, 443 HTTPS.

---

## 1.3 IP Addressing

### IPv4 Address Classes (classful, historical but still tested)

| Class | First octet range | Default subnet | Purpose |
|-------|-------------------|----------------|---------|
| A | 1 – 126 | 255.0.0.0 (/8) | Large networks; first octet is network |
| B | 128 – 191 | 255.255.0.0 (/16) | Medium networks |
| C | 192 – 223 | 255.255.255.0 (/24) | Small networks |
| D | 224 – 239 | — | Multicast |
| E | 240 – 255 | — | Reserved/experimental |

- **127.x.x.x** is the **loopback** range (e.g., 127.0.0.1 for localhost).
- **0.0.0.0** means "any address" / default route.
- **255.255.255.255** is the limited broadcast address.

### Subnet Masking and CIDR
- A **subnet mask** is a 32-bit number of contiguous 1s followed by 0s separating the network and host portions.
  - Example: 255.255.255.0 → first 24 bits are network, last 8 are host.
- **CIDR (Classless Inter-Domain Routing)** notation appends `/prefix_length`, e.g., `192.168.1.0/24`.
- `/24` gives 2⁸−2 = **254 usable hosts** (subtract network and broadcast addresses).
- `/30` gives 2 usable hosts (used for point-to-point links).

### Private IP Ranges (RFC 1918) — NOT routable on the public Internet

| Class | Range | CIDR |
|-------|-------|------|
| A | 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 |
| B | 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 |
| C | 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |

### IPv4 vs IPv6

| Feature | IPv4 | IPv6 |
|---------|------|------|
| Address size | 32-bit (≈4.3 billion) | 128-bit (≈3.4×10³⁸) |
| Notation | Dotted decimal, e.g. 192.168.1.1 | Hex colon, e.g. 2001:0db8::1 |
| NAT | Required (address shortage) | Typically not needed |
| Security | IPSec optional | IPSec built-in |
| Broadcast | Uses broadcast | No broadcast, uses multicast/anycast |
| Header | Variable (20–60 bytes) | Fixed 40 bytes, simpler routing |
| DHCP | DHCPv4 (or static) | DHCPv6 or SLAAC (auto-config) |

### NAT and PAT
- **NAT (Network Address Translation)** maps private IPs inside a network to a public IP (and vice versa) at the router. Hides internal addresses and conserves public IPv4 space.
- **PAT (Port Address Translation)** a.k.a. NAT Overload — maps *many* private IPs to *one* public IP using different source port numbers. This is the NAT used in most home routers.

---

## 1.4 Protocols

### DNS (Domain Name System — UDP/53, TCP/53 for zone transfers)
Translates human-readable domain names (e.g., `www.example.com`) into IP addresses (e.g., `93.184.216.34`).
- **Resolver** (your ISP/device) → **Root server** → **TLD server** (.com) → **Authoritative server** (example.com) → returns IP.
- Types of records: **A** (IPv4), **AAAA** (IPv6), **CNAME** (alias), **MX** (mail), **NS** (name server), **PTR** (reverse DNS).

### DHCP (Dynamic Host Configuration Protocol — UDP 67/68)
Assigns IP addresses automatically to clients. Four-step process called **DORA**:
1. **Discover** — client broadcasts looking for a DHCP server.
2. **Offer** — server offers an IP lease.
3. **Request** — client requests that IP.
4. **Acknowledge** — server confirms and assigns IP, subnet mask, default gateway, DNS servers.

### ARP (Address Resolution Protocol)
Maps a known **IP address** to its corresponding **MAC address** on the same LAN. The device broadcasts "Who has 192.168.1.5?" and the owner replies "I am, MAC aa:bb:cc:dd:ee:ff". Results are cached in the **ARP table**.
- **RARP** (Reverse ARP) does the opposite: MAC → IP (rare today, replaced by DHCP).

### ICMP (Internet Control Message Protocol)
Used for error reporting and diagnostics. **Ping** sends ICMP Echo Request; recipient replies with ICMP Echo Reply. **Traceroute** (or `tracert`) uses ICMP TTL-exceeded messages to discover the path/hops to a destination.

### HTTP vs HTTPS

| Feature | HTTP | HTTPS |
|---------|------|-------|
| Port | 80 | 443 |
| Encryption | None (plaintext) | Encrypted with TLS/SSL |
| Security | Vulnerable to eavesdropping/MITM | Authenticates server, encrypts payload |
| URL prefix | http:// | https:// |
| Nature | Stateless, request-response | Same model, over secure channel |

Both HTTP and HTTPS are **stateless** — each request is independent; cookies/sessions maintain state on top.

---

## 1.5 Network Devices

### Hub vs Switch vs Router vs Firewall

| Device | OSI Layer | Function | Collision/Broadcast Domains |
|--------|-----------|----------|-----------------------------|
| **Hub** | 1 (Physical) | Dumb repeater; broadcasts every frame to every port | 1 collision domain, 1 broadcast domain |
| **Switch** | 2 (Data Link) | Forwards frames based on MAC address using a MAC table | 1 collision domain **per port**, 1 broadcast domain |
| **Router** | 3 (Network) | Forwards packets between different networks based on IP | Separates broadcast domains; uses routing table |
| **Firewall** | 3–7 | Filters traffic based on rules (IPs, ports, applications) | Depends on type |

### MAC Address Table (Switch)
The switch learns MAC-to-port mappings as frames arrive. When a frame with destination MAC unknown arrives, the switch **floods** it out all ports except the ingress port. The target host replies, the switch learns its port, and future frames are forwarded directly (unicast) instead of flooded.

### Routing Table (Router)
Contains entries: **Destination network, Next-hop IP, Exit interface, Metric**. Longest-prefix-match wins. Routes can be **static** (manually entered) or from dynamic protocols (OSPF, BGP, EIGRP). The **default route** (0.0.0.0/0) is used when nothing else matches.

### VLANs (Virtual LANs)
Logically segment a single physical switch into multiple broadcast domains. Benefits:
- Isolates traffic (security).
- Groups users by department/function regardless of physical location.
- Reduces unnecessary broadcast traffic.
- Trunk ports carry traffic for multiple VLANs using **802.1Q tagging**.

---

## 1.6 Security Concepts

### CIA Triad
The foundation of information security:
- **Confidentiality** — only authorized parties can access data (encryption, access control).
- **Integrity** — data is not tampered with (hashing, checksums, digital signatures).
- **Availability** — data/services are accessible when needed (redundancy, backups, DoS protection).

### Common Attack Types

| Attack | Description |
|--------|-------------|
| **DoS** | Denial of Service — overwhelm a target with traffic from one source to make it unavailable. |
| **DDoS** | Distributed DoS — traffic from thousands of compromised hosts (botnet), much harder to stop. |
| **MITM** | Man-in-the-Middle — attacker secretly intercepts/relays communications (e.g., ARP spoofing on Wi-Fi). |
| **Phishing** | Deceptive emails/sites that trick users into revealing credentials or installing malware. |
| **SQL Injection** | Inserting malicious SQL into input fields to read/modify/delete a database. |
| **XSS (Cross-Site Scripting)** | Injecting malicious JavaScript into web pages viewed by other users. |
| **Brute Force** | Trying every possible password/key until the right one is found. |
| **Replay Attack** | Capturing valid data and retransmitting it later to impersonate a user. |
| **Spoofing** | Faking identity (IP spoofing, email spoofing, MAC spoofing) to impersonate someone else. |

### Firewall Types
1. **Packet-filtering** (stateless) — inspect individual packets based on IP/port/protocol (Layer 3/4), cheap and fast.
2. **Stateful** — tracks active connections/sessions; allows replies automatically; the most common today.
3. **Application layer (Proxy / Next-Gen)** — inspects packet content up to Layer 7 (URLs, application data); deep packet inspection.

### IDS vs IPS
- **IDS (Intrusion Detection System)** — monitors and *alerts* on suspicious traffic; does not block. Passive.
- **IPS (Intrusion Prevention System)** — detects and *actively blocks/drops* malicious traffic in-line. Active.

### VPN (Virtual Private Network)
Creates an encrypted tunnel over an untrusted network (Internet).
- **Site-to-Site VPN** — connects two entire networks (e.g., branch office to HQ), typically using IPsec.
- **Remote Access VPN** — individual user connects to the corporate network from outside (e.g., OpenVPN, SSL VPN, Cisco AnyConnect).
- **Tunneling** encapsulates packets (e.g., GRE, IPsec, or TLS wrapping) so private traffic can traverse the public Internet securely.

### AAA Framework
- **Authentication** — who are you? (passwords, biometrics, MFA)
- **Authorization** — what are you allowed to do? (permissions, ACLs, RBAC)
- **Accounting** — what did you do? (logs, audit trails, billing)

Common AAA protocols: RADIUS, TACACS+.

### Multi-Factor Authentication (MFA)
Requires two or more of:
1. Something you **know** (password, PIN)
2. Something you **have** (phone, token, smart card)
3. Something you **are** (fingerprint, face, iris — biometrics)

MFA defeats many password-only attacks (phishing, credential stuffing, brute force).

---

## 1.7 Cryptography

### Symmetric vs Asymmetric Encryption

| Feature | Symmetric | Asymmetric |
|---------|-----------|------------|
| Keys | **Same key** encrypts & decrypts | **Key pair**: public key encrypts, private key decrypts (or vice versa for signing) |
| Speed | Fast (good for bulk data) | Slow (used for key exchange / signatures) |
| Key distribution problem | Yes — must securely share the secret key | No — public key can be freely distributed |
| Examples | **AES, DES, 3DES, Blowfish, RC4** | **RSA, ECC, DSA, ElGamal** |

### Public vs Private Key Roles
- **Public key** — shared openly; used to encrypt data that only the holder of the private key can decrypt, or to verify signatures.
- **Private key** — kept secret; used to decrypt data or to create digital signatures.

### Hashing vs Encryption

| Hashing | Encryption |
|---------|------------|
| **One-way** (cannot reverse to original) | Reversible with the right key |
| Produces fixed-size digest (e.g., SHA-256 → 256 bits) | Produces variable-size ciphertext |
| Used for integrity checks (passwords stored as hashes, file checksums) | Used for confidentiality |
| Examples: MD5, SHA-1, SHA-256, SHA-3, bcrypt | Examples: AES, RSA, DES, 3DES |

### Common Algorithms
- **AES** — Symmetric block cipher; key sizes 128/192/256 bits; current U.S. government standard.
- **DES** — Old symmetric (56-bit key), broken; replaced by 3DES then AES.
- **RSA** — Asymmetric; based on factoring large primes; used for key exchange and signatures.
- **MD5** — Hash, 128-bit output; **broken** (collisions found); do not use for security.
- **SHA-256** — Hash, 256-bit output; part of SHA-2 family; widely used (Bitcoin, TLS, file integrity).

### Digital Signatures & Certificates
- **Digital signature** = sender hashes the message, then encrypts the hash with their **private key**. Anyone with the sender's **public key** can decrypt the hash and verify both integrity and authenticity.
- **Digital certificate** (X.509) binds a public key to an identity (domain/organization). Issued by a **Certificate Authority (CA)** like Let's Encrypt, DigiCert, etc. Prevents MITM by establishing trust chains.

### SSL/TLS Handshake (simplified)
1. Client sends `ClientHello` (supported cipher suites, random number).
2. Server responds `ServerHello`, sends its **certificate** (with public key), selects cipher suite.
3. Client verifies certificate, generates a **premaster secret**, encrypts it with server's public key, sends to server.
4. Both sides derive a shared **session key** from the premaster secret.
5. `Finished` messages exchanged, encrypted with session key — symmetric encryption is used for the rest of the session.

TLS replaced SSL (SSL 3.0 is deprecated/insecure). Modern TLS = TLS 1.2/1.3.

---

## 1.8 Cloud Computing

### Service Models

| Model | What the customer manages | What the provider manages | Examples |
|-------|---------------------------|---------------------------|----------|
| **IaaS** (Infrastructure) | Apps, data, runtime, OS | Virtualization, servers, storage, networking | **AWS EC2, Azure VMs, GCP Compute Engine** |
| **PaaS** (Platform) | Apps, data | Runtime, OS, virtualization, servers, networking | **Azure App Service, AWS Elastic Beanstalk, Heroku, Google App Engine** |
| **SaaS** (Software) | Just the user/data | Everything else (app, runtime, OS, infra) | **Gmail, Salesforce, Microsoft 365, Netflix, Zoom** |

Mnemonic: IaaS = you rent a house; PaaS = you rent an apartment (building managed); SaaS = you stay in a hotel (everything provided).

### Deployment Models
- **Public cloud** — shared infrastructure, owned by provider (AWS, Azure, GCP), pay-as-you-go.
- **Private cloud** — dedicated to one organization (on-prem or hosted); more control/compliance.
- **Hybrid cloud** — mix of public and private connected together; workloads move between them.
- (Community, Multi-cloud are variants.)

### Advantages of Cloud
- **Scalability** — scale up/down resources as load changes (vertical = bigger machine; horizontal = more machines).
- **Elasticity** — automatically add/remove resources to match current demand (auto-scaling groups).
- **Pay-as-you-go** — pay only for what you consume (no upfront capital expense).
- High availability, global reach, disaster recovery options, rapid deployment.

### Virtualization & Hypervisors
- **Virtualization** lets one physical machine run multiple "virtual machines" (VMs) that behave like independent computers.
- **Hypervisor** = software layer that manages VMs.
  - **Type 1 (Bare-metal)** — runs directly on hardware; used in data centers. Examples: VMware ESXi, Microsoft Hyper-V, KVM, Xen.
  - **Type 2 (Hosted)** — runs on top of a host OS as an application. Examples: VMware Workstation/Fusion, VirtualBox, Parallels.

### Containers vs VMs
- **VMs** virtualize the hardware — each VM has its own full guest OS; heavy isolation but large overhead.
- **Containers** virtualize the OS — they share the host kernel but have isolated userspace; lightweight, fast to start. Docker is the most common container platform; Kubernetes orchestrates containers at scale.

### Basic AWS/Azure/GCP Services (concept level)
- **Compute**: AWS EC2, Azure VM, GCP Compute Engine (IaaS VMs); AWS Lambda/Azure Functions/GCP Cloud Functions (serverless Functions-as-a-Service).
- **Storage**: AWS S3, Azure Blob Storage, GCP Cloud Storage (object storage); AWS EBS (block storage for VMs).
- **Database**: AWS RDS, Azure SQL, GCP Cloud SQL (managed relational DB); AWS DynamoDB (NoSQL).
- **Networking**: AWS VPC, Azure VNet (virtual private networks); ELB/ALB, Azure Load Balancer (load balancing); Route 53 (DNS).
- **CDN**: CloudFront, Azure CDN, Cloud CDN.

---

# Practice Questions — Networking, Security & Cloud

**(Answers at the end)**

### OSI Model
1. At which OSI layer do routers operate?
   a) Data Link  b) Network  c) Transport  d) Session
2. Which PDU is associated with the Transport layer?
   a) Bit  b) Frame  c) Packet  d) Segment
3. HTTP operates at which layer?
   a) Application  b) Presentation  c) Session  d) Transport
4. Switches operate at Layer ___ and use ___ addresses.
   a) 2, MAC  b) 3, IP  c) 1, Port  d) 2, IP
5. Which layer is responsible for encryption and data format translation?
   a) Application  b) Presentation  c) Session  d) Transport

### TCP/IP & Ports
6. Which protocol is connection-oriented and guarantees delivery?
   a) UDP  b) ICMP  c) TCP  d) IP
7. HTTPS runs on port:
   a) 22  b) 80  c) 443  d) 53
8. DNS primarily uses which transport protocol for lookups?
   a) TCP  b) UDP  c) ICMP  d) ARP
9. What is the correct order of the TCP three-way handshake?
   a) ACK, SYN, SYN-ACK  b) SYN, ACK, FIN  c) SYN, SYN-ACK, ACK  d) SYN, FIN, ACK
10. Which two ports does DHCP use?
    a) 20/21  b) 67/68  c) 80/443  d) 22/23

### IP Addressing
11. Which of the following is a Class C private address range?
    a) 10.0.0.0/8  b) 172.16.0.0/12  c) 192.168.0.0/16  d) 127.0.0.0/8
12. How many usable host addresses are in a /24 subnet?
    a) 256  b) 255  c) 254  d) 128
13. 127.0.0.1 is a(n) ___ address.
    a) private  b) loopback  c) public  d) multicast
14. Which is NOT true about IPv6?
    a) 128-bit addresses  b) Uses broadcast for delivery  c) Has IPSec built-in  d) Uses hex-colon notation
15. PAT (NAT Overload) primarily helps with:
    a) Encrypting traffic  b) IPv4 address conservation  c) Routing between VLANs  d) DNS resolution

### Protocols
16. The DHCP four-step process is:
    a) Discover, Offer, Request, Acknowledge  b) Discover, Reply, Request, Accept  c) SYN, SYN-ACK, ACK, FIN  d) Query, Offer, Ack, Done
17. ARP resolves:
    a) Domain name to IP  b) IP to MAC  c) MAC to port  d) Port to service
18. Which protocol is used by the `ping` command?
    a) TCP  b) UDP  c) ICMP  d) ARP
19. Which DNS record type maps a hostname to an IPv4 address?
    a) AAAA  b) MX  c) A  d) CNAME
20. Which of the following is stateless?
    a) TCP  b) HTTP  c) UDP and HTTP  d) Neither

### Network Devices
21. Which device creates a single collision domain and a single broadcast domain, repeating signals out all ports?
    a) Switch  b) Router  c) Hub  d) Firewall
22. A switch forwards frames based on:
    a) IP address  b) MAC address  c) Port number  d) Hostname
23. VLANs are used primarily to:
    a) Speed up Internet access  b) Segment broadcast domains  c) Replace routers  d) Encrypt traffic
24. A router operates at Layer ___ and separates ___ domains.
    a) 2, collision  b) 3, broadcast  c) 3, collision  d) 4, routing
25. When a switch doesn't know the destination MAC, it ___ the frame.
    a) drops  b) floods  c) routes  d) encrypts

### Security
26. Which part of the CIA triad ensures data is not altered by unauthorized parties?
    a) Confidentiality  b) Integrity  c) Availability  d) Authentication
27. An attack that overwhelms a target from many compromised machines is:
    a) DoS  b) Phishing  c) DDoS  d) Spoofing
28. Injecting malicious SQL through an input field is called:
    a) XSS  b) CSRF  c) SQL Injection  d) MITM
29. An IDS:
    a) Blocks attacks in-line  b) Only detects and alerts  c) Encrypts traffic  d) Replaces firewalls
30. Which of the following requires something you know AND something you have?
    a) Password  b) Biometrics  c) MFA  d) Firewall

### Cryptography
31. Which is an asymmetric encryption algorithm?
    a) AES  b) DES  c) RSA  d) Blowfish
32. Hashing is primarily used for:
    a) Confidentiality  b) Integrity verification  c) Key exchange  d) Speed
33. Which hash algorithm produces a 256-bit digest?
    a) MD5  b) SHA-1  c) SHA-256  d) DES
34. In asymmetric cryptography, what is used to encrypt a message so only the recipient can read it?
    a) Sender's private key  b) Sender's public key  c) Recipient's public key  d) Recipient's private key
35. Digital signatures provide:
    a) Confidentiality only  b) Integrity and authentication  c) Compression  d) Routing

### Cloud
36. AWS EC2 is an example of:
    a) IaaS  b) PaaS  c) SaaS  d) FaaS
37. Gmail is an example of:
    a) IaaS  b) PaaS  c) SaaS  d) XaaS
38. Which hypervisor type runs directly on hardware?
    a) Type 1  b) Type 2  c) Type 3  d) Hosted
39. Containers differ from VMs mainly because:
    a) They use a separate kernel per container  b) They share the host OS kernel  c) They cannot run on Linux  d) They are slower
40. Auto-scaling that adds or removes resources automatically based on demand demonstrates:
    a) Rigidity  b) Elasticity  c) Static hosting  d) Latency

---

## Answer Key — Networking, Security & Cloud

1. b | 2. d | 3. a | 4. a | 5. b
6. c | 7. c | 8. b | 9. c | 10. b
11. c | 12. c | 13. b | 14. b | 15. b
16. a | 17. b | 18. c | 19. c | 20. c
21. c | 22. b | 23. b | 24. b | 25. b
26. b | 27. c | 28. c | 29. b | 30. c
31. c | 32. b | 33. c | 34. c | 35. b
36. a | 37. c | 38. a | 39. b | 40. b
