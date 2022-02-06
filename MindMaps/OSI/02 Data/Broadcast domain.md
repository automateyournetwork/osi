# Broadcast domain
## [URL](https://en.wikipedia.org/wiki/Broadcast_domain) - https://en.wikipedia.org/wiki/Broadcast_domain
## Catagories
### All Wikipedia articles written in American English
### All articles lacking sources
### Articles lacking sources from January 2022
### Articles with short description
### Network architecture
### Short description matches Wikidata
### Use American English from March 2019
### "A broadcast domain is a logical division of a computer network, in which all nodes can reach each other by broadcast at the data link layer. A broadcast domain can be within the same LAN segment or it can be bridged to other LAN segments. 
### In terms of current popular technologies, any computer connected to the same Ethernet repeater or switch is a member of the same broadcast domain. Further, any computer connected to the same set of inter-connected switches/repeaters is a member of the same broadcast domain. Routers and other higher-layer devices form boundaries between broadcast domains. 
### The notion of broadcast domain should be contrasted with that of collision domain, which would be all nodes on the same set of inter-connected repeaters, divided by switches and learning bridges. Collision domains are generally smaller than, and contained within, broadcast domains. 
### While some layer two network devices are able to divide the collision domains, broadcast domains are only divided by layer 3 network devices such as routers or layer 3 switches. Separating VLANs divides broadcast domains as well.
## Further explanation  
### The distinction between broadcast and collision domains comes about because simple Ethernet and similar systems use a shared transmission system. In simple Ethernet (without switches or bridges), data frames are transmitted to all other nodes on a network. Each receiving node checks the destination address of each frame, and simply ignores any frame not addressed to its own MAC address or the broadcast address. 
### Switches act as buffers, receiving and analyzing the frames from each connected network segment. Frames destined for nodes connected to the originating segment are not forwarded by the switch. Frames destined for a specific node on a different segment are sent only to that segment. Only broadcast frames are forwarded to all other segments. This reduces unnecessary traffic and collisions. 
### In such a switched network, transmitted frames may not be received by all other reachable nodes. Nominally, only broadcast frames will be received by all other nodes. Collisions are localized to the physical-layer network segment they occur on. Thus, the broadcast domain is the entire inter-connected layer two network, and the segments connected to each switch/bridge port are each a collision domain. To clarify; repeaters do not divide collision domains but switches do. This means that since switches have become commonplace, collision domains are isolated to the specific half-duplex segment between the switch port and the connected node. Full-duplex segments, or links, don't form a collision domain as there is a dedicated channel between each transmitter and receiver, making collisions a thing-of-the-past in modern wired networks. 
### In a switched network, enabling promiscuous mode for packet capturing results in no extra data being collected, as a NIC with promiscuous mode enabled simply neglects to drop Ethernet frames with a destination field populated with a MAC from another device. Such frames would not be forwarded by the switch to any ports on which that MAC is not communicating and with which it is associated in the MAC address table. 
### Not all network systems or media feature broadcast/collision domains. For example, PPP links.
## Broadcast domain control  
### With a sufficiently sophisticated switch, it is possible to create a network in which the normal notion of a broadcast domain is strictly controlled. One implementation of this concept is termed a \"private VLAN\". Another implementation is possible with Linux and iptables. One helpful analogy is that by creating multiple VLANs, the number of broadcast domains increases, but the size of each broadcast domain decreases. This is because a virtual LAN (or VLAN) is technically a broadcast domain. 
### This is achieved by designating one or more \"server\" or \"provider\" nodes, either by MAC address or switch port. Broadcast frames are allowed to originate from these sources, and are sent to all other nodes. Broadcast frames from all other sources are directed only to the server/provider nodes. Traffic from other sources not destined to the server/provider nodes (\"peer-to-peer\" traffic) is blocked. 
### The result is a network based on a nominally shared transmission system; like Ethernet, but in which \"client\" nodes cannot communicate with each other, only with the server/provider. A common application is Internet providers. Allowing direct data link layer communication between customer nodes exposes the network to various security attacks, such as ARP spoofing. Controlling the broadcast domain in this fashion provides many of the advantages of a point-to-point network, using commodity broadcast-based hardware.
## See also  
### Network layer 
### Collision domain
## References  
### Collision & broadcast domain, Study CCNA 
### Collision Domains vs. Broadcast Domains, ciscoskills.net 
### Broadcast Domain Explained"
## References
### [Reference](http://scholar.google.com/scholar?q=%22Broadcast+domain%22) - http://scholar.google.com/scholar?q=%22Broadcast+domain%22
### [Reference](http://www.google.com/search?&q=%22Broadcast+domain%22&tbs=bkt:s&tbm=bks) - http://www.google.com/search?&q=%22Broadcast+domain%22&tbs=bkt:s&tbm=bks
### [Reference](http://www.google.com/search?as_eq=wikipedia&q=%22Broadcast+domain%22) - http://www.google.com/search?as_eq=wikipedia&q=%22Broadcast+domain%22
### [Reference](http://www.google.com/search?tbm=nws&q=%22Broadcast+domain%22+-wikipedia&tbs=ar:1) - http://www.google.com/search?tbm=nws&q=%22Broadcast+domain%22+-wikipedia&tbs=ar:1
### [Reference](http://www.google.com/search?tbs=bks:1&q=%22Broadcast+domain%22+-wikipedia) - http://www.google.com/search?tbs=bks:1&q=%22Broadcast+domain%22+-wikipedia
### [Reference](http://study-ccna.com/collision-broadcast-domain) - http://study-ccna.com/collision-broadcast-domain
### [Reference](http://ciscoskills.net/2011/03/30/collision-domains-vs-broadcast-domains/) - http://ciscoskills.net/2011/03/30/collision-domains-vs-broadcast-domains/
### [Reference](https://www.youtube.com/watch?v=HqAYJZQPP2Y) - https://www.youtube.com/watch?v=HqAYJZQPP2Y
### [Reference](https://www.jstor.org/action/doBasicSearch?Query=%22Broadcast+domain%22&acc=on&wc=on) - https://www.jstor.org/action/doBasicSearch?Query=%22Broadcast+domain%22&acc=on&wc=on
## Images
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20210726203439%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20210726203439%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20201004174738%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20201004174738%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171208221057%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171208221057%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171207131032%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171207131032%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20160612140736%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20160612140736%21Question_book-new.svg