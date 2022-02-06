# Medium access control
## [URL](https://en.wikipedia.org/wiki/Medium_access_control) - https://en.wikipedia.org/wiki/Medium_access_control
## Catagories
### All articles with failed verification
### Articles with failed verification from January 2022
### Articles with short description
### Channel access methods
### Link protocols
### Media access control
### Short description matches Wikidata
### "In IEEE 802 LAN/MAN standards, the medium access control (MAC, also called media access control) sublayer is the layer that controls the hardware responsible for interaction with the wired, optical or wireless transmission medium. The MAC sublayer and the logical link control (LLC) sublayer together make up the data link layer. Within the data link layer, the LLC provides flow control and multiplexing for the logical link (i.e. EtherType, 802.1Q VLAN tag etc), while the MAC provides flow control and multiplexing for the transmission medium. 
### These two sublayers together correspond to layer 2 of the OSI model. For compatibility reasons, LLC is optional for implementations of IEEE 802.3 (the frames are then \"raw\"), but compulsory for implementations of other IEEE 802 physical layer standards. Within the hierarchy of the OSI model and IEEE 802 standards, the MAC sublayer provides a control abstraction of the physical layer such that the complexities of physical link control are invisible to the LLC and upper layers of the network stack. Thus any LLC sublayer (and higher layers) may be used with any MAC. In turn, the medium access control block is formally connected to the PHY via a media-independent interface. Although the MAC block is today typically integrated with the PHY within the same device package, historically any MAC could be used with any PHY, independent of the transmission medium. 
### When sending data to another device on the network, the MAC sublayer encapsulates higher-level frames into frames appropriate for the transmission medium (i.e. the MAC adds a syncword preamble and also padding if necessary), adds a frame check sequence to identify transmission errors, and then forwards the data to the physical layer as soon as the appropriate channel access method permits it. For topologies with a collision domain (bus, ring, mesh, point-to-multipoint topologies), controlling when data is sent and when to wait is necessary to avoid collisions. Additionally, the MAC is also responsible for compensating for collisions by initiating retransmission if a jam signal is detected. When receiving data from the physical layer, the MAC block ensures data integrity by verifying the sender's frame check sequences, and strips off the sender's preamble and padding before passing the data up to the higher layers.
## Functions performed in the MAC sublayer  
### According to IEEE Std 802-2001 section 6.2.3 \"MAC sublayer\", the primary functions performed by the MAC layer are: 
### Frame delimiting and recognition 
### Addressing of destination stations (both as individual stations and as groups of stations) 
### Conveyance of source-station addressing information 
### Transparent data transfer of LLC PDUs, or of equivalent information in the Ethernet sublayer 
### Protection against errors, generally by means of generating and checking frame check sequences 
### Control of access to the physical transmission mediumIn the case of Ethernet, the functions required of a MAC are: 
### receive/transmit normal frames 
### half-duplex retransmission and backoff functions 
### append/check FCS (frame check sequence) 
### interframe gap enforcement 
### discard malformed frames 
### prepend(tx)/remove(rx) preamble, SFD (start frame delimiter), and padding 
### half-duplex compatibility: append(tx)/remove(rx) MAC address
## Addressing mechanism  
### The local network addresses used in IEEE 802 networks and FDDI networks are called media access control addresses; they are based on the addressing scheme that was used in early Ethernet implementations. A MAC address is intended as a unique serial number. MAC addresses are typically assigned to network interface hardware at the time of manufacture. The most significant part of the address identifies the manufacturer, who assigns the remainder of the address, thus provide a potentially unique address. This makes it possible for frames to be delivered on a network link that interconnects hosts by some combination of repeaters, hubs, bridges and switches, but not by network layer  routers. Thus, for example, when an IP packet reaches its destination (sub)network, the destination IP address (a layer 3 or network layer concept) is resolved with the Address Resolution Protocol for IPv4, or by Neighbor Discovery Protocol (IPv6) into the MAC address (a layer 2 concept) of the destination host. 
### Examples of physical networks are Ethernet networks and Wi-Fi networks, both of which are IEEE 802 networks and use IEEE 802 48-bit MAC addresses. 
### A MAC layer is not required in full-duplex point-to-point communication, but address fields are included in some point-to-point protocols for compatibility reasons.
## Channel access control mechanism  
### The channel access control mechanisms provided by the MAC layer are also known as a multiple access method. This makes it possible for several stations connected to the same physical medium to share it. Examples of shared physical media are bus networks, ring networks, hub networks, wireless networks and half-duplex point-to-point links. The multiple access method may detect or avoid data packet collisions if a packet mode contention based channel access method is used, or reserve resources to establish a logical channel if a circuit-switched or channelization-based channel access method is used. The channel access control mechanism relies on a physical layer multiplex scheme. 
### The most widespread multiple access method is the contention-based CSMA/CD used in Ethernet networks. This mechanism is only utilized within a network collision domain, for example an Ethernet bus network or a hub-based star topology network. An Ethernet network may be divided into several collision domains, interconnected by bridges and switches. 
### A multiple access method is not required in a switched full-duplex network, such as today's switched Ethernet networks, but is often available in the equipment for compatibility reasons.
## Channel access control mechanism for concurrent transmission  
### Use of directional antennas and millimeter-wave communication in a wireless personal area network increases the probability of concurrent scheduling of non\u2010interfering transmissions in a localized area, which results in an immense increase in network throughput. However, the optimum scheduling of concurrent transmission is an NP-hard problem.
## Cellular networks  
### Cellular networks, such as GSM, UMTS or LTE networks, also use a MAC layer. The MAC protocol in cellular networks is designed to maximize the utilization of the expensive licensed spectrum. The air interface of a cellular network is at layers 1 and 2 of the OSI model; at layer 2, it is divided into multiple protocol layers. In UMTS and LTE, those protocols are the Packet Data Convergence Protocol (PDCP), the Radio Link Control (RLC) protocol, and the MAC protocol. The base station has absolute control over the air interface and schedules the downlink access as well as the uplink access of all devices. The MAC protocol is specified by 3GPP in TS 25.321 for UMTS, TS 36.321 for LTE and TS 38.321 for 5G.
## See also  
### List of channel access methods 
### Isochronous media access controller 
### MAC-Forced Forwarding 
### MACsec (IEEE 802.1AE)
## References "
## References
### [Reference](http://www.3gpp.org/ftp/Specs/html-info/25321.htm) - http://www.3gpp.org/ftp/Specs/html-info/25321.htm
### [Reference](http://www.3gpp.org/ftp/Specs/html-info/36321.htm) - http://www.3gpp.org/ftp/Specs/html-info/36321.htm
### [Reference](http://www.3gpp.org/ftp/Specs/html-info/38321.htm) - http://www.3gpp.org/ftp/Specs/html-info/38321.htm
### [Reference](http://arxiv.org/abs/1801.06018) - http://arxiv.org/abs/1801.06018
### [Reference](http://doi.org/10.4218%2Fetrij.14.0113.0703) - http://doi.org/10.4218%2Fetrij.14.0113.0703
### [Reference](http://standards.ieee.org/getieee802/download/802-2001.pdf) - http://standards.ieee.org/getieee802/download/802-2001.pdf
### [Reference](https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://www.itu.int/rec/T-REC-X.225-199511-I/en
### [Reference](https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en
### [Reference](https://standards.ieee.org/standard/802_3-2002.html) - https://standards.ieee.org/standard/802_3-2002.html
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/6/6f/Multiplexing_diagram.svg) - https://upload.wikimedia.org/wikipedia/commons/6/6f/Multiplexing_diagram.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/archive/6/6f/20130817141959%21Multiplexing_diagram.svg) - https://upload.wikimedia.org/wikipedia/commons/archive/6/6f/20130817141959%21Multiplexing_diagram.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/archive/6/6f/20130817135756%21Multiplexing_diagram.svg) - https://upload.wikimedia.org/wikipedia/commons/archive/6/6f/20130817135756%21Multiplexing_diagram.svg