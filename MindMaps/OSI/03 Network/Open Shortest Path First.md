# Open Shortest Path First
## [URL](https://en.wikipedia.org/wiki/Open_Shortest_Path_First) - https://en.wikipedia.org/wiki/Open_Shortest_Path_First
## Catagories
### All Wikipedia articles written in American English
### All articles with failed verification
### All articles with unsourced statements
### Application layer protocols
### Articles with LCCN identifiers
### Articles with failed verification from January 2022
### Articles with short description
### Articles with unsourced statements from February 2012
### Articles with unsourced statements from January 2017
### Articles with unsourced statements from October 2019
### CS1 maint: url-status
### Harv and Sfn no-target errors
### Internet Standards
### Internet protocols
### Routing protocols
### Short description is different from Wikidata
### Use American English from May 2020
### Use mdy dates from September 2017
### "Open Shortest Path First (OSPF) is a routing protocol for Internet Protocol (IP) networks. It uses a link state routing (LSR) algorithm and falls into the group of interior gateway protocols (IGPs), operating within a single autonomous system (AS).  
### OSPF gathers link state information from available routers and constructs a topology map of the network. The topology is presented as a routing table to the Internet Layer for routing packets by their destination IP address. OSPF supports Internet Protocol Version 4 (IPv4) and Internet Protocol Version 6 (IPv6) networks and supports the Classless Inter-Domain Routing (CIDR) addressing model. 
### OSPF is widely used in large enterprise networks. IS-IS, another LSR-based protocol, is more common in large service provider networks. 
### Originally designed in the 1980s, OSPF is defined for IPv4 in protocol version 2 by RFC 2328 (1998). The updates for IPv6 are specified as OSPF Version 3 in RFC 5340 (2008). OSPF supports the Classless Inter-Domain Routing (CIDR) addressing model.
## Concepts  
### OSPF is an interior gateway protocol (IGP) for routing Internet Protocol (IP) packets within a single routing domain, such as an autonomous system. It gathers link state information from available routers and constructs a topology map of the network. The topology is presented as a routing table to the Internet Layer which routes packets based solely on their destination IP address. 
### OSPF detects changes in the topology, such as link failures, and converges on a new loop-free routing structure within seconds. It computes the shortest-path tree for each route using a method based on Dijkstra's algorithm. The OSPF routing policies for constructing a route table are governed by link metrics associated with each routing interface. Cost factors may be the distance of a router (round-trip time), data throughput of a link, or link availability and reliability, expressed as simple unitless numbers. This provides a dynamic process of traffic load balancing between routes of equal cost. 
### OSPF divides the network into routing areas to simplify administration and optimize traffic and resource utilization. Areas are identified by 32-bit numbers, expressed either simply in decimal, or often in the same octet-based dot-decimal notation used for IPv4 addresses. By convention, area 0 (zero), or 0.0.0.0, represents the core or backbone area of an OSPF network. While the identifications of other areas may be chosen at will, administrators often select the IP address of a main router in an area as the area identifier. Each additional area must have a connection to the OSPF backbone area. Such connections are maintained by an interconnecting router, known as an area border router (ABR). An ABR maintains separate link-state databases for each area it serves and maintains summarized routes for all areas in the network. 
### OSPF runs over Internet Protocol Version 4 (IPv4) and Internet Protocol Version 6 (IPv6), but does not use a transport protocol, such as UDP or TCP. It encapsulates its data directly in IP packets with protocol number 89. This is in contrast to other routing protocols, such as the Routing Information Protocol (RIP) and the Border Gateway Protocol (BGP). OSPF implements its own transport error detection and correction functions. OSPF uses multicast addressing for distributing route information within a broadcast domain. It reserves the multicast addresses 224.0.0.5 (IPv4) and FF02::5 (IPv6) for all SPF/link state routers (AllSPFRouters) and 224.0.0.6 (IPv4) and FF02::6 (IPv6) for all Designated Routers (AllDRouters). For non-broadcast networks, special provisions for configuration facilitate neighbor discovery. OSPF multicast IP packets never traverse IP routers, they never travel more than one hop. The protocol may therefore be considered a link layer protocol, but is often also attributed to the application layer in the TCP/IP model. It has a virtual link feature that can be used to create an adjacency tunnel across multiple hops. OSPF over IPv4 can operate securely between routers, optionally using a variety of authentication methods to allow only trusted routers to participate in routing. OSPFv3 (IPv6) relies on standard IPv6 protocol security (IPsec), and has no internal authentication methods. 
### For routing IP multicast traffic, OSPF supports the Multicast Open Shortest Path First (MOSPF) protocol. Cisco does not include MOSPF in their OSPF implementations. Protocol Independent Multicast (PIM) in conjunction with OSPF or other IGPs, is widely deployed. 
### OSPF version 3 introduces modifications to the IPv4 implementation of the protocol. Except for virtual links, all neighbor exchanges use IPv6 link-local addressing exclusively. The IPv6 protocol runs per link, rather than based on the subnet. All IP prefix information has been removed from the link-state advertisements and from the hello discovery packet making OSPFv3 essentially protocol-independent.  Despite the expanded IP addressing to 128 bits in IPv6, area and router Identifications are still based on 32-bit numbers.
## Router relationships  
### OSPF supports complex networks with multiple routers, including backup routers, to balance traffic load on multiple links to other subnets. Neighboring routers in the same broadcast domain or at each end of a point-to-point link communicate with each other via the OSPF protocol. Routers form adjacencies when they have detected each other. This detection is initiated when a router identifies itself in a hello protocol packet. Upon acknowledgment, this establishes a two-way state and the most basic relationship. The routers in an Ethernet or Frame Relay network select a designated router (DR) and a backup designated router (BDR) which act as a hub to reduce traffic between routers. OSPF uses both unicast and multicast transmission modes to send \"hello\" packets and link-state updates. 
### As a link-state routing protocol, OSPF establishes and maintains neighbor relationships for exchanging routing updates with other routers. The neighbor relationship table is called an adjacency database. Two OSPF routers are neighbors if they are members of the same subnet and share the same area ID, subnet mask, timers and authentication. In essence, OSPF neighborship is a relationship between two routers that allow them to see and understand each other but nothing more. OSPF neighbors do not exchange any routing information \u2013 the only packets they exchange are hello packets.  OSPF adjacencies are formed between selected neighbors and allow them to exchange routing information. Two routers must first be neighbors and only then, can they become adjacent. Two routers become adjacent if at least one of them is designated router or backup designated router (on multiaccess-type networks), or they are interconnected by a point-to-point or point-to-multipoint network type. For forming a neighbor relationship between, the interfaces used to form the relationship must be in the same OSPF area. While an interface may be configured to belong to multiple areas, this is generally not practiced. When configured in a second area, an interface must be configured as a secondary interface.
## Operation modes  
### The OSPF can have different operation modes on the following setups on an interface/network: 

### Broadcast (default), each router advertises itself by periodically multicasting hello packets, and the use of designated routers. Using multicast 
### Non-broadcast multi-access, with the use of designated routers. May need static configuration. Packets are sent as unicast, 
### Point-to-multipoint, where OSPF treats neighbours as point-to-point links. No designated router is elected. Using multicast. Separate hello packets are sent to each neighbor. 
### Point-to-point. Each router advertises itself by periodically multicasting hello packets. No designated router is elected. The interface can be IP unnumbered (without assigning a unique IP address to it). Using multicast. 
### Virtual links, the packets are sent as unicast. Can only be configured on a non-backbone area (but not stub-area). Endpoints need to be ABR, the virtual links behave as unnumbered point-to-point connections. The cost of an intra-area path between the two routers is added to the link. 
### Virtual link over Generic Routing Encapsulation (GRE). Since OSPF does not support virtual links for other areas then the backbone. A workaround is to use GRE over backbone area. Note if the same IP or router ID is used the link creates two equal-cost routes to the destination. 
### Sham link A link that connects sites that belong to the same OSPF area and share an OSPF backdoor link via MPLS VPN backbone.
## Adjacency state machine  
### Each OSPF router within a network communicates with other neighboring routers on each connecting interface to establish the states of all adjacencies. Every such communication sequence is a separate conversation identified by the pair of router IDs of the communicating neighbors. RFC 2328 specifies the protocol for initiating these conversations (Hello Protocol) and for establishing full adjacencies (Database Description Packets, Link State Request Packets). During its course, each router conversation transitions through a maximum of eight conditions defined by a state machine: 
### Down: The state down represents the initial state of a conversation when no information has been exchanged and retained between routers with the Hello Protocol. 
### Attempt: The Attempt state is similar to the Down state, except that a router is in the process of efforts to establish a conversation with another router, but is only used on NBMA networks. 
### Init: The Init state indicates that a HELLO packet has been received from a neighbor, but the router has not established a two-way conversation. 
### 2-Way: The 2-Way state indicates the establishment of a bidirectional conversation between two routers. This state immediately precedes the establishment of adjacency. This is the lowest state of a router that may be considered as a Designated Router. 
### ExStart: The ExStart state is the first step of adjacency of two routers. 
### Exchange: In the Exchange state, a router is sending its link-state database information to the adjacent neighbor. At this state, a router is able to exchange all OSPF routing protocol packets. 
### Loading: In the Loading state, a router requests the most recent link-state advertisements (LSAs) from its neighbor discovered in the previous state. 
### Full: The Full state concludes the conversation when the routers are fully adjacent, and the state appears in all router- and network-LSAs. The link state databases of the neighbors are fully synchronized.
## OSPF areas  
### A network is divided into OSPF areas that are logical groupings of hosts and networks. An area includes its connecting router having an interface for each connected network link. Each router maintains a separate link-state database for the area whose information may be summarized towards the rest of the network by the connecting router. Thus, the topology of an area is unknown outside the area. This reduces the routing traffic between parts of an autonomous system. 
### OSPF can handle thousands of routers with more a concern of reaching capacity of the forwarding information base (FIB) table when the network contains lots of routes and lower-end devices. Modern low-end routers have a full gigabyte of RAM  which allows them to handle many routers in an area 0.  Many resources refer to OSPF guides from over 20 years ago where it was impressive to have 64 MB of RAM. 
### Areas are uniquely identified with 32-bit numbers. The area identifiers are commonly written in the dot-decimal notation, familiar from IPv4 addressing. However, they are not IP addresses and may duplicate, without conflict, any IPv4 address. The area identifiers for IPv6 implementations (OSPFv3) also use 32-bit identifiers written in the same notation. When dotted formatting is omitted, most implementations expand area 1 to the area identifier 0.0.0.1, but some have been known to expand it as 1.0.0.0.Several vendors (Cisco, Allied Telesis, Juniper, Alcatel-Lucent, Huawei, Quagga), implement Totally stubby and NSSA totally stubby area for stub and not-so-stubby areas. Although not covered by RFC standards, they are considered by many to be standard features in OSPF implementations. 
### OSPF defines several area types:  

### Backbone 
### Non-Backbone/regular 
### Stub, 
### Totally stubby 
### Not-so-stubby 
### Totally Not-so-stubby 
### Transit.
## Backbone area  

### The backbone area (also known as area 0 or area 0.0.0.0) forms the core of an OSPF network. All other areas are connected to it, either directly or through other routers. OSPF requires this to prevent routing loops.  Inter-area routing happens via routers connected to the backbone area and to their own associated areas. It is the logical and physical structure for the 'OSPF domain' and is attached to all nonzero areas in the OSPF domain. Note that in OSPF the term Autonomous System Boundary Router (ASBR) is historic, in the sense that many OSPF domains can coexist in the same Internet-visible autonomous system, RFC 1996.All OSPF areas must connect to the backbone area. This connection, however, can be through a virtual link. For example, assume area 0.0.0.1 has a physical connection to area 0.0.0.0. Further assume that area 0.0.0.2 has no direct connection to the backbone, but this area does have a connection to area 0.0.0.1. Area 0.0.0.2 can use a virtual link through the transit area 0.0.0.1 to reach the backbone.  To be a transit area, an area has to have the transit attribute, so it cannot be stubby in any way.
## Regular area  

### A regular area is just a non-backbone (nonzero) area without specific feature, generating and receiving summary and external LSAs. The backbone area is a special type of such area.
## Transit area  

### A transit area is an area with two or more OSPF border routers and is used to pass network traffic from one adjacent area to another. The transit area does not originate this traffic and is not the destination of such traffic. The backbone area is a special type of transit area. 
### Examples of this: 

### Backbone area 
### In OSPF requires all areas to be directly connected to the backbone area, if not Virtual links have to be used, and the area that it transit called Transit area.
## Stub area  

### In hello packets the E flag is not high, indication \"External routing: not capable\"A stub area is an area that does not receive route advertisements external to the AS and routing from within the area is based entirely on a default route. An ABR deletes type 4, 5 LSAs from internal routers, sends them a default route of 0.0.0.0 and turns itself into a default gateway. This reduces LSDB and routing table size for internal routers. 
### Modifications to the basic concept of stub area have been implemented by systems vendors, such as the totally stubby area (TSA) and the not-so-stubby area (NSSA), both an extension in Cisco Systems routing equipment.
## Totally stubby area  

### A totally stubby area is similar to a stub area. However, this area does not allow summary routes in addition to not having external routes, that is, inter-area (IA) routes are not summarized into totally stubby areas.  The only way for traffic to get routed outside the area is a default route which is the only Type-3 LSA advertised into the area.  When there is only one route out of the area, fewer routing decisions have to be made by the route processor, which lowers system resource utilization. 

### Occasionally, it is said that a TSA can have only one ABR.
## Not-so-stubby area  

### In hello packets the N flag is set high, indication \"NSSA: supported\"A not-so-stubby area (NSSA) is a type of stub area that can import autonomous system external routes and send them to other areas, but still cannot receive AS-external routes from other areas. 
### NSSA is an extension of the stub area feature that allows the injection of external routes in a limited fashion into the stub area. A case study simulates an NSSA getting around the Stub Area problem of not being able to import external addresses. It visualizes the following activities: the ASBR imports external addresses with a type 7 LSA, the ABR converts a type 7 LSA to type 5 and floods it to other areas, the ABR acts as an \"ASBR\" for other areas. 
### The ASBRs do not take type 5 LSAs and then convert to type 7 LSAs for the area.
## Totally Not-so-stubby area  

### An addition to the standard functionality of an NSSA, the totally stubby NSSA is an NSSA that takes on the attributes of a TSA, meaning that type 3 and 4 summary routes are not flooded into this type of area.  It is also possible to declare an area both totally stubby and not-so-stubby, which means that the area will receive only the default route from area 0.0.0.0, but can also contain an autonomous system boundary router (ASBR) that accepts external routing information and injects it into the local area, and from the local area into area 0.0.0.0. 

### Redistribution into an NSSA area creates a special type of LSA known as type 7, which can exist only in an NSSA area. An NSSA ASBR generates this LSA, and an NSSA ABR router translates it into type 5 LSA which gets propagated into the OSPF domain.A newly acquired subsidiary is one example of where it might be suitable for an area to be simultaneously not-so-stubby and totally stubby if the practical place to put an ASBR is on the edge of a totally stubby area. In such a case, the ASBR does send externals into the totally stubby area, and they are available to OSPF speakers within that area. In Cisco's implementation, the external routes can be summarized before injecting them into the totally stubby area. In general, the ASBR should not advertise default into the TSA-NSSA, although this can work with extremely careful design and operation, for the limited special cases in which such an advertisement makes sense. 
### By declaring the totally stubby area as NSSA, no external routes from the backbone, except the default route, enter the area being discussed. The externals do reach area 0.0.0.0 via the TSA-NSSA, but no routes other than the default route enter the TSA-NSSA. Routers in the TSA-NSSA send all traffic to the ABR, except to routes advertised by the ASBR.
## Router types  
### OSPF defines the following overlapping categories of routers: 

### Internal router (IR) 
### An internal router has all its interfaces belonging to the same area. 
### Area border router (ABR) 
### An area border router  is a router that connects one or more areas to the main backbone network.  It is considered a member of all areas it is connected to.  An ABR keeps multiple instances of the link-state database in memory, one for each area to which that router is connected. 
### Backbone router (BR) 
### A backbone router has an interface to the backbone area. Backbone routers may also be area routers, but do not have to be. 
### Autonomous system boundary router (ASBR) 
### An autonomous system boundary router is a router that is connected by using more than one routing protocol and that exchanges routing information with routers autonomous systems.  ASBRs typically also run an exterior routing protocol (e.g., BGP), or use static routes, or both.  An ASBR is used to distribute routes received from other, external ASs throughout its own autonomous system. An ASBR creates External LSAs for external addresses and floods them to all areas via ABR. Routers in other areas use ABRs as next hops to access external addresses. Then ABRs forward packets to the ASBR that announces the external addresses.The router type is an attribute of an OSPF process. A given physical router may have one or more OSPF processes. For example, a router that is connected to more than one area, and which receives routes from a BGP process connected to another AS, is both an area border router and an autonomous system boundary router. 
### Each router has an identifier, customarily written in the dotted-decimal format (e.g., 1.2.3.4) of an IP address. This identifier must be established in every OSPF instance. If not explicitly configured, the highest logical IP address will be duplicated as the router identifier. However, since the router identifier is not an IP address, it does not have to be a part of any routable subnet in the network, and often isn't to avoid confusion.
## Non-point-to-point network  

### On networks (same subnet) with more than 2 OSPF routers as system of designated router (DR) and backup designated router (BDR), is used to reducing network traffic by providing a source for routing updates. 
### This is done using multicast address's: 

### 224.0.0.5, all routers in the topology will listen on that multicast address. 
### 224.0.0.6, DR and BRD will listen on that multicast address.The DR and BDR maintains a complete topology table of the network and sends the updates to the other routers via multicast. All routers in a multi-access network segment will form a slave/master relationship with the DR and BDR. They will form adjacencies with the DR and BDR only. Every time a router sends an update, it sends it to the DR and BDR on the multicast address 224.0.0.6. The DR will then send the update out to all other routers in the area, to the multicast address 224.0.0.5. This way all the routers do not have to constantly update each other, and can rather get all their updates from a single source.  The use of multicasting further reduces the network load.  DRs and BDRs are always setup/elected on OSPF broadcast networks.  DR's can also be elected on NBMA (Non-Broadcast Multi-Access) networks such as Frame Relay or ATM.  DRs or BDRs are not elected on point-to-point links (such as a point-to-point WAN connection) because the two routers on either side of the link must become fully adjacent and the bandwidth between them cannot be further optimized. DR and non-DR routers evolve from 2-way to full adjacency relationships by exchanging DD, Request, and Update.
## Designated router  
### A designated router (DR) is the router interface elected among all routers on a particular multiaccess network segment, generally assumed to be broadcast multiaccess. Special techniques, often vendor-dependent, may be needed to support the DR function on non-broadcast multiaccess (NBMA) media.  It is usually wise to configure the individual virtual circuits of an NBMA subnet as individual point-to-point lines; the techniques used are implementation-dependent.
## Backup designated router  
### A backup designated router (BDR) is a router that becomes the designated router if the current designated router has a problem or fails.  The BDR is the OSPF router with the second-highest priority at the time of the last election. 
### A given router can have some interfaces that are designated (DR) and others that are backup designated (BDR), and others that are non-designated. If no router is a DR or a BDR on a given subnet, the BDR is first elected, and then a second election is held for the DR.:\u200a75\u200a
## Designated router election  
### The DR is elected based on the following default criteria: 

### If the priority setting on an OSPF router is set to 0, that means it can NEVER become a DR or BDR. 
### When a DR fails and the BDR takes over, there is another election to see who becomes the replacement BDR. 
### The router sending the Hello packets with the highest priority wins the election. 
### If two or more routers tie with the highest priority setting, the router sending the Hello with the highest RID (Router ID) wins. NOTE: a RID is the highest logical (loopback) IP address configured on a router, if no logical/loopback IP address is set then the router uses the highest IP address configured on its active interfaces (e.g. 192.168.0.1 would be higher than 10.1.1.2). 
### Usually the router with the second-highest priority number becomes the BDR. 
### The priority values range between 0 \u2013 255, with a higher value increasing its chances of becoming DR or BDR. 
### If a higher priority OSPF router comes online after the election has taken place, it will not become DR or BDR until (at least) the DR and BDR fail. 
### If the current DR 'goes down' the current BDR becomes the new DR and a new election takes place to find another BDR. If the new DR then 'goes down' and the original DR is now available, still previously chosen BDR will become DR.
## Protocol messages  
### Unlike other routing protocols, OSPF does not carry data via a transport protocol, such as the User Datagram Protocol (UDP) or the Transmission Control Protocol (TCP). Instead, OSPF forms IP datagrams directly, packaging them using protocol number 89 for the IP Protocol field. OSPF defines five different message types, for various types of communication. Multiple packets can be send per frame. 
### OSFP uses the following packets 5 type: 

### Hello 
### Database description 
### Link State Request 
### Link State Update 
### Link State Acknowledgement
## Hello Packet  
### OSPF's Hello messages are used as a form of greeting, to allow a router to discover other adjacent routers on its local links and networks. The messages establish relationships between neighboring devices (called adjacencies) and communicate key parameters about how OSPF is to be used in the autonomous system or area. During normal operation, routers send hello messages to their neighbors at regular intervals (the hello interval); if a router stops receiving hello messages from a neighbor, after a set period (the dead interval) the router will assume the neighbor has gone down.
## Database description DBD  
### Database description messages contain descriptions of the topology of the autonomous system or area. They convey the contents of the link-state database (LSDB) for the area from one router to another. Communicating a large LSDB may require several messages to be sent by having the sending device designated as a master device and sending messages in sequence, with the slave (recipient of the LSDB information) responding with acknowledgments.
## Link state packets  

### Link state request (LSR) 
### Link state request messages are used by one router to request updated information about a portion of the LSDB from another router. The message specifies the link(s) for which the requesting device wants more current information.Link state update (LSU) 
### Link-state update messages contain updated information about the state of certain links on the LSDB. They are sent in response to a link state request message, and also broadcast or multicast by routers on a regular basis. Their contents are used to update the information in the LSDBs of routers that receive them.Link state acknowledgment (LSAck) 
### Link-state acknowledgment messages provide reliability to the link-state exchange process, by explicitly acknowledging receipt of a Link State Update message.
## OSPF v2 area types and accepted LSAs  
### Not all area types use all LSA. Below is a matrix of accepted LSAs.
## Routing metrics  
### OSPF uses path cost as its basic routing metric, which was defined by the standard not to equate to any standard value such as speed, so the network designer could pick a metric important to the design. In practice, it is determined by comparing the speed of the interface to a reference-bandwidth for the OSPF process.  The cost is determined by dividing the reference bandwidth by the interface speed (although the cost for any interface can be manually overridden). If a reference bandwidth is set to '10000', then a 10 Gbit/s link will have a cost of 1.  Any speeds less than 1 are rounded up to 1. Here is an example table that shows the routing metric or 'cost calculation' on an interface. 

### Type-1 LSA has a size of 16-bit field (65,535 in decimal) 
### Type-3 LSA has a size of 24-bit field (16,777,216 in decimal)OSPF is a layer 3 protocol: if a layer 2 switch is between the two devices running OSPF, one side may negotiate a speed different from the other side. This can create an asymmetric routing on the link (Router 1 to Router 2 could cost '1' and the return path could cost '10'), which may lead to unintended consequences. 
### Metrics, however, are only directly comparable when of the same type. Four types of metrics are recognized. In decreasing preference, these types are (for example, an intra-area route is always preferred to an external route regardless of metric): 

### Intra-area 
### Inter-area 
### External Type 1, which includes both the external path cost and the sum of internal path costs to the ASBR that advertises the route, 
### External Type 2, the value of which is solely that of the external path cost,
## OSPF v3  
### OSPF version 3 introduces modifications to the IPv4 implementation of the protocol.  
### Despite the expanded IP addressing to 128-bits in IPv6, area and router identifications are still based on 32-bit numbers.
## High level Changes  
### Except for virtual links, all neighbor  exchanges use IPv6 link-local addressing exclusively. The IPv6 protocol runs per link, rather than based on the subnet. 
### All IP prefix information has been removed from the link-state advertisements and from the hello discovery packet making OSPFv3 essentially protocol-independent. 
### Three separate flooding scopes for LSAs: 
### Link-local scope, LSA is only flooded on the local link and no further. 
### Area scope, LSA is flooded throughout a single OSPF area. 
### AS scope.  LSA is flooded throughout the routing domain. 
### Use of IPv6 Link-Local Addresses, for neighbor discovery, auto-configuration. 
### Authentication has been moved to the IP Authentication Header
## Changes introduced in OSPF v3, then backported by vendors to v2  
### Explicit Support for Multiple Instances per Link
## Packet Format Changes  
### OSPF version number changed to 3 
### From the LSA header, The Options field has been removed. 
### In Hello packets and Database Description, the Options field is changed from 16 to 24 bit. 
### In Hello packet, the address information has been removed. the Interface ID has been added. 
### In router-LSAs, Two Options bits, the \"R-bit\" and the \"V6-bit\", have been added. 
### \"R-bit\", Allows for multi-homed hosts to participate in the routing protocol. 
### \"V6-bit\", specializes the R-bit. 
### Add \"Instance ID\" that allows multiple OSPF protocol instances on the same logical interface.
## LSA Format Changes  
### The LSA Type field, is changed to 16. 
### Add support for Handling Unknown LSA Types 
### Three of bits is used for encoding flooding scope. 
### With IPv6, addresses in LSAs are now expressed as prefix and prefix length. 
### In Router-LSAs and network-LSAs, the address information is removed. 
### Router-LSAs and network-LSAs, is made network protocol independent. 
### A new LSA type is added Link-LSA, Link-LSA provide the router's link-local address to all other routers attached to the logical interface, list of IPv6 prefixes to associate with the link, and can send information that reflect the router's capabilities. 
### LSA Type-3 summary-LSAs have been renamed \"inter-area-prefix-LSAs\". 
### LSA Type-4 summary LSAs have been renamed \"inter-area-router-LSAs\". 
### Intra-area-prefix-LSA is added, a LSA that carries all IPv6 prefix information.
## OSPF over MPLS-VPN  

### A customer can use OSPF over a MPLS-VPN, where the service provider uses  BGP or RIP as their interior gateway protocol. 
### When using OSPF over MPLS-VPN, the VPN backbone becomes part of the OSPF backbone area 0. In all areas, isolated copies of the IGP are run. 
### Advantages:  

### The MPLS-VPN is transparent to the customer's OSPF standard routing. 
### Customer's equipment only needs to support OSPF. 
### Reduce the need for tunnels (Generic Routing Encapsulation, IPsec, wireguard) to use OSPF.To achieve this, a non-standard OSPF-BGP redistribution is used. All OSPF routes retain the source LSA type and metric. 
### To prevent loops, an optional DN bit is used in LSAs to indicate that a route has already been sent from the provider edge to the customer's equipment.
## OSPF extensions 
## Traffic engineering  
### OSPF-TE is an extension to OSPF extending the expressivity to allow for traffic engineering and use on non-IP networks. Using OSPF-TE, more information about the topology can be exchanged using opaque LSA carrying type\u2013length\u2013value elements. These extensions allow OSPF-TE to run completely out of band of the data plane network. This means that it can also be used on non-IP networks, such as optical networks. 
### OSPF-TE is used in GMPLS networks as a means to describe the topology over which GMPLS paths can be established. GMPLS uses its own path setup and forwarding protocols, once it has the full network map. 
### In the Resource Reservation Protocol (RSVP), OSPF-TE is used for recording and flooding RSVP signaled bandwidth reservations for label switched paths within the link-state database.
## Optical routing  
### RFC 3717 documents work in optical routing for IP based on extensions to OSPF and IS-IS.
## Multicast Open Shortest Path First  
### The Multicast Open Shortest Path First (MOSPF) protocol is an extension to OSPF to support multicast routing. MOSPF allows routers to share information about group memberships.
## OSPF in broadcast and non-broadcast networks  
### In broadcast multiple-access networks, neighbor adjacency is formed dynamically using multicast hello packets to 224.0.0.5. A DR and BDR are elected normally, and function normally. 
### For non-broadcast multiple-access networks (NBMA), the following two official modes are defined: 
### non-broadcast 
### point-to-multipointCisco has defined the following three additional modes for OSPF in NBMA topologies: 
### point-to-multipoint non-broadcast 
### broadcast 
### point-to-point
## Notable implementations  
### Allied Telesis implements OSPFv2 & OSPFv3 in Allied Ware Plus (AW+) 
### Arista Networks implements OSPFv2 and OSPFv3 
### BIRD implements both OSPFv2 and OSPFv3 
### Cisco IOS and NX-OS 
### Cisco Meraki 
### D-Link implements OSPFv2 on Unified Services Router. 
### Dell's FTOS implements OSPFv2 and OSPFv3 
### ExtremeXOS 
### GNU Zebra, a GPL routing suite for Unix-like systems supporting OSPF 
### Juniper Junos 
### NetWare implements OSPF in its Multi Protocol Routing module. 
### OpenBSD includes OpenOSPFD, an OSPFv2 implementation. 
### Quagga, a fork of GNU Zebra for Unix-like systems 
### FRRouting, the successor of Quagga 
### XORP, a routing suite implementing RFC2328 (OSPFv2) and RFC2740 (OSPFv3) for both IPv4 and IPv6 
### Windows NT 4.0 Server, Windows 2000 Server and Windows Server 2003 implemented OSPFv2 in the Routing and Remote Access Service, although the functionality was removed in Windows Server 2008.
## Applications  
### OSPF is a widely deployed routing protocol that can converge a network in a few seconds and guarantee loop-free paths. It has many features that allow the imposition of policies about the propagation of routes that it may be appropriate to keep local, for load sharing, and for selective route importing. IS-IS, in contrast, can be tuned for lower overhead in a stable network, the sort more common in ISP than enterprise networks. There are some historical accidents that made IS-IS the preferred IGP for ISPs, but ISPs today may well choose to use the features of the now-efficient implementations of OSPF, after first considering the pros and cons of IS-IS in service provider environments.OSPF can provide better load-sharing on external links than other IGPs. When the default route to an ISP is injected into OSPF from multiple ASBRs as a Type I external route and the same external cost specified, other routers will go to the ASBR with the least path cost from its location. This can be tuned further by adjusting the external cost. If the default route from different ISPs is injected with different external costs, as a Type II external route, the lower-cost default becomes the primary exit and the higher-cost becomes the backup only. 
### The only real limiting factor that may compel major ISPs to select IS-IS over OSPF is if they have a network with more than 850 routers.
## See also  
### Fabric Shortest Path First 
### Mesh networking 
### Route analytics 
### Routing 
### Shortest path problem
## References 
## Further reading  
### Colton, Andrew (October 2003). OSPF for Cisco Routers. Rocket Science Press. ISBN 978-0972286213. 
### Doyle, Jeff; Carroll, Jennifer (2005). Routing TCP/IP. Vol. 1 (2nd ed.). Cisco Press. ISBN 978-1-58705-202-6. 
### Moy, John T. (1998). OSPF: Anatomy of an Internet Routing Protocol. Addison-Wesley. ISBN 978-0201634723. 
### Parkhurst, William R. (2002). Cisco OSPF Command and Configuration Handbook. ISBN 978-1-58705-071-8. 
### Basu, Anindya; Riecke, Jon (2001). \"Stability issues in OSPF routing\". Proceedings of the 2001 conference on Applications, technologies, architectures, and protocols for computer communications. SIGCOMM '01. pp. 225\u2013236. CiteSeerX 10.1.1.99.6393. doi:10.1145/383059.383077. ISBN 978-1-58113-411-7. S2CID 7555753. 
### Valadas, Rui (2019). OSPF and IS-IS: From Link State Routing Principles to Technologies. CRC Press. doi:10.1201/9780429027543. ISBN 9780429027543.
## External links  
### IETF OSPF Working Group 
### Cisco OSPF 
### Cisco OSPF Areas and Virtual Links 
### Summary of OSPF v2"
## Links
### 10 GigE
### 2.5GBASE-T and 5GBASE-T
### Addison-Wesley
### Address Resolution Protocol
### Allied Telesis
### Application layer
### Arista Networks
### Autonomous system (Internet)
### BGP
### Bird Internet routing daemon
### Border Gateway Protocol
### Broadcast domain
### Broadcasting (networking)
### Cisco IOS
### Cisco Meraki
### Cisco NX-OS
### Cisco Press
### Cisco Systems
### CiteSeerX (identifier)
### Classless Inter-Domain Routing
### Communication protocol
### Convergence (routing)
### D-Link
### DHCPv6
### Data type
### Datagram Congestion Control Protocol
### Dijkstra's algorithm
### Doi (identifier)
### Domain Name System
### Dot-decimal notation
### Dynamic Host Configuration Protocol
### Enterprise network
### Explicit Congestion Notification
### ExtremeXOS
### FRRouting
### Fabric Shortest Path First
### File Transfer Protocol
### Force10 Networks
### Forwarding information base
### GMPLS
### GNU General Public License
### GNU Zebra
### Generic Routing Encapsulation
### HTTPS
### Hypertext Transfer Protocol
### IETF
### IP address
### IP multicast
### IPsec
### IPv4
### IPv6
### IS-IS
### ISBN (identifier)
### Instance (computer science)
### Interior gateway protocol
### Internet Control Message Protocol
### Internet Control Message Protocol for IPv6
### Internet Group Management Protocol
### Internet Layer
### Internet Message Access Protocol
### Internet Protocol
### Internet layer
### Internet protocol suite
### Juniper Junos
### Label switched path
### Lightweight Directory Access Protocol
### Link-state advertisement
### Link-state routing protocol
### Link layer
### List of IP protocol numbers
### MQTT
### Media Gateway Control Protocol
### Medium access control
### Mesh networking
### Metrics (networking)
### Multicast
### Multicast Open Shortest Path First
### Multicast address
### Multiprotocol Label Switching
### Neighbor Discovery Protocol
### NetWare
### Network News Transfer Protocol
### Network Time Protocol
### Network service provider
### Non-broadcast multiaccess
### Non-broadcast multiple-access network
### OpenBSD
### OpenOSPFD
### Open Network Computing Remote Procedure Call
### Point-to-Point Protocol
### Point-to-multipoint communication
### Point-to-point (network topology)
### Point-to-point link
### Post Office Protocol
### Precision Time Protocol
### Protocol Independent Multicast
### QUIC
### Quagga (Software)
### RFC (identifier)
### Real-time Transport Protocol
### Real Time Streaming Protocol
### Request for Comments
### Resource Reservation Protocol
### Rocket Science Press
### Round-trip time
### Route analytics
### Route redistribution
### Route summarization
### Routing
### Routing Information Protocol
### Routing and Remote Access Service
### Routing loop
### Routing protocol
### S2CID (identifier)
### SIGCOMM
### Secure Shell
### Session Initiation Protocol
### Shortest-path tree
### Shortest path problem
### Simple Mail Transfer Protocol
### Simple Network Management Protocol
### Small form-factor pluggable transceiver
### Stream Control Transmission Protocol
### Subnetwork
### Telnet
### Transmission Control Protocol
### Transmission control protocol
### Transport Layer Security
### Transport layer
### Transport protocol
### Tunneling protocol
### Type–length–value
### Unicast
### Unix-like
### User Datagram Protocol
### User datagram protocol
### Windows 2000
### Windows NT 4.0
### Windows Server 2003
### Windows Server 2008
### Wireguard
### XMPP
### XORP
## References
### [Reference](http://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) - http://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html
### [Reference](http://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/12-4t/iro-12-4t-book/iro-cfg.html) - http://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/12-4t/iro-12-4t-book/iro-cfg.html
### [Reference](http://www.cisco.com/en/US/docs/ios/iproute_ospf/command/reference/iro_cr_book.pdf) - http://www.cisco.com/en/US/docs/ios/iproute_ospf/command/reference/iro_cr_book.pdf
### [Reference](http://www.ciscopress.com/bookstore/product.asp?isbn=1587052024) - http://www.ciscopress.com/bookstore/product.asp?isbn=1587052024
### [Reference](http://www.groupstudy.com/bookstore/samples/thomas/) - http://www.groupstudy.com/bookstore/samples/thomas/
### [Reference](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.99.6393) - http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.99.6393
### [Reference](http://doi.org/10.1145%2F383059.383077) - http://doi.org/10.1145%2F383059.383077
### [Reference](http://doi.org/10.1201%2F9780429027543) - http://doi.org/10.1201%2F9780429027543
### [Reference](http://doi.org/10.17487%2FRFC2328) - http://doi.org/10.17487%2FRFC2328
### [Reference](http://doi.org/10.17487%2FRFC3630) - http://doi.org/10.17487%2FRFC3630
### [Reference](http://doi.org/10.17487%2FRFC3717) - http://doi.org/10.17487%2FRFC3717
### [Reference](http://doi.org/10.17487%2FRFC4577) - http://doi.org/10.17487%2FRFC4577
### [Reference](http://doi.org/10.17487%2FRFC5340) - http://doi.org/10.17487%2FRFC5340
### [Reference](http://datatracker.ietf.org/doc/rfc3630/) - http://datatracker.ietf.org/doc/rfc3630/
### [Reference](http://tools.ietf.org/html/rfc1930) - http://tools.ietf.org/html/rfc1930
### [Reference](http://tools.ietf.org/html/rfc2328#page-185) - http://tools.ietf.org/html/rfc2328#page-185
### [Reference](http://tools.ietf.org/html/rfc5340#page-57) - http://tools.ietf.org/html/rfc5340#page-57
### [Reference](https://www.cisco.com/c/en/us/products/ios-nx-os-software/open-shortest-path-first-ospf/index.html) - https://www.cisco.com/c/en/us/products/ios-nx-os-software/open-shortest-path-first-ospf/index.html
### [Reference](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13703-8.html) - https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13703-8.html
### [Reference](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/15-sy/iro-15-sy-book/iro-sham-link.html) - https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/15-sy/iro-15-sy-book/iro-sham-link.html
### [Reference](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/mp_l3_vpns/configuration/xe-16-10/mp-l3-vpns-xe-16-10-book/mpls-vpn-ospf-pe-and-ce-support.html) - https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/mp_l3_vpns/configuration/xe-16-10/mp-l3-vpns-xe-16-10-book/mpls-vpn-ospf-pe-and-ce-support.html
### [Reference](https://mikrotik.com/product/rb4011igs_rm) - https://mikrotik.com/product/rb4011igs_rm
### [Reference](https://www.networkworld.com/article/2348778/my-favorite-interview-question.html) - https://www.networkworld.com/article/2348778/my-favorite-interview-question.html
### [Reference](https://www.oreilly.com/library/view/cisco-ios-cookbook/0596527225/ch08s15.html) - https://www.oreilly.com/library/view/cisco-ios-cookbook/0596527225/ch08s15.html
### [Reference](https://www.oreilly.com/library/view/cisco-ios-cookbook/0596527225/ch08s04.html) - https://www.oreilly.com/library/view/cisco-ios-cookbook/0596527225/ch08s04.html
### [Reference](https://routing-bits.com/2009/08/06/ospf-convergence/) - https://routing-bits.com/2009/08/06/ospf-convergence/
### [Reference](https://www.racf.bnl.gov/Facility/TechnologyMeeting/Archive/06-30-04-CISCO/Using-OSPF-in-MPLS-VPN-Environment.pdf) - https://www.racf.bnl.gov/Facility/TechnologyMeeting/Archive/06-30-04-CISCO/Using-OSPF-in-MPLS-VPN-Environment.pdf
### [Reference](https://id.loc.gov/authorities/subjects/sh2003001440) - https://id.loc.gov/authorities/subjects/sh2003001440
### [Reference](https://www.packetcoders.io/ospf-areas-explained/) - https://www.packetcoders.io/ospf-areas-explained/
### [Reference](https://kb.juniper.net/InfoCenter/index?page=content&id=KB19371) - https://kb.juniper.net/InfoCenter/index?page=content&id=KB19371
### [Reference](https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/secondary-edit-protocols-ospf.html) - https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/secondary-edit-protocols-ospf.html
### [Reference](https://www.juniper.net/documentation/en_US/junose15.1/topics/concept/ospf-sham-links-overview.html) - https://www.juniper.net/documentation/en_US/junose15.1/topics/concept/ospf-sham-links-overview.html
### [Reference](https://www.juniper.net/documentation/us/en/software/junos/ospf/topics/topic-map/configuring-ospf-areas.html#id-ospf-designated-router-overview) - https://www.juniper.net/documentation/us/en/software/junos/ospf/topics/topic-map/configuring-ospf-areas.html#id-ospf-designated-router-overview
### [Reference](https://www.juniper.net/documentation/us/en/software/junos/interfaces-ethernet-switches/topics/topic-map/switches-interface-gre.html) - https://www.juniper.net/documentation/us/en/software/junos/interfaces-ethernet-switches/topics/topic-map/switches-interface-gre.html
### [Reference](https://packetpushers.net/podcast/show-134-ospf-design-part-1-debunking-the-multiple-area-myth) - https://packetpushers.net/podcast/show-134-ospf-design-part-1-debunking-the-multiple-area-myth
### [Reference](https://web.archive.org/web/20000831182105/http://www.groupstudy.com/bookstore/samples/thomas/) - https://web.archive.org/web/20000831182105/http://www.groupstudy.com/bookstore/samples/thomas/
### [Reference](https://web.archive.org/web/20120425041808/http://www.cisco.com/en/US/docs/ios/iproute_ospf/command/reference/iro_cr_book.pdf) - https://web.archive.org/web/20120425041808/http://www.cisco.com/en/US/docs/ios/iproute_ospf/command/reference/iro_cr_book.pdf
### [Reference](https://web.archive.org/web/20160612140344/https://www.nanog.org/meetings/abstract?id=1149) - https://web.archive.org/web/20160612140344/https://www.nanog.org/meetings/abstract?id=1149
### [Reference](https://web.archive.org/web/20180620232619/https://www.nanog.org/meetings/abstract?id=1084) - https://web.archive.org/web/20180620232619/https://www.nanog.org/meetings/abstract?id=1084
### [Reference](https://www.freesoft.org/CIE/Topics/89.htm) - https://www.freesoft.org/CIE/Topics/89.htm
### [Reference](https://www.iana.org/assignments/bgp-extended-communities/bgp-extended-communities.xhtml) - https://www.iana.org/assignments/bgp-extended-communities/bgp-extended-communities.xhtml
### [Reference](https://datatracker.ietf.org/doc/html/rfc1131) - https://datatracker.ietf.org/doc/html/rfc1131
### [Reference](https://datatracker.ietf.org/doc/html/rfc1247) - https://datatracker.ietf.org/doc/html/rfc1247
### [Reference](https://datatracker.ietf.org/doc/html/rfc1583) - https://datatracker.ietf.org/doc/html/rfc1583
### [Reference](https://datatracker.ietf.org/doc/html/rfc2178) - https://datatracker.ietf.org/doc/html/rfc2178
### [Reference](https://datatracker.ietf.org/doc/html/rfc2328) - https://datatracker.ietf.org/doc/html/rfc2328
### [Reference](https://datatracker.ietf.org/doc/html/rfc2740) - https://datatracker.ietf.org/doc/html/rfc2740
### [Reference](https://datatracker.ietf.org/doc/html/rfc3101) - https://datatracker.ietf.org/doc/html/rfc3101
### [Reference](https://datatracker.ietf.org/doc/html/rfc3137) - https://datatracker.ietf.org/doc/html/rfc3137
### [Reference](https://datatracker.ietf.org/doc/html/rfc3717) - https://datatracker.ietf.org/doc/html/rfc3717
### [Reference](https://datatracker.ietf.org/doc/html/rfc4576) - https://datatracker.ietf.org/doc/html/rfc4576
### [Reference](https://datatracker.ietf.org/doc/html/rfc4577) - https://datatracker.ietf.org/doc/html/rfc4577
### [Reference](https://datatracker.ietf.org/doc/html/rfc5340) - https://datatracker.ietf.org/doc/html/rfc5340
### [Reference](https://datatracker.ietf.org/doc/html/rfc5709) - https://datatracker.ietf.org/doc/html/rfc5709
### [Reference](https://datatracker.ietf.org/doc/html/rfc6549) - https://datatracker.ietf.org/doc/html/rfc6549
### [Reference](https://datatracker.ietf.org/doc/html/rfc6845) - https://datatracker.ietf.org/doc/html/rfc6845
### [Reference](https://datatracker.ietf.org/doc/html/rfc6860) - https://datatracker.ietf.org/doc/html/rfc6860
### [Reference](https://datatracker.ietf.org/doc/html/rfc7503) - https://datatracker.ietf.org/doc/html/rfc7503
### [Reference](https://datatracker.ietf.org/doc/html/rfc8362) - https://datatracker.ietf.org/doc/html/rfc8362
### [Reference](https://datatracker.ietf.org/wg/ospf/charter/) - https://datatracker.ietf.org/wg/ospf/charter/
### [Reference](https://tools.ietf.org/html/rfc3101) - https://tools.ietf.org/html/rfc3101
### [Reference](https://www.nanog.org/meetings/abstract?id=1084) - https://www.nanog.org/meetings/abstract?id=1084
### [Reference](https://www.nanog.org/meetings/abstract?id=1149) - https://www.nanog.org/meetings/abstract?id=1149
### [Reference](https://api.semanticscholar.org/CorpusID:7555753) - https://api.semanticscholar.org/CorpusID:7555753
### [Reference](https://www.wikidata.org/wiki/Q220169#identifiers) - https://www.wikidata.org/wiki/Q220169#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/8/83/OSPF-MPLS_VPN_figur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/8/83/OSPF-MPLS_VPN_figur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/4/41/OSPF-NSSA_figur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/4/41/OSPF-NSSA_figur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/9/97/OSPF-Totally_NSSA_figur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/9/97/OSPF-Totally_NSSA_figur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/5/58/OSPF-Totally_stubby_area_figur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/5/58/OSPF-Totally_stubby_area_figur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/e/ed/OSPF-Trasit_area_virtual_linkfigur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/e/ed/OSPF-Trasit_area_virtual_linkfigur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/5/5a/OSPF-Type-4_%26_Type-5_figur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/5/5a/OSPF-Type-4_%26_Type-5_figur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/8/89/OSPF-area0_area122_mutliarea_figur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/8/89/OSPF-area0_area122_mutliarea_figur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/b/b4/OSPF-area0_standalone_figur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/b/b4/OSPF-area0_standalone_figur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/6/62/OSPF-stubby_area_figur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/6/62/OSPF-stubby_area_figur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/07/OSPF-type3_Summary-LSAs_figur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/0/07/OSPF-type3_Summary-LSAs_figur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/e/e8/OSPF-type_1_figur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/e/e8/OSPF-type_1_figur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/08/OSPF-type_2_Network-LSA_figur.drawio.png) - https://upload.wikimedia.org/wikipedia/commons/0/08/OSPF-type_2_Network-LSA_figur.drawio.png
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg