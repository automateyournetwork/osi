# Anycast
## [URL](https://en.wikipedia.org/wiki/Anycast) - https://en.wikipedia.org/wiki/Anycast
## Catagories
### All Wikipedia articles written in American English
### Articles with short description
### Domain Name System
### Internet architecture
### Multihoming
### Short description matches Wikidata
### Use American English from January 2019
### Use mdy dates from September 2021
### "Anycast is a network addressing and routing methodology in which a single destination IP address is shared by devices (generally servers) in multiple locations. Routers direct packets addressed to this destination to the location nearest the sender, using their normal decision-making algorithms, typically the lowest number of BGP network hops. Anycast routing is widely used by content delivery networks such as web and DNS hosts, to bring their content closer to end users.
## Addressing methods  
### There are four principal addressing methods in the Internet Protocol: 

### Unicast delivers a message to a single specific node using a one-to-one association between a sender and destination: each destination address uniquely identifies a single receiver endpoint. 
### Broadcast delivers a message to all nodes in the network using a one-to-all association; a single datagram (or packet) from one sender is routed to all of the possibly multiple endpoints associated with the broadcast address. The network automatically replicates datagrams as needed to reach all the recipients within the scope of the broadcast, which is generally an entire network subnet. 
### Multicast delivers a message to a group of nodes that have expressed interest in receiving the message using a one-to-many-of-many or many-to-many-of-many association; datagrams are routed simultaneously in a single transmission to many recipients. Multicast differs from broadcast in that the destination address designates a subset, not necessarily all, of the accessible nodes. 
### Anycast delivers a message to any one out of a group of nodes, typically the one nearest to the source using a one-to-one-of-many association where datagrams are routed to any single member of a group of potential receivers that are all identified by the same destination address.  The routing algorithm selects the single receiver from the group based on which is the nearest according to some distance or cost measure.
## History  
### The first documented use of anycast routing for topological load-balancing of Internet-connected services was in 1989, the technique was first formally documented in the IETF four years later in RFC 1546, and it was first applied to critical infrastructure in 2001 with the anycasting of the I-root nameserver.
## Early objections  
### Early objections to the deployment of anycast routing centered on the perceived conflict between long-lived TCP connections and the volatility of the Internet's routed topology. In concept, a long-lived connection, such as an FTP file transfer (which might have taken hours to complete in the mid-1990s, when this issue was being debated) might be re-routed to a different anycast instance in mid-connection due to changes in network topology or routing, with the result that the server changes mid-connection, and the new server is not aware of the connection and does not possess the TCP connection state of the previous anycast instance. 
### In practice, such problems were not observed, and these objections dissipated by the early 2000s. Many initial anycast deployments consisted of DNS servers, using principally UDP transport. Measurements of long-term anycast flows revealed very few failures due to mid-connection instance switches, far fewer (less than 0.017% or \"less than one flow per ten thousand per hour of duration\" according to various sources) than were attributed to other causes of failure. Numerous mechanisms were developed to efficiently share state between anycast instances. And some TCP-based protocols, notably HTTP, incorporated \"redirect\" mechanisms, whereby anycast service addresses could be used to locate the nearest instance of a service, whereupon a user would be redirected to that specific instance prior to the initiation of any long-lived stateful transaction.
## Internet Protocol version 4  
### Anycast can be implemented via Border Gateway Protocol (BGP). Multiple hosts (usually in different geographic areas) are given the same unicast IP address and different routes to the address are announced through BGP.  Routers consider these to be alternative routes to the same destination, even though they are actually routes to different destinations with the same address. As usual, routers select a route by whatever distance metric is in use (the least cost, least congested, shortest).  Selecting a route in this setup amounts to selecting a destination.
## Internet Protocol version 6  
### Anycast is supported explicitly in IPv6. RFC 4291, which covers IPv6 addressing architecture, reserves Interface Identifier 0 within an IPv6 subnet as the \"Subnet Router\" anycast address.  In addition, RFC 2526 reserves a block of 128 Interface Identifiers within a subnet as anycast addresses. 
### Most IPv6 routers on the path of an anycast packet through the network will not distinguish it from a unicast packet, but special handling is required from the routers near the destination (that is, within the scope of the anycast address) as they are required to route an anycast packet to the \"nearest\" interface within that scope which has the proper anycast address, according to whatever measure of distance (hops, cost, etc.) is being used. 
### The method used in IPv4 of advertising multiple routes in BGP to multiply-assigned unicast addresses also still works in IPv6, and can be used to route packets to the nearest of several geographically dispersed hosts with the same address.  This approach, which does not depend on anycast-aware routers,  has the same use cases together with the same problems and limitations as in IPv4.
## Applications  
### With the growth of the Internet, network services increasingly have high-availability requirements. As a result, operation of anycast services (RFC 4786) has grown in popularity among network operators.
## Domain Name System  
### All Internet root nameservers are implemented as clusters of hosts using anycast addressing. All 13 root servers A\u2013M exist in multiple locations, with 11 on multiple continents. (Root servers B and H exist in two U.S. locations.) The servers use anycast address announcements to provide a decentralized service. This has accelerated the deployment of physical (rather than logical) root servers outside the United States. RFC 3258 documents the use of anycast addressing to provide authoritative DNS services. Many commercial DNS providers have switched to an IP anycast environment to increase query performance and redundancy, and to implement load balancing.
## IPv6 transition  
### In IPv4 to IPv6 transitioning, anycast addressing may be deployed to provide IPv6 compatibility to IPv4 hosts. This method, 6to4, uses a default gateway with the IP address 192.88.99.1, as described in RFC 3068. This allows multiple providers to implement 6to4 gateways without hosts having to know each individual provider's gateway addresses. This method has been deprecated in RFC 7526.
## Content delivery networks  
### Content delivery networks may use anycast for actual HTTP connections to their distribution centers, or for DNS. Because most HTTP connections to such networks request static content such as images and style sheets, they are generally short-lived and stateless across subsequent TCP sessions. The general stability of routes and statelessness of connections makes anycast suitable for this application, even though it uses TCP.
## Connectivity between Anycast and Multicast network  
### Anycast rendezvous point can be used in Multicast Source Discovery Protocol (MSDP) and its advantageous application as Anycast RP is an intra-domain feature that provides redundancy and load-sharing capabilities. If the multiple anycast rendezvous point is used, IP routing automatically will select the topologically closest rendezvous point for each source and receiver.  It would provide a multicast network with the fault tolerance requirements.
## Security  
### Anycast allows any operator whose routing information is accepted by an intermediate router to hijack any packets intended for the anycast address. While this at first sight appears insecure, it is no different from the routing of ordinary IP packets, and no more or less secure. As with conventional IP routing, careful filtering of who is and is not allowed to propagate route announcements is crucial to prevent man-in-the-middle or blackhole attacks. The former can also be prevented by encrypting and authenticating messages, such as using Transport Layer Security, while the latter can be frustrated by onion routing.
## Reliability  
### Anycast is normally highly reliable, as it can provide automatic failover without adding complexity or new potential points of failure.  Anycast applications typically feature external \"heartbeat\" monitoring of the server's function, and withdraw the route announcement if the server fails. In some cases this is done by the actual servers announcing the anycast prefix to the router over OSPF or another IGP. If the servers die, the router will automatically withdraw the announcement. \"Heartbeat\" functionality is important because, if the announcement continues for a failed server, the server will act as a \"black hole\" for nearby clients; this is the most serious mode of failure for an anycast system. Even in this event, this kind of failure will only cause a total failure for clients that are closer to this server than any other, and will not cause a global failure. However, even the automation necessary to implement \"heartbeat\" routing withdrawal can itself add a potential point of failure, as seen in the 2021 Facebook outage.
## Mitigation of denial-of-service attacks  
### In denial-of-service attacks, a rogue network host may advertise itself as an anycast server for a vital network service, to provide false information or simply block service. Anycast methodologies on the Internet may be exploited to distribute DDoS attacks and reduce their effectiveness:  As traffic is routed to the closest node, a process over which the attacker has no control, the DDoS traffic flow will be distributed amongst the closest nodes.  Thus, not all nodes might be affected.  This may be a reason to deploy anycast addressing.The effectiveness of this technique depends upon maintaining the secrecy of any unicast addresses associated with anycast service nodes, however, since an attacker in possession of the unicast addresses of individual nodes can attack them from any location, bypassing anycast addressing methods.
## Local and global nodes  
### Some anycast deployments on the Internet distinguish between local and global nodes to benefit the local community, by addressing local nodes preferentially. An example is the Domain Name System. Local nodes are often announced with the no-export BGP community to prevent hosts from announcing them to their peers, i.e. the announcement is kept in the local area. Where both local and global nodes are deployed, the announcements from global nodes are often AS prepended (i.e. the AS is added a few more times) to make the path longer so that a local node announcement is preferred over a global node announcement.
## See also  

### Multihoming 
### Line hunting, for an equivalent system for telephones
## References 
## External links  
### Best Practices in IPv4 Anycast Routing Tutorial on anycast routing configuration."
## Links
### 2021 Facebook outage
### 6to4
### Addressing
### Anycast
### Autonomous system (Internet)
### BGP
### Border Gateway Protocol
### Border gateway protocol
### Broadcast address
### Broadcasting (networking)
### Content delivery network
### DDoS
### DNS
### Datagram
### Denial-of-service attack
### Doi (identifier)
### Domain Name System
### Failover
### HTTP
### Hop (networking)
### ICANN
### IEEE
### IP address
### IPv6
### IPv6 transition mechanisms
### ISBN (identifier)
### Interior gateway protocol
### Internet Engineering Task Force
### Internet Protocol
### Line hunting
### Man-in-the-middle attack
### Multicast
### Multihoming
### Onion routing
### Open Shortest Path First
### Packet (information technology)
### Packet Clearing House
### Packet drop attack
### RFC (identifier)
### Root name server
### Root nameserver
### Router (computing)
### Routing
### Style sheet (web development)
### Subnetwork
### Transmission Control Protocol
### Transport Layer Security
### Unicast
### United States
## References
### [Reference](http://www.isi.edu/b-root/) - http://www.isi.edu/b-root/
### [Reference](http://pch.net/root-servers) - http://pch.net/root-servers
### [Reference](http://www.pch.net/resources/papers/ipv4-anycast/ipv4-anycast.pdf) - http://www.pch.net/resources/papers/ipv4-anycast/ipv4-anycast.pdf
### [Reference](http://doi.org/10.1109%2F4236.991450) - http://doi.org/10.1109%2F4236.991450
### [Reference](http://www.icann.org/announcements/factsheet-dns-attack-08mar07_v1.1.pdf) - http://www.icann.org/announcements/factsheet-dns-attack-08mar07_v1.1.pdf
### [Reference](http://tools.ietf.org/pdf/rfc1546.pdf) - http://tools.ietf.org/pdf/rfc1546.pdf
### [Reference](http://tools.ietf.org/pdf/rfc4786.pdf) - http://tools.ietf.org/pdf/rfc4786.pdf
### [Reference](http://www.root-servers.org/) - http://www.root-servers.org/
### [Reference](https://www.cisco.com/c/en/us/td/docs/ios/solutions_docs/ip_multicast/White_papers/anycast.html) - https://www.cisco.com/c/en/us/td/docs/ios/solutions_docs/ip_multicast/White_papers/anycast.html
### [Reference](https://books.google.com/books?id=Tyte75MFbHkC&q=anycast+local+and+global+nodes&pg=PA102) - https://books.google.com/books?id=Tyte75MFbHkC&q=anycast+local+and+global+nodes&pg=PA102
### [Reference](https://www.mail-archive.com/nanog@nanog.org/msg103547.html) - https://www.mail-archive.com/nanog@nanog.org/msg103547.html
### [Reference](https://www.microsoft.com/en-us/research/uploads/prod/2019/07/regionalloss.pdf) - https://www.microsoft.com/en-us/research/uploads/prod/2019/07/regionalloss.pdf
### [Reference](https://www.pch.net/resources/Tutorials/anycast/Anycast-v06.pdf) - https://www.pch.net/resources/Tutorials/anycast/Anycast-v06.pdf
### [Reference](https://web.archive.org/web/20200105061928/https://books.google.ca/books?id=Tyte75MFbHkC&lpg=PA103&ots=p3K484ueyF&dq=anycast%20local%20and%20global%20nodes&pg=PA102%23v=onepage&q=anycast%20local%20and%20global%20nodes&f=false) - https://web.archive.org/web/20200105061928/https://books.google.ca/books?id=Tyte75MFbHkC&lpg=PA103&ots=p3K484ueyF&dq=anycast%20local%20and%20global%20nodes&pg=PA102%23v=onepage&q=anycast%20local%20and%20global%20nodes&f=false
### [Reference](https://www.enog.org/wp-content/uploads/presentations/enog-14/20-Anycast-DNS-network-ENOG14.pdf) - https://www.enog.org/wp-content/uploads/presentations/enog-14/20-Anycast-DNS-network-ENOG14.pdf
### [Reference](https://datatracker.ietf.org/doc/html/rfc1546) - https://datatracker.ietf.org/doc/html/rfc1546
### [Reference](https://datatracker.ietf.org/doc/html/rfc2526) - https://datatracker.ietf.org/doc/html/rfc2526
### [Reference](https://datatracker.ietf.org/doc/html/rfc3068) - https://datatracker.ietf.org/doc/html/rfc3068
### [Reference](https://datatracker.ietf.org/doc/html/rfc3258) - https://datatracker.ietf.org/doc/html/rfc3258
### [Reference](https://datatracker.ietf.org/doc/html/rfc4291) - https://datatracker.ietf.org/doc/html/rfc4291
### [Reference](https://datatracker.ietf.org/doc/html/rfc4786) - https://datatracker.ietf.org/doc/html/rfc4786
### [Reference](https://datatracker.ietf.org/doc/html/rfc7526) - https://datatracker.ietf.org/doc/html/rfc7526
### [Reference](https://archive.nanog.org/meetings/nanog37/presentations/matt.levine.pdf) - https://archive.nanog.org/meetings/nanog37/presentations/matt.levine.pdf
### [Reference](https://bill.herrin.us/network/anycasttcp.html) - https://bill.herrin.us/network/anycasttcp.html
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/dc/Broadcast.svg) - https://upload.wikimedia.org/wikipedia/commons/d/dc/Broadcast.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/f/f9/Crystal_Clear_app_linneighborhood.svg) - https://upload.wikimedia.org/wikipedia/commons/f/f9/Crystal_Clear_app_linneighborhood.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/30/Multicast.svg) - https://upload.wikimedia.org/wikipedia/commons/3/30/Multicast.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/7/75/Unicast.svg) - https://upload.wikimedia.org/wikipedia/commons/7/75/Unicast.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/1/18/Anycast-BM.svg) - https://upload.wikimedia.org/wikipedia/en/1/18/Anycast-BM.svg