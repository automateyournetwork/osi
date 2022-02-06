# Internet Protocol
## [URL](https://en.wikipedia.org/wiki/Internet_Protocol) - https://en.wikipedia.org/wiki/Internet_Protocol
## Catagories
### All articles containing potentially dated statements
### All articles with failed verification
### Articles containing potentially dated statements from September 2021
### Articles with GND identifiers
### Articles with failed verification from January 2022
### Articles with short description
### CS1 errors: missing periodical
### Internet
### Internet Protocol
### Internet layer protocols
### Short description is different from Wikidata
### "The Internet Protocol (IP) is the network layer communications protocol in the Internet protocol suite for relaying datagrams across network boundaries. Its routing function enables internetworking, and essentially establishes the Internet. 
### IP has the task of delivering packets from the source host to the destination host solely based on the IP addresses in the packet headers. For this purpose, IP defines packet structures that encapsulate the data to be delivered.  It also defines addressing methods that are used to label the datagram with source and destination information. 
### IP was the connectionless datagram service in the original Transmission Control Program introduced by Vint Cerf and Bob Kahn in 1974, which was complemented by a connection-oriented service that became the basis for the Transmission Control Protocol (TCP). The Internet protocol suite is therefore often referred to as TCP/IP. 
### The first major version of IP, Internet Protocol Version 4 (IPv4), is the dominant protocol of the Internet. Its successor is Internet Protocol Version 6 (IPv6), which has been in increasing deployment on the public Internet since c. 2006.
## Function  

### The Internet Protocol is responsible for addressing host interfaces, encapsulating data into datagrams (including fragmentation and reassembly) and routing datagrams from a source host interface to a destination host interface across one or more IP networks. For these purposes, the Internet Protocol defines the format of packets and provides an addressing system. 
### Each datagram has two components: a header and a payload. The IP header includes source IP address, destination IP address, and other metadata needed to route and deliver the datagram. The payload is the data that is transported. This method of nesting the data payload in a packet with a header is called encapsulation. 
### IP addressing entails the assignment of IP addresses and associated parameters to host interfaces. The address space is divided into subnetworks, involving the designation of network prefixes. IP routing is performed by all hosts, as well as routers, whose main function is to transport packets across network boundaries. Routers communicate with one another via specially designed routing protocols, either interior gateway protocols or exterior gateway protocols, as needed for the topology of the network.
## Version history  

### In May 1974, the Institute of Electrical and Electronics Engineers (IEEE) published a paper entitled \"A Protocol for Packet Network Intercommunication\". The paper's authors, Vint Cerf and Bob Kahn, described an internetworking protocol for sharing resources using packet switching among network nodes. A central control component of this model was the \"Transmission Control Program\" that incorporated both connection-oriented links and datagram services between hosts. The monolithic Transmission Control Program was later divided into a modular architecture consisting of the Transmission Control Protocol and User Datagram Protocol at the transport layer and the Internet Protocol at the internet layer. The model became known as the Department of Defense (DoD) Internet Model and Internet protocol suite, and informally as TCP/IP. 
### IP versions 1 to 3 were experimental versions, designed between 1973 and 1978. The following Internet Experiment Note (IEN) documents describe version 3 of the Internet Protocol, prior to the modern version of IPv4: 

### IEN 2 (Comments on Internet Protocol and TCP), dated August 1977 describes the need to separate the TCP and Internet Protocol functionalities (which were previously combined.)  It proposes the first version of the IP header, using 0 for the version field. 
### IEN 26 (A Proposed New Internet Header Format), dated February 1978 describes a version of the IP header that uses a 1-bit version field. 
### IEN 28 (Draft Internetwork Protocol Description Version 2), dated February 1978 describes IPv2. 
### IEN 41 (Internetwork Protocol Specification Version 4), dated June 1978 describes the first protocol to be called IPv4.  The IP header is different from the modern IPv4 header. 
### IEN 44 (Latest Header Formats), dated June 1978 describes another version of IPv4, also with a header different from the modern IPv4 header. 
### IEN 54 (Internetwork Protocol Specification Version 4), dated September 1978 is the first description of IPv4 using the header that would be standardized in RFC 760.The dominant internetworking protocol in the Internet Layer in use is IPv4; the number 4 identifies the protocol version, carried in every IP datagram. IPv4 is described in RFC 791 (1981). 
### Version number 5 was used by the Internet Stream Protocol, an experimental streaming protocol that was not adopted.The successor to IPv4 is IPv6. IPv6 was a result of several years of experimentation and dialog during which various protocol models were proposed, such as TP/IX (RFC 1475), PIP (RFC 1621) and TUBA (TCP and UDP with Bigger Addresses, RFC 1347). Its most prominent difference from version 4 is the size of the addresses. While IPv4 uses 32 bits for addressing, yielding c. 4.3 billion (4.3\u00d7109) addresses, IPv6 uses 128-bit addresses providing ca. 3.4\u00d71038 addresses. Although adoption of IPv6 has been slow, as of September 2021, most countries in the world show significant adoption of IPv6, with over 35% of Google's traffic being carried over IPv6 connections.The assignment of the new protocol as IPv6 was uncertain until due diligence assured that IPv6 had not been used previously. Other Internet Layer protocols have been assigned version numbers, such as 7 (IP/TX), 8 and 9 (historic). Notably, on April 1, 1994, the IETF published an April Fools' Day joke about IPv9. IPv9 was also used in an alternate proposed address space expansion called TUBA. A 2004 Chinese proposal for an \"IPv9\" protocol appears to be unrelated to all of these, and is not endorsed by the IETF.
## Reliability  
### The design of the Internet protocol suite adheres to the end-to-end principle, a concept adapted from the CYCLADES project. Under the end-to-end principle, the network infrastructure is considered inherently unreliable at any single network element or transmission medium and is dynamic in terms of the availability of links and nodes. No central monitoring or performance measurement facility exists that tracks or maintains the state of the network. For the benefit of reducing network complexity, the intelligence in the network is purposely located in the end nodes.As a consequence of this design, the Internet Protocol only provides best-effort delivery and its service is characterized as unreliable. In network architectural parlance, it is a connectionless protocol, in contrast to connection-oriented communication. Various fault conditions may occur, such as data corruption, packet loss and duplication. Because routing is dynamic, meaning every packet is treated independently, and because the network maintains no state based on the path of prior packets, different packets may be routed to the same destination via different paths, resulting in out-of-order delivery to the receiver. 
### All fault conditions in the network must be detected and compensated by the participating end nodes. The upper layer protocols of the Internet protocol suite are responsible for resolving reliability issues. For example, a host may buffer network data to ensure correct ordering before the data is delivered to an application. 
### IPv4 provides safeguards to ensure that the header of an IP packet is error-free. A routing node discards packets that fail a header checksum test. Although the Internet Control Message Protocol (ICMP) provides notification of errors, a routing node is not required to notify either end node of errors. IPv6, by contrast, operates without header checksums, since current link layer technology is assumed to provide sufficient error detection.
## Link capacity and capability  
### The dynamic nature of the Internet and the diversity of its components provide no guarantee that any particular path is actually capable of, or suitable for, performing the data transmission requested. One of the technical constraints is the size of data packets possible on a given link. Facilities exist to examine the maximum transmission unit (MTU) size of the local link and Path MTU Discovery can be used for the entire intended path to the destination.The IPv4 internetworking layer automatically fragments a datagram into smaller units for transmission when the link MTU is exceeded. IP provides re-ordering of fragments received out of order. An IPv6 network does not perform fragmentation in network elements, but requires end hosts and higher-layer protocols to avoid exceeding the path MTU.The Transmission Control Protocol (TCP) is an example of a protocol that adjusts its segment size to be smaller than the MTU. The User Datagram Protocol (UDP) and ICMP disregard MTU size, thereby forcing IP to fragment oversized datagrams.
## Security  
### During the design phase of the ARPANET and the early Internet, the security aspects and needs of a public, international network could not be adequately anticipated.  Consequently, many Internet protocols exhibited vulnerabilities highlighted by network attacks and later security assessments.  In 2008, a thorough security assessment and proposed mitigation of problems was published. The IETF has been pursuing further studies.
## See also  

### ICANN 
### IP routing 
### List of IP protocol numbers 
### Next-generation network
## References 
## External links  
### Manfred Lindner. \"IP Technology\" (PDF). Retrieved 2018-02-11. 
### Manfred Lindner. \"IP Routing\" (PDF). Retrieved 2018-02-11."
## Links
### 1,000,000,000 (number)
### 128-bit
### 32-bit
### ARPANET
### Address Resolution Protocol
### Application layer
### April Fools' Day
### Arbor Networks
### Best-effort delivery
### Bob Kahn
### Border Gateway Protocol
### CYCLADES
### Centre for the Protection of National Infrastructure
### Checksum
### Communications protocol
### Comparison of IPv6 support in common applications
### Comparison of IPv6 support in operating systems
### Connection-oriented communication
### Connectionless communication
### Connectionless protocol
### DHCPv6
### Data buffer
### Data corruption
### Datagram
### Datagram Congestion Control Protocol
### Doi (identifier)
### Domain Name System
### Dynamic Host Configuration Protocol
### Encapsulation (networking)
### End-to-end principle
### End node
### Explicit Congestion Notification
### Exterior gateway protocol
### File Transfer Protocol
### HTTPS
### Header (computing)
### Host (network)
### Host interface
### Hypertext Transfer Protocol
### ICANN
### IETF
### IP address
### IP fragmentation
### IP header
### IP routing
### IPsec
### IPv4
### IPv4 address exhaustion
### IPv6
### IPv6 address
### IPv6 deployment
### IPv6 packet
### IPv6 transition mechanism
### IPv9 (China)
### ISBN (identifier)
### ISSN (identifier)
### Institute of Electrical and Electronics Engineers
### Interior gateway protocol
### Internet
### Internet Control Message Protocol
### Internet Control Message Protocol for IPv6
### Internet Experiment Note
### Internet Group Management Protocol
### Internet Layer
### Internet Message Access Protocol
### Internet Stream Protocol
### Internet layer
### Internet protocol suite
### Internetworking
### Lightweight Directory Access Protocol
### Link layer
### List of IP protocol numbers
### List of IPv6 tunnel brokers
### MQTT
### Maximum transmission unit
### Media Gateway Control Protocol
### Medium access control
### Mobile IP
### Multicast Listener Discovery
### Multicast router discovery
### Neighbor Discovery Protocol
### Network News Transfer Protocol
### Network Time Protocol
### Network complexity
### Network layer
### Network node
### Next-generation network
### NortonLifeLock
### Open Network Computing Remote Procedure Call
### Open Shortest Path First
### Out-of-order delivery
### PRNET
### Packet (information technology)
### Packet loss
### Packet switching
### Path MTU Discovery
### Payload (computing)
### Point-to-Point Protocol
### Post Office Protocol
### Precision Time Protocol
### QUIC
### RFC (identifier)
### Real-time Transport Protocol
### Real Time Streaming Protocol
### Reliability (computer networking)
### Resource Reservation Protocol
### Router (computing)
### Routing
### Routing Information Protocol
### Routing protocol
### SATNET
### Secure Neighbor Discovery
### Secure Shell
### Session Initiation Protocol
### Simple Mail Transfer Protocol
### Simple Network Management Protocol
### Site Multihoming by IPv6 Intermediation
### Stream Control Transmission Protocol
### Subnetwork
### Telnet
### Transmission Control Protocol
### Transport Layer Security
### Transport layer
### Tunneling protocol
### Upper layer protocol
### User Datagram Protocol
### Vint Cerf
### World IPv6 Day and World IPv6 Launch Day
### XMPP
## References
### [Reference](http://archive.oreilly.com/cs/user/view/cs_msg/25036) - http://archive.oreilly.com/cs/user/view/cs_msg/25036
### [Reference](http://www.symantec.com/connect/articles/basic-journey-packet) - http://www.symantec.com/connect/articles/basic-journey-packet
### [Reference](http://www.tcpipguide.com/free/t_IPFunctions.htm) - http://www.tcpipguide.com/free/t_IPFunctions.htm
### [Reference](http://doi.org/10.1109%2FTCOM.1974.1092259) - http://doi.org/10.1109%2FTCOM.1974.1092259
### [Reference](http://doi.org/10.17487%2FRFC1347) - http://doi.org/10.17487%2FRFC1347
### [Reference](http://doi.org/10.17487%2FRFC6274) - http://doi.org/10.17487%2FRFC6274
### [Reference](http://doi.org/10.1787%2F5jxt46d07bhc-en) - http://doi.org/10.1787%2F5jxt46d07bhc-en
### [Reference](http://www.eitc.org/research-opportunities/future-internet-and-optical-quantum-communications/internet-networks-and-tcp-ip/ip-technologies-and-migration) - http://www.eitc.org/research-opportunities/future-internet-and-optical-quantum-communications/internet-networks-and-tcp-ip/ip-technologies-and-migration
### [Reference](http://www.rfc-editor.org/ien/ien2.txt) - http://www.rfc-editor.org/ien/ien2.txt
### [Reference](http://www.rfc-editor.org/ien/ien26.pdf) - http://www.rfc-editor.org/ien/ien26.pdf
### [Reference](http://www.rfc-editor.org/ien/ien28.pdf) - http://www.rfc-editor.org/ien/ien28.pdf
### [Reference](http://www.rfc-editor.org/ien/ien41.pdf) - http://www.rfc-editor.org/ien/ien41.pdf
### [Reference](http://www.rfc-editor.org/ien/ien44.pdf) - http://www.rfc-editor.org/ien/ien44.pdf
### [Reference](http://www.rfc-editor.org/ien/ien54.pdf) - http://www.rfc-editor.org/ien/ien54.pdf
### [Reference](http://www.worldcat.org/issn/1558-0857) - http://www.worldcat.org/issn/1558-0857
### [Reference](http://www.cpni.gov.uk/Docs/InternetProtocol.pdf) - http://www.cpni.gov.uk/Docs/InternetProtocol.pdf
### [Reference](https://www.ict.tuwien.ac.at/lva/384.081/datacom/09-IP_Technology_v6-3_handout.pdf) - https://www.ict.tuwien.ac.at/lva/384.081/datacom/09-IP_Technology_v6-3_handout.pdf
### [Reference](https://www.ict.tuwien.ac.at/lva/384.081/datacom/10-IP_Routing_v6-2_handout.pdf) - https://www.ict.tuwien.ac.at/lva/384.081/datacom/10-IP_Routing_v6-2_handout.pdf
### [Reference](https://blog.alertlogic.com/blog/where-is-ipv1,-2,-3,and-5/) - https://blog.alertlogic.com/blog/where-is-ipv1,-2,-3,and-5/
### [Reference](https://www.arbornetworks.com/blog/asert/ipv6-fragmentation/) - https://www.arbornetworks.com/blog/asert/ipv6-fragmentation/
### [Reference](https://books.google.com/books?id=XDJlDwAAQBAJ&q=The+dynamic+nature+of+the+Internet+and+the+diversity+of+its+components+provide+no+guarantee+that+any+particular+path+is+actually+capable+of,+or+suitable+for,+performing+the+data+transmission+requested.+One+of+the+technical+constraints+is+the+size+of+data+packets+possible+on+a+given+link.+Facilities+exist+to+examine+the+maximum+transmission+unit+(MTU)+size+of+the+local+link+and+Path+MTU+Discovery+can+be+used+for+the+entire+intended+path+to+the+destination.&pg=PA332) - https://books.google.com/books?id=XDJlDwAAQBAJ&q=The+dynamic+nature+of+the+Internet+and+the+diversity+of+its+components+provide+no+guarantee+that+any+particular+path+is+actually+capable+of,+or+suitable+for,+performing+the+data+transmission+requested.+One+of+the+technical+constraints+is+the+size+of+data+packets+possible+on+a+given+link.+Facilities+exist+to+examine+the+maximum+transmission+unit+(MTU)+size+of+the+local+link+and+Path+MTU+Discovery+can+be+used+for+the+entire+intended+path+to+the+destination.&pg=PA332
### [Reference](https://www.google.com/intl/en/ipv6/statistics.html#tab=ipv6-adoption) - https://www.google.com/intl/en/ipv6/statistics.html#tab=ipv6-adoption
### [Reference](https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf) - https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf
### [Reference](https://d-nb.info/gnd/4482590-0) - https://d-nb.info/gnd/4482590-0
### [Reference](https://labs.ripe.net/author/stephen_strowes/ipv6-adoption-in-2021/) - https://labs.ripe.net/author/stephen_strowes/ipv6-adoption-in-2021/
### [Reference](https://web.archive.org/web/20100211145721/http://www.cpni.gov.uk/Docs/InternetProtocol.pdf) - https://web.archive.org/web/20100211145721/http://www.cpni.gov.uk/Docs/InternetProtocol.pdf
### [Reference](https://web.archive.org/web/20150705060055/http://archive.oreilly.com/cs/user/view/cs_msg/25036) - https://web.archive.org/web/20150705060055/http://archive.oreilly.com/cs/user/view/cs_msg/25036
### [Reference](https://www.iana.org/assignments/version-numbers/version-numbers.xhtml) - https://www.iana.org/assignments/version-numbers/version-numbers.xhtml
### [Reference](https://datatracker.ietf.org/doc/html/rfc1347) - https://datatracker.ietf.org/doc/html/rfc1347
### [Reference](https://datatracker.ietf.org/doc/html/rfc1475) - https://datatracker.ietf.org/doc/html/rfc1475
### [Reference](https://datatracker.ietf.org/doc/html/rfc1606) - https://datatracker.ietf.org/doc/html/rfc1606
### [Reference](https://datatracker.ietf.org/doc/html/rfc1621) - https://datatracker.ietf.org/doc/html/rfc1621
### [Reference](https://datatracker.ietf.org/doc/html/rfc1726) - https://datatracker.ietf.org/doc/html/rfc1726
### [Reference](https://datatracker.ietf.org/doc/html/rfc2460) - https://datatracker.ietf.org/doc/html/rfc2460
### [Reference](https://datatracker.ietf.org/doc/html/rfc6274) - https://datatracker.ietf.org/doc/html/rfc6274
### [Reference](https://datatracker.ietf.org/doc/html/rfc760) - https://datatracker.ietf.org/doc/html/rfc760
### [Reference](https://datatracker.ietf.org/doc/html/rfc791) - https://datatracker.ietf.org/doc/html/rfc791
### [Reference](https://www.oecd-ilibrary.org/science-and-technology/the-economics-of-transition-to-internet-protocol-version-6-ipv6_5jxt46d07bhc-en) - https://www.oecd-ilibrary.org/science-and-technology/the-economics-of-transition-to-internet-protocol-version-6-ipv6_5jxt46d07bhc-en
### [Reference](https://www.wikidata.org/wiki/Q8795#identifiers) - https://www.wikidata.org/wiki/Q8795#identifiers
### [Reference](https://hfhr.pl/wp-content/journal/42r9j.php?tag=internet-protocols-84ec25) - https://hfhr.pl/wp-content/journal/42r9j.php?tag=internet-protocols-84ec25
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/f/f9/Crystal_Clear_app_linneighborhood.svg) - https://upload.wikimedia.org/wikipedia/commons/f/f9/Crystal_Clear_app_linneighborhood.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/1/13/First_Internet_Demonstration%2C_1977.jpg) - https://upload.wikimedia.org/wikipedia/commons/1/13/First_Internet_Demonstration%2C_1977.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/3e/TCP_and_IP_protocols_development_timeline-en.svg) - https://upload.wikimedia.org/wikipedia/commons/3/3e/TCP_and_IP_protocols_development_timeline-en.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/3b/UDP_encapsulation.svg) - https://upload.wikimedia.org/wikipedia/commons/3/3b/UDP_encapsulation.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/9/99/Wiktionary-logo-en-v2.svg) - https://upload.wikimedia.org/wikipedia/commons/9/99/Wiktionary-logo-en-v2.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg