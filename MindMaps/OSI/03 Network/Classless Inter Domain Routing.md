# Classless Inter-Domain Routing
## [URL](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) - https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing
## Catagories
### All articles with unsourced statements
### Articles with short description
### Articles with unsourced statements from April 2019
### IP addresses
### Internet Standards
### Internet architecture
### Routing
### Short description is different from Wikidata
### "Classless Inter-Domain Routing (CIDR ) is a method for allocating IP addresses and for IP routing. The Internet Engineering Task Force introduced CIDR in 1993 to replace the previous classful network addressing architecture on the Internet. Its goal was to slow the growth of routing tables on routers across the Internet, and to help slow the rapid exhaustion of IPv4 addresses.IP addresses are described as consisting of two groups of bits in the address: the most significant bits are the network prefix, which identifies a whole network or subnet, and the least significant set forms the host identifier, which specifies a particular interface of a host on that network. This division is used as the basis of traffic routing between IP networks and for address allocation policies. 
### Whereas classful network design for IPv4 sized the network prefix as one or more 8-bit groups, resulting in the blocks of Class A, B, or C addresses, under CIDR address space is allocated to Internet service providers and end users on any address-bit boundary. In IPv6, however, the interface identifier has a fixed size of 64 bits by convention, and smaller subnets are never allocated to end users.  
### CIDR encompasses several concepts. It is based on variable-length subnet masking (VLSM) which allows the specification of arbitrary-length prefixes. CIDR introduced a new method of representation for IP addresses, now commonly known as CIDR notation, in which an address or routing prefix is written with a suffix indicating the number of bits of the prefix, such as 192.0.2.0/24 for IPv4, and 2001:db8::/32 for IPv6. CIDR introduced an administrative process of allocating address blocks to organizations based on their actual and short-term projected needs. The aggregation of multiple contiguous prefixes resulted in supernets in the larger Internet, which whenever possible are advertised as aggregates, thus reducing the number of entries in the global routing table.
## Background  
### An IP address is interpreted as composed of two parts: a network-identifying prefix followed by a host identifier within that network.  In automating the routing of packets to a given IP network, the question is how many bits of the address are in the network prefix, and how many are in the host identifier.  In the previous IPv4 classful network architecture, the top three bits of the 32-bit IP address defined how many bits were in the network prefix: 
### The advantage of this system is that the network prefix could be determined for any IP address without any further information.  The disadvantage is because only three sizes are available, networks were usually too big or too small for most organizations to use.  The smallest allocation and routing block contained 256 addresses \u2014 larger than necessary for personal or department networks, but too small for most enterprises.  The next larger block contained 65536 addresses\u2014too large to be used efficiently even by large organizations.  But for network users who needed more than 65536 addresses, the only other size gave them far too many, more than 16 million.  This led to inefficiencies in address use as well as inefficiencies in routing, because it required a large number of allocated class-C networks with individual route announcements, being geographically dispersed with little opportunity for route aggregation. 
### During the first decade of the Internet after the invention of the Domain Name System (DNS) it became apparent that the devised system based on the classful network scheme of allocating the IP address space and the routing of IP packets was not scalable. This led to the successive development of subnetting and CIDR.  The formerly meaningful class distinctions based on the top 3 address bits were removed, and the new system was described as being classless, with respect to the old system, which became known as classful.  Routing protocols were revised to carry not just Internet addresses, but also their matching subnet masks.  Implementing CIDR required every host and router on the Internet to be reprogrammed in small ways\u2014no small feat at a time when the Internet was entering a period of rapid growth.  In 1993, the Internet Engineering Task Force published a new set of standards, RFC 1518 and RFC 1519, to define this new concept of allocation of IP address blocks and new methods of routing IPv4 packets. An updated version of the specification was published as RFC 4632 in 2006.After a period of experimenting with various alternatives, Classless Inter-Domain Routing was based on variable-length subnet masking (VLSM), which allows each network to be allocated or divided into various power-of-two-sized subnets, providing the opportunity to size each network or subnet appropriately for local needs. Variable-length subnet masks were mentioned as one alternative in RFC 950.  Techniques for grouping addresses for common operations were based on the concept of cluster addressing, first proposed by Carl-Herbert Rokitansky.
## CIDR notation  
### CIDR notation is a compact representation of an IP address and its associated network mask. The notation was invented by Phil Karn in the 1980s.  CIDR notation specifies an IP address, a slash ('/') character, and a decimal number. The decimal number is the count of consecutive leading 1-bits (from left to right) in the network mask.  The number can also be thought of as the width (in bits) of the network prefix.  The IP address in CIDR notation is always represented according to the standards for IPv4 or IPv6. 
### The address may denote a specific interface address (including a host identifier, such as 10.0.0.1/8), or it may be the beginning address of an entire network (using a host identifier of 0, as in 10.0.0.0/8 or its equivalent 10/8). CIDR notation can even be used with no IP address at all, e.g. when referring to a /24 as a generic description of an IPv4 network that has a 24-bit prefix and 8-bit host numbers. 
### For example: 

### 198.51.100.14/24 represents the IPv4 address 198.51.100.14 and its associated network prefix 198.51.100.0, or equivalently, its subnet mask 255.255.255.0, which has 24 leading 1-bits. 
### the IPv4 block 198.51.100.0/22 represents the 1024 IPv4 addresses from 198.51.100.0 to 198.51.103.255. 
### the IPv6 block 2001:db8::/48 represents the block of IPv6 addresses from 2001:db8:0:0:0:0:0:0 to 2001:db8:0:ffff:ffff:ffff:ffff:ffff. 
### ::1/128 represents the IPv6 loopback address. Its prefix length is 128 which is the number of bits in the address.In IPv4, what is now called CIDR notation came into wide use only after the implementation of CIDR.  It does not appear in the original CIDR standards, which instead used a dotted-decimal subnet mask after the slash; for example, 192.24.12.0/255.255.252.0.  Describing the network prefix's width as a single number (192.24.12.0/22) was easier for network administrators to conceptualize and to mentally calculate, so it gradually became incorporated into later standards documents and into network configuration interfaces. 
### The number of addresses inside a network or subnet may be calculated as 2address length \u2212 prefix length, where address length is 128 for IPv6 and 32 for IPv4. For example, in IPv4, the prefix length /29 gives: 232\u221229  23  8 addresses.
## Subnet masks  
### A subnet mask is a bitmask that encodes the prefix length associated with an IPv4 address or network in quad-dotted notation: 32 bits, starting with a number of 1-bits equal to the prefix length, ending with 0-bits, and encoded in four-part dotted-decimal format: 255.255.255.0.  A subnet mask encodes the same information as a prefix length but predates the advent of CIDR. In CIDR notation, the prefix bits are always contiguous. Subnet masks were allowed by RFC 950 to specify non-contiguous bits until RFC 4632:\u200aSection 5.1\u200a stated that the mask must be left contiguous. Given this constraint, a subnet mask and CIDR notation serve exactly the same function.
## CIDR blocks  
### CIDR is principally a bitwise, prefix-based standard for the representation of IP addresses and their routing properties. It facilitates routing by allowing blocks of addresses to be grouped into single routing table entries. These groups, commonly called CIDR blocks, share an initial sequence of bits in the binary representation of their IP addresses. IPv4 CIDR blocks are identified using a syntax similar to that of IPv4 addresses: a dotted-decimal address, followed by a slash, then a number from 0 to 32, i.e., a.b.c.d/n. The dotted decimal portion is the IPv4 address. The number following the slash is the prefix length, the number of shared initial bits, counting from the most-significant bit of the address. When emphasizing only the size of a network, the address portion of the notation is usually omitted. Thus, a /20 block is a CIDR block with an unspecified 20-bit prefix. 
### An IP address is part of a CIDR block and is said to match the CIDR prefix if the initial n bits of the address and the CIDR prefix are the same. An IPv4 address is 32 bits so an n-bit CIDR prefix leaves 32 \u2212 n bits unmatched, meaning that 232\u2212n IPv4 addresses match a given n-bit CIDR prefix. Shorter CIDR prefixes match more addresses, while longer prefixes match fewer. In the case of overlaid CIDR blocks, an address can match multiple CIDR prefixes of different lengths. 

### CIDR is also used for IPv6 addresses and the syntax semantic is identical. The prefix length can range from 0 to 128, due to the larger number of bits in the address. However, by convention, a subnet on broadcast MAC layer networks always has 64-bit host identifiers. Larger prefixes are rarely used even on point-to-point links.
## Assignment of CIDR blocks  
### The Internet Assigned Numbers Authority (IANA) issues to regional Internet registries (RIRs) large, short-prefix CIDR blocks. However, a /8 (with over sixteen million addresses) is the largest block IANA will allocate. For example, 62.0.0.0/8 is administered by RIPE NCC, the European RIR. The RIRs, each responsible for a single, large, geographic area, such as Europe or North America, subdivide these blocks and allocate subnets to local Internet registries (LIRs). Similar subdividing may be repeated several times at lower levels of delegation. End-user networks receive subnets sized according to their projected short-term need.  Networks served by a single ISP are encouraged by IETF recommendations to obtain IP address space directly from their ISP.  Networks served by multiple ISPs, on the other hand, may obtain provider-independent address space directly from the appropriate RIR. 

### For example, in the late 1990s, the IP address 208.130.29.33 (since reassigned) was used by www.freesoft.org. An analysis of this address identified three CIDR prefixes. 208.128.0.0/11, a large CIDR block containing over 2 million addresses, had been assigned by ARIN (the North American RIR) to MCI. Automation Research Systems (ARS), a Virginia VAR, leased an Internet connection from MCI and was assigned the 208.130.28.0/22 block, capable of addressing just over 1000 devices. ARS used a /24 block for its publicly accessible servers, of which 208.130.29.33 was one. All of these CIDR prefixes would be used, at different locations in the network. Outside MCI's network, the 208.128.0.0/11 prefix would be used to direct to MCI traffic bound not only for 208.130.29.33, but also for any of the roughly two million IP addresses with the same initial 11 bits. Within MCI's network, 208.130.28.0/22 would become visible, directing traffic to the leased line serving ARS. Only within the ARS corporate network would the 208.130.29.0/24 prefix have been used.
## IPv4 CIDR blocks  
### In common usage, the first address in a subnet, all binary zero in the host identifier, is reserved for referring to the network itself, while the last address, all binary one in the host identifier, is used as a broadcast address for the network; this reduces the number of addresses available for hosts by 2.  As a result, a /31 network, with one binary digit in the host identifier, would be unusable, as such a subnet would provide no available host addresses after this reduction. RFC 3021 creates an exception to the \"host all ones\" and \"host all zeros\" rules to make /31 networks usable for point-to-point links. /32 addresses (single-host network) must be accessed by explicit routing rules, as there is no room in such a network for a gateway. 
### In routed subnets larger than /31 or /32, the number of available host addresses is usually reduced by two, namely the largest address, which is reserved as the broadcast address, and the smallest address, which identifies the network itself.
## IPv6 CIDR blocks  

### The large address size used in IPv6 permitted implementation of worldwide route summarization and guaranteed sufficient address pools at each site. The standard subnet size for IPv6 networks is a /64 block, which is required for the operation of stateless address autoconfiguration. At first, the IETF recommended in RFC 3177 as a best practice that all end sites receive a /48 address allocation, however, criticism and reevaluation of actual needs and practices has led to more flexible allocation recommendations in RFC 6177 suggesting a significantly smaller allocation for some sites, such as a /56 block for home networks. 
### This IPv6 subnetting reference lists the sizes for IPv6 subnetworks. Different types of network links may require different subnet sizes. The subnet mask separates the bits of the network identifier prefix from the bits of the interface identifier. Selecting a smaller prefix size results in fewer number of networks covered, but with more addresses within each network. 
### 2001:0db8:0123:4567:89ab:cdef:1234:5678 
### |||| |||| |||| |||| |||| |||| |||| |||| 
### |||| |||| |||| |||| |||| |||| |||| |||128     Single end-points and loopback 
### |||| |||| |||| |||| |||| |||| |||| |||127   Point-to-point links (inter-router) 
### |||| |||| |||| |||| |||| |||| |||| ||124 
### |||| |||| |||| |||| |||| |||| |||| |120 
### |||| |||| |||| |||| |||| |||| |||| 116 
### |||| |||| |||| |||| |||| |||| |||112 
### |||| |||| |||| |||| |||| |||| ||108 
### |||| |||| |||| |||| |||| |||| |104 
### |||| |||| |||| |||| |||| |||| 100 
### |||| |||| |||| |||| |||| |||96 
### |||| |||| |||| |||| |||| ||92 
### |||| |||| |||| |||| |||| |88 
### |||| |||| |||| |||| |||| 84 
### |||| |||| |||| |||| |||80 
### |||| |||| |||| |||| ||76 
### |||| |||| |||| |||| |72 
### |||| |||| |||| |||| 68 
### |||| |||| |||| |||64   Single LAN; default prefix size for SLAAC 
### |||| |||| |||| ||60   Some (very limited) 6rd deployments (/60  16 /64 blocks) 
### |||| |||| |||| |56   Minimal end sites assignment; e.g. home network (/56  256 /64 blocks) 
### |||| |||| |||| 52   /52 block  4096 /64 blocks 
### |||| |||| |||48   Typical assignment for larger sites (/48  65536 /64 blocks) 
### |||| |||| ||44 
### |||| |||| |40 
### |||| |||| 36   possible future local Internet registry (LIR) extra-small allocations 
### |||| |||32   LIR minimum allocations 
### |||| ||28   LIR medium allocations 
### |||| |24   LIR large allocations 
### |||| 20   LIR extra large allocations 
### |||16 
### ||12   Regional Internet registry (RIR) allocations from IANA 
### |8 
### 4
## Prefix aggregation  
### CIDR provides fine-grained routing prefix aggregation. For example, if the first 20 bits of their network prefixes match, sixteen contiguous /24 networks can be aggregated and advertised to a larger network as a single /20 routing table entry. This reduces the number of routes that have to be advertised.
## See also  
### Internet protocol suite
## References 
## Further reading  
### Classless IN-ADDR.ARPA delegation. March 1998. doi:10.17487/RFC2317. RFC 2317. 
### CIDR and Classful Routing. August 1995. doi:10.17487/RFC1817. RFC 1817.
## External links  
### CIDR Report (updated daily)"
## References
### [Reference](http://www.getipv6.info/index.php/IPv6_Addressing_Plans) - http://www.getipv6.info/index.php/IPv6_Addressing_Plans
### [Reference](http://doi.org/10.17487%2FRFC0922) - http://doi.org/10.17487%2FRFC0922
### [Reference](http://doi.org/10.17487%2FRFC0943) - http://doi.org/10.17487%2FRFC0943
### [Reference](http://doi.org/10.17487%2FRFC0950) - http://doi.org/10.17487%2FRFC0950
### [Reference](http://doi.org/10.17487%2FRFC1517) - http://doi.org/10.17487%2FRFC1517
### [Reference](http://doi.org/10.17487%2FRFC1518) - http://doi.org/10.17487%2FRFC1518
### [Reference](http://doi.org/10.17487%2FRFC1519) - http://doi.org/10.17487%2FRFC1519
### [Reference](http://doi.org/10.17487%2FRFC1812) - http://doi.org/10.17487%2FRFC1812
### [Reference](http://doi.org/10.17487%2FRFC1817) - http://doi.org/10.17487%2FRFC1817
### [Reference](http://doi.org/10.17487%2FRFC1878) - http://doi.org/10.17487%2FRFC1878
### [Reference](http://doi.org/10.17487%2FRFC2167) - http://doi.org/10.17487%2FRFC2167
### [Reference](http://doi.org/10.17487%2FRFC2317) - http://doi.org/10.17487%2FRFC2317
### [Reference](http://doi.org/10.17487%2FRFC3177) - http://doi.org/10.17487%2FRFC3177
### [Reference](http://doi.org/10.17487%2FRFC4632) - http://doi.org/10.17487%2FRFC4632
### [Reference](http://doi.org/10.17487%2FRFC6177) - http://doi.org/10.17487%2FRFC6177
### [Reference](http://www.ietf.org/mail-archive/web/ietf/current/msg24136.html) - http://www.ietf.org/mail-archive/web/ietf/current/msg24136.html
### [Reference](https://www.ripe.net/info/info-services/addressing.html) - https://www.ripe.net/info/info-services/addressing.html
### [Reference](https://web.archive.org/web/20110203130851/http://ripe.net/info/info-services/addressing.html) - https://web.archive.org/web/20110203130851/http://ripe.net/info/info-services/addressing.html
### [Reference](https://www.cidr-report.org/as2.0/) - https://www.cidr-report.org/as2.0/
### [Reference](https://www.iana.org/assignments/ipv6-unicast-address-assignments/ipv6-unicast-address-assignments.xml) - https://www.iana.org/assignments/ipv6-unicast-address-assignments/ipv6-unicast-address-assignments.xml
### [Reference](https://datatracker.ietf.org/doc/html/rfc1517) - https://datatracker.ietf.org/doc/html/rfc1517
### [Reference](https://datatracker.ietf.org/doc/html/rfc1518) - https://datatracker.ietf.org/doc/html/rfc1518
### [Reference](https://datatracker.ietf.org/doc/html/rfc1519) - https://datatracker.ietf.org/doc/html/rfc1519
### [Reference](https://datatracker.ietf.org/doc/html/rfc1812) - https://datatracker.ietf.org/doc/html/rfc1812
### [Reference](https://datatracker.ietf.org/doc/html/rfc1812#section-4.2.3.1) - https://datatracker.ietf.org/doc/html/rfc1812#section-4.2.3.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1817) - https://datatracker.ietf.org/doc/html/rfc1817
### [Reference](https://datatracker.ietf.org/doc/html/rfc1878) - https://datatracker.ietf.org/doc/html/rfc1878
### [Reference](https://datatracker.ietf.org/doc/html/rfc2167) - https://datatracker.ietf.org/doc/html/rfc2167
### [Reference](https://datatracker.ietf.org/doc/html/rfc2317) - https://datatracker.ietf.org/doc/html/rfc2317
### [Reference](https://datatracker.ietf.org/doc/html/rfc3021) - https://datatracker.ietf.org/doc/html/rfc3021
### [Reference](https://datatracker.ietf.org/doc/html/rfc3177) - https://datatracker.ietf.org/doc/html/rfc3177
### [Reference](https://datatracker.ietf.org/doc/html/rfc4632) - https://datatracker.ietf.org/doc/html/rfc4632
### [Reference](https://datatracker.ietf.org/doc/html/rfc4862) - https://datatracker.ietf.org/doc/html/rfc4862
### [Reference](https://datatracker.ietf.org/doc/html/rfc6177) - https://datatracker.ietf.org/doc/html/rfc6177
### [Reference](https://datatracker.ietf.org/doc/html/rfc922) - https://datatracker.ietf.org/doc/html/rfc922
### [Reference](https://datatracker.ietf.org/doc/html/rfc922#section-7) - https://datatracker.ietf.org/doc/html/rfc922#section-7
### [Reference](https://datatracker.ietf.org/doc/html/rfc943) - https://datatracker.ietf.org/doc/html/rfc943
### [Reference](https://datatracker.ietf.org/doc/html/rfc950) - https://datatracker.ietf.org/doc/html/rfc950
### [Reference](https://datatracker.ietf.org/doc/html/rfc950#section-2.1) - https://datatracker.ietf.org/doc/html/rfc950#section-2.1
### [Reference](https://seclists.org/nanog/2018/Dec/334) - https://seclists.org/nanog/2018/Dec/334
### [Reference](https://seclists.org/nanog/2018/Dec/368) - https://seclists.org/nanog/2018/Dec/368
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/2/26/CIDR_Address.svg) - https://upload.wikimedia.org/wikipedia/commons/2/26/CIDR_Address.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/7/7b/IP_Address_Match.svg) - https://upload.wikimedia.org/wikipedia/commons/7/7b/IP_Address_Match.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/38/IPv6_CIDR_table-en.svg) - https://upload.wikimedia.org/wikipedia/commons/3/38/IPv6_CIDR_table-en.svg