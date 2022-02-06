# IP routing
## [URL](https://en.wikipedia.org/wiki/IP_routing) - https://en.wikipedia.org/wiki/IP_routing
## Catagories
### All Wikipedia articles in need of updating
### All articles needing additional references
### All articles with unsourced statements
### Articles needing additional references from June 2020
### Articles with multiple maintenance issues
### Articles with obsolete information from June 2020
### Articles with short description
### Articles with unsourced statements from November 2016
### Routing
### Short description matches Wikidata
### "IP routing is the application routing methodologies to IP networks. This involves not only protocols and technologies but includes the policies of the worldwide organization and configuration of Internet infrastructure. In each IP network node, IP routing involves the determination of a suitable path for a network packet from a source to its destination in an IP network. The process uses static configuration rules or dynamically obtained from routing protocols to select specific packet forwarding methods to direct traffic to the next available intermediate network node one hop closer to the desired final destination, a total path potentially spanning multiple computer networks. 
### Networks are separated from each other by specialized hosts, called gateways or routers with specialized software support optimized for routing. In routers, packets arriving at an interface are examined for source and destination addressing and queued to the appropriate outgoing interface according to their destination address and a set of rules and performance metrics. Rules are encoded in a routing table that contains entries for all interfaces and their connected networks. If no rule satisfies the requirements for a network packet, it is forwarded to a default route. Routing tables are maintained either manually by a network administrator, or updated dynamically with a routing protocol. Routing rules may contain other parameters than source and destination, such as limitations on available bandwidth, expected packet loss rates, and specific technology requirements. 
### IP forwarding algorithms take into account the size of each packet, the type of service specified in the header, as well as characteristics of the available links to other routers in the network, such as link capacity, utilization rate, and maximum datagram size that is supported on the link. In general, most routing software determines a route through a shortest path algorithm. However, other routing protocols may use other metrics for determining the best path. Based on the metrics required and present for each link, each path has an associated cost. The routing algorithm attempts to minimize the cost when choosing the next hop. 
### A routing protocol is a software mechanism by which routers communicate and share information about the topology of the network, and the capabilities of each routing node. It thus implements the network-global rules by which traffic is directed within a network and across multiple networks. Different protocols are often used for different topologies or different application areas. For example, the Open Shortest Path First (OSPF) protocol is generally used for routing packets between subnetworks within an enterprise and the Border Gateway Protocol (BGP) is used on a global scale. BGP is the de facto standard of worldwide Internet routing.
## Protocol classification  
### Routing protocols may be broadly distinguished by their realm of operation in terms of network scope. Interior gateway protocols are used for routing within autonomous systems, while exterior gateway protocols route traffic between them. The former group is exemplified by the Routing Information Protocol (RIP) and Open Shortest Path First (OSPF), while the Exterior Gateway Protocol (EGP) and the Border Gateway Protocol (BGP) are examples of the exterior type. BGP is the dominant route distribution protocol used in the Internet.
## Routing algorithm  
### The IP forwarding algorithm is a specific implementation of routing for IP networks. In order to achieve a successful transfer of data, the algorithm uses a routing table to select a next-hop router as the next destination for a datagram. The IP address of the selected router is known as the next-hop address.When several destinations are matching, the route with the longest subnet mask is chosen (the most specific one). If there are multiple routes with the same subnet mask, the route with the lowest metric is used. If there are multiple default routes, the metric is also used to determine which to use. If there are multiple routes with the same subnet mask and metric, the system may use equal-cost multi-path routing as a forwarding strategy. 
### The IP forwarding algorithm states: 
### Given a destination IP address, D, and network prefix, N:if ( N matches a directly connected network address ) 
### Deliver datagram to D over that network link; 
### else if ( The routing table contains a route for N ) 
### Send datagram to the next-hop address listed in the routing table; 
### else if ( a default route exists ) 
### Send datagram to the default route; 
### else 
### Send a forwarding error message to the originator;When no route is available, an ICMP error message is sent to the originator of the packet, to inform that host that the packet could not be delivered, and to avoid unnecessary retransmission to avoid network congestion. 
### The sending host should either stop transmitting or choose another address or route.
## Routing table  
### The following presents a typical routing table in a Unix-like operating system: 

### Kernel IP routing table 
### Destination     Gateway         Genmask         Flags Metric Ref    Use Iface 
### 0.0.0.0         71.46.14.1      0.0.0.0         UG    0      0        0 ppp0 
### 10.0.0.0        0.0.0.0         255.0.0.0       U     0      0        0 eth0 
### 71.46.14.1      0.0.0.0         255.255.255.255 UH    0      0        0 ppp0 
### 169.254.0.0     0.0.0.0         255.255.0.0     U     0      0        0 eth0 
### 172.16.0.0      0.0.0.0         255.240.0.0     U     0      0        0 eth0 
### 192.168.0.0     0.0.0.0         255.255.0.0     U     0      0        0 eth0 
### 192.168.1.0     192.168.96.1    255.255.255.0   UG    0      0        0 eth0 
### 192.168.96.0    0.0.0.0         255.255.255.0   U     0      0        0 eth0 

### The host has several network interfaces. eth0 is the interface name of the network interface card representing an Ethernet port. ppp0 is a PPPoE interface, which is configured as the default route in this example. 
### A default route is recognized by the destination 0.0.0.0 and the flag G. A network router is identified by the network mask 255.255.255.255 and the flag H.
## See also  
### Multipath routing
## References "
## Links
### Autonomous system (Internet)
### Bitmask
### Border Gateway Protocol
### Computer network
### Datagram
### Default route
### Equal-cost multi-path routing
### Ethernet
### Exterior Gateway Protocol
### Exterior gateway protocol
### IP address
### IP network
### Interior gateway protocol
### Internet
### Internet Control Message Protocol
### Ip address
### Metrics (networking)
### Multipath routing
### Network congestion
### Network interface card
### Network packet
### Network router
### Open Shortest Path First
### PPPoE
### Packet forwarding
### Retransmission (data networks)
### Router (computing)
### Routing
### Routing Information Protocol
### Routing protocol
### Routing table
### Shortest path
### Subnet mask
## References
### [Reference](http://scholar.google.com/scholar?q=%22IP+routing%22) - http://scholar.google.com/scholar?q=%22IP+routing%22
### [Reference](http://www.google.com/search?&q=%22IP+routing%22&tbs=bkt:s&tbm=bks) - http://www.google.com/search?&q=%22IP+routing%22&tbs=bkt:s&tbm=bks
### [Reference](http://www.google.com/search?as_eq=wikipedia&q=%22IP+routing%22) - http://www.google.com/search?as_eq=wikipedia&q=%22IP+routing%22
### [Reference](http://www.google.com/search?tbm=nws&q=%22IP+routing%22+-wikipedia&tbs=ar:1) - http://www.google.com/search?tbm=nws&q=%22IP+routing%22+-wikipedia&tbs=ar:1
### [Reference](http://www.google.com/search?tbs=bks:1&q=%22IP+routing%22+-wikipedia) - http://www.google.com/search?tbs=bks:1&q=%22IP+routing%22+-wikipedia
### [Reference](https://www.jstor.org/action/doBasicSearch?Query=%22IP+routing%22&acc=on&wc=on) - https://www.jstor.org/action/doBasicSearch?Query=%22IP+routing%22&acc=on&wc=on
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/b/bd/Ambox_current_red_Asia_Australia.svg) - https://upload.wikimedia.org/wikipedia/commons/b/bd/Ambox_current_red_Asia_Australia.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/b/b4/Ambox_important.svg) - https://upload.wikimedia.org/wikipedia/en/b/b4/Ambox_important.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg