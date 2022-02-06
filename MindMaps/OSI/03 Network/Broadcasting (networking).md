# Broadcasting (networking)
## [URL](https://en.wikipedia.org/wiki/Broadcasting_(networking)) - https://en.wikipedia.org/wiki/Broadcasting_(networking)
## Catagories
### Articles with short description
### Inter-process communication
### Network topology
### Packets (information technology)
### Short description is different from Wikidata
### Telecommunication services
### "In computer networking, telecommunication and information theory, broadcasting is a method of transferring a message to all recipients simultaneously.  Broadcasting can be performed as a high-level operation in a program, for example, broadcasting in Message Passing Interface, or it may be a low-level networking operation, for example broadcasting on Ethernet. 
### All-to-all communication is a computer communication method in which each sender transmits messages to all receivers within a group. In networking this can be accomplished using broadcast or multicast. This is in contrast with the point-to-point method in which each sender communicates with one receiver.
## Addressing methods  
### There are four principal addressing methods in the Internet Protocol: 

### Unicast delivers a message to a single specific node using a one-to-one association between a sender and destination: each destination address uniquely identifies a single receiver endpoint. 
### Broadcast delivers a message to all nodes in the network using a one-to-all association; a single datagram (or packet) from one sender is routed to all of the possibly multiple endpoints associated with the broadcast address. The network automatically replicates datagrams as needed to reach all the recipients within the scope of the broadcast, which is generally an entire network subnet. 
### Multicast delivers a message to a group of nodes that have expressed interest in receiving the message using a one-to-many-of-many or many-to-many-of-many association; datagrams are routed simultaneously in a single transmission to many recipients. Multicast differs from broadcast in that the destination address designates a subset, not necessarily all, of the accessible nodes. 
### Anycast delivers a message to any one out of a group of nodes, typically the one nearest to the source using a one-to-one-of-many association where datagrams are routed to any single member of a group of potential receivers that are all identified by the same destination address.  The routing algorithm selects the single receiver from the group based on which is the nearest according to some distance or cost measure.
## Overview  
### In computer networking, broadcasting refers to transmitting a packet that will be received by every device on the network. In practice, the scope of the broadcast is limited to a broadcast domain. 
### Broadcasting is the most general communication method, and is also the most intensive, in the sense that many messages may be required and many network devices are involved. This is in contrast to unicast addressing in which a host sends datagrams to another single host, identified by a unique address. 
### Broadcasting may be performed as all scatter in which each sender performs its own scatter in which the messages are distinct for each receiver, or all broadcast in which they are the same.The MPI message passing method which is the de facto standard on large computer clusters includes the MPI_Alltoall method.Not all network technologies support broadcast addressing; for example, neither X.25 nor frame relay have broadcast capability. The Internet Protocol Version 4 (IPv4), which is the primary networking protocol in use today on the Internet and all networks connected to it, supports broadcast, but the broadcast domain is the broadcasting host's subnet, which is typically small; there is no way to do an Internet-wide broadcast. Broadcasting is largely confined to local area network (LAN) technologies, most notably Ethernet and Token Ring, where the performance impact of broadcasting is not as large as it would be in a wide area network. 
### The successor to IPv4, IPv6 does not implement the broadcast method, so as to prevent disturbing all nodes in a network when only a few may be interested in a particular service. Instead IPv6 relies on multicast addressing - a conceptually similar one-to-many routing methodology. However, multicasting limits the pool of receivers to those that join a specific multicast receiver group. 
### Both Ethernet and IPv4 use an all-ones broadcast address to indicate a broadcast packet. Token Ring uses a special value in the IEEE 802.2 control field. 
### Broadcasting may be abused to perform a type of DoS-attack known as a Smurf attack. The attacker sends forged ping requests with the source IP-address of the victim computer. The victim computer is flooded by the replies from all computers in the domain.
## See also  
### Broadcast radiation 
### Point-to-multipoint communication 
### Broadcast, Unknown-Unicast and Multicast traffic 
### Terminating Reliable Broadcast
## References 
## External links  
### \"Network Broadcasting and Multicast\". Archived from the original on 2007-10-11."
## References
### [Reference](http://www.comptechdoc.org/independent/networking/guide/netbroadcasting.html) - http://www.comptechdoc.org/independent/networking/guide/netbroadcasting.html
### [Reference](https://archive.org/details/computernetworks00tane_2/page/368) - https://archive.org/details/computernetworks00tane_2/page/368
### [Reference](https://web.archive.org/web/20071011130826/http://www.comptechdoc.org/independent/networking/guide/netbroadcasting.html) - https://web.archive.org/web/20071011130826/http://www.comptechdoc.org/independent/networking/guide/netbroadcasting.html
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/dc/Broadcast.svg) - https://upload.wikimedia.org/wikipedia/commons/d/dc/Broadcast.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/30/Multicast.svg) - https://upload.wikimedia.org/wikipedia/commons/3/30/Multicast.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/7/75/Unicast.svg) - https://upload.wikimedia.org/wikipedia/commons/7/75/Unicast.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/1/18/Anycast-BM.svg) - https://upload.wikimedia.org/wikipedia/en/1/18/Anycast-BM.svg