# Routing Information Protocol
## [URL](https://en.wikipedia.org/wiki/Routing_Information_Protocol) - https://en.wikipedia.org/wiki/Routing_Information_Protocol
## Catagories
### All articles with failed verification
### Articles with failed verification from January 2022
### Articles with short description
### CS1 errors: external links
### CS1 maint: uses authors parameter
### Internet Standards
### Internet protocols
### Routing protocols
### Short description matches Wikidata
### Use dmy dates from September 2020
### "The Routing Information Protocol (RIP) is one of the oldest distance-vector routing protocols which employs the hop count as a routing metric. RIP prevents routing loops by implementing a limit on the number of hops allowed in a path from source to destination. The largest number of hops allowed for RIP is 15, which limits the size of networks that RIP can support. 
### RIP implements the split horizon, route poisoning, and holddown mechanisms to prevent incorrect routing information from being propagated. 
### In RIPv1 routers broadcast updates with their routing table every 30 seconds. In the early deployments, routing tables were small enough that the traffic was not significant. As networks grew in size, however, it became evident there could be a massive traffic burst every 30 seconds, even if the routers had been initialized at random times. 
### In most networking environments, RIP is not the preferred choice of routing protocol, as its time to converge and scalability are poor compared to EIGRP, OSPF, or IS-IS. However, it is easy to configure, because RIP does not require any parameters, unlike other protocols. 
### RIP uses the User Datagram Protocol (UDP) as its transport protocol, and is assigned the reserved port number 520.
## Development of distance-vector routing  
### Based on the Bellman\u2013Ford algorithm and the Ford\u2013Fulkerson algorithm, Distance-vector routing protocols started to be implemented from 1969 onwards in data networks such as the ARPANET and CYCLADES. The predecessor of RIP was the Gateway Information Protocol (GWINFO) which was developed by Xerox in the mid-1970s to route its experimental network. As part of the Xerox Network Systems (XNS) protocol suite GWINFO transformed into the XNS Routing Information Protocol. This XNS RIP in turn became the basis for early routing protocols, such as Novell's IPX RIP, AppleTalk's Routing Table Maintenance Protocol (RTMP), and the IP RIP. The 1982 Berkley Software Distribution of the UNIX operating system implemented RIP in the routed daemon. The 4.2BSD release proved popular and became the basis for subsequent UNIX versions, which implemented RIP in the routed or gated daemon. Ultimately RIP had been extensively deployed before the standard written by Charles Hedrick was passed as RIPv1 in 1988.
## The RIP hop count  
### The routing metric used by RIP counts the number of routers that need to be passed to reach a destination IP network. The hop count 0 denotes a network that is directly connected to the router. 16 hops denote a network that is unreachable, according to the RIP hop limit.
## Versions  
### There are three standardized versions of the Routing Information Protocol: RIPv1 and RIPv2 for IPv4, and RIPng for IPv6.
## RIP version 1  
### The original specification of RIP, defined in RFC 1058, was published in 1988. When starting up, and every 30 seconds thereafter, a router with RIPv1 implementation broadcasts to 255.255.255.255 a request message through every RIPv1 enabled interface. Neighbouring routers receiving the request message respond with a RIPv1 segment, containing their routing table. The requesting router updates its own routing table, with the reachable IP network address, hop count and next hop, that is the router interface IP address from which the RIPv1 response was sent. As the requesting router receives updates from different neighbouring routers it will only update the reachable networks in its routing table, if it receives information about a reachable network it has not yet in its routing table or information that a network it has in its routing table is reachable with a lower hop count. Therefore, a RIPv1 router will in most cases only have one entry for a reachable network, the one with the lowest hop count. If a router receives information from two different neighbouring router that the same network is reachable with the same hop count but via two different routes, the network will be entered into the routing table two times with different next hop routers. The RIPv1 enabled router will then perform what is known as equal-cost load balancing for IP packets.RIPv1 enabled routers not only request the routing tables of other routers every 30 seconds, they also listen to incoming requests from neighbouring routers and send their own routing table in turn. RIPv1 routing tables are therefore updated every 25 to 35 seconds. The RIPv1 protocol adds a small random time variable to the update time, to avoid routing tables synchronizing across a LAN. It was thought, as a result of random initialization, the routing updates would spread out in time, but this was not true in practice. Sally Floyd and Van Jacobson showed in 1994 that, without slight randomization of the update timer, the timers synchronized over time.RIPv1 can be configured into silent mode, so that a router requests and processes neighbouring routing tables, and keeps its routing table and hop count for reachable networks up to date, but does not needlessly send its own routing table into the network. Silent mode is commonly implemented to hosts.RIPv1 uses classful routing. The periodic routing updates do not carry subnet information, lacking support for variable length subnet masks (VLSM). This limitation makes it impossible to have different-sized subnets inside of the same network class. In other words, all subnets in a network class must have the same size. There is also no support for router authentication, making RIP vulnerable to various attacks.
## RIP version 2  
### Due to the deficiencies of the original RIP specification, RIP version 2 (RIPv2) was developed in 1993, published as RFC 1723 in 1994, and declared Internet Standard 56 in 1998. It included the ability to carry subnet information, thus supporting Classless Inter-Domain Routing (CIDR). To maintain backward compatibility, the hop count limit of 15 remained. RIPv2 has facilities to fully interoperate with the earlier specification if all Must Be Zero protocol fields in the RIPv1 messages are properly specified. In addition, a compatibility switch feature allows fine-grained interoperability adjustments. 
### In an effort to avoid unnecessary load on hosts that do not participate in routing, RIPv2 multicasts the entire routing table to all adjacent routers at the address 224.0.0.9, as opposed to RIPv1 which uses broadcast. Unicast addressing is still allowed for special applications. 
### (MD5) authentication for RIP was introduced in 1997.Route tags were also added in RIP version 2. This functionality allows a distinction between routes learned from the RIP protocol and routes learned from other protocols.
## RIPng  
### RIPng (RIP next generation), defined in RFC 2080, is an extension of RIPv2 for support of IPv6, the next generation Internet Protocol. The main differences between RIPv2 and RIPng are: 

### Support of IPv6 networking. 
### While RIPv2 supports RIPv1 updates authentication, RIPng does not. IPv6 routers were, at the time, supposed to use IPsec for authentication. 
### RIPv2 encodes the next-hop into each route entry, RIPng requires specific encoding of the next hop for a set of route entries.RIPng sends updates on UDP port 521 using the multicast group ff02::9.
## RIP messages between routers  
### RIP messages use the User Datagram Protocol on port 520 and all RIP messages exchanged between routers are encapsulated in a UDP segment.
## RIPv1 Messages  
### RIP defined two types of messages: 
### Request Message 
### Asking a neighbouring RIPv1 enabled router to send its routing table. 
### Response Message 
### Carries the routing table of a router.
## Timers  
### The routing information protocol uses the following timers as part of its operation: 
### Update Timer 
### Controls the interval between two gratuitous Response Messages. By default the value is 30 seconds. The response message is broadcast to all its RIP enabled interface. 
### Invalid Timer 
### The invalid timer specifies how long a routing entry can be in the routing table without being updated. This is also called as expiration Timer. By default, the value is 180 seconds. After the timer expires the hop count of the routing entry will be set to 16, marking the destination as unreachable. 
### Flush Timer 
### The flush timer controls the time between the route is invalidated or marked as unreachable and removal of entry from the routing table. By default the value is 240 seconds. This is 60 seconds longer than Invalid timer.  So for 60 seconds the router will be advertising about this unreachable route to all its neighbours. This timer must be set to a higher value than the invalid timer. 
### Holddown Timer 
### The hold-down timer is started per route entry, when the hop count is changing from lower value to higher value. This allows the route to get stabilized. During this time no update can be done to that routing entry.  This is not part of the RFC 1058. This is Cisco's implementation.  The default value of this timer is 180 seconds.
## Limitations  
### The hop count cannot exceed 15, or routes will be dropped. 
### Variable Length Subnet Masks are not supported by RIP version 1 (which is obsolete). 
### RIP has slow convergence and count to infinity problems.
## Implementations  
### Cisco IOS, software used in Cisco routers (supports version 1, version 2 and RIPng) 
### Cisco NX-OS software used in Cisco Nexus data center switches (supports RIPv2 only) 
### Junos software used in Juniper routers, switches, and firewalls (supports RIPv1 and RIPv2) 
### Routing and Remote Access, a Windows Server feature, contains RIP support 
### Quagga, a free open source software routing suite based on GNU Zebra 
### BIRD, a free open source software routing suite 
### Zeroshell, a free open source software routing suite 
### A RIP implementation first introduced in 4.2BSD, routed, survives in several of its descendants, including FreeBSD and NetBSD. 
### OpenBSD introduced a new implementation, ripd, in version 4.1 and retired routed in version 4.4. 
### Netgear routers commonly offer a choice of two implementations of RIPv2; these are labelled RIP_2M and RIP_2B. RIP_2M is the standard RIPv2 implementation using multicasting - which requires all routers on the network to support RIPv2 and multicasting, whereas RIP_2B sends RIPv2 packets using subnet broadcasting - making it more compatible with routers that do not support multicasting, including RIPv1 routers. 
### Huawei HG633 ADSL/VDSL routers support passive and active routing with RIP v1 & v2 on the LAN and WAN side.
## Similar protocols  
### Cisco's proprietary Interior Gateway Routing Protocol (IGRP) was a somewhat more capable protocol than RIP. It belongs to the same basic family of distance-vector routing protocols.  
### Cisco has ceased support and distribution of IGRP in their router software. It was replaced by the Enhanced Interior Gateway Routing Protocol (EIGRP) which is a completely new design. While EIGRP still uses a distance-vector model, it relates to IGRP only in using the same routing metrics. IGRP supports multiple metrics for each route, including bandwidth, delay, load, MTU, and reliability.
## See also  
### Convergence (routing)
## References 
## Further reading  
### Malkin, Gary Scott (2000). RIP: An Intra-Domain Routing Protocol. Addison-Wesley Longman. ISBN 0-201-43320-6. 
### Edward A. Taft, Gateway Information Protocol (revised) (Xerox Parc, Palo Alto, May, 1979) 
### Xerox System Integration Standard - Internet Transport Protocols (Xerox, Stamford, 1981)"
## Links
### ARPANET
### Address Resolution Protocol
### AppleTalk
### Application layer
### Bandwidth (computing)
### Bellman–Ford algorithm
### Berkeley Software Distribution
### Berkley Software Distribution
### Bird Internet routing daemon
### Border Gateway Protocol
### Broadcasting (networking)
### CYCLADES
### Cisco
### Cisco IOS
### Cisco Systems
### Classful address
### Classless Inter-Domain Routing
### Convergence (routing)
### Count to infinity
### DHCPv6
### Daemon (computing)
### Data networks
### Datagram Congestion Control Protocol
### Distance-vector routing protocol
### Doi (identifier)
### Domain Name System
### Dynamic Host Configuration Protocol
### Enhanced Interior Gateway Routing Protocol
### Explicit Congestion Notification
### File Transfer Protocol
### Ford–Fulkerson algorithm
### FreeBSD
### Free software
### GNU Zebra
### HTTPS
### Holddown
### Hop (networking)
### Hopcount
### Huawei
### Hypertext Transfer Protocol
### IETF
### IPsec
### IPv4
### IPv6
### IS-IS
### ISBN (identifier)
### Interior Gateway Routing Protocol
### Internet Control Message Protocol
### Internet Control Message Protocol for IPv6
### Internet Group Management Protocol
### Internet Message Access Protocol
### Internet Protocol
### Internet Standard
### Internet layer
### Internet protocol suite
### Junos
### Lightweight Directory Access Protocol
### Link layer
### Load (computing)
### MD5
### MQTT
### Maximum transmission unit
### Media Gateway Control Protocol
### Medium access control
### Metrics (networking)
### Multicast
### Multicast address
### Neighbor Discovery Protocol
### NetBSD
### Netgear
### Network News Transfer Protocol
### Network Time Protocol
### Network class
### Network delay
### Novell
### OpenBSD
### Open Network Computing Remote Procedure Call
### Open Shortest Path First
### Open source software
### Point-to-Point Protocol
### Port number
### Post Office Protocol
### Precision Time Protocol
### QUIC
### Quagga (software)
### RFC (identifier)
### Real-time Transport Protocol
### Real Time Streaming Protocol
### Reliability (computer networking)
### Resource Reservation Protocol
### Route poisoning
### Routing loop problem
### Routing protocol
### Routing table
### Scale (computing)
### Secure Shell
### Session Initiation Protocol
### Simple Mail Transfer Protocol
### Simple Network Management Protocol
### Split horizon
### Stream Control Transmission Protocol
### Subnetwork
### Telnet
### Transmission Control Protocol
### Transport Layer Security
### Transport layer
### Tunneling protocol
### UNIX
### Unicast
### User Datagram Protocol
### VLSM
### Windows Server 2003
### XMPP
### Xerox
### Xerox Network Systems
### Zeroshell
## References
### [Reference](http://netbsd.gw.com/cgi-bin/man-cgi?routed+8+NetBSD-current) - http://netbsd.gw.com/cgi-bin/man-cgi?routed+8+NetBSD-current
### [Reference](http://kb.netgear.com/app/answers/detail/a_id/24088) - http://kb.netgear.com/app/answers/detail/a_id/24088
### [Reference](http://www.routeralley.com/guides/rip.pdf) - http://www.routeralley.com/guides/rip.pdf
### [Reference](http://doi.org/10.17487%2FRFC2080) - http://doi.org/10.17487%2FRFC2080
### [Reference](http://doi.org/10.17487%2FRFC2453) - http://doi.org/10.17487%2FRFC2453
### [Reference](http://www.freebsd.org/cgi/man.cgi?query=routed&sektion=8) - http://www.freebsd.org/cgi/man.cgi?query=routed&sektion=8
### [Reference](http://www.icir.org/floyd/papers/sync_94.pdf) - http://www.icir.org/floyd/papers/sync_94.pdf
### [Reference](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/6-x/unicast/configuration/guide/l3_cli_nxos/l3_rip.html) - https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/6-x/unicast/configuration/guide/l3_cli_nxos/l3_rip.html
### [Reference](https://www.iana.org/) - https://www.iana.org/
### [Reference](https://www.iana.org/assignments/port-numbers) - https://www.iana.org/assignments/port-numbers
### [Reference](https://datatracker.ietf.org/doc/html/rfc2080) - https://datatracker.ietf.org/doc/html/rfc2080
### [Reference](https://datatracker.ietf.org/doc/html/rfc2453) - https://datatracker.ietf.org/doc/html/rfc2453
### [Reference](https://tools.ietf.org/html/rfc1058) - https://tools.ietf.org/html/rfc1058
### [Reference](https://man.openbsd.org/ripd.8) - https://man.openbsd.org/ripd.8
## Images