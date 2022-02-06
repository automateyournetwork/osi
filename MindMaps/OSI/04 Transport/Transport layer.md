# Transport layer
## [URL](https://en.wikipedia.org/wiki/Transport_layer) - https://en.wikipedia.org/wiki/Transport_layer
## Catagories
### All Wikipedia articles written in American English
### All articles needing additional references
### All articles with failed verification
### Articles needing additional references from October 2015
### Articles with failed verification from January 2022
### Articles with short description
### OSI model
### Short description is different from Wikidata
### Use American English from March 2019
### Use mdy dates from March 2019
### "In computer networking, the transport layer is a conceptual division of methods in the layered architecture of protocols in the network stack in the Internet protocol suite and the OSI model. The protocols of this layer provide end-to-end communication services for applications.:\u200a\u00a71.1.3\u200a It provides services such as connection-oriented communication, reliability, flow control, and multiplexing. 
### The details of implementation and semantics of the transport layer of the Internet protocol suite, which is the foundation of the Internet, and the OSI model of general networking are different. The protocols in use today in this layer for the Internet all originated in the development of TCP/IP. In the OSI model the transport layer is often referred to as Layer 4, or L4, while numbered layers are not used in TCP/IP. 
### The best-known transport protocol of the Internet protocol suite is the Transmission Control Protocol (TCP). It is used for connection-oriented transmissions, whereas the connectionless User Datagram Protocol (UDP) is used for simpler messaging transmissions. TCP is the more complex protocol, due to its stateful design incorporating reliable transmission and data stream services.  Together, TCP and UDP comprise essentially all traffic on the Internet and are the only protocols implemented in every major operating system. Additional transport layer protocols that have been defined and implemented include the Datagram Congestion Control Protocol (DCCP) and the Stream Control Transmission Protocol (SCTP).
## Services  
### Transport layer services are conveyed to an application via a programming interface to the transport layer protocols. The services may include the following features: 

### Connection-oriented communication: It is normally easier for an application to interpret a connection as a data stream rather than having to deal with the underlying connection-less models, such as the datagram model of the User Datagram Protocol (UDP) and of the Internet Protocol (IP). 
### Same order delivery: The network layer doesn't generally guarantee that packets of data will arrive in the same order that they were sent, but often this is a desirable feature. This is usually done through the use of segment numbering, with the receiver passing them to the application in order. This can cause head-of-line blocking. 
### Reliability: Packets may be lost during transport due to network congestion and errors. By means of an error detection code, such as a checksum, the transport protocol may check that the data is not corrupted, and verify correct receipt by sending an ACK or NACK message to the sender. Automatic repeat request schemes may be used to retransmit lost or corrupted data. 
### Flow control: The rate of data transmission between two nodes must sometimes be managed to prevent a fast sender from transmitting more data than can be supported by the receiving data buffer, causing a buffer overrun. This can also be used to improve efficiency by reducing buffer underrun. 
### Congestion avoidance: Congestion control can control traffic entry into a telecommunications network, so as to avoid congestive collapse by attempting to avoid oversubscription of any of the processing or link capabilities of the intermediate nodes and networks and taking resource reducing steps, such as reducing the rate of sending packets. For example, automatic repeat requests may keep the network in a congested state; this situation can be avoided by adding congestion avoidance to the flow control, including slow-start. This keeps the bandwidth consumption at a low level in the beginning of the transmission, or after packet retransmission. 
### Multiplexing: Ports can provide multiple endpoints on a single node. For example, the name on a postal address is a kind of multiplexing, and distinguishes between different recipients of the same location. Computer applications will each listen for information on their own ports, which enables the use of more than one network service at the same time. It is part of the transport layer in the TCP/IP model, but of the session layer in the OSI model.
## Analysis  
### The transport layer is responsible for delivering data to the appropriate application process on the host computers. This involves statistical multiplexing of data from different application processes, i.e. forming data segments, and adding source and destination port numbers in the header of each transport layer data segment. Together with the source and destination IP address, the port numbers constitute a network socket, i.e. an identification address of the process-to-process communication. In the OSI model, this function is supported by the session layer. 
### Some transport layer protocols, for example TCP, but not UDP, support virtual circuits, i.e. provide connection-oriented communication over an underlying packet-oriented datagram network. A byte-stream is delivered while hiding the packet mode communication for the application processes. This involves connection establishment, dividing of the data stream into packets called segments, segment numbering and reordering of out-of order data. 
### Finally, some transport layer protocols, for example TCP, but not UDP, provide end-to-end reliable communication, i.e. error recovery by means of error detecting code and automatic repeat request (ARQ) protocol. The ARQ protocol also provides flow control, which may be combined with congestion avoidance. 
### UDP is a very simple protocol, and does not provide virtual circuits, nor reliable communication, delegating these functions to the application program. UDP packets are called datagrams, rather than segments. 
### TCP is used for many protocols, including HTTP web browsing and email transfer. UDP may be used for multicasting and broadcasting, since retransmissions are not possible to a large amount of hosts. UDP typically gives higher throughput and shorter latency, and is therefore often used for real-time multimedia communication where packet loss occasionally can be accepted, for example IP-TV and IP-telephony, and for online computer games. 
### Many non-IP-based networks, such as X.25, Frame Relay and ATM, implement the connection-oriented communication at the network or data link layer rather than the transport layer. In X.25, in telephone network modems and in wireless communication systems, reliable node-to-node communication is implemented at lower protocol layers. 
### The OSI connection-mode transport layer protocol specification defines five classes of transport protocols: TP0, providing the least error recovery, to TP4, which is designed for less reliable networks.
## Protocols  
### This list shows some protocols that are commonly placed in the transport layers of the Internet protocol suite, the OSI protocol suite, NetWare's IPX/SPX, AppleTalk, and Fibre Channel.
## Comparison of transport layer protocols 
## Comparison of OSI transport protocols  
### ISO/IEC 8073/ITU-T Recommendation X.224, \"Information Technology - Open Systems Interconnection - Protocol for providing the connection-mode transport service\", defines five classes of connection-mode transport protocols designated class 0 (TP0) to class 4 (TP4).  Class 0 contains no error recovery, and was designed for use on network layers that provide error-free connections. Class 4 is closest to TCP, although TCP contains functions, such as the graceful close, which OSI assigns to the session layer.  All OSI connection-mode protocol classes provide expedited data and preservation of record boundaries.  Detailed characteristics of the classes are shown in the following table: 
### There is also a connectionless transport protocol, specified by ISO/IEC 8602/ITU-T Recommendation X.234.
## References "
## Links
### ASCII
### ASN.1
### Abstraction layer
### Acknowledgement (data networks)
### Address Resolution Protocol
### AppleTalk
### Application layer
### Application software
### Asynchronous Transfer Mode
### Automatic repeat request
### Bluetooth
### Border Gateway Protocol
### Broadcasting (networking)
### Buffer underrun
### Checksum
### Computer network
### Congestion avoidance
### Congestion control
### Congestive collapse
### Connection-oriented communication
### Cyclic UDP
### DHCPv6
### Data buffer
### Data link
### Data link layer
### Data stream
### Datagram
### Datagram Congestion Control Protocol
### Digital subscriber line
### Doi (identifier)
### Domain Name System
### Dynamic Host Configuration Protocol
### Error detecting code
### Error detection code
### Error recovery
### Explicit Congestion Notification
### External Data Representation
### Fibre Channel
### Fibre Channel Protocol
### File Transfer Protocol
### Flow control (data)
### Frame Relay
### G.hn
### Generic Framing Procedure
### Gopher (protocol)
### HTTP
### HTTPS
### Head-of-line blocking
### High-Level Data Link Control
### Hypertext Transfer Protocol
### I.430
### I.431
### IEEE 1394
### IEEE 802.11
### IEEE 802.15
### IEEE 802.16
### IEEE 802.2
### IEEE 802.3
### IL Protocol
### IPX/SPX
### IPsec
### IPv4
### IPv6
### IS-IS
### Internet
### Internet Control Message Protocol
### Internet Control Message Protocol for IPv6
### Internet Group Management Protocol
### Internet Message Access Protocol
### Internet Protocol
### Internet layer
### Internet protocol suite
### Internetwork Packet Exchange
### LAPB
### Layer 2 Tunneling Protocol
### Lightweight Directory Access Protocol
### Link Access Procedure for Frame Relay
### Link layer
### List of ITU-T V-series recommendations
### Logical link control
### MIME
### MQTT
### Maximum transmission unit
### Media Gateway Control Protocol
### Medium access control
### Micro Transport Protocol
### Multi-homing
### Multicast
### Multipath TCP
### Multiplexing
### NACK-Oriented Reliable Multicast
### NETCONF
### Nagle's algorithm
### Named pipe
### Negative-acknowledge character
### Neighbor Discovery Protocol
### NetBIOS
### NetWare
### Network File System
### Network News Transfer Protocol
### Network Time Protocol
### Network congestion
### Network layer
### Network service
### Network socket
### OSI model
### OSI protocols
### Open Network Computing Remote Procedure Call
### Open Shortest Path First
### Optical Transport Network
### Packet (information technology)
### Packet Layer Protocol
### Parallel Line Internet Protocol
### Passive optical network
### Physical layer
### Plesiochronous digital hierarchy
### Point-to-Point Protocol
### Point-to-Point Tunneling Protocol
### Post Office Protocol
### Precision Time Protocol
### Presentation layer
### Pretty Good Privacy
### Protocol data unit
### QUIC
### RFC (identifier)
### RS-232
### RS-449
### Real-time Transport Protocol
### Real Time Streaming Protocol
### Reliability (computer networking)
### Reliable Data Protocol
### Reliable User Datagram Protocol
### Resource Reservation Protocol
### Routing Information Protocol
### SOCKS
### SPDY
### Secure Shell
### Serial Line Internet Protocol
### Session Announcement Protocol
### Session Initiation Protocol
### Session layer
### Short Message Peer-to-Peer
### Simple Mail Transfer Protocol
### Simple Network Management Protocol
### Simple Sensor Interface protocol
### Slow-start
### Stateful design
### Statistical multiplexing
### Stream (computing)
### Stream Control Transmission Protocol
### Structured Stream Transport
### Synchronous Data Link Control
### Synchronous optical networking
### TCP/IP model
### TCP and UDP port
### Telnet
### Throughput
### Transmission Control Protocol
### Transport Layer Security
### Tunneling protocol
### UDP-Lite
### USB
### User Datagram Protocol
### Virtual circuit
### X.25
### XMPP
## References
### [Reference](http://scholar.google.com/scholar?q=%22Transport+layer%22) - http://scholar.google.com/scholar?q=%22Transport+layer%22
### [Reference](http://www.google.com/search?&q=%22Transport+layer%22&tbs=bkt:s&tbm=bks) - http://www.google.com/search?&q=%22Transport+layer%22&tbs=bkt:s&tbm=bks
### [Reference](http://www.google.com/search?as_eq=wikipedia&q=%22Transport+layer%22) - http://www.google.com/search?as_eq=wikipedia&q=%22Transport+layer%22
### [Reference](http://www.google.com/search?tbm=nws&q=%22Transport+layer%22+-wikipedia&tbs=ar:1) - http://www.google.com/search?tbm=nws&q=%22Transport+layer%22+-wikipedia&tbs=ar:1
### [Reference](http://www.google.com/search?tbs=bks:1&q=%22Transport+layer%22+-wikipedia) - http://www.google.com/search?tbs=bks:1&q=%22Transport+layer%22+-wikipedia
### [Reference](http://www.itu.int/rec/T-REC-X.224-199511-I/en/) - http://www.itu.int/rec/T-REC-X.224-199511-I/en/
### [Reference](http://www.itu.int/rec/T-REC-X.234-199407-I/en/) - http://www.itu.int/rec/T-REC-X.234-199407-I/en/
### [Reference](http://doi.org/10.17487%2FRFC1122) - http://doi.org/10.17487%2FRFC1122
### [Reference](https://docs.oracle.com/cd/E19455-01/806-0916/6ja85398m/index.html) - https://docs.oracle.com/cd/E19455-01/806-0916/6ja85398m/index.html
### [Reference](https://www.cs.cornell.edu/zeno/Papers/cyclicudp.pdf) - https://www.cs.cornell.edu/zeno/Papers/cyclicudp.pdf
### [Reference](https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://www.itu.int/rec/T-REC-X.225-199511-I/en
### [Reference](https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en
### [Reference](https://datatracker.ietf.org/doc/html/rfc1122) - https://datatracker.ietf.org/doc/html/rfc1122
### [Reference](https://www.jstor.org/action/doBasicSearch?Query=%22Transport+layer%22&acc=on&wc=on) - https://www.jstor.org/action/doBasicSearch?Query=%22Transport+layer%22&acc=on&wc=on
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/4/40/Internet_Protocol_Analysis_-_Transport_Layer.png) - https://upload.wikimedia.org/wikipedia/commons/4/40/Internet_Protocol_Analysis_-_Transport_Layer.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg) - https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg