# Network packet
## [URL](https://en.wikipedia.org/wiki/Network_packet) - https://en.wikipedia.org/wiki/Network_packet
## Catagories
### All articles needing additional references
### Articles needing additional references from August 2014
### Articles with short description
### CS1 maint: url-status
### Packets (information technology)
### Short description is different from Wikidata
### Units of information
### "In telecommunications and computer networking, a network packet is a formatted unit of data carried by a packet-switched network. A packet consists of control information and user data; the latter is also known as the payload. Control information provides data for delivering the payload (e.g., source and destination network addresses, error detection codes, or sequencing information). Typically, control information is found in packet headers and trailers. 
### In packet switching, the bandwidth of the transmission medium is shared between multiple communication sessions, in contrast to circuit switching, in which circuits are preallocated for the duration of one session and data is typically transmitted as a continuous bit stream.
## Terminology  
### In the seven-layer OSI model of computer networking, packet strictly refers to a protocol data unit at layer 3, the network layer. A data unit at layer 2, the data link layer, is a frame. In layer 4, the transport layer, the data units are segments and datagrams. Thus, in the example of TCP/IP communication over Ethernet, a TCP segment is carried in one or more IP packets, which are each carried in one or more Ethernet frames.
## Architecture  
### The basis of the packet concept is the postal letter: the header is like the envelope, the payload is the entire content inside the envelope, and the footer would be your signature at the bottom.Network design can achieve two major results by using packets: error detection and multiple host addressing.
## Framing  
### Different communications protocols use different conventions for distinguishing between the elements of a packet and for formatting the user data. For example, in Point-to-Point Protocol, the packet is formatted in 8-bit bytes, and special characters are used to delimit the different elements. Other protocols, like Ethernet, establish the start of the header and data elements by their location relative to the start of the packet. Some protocols format the information at a bit level instead of a byte level.
## Contents  
### A packet may contain any of the following components: 

### Addresses 
### The routing of network packets requires two network addresses, the source address of the sending host, and the destination address of the receiving host.Error detection and correction 
### Error detection and correction is performed at various layers in the protocol stack. Network packets may contain a checksum, parity bits or cyclic redundancy checks to detect errors that occur during transmission.At the transmitter, the calculation is performed before the packet is sent. When received at the destination, the checksum is recalculated, and compared with the one in the packet. If discrepancies are found, the packet may be corrected or discarded. Any packet loss due to these discards is dealt with by the network protocol.In some cases modifications of the network packet may be necessary while routing, in which cases checksums are recalculated.Hop limit 
### Under fault conditions, packets can end up traversing a closed circuit. If nothing was done, eventually the number of packets circulating would build up until the network was congested to the point of failure. Time to live is a field that is decreased by one each time a packet goes through a network hop. If the field reaches zero, routing has failed, and the packet is discarded.Ethernet packets have no time-to-live field and so are subject to broadcast radiation in the presence of a switching loop.Length 
### There may be a field to identify the overall packet length. However, in some types of networks, the length is implied by the duration of the transmission.Protocol identifier 
### It is often desirable to carry different communication protocols on the same network. A protocol identifier field can distinguish packets using different protocols and allows the protocol stack to properly process different types of packets.Priority 
### Some networks implement quality of service which can prioritize some types of packets above others. This field indicates which packet queue should be used; a high priority queue is emptied more quickly than lower priority queues at points in the network where congestion is occurring.Payload 
### In general, the payload is the data that is carried on behalf of an application. It is usually of variable length, up to a maximum that is set by the network protocol and sometimes the equipment on the route. When necessary, some networks can break a larger packet into smaller packets.
## Examples 
## Internet protocol  
### IP packets are composed of a header and payload. The header consists of fixed and optional fields. The payload appears immediately after the header. An IP packet has no trailer. However, an IP packet is often carried as the payload inside an Ethernet frame, which has its own header and trailer. 
### Per the end-to-end principle, IP networks do not provide guarantees of delivery, non-duplication, or in-order delivery of packets. However, it is common practice to layer a reliable transport protocol such as Transmission Control Protocol on top of the packet service to provide such protection.
## NASA Deep Space Network  
### The Consultative Committee for Space Data Systems (CCSDS) packet telemetry standard defines the protocol used for the transmission of spacecraft instrument data over the deep-space channel. Under this standard, an image or other data sent from a spacecraft instrument is transmitted using one or more packets.
## MPEG packetized stream  
### Packetized elementary stream (PES) is a specification associated with the MPEG-2 standard that allows an elementary stream to be divided into packets. The elementary stream is packetized by encapsulating sequential data bytes from the elementary stream between PES packet headers. 
### A typical method of transmitting elementary stream data from a video or audio encoder is to first create PES packets from the elementary stream data and then to encapsulate these PES packets inside an MPEG transport stream (TS) packets or an MPEG program stream (PS). The TS packets can then be transmitted using broadcasting techniques, such as those used in an ATSC and DVB.
## NICAM  
### In order to provide mono \"compatibility\", the NICAM signal is transmitted on a subcarrier alongside the sound carrier. This means that the FM or AM regular mono sound carrier is left alone for reception by monaural receivers. The NICAM packet (except for the header) is scrambled with a nine-bit pseudo-random bit-generator before transmission. Making the NICAM bitstream look more like white noise is important because this reduces signal patterning on adjacent TV channels.
## See also 
## References "
## References
### [Reference](http://scholar.google.com/scholar?q=%22Network+packet%22) - http://scholar.google.com/scholar?q=%22Network+packet%22
### [Reference](http://www.google.com/search?&q=%22Network+packet%22&tbs=bkt:s&tbm=bks) - http://www.google.com/search?&q=%22Network+packet%22&tbs=bkt:s&tbm=bks
### [Reference](http://www.google.com/search?as_eq=wikipedia&q=%22Network+packet%22) - http://www.google.com/search?as_eq=wikipedia&q=%22Network+packet%22
### [Reference](http://www.google.com/search?tbm=nws&q=%22Network+packet%22+-wikipedia&tbs=ar:1) - http://www.google.com/search?tbm=nws&q=%22Network+packet%22+-wikipedia&tbs=ar:1
### [Reference](http://www.google.com/search?tbs=bks:1&q=%22Network+packet%22+-wikipedia) - http://www.google.com/search?tbs=bks:1&q=%22Network+packet%22+-wikipedia
### [Reference](http://www.tcpipguide.com/free/t_UnderstandingTheOSIReferenceModelAnAnalogy.htm) - http://www.tcpipguide.com/free/t_UnderstandingTheOSIReferenceModelAnAnalogy.htm
### [Reference](http://www.msc.uky.edu/ken/cs471/notes/chap5.htm) - http://www.msc.uky.edu/ken/cs471/notes/chap5.htm
### [Reference](https://www.cloudflare.com/en-in/learning/ddos/glossary/open-systems-interconnection-model-osi/) - https://www.cloudflare.com/en-in/learning/ddos/glossary/open-systems-interconnection-model-osi/
### [Reference](https://archive.org/details/businessdatacomm00stal/page/632) - https://archive.org/details/businessdatacomm00stal/page/632
### [Reference](https://web.archive.org/web/20140809215056/http://www.tcpipguide.com/free/t_UnderstandingTheOSIReferenceModelAnAnalogy.htm) - https://web.archive.org/web/20140809215056/http://www.tcpipguide.com/free/t_UnderstandingTheOSIReferenceModelAnAnalogy.htm
### [Reference](https://www.jstor.org/action/doBasicSearch?Query=%22Network+packet%22&acc=on&wc=on) - https://www.jstor.org/action/doBasicSearch?Query=%22Network+packet%22&acc=on&wc=on
## Images
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20210726203439%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20210726203439%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20201004174738%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20201004174738%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171208221057%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171208221057%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171207131032%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171207131032%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20160612140736%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20160612140736%21Question_book-new.svg