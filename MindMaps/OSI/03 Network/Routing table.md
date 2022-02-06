# Routing table
## [URL](https://en.wikipedia.org/wiki/Routing_table) - https://en.wikipedia.org/wiki/Routing_table
## Catagories
### Articles with short description
### Internet architecture
### Routing
### Short description is different from Wikidata
### "In computer networking, a routing table, or routing information base (RIB), is a data table stored in a router or a network host that lists the routes to particular network destinations, and in some cases, metrics (distances) associated with those routes. The routing table contains information about the topology of the network immediately around it.  
### The construction of routing tables is the primary goal of routing protocols. Static routes are entries made in a routing table by non-automatic means and which are fixed rather than being the result of routing protocols and associated network topology-discovery procedures.
## Overview  
### A routing table is analogous to a distribution map in package delivery. Whenever a node needs to send data to another node on a network, it must first know where to send it. If the node cannot directly connect to the destination node, it has to send it via other nodes along a route to the destination node. Each node needs to keep track of which way to deliver various packages of data, and for this it uses a routing table. A routing table is a database that keeps track of paths, like a map, and uses these to determine which way to forward traffic. A routing table is a data file in RAM that is used to store route information about directly connected and remote networks. Nodes can also share the contents of their routing table with other nodes. 
### The primary function of a router is to forward a packet toward its destination network, which is the destination IP address of the packet. To do this, a router needs to search the routing information stored in its routing table. The routing table contains network/next hop associations. These associations tell a router that a particular destination can be optimally reached by sending the packet to a specific router that represents the next hop on the way to the final destination. The next hop association can also be the outgoing or exit interface to the final destination. 
### With hop-by-hop routing, each routing table lists, for all reachable destinations, the address of the next device along the path to that destination: the next hop.  Assuming that the routing tables are consistent, the simple algorithm of relaying packets to their destination's next hop thus suffices to deliver data anywhere in a network.  Hop-by-hop is the fundamental characteristic of the IP Internet layer and the OSI Network Layer. 
### When a router interface is configured with an IP address and subnet mask, the interface becomes a host on that attached network. A directly connected network is a network that is directly attached to one of the router interfaces. The network address and subnet mask of the interface, along with the interface type and number, are entered into the routing table as a directly connected network. 
### A remote network is a network that can only be reached by sending the packet to another router. Routing table entries to remote networks may be either dynamic or static. Dynamic routes are routes to remote networks that were learned automatically by the router through a dynamic routing protocol. Static routes are routes that a network administrator manually configured. 
### Routing tables are also a key aspect of certain security operations, such as unicast reverse path forwarding (uRPF). In this technique, which has several variants, the router also looks up, in the routing table, the source address of the packet.  If there exists no route back to the source address, the packet is assumed to be malformed or involved in a network attack and is dropped.
## Difficulties  
### The need to record routes to large numbers of devices using limited storage space represents a major challenge in routing table construction. In the Internet, the currently dominant address aggregation technology is a bitwise prefix matching scheme called Classless Inter-Domain Routing (CIDR). Supernetworks can also be used to help control routing table size.
## Contents  
### The routing table consists of at least three information fields: 

### network identifier: The destination subnet and netmask 
### metric: The routing metric of the path through which the packet is to be sent. The route will go in the direction of the gateway with the lowest metric. 
### next hop: The next hop, or gateway, is the address of the next station to which the packet is to be sent on the way to its final destinationDepending on the application and implementation, it can also contain additional values that refine path selection:  

### quality of service associated with the route. For example, the U flag indicates that an IP route is up. 
### filtering criteria: Access-control lists associated with the route 
### interface: Such as eth0 for the first Ethernet card, eth1 for the second Ethernet card, etc.Shown below is an example of what the table above could look like on a computer connected to the internet via a home router: 

### The columns Network destination and Netmask together describe the Network identifier as mentioned earlier. For example, destination 192.168.0.0 and netmask 255.255.255.0 can be written as 192.168.0.0/24. 
### The Gateway column contains the same information as the Next hop, i.e. it points to the gateway through which the network can be reached. 
### The Interface indicates what locally available interface is responsible for reaching the gateway. In this example, gateway 192.168.0.1 (the internet router) can be reached through the local network card with address 192.168.0.100. 
### Finally, the Metric indicates the associated cost of using the indicated route. This is useful for determining the efficiency of a certain route from two points in a network. In this example, it is more efficient to communicate with the computer itself through the use of address 127.0.0.1 (called \u201clocalhost\u201d) than it would be through 192.168.0.100 (the IP address of the local network card).
## Forwarding table  
### Routing tables are generally not used directly for packet forwarding in modern router architectures; instead, they are used to generate the information for a simpler forwarding table. This forwarding table contains only the routes which are chosen by the routing algorithm as preferred routes for packet forwarding. It is often in a compressed or pre-compiled format that is optimized for hardware storage and lookup. 
### This router architecture separates the control plane function of the routing table from the forwarding plane function of the forwarding table. This separation of control and forwarding provides uninterrupted high-performance forwarding.
## See also  
### Lule\u00e5 algorithm
## References 
## External links  
### IP Routing from the Linux Network Administrators Guide"
## References
### [Reference](http://doi.org/10.17487%2FRFC3704) - http://doi.org/10.17487%2FRFC3704
### [Reference](http://www.faqs.org/docs/linux_network/x-087-2-issues.routing.html) - http://www.faqs.org/docs/linux_network/x-087-2-issues.routing.html
### [Reference](http://tools.ietf.org/html/rfc1812) - http://tools.ietf.org/html/rfc1812
### [Reference](http://www.ietf.org/rfc/rfc3746.txt) - http://www.ietf.org/rfc/rfc3746.txt
### [Reference](https://datatracker.ietf.org/doc/html/rfc3704) - https://datatracker.ietf.org/doc/html/rfc3704
## Images