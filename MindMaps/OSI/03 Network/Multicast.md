# Multicast
## [URL](https://en.wikipedia.org/wiki/Multicast) - https://en.wikipedia.org/wiki/Multicast
## Catagories
### All articles to be expanded
### Articles prone to spam from April 2015
### Articles to be expanded from March 2020
### Articles using small message boxes
### Articles with LCCN identifiers
### Articles with short description
### Internet architecture
### Internet broadcasting
### Short description is different from Wikidata
### Television terminology
### "In computer networking, multicast is group communication where data transmission is addressed to a group of destination computers simultaneously. Multicast can be one-to-many or many-to-many distribution. Multicast should not be confused with physical layer point-to-multipoint communication. 
### Group communication may either be application layer multicast or network assisted multicast, where the latter makes it possible for the source to efficiently send to the group in a single transmission. Copies are automatically created in other network elements, such as routers, switches and cellular network base stations, but only to network segments that currently contain members of the group. Network assisted multicast may be implemented at the data link layer using one-to-many addressing and switching such as Ethernet multicast addressing, Asynchronous Transfer Mode (ATM), point-to-multipoint virtual circuits (P2MP) or InfiniBand multicast. Network assisted multicast may also be implemented at the Internet layer using IP multicast. In IP multicast the implementation of the multicast concept occurs at the IP routing level, where routers create optimal distribution paths for datagrams sent to a multicast destination address. 
### Multicast is often employed in Internet Protocol (IP) applications of streaming media, such as IPTV and multipoint videoconferencing.
## Ethernet  
### Ethernet frames with a value of 1 in the least-significant bit of the first octet of the destination address are treated as multicast frames and are flooded to all points on the network. This mechanism constitutes multicast at the data link layer. This mechanism is used by IP multicast to achieve one-to-many transmission for IP on Ethernet networks. Modern Ethernet controllers filter received packets to reduce CPU load, by looking up the hash of a multicast destination address in a table, initialized by software, which controls whether a multicast packet is dropped or fully received. 
### Ethernet multicast is available on all Ethernet networks. Multicasts span the broadcast domain of the network. Multiple Registration Protocol can be used to control Ethernet multicast delivery.
## IP  

### IP multicast is a technique for one-to-many communication over an IP network. The destination nodes send Internet Group Management Protocol join and leave messages, for example in the case of IPTV when the user changes from one TV channel to another. IP multicast scales to a larger receiver population by not requiring prior knowledge of who or how many receivers there are. Multicast uses network infrastructure efficiently by requiring the source to send a packet only once, even if it needs to be delivered to a large number of receivers. The nodes in the network take care of replicating the packet to reach multiple receivers only when necessary. 
### The most common transport layer protocol to use multicast addressing is User Datagram Protocol (UDP). By its nature, UDP is not reliable\u2014messages may be lost or delivered out of order. By adding loss detection and retransmission mechanisms, reliable multicast has been implemented on top of UDP or IP by various middleware products, e.g. those that implement the Real-Time Publish-Subscribe (RTPS) Protocol of the Object Management Group (OMG) Data Distribution Service (DDS) standard, as well as by special transport protocols such as Pragmatic General Multicast (PGM). 
### IP multicast is always available within the local subnet. Achieving IP multicast service over a wider area requires multicast routing. Many networks, including the Internet, do not support multicast routing. Multicast routing functionality is available in enterprise-grade network equipment but is typically not available until configured by a network administrator. The Internet Group Management Protocol is used to control IP multicast delivery.
## Application layer  
### Application layer multicast overlay services are not based on IP multicast or data link layer multicast. Instead they use multiple unicast transmissions to simulate a multicast. These services are designed for application-level group communication. Internet Relay Chat (IRC) implements a single spanning tree across its overlay network for all conference groups. The lesser-known PSYC technology uses custom multicast strategies per conference. Some peer-to-peer technologies employ the multicast concept known as peercasting when distributing content to multiple recipients. 
### Explicit multi-unicast (Xcast) is another multicast strategy that includes addresses of all intended destinations within each packet. As such, given maximum transmission unit limitations, Xcast cannot be used for multicast groups with many destinations. The Xcast model generally assumes that stations participating in the communication are known ahead of time, so that distribution trees can be generated and resources allocated by network elements in advance of actual data traffic.
## Wireless networks  
### Wireless communications (with exception to point-to-point radio links using directional antennas) are inherently broadcasting media.  However, the communication service provided may be unicast, multicast as well as broadcast, depending on if the data is addressed to one, to a group or to all receivers in the covered network, respectively.
## Television  
### In digital television, the concept of multicast service sometimes is used to refer to content protection by broadcast encryption, i.e. encrypted pay television content over a simplex broadcast channel only addressed to paying viewers. In this case, data is broadcast to all receivers but only addressed to a specific group. 
### The concept of interactive multicast, for example using IP multicast, may be used over TV broadcast networks to improve efficiency, offer more TV programs, or reduce the required spectrum. Interactive multicast implies that TV programs are sent only over transmitters where there are viewers and that only the most popular programs are transmitted. It relies on an additional interaction channel (a back-channel or return channel), where user equipment may send join and leave messages when the user changes TV channel. Interactive multicast has been suggested as an efficient transmission scheme in DVB-H and DVB-T2 terrestrial digital television systems, A similar concept is switched broadcast over cable-TV networks, where only the currently most popular content is delivered in the cable-TV network. Scalable video multicast in an application of interactive multicast, where a subset of the viewers receive additional data for high-resolution video. 
### TV gateways converts satellite (DVB-S, DVB-S2), cable (DVB-C, DVB-C2) and terrestrial television (DVB-T, DVB-T2) to IP for distribution using unicast and multicast in home, hospitality and enterprise applications 
### Another similar concept is Cell-TV, and implies TV distribution over 3G cellular networks using the network-assisted multicasting offered by the Multimedia Broadcast Multicast Service (MBMS) service, or over 4G/LTE cellular networks with the eMBMS (enhanced MBMS) service.
## See also 
## References "
## Links
### Any-source multicast
### Anycast
### Application layer
### Asynchronous Transfer Mode
### Base station subsystem
### Broadcast, unknown-unicast and multicast traffic
### Broadcast domain
### Broadcast encryption
### Broadcasting (networking)
### Cable television
### Cell-TV
### Computer networking
### Content delivery network
### DVB-C
### DVB-C2
### DVB-CPCM
### DVB-H
### DVB-S
### DVB-S2
### DVB-T
### DVB-T2
### Data Distribution Service
### Data link layer
### Data transmission
### Datagram
### Digital television
### Digital terrestrial television
### Directional antenna
### Ethernet frame
### Flooding algorithm
### IPTV
### IP multicast
### InfiniBand
### Interactive television
### Internet Group Management Protocol
### Internet Protocol
### Internet Relay Chat
### Internet layer
### LTE (telecommunication)
### MAC address
### Many-to-many
### Maximum transmission unit
### Mbone
### Middleware
### Multicast
### Multicast address
### Multicast channel
### Multicast lightpaths
### Multicast routing
### Multimedia Broadcast Multicast Service
### Multiple Registration Protocol
### Narada multicast protocol
### Network switch
### Non-broadcast multiple-access network
### Object Management Group
### Overlay network
### Pay television
### Peer-to-peer
### Peercasting
### Point-to-multipoint communication
### Point-to-point radio link
### Pragmatic General Multicast
### Push technology
### RFC (identifier)
### Real-Time Publish-Subscribe (RTPS) Protocol
### Reliability (computer networking)
### Reliable multicast
### Return channel
### Router (computing)
### Routing
### Satellite television
### Scalable video multicast
### Source-specific multicast
### Spanning tree
### Streaming media
### TV gateway
### Transport layer
### Unicast
### User Datagram Protocol
### Videoconferencing
### Xcast
## References
### [Reference](http://www.psyc.eu/whitepaper/) - http://www.psyc.eu/whitepaper/
### [Reference](http://tools.ietf.org/html/rfc1324) - http://tools.ietf.org/html/rfc1324
### [Reference](http://tools.ietf.org/html/rfc5058) - http://tools.ietf.org/html/rfc5058
### [Reference](http://apachepersonal.miun.se/~mageri/myresearch/bmsb2013-Eriksson.pdf) - http://apachepersonal.miun.se/~mageri/myresearch/bmsb2013-Eriksson.pdf
### [Reference](https://books.google.com/books?id=EUUqAAAACAAJ&dq=multicast+%22one+to+many%22+television&hl=sv&sa=X&ei=bYNyU_q-FofyyAPKu4GYAQ&redir_esc=y) - https://books.google.com/books?id=EUUqAAAACAAJ&dq=multicast+%22one+to+many%22+television&hl=sv&sa=X&ei=bYNyU_q-FofyyAPKu4GYAQ&redir_esc=y
### [Reference](https://books.google.com/books?id=I4excGQVTVkC&pg=PA302&dq=multicast+%22one+to+many%22+%22group+communication%22+-IP_multicast&hl=sv&sa=X&ei=iIRyU7rEJemdyQPktICQCA&ved=0CDIQ6AEwAA#v=onepage&q=multicast%20%22one%20to%20many%22%20%22group%20communication%22%20-IP_multicast&f=false) - https://books.google.com/books?id=I4excGQVTVkC&pg=PA302&dq=multicast+%22one+to+many%22+%22group+communication%22+-IP_multicast&hl=sv&sa=X&ei=iIRyU7rEJemdyQPktICQCA&ved=0CDIQ6AEwAA#v=onepage&q=multicast%20%22one%20to%20many%22%20%22group%20communication%22%20-IP_multicast&f=false
### [Reference](https://id.loc.gov/authorities/subjects/sh97007256) - https://id.loc.gov/authorities/subjects/sh97007256
### [Reference](https://www.researchgate.net/publication/316921061) - https://www.researchgate.net/publication/316921061
### [Reference](https://www.wikidata.org/wiki/Q899288#identifiers) - https://www.wikidata.org/wiki/Q899288#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/dc/Broadcast.svg) - https://upload.wikimedia.org/wikipedia/commons/d/dc/Broadcast.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/30/Multicast.svg) - https://upload.wikimedia.org/wikipedia/commons/3/30/Multicast.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/8/81/Multicast_Protocols-en.svg) - https://upload.wikimedia.org/wikipedia/commons/8/81/Multicast_Protocols-en.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/7/75/Unicast.svg) - https://upload.wikimedia.org/wikipedia/commons/7/75/Unicast.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/1/1c/Wiki_letter_w_cropped.svg) - https://upload.wikimedia.org/wikipedia/commons/1/1c/Wiki_letter_w_cropped.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg) - https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/1/18/Anycast-BM.svg) - https://upload.wikimedia.org/wikipedia/en/1/18/Anycast-BM.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg