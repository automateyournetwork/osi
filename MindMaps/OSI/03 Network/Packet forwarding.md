# Packet forwarding
## [URL](https://en.wikipedia.org/wiki/Packet_forwarding) - https://en.wikipedia.org/wiki/Packet_forwarding
## Catagories
### All articles needing additional references
### Articles needing additional references from July 2009
### Articles with short description
### Routing
### Short description is different from Wikidata
### "Packet forwarding is the relaying of packets from one network segment to another by nodes in a computer network. The network layer in the OSI model is responsible for packet forwarding.
## Models  
  
### The simplest forwarding model\u200d\u2014\u200cunicasting\u200d\u2014\u200cinvolves a packet being relayed from link to link along a chain leading from the packet's source to its destination. However, other forwarding strategies are commonly used. Broadcasting requires a packet to be duplicated and copies sent on multiple links with the goal of delivering a copy to every device on the network. In practice, broadcast packets are not forwarded everywhere on a network, but only to devices within a broadcast domain, making broadcast a relative term. Less common than broadcasting, but perhaps of greater utility and theoretical significance, is multicasting, where a packet is selectively duplicated and copies delivered to each of a set of recipients. 
### Networking technologies tend to naturally support certain forwarding models. For example, fiber optics and copper cables run directly from one machine to another to form a natural unicast media \u2013 data transmitted at one end is received by only one machine at the other end. However, as illustrated in the diagrams, nodes can forward packets to create multicast or broadcast distributions from naturally unicast media. Likewise, traditional Ethernet (10BASE5 and 10BASE2, but not the more modern 10BASE-T) are natural broadcast media \u2013 all the nodes are attached to a single long cable and a packet transmitted by one device is seen by every other device attached to the cable. Ethernet nodes implement unicast by ignoring packets not directly addressed to them. A wireless network is naturally multicast \u2013  all devices within a reception radius of a transmitter can receive its packets. Wireless nodes ignore packets addressed to other devices, but require forwarding to reach nodes outside their reception radius.
## Decisions  
### At nodes where multiple outgoing links are available, the choice of which, all, or any to use for forwarding a given packet requires a decision making process that, while simple in concept, is sometimes bewilderingly complex. Since a forwarding decision must be made for every packet handled by a node, the total time required for this can become a major limiting factor in overall network performance. Much of the design effort of high-speed routers and switches has been focused on making rapid forwarding decisions for large numbers of packets. 
### The forwarding decision is generally made using one of two processes: routing, which uses information encoded in a device's address to infer its location on the network, or bridging, which makes no assumptions about where addresses are located and depends heavily on broadcasting to locate unknown addresses. The heavy overhead of broadcasting has led to the dominance of routing in large networks, particularly the Internet; bridging is largely relegated to small networks where the overhead of broadcasting is tolerable. However, since large networks are usually composed of many smaller networks linked together, it would be inaccurate to state that bridging has no use on the Internet; rather, its use is localized.
## Methods  
### A node can use one of two different methods to forward packets: store-and-forward or cut-through switching.
## See also  
### Equal-cost multi-path routing 
### Forwarding information base 
### Node-to-node data transfer 
### Per-hop behaviour 
### Port forwarding
## References "
## Links
### 10BASE-T
### 10BASE2
### 10BASE5
### Bridging (networking)
### Broadcast domain
### Broadcasting (networks)
### Computer network
### Cut-through switching
### Equal-cost multi-path routing
### Ethernet
### Forwarding information base
### Internet
### Multicast
### Network layer
### Network segment
### Network switch
### Node-to-node data transfer
### Node (networking)
### OSI model
### Packet (information technology)
### Per-hop behaviour
### Port forwarding
### Protocol Independent Multicast
### Router (computing)
### Routing
### Store-and-forward
### Unicast
### Wireless network
## References
### [Reference](http://scholar.google.com/scholar?q=%22Packet+forwarding%22) - http://scholar.google.com/scholar?q=%22Packet+forwarding%22
### [Reference](http://www.google.com/search?&q=%22Packet+forwarding%22&tbs=bkt:s&tbm=bks) - http://www.google.com/search?&q=%22Packet+forwarding%22&tbs=bkt:s&tbm=bks
### [Reference](http://www.google.com/search?as_eq=wikipedia&q=%22Packet+forwarding%22) - http://www.google.com/search?as_eq=wikipedia&q=%22Packet+forwarding%22
### [Reference](http://www.google.com/search?tbm=nws&q=%22Packet+forwarding%22+-wikipedia&tbs=ar:1) - http://www.google.com/search?tbm=nws&q=%22Packet+forwarding%22+-wikipedia&tbs=ar:1
### [Reference](http://www.google.com/search?tbs=bks:1&q=%22Packet+forwarding%22+-wikipedia) - http://www.google.com/search?tbs=bks:1&q=%22Packet+forwarding%22+-wikipedia
### [Reference](http://inspirehep.net/record/887357/files/cer-002474543.pdf) - http://inspirehep.net/record/887357/files/cer-002474543.pdf
### [Reference](https://www.jstor.org/action/doBasicSearch?Query=%22Packet+forwarding%22&acc=on&wc=on) - https://www.jstor.org/action/doBasicSearch?Query=%22Packet+forwarding%22&acc=on&wc=on
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/4/46/Broadcast_forwarding.png) - https://upload.wikimedia.org/wikipedia/commons/4/46/Broadcast_forwarding.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/7/7b/Multicast_forwarding.png) - https://upload.wikimedia.org/wikipedia/commons/7/7b/Multicast_forwarding.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/5/5f/Unicast_forwarding.png) - https://upload.wikimedia.org/wikipedia/commons/5/5f/Unicast_forwarding.png
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg