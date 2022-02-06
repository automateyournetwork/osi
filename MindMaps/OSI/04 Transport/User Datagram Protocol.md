# User Datagram Protocol
## [URL](https://en.wikipedia.org/wiki/User_Datagram_Protocol) - https://en.wikipedia.org/wiki/User_Datagram_Protocol
## Catagories
### 1980 introductions
### All articles with failed verification
### Articles with GND identifiers
### Articles with failed verification from January 2022
### Articles with short description
### Internet Standards
### Internet protocols
### Short description matches Wikidata
### Transport layer protocols
### Use dmy dates from August 2021
### "In computer networking, the User Datagram Protocol (UDP) is one of the core members of the Internet protocol suite. With UDP, computer applications can send messages, in this case referred to as datagrams, to other hosts on an Internet Protocol (IP) network. Prior communications are not required in order to set up communication channels or data paths. 
### UDP uses a simple connectionless communication model with a minimum of protocol mechanisms. UDP provides checksums for data integrity, and port numbers for addressing different functions at the source and destination of the datagram. It has no handshaking dialogues, and thus exposes the user's program to any unreliability of the underlying network; there is no guarantee of delivery, ordering, or duplicate protection. If error-correction facilities are needed at the network interface level, an application may instead use Transmission Control Protocol (TCP) or Stream Control Transmission Protocol (SCTP) which are designed for this purpose. 
### UDP is suitable for purposes where error checking and correction are either not necessary or are performed in the application; UDP avoids the overhead of such processing in the protocol stack. Time-sensitive applications often use UDP because dropping packets is preferable to waiting for packets delayed due to retransmission, which may not be an option in a real-time system.The protocol was designed by David P. Reed in 1980 and formally defined in RFC 768.
## Attributes  
### UDP is a simple message-oriented transport layer protocol that is documented in RFC 768. Although UDP provides integrity verification (via checksum) of the header and payload, it provides no guarantees to the upper layer protocol for message delivery and the UDP layer retains no state of UDP messages once sent. For this reason, UDP sometimes is referred to as Unreliable Datagram Protocol. If transmission reliability is desired, it must be implemented in the user's application. 
### A number of UDP's attributes make it especially suited for certain applications. 

### It is transaction-oriented, suitable for simple query-response protocols such as the Domain Name System or the Network Time Protocol. 
### It provides datagrams, suitable for modeling other protocols such as IP tunneling or remote procedure call and the Network File System. 
### It is simple, suitable for bootstrapping or other purposes without a full protocol stack, such as the DHCP and Trivial File Transfer Protocol. 
### It is stateless, suitable for very large numbers of clients, such as in streaming media applications such as IPTV. 
### The lack of retransmission delays makes it suitable for real-time applications such as Voice over IP, online games, and many protocols using Real Time Streaming Protocol. 
### Because it supports multicast, it is suitable for broadcast information such as in many kinds of service discovery and shared information such as Precision Time Protocol and Routing Information Protocol.
## Ports  
### Applications can use datagram sockets to establish host-to-host communications. An application binds a socket to its endpoint of data transmission, which is a combination of an IP address and a port. In this way, UDP provides application multiplexing. A port is a software structure that is identified by the port number, a 16-bit integer value, allowing for port numbers between 0 and 65535. Port 0 is reserved but is a permissible source port value if the sending process does not expect messages in response. 
### The Internet Assigned Numbers Authority (IANA) has divided port numbers into three ranges. Port numbers 0 through 1023 are used for common, well-known services. On Unix-like operating systems, using one of these ports requires superuser operating permission. Port numbers 1024 through 49151 are the registered ports used for IANA-registered services. Ports 49152 through 65535 are dynamic ports that are not officially designated for any specific service, and may be used for any purpose. These may also be used as ephemeral ports, which software running on the host may use to dynamically create communications endpoints as needed.
## UDP datagram structure  
### A UDP datagram consists of a datagram header and a data section. The UDP datagram header consists of 4 fields, each of which is 2 bytes (16 bits). The data section follows the header and is the payload data carried for the application. 
### The use of the checksum and source port fields is optional in IPv4 (pink background in table). In IPv6 only the source port field is optional. 

### Source port number 
### This field identifies the sender's port, when used, and should be assumed to be the port to reply to if needed. If not used, it should be zero. If the source host is the client, the port number is likely to be an ephemeral port number. If the source host is the server, the port number is likely to be a well-known port number. 
### Destination port number 
### This field identifies the receiver's port and is required. Similar to source port number, if the client is the destination host then the port number will likely be an ephemeral port number and if the destination host is the server then the port number will likely be a well-known port number. 
### Length 
### This field specifies the length in bytes of the UDP header and UDP data. The minimum length is 8 bytes, the length of the header. The field size sets a theoretical limit of 65,535 bytes (8-byte header + 65,527 bytes of data) for a UDP datagram. However the actual limit for the data length, which is imposed by the underlying IPv4 protocol, is 65,507 bytes (65,535 bytes \u2212 8-byte UDP header \u2212 20-byte IP header). 
### Using IPv6 jumbograms it is possible to have UDP datagrams of size greater than 65,535 bytes. RFC 2675 specifies that the length field is set to zero if the length of the UDP header plus UDP data is greater than 65,535. 
### Checksum 
### The checksum field may be used for error-checking of the header and data. This field is optional in IPv4, and mandatory in IPv6. The field carries all-zeros if unused.
## Checksum computation  
### The method used to compute the checksum is defined in RFC 768, and efficient calculation is discussed in RFC 1071: 

### Checksum is the 16-bit one's complement of the one's complement sum of a pseudo header of information from the IP header, the UDP header, and the data, padded with zero octets at the end (if necessary) to make a multiple of two octets. 
### In other words, all 16-bit words are summed using one's complement arithmetic. Add the 16-bit values up. On each addition, if a carry-out (17th bit) is produced, swing that 17th carry bit around and add it to the least significant bit of the running total. Finally, the sum is then one's complemented to yield the value of the UDP checksum field. 
### If the checksum calculation results in the value zero (all 16 bits 0) it should be sent as the one's complement (all 1s) as a zero-value checksum indicates no checksum has been calculated. In this case, any specific processing is not required at the receiver, because all 0s and all 1s are equal to zero in 1's complement arithmetic. 
### The differences between IPv4 and IPv6 are in the pseudo header used to compute the checksum, and that the checksum is not optional in IPv6.
## IPv4 pseudo header  
### When UDP runs over IPv4, the checksum is computed using a \"pseudo header\" that contains some of the same information from the real IPv4 header.:\u200a2\u200a  The pseudo header is not the real IPv4 header used to send an IP packet, it is used only for the checksum calculation. 

### The source and destination addresses are those in the IPv4 header. The protocol is that for UDP (see List of IP protocol numbers): 17 (0x11). The UDP length field is the length of the UDP header and data. The field data stands for the transmitted data. 
### UDP checksum computation is optional for IPv4. If a checksum is not used it should be set to the value zero.
## IPv6 pseudo header  
### When UDP runs over IPv6, the checksum is mandatory. The method used to compute it is changed as documented in RFC 2460: 

### Any transport or other upper-layer protocol that includes the addresses from the IP header in its checksum computation must be modified for use over IPv6 to include the 128-bit IPv6 addresses. 
### When computing the checksum, again a pseudo header is used that mimics the real IPv6 header: 

### The source address is the one in the IPv6 header. The destination address is the final destination; if the IPv6 packet does not contain a Routing header, that will be the destination address in the IPv6 header; otherwise, at the originating node, it will be the address in the last element of the Routing header, and, at the receiving node, it will be the destination address in the IPv6 header. The value of the Next Header field is the protocol value for UDP: 17. The UDP length field is the length of the UDP header and data.
## Reliability and congestion control  
### Lacking reliability, UDP applications may encounter some packet loss, reordering, errors or duplication.  If using UDP, the end-user applications must provide any necessary handshaking such as real-time confirmation that the message has been received. Applications, such as TFTP, may add rudimentary reliability mechanisms into the application layer as needed. If an application requires a high degree of reliability, a protocol such as the Transmission Control Protocol may be used instead. 
### Most often, UDP applications do not employ reliability mechanisms and may even be hindered by them. Streaming media, real-time multiplayer games and voice over IP (VoIP) are examples of applications that often use UDP. In these particular applications, loss of packets is not usually a fatal problem. In VoIP, for example, latency and jitter are the primary concerns.  The use of TCP would cause jitter if any packets were lost as TCP does not provide subsequent data to the application while it is requesting re-sending of the missing data.
## Applications  
### Numerous key Internet applications use UDP, including: the Domain Name System (DNS), where queries must be fast and only consist of a single request followed by a single reply packet, the Simple Network Management Protocol (SNMP), the Routing Information Protocol (RIP) and the Dynamic Host Configuration Protocol (DHCP). 
### Voice and video traffic is generally transmitted using UDP. Real-time video and audio streaming protocols are designed to handle occasional lost packets, so only slight degradation in quality occurs, rather than large delays if lost packets were retransmitted. Because both TCP and UDP run over the same network, in the mid-2000s a few businesses found that a increasing UDP traffic from these real-time applications slightly hindered the performance of applications using TCP such as point of sale, accounting, and database systems (when TCP detects packet loss, it will throttle back its data rate usage).Some VPN systems such as OpenVPN may use UDP and perform error checking at the application level while implementing reliable connections. 
### QUIC is a transport protocol built on top of UDP. QUIC provides a reliable and secure connection. HTTP/3 uses QUIC as opposed to earlier versions of HTTPS which use a combination of TCP and TLS to ensure reliability and security respectively. This means that HTTP/3 uses a single handshake to set up a connection, rather than having two separate handshakes for TCP and TLS, meaning the overall time to establish a connection is reduced.
## Comparison of UDP and TCP  

### Transmission Control Protocol is a connection-oriented protocol and requires handshaking to set up end-to-end communications. Once a connection is set up, user data may be sent bi-directionally over the connection. 

### Reliable \u2013 TCP manages message acknowledgment, retransmission and timeouts. Multiple attempts to deliver the message are made. If data gets lost along the way, data will be re-sent. In TCP, there's either no missing data, or, in case of multiple timeouts, the connection is dropped. 
### Ordered \u2013 If two messages are sent over a connection in sequence, the first message will reach the receiving application first. When data segments arrive in the wrong order, TCP buffers the out-of-order data until all data can be properly re-ordered and delivered to the application. 
### Heavyweight \u2013 TCP requires three packets to set up a socket connection before any user data can be sent. TCP handles reliability and congestion control. 
### Streaming \u2013 Data is read as a byte stream, no distinguishing indications are transmitted to signal message (segment) boundaries.User Datagram Protocol is a simpler message-based connectionless protocol. Connectionless protocols do not set up a dedicated end-to-end connection. Communication is achieved by transmitting information in one direction from source to destination without verifying the readiness or state of the receiver. 

### Unreliable \u2013 When a UDP message is sent, it cannot be known if it will reach its destination; it could get lost along the way. There is no concept of acknowledgment, retransmission, or timeout. 
### Not ordered \u2013 If two messages are sent to the same recipient, the order in which they arrive cannot be guaranteed. 
### Lightweight \u2013 There is no ordering of messages, no tracking connections, etc. It is a very simple transport layer designed on top of IP. 
### Datagrams \u2013 Packets are sent individually and are checked for integrity on arrival. Packets have definite boundaries which are honored upon receipt; a read operation at the receiver socket will yield an entire message as it was originally sent. 
### No congestion control \u2013 UDP itself does not avoid congestion. Congestion control measures must be implemented at the application level or in the network. 
### Broadcasts \u2013 being connectionless, UDP can broadcast - sent packets can be addressed to be receivable by all devices on the subnet. 
### Multicast \u2013 a multicast mode of operation is supported whereby a single datagram packet can be automatically routed without duplication to a group of subscribers.
## Standards  
### RFC 768 \u2013 User Datagram Protocol 
### RFC 2460 \u2013 Internet Protocol, Version 6 (IPv6) Specification 
### RFC 2675 \u2013 IPv6 Jumbograms 
### RFC 4113 \u2013 Management Information Base for the UDP 
### RFC 8085 \u2013 UDP Usage Guidelines
## See also 
## References 
## External links  
### IANA Port Assignments 
### The Trouble with UDP Scanning (PDF) 
### Breakdown of UDP frame 
### UDP on MSDN Magazine Sockets and WCF 
### UDP connections"
## References
### [Reference](http://ipv6.com/articles/general/User-Datagram-Protocol.htm) - http://ipv6.com/articles/general/User-Datagram-Protocol.htm
### [Reference](http://msdn.microsoft.com/en-us/magazine/cc163648.aspx) - http://msdn.microsoft.com/en-us/magazine/cc163648.aspx
### [Reference](http://www.networkperformancedaily.com/2007/08/whiteboard_series_nice_guys_fi.html) - http://www.networkperformancedaily.com/2007/08/whiteboard_series_nice_guys_fi.html
### [Reference](http://www.networksorcery.com/enp/protocol/udp.htm) - http://www.networksorcery.com/enp/protocol/udp.htm
### [Reference](http://condor.depaul.edu/~jkristof/papers/udpscanning.pdf) - http://condor.depaul.edu/~jkristof/papers/udpscanning.pdf
### [Reference](http://doi.org/10.17487%2FRFC0768) - http://doi.org/10.17487%2FRFC0768
### [Reference](http://doi.org/10.17487%2FRFC8200) - http://doi.org/10.17487%2FRFC8200
### [Reference](http://www.faqs.org/docs/iptables/udpconnections.html) - http://www.faqs.org/docs/iptables/udpconnections.html
### [Reference](http://tools.ietf.org/html/rfc2460) - http://tools.ietf.org/html/rfc2460
### [Reference](http://mathforum.org/library/drmath/view/54379.html) - http://mathforum.org/library/drmath/view/54379.html
### [Reference](https://d-nb.info/gnd/4728148-0) - https://d-nb.info/gnd/4728148-0
### [Reference](https://web.archive.org/web/20201117162031/http://mathforum.org/library/drmath/view/54379.html) - https://web.archive.org/web/20201117162031/http://mathforum.org/library/drmath/view/54379.html
### [Reference](https://www.chromium.org/quic) - https://www.chromium.org/quic
### [Reference](https://www.iana.org/assignments/port-numbers) - https://www.iana.org/assignments/port-numbers
### [Reference](https://datatracker.ietf.org/doc/html/rfc1071) - https://datatracker.ietf.org/doc/html/rfc1071
### [Reference](https://datatracker.ietf.org/doc/html/rfc2460) - https://datatracker.ietf.org/doc/html/rfc2460
### [Reference](https://datatracker.ietf.org/doc/html/rfc2675) - https://datatracker.ietf.org/doc/html/rfc2675
### [Reference](https://datatracker.ietf.org/doc/html/rfc4113) - https://datatracker.ietf.org/doc/html/rfc4113
### [Reference](https://datatracker.ietf.org/doc/html/rfc768) - https://datatracker.ietf.org/doc/html/rfc768
### [Reference](https://datatracker.ietf.org/doc/html/rfc8085) - https://datatracker.ietf.org/doc/html/rfc8085
### [Reference](https://datatracker.ietf.org/doc/html/rfc8200) - https://datatracker.ietf.org/doc/html/rfc8200
### [Reference](https://datatracker.ietf.org/doc/html/rfc8200#page-27-28) - https://datatracker.ietf.org/doc/html/rfc8200#page-27-28
### [Reference](https://tools.ietf.org/html/rfc2460) - https://tools.ietf.org/html/rfc2460
### [Reference](https://www.wikidata.org/wiki/Q11163#identifiers) - https://www.wikidata.org/wiki/Q11163#identifiers
### [Reference](https://archive.today/20070731124008/http://www.networkperformancedaily.com/2007/08/whiteboard_series_nice_guys_fi.html) - https://archive.today/20070731124008/http://www.networkperformancedaily.com/2007/08/whiteboard_series_nice_guys_fi.html
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg) - https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg