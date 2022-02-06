# Address Resolution Protocol
## [URL](https://en.wikipedia.org/wiki/Address_Resolution_Protocol) - https://en.wikipedia.org/wiki/Address_Resolution_Protocol
## Catagories
### Address Resolution Protocol
### All articles with failed verification
### Articles with failed verification from January 2022
### Articles with short description
### Internet Standards
### Short description is different from Wikidata
### Windows commands
### "The Address Resolution Protocol (ARP) is a communication protocol used for discovering the link layer address, such as a MAC address, associated with a given internet layer address, typically an IPv4 address. This mapping is a critical function in the Internet protocol suite. ARP was defined in 1982 by RFC 826, which is Internet Standard STD 37. 
### ARP has been implemented with many combinations of network and data link layer technologies, such as IPv4, Chaosnet, DECnet and Xerox PARC Universal Packet (PUP) using IEEE 802 standards, FDDI, X.25, Frame Relay and Asynchronous Transfer Mode (ATM). 
### In Internet Protocol Version 6 (IPv6) networks, the functionality of ARP is provided by the Neighbor Discovery Protocol (NDP).
## Operating scope  
### The Address Resolution Protocol is a request-response protocol whose messages are encapsulated by a link layer protocol. It is communicated within the boundaries of a single network, never routed across internetworking nodes. This property places ARP in the link layer of the Internet protocol suite.
## Packet structure  
### The Address Resolution Protocol uses a simple message format containing one address resolution request or response. The size of the ARP message depends on the link layer and network layer address sizes. The message header specifies the types of network in use at each layer as well as the size of addresses of each. The message header is completed with the operation code for request (1) and reply (2). The payload of the packet consists of four addresses, the hardware and protocol address of the sender and receiver hosts. 
### The principal packet structure of ARP packets is shown in the following table which illustrates the case of IPv4 networks running on Ethernet. In this scenario, the packet has 48-bit fields for the sender hardware address (SHA) and target hardware address (THA), and 32-bit fields for the corresponding sender and target protocol addresses (SPA and TPA). The ARP packet size in this case is 28 bytes. 

### Hardware type (HTYPE) 
### This field specifies the network link protocol type. Example: Ethernet is 1. 
### Protocol type (PTYPE) 
### This field specifies the internetwork protocol for which the ARP request is intended. For IPv4, this has the value 0x0800. The permitted PTYPE values share a numbering space with those for EtherType. 
### Hardware length (HLEN) 
### Length (in octets) of a hardware address. Ethernet address length is 6. 
### Protocol length (PLEN) 
### Length (in octets) of internetwork addresses. The internetwork protocol is specified in PTYPE. Example: IPv4 address length is 4. 
### Operation 
### Specifies the operation that the sender is performing: 1 for request, 2 for reply. 
### Sender hardware address (SHA) 
### Media address of the sender. In an ARP request this field is used to indicate the address of the host sending the request. In an ARP reply this field is used to indicate the address of the host that the request was looking for. 
### Sender protocol address (SPA) 
### Internetwork address of the sender. 
### Target hardware address (THA) 
### Media address of the intended receiver. In an ARP request this field is ignored. In an ARP reply this field is used to indicate the address of the host that originated the ARP request. 
### Target protocol address (TPA) 
### Internetwork address of the intended receiver.ARP protocol parameter values have been standardized and are maintained by the Internet Assigned Numbers Authority (IANA).The EtherType for ARP is 0x0806. This appears in the Ethernet frame header when the payload is an ARP packet and is not to be confused with PTYPE, which appears within this encapsulated ARP packet.
## Example  
### Two computers in an office (Computer 1 and Computer 2) are connected to each other in a local area network by Ethernet cables and network switches, with no intervening gateways or routers. Computer 1 has a packet to send to Computer 2. Through DNS, it determines that Computer 2 has the IP address 192.168.0.55. 
### To send the message, it also requires Computer 2's MAC address. First, Computer 1 uses a cached ARP table to look up 192.168.0.55 for any existing records of Computer 2's MAC address (00:eb:24:b2:05:ac). If the MAC address is found, it sends an Ethernet frame with destination address 00:eb:24:b2:05:ac, containing the IP packet onto the link. If the cache did not produce a result for 192.168.0.55, Computer 1 has to send a broadcast ARP request message (destination FF:FF:FF:FF:FF:FF MAC address), which is accepted by all computers on the local network, requesting an answer for 192.168.0.55. 
### Computer 2 responds with an ARP response message containing its MAC and IP addresses. As part of fielding the request, Computer 2 may insert an entry for Computer 1 into its ARP table for future use. 
### Computer 1 receives and caches the response information in its ARP table and can now send the packet.
## ARP probe  
### An ARP probe is an ARP request constructed with an all-zero SPA. Before beginning to use an IPv4 address (whether received from manual configuration, DHCP, or some other means), a host implementing this specification must test to see if the address is already in use, by broadcasting ARP probe packets.
## ARP announcements  
### ARP may also be used as a simple announcement protocol. This is useful for updating other hosts' mappings of a hardware address when the sender's IP address or MAC address changes. Such an announcement, also called a gratuitous ARP (GARP) message, is usually broadcast as an ARP request containing the SPA in the target field (TPASPA), with THA set to zero. An alternative way is to broadcast an ARP reply with the sender's SHA and SPA duplicated in the target fields (TPASPA, THASHA). 
### The ARP request and ARP reply announcements are both standards-based methods, but the ARP request method is preferred. Some devices may be configured for the use of either of these two types of announcements.An ARP announcement is not intended to solicit a reply; instead, it updates any cached entries in the ARP tables of other hosts that receive the packet. The operation code in the announcement may be either request or reply; the ARP standard specifies that the opcode is only processed after the ARP table has been updated from the address fields.Many operating systems issue an ARP announcement during startup. This helps to resolve problems which would otherwise occur if, for example, a network card was recently changed (changing the IP-address-to-MAC-address mapping) and other hosts still have the old mapping in their ARP caches. 
### ARP announcements are also used by some network interfaces to provide load balancing for incoming traffic. In a team of network cards, it is used to announce a different MAC address within the team that should receive incoming packets. 
### ARP announcements can be used in the Zeroconf protocol to allow automatic assignment of a link-local IP addresses to an interface where no other IP address configuration is available. The announcements are used to ensure an address chosen by a host is not in use by other hosts on the network link.This function can be dangerous from a cybersecurity viewpoint since an attacker can obtain information about the other hosts of its subnet to save in their ARP cache (ARP spoofing) an entry where the attacker MAC is associated, for instance, to the IP of the default gateway, thus allowing him to intercept all the traffic to external networks.
## ARP mediation  
### ARP mediation refers to the process of resolving Layer-2 addresses through a virtual private wire service (VPWS) when different resolution protocols are used on the connected circuits, e.g., Ethernet on one end and Frame Relay on the other.  In IPv4, each provider edge (PE) device discovers the IP address of the locally attached customer edge (CE) device and distributes that IP address to the corresponding remote PE device.  Then each PE device responds to local ARP requests using the IP address of the remote CE device and the hardware address of the local PE device.  In IPv6, each PE device discovers the IP address of both local and remote CE devices and then intercepts local Neighbor Discovery (ND) and Inverse Neighbor Discovery (IND) packets and forwards them to the remote PE device.
## Inverse ARP and Reverse ARP  
### Inverse Address Resolution Protocol (Inverse ARP or InARP) is used to obtain network layer addresses (for example, IP addresses) of other nodes from data link layer (Layer 2) addresses. Since ARP translates layer-3 addresses to layer-2 addresses, InARP may be described as its inverse. In addition, InARP is implemented as a protocol extension to ARP: it uses the same packet format as ARP, but different operation codes. 
### InARP is primarily used in Frame Relay (DLCI) and ATM networks, in which layer-2 addresses of virtual circuits are sometimes obtained from layer-2 signaling, and the corresponding layer-3 addresses must be available before those virtual circuits can be used.The Reverse Address Resolution Protocol (Reverse ARP or RARP), like InARP, translates layer-2 addresses to layer-3 addresses. However, in InARP the requesting station queries the layer-3 address of another node, whereas RARP is used to obtain the layer-3 address of the requesting station itself for address configuration purposes. RARP is obsolete; it was replaced by BOOTP, which was later superseded by the Dynamic Host Configuration Protocol (DHCP).
## ARP spoofing and proxy ARP  

### Because ARP does not provide methods for authenticating ARP replies on a network, ARP replies can come from systems other than the one with the required Layer 2 address.  An ARP proxy is a system that answers the ARP request on behalf of another system for which it will forward traffic, normally as a part of the network's design, such as for a dialup internet service. By contrast, in ARP spoofing the answering system, or spoofer, replies to a request for another system's address with the aim of intercepting data bound for that system. A malicious user may use ARP spoofing to perform a man-in-the-middle or denial-of-service attack on other users on the network. Various software exists to both detect and perform ARP spoofing attacks, though ARP itself does not provide any methods of protection from such attacks.
## Alternatives  
### IPv6 uses the Neighbor Discovery Protocol and its extensions such as Secure Neighbor Discovery, rather than ARP. 
### Computers can maintain lists of known addresses, rather than using an active protocol. In this model, each computer maintains a database of the mapping of Layer 3 addresses (e.g., IP addresses) to Layer 2 addresses (e.g., Ethernet MAC addresses). This data maintained primarily by interpreting ARP packets from the local network link. Thus, it is often called the ARP cache. Since at least the 1980s, networked computers have a utility called arp for interrogating or manipulating this database.Historically, other methods were used to maintain the mapping between addresses, such as static configuration files, or centrally maintained lists.
## ARP stuffing  
### Embedded systems such as networked cameras and networked power distribution devices, which lack a user interface, can use so-called ARP stuffing to make an initial network connection, although this is a misnomer, as ARP is not involved. 
### ARP stuffing is accomplished as follows: 

### The user's computer has an IP address stuffed manually into its address table (normally with the arp command with the MAC address taken from a label on the device) 
### The computer sends special packets to the device, typically a ping packet with a non-default size. 
### The device then adopts this IP address 
### The user then communicates with it by telnet or web protocols to complete the configuration.Such devices typically have a method to disable this process once the device is operating normally, as the capability can make it vulnerable to attack.
## Standards documents  
### RFC 826 - Ethernet Address Resolution Protocol, Internet Standard STD 37. 
### RFC 903 - Reverse Address Resolution Protocol, Internet Standard STD 38. 
### RFC 2390 - Inverse Address Resolution Protocol, draft standard 
### RFC 5227 - IPv4 Address Conflict Detection, proposed standard
## See also  
### Arping 
### Arptables 
### Arpwatch 
### Bonjour Sleep Proxy 
### Cisco HDLC
## References 
## External links  
### \"ARP Sequence Diagram (pdf)\" (PDF). Archived from the original (PDF) on 2021-03-01. 
### Gratuitous ARP 
### Information and sample capture from Wireshark 
### ARP-SK ARP traffic generation tools"
## References
### [Reference](http://www.apcmedia.com/salestools/ASTE-6Z6K56_R0_EN.pdf) - http://www.apcmedia.com/salestools/ASTE-6Z6K56_R0_EN.pdf
### [Reference](http://www.axis.com/files/manuals/ig_p13Series_38731_en_1006.pdf) - http://www.axis.com/files/manuals/ig_p13Series_38731_en_1006.pdf
### [Reference](http://support.citrix.com/article/CTX112701) - http://support.citrix.com/article/CTX112701
### [Reference](http://www.eventhelix.com/RealtimeMantra/Networking/Arp.pdf) - http://www.eventhelix.com/RealtimeMantra/Networking/Arp.pdf
### [Reference](http://www.grc.com/nat/arp.htm) - http://www.grc.com/nat/arp.htm
### [Reference](http://manpages.ubuntu.com/manpages/lucid/man8/arp.8.html) - http://manpages.ubuntu.com/manpages/lucid/man8/arp.8.html
### [Reference](http://doi.org/10.17487%2FRFC0903) - http://doi.org/10.17487%2FRFC0903
### [Reference](http://doi.org/10.17487%2FRFC5227) - http://doi.org/10.17487%2FRFC5227
### [Reference](http://doi.org/10.17487%2FRFC6575) - http://doi.org/10.17487%2FRFC6575
### [Reference](http://www.freebsd.org/cgi/man.cgi?query=arp&apropos=0&sektion=0&manpath=2.10+BSD&arch=default&format=html) - http://www.freebsd.org/cgi/man.cgi?query=arp&apropos=0&sektion=0&manpath=2.10+BSD&arch=default&format=html
### [Reference](http://www.freebsd.org/cgi/man.cgi?query=ethers&sektion=5&apropos=0&manpath=SunOS+4.1.3) - http://www.freebsd.org/cgi/man.cgi?query=ethers&sektion=5&apropos=0&manpath=SunOS+4.1.3
### [Reference](http://www.iana.org/assignments/arp-parameters/arp-parameters.xhtml) - http://www.iana.org/assignments/arp-parameters/arp-parameters.xhtml
### [Reference](http://tools.ietf.org/html/rfc2002#section-4.6) - http://tools.ietf.org/html/rfc2002#section-4.6
### [Reference](http://tools.ietf.org/html/rfc2131#section-4.4.1) - http://tools.ietf.org/html/rfc2131#section-4.4.1
### [Reference](http://tools.ietf.org/html/rfc2390) - http://tools.ietf.org/html/rfc2390
### [Reference](http://tools.ietf.org/html/rfc826) - http://tools.ietf.org/html/rfc826
### [Reference](http://www1.ietf.org/mail-archive/web/dhcwg/current/msg03797.html) - http://www1.ietf.org/mail-archive/web/dhcwg/current/msg03797.html
### [Reference](http://wiki.wireshark.org/Gratuitous_ARP) - http://wiki.wireshark.org/Gratuitous_ARP
### [Reference](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man8/arp.8.html) - https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man8/arp.8.html
### [Reference](https://gitlab.com/wireshark/wireshark/-/wikis/AddressResolutionProtocol) - https://gitlab.com/wireshark/wireshark/-/wikis/AddressResolutionProtocol
### [Reference](https://technet.microsoft.com/en-us/library/cc786759(WS.10).aspx) - https://technet.microsoft.com/en-us/library/cc786759(WS.10).aspx
### [Reference](https://web.archive.org/web/20071012093401/http://www1.ietf.org/mail-archive/web/dhcwg/current/msg03797.html) - https://web.archive.org/web/20071012093401/http://www1.ietf.org/mail-archive/web/dhcwg/current/msg03797.html
### [Reference](https://web.archive.org/web/20090903074149/http://sid.rstack.org/arp-sk/) - https://web.archive.org/web/20090903074149/http://sid.rstack.org/arp-sk/
### [Reference](https://web.archive.org/web/20111125012617/http://www.apcmedia.com/salestools/ASTE-6Z6K56_R0_EN.pdf) - https://web.archive.org/web/20111125012617/http://www.apcmedia.com/salestools/ASTE-6Z6K56_R0_EN.pdf
### [Reference](https://web.archive.org/web/20120316213518/http://manpages.ubuntu.com/manpages/lucid/man8/arp.8.html) - https://web.archive.org/web/20120316213518/http://manpages.ubuntu.com/manpages/lucid/man8/arp.8.html
### [Reference](https://web.archive.org/web/20210301060206/http://www.eventhelix.com/RealtimeMantra/Networking/Arp.pdf) - https://web.archive.org/web/20210301060206/http://www.eventhelix.com/RealtimeMantra/Networking/Arp.pdf
### [Reference](https://www.iana.org/assignments/arp-parameters/arp-parameters.xhtml) - https://www.iana.org/assignments/arp-parameters/arp-parameters.xhtml
### [Reference](https://www.iana.org/assignments/ethernet-numbers/ethernet-numbers.xhtml) - https://www.iana.org/assignments/ethernet-numbers/ethernet-numbers.xhtml
### [Reference](https://datatracker.ietf.org/doc/html/rfc1122) - https://datatracker.ietf.org/doc/html/rfc1122
### [Reference](https://datatracker.ietf.org/doc/html/rfc2390) - https://datatracker.ietf.org/doc/html/rfc2390
### [Reference](https://datatracker.ietf.org/doc/html/rfc3927) - https://datatracker.ietf.org/doc/html/rfc3927
### [Reference](https://datatracker.ietf.org/doc/html/rfc5227) - https://datatracker.ietf.org/doc/html/rfc5227
### [Reference](https://datatracker.ietf.org/doc/html/rfc5342) - https://datatracker.ietf.org/doc/html/rfc5342
### [Reference](https://datatracker.ietf.org/doc/html/rfc6575) - https://datatracker.ietf.org/doc/html/rfc6575
### [Reference](https://datatracker.ietf.org/doc/html/rfc826) - https://datatracker.ietf.org/doc/html/rfc826
### [Reference](https://datatracker.ietf.org/doc/html/rfc903) - https://datatracker.ietf.org/doc/html/rfc903
### [Reference](https://tools.ietf.org/html/rfc2002#section-4.6) - https://tools.ietf.org/html/rfc2002#section-4.6
### [Reference](https://tools.ietf.org/html/rfc5227#section-3) - https://tools.ietf.org/html/rfc5227#section-3
### [Reference](https://tools.ietf.org/html/rfc5944#section-4.6) - https://tools.ietf.org/html/rfc5944#section-4.6
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/33/ARP_Spoofing.svg) - https://upload.wikimedia.org/wikipedia/commons/3/33/ARP_Spoofing.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg) - https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg