# Distance-vector routing protocol
## [URL](https://en.wikipedia.org/wiki/Distance-vector_routing_protocol) - https://en.wikipedia.org/wiki/Distance-vector_routing_protocol
## Catagories
### All articles lacking in-text citations
### All articles that are too technical
### Articles lacking in-text citations from September 2010
### Articles with multiple maintenance issues
### Articles with short description
### Routing algorithms
### Routing protocols
### Short description matches Wikidata
### Wikipedia articles that are too technical from November 2013
### "A distance-vector routing protocol in data networks determines the best route for data packets based on distance. Distance-vector routing protocols measure the distance by the number of routers a packet has to pass, one router counts as one hop. Some distance-vector protocols also take into account network latency and other factors that influence traffic on a given route. To determine the best route across a network, routers, on which a distance-vector protocol is implemented, exchange information with one another, usually routing tables plus hop counts for destination networks and possibly other traffic information. Distance-vector routing protocols also require that a router informs its neighbours of network topology changes periodically. 
### Distance-vector routing protocols use the Bellman\u2013Ford algorithm to calculate the best route. Another way of calculating the best route across a network is based on link cost, and is implemented through link-state routing protocols. 
### The term distance vector refers to the fact that the protocol manipulates vectors (arrays) of distances to other nodes in the network.  The distance vector algorithm was the original ARPANET routing algorithm and was implemented more widely in local area networks with the Routing Information Protocol (RIP).
## Methodology  
### Routers that use distance-vector protocol determine the distance between themselves and a destination. The best route for Internet Protocol packets that carry data across a data network is measured in terms of the numbers of routers (hops) a packet has to pass to reach its destination network. Additionally some distance-vector protocols take into account other traffic information, such as network latency. To establish the best route, routers regularly exchange information with neighbouring routers, usually their routing table, hop count for a destination network and possibly other traffic related information. Routers that implement distance-vector protocol rely purely on the information provided to them by other routers, and do not assess the network topology.Distance-vector protocols update the routing tables of routers and determine the route on which a packet will be sent by the next hop which is the exit interface of the router and the IP address of the interface of the receiving router. Distance is a measure of the cost to reach a certain node. The least cost route between any two nodes is the route with minimum distance. 
### Updates are performed periodically in a distance-vector protocol where all or part of a router's routing table is sent to all its neighbours that are configured to use the same distance-vector routing protocol. Once a router has this information it is able to amend its own routing table to reflect the changes and then inform its neighbours of the changes. This process has been described as \u2018routing by rumour\u2019 because routers are relying on the information they receive from other routers and cannot determine if the information is actually valid and true. There are a number of features which can be used to help with instability and inaccurate routing information.
## Development of distance-vector routing  
### The oldest routing protocol, and the oldest distance-vector protocol, is version 1 of the Routing Information Protocol (RIPv1). RIPv1 was formally standardised in 1988. It establishes the shortest path across a network purely on the basis of the hops, that is numbers of routers that need to be passed to reach the destination network. RIP is an interior gateway protocol, so it can be used in local area networks (LANs) on interior or border routers. Routers with RIPv1 implementation exchange their routing tables with neighbouring routers by broadcasting a RIPv1 packet every 30 second into all connected networks. RIPv1 is not suitable for large networks as it limits the number of hops to 15. This hop limit was introduced to avoid routing loops, but also means that networks that are connected through more than 15 routers are unreachable.The distance-vector protocol designed for use in wide area networks (WANs) is the Border Gateway Protocol (BGP). BGP is an exterior gateway protocol and therefore implemented on border and exterior routers on the Internet. It exchanges information between routers through a Transmission Control Protocol (TCP) session. Routers with BGP implementation determine the shortest path across a network based on a range of factors other than hops. BGP can also be configured by administrators so that certain routes are preferred or avoided. BGP is used by internet service providers (ISPs) and telecommunication companies.Among the distance-vector protocols that have been described as a hybrid, because it uses routing methods associated with link-state routing protocols, is the proprietary Enhanced Interior Gateway Routing Protocol (EIGRP). It was developed by Cisco in the 1980s and was designed to offer better convergence and cause less network traffic between routers than the link-state routing protocol Open Shortest Path First (OSPF).Another example of a distance-vector routing protocol is Babel.
## Count to infinity problem  
### The Bellman\u2013Ford algorithm does not prevent routing loops from happening and suffers from the count to infinity problem. The core of the count-to-infinity problem is that if A tells B that it has a path somewhere, there is no way for B to know if the path has B as a part of it.  To see the problem clearly, imagine a subnet connected like A\u2013B\u2013C\u2013D\u2013E\u2013F, and let the metric between the routers be \"number of jumps\". Now suppose that A is taken offline. In the vector-update-process B notices that the route to A, which was distance 1, is down \u2013 B does not receive the vector update from A. The problem is, B also gets an update from C, and C is still not aware of the fact that A is down \u2013 so it tells B that A is only two jumps from C (C to B to A). Since B doesn't know that the path from C to A is through itself (B), it updates its table with the new value \"B to A   2 + 1\". Later on, B forwards the update to C and due to the fact that A is reachable through B (From C's point of view), C decides to update its table to \"C to A  3 + 1\". This slowly propagates through the network until it becomes infinity (in which case the algorithm corrects itself, due to the relaxation property of Bellman-Ford).
## Workarounds and solutions  
### RIP uses the split horizon with poison reverse technique to reduce the chance of forming loops and uses a maximum number of hops to counter the 'count to infinity' problem. These measures avoid the formation of routing loops in some, but not all, cases.  The addition of a hold time (refusing route updates for a few minutes after a route retraction) avoids loop formation in virtually all cases, but causes a significant increase in convergence times. 
### More recently, a number of loop-free distance vector protocols have been developed \u2014 notable examples are EIGRP, DSDV and Babel.  These avoid loop formation in all cases, but suffer from increased complexity, and their deployment has been slowed down by the success of link state routing protocols such as OSPF.
## Example  
### In this network we have 4 routers A, B, C and D: 

### We mark the current time (or iteration) in the algorithm with T, and begin (at time 0, or T0) by creating distance matrices for each router to its immediate neighbours. As we build the routing tables below, the shortest path is highlighted in green, and a new shortest path is highlighted in yellow. Grey columns indicate nodes that are not neighbors of the current node, and are therefore not considered as a valid direction in its table. Red indicates invalid entries in the table since they refer to distances from a node to itself, or via itself.
## References  

### \"RFC1058 - Routing Information Protocol\", C. Hedrick, Internet Engineering Task Force,  June 1988 
### \"RFC1723 - RIP Version 2 Carrying Additional Information\", G. Malkin, Internet Engineering Task Force, November, 1994 
### \"RFC2453 -  RIP Version 2\", G. Malkin, Internet Engineering Task Force, November, 1998 
### \"A Path-Finding Algorithm for Loop-Free Routing,  J.J. Garcia-Luna-Aceves and S. Murthy,  IEEE/ACM Transactions on Networking, February 1997 
### \"Detection of Invalid Routing Announcements in the RIP Protocol\", D. Pei, D. Massey, and L. Zhang, IEEE Global Communications Conference (Globecom), December, 2003
## Further reading  
### Section \"Link-State Versus Distance Vector\" in the Chapter \"Routing Basics\" in the Cisco \"Internetworking Technology Handbook\" 
### Section 5.2 \"Routing Algorithms\" in Chapter \"5 THE NETWORK LAYER\" from \"Computer Networks\" 4th. Edition by Andrew S. Tanenbaum"
## Links
### ARPANET
### Array data structure
### Babel (protocol)
### Bellman�Ford algorithm
### Border Gateway Protocol
### Broadcasting (networking)
### Cisco
### Cisco Systems
### DSDV
### Data
### Data network
### Data networks
### EIGRP
### Enhanced Interior Gateway Routing Protocol
### Exterior gateway protocol
### ISBN (identifier)
### Interior gateway protocol
### Internet
### Internet Protocol
### Internet service providers
### Link-state routing protocol
### Link state routing protocol
### Local area networks
### Network latency
### Network packet
### Network topology
### OSPF
### Open Shortest Path First
### RFC (identifier)
### Router (computing)
### Routing Information Protocol
### Routing loop
### Routing protocol
### Routing table
### Routing tables
### Split horizon route advertisement
### Transmission Control Protocol
### Wide area network
## References
### [Reference](http://docwiki.cisco.com/wiki/Routing_Basics#Link-State_Versus_Distance_Vector) - http://docwiki.cisco.com/wiki/Routing_Basics#Link-State_Versus_Distance_Vector
### [Reference](http://authors.phptr.com/tanenbaumcn4/) - http://authors.phptr.com/tanenbaumcn4/
### [Reference](http://tools.ietf.org/html/rfc1058) - http://tools.ietf.org/html/rfc1058
### [Reference](http://www.ietf.org/rfc/rfc1058.txt) - http://www.ietf.org/rfc/rfc1058.txt
### [Reference](http://www.ietf.org/rfc/rfc1723.txt) - http://www.ietf.org/rfc/rfc1723.txt
### [Reference](http://www.ietf.org/rfc/rfc2453.txt) - http://www.ietf.org/rfc/rfc2453.txt
### [Reference](https://archive.org/details/networkguidetone00dean_142) - https://archive.org/details/networkguidetone00dean_142
### [Reference](https://archive.org/details/networkguidetone00dean_142/page/n294) - https://archive.org/details/networkguidetone00dean_142/page/n294
### [Reference](https://archive.org/details/networkguidetone00dean_142/page/n295) - https://archive.org/details/networkguidetone00dean_142/page/n295
### [Reference](https://datatracker.ietf.org/doc/html/rfc1058) - https://datatracker.ietf.org/doc/html/rfc1058
### [Reference](https://tools.ietf.org/html/rfc1058.html) - https://tools.ietf.org/html/rfc1058.html
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/4/46/Networkabcd.svg) - https://upload.wikimedia.org/wikipedia/commons/4/46/Networkabcd.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/a/a4/Text_document_with_red_question_mark.svg) - https://upload.wikimedia.org/wikipedia/commons/a/a4/Text_document_with_red_question_mark.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/b/b4/Ambox_important.svg) - https://upload.wikimedia.org/wikipedia/en/b/b4/Ambox_important.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/f/f2/Edit-clear.svg) - https://upload.wikimedia.org/wikipedia/en/f/f2/Edit-clear.svg