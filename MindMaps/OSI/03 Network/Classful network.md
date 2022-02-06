# Classful network
## [URL](https://en.wikipedia.org/wiki/Classful_network) - https://en.wikipedia.org/wiki/Classful_network
## Catagories
### All articles needing additional references
### All articles with unsourced statements
### Articles needing additional references from March 2018
### Articles with short description
### Articles with unsourced statements from July 2018
### Articles with unsourced statements from March 2018
### IP addresses
### Internet architecture
### Short description matches Wikidata
### "A classful network is a network addressing architecture used in the Internet from 1981 until the introduction of Classless Inter-Domain Routing in 1993. The method divides the IP address space for Internet Protocol version 4 (IPv4) into five address classes based on the leading four address bits. Classes A, B, and C provide unicast addresses for networks of three different network sizes. Class D is for multicast networking and the class E address range is reserved for future or experimental purposes. 
### Since its discontinuation, remnants of classful network concepts have remained in practice only in limited scope in the default configuration parameters of some network software and hardware components, most notably in the default configuration of subnet masks.
## Background  
### In the original address definition, the most significant eight bits of the 32-bit IPv4 address was the network number field which specified the particular network a host was attached to. The remaining 24 bits specified the local address, also called rest field (the rest of the address), which uniquely identified a host connected to that network. This format was sufficient at a time when only a few large networks existed, such as the ARPANET (network number 10), and before the wide proliferation of local area networks (LANs). As a consequence of this architecture, the address space supported only a low number (254) of independent networks. 
### Before the introduction of address classes, the only address blocks available were these large blocks which later became known as Class A networks. As a result, some organizations involved in the early development of the Internet received address space allocations far larger than they would ever need (2,147,483,648 IP addresses each!). It became clear early in the growth of the network that this would be a critical scalability limitation.
## Introduction of address classes  
### Expansion of the network had to ensure compatibility with the existing address space and the IPv4 packet structure, and avoid the renumbering of the existing networks. The solution was to expand the definition of the network number field to include more bits, allowing more networks to be designated, each potentially having fewer hosts. Since all existing network numbers at the time were smaller than 64, they had only used the 6 least-significant bits of the network number field. Thus it was possible to use the most-significant bits of an address to introduce a set of address classes while preserving the existing network numbers in the first of these classes. 
### The new addressing architecture was introduced by RFC 791 in 1981 as a part of the specification of the Internet Protocol. It divided the address space into primarily three address formats, henceforth called address classes, and left a fourth range reserved to be defined later. 
### The first class, designated as Class A, contained all addresses in which the most significant bit is zero. The network number for this class is given by the next 7 bits, therefore accommodating 128 networks in total, including the zero network, and including the IP networks already allocated. A Class B network was a network in which all addresses had the two most-significant bits set to 1 and 0 respectively. For these networks, the network address was given by the next 14 bits of the address, thus leaving 16 bits for numbering host on the network for a total of 65536 addresses per network. Class C was defined with the 3 high-order bits set to 1, 1, and 0, and designating the next 21 bits to number the networks, leaving each network with 256 local addresses. 
### The leading bit sequence 111 designated an at-the-time unspecified addressing mode (\"escape to extended addressing mode\"), which was later subdivided as Class D (1110) for multicast addressing, while leaving as reserved for future use the 1111 block designated as Class E.This architecture change extended the addressing capacity of the Internet but did not prevent IP address exhaustion. The problem was that many sites needed larger address blocks than a Class C network provided, and therefore they received a Class B block, which was in most cases much larger than required. Due to the rapid growth of the Internet, the pool of unassigned Class B addresses (214, or about 16,000) was rapidly being depleted. Classful networking was replaced by Classless Inter-Domain Routing (CIDR), starting in 1993 with the specification of RFC 1518 and RFC 1519, to attempt to solve this problem.
## Classful addressing definition  
### Under classful network addressing, the 32-bit IPv4 address space was partitioned into 5 classes (A-E) as shown in the following tables. 

### ClassesBit-wise representationIn the following bit-wise representation, 

### n indicates a bit used for the network ID. 
### H indicates a bit used for the host ID. 
### X indicates a bit without a specified purpose.Class A 
 0.  0.  0.  0  00000000.00000000.00000000.00000000 
### 127.255.255.255  01111111.11111111.11111111.11111111 
                 0nnnnnnn.HHHHHHHH.HHHHHHHH.HHHHHHHH 

### Class B 
### 128.  0.  0.  0  10000000.00000000.00000000.00000000 
### 191.255.255.255  10111111.11111111.11111111.11111111 
                 10nnnnnn.nnnnnnnn.HHHHHHHH.HHHHHHHH 

### Class C 
### 192.  0.  0.  0  11000000.00000000.00000000.00000000 
### 223.255.255.255  11011111.11111111.11111111.11111111 
                 110nnnnn.nnnnnnnn.nnnnnnnn.HHHHHHHH 

### Class D 
### 224.  0.  0.  0  11100000.00000000.00000000.00000000 
### 239.255.255.255  11101111.11111111.11111111.11111111 
                 1110XXXX.XXXXXXXX.XXXXXXXX.XXXXXXXX 

### Class E 
### 240.  0.  0.  0  11110000.00000000.00000000.00000000 
### 255.255.255.255  11111111.11111111.11111111.11111111 
                 1111XXXX.XXXXXXXX.XXXXXXXX.XXXXXXXX 

### The number of addresses usable for addressing specific hosts in each network is always 2N - 2, where N is the number of rest field bits, and the subtraction of 2 adjusts for the use of the all-bits-zero host value to represent the network address and the all-bits-one host value for use as a broadcast address. Thus, for a Class C address with 8 bits available in the host field, the maximum number of hosts is 254. 
### Today, IP addresses are associated with a subnet mask. This was not required in a classful network because the mask was implied by the address itself; any network device would inspect the first few bits of the IP address to determine the class of the address and thus its netmask. 
### The blocks numerically at the start and end of classes A, B and C were originally reserved for special addressing or future features, i.e., 0.0.0.0/8 and 127.0.0.0/8 are reserved in former class A; 128.0.0.0/16 and 191.255.0.0/16 were reserved in former class B but are now available for assignment; 192.0.0.0/24 and 223.255.255.0/24 are reserved in former class C. While the 127.0.0.0/8 network is a Class A network, it is designated for loopback and cannot be assigned to a network.Class D is reserved for multicast and cannot be used for regular unicast traffic. Class E is reserved and cannot be used on the public Internet. Many older routers will not accept using it in any context.
## See also  
### IPv4 subnetting reference 
### List of assigned /8 IPv4 address blocks
## Notes 
## References 
## External links  
### IANA, Current IPv4 /8 delegations 
### Overview of IP addressing, both classless and classful (404) 
### Postel, Jon (September 1981). Assigned Numbers. doi:10.17487/RFC0790. RFC 790., which includes a list of Class A networks as of that date."
## References
### [Reference](http://scholar.google.com/scholar?q=%22Classful+network%22) - http://scholar.google.com/scholar?q=%22Classful+network%22
### [Reference](http://www.google.com/search?&q=%22Classful+network%22&tbs=bkt:s&tbm=bks) - http://www.google.com/search?&q=%22Classful+network%22&tbs=bkt:s&tbm=bks
### [Reference](http://www.google.com/search?as_eq=wikipedia&q=%22Classful+network%22) - http://www.google.com/search?as_eq=wikipedia&q=%22Classful+network%22
### [Reference](http://www.google.com/search?tbm=nws&q=%22Classful+network%22+-wikipedia&tbs=ar:1) - http://www.google.com/search?tbm=nws&q=%22Classful+network%22+-wikipedia&tbs=ar:1
### [Reference](http://www.google.com/search?tbs=bks:1&q=%22Classful+network%22+-wikipedia) - http://www.google.com/search?tbs=bks:1&q=%22Classful+network%22+-wikipedia
### [Reference](http://doi.org/10.17487%2FRFC0760) - http://doi.org/10.17487%2FRFC0760
### [Reference](http://doi.org/10.17487%2FRFC0790) - http://doi.org/10.17487%2FRFC0790
### [Reference](http://doi.org/10.17487%2FRFC0791) - http://doi.org/10.17487%2FRFC0791
### [Reference](http://tools.ietf.org/html/rfc5735) - http://tools.ietf.org/html/rfc5735
### [Reference](http://tools.ietf.org/html/rfc988) - http://tools.ietf.org/html/rfc988
### [Reference](https://www.ge.com/digital/documentation/cimplicity/version10/oxy_ex-2/advanced_features/topics/g_cimplicity_advanced_features_multicast_ip_addr.html) - https://www.ge.com/digital/documentation/cimplicity/version10/oxy_ex-2/advanced_features/topics/g_cimplicity_advanced_features_multicast_ip_addr.html
### [Reference](https://web.archive.org/web/20100430190605/http://www.iana.org/assignments/ipv4-address-space/) - https://web.archive.org/web/20100430190605/http://www.iana.org/assignments/ipv4-address-space/
### [Reference](https://web.archive.org/web/20110401192204/http://oreilly.com/catalog/coreprot/chapter/appb.html) - https://web.archive.org/web/20110401192204/http://oreilly.com/catalog/coreprot/chapter/appb.html
### [Reference](https://datatracker.ietf.org/doc/html/rfc760) - https://datatracker.ietf.org/doc/html/rfc760
### [Reference](https://datatracker.ietf.org/doc/html/rfc760#section-3.1) - https://datatracker.ietf.org/doc/html/rfc760#section-3.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc790) - https://datatracker.ietf.org/doc/html/rfc790
### [Reference](https://datatracker.ietf.org/doc/html/rfc791) - https://datatracker.ietf.org/doc/html/rfc791
### [Reference](https://datatracker.ietf.org/doc/rfcmarkup?url=https://www.rfc-editor.org/ien/ien46.txt) - https://datatracker.ietf.org/doc/rfcmarkup?url=https://www.rfc-editor.org/ien/ien46.txt
### [Reference](https://www.jstor.org/action/doBasicSearch?Query=%22Classful+network%22&acc=on&wc=on) - https://www.jstor.org/action/doBasicSearch?Query=%22Classful+network%22&acc=on&wc=on
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/6/60/Internet_map_in_February_82.png) - https://upload.wikimedia.org/wikipedia/commons/6/60/Internet_map_in_February_82.png
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg