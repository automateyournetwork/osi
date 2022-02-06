# Logical link control
## [URL](https://en.wikipedia.org/wiki/Logical_link_control) - https://en.wikipedia.org/wiki/Logical_link_control
## Catagories
### All articles lacking sources
### Articles lacking sources from October 2009
### Logical link control
### "In the IEEE 802 reference model of computer networking, the logical link control (LLC) data communication protocol layer is the upper sublayer of the data link layer (layer 2) of the seven-layer OSI model. The LLC sublayer acts as an interface between the media access control (MAC) sublayer and the network layer.  
### The LLC sublayer provides multiplexing mechanisms that make it possible for several network protocols (e.g. IP, IPX and DECnet) to coexist within a multipoint network and to be transported over the same network medium. It can also provide flow control and automatic repeat request (ARQ) error management mechanisms.
## Operation  
### The LLC sublayer is primarily concerned with multiplexing protocols transmitted over the MAC layer (when transmitting) and demultiplexing them (when receiving). 
### It can also provide node-to-node flow control and error management. 
### The flow control and error management capabilities of the LLC sublayer are used by protocols such as the NetBIOS Frames protocol. However, most protocol stacks running atop 802.2 do not use LLC sublayer flow control and error management. In these cases flow control and error management are taken care of by a transport layer protocol such as TCP or by some application layer protocol. These higher layer protocols work in an end-to-end fashion, i.e. re-transmission is done from the original source to the final destination, rather than on individual physical segments. For these protocol stacks only the multiplexing capabilities of the LLC sublayer are used.
## Application examples 
## X.25 and LAPB  
### An LLC sublayer was a key component in early packet switching networks such as X.25 networks with the LAPB data link layer protocol, where flow control and error management were carried out in a node-to-node fashion, meaning that if an error was detected in a frame, the frame was retransmitted from one switch to next instead. This extensive handshaking between the nodes made the networks slow.
## Local area network  
### The IEEE 802.2 standard specifies the LLC sublayer for all IEEE 802 local area networks, such as IEEE 802.3/Ethernet (when Ethernet II frame format is not used), IEEE 802.5, and IEEE 802.11.  IEEE 802.2 is also used in some non-IEEE 802 networks such as FDDI.
## Ethernet  
### Since bit errors are very rare in wired networks, Ethernet does not provide flow control or automatic repeat request (ARQ), meaning that incorrect packets are detected but only cancelled, not retransmitted (except in case of collisions detected by the CSMA/CD MAC layer protocol). Instead, retransmissions rely on higher layer protocols. 
### As the EtherType in an Ethernet frame using Ethernet II framing is used to multiplex different protocols on top of the Ethernet MAC header it can be seen as an LLC identifier. However, Ethernet frames lacking an EtherType have no LLC identifier in the Ethernet header, and, instead, use an IEEE 802.2 LLC header after the Ethernet header to provide the protocol multiplexing function.
## Wireless LAN  
### In wireless communications, bit errors are very common. In wireless networks such as IEEE 802.11, flow control and error management is part of the CSMA/CA MAC protocol, and not part of the LLC layer. The LLC sublayer follows the IEEE 802.2 standard.
## HDLC  
### Some non-IEEE 802 protocols can be thought of as being split into MAC and LLC layers.  For example, while HDLC specifies both MAC functions (framing of packets) and LLC functions (protocol multiplexing, flow control, detection, and error control through a retransmission of dropped packets when indicated), some protocols such as Cisco HDLC can use HDLC-like packet framing and their own LLC protocol.
## PPP and modems  
### Over telephone network modems, PPP link layer protocols can be considered as a LLC protocol, providing multiplexing, but it does not provide flow control and error management. In a telephone network, bit errors might be common, meaning that error management is crucial, but that is today provided by modern protocols. Today's modem protocols have inherited LLC features from the older LAPM link layer protocol, made for modem communication in old X.25 networks.
## Cellular systems  
### The GPRS LLC layer also does ciphering and deciphering of SN-PDU (SNDCP) packets.
## Power lines  
### Another example of a data link layer which is split between LLC (for flow and error control) and MAC (for multiple access) is the ITU-T G.hn standard, which provides high-speed local area networking over existing home wiring (power lines, phone lines and coaxial cables).
## See also  
### Subnetwork Access Protocol (SNAP) 
### Virtual Circuit Multiplexing (VC-MUX)"
## References
### [Reference](http://scholar.google.com/scholar?q=%22Logical+link+control%22) - http://scholar.google.com/scholar?q=%22Logical+link+control%22
### [Reference](http://www.google.com/search?&q=%22Logical+link+control%22&tbs=bkt:s&tbm=bks) - http://www.google.com/search?&q=%22Logical+link+control%22&tbs=bkt:s&tbm=bks
### [Reference](http://www.google.com/search?as_eq=wikipedia&q=%22Logical+link+control%22) - http://www.google.com/search?as_eq=wikipedia&q=%22Logical+link+control%22
### [Reference](http://www.google.com/search?tbm=nws&q=%22Logical+link+control%22+-wikipedia&tbs=ar:1) - http://www.google.com/search?tbm=nws&q=%22Logical+link+control%22+-wikipedia&tbs=ar:1
### [Reference](http://www.google.com/search?tbs=bks:1&q=%22Logical+link+control%22+-wikipedia) - http://www.google.com/search?tbs=bks:1&q=%22Logical+link+control%22+-wikipedia
### [Reference](https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://www.itu.int/rec/T-REC-X.225-199511-I/en
### [Reference](https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en
### [Reference](https://www.jstor.org/action/doBasicSearch?Query=%22Logical+link+control%22&acc=on&wc=on) - https://www.jstor.org/action/doBasicSearch?Query=%22Logical+link+control%22&acc=on&wc=on
## Images
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20210726203439%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20210726203439%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20201004174738%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20201004174738%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171208221057%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171208221057%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171207131032%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171207131032%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20160612140736%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20160612140736%21Question_book-new.svg