# Subnetwork
## [URL](https://en.wikipedia.org/wiki/Subnetwork) - https://en.wikipedia.org/wiki/Subnetwork
## Catagories
### Articles with Curlie links
### Articles with GND identifiers
### Articles with short description
### IP addresses
### Internet architecture
### Routing
### Short description is different from Wikidata
### "A subnetwork or subnet is a logical subdivision of an IP network.:\u200a1,\u200a16\u200a The practice of dividing a network into two or more networks is called subnetting. 
### Computers that belong to the same subnet are addressed with an identical most-significant bit-group in their IP addresses. This results in the logical division of an IP address into two fields: the network number or routing prefix and the rest field or host identifier. The rest field is an identifier for a specific host or network interface. 
### The routing prefix may be expressed in Classless Inter-Domain Routing (CIDR) notation written as the first address of a network, followed by a slash character (/), and ending with the bit-length of the prefix. For example, 198.51.100.0/24 is the prefix of the Internet Protocol version 4 network starting at the given address, having 24 bits allocated for the network prefix, and the remaining 8 bits reserved for host addressing. Addresses in the range 198.51.100.0 to 198.51.100.255 belong to this network, with 198.51.100.255 as the subnet broadcast address. The IPv6 address specification 2001:db8::/32 is a large address block with 296 addresses, having a 32-bit routing prefix. 
### For IPv4, a network may also be characterized by its subnet mask or netmask, which is the bitmask that, when applied by a bitwise AND operation to any IP address in the network, yields the routing prefix. Subnet masks are also expressed in dot-decimal notation like an IP address. For example, the prefix 198.51.100.0/24 would have the subnet mask 255.255.255.0. 
### Traffic is exchanged between subnetworks through routers when the routing prefixes of the source address and the destination address differ. A router serves as a logical or physical boundary between the subnets. 
### The benefits of subnetting an existing network vary with each deployment scenario. In the address allocation architecture of the Internet using CIDR and in large organizations, it is necessary to allocate address space efficiently. Subnetting may also enhance routing efficiency, or have advantages in network management when subnetworks are administratively controlled by different entities in a larger organization. Subnets may be arranged logically in a hierarchical architecture, partitioning an organization's network address space into a tree-like routing structure, or other structures such as meshes.
## Network addressing and routing  

### Computers participating in a network such as the Internet each have at least one network address. Usually, this address is unique to each device and can either be configured automatically with the Dynamic Host Configuration Protocol (DHCP) by a network server, manually by an administrator, or automatically by stateless address autoconfiguration. 
### An address fulfills the functions of identifying the host and locating it on the network. The most common network addressing architecture is Internet Protocol version 4 (IPv4), but its successor, IPv6, has been increasingly deployed since approximately 2006. An IPv4 address consists of 32 bits. An IPv6 address consists of 128 bits. In both systems, an IP address is divided into two logical parts, the network prefix and the host identifier. All hosts on a subnetwork have the same network prefix. This prefix occupies the most-significant bits of the address. The number of bits allocated within a network to the prefix may vary between subnets, depending on the network architecture. The host identifier is a unique local identification and is either a host number on the local network or an interface identifier. 
### This addressing structure permits the selective routing of IP packets across multiple networks via special gateway computers, called routers, to a destination host if the network prefixes of origination and destination hosts differ, or sent directly to a target host on the local network if they are the same. Routers constitute logical or physical borders between the subnets, and manage traffic between them. Each subnet is served by a designated default router but may consist internally of multiple physical Ethernet segments interconnected by network switches. 
### The routing prefix of an address is identified by the subnet mask, written in the same form used for IP addresses. For example, the subnet mask for a routing prefix that is composed of the most-significant 24 bits of an IPv4 address is written as 255.255.255.0. 
### The modern standard form of specification of the network prefix is CIDR notation, used for both IPv4 and IPv6. It counts the number of bits in the prefix and appends that number to the address after a slash (/) character separator. This notation was introduced with Classless Inter-Domain Routing (CIDR). 
### In IPv6 this is the only standards-based form to denote network or routing prefixes. 
### For example, the IPv4 network 192.0.2.0 with the subnet mask 255.255.255.0 is written as 192.0.2.0/24, and the IPv6 notation 2001:db8::/32 designates the address 2001:db8:: and its network prefix consisting of the most significant 32 bits. 
### In classful networking in IPv4, before the introduction of CIDR, the network prefix could be directly obtained from the IP address, based on its highest order bit sequence. This determined the class (A, B, C) of the address and therefore the subnet mask. Since the introduction of CIDR, however, the assignment of an IP address to a network interface requires two parameters, the address and a subnet mask. 
### Given an IPv4 source address, its associated subnet mask, and the destination address, a router can determine whether the destination is on a locally connected network or a remote network. The subnet mask of the destination is not needed, and is generally not known to a router. For IPv6, however, on-link determination is different in detail and requires the Neighbor Discovery Protocol (NDP). IPv6 address assignment to an interface carries no requirement of a matching on-link prefix and vice versa, with the exception of link-local addresses. 
### Since each locally connected subnet must be represented by a separate entry in the routing tables of each connected router, subnetting increases routing complexity. However, by careful design of the network, routes to collections of more distant subnets within the branches of a tree hierarchy can be aggregated into a supernetwork and represented by single routes.
## Internet Protocol version 4 
## Determining the network prefix  
### An IPv4 subnet mask consists of 32 bits; it is a sequence of ones (1) followed by a block of zeros (0). The ones indicate bits in the address used for the network prefix and the trailing block of zeros designates that part as being the host identifier. 
### The following example shows the separation of the network prefix and the host identifier from an address (192.0.2.130) and its associated /24 subnet mask (255.255.255.0). The operation is visualized in a table using binary address formats. 

### The result of the bitwise AND operation of IP address and the subnet mask is the network prefix 192.0.2.0. The host part, which is 130, is derived by the bitwise AND operation of the address and the one's complement of the subnet mask.
## Subnetting  
### Subnetting is the process of designating some high-order bits from the host part as part of the network prefix and adjusting the subnet mask appropriately. This divides a network into smaller subnets. The following diagram modifies the above example by moving 2 bits from the host part to the network prefix to form four smaller subnets each one quarter of the previous size.
## Special addresses and subnets  
### IPv4 uses specially designated address formats to facilitate recognition of special address functionality. The first and the last subnets obtained by subnetting a larger network have traditionally had a special designation and, early on, special usage implications. In addition, IPv4 uses the all ones host address, i.e. the last address within a network, for broadcast transmission to all hosts on the link. 

### The first subnet obtained from subnetting a larger network has all bits in the subnet bit group set to zero (0). It is therefore called subnet zero. The last subnet obtained from subnetting a larger network has all bits in the subnet bit group set to one (1). It is therefore called the all-ones subnet.The IETF originally discouraged the production use of these two subnets. When the prefix length is not available, the larger network and the first subnet have the same address, which may lead to confusion. Similar confusion is possible with the broadcast address at the end of the last subnet. Therefore, reserving the subnet values consisting of all zeros and all ones on the public Internet was recommended, reducing the number of available subnets by two for each subnetting. This inefficiency was removed, and the practice was declared obsolete in 1995 and is only relevant when dealing with legacy equipment.Although the all-zeros and the all-ones host values are reserved for the network address of the subnet and its broadcast address, respectively, in systems using CIDR all subnets are available in a subdivided network. For example, a /24 network can be divided into sixteen usable /28 networks. Each broadcast address, i.e. *.15, *.31, \u2026, *.255, reduces only the host count in each subnetwork.
## Subnet host count  
### The number of subnetworks available and the number of possible hosts in a network may be readily calculated. For instance, the 192.168.5.0/24 network may be subdivided into the following four /26 subnets. The highlighted two address bits become part of the network number in this process. 

### The remaining bits after the subnet bits are used for addressing hosts within the subnet. In the above example, the subnet mask consists of 26 bits, making it 255.255.255.192, leaving 6 bits for the host identifier. This allows for 62 host combinations (26\u22122). 
### In general, the number of available hosts on a subnet is 2h\u22122, where h is the number of bits used for the host portion of the address. The number of available subnets is 2n, where n is the number of bits used for the network portion of the address. 
### There is an exception to this rule for 31-bit subnet masks, which means the host identifier is only one bit long for two permissible addresses. In such networks, usually point-to-point links, only two hosts (the end points) may be connected and a specification of network and broadcast addresses is not necessary.
## Internet Protocol version 6  

### The design of the IPv6 address space differs significantly from IPv4. The primary reason for subnetting in IPv4 is to improve efficiency in the utilization of the relatively small address space available, particularly to enterprises. No such limitations exist in IPv6, as the large address space available, even to end-users, is not a limiting factor. 
### As in IPv4, subnetting in IPv6 is based on the concepts of variable-length subnet masking (VLSM) and the Classless Inter-Domain Routing methodology. It is used to route traffic between the global allocation spaces and within customer networks between subnets and the Internet at large. 
### A compliant IPv6 subnet always uses addresses with 64 bits in the host identifier. Given the address size of 128 bits, it therefore has a /64 routing prefix. Although it is technically possible to use smaller subnets, they are impractical for local area networks based on Ethernet technology, because 64 bits are required for stateless address autoconfiguration. The Internet Engineering Task Force recommends the use of /127 subnets for point-to-point links, which have only two hosts.IPv6 does not implement special address formats for broadcast traffic or network numbers, and thus all addresses in a subnet are acceptable for host addressing. The all-zeroes address is reserved as the subnet-router anycast address.In the past, the recommended allocation for an IPv6 customer site was an address space with a 48-bit (/48) prefix. However, this recommendation was revised to encourage smaller blocks, for example using 56-bit prefixes. Another common allocation size for residential customer networks has a 64-bit prefix.
## See also  
### Autonomous system (Internet)
## References 
## Further reading  
### Requirements for IPv4 Routers. doi:10.17487/RFC1812. RFC 1812. 
### Utility of subnets of Internet networks. doi:10.17487/RFC0917. RFC 917. 
### DNS Encodings of Network Names and Other Type. doi:10.17487/RFC1101. RFC 1101. 
### Blank, Andrew G. (2006). TCP/IP Foundations. Wiley. ISBN 9780782151138. 
### Lammle, Todd (2005). CCNA Cisco Certified Network Associate Study Guide 5th Edition. San Francisco, London: Sybex. 
### Groth, David; Skandier, Toby (2005). Network + Study Guide (4th ed.). San Francisco, London: Wiley.
## External links  
### Cisco-IP Addressing and Subnetting for New Users 
### Subnetworking at Curlie 
### Netmask Quick Reference Chart"
## References
### [Reference](http://www.cisco.com/en/US/tech/tk365/technologies_tech_note09186a00800a67f5.shtml) - http://www.cisco.com/en/US/tech/tk365/technologies_tech_note09186a00800a67f5.shtml
### [Reference](http://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a0080093f18.shtml) - http://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a0080093f18.shtml
### [Reference](http://www.getipv6.info/index.php?title=IPv6_Addressing_Plans&oldid=2998) - http://www.getipv6.info/index.php?title=IPv6_Addressing_Plans&oldid=2998
### [Reference](http://unixwiz.net/techtips/netmask-ref.html) - http://unixwiz.net/techtips/netmask-ref.html
### [Reference](http://doi.org/10.17487%2FRFC0917) - http://doi.org/10.17487%2FRFC0917
### [Reference](http://doi.org/10.17487%2FRFC0950) - http://doi.org/10.17487%2FRFC0950
### [Reference](http://doi.org/10.17487%2FRFC1101) - http://doi.org/10.17487%2FRFC1101
### [Reference](http://doi.org/10.17487%2FRFC1122) - http://doi.org/10.17487%2FRFC1122
### [Reference](http://doi.org/10.17487%2FRFC1812) - http://doi.org/10.17487%2FRFC1812
### [Reference](http://doi.org/10.17487%2FRFC1878) - http://doi.org/10.17487%2FRFC1878
### [Reference](http://doi.org/10.17487%2FRFC2464) - http://doi.org/10.17487%2FRFC2464
### [Reference](http://doi.org/10.17487%2FRFC3021) - http://doi.org/10.17487%2FRFC3021
### [Reference](http://doi.org/10.17487%2FRFC4291) - http://doi.org/10.17487%2FRFC4291
### [Reference](http://doi.org/10.17487%2FRFC4632) - http://doi.org/10.17487%2FRFC4632
### [Reference](http://doi.org/10.17487%2FRFC4861) - http://doi.org/10.17487%2FRFC4861
### [Reference](http://doi.org/10.17487%2FRFC4862) - http://doi.org/10.17487%2FRFC4862
### [Reference](http://doi.org/10.17487%2FRFC5942) - http://doi.org/10.17487%2FRFC5942
### [Reference](http://doi.org/10.17487%2FRFC6164) - http://doi.org/10.17487%2FRFC6164
### [Reference](http://doi.org/10.17487%2FRFC6177) - http://doi.org/10.17487%2FRFC6177
### [Reference](http://doi.org/10.17487%2FRFC6547) - http://doi.org/10.17487%2FRFC6547
### [Reference](http://www.worldcat.org/issn/2070-1721) - http://www.worldcat.org/issn/2070-1721
### [Reference](https://d-nb.info/gnd/4588594-1) - https://d-nb.info/gnd/4588594-1
### [Reference](https://curlie.org/Computers/Internet/Protocols/IP/Addressing/) - https://curlie.org/Computers/Internet/Protocols/IP/Addressing/
### [Reference](https://datatracker.ietf.org/doc/html/rfc1101) - https://datatracker.ietf.org/doc/html/rfc1101
### [Reference](https://datatracker.ietf.org/doc/html/rfc1122) - https://datatracker.ietf.org/doc/html/rfc1122
### [Reference](https://datatracker.ietf.org/doc/html/rfc1122#section-3.3.1) - https://datatracker.ietf.org/doc/html/rfc1122#section-3.3.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1812) - https://datatracker.ietf.org/doc/html/rfc1812
### [Reference](https://datatracker.ietf.org/doc/html/rfc1878) - https://datatracker.ietf.org/doc/html/rfc1878
### [Reference](https://datatracker.ietf.org/doc/html/rfc2464) - https://datatracker.ietf.org/doc/html/rfc2464
### [Reference](https://datatracker.ietf.org/doc/html/rfc2464#section-4) - https://datatracker.ietf.org/doc/html/rfc2464#section-4
### [Reference](https://datatracker.ietf.org/doc/html/rfc3021) - https://datatracker.ietf.org/doc/html/rfc3021
### [Reference](https://datatracker.ietf.org/doc/html/rfc4291) - https://datatracker.ietf.org/doc/html/rfc4291
### [Reference](https://datatracker.ietf.org/doc/html/rfc4291#section-2) - https://datatracker.ietf.org/doc/html/rfc4291#section-2
### [Reference](https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.1) - https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc4291#section-2.6.1) - https://datatracker.ietf.org/doc/html/rfc4291#section-2.6.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc4632) - https://datatracker.ietf.org/doc/html/rfc4632
### [Reference](https://datatracker.ietf.org/doc/html/rfc4861) - https://datatracker.ietf.org/doc/html/rfc4861
### [Reference](https://datatracker.ietf.org/doc/html/rfc4862) - https://datatracker.ietf.org/doc/html/rfc4862
### [Reference](https://datatracker.ietf.org/doc/html/rfc4862#section-5.5.3) - https://datatracker.ietf.org/doc/html/rfc4862#section-5.5.3
### [Reference](https://datatracker.ietf.org/doc/html/rfc5942) - https://datatracker.ietf.org/doc/html/rfc5942
### [Reference](https://datatracker.ietf.org/doc/html/rfc6164) - https://datatracker.ietf.org/doc/html/rfc6164
### [Reference](https://datatracker.ietf.org/doc/html/rfc6177) - https://datatracker.ietf.org/doc/html/rfc6177
### [Reference](https://datatracker.ietf.org/doc/html/rfc6547) - https://datatracker.ietf.org/doc/html/rfc6547
### [Reference](https://datatracker.ietf.org/doc/html/rfc917) - https://datatracker.ietf.org/doc/html/rfc917
### [Reference](https://datatracker.ietf.org/doc/html/rfc950) - https://datatracker.ietf.org/doc/html/rfc950
### [Reference](https://datatracker.ietf.org/doc/html/rfc950#page-6) - https://datatracker.ietf.org/doc/html/rfc950#page-6
### [Reference](https://www.wikidata.org/wiki/Q11414#identifiers) - https://www.wikidata.org/wiki/Q11414#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/1/14/Subnetting_Concept-en.svg) - https://upload.wikimedia.org/wikipedia/commons/1/14/Subnetting_Concept-en.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/b/b3/Subnetting_Concept.svg) - https://upload.wikimedia.org/wikipedia/commons/b/b3/Subnetting_Concept.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg) - https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg