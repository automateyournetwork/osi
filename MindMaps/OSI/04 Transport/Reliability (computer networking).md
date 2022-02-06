# Reliability (computer networking)
## [URL](https://en.wikipedia.org/wiki/Reliability_(computer_networking)) - https://en.wikipedia.org/wiki/Reliability_(computer_networking)
## Catagories
### All Wikipedia articles written in American English
### All articles with unsourced statements
### Articles with unsourced statements from November 2017
### CS1 maint: archived copy as title
### Network protocols
### Reliability engineering
### Use American English from January 2020
### "In computer networking, a reliable protocol is a communication protocol that notifies the sender whether or not the delivery of data to intended recipients was successful.  Reliability is a synonym for assurance, which is the term used by the ITU and ATM Forum. 
### Reliable protocols typically incur more overhead than unreliable protocols, and as a result, function more slowly and with less scalability. This often is not an issue for unicast protocols, but it may become a problem for reliable multicast protocols. 
### Transmission Control Protocol (TCP), the main protocol used on the Internet, is a reliable unicast protocol. UDP is an unreliable protocol and is often used in computer games, streaming media or in other situations where speed is an issue and some data loss may be tolerated because of the transitory nature of the data. 
### Often, a reliable unicast protocol is also connection oriented. For example, TCP is connection oriented, with the virtual-circuit ID consisting of source and destination IP addresses and port numbers. However, some unreliable protocols are connection oriented, such as Asynchronous Transfer Mode and Frame Relay. In addition, some connectionless protocols, such as IEEE 802.11, are reliable.
## History  
### Building on the packet switching concepts proposed by Donald Davies, the first communication protocol on the ARPANET was a reliable packet delivery procedure to connect its hosts via the 1822 interface. A host computer simply arranged the data in the correct packet format, inserted the address of the destination host computer, and sent the message across the interface to its connected Interface Message Processor (IMP). Once the message was delivered to the destination host, an acknowledgment was delivered to the sending host. If the network could not deliver the message, the IMP would send an error message back to the sending host. 
### Meanwhile, the developers of CYCLADES and of ALOHAnet demonstrated that it was possible to build an effective computer network without providing reliable packet transmission. This lesson was later embraced by the designers of Ethernet. 
### If a network does not guarantee packet delivery, then it becomes the host's responsibility to provide reliability by detecting and retransmitting lost packets. Subsequent experience on the ARPANET indicated that the network itself could not reliably detect all packet delivery failures, and this pushed responsibility for error detection onto the sending host in any case. This led to the development of the end-to-end principle, which is one of the Internet's fundamental design principles.
## Reliability properties  
### A reliable service is one that notifies the user if delivery fails, while an unreliable one does not notify the user if delivery fails. For example, Internet Protocol (IP) provides an unreliable service. Together, Transmission Control Protocol (TCP) and IP provide a reliable service, whereas User Datagram Protocol (UDP) and IP provide an unreliable one. 
### In the context of distributed protocols, reliability properties specify the guarantees that the protocol provides with respect to the delivery of messages to the intended recipient(s). 
### An example of a reliability property for a unicast protocol is \"at least once\", i.e. at least one copy of the message is guaranteed to be delivered to the recipient. 
### Reliability properties for multicast protocols can be expressed on a per-recipient basis (simple reliability properties), or they may relate the fact of delivery or the order of delivery among the different recipients (strong reliability properties). In the context of multicast protocols, strong reliability properties express the guarantees that the protocol provides with respect to the delivery of messages to different recipients. 
### An example of a strong reliability property is last copy recall, meaning that as long as at least a single copy of a message remains available at any of the recipients, every other recipient that does not fail eventually also receives a copy. Strong reliability properties such as this one typically require that messages are retransmitted or forwarded among the recipients. 
### An example of a reliability property stronger than last copy recall is atomicity. The property states that if at least a single copy of a message has been delivered to a recipient, all other recipients will eventually receive a copy of the message. In other words, each message is always delivered to either all or none of the recipients. 
### One of the most complex strong reliability properties is virtual synchrony. 
### Reliable messaging is the concept of message passing across an unreliable infrastructure whilst being able to make certain guarantees about the successful transmission of the messages. For example, that if the message is delivered, it is delivered at most once, or that all messages successfully delivered arrive in a particular order. 
### Reliable delivery can be contrasted with best-effort delivery, where there is no guarantee that messages will be delivered quickly, in order, or at all.  
## Implementations  
### A reliable delivery protocol can be built on an unreliable protocol. An extremely common example is the layering of Transmission Control Protocol on the Internet Protocol, a combination known as TCP/IP. 
### Strong reliability properties are offered by group communication systems (GCSs) such as IS-IS, Appia framework, Spread, JGroups or QuickSilver Scalable Multicast. The QuickSilver Properties Framework is a flexible platform that allows strong reliability properties to be expressed in a purely declarative manner, using a simple rule-based language, and automatically translated into a hierarchical protocol. 
### One protocol that implements reliable messaging is WS-ReliableMessaging, which handles reliable delivery of SOAP messages.The ATM Service-Specific Coordination Function provides for transparent assured delivery with AAL5.IEEE 802.11 attempts to provide reliable service for all traffic. The sending station will resend a frame if the sending station doesn't receive an ACK frame within a predetermined period of time.
## Real-time systems  
### There is, however, a problem with the definition of reliability as \"delivery or notification of failure\" in real-time computing. In such systems, failure to deliver the real-time data will adversely affect the performance of the systems, and some systems, e.g. safety-critical, safety-involved, and some secure mission-critical systems, must be proved to perform at some specified minimum level. This, in turn, requires that a specified minimum reliability for the delivery of the critical data be met. Therefore, in these cases, it is only the delivery that matters; notification of the failure to deliver does ameliorate the failure. In hard real-time systems, all data must be delivered by the deadline or it is considered a system failure. In firm real-time systems, late data is still valueless but the system can tolerate some amount of late or missing data.There are a number of protocols that are capable of addressing real-time requirements for reliable delivery and timeliness: 
### MIL-STD-1553B and STANAG 3910 are well-known examples of such timely and reliable protocols for avionic data buses. MIL-1553 uses a 1 Mbit/s shared media for the transmission of data and the control of these transmissions, and is widely used in federated military avionics systems. It uses a bus controller (BC) to command the connected remote terminals (RTs) to receive or transmit this data. The BC can, therefore, ensure that there will be no congestion, and transfers are always timely. The MIL-1553 protocol also allows for automatic retries that can still ensure timely delivery and increase the reliability above that of the physical layer. STANAG 3910, also known as EFABus in its use on the Eurofighter Typhoon, is, in effect, a version of MIL-1553 augmented with a 20 Mbit/s shared media bus for data transfers, retaining the 1 Mbit/s shared media bus for control purposes. 
### The Asynchronous Transfer Mode (ATM), the Avionics Full-Duplex Switched Ethernet (AFDX), and Time Triggered Ethernet (TTEthernet) are examples of packet-switched networks protocols where the timeliness and reliability of data transfers can be assured by the network. AFDX and TTEthernet are also based on IEEE 802.3 Ethernet, though not entirely compatible with it. 
### ATM uses connection-oriented virtual channels (VCs) which have fully deterministic paths through the network, and usage and network parameter control (UPC/NPC), which are implemented within the network, to limit the traffic on each VC separately. This allows the usage of the shared resources (switch buffers) in the network to be calculated from the parameters of the traffic to be carried in advance, i.e. at system design time. That they are implemented by the network means that these calculations remain valid even when other users of the network behave in unexpected ways, i.e. transmit more data than they are expected to. The calculated usages can then be compared with the capacities of these resources to show that, given the constraints on the routes and the bandwidths of these connections, the resource used for these transfers will never be over-subscribed. These transfers will therefore never be affected by congestion and there will be no losses due to this effect. Then, from the predicted maximum usages of the switch buffers, the maximum delay through the network can also be predicted. However, for the reliability and timeliness to be proved, and for the proofs to be tolerant of faults in and malicious actions by the equipment connected to the network, the calculations of these resource usages cannot be based on any parameters that are not actively enforced by the network, i.e. they cannot be based on what the sources of the traffic are expected to do or on statistical analyses of the traffic characteristics (see network calculus).AFDX uses frequency domain bandwidth allocation and traffic policing, that allows the traffic on each virtual link (VL) to be limited so that the requirements for shared resources can be predicted and congestion prevented so it can be proved not to affect the critical data. However, the techniques for predicting the resource requirements and proving that congestion is prevented are not part of the AFDX standard. 
### TTEthernet provides the lowest possible latency in transferring data across the network by using time-domain control methods \u2013 each time triggered transfer is scheduled at a specific time so that contention for shared resources is controlled and thus the possibility of congestion is eliminated. The switches in the network enforce this timing to provide tolerance of faults in, and malicious actions on the part of, the other connected equipment. However, \"synchronized local clocks are the fundamental prerequisite for time-triggered communication\". This is because the sources of critical data will have to have the same view of time as the switch, in order that they can transmit at the correct time and the switch will see this as correct. This also requires that the sequence with which a critical transfer is scheduled has to be predictable to both source and switch. This, in turn, will limit the transmission schedule to a highly deterministic one, e.g. the cyclic executive. 
### However, low latency in transferring data over the bus or network does not necessarily translate into low transport delays between the application processes that source and sink this data. This is especially true where the transfers over the bus or network are cyclically scheduled (as is commonly the case with MIL-STD-1553B and STANAG 3910, and necessarily so with AFDX and TTEthernet) but the application processes are not synchronized with this schedule. 
### With both AFDX and TTEthernet, there are additional functions required of the interfaces, e.g. AFDX's Bandwidth Allocation Gap control, and TTEthernet's requirement for very close synchronization of the sources of time-triggered data, that make it difficult to use standard Ethernet interfaces. Other methods for control of the traffic in the network that would allow the use of such standard IEEE 802.3 network interfaces is a subject of current research.
## References "
## References
### [Reference](http://download.boulder.ibm.com/ibmdl/pub/software/dw/specs/ws-rm/ws-reliablemessaging200502.pdf) - http://download.boulder.ibm.com/ibmdl/pub/software/dw/specs/ws-rm/ws-reliablemessaging200502.pdf
### [Reference](http://www.csl.sri.com/users/bruno/publis/fmics2010.pdf) - http://www.csl.sri.com/users/bruno/publis/fmics2010.pdf
### [Reference](http://www.techsat.com/fileadmin/media/pdf/infokiosk/TechSAT_TUT-AFDX-EN.pdf) - http://www.techsat.com/fileadmin/media/pdf/infokiosk/TechSAT_TUT-AFDX-EN.pdf
### [Reference](http://www.ismlab.usf.edu/dcom/Ch10_Roberts_EvolutionPacketSwitching_IEEE_1978.pdf) - http://www.ismlab.usf.edu/dcom/Ch10_Roberts_EvolutionPacketSwitching_IEEE_1978.pdf
### [Reference](http://doi.org/10.1016%2F0140-3664(96)01063-8) - http://doi.org/10.1016%2F0140-3664(96)01063-8
### [Reference](http://doi.org/10.1109%2FAVFOP.2013.6661601) - http://doi.org/10.1109%2FAVFOP.2013.6661601
### [Reference](http://www.w3.org/2001/03/WSWS-popa/paper40) - http://www.w3.org/2001/03/WSWS-popa/paper40
### [Reference](https://books.google.com/books?id=pIH-JijUNS0C&pg=PA25) - https://books.google.com/books?id=pIH-JijUNS0C&pg=PA25
### [Reference](https://web.archive.org/web/20150203164824/https://www.kth.se/polopoly_fs/1.146328!/Menu/general/column-content/attachment/3_Ekman_Saab.pdf) - https://web.archive.org/web/20150203164824/https://www.kth.se/polopoly_fs/1.146328!/Menu/general/column-content/attachment/3_Ekman_Saab.pdf
### [Reference](https://web.archive.org/web/20150618140031/http://www.techsat.com/fileadmin/media/pdf/infokiosk/TechSAT_TUT-AFDX-EN.pdf) - https://web.archive.org/web/20150618140031/http://www.techsat.com/fileadmin/media/pdf/infokiosk/TechSAT_TUT-AFDX-EN.pdf
### [Reference](https://doi.org/10.1109%2FMILCOM.1999.821329) - https://doi.org/10.1109%2FMILCOM.1999.821329
### [Reference](https://api.semanticscholar.org/CorpusID:3162009) - https://api.semanticscholar.org/CorpusID:3162009
### [Reference](https://www.kth.se/polopoly_fs/1.146328!/Menu/general/column-content/attachment/3_Ekman_Saab.pdf) - https://www.kth.se/polopoly_fs/1.146328!/Menu/general/column-content/attachment/3_Ekman_Saab.pdf
## Images