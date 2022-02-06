# IPv4
## [URL](https://en.wikipedia.org/wiki/IPv4) - https://en.wikipedia.org/wiki/IPv4
## Catagories
### All articles with failed verification
### Articles containing video clips
### Articles with GND identifiers
### Articles with failed verification from January 2022
### Articles with short description
### CS1 errors: missing periodical
### CS1 maint: others
### IPv4
### Internet Standards
### Internet layer protocols
### Network layer protocols
### Pages using Sister project links with default search
### Short description matches Wikidata
### "Internet Protocol version 4 (IPv4) is the fourth version of the Internet Protocol (IP). It is one of the core protocols of standards-based internetworking methods in the Internet and other packet-switched networks. IPv4 was the first version deployed for production on SATNET in 1982 and on the ARPANET in January 1983. It is still used to route most Internet traffic today, even with the ongoing deployment of Internet Protocol version 6 (IPv6), its successor. 
### IPv4 uses a 32-bit address space which provides 4,294,967,296 (232) unique addresses, but large blocks are reserved for special networking purposes.
## History  
### Internet Protocol version 4 is described in IETF publication RFC 791 (September 1981), replacing an earlier definition of January 1980 (RFC 760). In March 1982, the US Department of Defense decided on the Internet Protocol Suite (TCP/IP) as the standard for all military computer networking.
## Purpose  
### The Internet Protocol is the protocol that defines and enables internetworking at the internet layer of the Internet Protocol Suite. In essence it forms the Internet. It uses a logical addressing system and performs routing, which is the forwarding of packets from a source host to the next router that is one hop closer to the intended destination host on another network. 
### IPv4 is a connectionless protocol, and operates on a best-effort delivery model, in that it does not guarantee delivery, nor does it assure proper sequencing or avoidance of duplicate delivery. These aspects, including data integrity, are addressed by an upper layer transport protocol, such as the Transmission Control Protocol (TCP).
## Addressing  

### IPv4 uses 32-bit addresses which limits the address space to 4294967296 (232) addresses. 
### IPv4 reserves special address blocks for private networks (~18 million addresses) and multicast addresses (~270 million addresses).
## Address representations  
### IPv4 addresses may be represented in any notation expressing a 32-bit integer value. They are most often written in dot-decimal notation, which consists of four octets of the address expressed individually in decimal numbers and separated by periods. 
### For example, the quad-dotted IP address 192.0.2.235 represents the 32-bit decimal number 3221226219, which in hexadecimal format is 0xC00002EB. 
### CIDR notation combines the address with its routing prefix in a compact format, in which the address is followed by a slash character (/) and the count of leading consecutive 1 bits in the routing prefix (subnet mask). 
### Other address representations were in common use when classful networking was practiced. For example, the loopback address 127.0.0.1 is commonly written as 127.1, given that it belongs to a class-A network with eight bits for the network mask and 24 bits for the host number. When fewer than four numbers are specified in the address in dotted notation, the last value is treated as an integer of as many bytes as are required to fill out the address to four octets. Thus, the address 127.65530 is equivalent to 127.0.255.250.
## Allocation  
### In the original design of IPv4, an IP address was divided into two parts: the network identifier was the most significant octet of the address, and the host identifier was the rest of the address. The latter was also called the rest field. This structure permitted a maximum of 256 network identifiers, which was quickly found to be inadequate. 
### To overcome this limit, the most-significant address octet was redefined in 1981 to create network classes, in a system which later became known as classful networking. The revised system defined five classes. Classes A, B, and C had different bit lengths for network identification. The rest of the address was used as previously to identify a host within a network. Because of the different sizes of fields in different classes, each network class had a different capacity for addressing hosts. In addition to the three classes for addressing hosts, Class D was defined for multicast addressing and Class E was reserved for future applications. 
### Dividing existing classful networks into subnets began in 1985 with the publication of RFC 950. This division was made more flexible with the introduction of variable-length subnet masks (VLSM) in RFC 1109 in 1987. In 1993, based on this work, RFC 1517 introduced Classless Inter-Domain Routing (CIDR),  which expressed the number of bits (from the most significant) as, for instance, /24, and the class-based scheme was dubbed classful, by contrast. CIDR was designed to permit repartitioning of any address space so that smaller or larger blocks of addresses could be allocated to users. The hierarchical structure created by CIDR is managed by the Internet Assigned Numbers Authority (IANA) and the regional Internet registries (RIRs). Each RIR maintains a publicly searchable WHOIS database that provides information about IP address assignments.
## Special-use addresses  
### The Internet Engineering Task Force (IETF) and IANA have restricted from general use various reserved IP addresses for special purposes. Notably these addresses are used for multicast traffic and to provide addressing space for unrestricted uses on private networks.
## Private networks  
### Of the approximately four billion addresses defined in IPv4, about 18 million addresses in three ranges are reserved for use in private networks. Packets addresses in these ranges are not routable in the public Internet; they are ignored by all public routers. Therefore, private hosts cannot directly communicate with public networks, but require network address translation at a routing gateway for this purpose. 

### Since two private networks, e.g., two branch offices, cannot directly interoperate via the public Internet, the two networks must be bridged across the Internet via a virtual private network (VPN) or an IP tunnel, which encapsulates packets, including their headers containing the private addresses, in a protocol layer during transmission across the public network. Additionally, encapsulated packets may be encrypted for transmission across public networks to secure the data.
## Link-local addressing  
### RFC 3927 defines the special address block 169.254.0.0/16 for link-local addressing. These addresses are only valid on the link (such as a local network segment or point-to-point connection) directly connected to a host that uses them. These addresses are not routable. Like private addresses, these addresses cannot be the source or destination of packets traversing the internet. These addresses are primarily used for address autoconfiguration (Zeroconf) when a host cannot obtain an IP address from a DHCP server or other internal configuration methods. 
### When the address block was reserved, no standards existed for address autoconfiguration. Microsoft created an implementation called Automatic Private IP Addressing (APIPA), which was deployed on millions of machines and became a de facto standard. Many years later, in May 2005, the IETF defined a formal standard in RFC 3927, entitled Dynamic Configuration of IPv4 Link-Local Addresses.
## Loopback  

### The class A network 127.0.0.0 (classless network 127.0.0.0/8) is reserved for loopback. IP packets whose source addresses belong to this network should never appear outside a host. Packets received on a non-loopback interface with a loopback source or destination address must be dropped.
## First and last subnet addresses  

### The first address in a subnet is used to identify the subnet itself. In this address all host bits are 0. To avoid ambiguity in representation, this address is reserved. The last address has all host bits set to 1. It is used as a local broadcast address for sending messages to all devices on the subnet simultaneously. For networks of size /24 or larger, the broadcast address always ends in 255. 
### For example, in the subnet 192.168.5.0/24 (subnet mask 255.255.255.0) the identifier 192.168.5.0 is used to refer to the entire subnet. The broadcast address of the network is 192.168.5.255. 

### However, this does not mean that every address ending in 0 or 255 cannot be used as a host address. For example, in the /16 subnet 192.168.0.0/255.255.0.0, which is equivalent to the address range 192.168.0.0\u2013192.168.255.255, the broadcast address is 192.168.255.255. One can use the following addresses for hosts, even though they end with 255: 192.168.1.255, 192.168.2.255, etc. Also, 192.168.0.0 is the network identifier and must not be assigned to an interface. The addresses 192.168.1.0, 192.168.2.0, etc., may be assigned, despite ending with 0. 
### In the past, conflict between network addresses and broadcast addresses arose because some software used non-standard broadcast addresses with zeros instead of ones.In networks smaller than /24, broadcast addresses do not necessarily end with 255. For example, a CIDR subnet 203.0.113.16/28 has the broadcast address 203.0.113.31. 

### As a special case, a /31 network has capacity for just two hosts. These networks are typically used for point-to-point connections. There is no network identifier or broadcast address for these networks.
## Address resolution  

### Hosts on the Internet are usually known by names, e.g., www.example.com, not primarily by their IP address, which is used for routing and network interface identification. The use of domain names requires translating, called resolving, them to addresses and vice versa. This is analogous to looking up a phone number in a phone book using the recipient's name. 
### The translation between addresses and domain names is performed by the Domain Name System (DNS), a hierarchical, distributed naming system that allows for the subdelegation of namespaces to other DNS servers.
## Unnumbered interface  
### A unnumbered point-to-point (PtP) link, also called a transit link, is a link that doesn't have any IP network or subnet number associated with it, but still have a IP address. First introduced in 1993. The only purposes of a transit link is to route datagrams. 
### Unnumbered link is used to free IP addresses, when having a scarce IP address space, or reduce the management of assigning IP and configuration of interfaces. Previous every link needs to dedicated /30  or /31 subnet using 2-4 IP addresses per point to point link. When a link is unnumbered a router-id is used, router-id is IP address /32 borrowed from a defined (normally a loopback) interface. The same router-id can be used on multiple interfaces. 
### One of the disadvantage to unnumbered interface, is that is harder to do remote testing and management. 
### Phil Karn from Qualcomm is credit as original designer.
## Address space exhaustion  

### Since the 1980s, it was apparent that the pool of available IPv4 addresses was depleting at a rate that was not initially anticipated in the original design of the network. The main market forces that accelerated address depletion included the rapidly growing number of Internet users, who increasingly used mobile computing devices, such as laptop computers, personal digital assistants (PDAs), and smart phones with IP data services. In addition, high-speed Internet access was based on always-on devices. The threat of exhaustion motivated the introduction of a number of remedial technologies, such as: 

### Classless Inter-Domain Routing (CIDR), for smaller ISP allocations 
### Unnumbered interface, removed the need on transit links. 
### network address translation, removed the need for end-to-end principle.By the mid-1990s, pervasive use of network address translation (NAT) in network access provider systems, and strict usage-based allocation policies at the regional and local Internet registries. 

### The primary address pool of the Internet, maintained by IANA, was exhausted on 3 February 2011, when the last five blocks were allocated to the five RIRs. APNIC was the first RIR to exhaust its regional pool on 15 April 2011, except for a small amount of address space reserved for the transition technologies to IPv6, which is to be allocated under a restricted policy.The long-term solution to address exhaustion was the 1998 specification of a new version of the Internet Protocol, IPv6. It provides a vastly increased address space, but also allows improved route aggregation across the Internet, and offers large subnetwork allocations of a minimum of 264 host addresses to end users. However, IPv4 is not directly interoperable with IPv6, so that IPv4-only hosts cannot directly communicate with IPv6-only hosts. With the phase-out of the 6bone experimental network starting in 2004, permanent formal deployment of IPv6 commenced in 2006. Completion of IPv6 deployment is expected to take considerable time, so that intermediate transition technologies are necessary to permit hosts to participate in the Internet using both versions of the protocol.
## Packet structure  
### An IP packet consists of a header section and a data section. An IP packet has no data checksum or any other footer after the data section. 
### Typically the link layer encapsulates IP packets in frames with a CRC footer that detects most errors, many transport-layer protocols carried by IP also have their own error checking.
## Header  
### The IPv4 packet header consists of 14 fields, of which 13 are required. The 14th field is optional and aptly named: options. The fields in the header are packed with the most significant byte first (big endian), and for the diagram and discussion, the most significant bits are considered to come first (MSB 0 bit numbering). The most significant bit is numbered 0, so the version field is actually found in the four most significant bits of the first byte, for example. 

### Version 
### The first header field in an IP packet is the four-bit version field. For IPv4, this is always equal to 4. 
### Internet Header Length (IHL) 
### The IPv4 header is variable in size due to the optional 14th field (options). The IHL field contains the size of the IPv4 header, it has 4 bits that specify the number of 32-bit words in the header. The minimum value for this field is 5, which indicates a length of 5 \u00d7 32 bits  160 bits  20 bytes. As a 4-bit field, the maximum value is 15, this means that the maximum size of the IPv4 header is 15 \u00d7 32 bits  480 bits  60 bytes. 
### Differentiated Services Code Point (DSCP) 
### Originally defined as the type of service (ToS), this field specifies differentiated services (DiffServ) per RFC 2474. Real-time data streaming makes use of the DSCP field. An example is Voice over IP (VoIP), which is used for interactive voice services. 
### Explicit Congestion Notification (ECN) 
### This field is defined in RFC 3168 and allows end-to-end notification of network congestion without dropping packets. ECN is an optional feature available when both endpoints support it and effective when also supported by the underlying network. 
### Total Length 
### This 16-bit field defines the entire packet size in bytes, including header and data. The minimum size is 20 bytes (header without data) and the maximum is 65,535 bytes. All hosts are required to be able to reassemble datagrams of size up to 576 bytes, but most modern hosts handle much larger packets. Links may impose further restrictions on the packet size, in which case datagrams must be fragmented. Fragmentation in IPv4 is performed in either the sending host or in routers. Reassembly is performed at the receiving host. 
### Identification 
### This field is an identification field and is primarily used for uniquely identifying the group of fragments of a single IP datagram. Some experimental work has suggested using the ID field for other purposes, such as for adding packet-tracing information to help trace datagrams with spoofed source addresses, but RFC 6864 now prohibits any such use. 
### Flags 
### A three-bit field follows and is used to control or identify fragments. They are (in order, from most significant to least significant): 
### bit 0: Reserved; must be zero. 
### bit 1: Don't Fragment (DF) 
### bit 2: More Fragments (MF) 
### If the DF flag is set, and fragmentation is required to route the packet, then the packet is dropped. This can be used when sending packets to a host that does not have resources to perform reassembly of fragments. It can also be used for path MTU discovery, either automatically by the host IP software, or manually using diagnostic tools such as ping or traceroute. 
### For unfragmented packets, the MF flag is cleared. For fragmented packets, all fragments except the last have the MF flag set. The last fragment has a non-zero Fragment Offset field, differentiating it from an unfragmented packet. 
### Fragment offset 
### This field specifies the offset of a particular fragment relative to the beginning of the original unfragmented IP datagram in units of eight-byte blocks. The first fragment has an offset of zero. The 13 bit field allows a maximum offset of (213 \u2013 1) \u00d7 8  65,528 bytes, which, with the header length included (65,528 + 20  65,548 bytes), supports fragmentation of packets exceeding the maximum IP length of 65,535 bytes. 
### Time to live (TTL) 
### An eight-bit time to live field limits a datagram's lifetime to prevent network failure in the event of a routing loop. It is specified in seconds, but time intervals less than 1 second are rounded up to 1. In practice, the field is used as a hop count\u2014when the datagram arrives at a router, the router decrements the TTL field by one. When the TTL field hits zero, the router discards the packet and typically sends an ICMP time exceeded message to the sender. 
### The program traceroute sends messages with adjusted TTL values and uses these ICMP time exceeded messages to identify the routers traversed by packets from the source to the destination. 
### Protocol 
### This field defines the protocol used in the data portion of the IP datagram. IANA maintains a list of IP protocol numbers as directed by RFC 790. 
### Header checksum 
### The 16-bit IPv4 header checksum field is used for error-checking of the header. When a packet arrives at a router, the router calculates the checksum of the header and compares it to the checksum field. If the values do not match, the router discards the packet. Errors in the data field must be handled by the encapsulated protocol. Both UDP and TCP have separate checksums that apply to their data. 
### When a packet arrives at a router, the router decreases the TTL field in the header. Consequently, the router must calculate a new header checksum. 
### Source address 
### This field is the IPv4 address of the sender of the packet. Note that this address may be changed in transit by a network address translation device. 
### Destination address 
### This field is the IPv4 address of the receiver of the packet. As with the source address, this may be changed in transit by a network address translation device. 
### Options 
### The options field is not often used. Packets containing  some options may be considered as dangerous by some routers and be blocked. Note that the value in the IHL field must include enough extra 32-bit words to hold all the options plus any padding needed to ensure that the header contains an integer number of 32-bit words. If IHL is greater than 5 (i.e., it is from 6 to 15) it means that the options field is present and must be considered. The list of options may be terminated with an EOOL (End of Options List, 0x00) option; this is only necessary if the end of the options would not otherwise coincide with the end of the header. The possible options that can be put in the header are as follows:The table below shows the defined options for IPv4. The Option Type column is derived from the Copied, Option Class, and Option Number bits as defined above.
## Data  
### The packet payload is not included in the checksum. Its contents are interpreted based on the value of the Protocol header field. 
### List of IP protocol numbers contains a complete list of payload protocol types. Some of the common payload protocols include:
## Fragmentation and reassembly  

### The Internet Protocol enables traffic between networks. The design accommodates networks of diverse physical nature; it is independent of the underlying transmission technology used in the link layer. Networks with different hardware usually vary not only in transmission speed, but also in the maximum transmission unit (MTU). When one network wants to transmit datagrams to a network with a smaller MTU, it may fragment its datagrams. In IPv4, this function was placed at the Internet Layer and is performed in IPv4 routers limiting exposure to these issues by hosts. 
### In contrast, IPv6, the next generation of the Internet Protocol, does not allow routers to perform fragmentation; hosts must perform Path MTU Discovery before sending datagrams.
## Fragmentation  
### When a router receives a packet, it examines the destination address and determines the outgoing interface to use and that interface's MTU.  If the packet size is bigger than the MTU, and the Do not Fragment (DF) bit in the packet's header is set to 0, then the router may fragment the packet. 
### The router divides the packet into fragments. The maximum size of each fragment is the outgoing MTU minus the IP header size (20 bytes minimum; 60 bytes maximum). The router puts each fragment into its own packet, each fragment packet having the following changes: 

### The total length field is the fragment size. 
### The more fragments (MF) flag is set for all fragments except the last one, which is set to 0. 
### The fragment offset field is set, based on the offset of the fragment in the original data payload. This is measured in units of 8-byte blocks. 
### The header checksum field is recomputed.For example, for an MTU of 1,500 bytes and a header size of 20 bytes, the fragment offsets would be multiples of  
  
    
      
        
          
            
             1 
             , 
             500 
             \u2212 
             20 
            
           8 
          
        
        
       185 
      
    
   {\\displaystyle {\\frac {1,500-20}{8}}185} 
  (0, 185, 370, 555, 740, etc.). 
### It is possible that a packet is fragmented at one router, and that the fragments are further fragmented at another router. For example, a packet of 4,520 bytes, including a 20 bytes IP header is fragmented to two packets on a link with an MTU of 2,500 bytes: 

### The total data size is preserved: 2,480 bytes + 2,020 bytes  4,500 bytes. The offsets are  
  
    
      
       0 
      
    
   {\\displaystyle 0} 
  and  
  
    
      
        
          
            
             0 
             + 
             2 
             , 
             480 
            
           8 
          
        
        
       310 
      
    
   {\\displaystyle {\\frac {0+2,480}{8}}310} 
 . 
### When forwarded to a link with an MTU of 1,500 bytes, each fragment is fragmented into two fragments: 

### Again, the data size is preserved: 1,480 + 1,000  2,480, and 1,480 + 540  2,020. 
### Also in this case, the More Fragments bit remains 1 for all the fragments that came with 1 in them and for the last fragment that arrives, it works as usual, that is the MF bit is set to 0 only in the last one. And of course, the Identification field continues to have the same value in all re-fragmented fragments. This way, even if fragments are re-fragmented, the receiver knows they have initially all started from the same packet. 
### The last offset and last data size are used to calculate the total data size:  
  
    
      
       495 
       \u00d7 
       8 
       + 
       540 
        
       3 
       , 
       960 
       + 
       540 
        
       4 
       , 
       500 
      
    
   {\\displaystyle 495\\times 8+5403,960+5404,500} 
 .
## Reassembly  
### A receiver knows that a packet is a fragment, if at least one of the following conditions is true: 

### The flag more fragments is set, which is true for all fragments except the last. 
### The field fragment offset is nonzero, which is true for all fragments except the first.The receiver identifies matching fragments using the foreign and local address, the protocol ID, and the identification field. The receiver reassembles the data from fragments with the same ID using both the fragment offset and the more fragments flag. When the receiver receives the last fragment, which has the more fragments flag set to 0, it can calculate the size of the original data payload, by multiplying the last fragment's offset by eight, and adding the last fragment's data size. In the given example, this calculation was  
  
    
      
       495 
       \u00d7 
       8 
       + 
       540 
        
       4 
       , 
       500 
      
    
   {\\displaystyle 495\\times 8+5404,500} 
  bytes. When the receiver has all fragments, they can be reassembled in the correct sequence according to the offsets, to form the original datagram.
## Assistive protocols  
### IP addresses are not tied in any permanent manner to hardware identifications and, indeed, a network interface can have multiple IP addresses in modern operating systems. Hosts and routers need additional mechanisms to identify the relationship between device interfaces and IP addresses, in order to properly deliver an IP packet to the destination host on a link. The Address Resolution Protocol (ARP) performs this IP-address-to-hardware-address translation for IPv4. (A hardware address is also called a MAC address.) In addition, the reverse correlation is often necessary. For example, when an IP host is booted or connected to a network it needs to determine its IP address, unless an address is preconfigured by an administrator. Protocols for such inverse correlations exist in the Internet Protocol Suite. Currently used methods are Dynamic Host Configuration Protocol (DHCP), Bootstrap Protocol (BOOTP) and, infrequently, reverse ARP.
## See also  
### History of the Internet 
### List of assigned /8 IPv4 address blocks 
### List of IP protocol numbers
## Notes 
## References 
## External links  

### Internet Assigned Numbers Authority (IANA) 
### IP, Internet Protocol \u2014 IP Header Breakdown, including specific options 
### RFC 3344 \u2014 IPv4 Mobility 
### IPv6 vs. carrier-grade NAT/squeezing more out of IPv4 
### RIPE report on address consumption as of October 2003 
### Official current state of IPv4 /8 allocations, as maintained by IANA 
### Dynamically generated graphs of IPv4 address consumption with predictions of exhaustion dates\u2014Geoff Huston 
### IP addressing in China and the myth of address shortage 
### Countdown of remaining IPv4 available addresses (estimated)"
## References
### [Reference](http://www.3com.com/other/pdfs/infra/corpinfo/en_US/501302.pdf) - http://www.3com.com/other/pdfs/infra/corpinfo/en_US/501302.pdf
### [Reference](http://www.inetcore.com/project/ipv4ec/index_en.html) - http://www.inetcore.com/project/ipv4ec/index_en.html
### [Reference](http://www.networksorcery.com/enp/protocol/ip.htm) - http://www.networksorcery.com/enp/protocol/ip.htm
### [Reference](http://www.apnic.net/publications/news/2011/final-8) - http://www.apnic.net/publications/news/2011/final-8
### [Reference](http://technology.inquirer.net/infotech/infotech/view/20110121-315808/World-running-out-of-Internet-addresses) - http://technology.inquirer.net/infotech/infotech/view/20110121-315808/World-running-out-of-Internet-addresses
### [Reference](http://www.nro.net/news/ipv4-free-pool-depleted) - http://www.nro.net/news/ipv4-free-pool-depleted
### [Reference](http://bgp.potaroo.net/index-bgp.html) - http://bgp.potaroo.net/index-bgp.html
### [Reference](http://www.potaroo.net/tools/ipv4/index.html) - http://www.potaroo.net/tools/ipv4/index.html
### [Reference](http://portal.acm.org/citation.cfm?id=347057.347560) - http://portal.acm.org/citation.cfm?id=347057.347560
### [Reference](http://doi.org/10.1145%2F347057.347560) - http://doi.org/10.1145%2F347057.347560
### [Reference](http://doi.org/10.17487%2FRFC0791) - http://doi.org/10.17487%2FRFC0791
### [Reference](http://doi.org/10.17487%2FRFC0919) - http://doi.org/10.17487%2FRFC0919
### [Reference](http://doi.org/10.17487%2FRFC1726) - http://doi.org/10.17487%2FRFC1726
### [Reference](http://doi.org/10.17487%2FRFC1918) - http://doi.org/10.17487%2FRFC1918
### [Reference](http://doi.org/10.17487%2FRFC2544) - http://doi.org/10.17487%2FRFC2544
### [Reference](http://doi.org/10.17487%2FRFC3068) - http://doi.org/10.17487%2FRFC3068
### [Reference](http://doi.org/10.17487%2FRFC3232) - http://doi.org/10.17487%2FRFC3232
### [Reference](http://doi.org/10.17487%2FRFC3701) - http://doi.org/10.17487%2FRFC3701
### [Reference](http://doi.org/10.17487%2FRFC3927) - http://doi.org/10.17487%2FRFC3927
### [Reference](http://doi.org/10.17487%2FRFC5735) - http://doi.org/10.17487%2FRFC5735
### [Reference](http://doi.org/10.17487%2FRFC5737) - http://doi.org/10.17487%2FRFC5737
### [Reference](http://doi.org/10.17487%2FRFC5771) - http://doi.org/10.17487%2FRFC5771
### [Reference](http://doi.org/10.17487%2FRFC6598) - http://doi.org/10.17487%2FRFC6598
### [Reference](http://doi.org/10.17487%2FRFC6676) - http://doi.org/10.17487%2FRFC6676
### [Reference](http://doi.org/10.17487%2FRFC6890) - http://doi.org/10.17487%2FRFC6890
### [Reference](http://doi.org/10.17487%2FRFC7526) - http://doi.org/10.17487%2FRFC7526
### [Reference](http://www.faqs.org/faqs/cisco-networking-faq/section-23.html) - http://www.faqs.org/faqs/cisco-networking-faq/section-23.html
### [Reference](http://tools.ietf.org/html/rfc1122) - http://tools.ietf.org/html/rfc1122
### [Reference](http://tools.ietf.org/html/rfc1122#page-31) - http://tools.ietf.org/html/rfc1122#page-31
### [Reference](http://mailman.nanog.org/pipermail/nanog/2011-February/032107.html) - http://mailman.nanog.org/pipermail/nanog/2011-February/032107.html
### [Reference](http://www.worldcat.org/issn/2070-1721) - http://www.worldcat.org/issn/2070-1721
### [Reference](http://www.worldcat.org/oclc/972636788) - http://www.worldcat.org/oclc/972636788
### [Reference](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/13786-20.html) - https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/13786-20.html
### [Reference](https://www.google.com/intl/en/ipv6/statistics.html) - https://www.google.com/intl/en/ipv6/statistics.html
### [Reference](https://ipv4marketgroup.com/a-brief-history-of-ipv4/) - https://ipv4marketgroup.com/a-brief-history-of-ipv4/
### [Reference](https://d-nb.info/gnd/4588596-5) - https://d-nb.info/gnd/4588596-5
### [Reference](https://www.apnic.net/community/ecosystem/igf/articles/ip-addressing-in-china-2004) - https://www.apnic.net/community/ecosystem/igf/articles/ip-addressing-in-china-2004
### [Reference](https://web.archive.org/web/20010616012053/http://www.3com.com/other/pdfs/infra/corpinfo/en_US/501302.pdf) - https://web.archive.org/web/20010616012053/http://www.3com.com/other/pdfs/infra/corpinfo/en_US/501302.pdf
### [Reference](https://web.archive.org/web/20100608114541/http://www.networkworld.com/news/2010/060710-tech-argument-ipv6-nat.html) - https://web.archive.org/web/20100608114541/http://www.networkworld.com/news/2010/060710-tech-argument-ipv6-nat.html
### [Reference](https://web.archive.org/web/20110109025511/http://www.ripe.net/rs/news/ipv4-ncc-20031030.html) - https://web.archive.org/web/20110109025511/http://www.ripe.net/rs/news/ipv4-ncc-20031030.html
### [Reference](https://web.archive.org/web/20110125195711/http://technology.inquirer.net/infotech/infotech/view/20110121-315808/World-running-out-of-Internet-addresses) - https://web.archive.org/web/20110125195711/http://technology.inquirer.net/infotech/infotech/view/20110121-315808/World-running-out-of-Internet-addresses
### [Reference](https://web.archive.org/web/20110807162057/http://www.apnic.net/publications/news/2011/final-8) - https://web.archive.org/web/20110807162057/http://www.apnic.net/publications/news/2011/final-8
### [Reference](https://www.iana.org) - https://www.iana.org
### [Reference](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml) - https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
### [Reference](https://www.iana.org/assignments/ip-parameters/ip-parameters.xhtml#ip-parameters-1) - https://www.iana.org/assignments/ip-parameters/ip-parameters.xhtml#ip-parameters-1
### [Reference](https://www.iana.org/assignments/ipv4-address-space) - https://www.iana.org/assignments/ipv4-address-space
### [Reference](https://datatracker.ietf.org/doc/draft-ietf-rreq-iprouters-require/00/) - https://datatracker.ietf.org/doc/draft-ietf-rreq-iprouters-require/00/
### [Reference](https://datatracker.ietf.org/doc/html/rfc1109) - https://datatracker.ietf.org/doc/html/rfc1109
### [Reference](https://datatracker.ietf.org/doc/html/rfc1122#page-66) - https://datatracker.ietf.org/doc/html/rfc1122#page-66
### [Reference](https://datatracker.ietf.org/doc/html/rfc1517) - https://datatracker.ietf.org/doc/html/rfc1517
### [Reference](https://datatracker.ietf.org/doc/html/rfc1700) - https://datatracker.ietf.org/doc/html/rfc1700
### [Reference](https://datatracker.ietf.org/doc/html/rfc1716) - https://datatracker.ietf.org/doc/html/rfc1716
### [Reference](https://datatracker.ietf.org/doc/html/rfc1726) - https://datatracker.ietf.org/doc/html/rfc1726
### [Reference](https://datatracker.ietf.org/doc/html/rfc1726#section-6.2) - https://datatracker.ietf.org/doc/html/rfc1726#section-6.2
### [Reference](https://datatracker.ietf.org/doc/html/rfc1812) - https://datatracker.ietf.org/doc/html/rfc1812
### [Reference](https://datatracker.ietf.org/doc/html/rfc1916) - https://datatracker.ietf.org/doc/html/rfc1916
### [Reference](https://datatracker.ietf.org/doc/html/rfc1918) - https://datatracker.ietf.org/doc/html/rfc1918
### [Reference](https://datatracker.ietf.org/doc/html/rfc2544) - https://datatracker.ietf.org/doc/html/rfc2544
### [Reference](https://datatracker.ietf.org/doc/html/rfc3021) - https://datatracker.ietf.org/doc/html/rfc3021
### [Reference](https://datatracker.ietf.org/doc/html/rfc3068) - https://datatracker.ietf.org/doc/html/rfc3068
### [Reference](https://datatracker.ietf.org/doc/html/rfc3168) - https://datatracker.ietf.org/doc/html/rfc3168
### [Reference](https://datatracker.ietf.org/doc/html/rfc3232) - https://datatracker.ietf.org/doc/html/rfc3232
### [Reference](https://datatracker.ietf.org/doc/html/rfc3260) - https://datatracker.ietf.org/doc/html/rfc3260
### [Reference](https://datatracker.ietf.org/doc/html/rfc3344) - https://datatracker.ietf.org/doc/html/rfc3344
### [Reference](https://datatracker.ietf.org/doc/html/rfc3701) - https://datatracker.ietf.org/doc/html/rfc3701
### [Reference](https://datatracker.ietf.org/doc/html/rfc3927) - https://datatracker.ietf.org/doc/html/rfc3927
### [Reference](https://datatracker.ietf.org/doc/html/rfc5735) - https://datatracker.ietf.org/doc/html/rfc5735
### [Reference](https://datatracker.ietf.org/doc/html/rfc5737) - https://datatracker.ietf.org/doc/html/rfc5737
### [Reference](https://datatracker.ietf.org/doc/html/rfc5771) - https://datatracker.ietf.org/doc/html/rfc5771
### [Reference](https://datatracker.ietf.org/doc/html/rfc6201) - https://datatracker.ietf.org/doc/html/rfc6201
### [Reference](https://datatracker.ietf.org/doc/html/rfc6598) - https://datatracker.ietf.org/doc/html/rfc6598
### [Reference](https://datatracker.ietf.org/doc/html/rfc6676) - https://datatracker.ietf.org/doc/html/rfc6676
### [Reference](https://datatracker.ietf.org/doc/html/rfc6761) - https://datatracker.ietf.org/doc/html/rfc6761
### [Reference](https://datatracker.ietf.org/doc/html/rfc6815) - https://datatracker.ietf.org/doc/html/rfc6815
### [Reference](https://datatracker.ietf.org/doc/html/rfc6890) - https://datatracker.ietf.org/doc/html/rfc6890
### [Reference](https://datatracker.ietf.org/doc/html/rfc7526) - https://datatracker.ietf.org/doc/html/rfc7526
### [Reference](https://datatracker.ietf.org/doc/html/rfc791) - https://datatracker.ietf.org/doc/html/rfc791
### [Reference](https://datatracker.ietf.org/doc/html/rfc8190) - https://datatracker.ietf.org/doc/html/rfc8190
### [Reference](https://datatracker.ietf.org/doc/html/rfc919) - https://datatracker.ietf.org/doc/html/rfc919
### [Reference](https://datatracker.ietf.org/doc/html/rfc950) - https://datatracker.ietf.org/doc/html/rfc950
### [Reference](https://tools.ietf.org/html/rfc2460.html) - https://tools.ietf.org/html/rfc2460.html
### [Reference](https://tools.ietf.org/html/rfc923) - https://tools.ietf.org/html/rfc923
### [Reference](https://www.wikidata.org/wiki/Q11103#identifiers) - https://www.wikidata.org/wiki/Q11103#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/6/60/IPv4_Packet-en.svg) - https://upload.wikimedia.org/wikipedia/commons/6/60/IPv4_Packet-en.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/6/66/IPv4_address_structure_and_writing_systems-en.svg) - https://upload.wikimedia.org/wikipedia/commons/6/66/IPv4_address_structure_and_writing_systems-en.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg) - https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg) - https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/0/06/Wiktionary-logo-v2.svg) - https://upload.wikimedia.org/wikipedia/en/0/06/Wiktionary-logo-v2.svg