# IS-IS
## [URL](https://en.wikipedia.org/wiki/IS-IS) - https://en.wikipedia.org/wiki/IS-IS
## Catagories
### All articles with unsourced statements
### Articles with LCCN identifiers
### Articles with short description
### Articles with unsourced statements from February 2013
### ISO standards
### Internet Standards
### Internet protocols
### OSI protocols
### Routing protocols
### Short description is different from Wikidata
### "Intermediate System to Intermediate System  (IS-IS, also written ISIS) is a routing protocol designed to move information efficiently within a computer network, a group of physically connected computers or similar devices. It accomplishes this by determining the best route for data through a packet switching network. 
### The IS-IS protocol is defined in ISO/IEC 10589:2002 as an international standard within the Open Systems Interconnection (OSI) reference design.  The Internet Engineering Task Force (IETF) republished IS-IS in RFC 1142, but that RFC was later marked as historic by RFC 7142 because it republished a draft rather than a final version of the ISO standard, causing confusion. 
### IS-IS has been called \"the de facto standard for large service provider network backbones.\"
## Description  
### IS-IS is an interior gateway protocol, designed for use within an administrative domain or network.  This is in contrast to exterior gateway protocols, primarily Border Gateway Protocol (BGP), which is used for routing between autonomous systems (RFC 1930). 
### IS-IS is a link-state routing protocol, operating by reliably flooding link state information throughout a network of routers. Each IS-IS router independently builds a database of the network's topology, aggregating the flooded network information.  Like the OSPF protocol, IS-IS uses Dijkstra's algorithm for computing the best path through the network.  Packets (datagrams) are then forwarded, based on the computed ideal path, through the network to the destination.
## History  
### The IS-IS protocol was developed by a team of people working at Digital Equipment Corporation as part of DECnet Phase V. It was standardized by the ISO in 1992 as ISO 10589 for communication between network devices that are termed Intermediate Systems (as opposed to end systems or hosts) by the ISO. The purpose of IS-IS was to make possible the routing of datagrams using the ISO-developed OSI protocol stack called CLNS. 
### IS-IS was developed at roughly the same time that the Internet Engineering Task Force IETF was developing a similar protocol called OSPF. IS-IS was later extended to support routing of datagrams in the Internet Protocol (IP), the Network Layer protocol of the global Internet. This version of the IS-IS routing protocol was then called Integrated IS-IS (RFC 1195)
## Packet types  
### IS-IS adjacency can be either broadcast or point-to-point. 

### Hello Packet 
### The IS-IS hello packets needs to be exchanged periodically between 2 routers to establish adjacency. Based on the negotiation, one of them will be selected as DIS (Designated IS). This hello packet will be sent separately for Level-1 or Level-2. 
### LSP 
### This contains the actual route information. This LSP can contain many type\u2013length\u2013values (TLVs). 
### CSNP 
### This packet will be sent only by the DIS. By default for every 10 seconds, CSNP packet will be transmitted by DIS. This will contain the list of LSP IDs along with sequence number and checksum. 
### PSNP 
### If the router which receives CSNP packet finds some discrepancy in its own database, it will send an PSNP request asking the DIS to send specific LSP back to it.
## Comparison with OSPF  
### Both IS-IS and Open Shortest Path First (OSPF) are link-state protocols, and both use the same Dijkstra algorithm for computing the best path through the network. As a result, they are conceptually similar. Both support Classless Inter-Domain Routing, can use multicast to discover neighboring routers using hello packets, and can support authentication of routing updates. 
### OSPF was natively built to route IP and is itself a protocol that runs on top of IP, and OSPFv2 is only able to build IPv4 routing tables. IS-IS is an OSI Layer 3 protocol initially defined for routing CLNP. However, IS-IS is neutral regarding the type of network addresses for which it can route, and was easily extended to support IPv4 routing, using mechanisms described in RFC 1195, and later IPv6 as specified in RFC 5308.  To operate with IPv6 networks, the OSPF protocol was rewritten in OSPF v3 (as specified in RFC 5340). 
### Both OSPF and IS-IS routers build a topological representation of the network. This map indicates the subnets which each IS-IS router can reach, and the lowest-cost (shortest) path to a subnet is used to forward traffic. 
### IS-IS differs from OSPF in the way that \"areas\" are defined and routed between. IS-IS routers are designated as being: Level 1 (intra-area); Level 2 (inter area); or Level 1\u20132 (both). Routing information is exchanged between Level 1 routers and other Level 1 routers of the same area, and Level 2 routers can only form relationships and exchange information with other Level 2 routers. Level 1\u20132 routers exchange information with both levels and are used to connect the inter area routers with the intra area routers. 
### In OSPF, areas are delineated on the interface such that an area border router (ABR) is actually in two or more areas at once, effectively creating the borders between areas inside the ABR, whereas in IS-IS area borders are in between routers, designated as Level 2 or Level 1\u20132. The result is that an IS-IS router is only ever a part of a single area. 
### IS-IS also does not require Area 0 (Area Zero) to be the backbone area through which all inter-area traffic must pass. The logical view is that OSPF creates something of a spider web or star topology of many areas all attached directly to Area Zero and IS-IS, by contrast, creates a logical topology of a backbone of Level 2 routers with branches of Level 1\u20132 and Level 1 routers forming the individual areas. 
### IS-IS also differs from OSPF in the methods by which it reliably floods topology and topology change information through the network. However, the basic concepts are similar.OSPF has a larger set of extensions and optional features specified in the protocol standards. However, IS-IS is easier to expand: its use of TLV data allows engineers to implement support for new techniques without redesigning the protocol. For example, in order to support IPv6, the IS-IS protocol was extended to support a few additional TLVs, whereas OSPF required a new protocol draft (OSPFv3). In addition to that, IS-IS is less \"chatty\" and can scale to support larger networks. Given the same set of resources, IS-IS can support more routers in an area than OSPF. This has contributed to IS-IS as an ISP-scale protocol.The TCP/IP implementation, known as \"Integrated IS-IS\" or \"Dual IS-IS\", is described in RFC 1195.
## Other uses  
### IS-IS is also used as the control plane for IEEE 802.1aq Shortest Path Bridging (SPB).  SPB allows for shortest-path forwarding in an Ethernet mesh network context utilizing multiple equal cost paths.  This permits SPB to support large Layer 2 topologies, with fast convergence, and improved use of the mesh topology.  Combined with this is single point provisioning for logical connectivity membership.  IS-IS is therefore augmented with a small number of TLVs and sub-TLVs, and supports two Ethernet encapsulating data paths, 802.1ad Provider Bridges and 802.1ah Provider Backbone Bridges.  SPB requires no state machine or other substantive changes to IS-IS, and simply requires a new Network Layer Protocol Identifier (NLPID) and set of TLVs.  This extension to IS-IS is defined in the IETF proposed standard RFC 6329.
## Related protocols  
### Fabric Shortest Path First (FSPF) 
### Transparent Interconnect of Lots of Links (TRILL)
## References 
## External links  
### IS-IS standard (ISO/IEC 10589:2002, Second Edition) \u2013 free-of-charge PDF version 
### RFC 1195 \u2013 Use of OSI IS-IS for Routing in TCP/IP and Dual Environments 
### OSPF and IS-IS: A Comparative Anatomy by Dave Katz, Juniper 
### Collection of RFCs pertaining to IS-IS 
### IS-IS and OSPF difference discussion (Vishwas Manral, Manav Bhatia and Yasuhiro Ohara) 
### Google Quagga IS-IS implementation 
### Sample isisd.conf file: used with Quagga"
## Links
### 110 film
### 126 film
### 135 film
### A440 (pitch standard)
### ALGOL 60
### ANSI C
### ANSI escape code
### ASCII
### ASMO 449
### ASN.1
### Abstraction layer
### Accuracy and precision
### Ada Semantic Interface Specification
### Address Resolution Protocol
### Advanced Video Coding
### Antimagnetic watch
### AppleTalk
### Application layer
### ArmSCII
### Asynchronous Transfer Mode
### Autonomous system (Internet)
### Bluetooth
### Border Gateway Protocol
### British Standard Pipe
### Business Process Model and Notation
### C++
### CHILL
### CLNP
### CLNS
### COBOL
### C Sharp (programming language)
### Classless Inter-Domain Routing
### Cloud Infrastructure Management Interface
### Common Criteria
### Common Language Infrastructure
### Common Logic
### Common Object Request Broker Architecture
### Computer Graphics Metafile
### Computer network
### DECnet
### Data link layer
### Datagram
### Datagram Congestion Control Protocol
### De facto standard
### Delivery Multimedia Integration Framework
### Digital Equipment Corporation
### Digital object identifier
### Digital subscriber line
### Dijkstra's algorithm
### Document Style Semantics and Specification Language
### Domain Name System
### Dynamic Host Configuration Protocol
### ECMAScript
### EXPRESS (data modeling language)
### Envelope
### Equal-loudness contour
### Exterior gateway protocol
### External Data Representation
### FDI World Dental Federation notation
### FTAM
### Fabric Shortest Path First
### Fiber Distributed Data Interface
### File Allocation Table
### File Transfer Protocol
### Film speed
### Flowchart
### Frame Relay
### Fuel oil
### G.hn
### Generic Framing Procedure
### Gopher (protocol)
### Graphical Kernel System
### Guidelines for the Definition of Managed Objects
### HTML
### High-Level Data Link Control
### Hole punch
### Horsepower
### Hypertext Transfer Protocol
### I.430
### I.431
### IATF 16949
### IEEE 1394
### IEEE 802.11
### IEEE 802.15
### IEEE 802.16
### IEEE 802.1ad
### IEEE 802.1ah-2008
### IEEE 802.1aq
### IEEE 802.2
### IEEE 802.3
### IETF
### IPX/SPX
### IPsec
### IPv4
### IPv6
### ISBN (identifier)
### ISLISP
### ISO-8859-8-I
### ISO-TimeML
### ISO/IEC 10116
### ISO/IEC 10967
### ISO/IEC 11179
### ISO/IEC 11404
### ISO/IEC 11801
### ISO/IEC 12207
### ISO/IEC 14443
### ISO/IEC 14651
### ISO/IEC 15288
### ISO/IEC 15504
### ISO/IEC 15693
### ISO/IEC 15897
### ISO/IEC 17024
### ISO/IEC 17025
### ISO/IEC 18000
### ISO/IEC 18014
### ISO/IEC 19752
### ISO/IEC 19770
### ISO/IEC 19794-5
### ISO/IEC 20000
### ISO/IEC 2022
### ISO/IEC 21827
### ISO/IEC 27000
### ISO/IEC 27000-series
### ISO/IEC 27001
### ISO/IEC 27002
### ISO/IEC 27005
### ISO/IEC 27006
### ISO/IEC 29110
### ISO/IEC 38500
### ISO/IEC 42010
### ISO/IEC 4909
### ISO/IEC 5218
### ISO/IEC 646
### ISO/IEC 6523
### ISO/IEC 7064
### ISO/IEC 7810
### ISO/IEC 7811
### ISO/IEC 7812
### ISO/IEC 7813
### ISO/IEC 7816
### ISO/IEC 80000
### ISO/IEC 8652
### ISO/IEC 8820-5
### ISO/IEC 8859
### ISO/IEC 8859-1
### ISO/IEC 8859-10
### ISO/IEC 8859-11
### ISO/IEC 8859-12
### ISO/IEC 8859-13
### ISO/IEC 8859-14
### ISO/IEC 8859-15
### ISO/IEC 8859-16
### ISO/IEC 8859-2
### ISO/IEC 8859-3
### ISO/IEC 8859-4
### ISO/IEC 8859-5
### ISO/IEC 8859-6
### ISO/IEC 8859-7
### ISO/IEC 8859-8
### ISO/IEC 8859-9
### ISO/IEC 9126
### ISO/IEC 9529
### ISO/IEC 9797-1
### ISO/IEC 9995
### ISO/IEC TR 12182
### ISO/IEC base media file format
### ISO/IEEE 11073
### ISO/TR 11941
### ISO 1
### ISO 1000
### ISO 10005
### ISO 10006
### ISO 10007
### ISO 10160
### ISO 10161
### ISO 10206
### ISO 10218
### ISO 10303
### ISO 10303-21
### ISO 10303-22
### ISO 10303-28
### ISO 10487
### ISO 10628
### ISO 10962
### ISO 11170
### ISO 11783
### ISO 11784 and ISO 11785
### ISO 11898
### ISO 11940
### ISO 11940-2
### ISO 11992
### ISO 12006
### ISO 12620
### ISO 128
### ISO 13399
### ISO 13406-2
### ISO 13485
### ISO 13490
### ISO 13567
### ISO 13584
### ISO 14000
### ISO 14031
### ISO 1413
### ISO 14224
### ISO 14617
### ISO 14644
### ISO 14698
### ISO 14971
### ISO 15022
### ISO 15189
### ISO 15292
### ISO 15398
### ISO 15686
### ISO 15706-2
### ISO 15919
### ISO 15924
### ISO 15926
### ISO 15926 WIP
### ISO 1629
### ISO 16750
### ISO 17100
### ISO 1745
### ISO 18245
### ISO 19011
### ISO 19092-1
### ISO 19092-2
### ISO 19114
### ISO 19115
### ISO 19136
### ISO 19439
### ISO 19600
### ISO 2
### ISO 20022
### ISO 20121
### ISO 2014
### ISO 2015
### ISO 2033
### ISO 20400
### ISO 2047
### ISO 2145
### ISO 2146
### ISO 21500
### ISO 216
### ISO 217
### ISO 22000
### ISO 22300
### ISO 22395
### ISO 233
### ISO 25178
### ISO 259
### ISO 25964
### ISO 26000
### ISO 26262
### ISO 2709
### ISO 2711
### ISO 2788
### ISO 28000
### ISO 2848
### ISO 2852
### ISO 31
### ISO 31-0
### ISO 31-1
### ISO 31-10
### ISO 31-11
### ISO 31-12
### ISO 31-13
### ISO 31-2
### ISO 31-3
### ISO 31-4
### ISO 31-5
### ISO 31-6
### ISO 31-7
### ISO 31-8
### ISO 31-9
### ISO 31000
### ISO 3103
### ISO 3166
### ISO 3166-1
### ISO 3166-2
### ISO 3166-3
### ISO 3307
### ISO 361
### ISO 37001
### ISO 3864
### ISO 3977
### ISO 4
### ISO 4031
### ISO 4157
### ISO 4165
### ISO 4217
### ISO 428
### ISO 45001
### ISO 5
### ISO 50001
### ISO 518
### ISO 5426
### ISO 5427
### ISO 5428
### ISO 55000
### ISO 56000
### ISO 5775
### ISO 5776
### ISO 5964
### ISO 6344
### ISO 6346
### ISO 6385
### ISO 639
### ISO 639-1
### ISO 639-2
### ISO 639-3
### ISO 639-5
### ISO 639-6
### ISO 6438
### ISO 657
### ISO 668
### ISO 6709
### ISO 690
### ISO 6943
### ISO 7001
### ISO 7002
### ISO 7010
### ISO 7027
### ISO 704
### ISO 7200
### ISO 732
### ISO 7637
### ISO 7736
### ISO 8000
### ISO 8178
### ISO 8373
### ISO 843
### ISO 8501-1
### ISO 8583
### ISO 860
### ISO 8601
### ISO 8691
### ISO 898
### ISO 9
### ISO 9000
### ISO 9241
### ISO 9362
### ISO 9564
### ISO 965
### ISO 9660
### ISO 9897
### ISO 999
### ISO metric screw thread
### Institute of Electrical and Electronics Engineers
### Interior gateway protocol
### International Bank Account Number
### International Organization for Standardization
### International Securities Identification Number
### International Standard Atmosphere
### International Standard Audiovisual Number
### International Standard Book Number
### International Standard Identifier for Libraries and Related Organizations
### International Standard Music Number
### International Standard Musical Work Code
### International Standard Name Identifier
### International Standard Recording Code
### International Standard Serial Number
### International Standard Text Code
### Internet Control Message Protocol
### Internet Engineering Task Force
### Internet Group Management Protocol
### Internet Protocol
### Internet Protocol version 4
### Internetwork Packet Exchange
### Isis (disambiguation)
### Isofix
### JBIG
### JPEG 2000
### JPEG XR
### Kappa number
### Knowledge Discovery Metamodel
### Kunrei-shiki romanization
### LAPB
### Language Of Temporal Ordering Specification
### Layer 2 Tunneling Protocol
### Legal Entity Identifier
### Lexical Markup Framework
### Link-state routing protocol
### Link Access Procedure for Frame Relay
### Linux Standard Base
### List of IEC standards
### List of ISO romanizations
### List of ITU-T V-series recommendations
### List of International Organization for Standardization standards
### Logical link control
### Longitudinal redundancy check
### MIME
### MPEG-21
### MPEG-4
### MPEG-4 Part 11
### MPEG-4 Part 14
### MPEG-4 Part 2
### MPEG-4 Part 3
### Magnetic ink character recognition
### Manufacturing Message Specification
### Market Identifier Code
### MaxiCode
### Medium access control
### Meta-Object Facility
### Motion JPEG 2000
### Multibus
### Multicast
### NETCONF
### Named pipe
### NetBIOS
### Network File System
### Network Layer
### Network News Transfer Protocol
### Network Time Protocol
### Network layer
### O-ring
### OCR-A
### OCR-B
### OSI model
### OSPF
### Object Constraint Language
### Office Open XML
### On-board diagnostics
### OpenDocument
### Open Data Protocol
### Open Document Architecture
### Open Shortest Path First
### Open Systems Interconnection
### Open Virtualization Format
### Optical Transport Network
### PDF/A
### PDF/E
### PDF/UA
### PDF/VT
### PDF/X
### PDF417
### PHIGS
### POSIX
### Packet Layer Protocol
### Packet switching
### Parallel Line Internet Protocol
### Pascal (programming language)
### Passive optical network
### Photographic Activity Test
### Physical layer
### Pinyin
### Plesiochronous digital hierarchy
### Point-to-Point Protocol
### Point-to-Point Tunneling Protocol
### Portable Document Format
### Power take-off
### Presentation layer
### Pretty Good Privacy
### Process Specification Language
### Prolog
### Prontor-Compur
### Protocol stack
### QR code
### Quality function deployment
### RELAX NG
### RFC (identifier)
### RM-ODP
### RS-232
### RS-449
### Real-time Transport Protocol
### Renard series
### Requirements engineering
### Romanization of Armenian
### Romanization of Georgian
### Router (computing)
### Routing
### Routing protocol
### Ruby (programming language)
### SDMX
### SOCKS
### SPDY
### SQL
### STEP-NC
### Salt spray test
### Serial Line Internet Protocol
### Session Announcement Protocol
### Session Initiation Protocol
### Session layer
### Shoe size
### Short Message Peer-to-Peer
### Simple Mail Transfer Protocol
### Simple Network Management Protocol
### Simple Sensor Interface protocol
### Simple feature access
### Software maintenance
### Standard Generalized Markup Language
### Stream Control Transmission Protocol
### Synchronous Data Link Control
### Synchronous optical networking
### TIFF/EP
### TRILL (computing)
### Telnet
### Topic map
### Torx
### Transmission Control Protocol
### Transport layer
### Trusted Platform Module
### Type–length–value
### USB
### Unified Modeling Language
### Universal Coded Character Set
### User Datagram Protocol
### Versatile Video Coding
### Vicat softening point
### Water Resistant mark
### Web Content Accessibility Guidelines
### Whirlpool (hash function)
### X.25
### X.500
### X3D
### XML Metadata Interchange
### Z notation
## References
### [Reference](http://code.google.com/p/google-quagga/source/list?name=is-is) - http://code.google.com/p/google-quagga/source/list?name=is-is
### [Reference](http://www.networksorcery.com/enp/protocol/is-is.htm) - http://www.networksorcery.com/enp/protocol/is-is.htm
### [Reference](http://www.ietf.org/rfc/rfc1195.txt) - http://www.ietf.org/rfc/rfc1195.txt
### [Reference](http://standards.iso.org/ittf/PubliclyAvailableStandards/c030932_ISO_IEC_10589_2002(E).zip) - http://standards.iso.org/ittf/PubliclyAvailableStandards/c030932_ISO_IEC_10589_2002(E).zip
### [Reference](http://www.nada.kth.se/kurser/kth/2D1490/06/hemuppgifter/bhatia-manral-diff-isis-ospf-01.txt.html) - http://www.nada.kth.se/kurser/kth/2D1490/06/hemuppgifter/bhatia-manral-diff-isis-ospf-01.txt.html
### [Reference](https://id.loc.gov/authorities/subjects/sh2002000572) - https://id.loc.gov/authorities/subjects/sh2002000572
### [Reference](https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://www.itu.int/rec/T-REC-X.225-199511-I/en
### [Reference](https://web.archive.org/web/20070928004122/http://svn.dd-wrt.com:8000/dd-wrt/browser/src/router/quagga/isisd/isisd.conf.sample?rev=7215) - https://web.archive.org/web/20070928004122/http://svn.dd-wrt.com:8000/dd-wrt/browser/src/router/quagga/isisd/isisd.conf.sample?rev=7215
### [Reference](https://web.archive.org/web/20140907054246/http://www.nanog.org/meetings/nanog19/presentations/katz.ppt) - https://web.archive.org/web/20140907054246/http://www.nanog.org/meetings/nanog19/presentations/katz.ppt
### [Reference](https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en
### [Reference](https://datatracker.ietf.org/doc/html/rfc1142) - https://datatracker.ietf.org/doc/html/rfc1142
### [Reference](https://datatracker.ietf.org/doc/html/rfc1195) - https://datatracker.ietf.org/doc/html/rfc1195
### [Reference](https://datatracker.ietf.org/doc/html/rfc5308) - https://datatracker.ietf.org/doc/html/rfc5308
### [Reference](https://datatracker.ietf.org/doc/html/rfc5340) - https://datatracker.ietf.org/doc/html/rfc5340
### [Reference](https://datatracker.ietf.org/doc/html/rfc7142) - https://datatracker.ietf.org/doc/html/rfc7142
### [Reference](https://tools.ietf.org/html/rfc6329) - https://tools.ietf.org/html/rfc6329
### [Reference](https://www.iso.org/standard/30932.html) - https://www.iso.org/standard/30932.html
### [Reference](https://www.wikidata.org/wiki/Q1165964#identifiers) - https://www.wikidata.org/wiki/Q1165964#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg) - https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg