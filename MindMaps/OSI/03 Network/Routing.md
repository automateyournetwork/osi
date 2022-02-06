# Routing
## [URL](https://en.wikipedia.org/wiki/Routing) - https://en.wikipedia.org/wiki/Routing
## Catagories
### All Wikipedia articles written in American English
### Articles with LCCN identifiers
### Articles with short description
### CS1 maint: multiple names: authors list
### Commons category link from Wikidata
### Internet architecture
### Routing
### Short description matches Wikidata
### Use American English from December 2019
### "Routing is the process of selecting a path for traffic in a network or between or across multiple networks. Broadly, routing is performed in many types of networks, including circuit-switched networks, such as the public switched telephone network (PSTN), and computer networks, such as the Internet. 
### In packet switching networks, routing is the higher-level decision making that directs network packets from their source toward their destination through intermediate network nodes by specific packet forwarding mechanisms. Packet forwarding is the transit of network packets from one network interface to another.  Intermediate nodes are typically network hardware devices such as routers, gateways, firewalls, or switches. General-purpose computers also forward packets and perform routing, although they have no specially optimized hardware for the task. 
### The routing process usually directs forwarding on the basis of routing tables. Routing tables maintain a record of the routes to various network destinations. Routing tables may be specified by an administrator, learned by observing network traffic or built with the assistance of routing protocols. 
### Routing, in a narrower sense of the term, often refers to IP routing and is contrasted with bridging. IP routing assumes that network addresses are structured and that similar addresses imply proximity within the network. Structured addresses allow a single routing table entry to represent the route to a group of devices.  In large networks, structured addressing (routing, in the narrow sense) outperforms unstructured addressing (bridging). Routing has become the dominant form of addressing on the Internet. Bridging is still widely used within local area networks.
## Delivery schemes  
### Routing schemes differ in how they deliver messages: 

### Unicast delivers a message to a single specific node using a one-to-one association between a sender and destination: each destination address uniquely identifies a single receiver endpoint. 
### Broadcast delivers a message to all nodes in the network using a one-to-all association; a single datagram (or packet) from one sender is routed to all of the possibly multiple endpoints associated with the broadcast address. The network automatically replicates datagrams as needed to reach all the recipients within the scope of the broadcast, which is generally an entire network subnet. 
### Multicast delivers a message to a group of nodes that have expressed interest in receiving the message using a one-to-many-of-many or many-to-many-of-many association; datagrams are routed simultaneously in a single transmission to many recipients. Multicast differs from broadcast in that the destination address designates a subset, not necessarily all, of the accessible nodes. 
### Anycast delivers a message to any one out of a group of nodes, typically the one nearest to the source using a one-to-one-of-many association where datagrams are routed to any single member of a group of potential receivers that are all identified by the same destination address.  The routing algorithm selects the single receiver from the group based on which is the nearest according to some distance or cost measure.Unicast is the dominant form of message delivery on the Internet.  This article focuses on unicast routing algorithms.
## Topology distribution  
### With static routing, small networks may use manually configured routing tables. Larger networks have complex topologies that can change rapidly, making the manual construction of routing tables unfeasible. Nevertheless, most of the public switched telephone network (PSTN) uses pre-computed routing tables, with fallback routes if the most direct route becomes blocked (see routing in the PSTN). 
### Dynamic routing attempts to solve this problem by constructing routing tables automatically, based on information carried by routing protocols, allowing the network to act nearly autonomously in avoiding network failures and blockages. Dynamic routing dominates the Internet. Examples of dynamic-routing protocols and algorithms include Routing Information Protocol (RIP), Open Shortest Path First (OSPF) and Enhanced Interior Gateway Routing Protocol (EIGRP).
## Distance vector algorithms  

### Distance vector algorithms use the Bellman\u2013Ford algorithm. This approach assigns a cost number to each of the links between each node in the network. Nodes send information from point A to point B via the path that results in the lowest total cost (i.e. the sum of the costs of the links between the nodes used). 
### When a node first starts, it only knows of its immediate neighbors and the direct cost involved in reaching them. (This information \u2014 the list of destinations, the total cost to each, and the next hop to send data to get there \u2014 makes up the routing table, or distance table.) Each node, on a regular basis, sends to each neighbor node its own current assessment of the total cost to get to all the destinations it knows of. The neighboring nodes examine this information and compare it to what they already know; anything that represents an improvement on what they already have, they insert in their own table. Over time, all the nodes in the network discover the best next hop and total cost for all destinations. 
### When a network node goes down, any nodes that used it as their next hop discard the entry and convey the updated routing information to all adjacent nodes, which in turn repeat the process. Eventually, all the nodes in the network receive the updates and discover new paths to all the destinations that don't involve the down node.
## Link-state algorithms  

### When applying link-state algorithms, a graphical map of the network is the fundamental data used for each node. To produce its map, each node floods the entire network with information about the other nodes it can connect to.  Each node then independently assembles this information into a map. Using this map, each router independently determines the least-cost path from itself to every other node using a standard shortest paths algorithm such as Dijkstra's algorithm. The result is a tree graph rooted at the current node, such that the path through the tree from the root to any other node is the least-cost path to that node. This tree then serves to construct the routing table, which specifies the best next hop to get from the current node to any other node.
## Optimized Link State Routing algorithm  

### A link-state routing algorithm optimized for mobile ad hoc networks is the optimized Link State Routing Protocol (OLSR). OLSR is proactive; it uses Hello and Topology Control (TC) messages to discover and disseminate link-state information through the mobile ad hoc network. Using Hello messages, each node discovers 2-hop neighbor information and elects a set of multipoint relays (MPRs). MPRs distinguish OLSR from other link-state routing protocols.
## Path-vector protocol  

### Distance vector and link-state routing are both intra-domain routing protocols. They are used inside an autonomous system, but not between autonomous systems. Both of these routing protocols become intractable in large networks and cannot be used in inter-domain routing. Distance vector routing is subject to instability if there are more than a few hops in the domain. Link state routing needs significant resources to calculate routing tables. It also creates heavy traffic due to flooding. 
### Path-vector routing is used for inter-domain routing. It is similar to distance vector routing. Path-vector routing assumes that one node (there can be many) in each autonomous system acts on behalf of the entire autonomous system. This node is called the speaker node. The speaker node creates a routing table and advertises it to neighboring speaker nodes in neighboring autonomous systems. The idea is the same as distance vector routing except that only speaker nodes in each autonomous system can communicate with each other. The speaker node advertises the path, not the metric, of the nodes in its autonomous system or other autonomous systems. 
### The path-vector routing algorithm is similar to the distance vector algorithm in the sense that each border router advertises the destinations it can reach to its neighboring router. However, instead of advertising networks in terms of a destination and the distance to that destination, networks are advertised as destination addresses and path descriptions to reach those destinations. The path, expressed in terms of the domains (or confederations) traversed so far, is carried in a special path attribute that records the sequence of routing domains through which the reachability information has passed. A route is defined as a pairing between a destination and the attributes of the path to that destination, thus the name, path-vector routing; The routers receive a vector that contains paths to a set of destinations.
## Path selection  
### Path selection involves applying a routing metric to multiple routes to select (or predict) the best route. Most routing algorithms use only one network path at a time. Multipath routing and specifically equal-cost multi-path routing techniques enable the use of multiple alternative paths. 
### In computer networking, the metric is computed by a routing algorithm, and can cover information such as bandwidth, network delay, hop count, path cost, load, maximum transmission unit, reliability, and communication cost. The routing table stores only the best possible routes, while link-state or topological databases may store all other information as well. 
### In case of overlapping or equal routes, algorithms consider the following elements in priority order to decide which routes to install into the routing table: 

### Prefix length: A matching route table entry with a longer subnet mask is always preferred as it specifies the destination more exactly. 
### Metric: When comparing routes learned via the same routing protocol, a lower metric is preferred. Metrics cannot be compared between routes learned from different routing protocols. 
### Administrative distance: When comparing route table entries from different sources such as different routing protocols and static configuration, a lower administrative distance indicates a more reliable source and thus a preferred route.Because a routing metric is specific to a given routing protocol, multi-protocol routers must use some external heuristic to select between routes learned from different routing protocols. Cisco routers, for example, attribute a value known as the administrative distance to each route, where smaller administrative distances indicate routes learned from a protocol assumed to be more reliable. 
### A local administrator can set up host-specific routes that provide more control over network usage, permits testing, and better overall security. This is useful for debugging network connections or routing tables. 
### In some small systems, a single central device decides ahead of time the complete path of every packet. In some other small systems, whichever edge device injects a packet into the network decides ahead of time the complete path of that particular packet. In either case, the route-planning device needs to know a lot of information about what devices are connected to the network and how they are connected to each other. Once it has this information, it can use an algorithm such as A* search algorithm to find the best path. 
### In high-speed systems, there are so many packets transmitted every second that it is infeasible for a single device to calculate the complete path for each and every packet. Early high-speed systems dealt with this with circuit switching by setting up a path once for the first packet between some source and some destination; later packets between that same source and that same destination continue to follow the same path without recalculating until the circuit teardown. Later high-speed systems inject packets into the network without any one device ever calculating a complete path for packets. 
### In large systems, there are so many connections between devices, and those connections change so frequently, that it is infeasible for any one device to even know how all the devices are connected to each other, much less calculate a complete path through them. Such systems generally use next-hop routing. 
### Most systems use a deterministic dynamic routing algorithm. When a device chooses a path to a particular final destination, that device always chooses the same path to that destination until it receives information that makes it think some other path is better. 
### A few routing algorithms do not use a deterministic algorithm to find the best link for a packet to get from its original source to its final destination. Instead, to avoid congestion hot spots in packet systems, a few algorithms use a randomized algorithm\u2014Valiant's paradigm\u2014that routes a path to a randomly picked intermediate destination, and from there to its true final destination. In many early telephone switches, a randomizer was often used to select the start of a path through a multistage switching fabric. 
### Depending on the application for which path selection is performed, different metrics can be used. For example, for web requests one can use minimum latency paths to minimize web page load time, or for bulk data transfers one can choose the least utilized path to balance load across the network and increase throughput. A popular path selection objective is to reduce the average completion times of traffic flows and the total network bandwidth consumption. Recently, a path selection metric was proposed that computes the total number of bytes scheduled on the edges per path as selection metric. An empirical analysis of several path selection metrics, including this new proposal, has been made available.
## Multiple agents  
### In some networks, routing is complicated by the fact that no single entity is responsible for selecting paths; instead, multiple entities are involved in selecting paths or even parts of a single path. Complications or inefficiency can result if these entities choose paths to optimize their own objectives, which may conflict with the objectives of other participants. 
### A classic example involves traffic in a road system, in which each driver picks a path that minimizes their travel time. With such routing, the equilibrium routes can be longer than optimal for all drivers. In particular, Braess's paradox shows that adding a new road can lengthen travel times for all drivers. 
### In a single-agent model used, for example, for routing automated guided vehicles (AGVs) on a terminal, reservations are made for each vehicle to prevent simultaneous use of the same part of an infrastructure. This approach is also referred to as context-aware routing.The Internet is partitioned into autonomous systems (ASs) such as internet service providers (ISPs), each of which controls routes involving its network. Routing occurs at multiple levels. First, AS-level paths are selected via the BGP protocol that produces a sequence of ASs through which packets flow. Each AS may have multiple paths, offered by neighboring ASs, from which to choose. These routing decisions often correlate with business relationships with these neighboring ASs, which may be unrelated to path quality or latency. Second, once an AS-level path has been selected, there are often multiple corresponding router-level paths to choose from. This is due, in part, because two ISPs may be connected through multiple connections. In choosing the single router-level path, it is common practice for each ISP to employ hot-potato routing: sending traffic along the path that minimizes the distance through the ISP's own network\u2014even if that path lengthens the total distance to the destination. 
### For example, consider two ISPs, A and B. Each has a presence in New York, connected by a fast link with latency 5 ms\u2014and each has a presence in London connected by a 5 ms link. Suppose both ISPs have trans-Atlantic links that connect their two networks, but A's link has latency 100 ms and B's has latency 120 ms. When routing a message from a source in A's London network to a destination in B's New York network, A may choose to immediately send the message to B in London. This saves A the work of sending it along an expensive trans-Atlantic link, but causes the message to experience latency 125 ms when the other route would have been 20 ms faster. 
### A 2003 measurement study of Internet routes found that, between pairs of neighboring ISPs, more than 30% of paths have inflated latency due to hot-potato routing, with 5% of paths being delayed by at least 12 ms. Inflation due to AS-level path selection, while substantial, was attributed primarily to BGP's lack of a mechanism to directly optimize for latency, rather than to selfish routing policies. It was also suggested that, were an appropriate mechanism in place, ISPs would be willing to cooperate to reduce latency rather than use hot-potato routing. Such a mechanism was later published by the same authors, first for the case of two ISPs and then for the global case.
## Route analytics  
### As the Internet and IP networks have become mission critical business tools, there has been increased interest in techniques and methods to monitor the routing posture of networks. Incorrect routing or routing issues cause undesirable performance degradation, flapping or downtime. Monitoring routing in a network is achieved using route analytics tools and techniques.
## Centralized routing  
### In networks where a logically centralized control is available over the forwarding state, for example, using software-defined networking, routing techniques can be used that aim to optimize global and network-wide performance metrics. This has been used by large internet companies that operate many data centers in different geographical locations attached using private optical links, examples of which include Microsoft's Global WAN, Facebook's Express Backbone, and Google's B4.Global performance metrics to optimize include maximizing network utilization, minimizing traffic flow completion times, maximizing the traffic delivered prior to specific deadlines and reducing the completion times of flows. Work on the later over private WAN discusses modeling routing as a graph optimization problem by pushing all the queuing to the end-points. The authors also propose a heuristic to solve the problem efficiently while sacrificing negligible performance.
## See also 
## References 
## Further reading 
## External links  
### Count-To-Infinity Problem 
### \"Stability Features\". Archived from the original on 2015-09-25., ways of avoiding the count-to-infinity problem 
### Cisco IT Case Studies about Routing and Switching 
### \"IP Routing and Subnets\". www.eventhelix.com. Retrieved 2018-04-28."
## Links
### 1ESS switch
### A* search algorithm
### Administrative distance
### Anycast
### ArXiv (identifier)
### Automated guided vehicle
### Autonomous system (Internet)
### B.A.T.M.A.N.
### Babel (protocol)
### Bandwidth (computing)
### Bellman–Ford algorithm
### Bibcode (identifier)
### Border Gateway Multicast Protocol
### Border Gateway Protocol
### Braess's paradox
### Bridging (networking)
### Broadcast address
### Broadcasting (networking)
### Circuit switching
### Cisco
### CiteSeerX (identifier)
### Collection Tree Protocol
### Collective routing
### Computer
### Computer network
### Constrained Shortest Path First
### Datagram
### Deflection routing
### Dijkstra's algorithm
### Distance-vector routing protocol
### Distance Vector Multicast Routing Protocol
### Distributed Split Multi-Link Trunking
### Doi (identifier)
### Dynamic routing
### Edge disjoint shortest pair algorithm
### Enhanced Interior Gateway Routing Protocol
### Equal-cost multi-path routing
### Exterior Gateway Protocol
### Firewall (computing)
### Flood search routing
### Fuzzy routing
### Gateway (telecommunications)
### Geographic routing
### Graph (discrete mathematics)
### Heuristic
### Heuristic routing
### Hop (networking)
### Hop count
### Hot-potato routing
### IP routing
### IS-IS
### ISBN (identifier)
### Inter-domain
### Interior Gateway Routing Protocol
### Internet
### Internet service provider
### Jennifer Rexford
### Link-state routing protocol
### Local area network
### London
### Maximum transmission unit
### Metrics (networking)
### Millisecond
### Mission critical
### Mobile ad hoc network
### Multicast
### Multipath routing
### NSDI
### Nash equilibrium
### Network address
### Network delay
### Network hardware
### Network interface controller
### Network packet
### Network switch
### Network theory
### Network topology
### New York City
### Node (networking)
### Open Shortest Path First
### Optimized Link State Routing Protocol
### Packet (information technology)
### Packet forwarding
### Packet switching
### Path-vector routing protocol
### Path computation element
### Policy-based routing
### Public switched telephone network
### R-SMLT
### RFC (identifier)
### Route analytics
### Route flapping
### Router (computing)
### Routing
### Routing (disambiguation)
### Routing Information Protocol
### Routing in the PSTN
### Routing protocol
### Routing table
### S2CID (identifier)
### SIGCOMM
### Shortest path problem
### Small-world routing
### Software-defined networking
### Split multi-link trunking
### Static routing
### Subnetwork
### Teardown (communications)
### Tree (graph theory)
### Turn restriction routing
### Unicast
### Wormhole routing
## References
### [Reference](http://www.ciscopress.com/title/1578700892) - http://www.ciscopress.com/title/1578700892
### [Reference](http://www.ciscopress.com/title/1587052024) - http://www.ciscopress.com/title/1587052024
### [Reference](http://www.eventhelix.com/Realtimemantra/Networking/ip_routing.htm) - http://www.eventhelix.com/Realtimemantra/Networking/ip_routing.htm
### [Reference](http://research.microsoft.com/en-us/um/people/ratul/papers/nsdi2005-nexit.pdf) - http://research.microsoft.com/en-us/um/people/ratul/papers/nsdi2005-nexit.pdf
### [Reference](http://research.microsoft.com/en-us/um/people/ratul/papers/nsdi2007-wiser.pdf) - http://research.microsoft.com/en-us/um/people/ratul/papers/nsdi2007-wiser.pdf
### [Reference](http://wwwlehre.dhbw-stuttgart.de/~schulte/htme/55024.htm#HDR3) - http://wwwlehre.dhbw-stuttgart.de/~schulte/htme/55024.htm#HDR3
### [Reference](http://www.eecs.harvard.edu/~michaelm/postscripts/handbook2001.pdf) - http://www.eecs.harvard.edu/~michaelm/postscripts/handbook2001.pdf
### [Reference](http://www.cs.princeton.edu/~jrex/papers/policies.pdf) - http://www.cs.princeton.edu/~jrex/papers/policies.pdf
### [Reference](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.392.151) - http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.392.151
### [Reference](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.392.151) - http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.392.151
### [Reference](http://www.cs.washington.edu/research/networking/rocketfuel/papers/sigcomm2003.pdf) - http://www.cs.washington.edu/research/networking/rocketfuel/papers/sigcomm2003.pdf
### [Reference](http://rainer.baumann.info/public/tik262.pdf) - http://rainer.baumann.info/public/tik262.pdf
### [Reference](http://inspirehep.net/record/887357/files/cer-002474543.pdf) - http://inspirehep.net/record/887357/files/cer-002474543.pdf
### [Reference](http://www.st.ewi.tudelft.nl/~mathijs/publications/intinfra09.pdf) - http://www.st.ewi.tudelft.nl/~mathijs/publications/intinfra09.pdf
### [Reference](http://arxiv.org/abs/1712.03530) - http://arxiv.org/abs/1712.03530
### [Reference](http://arxiv.org/abs/1810.00169) - http://arxiv.org/abs/1810.00169
### [Reference](http://doi.org/10.1109%2FCOMST.2017.2782753) - http://doi.org/10.1109%2FCOMST.2017.2782753
### [Reference](http://doi.org/10.1109%2FLCOMM.2018.2872980) - http://doi.org/10.1109%2FLCOMM.2018.2872980
### [Reference](https://code.fb.com/data-center-engineering/building-express-backbone-facebook-s-new-long-haul-network/) - https://code.fb.com/data-center-engineering/building-express-backbone-facebook-s-new-long-haul-network/
### [Reference](https://azure.microsoft.com/en-us/blog/how-microsoft-builds-its-fast-and-reliable-global-network/) - https://azure.microsoft.com/en-us/blog/how-microsoft-builds-its-fast-and-reliable-global-network/
### [Reference](https://www.networkcomputing.com/networking/inside-googles-software-defined-network/512240144) - https://www.networkcomputing.com/networking/inside-googles-software-defined-network/512240144
### [Reference](https://ui.adsabs.harvard.edu/abs/2018arXiv181000169N) - https://ui.adsabs.harvard.edu/abs/2018arXiv181000169N
### [Reference](https://id.loc.gov/authorities/subjects/sh2006000147) - https://id.loc.gov/authorities/subjects/sh2006000147
### [Reference](https://www.researchgate.net/publication/323411017) - https://www.researchgate.net/publication/323411017
### [Reference](https://www.researchgate.net/publication/323723167) - https://www.researchgate.net/publication/323723167
### [Reference](https://www.researchgate.net/publication/328008697) - https://www.researchgate.net/publication/328008697
### [Reference](https://archive.org/details/routingtcpip00jeff) - https://archive.org/details/routingtcpip00jeff
### [Reference](https://web.archive.org/web/20061209093728/http://wiki.uni.lu/secan-lab/Count-To-Infinity+Problem.html) - https://web.archive.org/web/20061209093728/http://wiki.uni.lu/secan-lab/Count-To-Infinity+Problem.html
### [Reference](https://web.archive.org/web/20070216114435/http://www.cisco.com/web/about/ciscoitatwork/case_studies/routing.html) - https://web.archive.org/web/20070216114435/http://www.cisco.com/web/about/ciscoitatwork/case_studies/routing.html
### [Reference](https://web.archive.org/web/20150925085557/http://wwwlehre.dhbw-stuttgart.de/~schulte/htme/55024.htm#HDR3) - https://web.archive.org/web/20150925085557/http://wwwlehre.dhbw-stuttgart.de/~schulte/htme/55024.htm#HDR3
### [Reference](https://datatracker.ietf.org/doc/html/rfc1322) - https://datatracker.ietf.org/doc/html/rfc1322
### [Reference](https://api.semanticscholar.org/CorpusID:28143006) - https://api.semanticscholar.org/CorpusID:28143006
### [Reference](https://api.semanticscholar.org/CorpusID:52898719) - https://api.semanticscholar.org/CorpusID:52898719
### [Reference](https://www.wikidata.org/wiki/Q22725#identifiers) - https://www.wikidata.org/wiki/Q22725#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/dc/Broadcast.svg) - https://upload.wikimedia.org/wikipedia/commons/d/dc/Broadcast.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/30/Multicast.svg) - https://upload.wikimedia.org/wikipedia/commons/3/30/Multicast.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/7/75/Unicast.svg) - https://upload.wikimedia.org/wikipedia/commons/7/75/Unicast.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg) - https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/1/18/Anycast-BM.svg) - https://upload.wikimedia.org/wikipedia/en/1/18/Anycast-BM.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg) - https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg