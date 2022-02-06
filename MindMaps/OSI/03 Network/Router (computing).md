# Router (computing)
## [URL](https://en.wikipedia.org/wiki/Router_(computing)) - https://en.wikipedia.org/wiki/Router_(computing)
## Catagories
### All Wikipedia articles written in American English
### All articles with unsourced statements
### Articles with BNF identifiers
### Articles with GND identifiers
### Articles with LCCN identifiers
### Articles with short description
### Articles with unsourced statements from May 2017
### Commons category link is on Wikidata
### Computer networking
### Hardware routers
### Internet architecture
### Networking hardware
### Routers (computing)
### Server appliance
### Short description is different from Wikidata
### Use American English from June 2020
### Webarchive template wayback links
### "A router is a networking device that forwards data packets between computer networks. Routers perform the traffic directing functions on the Internet.  Data sent through the internet, such as a web page or email, is in the form of data packets.  A packet is typically forwarded from one router to another router through the networks that constitute an internetwork (e.g. the Internet) until it reaches its destination node.A router is connected to two or more data lines from different IP networks. When a data packet comes in on one of the lines, the router reads the network address information in the packet header to determine the ultimate destination.  Then, using information in its routing table or routing policy, it directs the packet to the next network on its journey. 
### The most familiar type of IP routers are home and small office routers that simply forward IP packets between the home computers and the Internet. More sophisticated routers, such as enterprise routers, connect large business or ISP networks up to the powerful core routers that forward data at high speed along the optical fiber lines of the Internet backbone.
## Operation  
### When multiple routers are used in interconnected networks, the routers can exchange information about destination addresses using a routing protocol. Each router builds up a routing table, a list of routes, between two computer systems on the interconnected networks.The software that runs the router is composed of two functional processing units that operate simultaneously, called planes: 
### Control plane: A router maintains a routing table that lists which route should be used to forward a data packet, and through which physical interface connection. It does this using internal pre-configured directives, called static routes, or by learning routes dynamically using a routing protocol. Static and dynamic routes are stored in the routing table. The control-plane logic then strips non-essential directives from the table and builds a forwarding information base (FIB) to be used by the forwarding plane. 
### Forwarding plane: This unit forwards the data packets between incoming and outgoing interface connections. It reads the header of each packet as it comes in, matches the destination to entries in the FIB supplied by the control plane, and directs the packet to the outgoing network specified in the FIB.
## Applications  

### A router may have interfaces for different types of physical layer connections, such as copper cables, fiber optic, or wireless transmission. It can also support different network layer transmission standards. Each network interface is used to enable data packets to be forwarded from one transmission system to another. Routers may also be used to connect two or more logical groups of computer devices known as subnets, each with a different network prefix. 
### Routers may provide connectivity within enterprises, between enterprises and the Internet, or between internet service providers' (ISPs') networks. The largest routers (such as the Cisco CRS-1 or Juniper PTX) interconnect the various ISPs, or may be used in large enterprise networks. Smaller routers usually provide connectivity for typical home and office networks. 
### All sizes of routers may be found inside enterprises. The most powerful routers are usually found in ISPs, academic and research facilities. Large businesses may also need more powerful routers to cope with ever-increasing demands of intranet data traffic. A hierarchical internetworking model for interconnecting routers in large networks is in common use.
## Access, core and distribution  

### Access routers, including small office/home office (SOHO) models, are located at home and customer sites such as branch offices that do not need hierarchical routing of their own. Typically, they are optimized for low cost. Some SOHO routers are capable of running alternative free Linux-based firmware like Tomato, OpenWrt, or DD-WRT.Distribution routers aggregate traffic from multiple access routers. Distribution routers are often responsible for enforcing quality of service across a wide area network (WAN), so they may have considerable memory installed, multiple WAN interface connections, and substantial onboard data processing routines. They may also provide connectivity to groups of file servers or other external networks.In enterprises, a core router may provide a collapsed backbone interconnecting the distribution tier routers from multiple buildings of a campus, or large enterprise locations. They tend to be optimized for high bandwidth, but lack some of the features of edge routers.
## Security  
### External networks must be carefully considered as part of the overall security strategy of the local network. A router may include a firewall, VPN handling, and other security functions, or they may be handled by separate devices. Routers also commonly perform network address translation which restricts connections initiated from external connections but is not recognized as a security feature by all experts. Some experts argue that open source routers are more secure and reliable than closed source routers because open-source routers allow mistakes to be quickly found and corrected.
## Routing different networks  
### Routers are also often distinguished on the basis of the network in which they operate. A router in a local area network (LAN) of a single organisation is called an interior router. A router that is operated in the Internet backbone is described as exterior router. While a router that connects a LAN with the Internet or a wide area network (WAN) is called a border router, or gateway router.
## Internet connectivity and internal use  
### Routers intended for ISP and major enterprise connectivity usually exchange routing information using the Border Gateway Protocol (BGP). RFC 4098 defines the types of BGP routers according to their functions: 
### Edge router (also called a provider edge router): Placed at the edge of an ISP network. The router uses Exterior Border Gateway Protocol (EBGP) to routers at other ISPs or large enterprise autonomous systems. 
### Subscriber edge router (also called a customer edge router): Located at the edge of the subscriber's network, it also uses EBGP to its provider's autonomous system. It is typically used in an (enterprise) organization. 
### Inter-provider border router: A BGP router for interconnecting ISPs that maintains BGP sessions with other BGP routers in ISP Autonomous Systems. 
### Core router: Resides within an Autonomous System as a backbone to carry traffic between edge routers. 
### Within an ISP: In the ISP's autonomous system, a router uses internal BGP to communicate with other ISP edge routers, other intranet core routers, or the ISP's intranet provider border routers. 
### Internet backbone: The Internet no longer has a clearly identifiable backbone, unlike its predecessor networks. See default-free zone (DFZ). The major ISPs' system routers make up what could be considered to be the current Internet backbone core. ISPs operate all four types of the BGP routers described here. An ISP core router is used to interconnect its edge and border routers. Core routers may also have specialized functions in virtual private networks based on a combination of BGP and Multi-Protocol Label Switching protocols. 
### Port forwarding: Routers are also used for port forwarding between private Internet-connected servers. 
### Voice, data, fax, and video processing routers: Commonly referred to as access servers or gateways, these devices are used to route and process voice, data, video and fax traffic on the Internet. Since 2005, most long-distance phone calls have been processed as IP traffic (VOIP) through a voice gateway. Use of access server-type routers expanded with the advent of the Internet, first with dial-up access and another resurgence with voice phone service. 
### Larger networks commonly use multilayer switches, with layer-3 devices being used to simply interconnect multiple subnets within the same security zone, and higher-layer switches when filtering, translation, load balancing, or other higher-level functions are required, especially between zones.
## History  

### The concept of an Interface computer was first proposed by Donald Davies for the NPL network in 1966. The same idea was conceived by Wesley Clark the following year for use in the ARPANET. Named Interface Message Processors (IMPs), these computers had fundamentally the same functionality as a router does today. The idea for a router (called gateway at the time) initially came about through an international group of computer networking researchers called the International Networking Working Group (INWG). Set up in 1972 as an informal group to consider the technical issues involved in connecting different networks, it became a subcommittee of the International Federation for Information Processing later that year. These gateway devices were different from most previous packet switching schemes in two ways. First, they connected dissimilar kinds of networks, such as serial lines and local area networks. Second, they were connectionless devices, which had no role in assuring that traffic was delivered reliably, leaving that function entirely to the hosts. This particular idea, the end-to-end principle, had been previously pioneered in the CYCLADES network. 
### The idea was explored in more detail, with the intention to produce a prototype system as part of two contemporaneous programs. One was the initial DARPA-initiated program, which created the TCP/IP architecture in use today. The other was a program at Xerox PARC to explore new networking technologies, which produced the PARC Universal Packet system; due to corporate intellectual property concerns it received little attention outside Xerox for years. Some time after early 1974, the first Xerox routers became operational. The first true IP router was developed by Ginny Strazisar at BBN, as part of that DARPA-initiated effort, during 1975\u20131976. By the end of 1976, three PDP-11-based routers were in service in the experimental prototype Internet.The first multiprotocol routers were independently created by staff researchers at MIT and Stanford in 1981 and both were also based on PDP-11s. Stanford's router program was by William Yeager and MIT's by Noel Chiappa. Virtually all networking now uses TCP/IP, but multiprotocol routers are still manufactured. They were important in the early stages of the growth of computer networking when protocols other than TCP/IP were in use. Modern routers that handle both IPv4 and IPv6 are multiprotocol but are simpler devices than ones processing AppleTalk, DECnet, IP, and Xerox protocols. 
### From the mid-1970s and in the 1980s, general-purpose minicomputers served as routers. Modern high-speed routers are network processors or highly specialized computers with extra hardware acceleration added to speed both common routing functions, such as packet forwarding, and specialized functions such as IPsec encryption. There is substantial use of Linux and Unix software-based machines, running open source routing code, for research and other applications. The Cisco IOS operating system was independently designed. Major router operating systems, such as Junos and NX-OS, are extensively modified versions of Unix software.
## Forwarding  

### The main purpose of a router is to connect multiple networks and forward packets destined either for directly attached networks or more remote networks. A router is considered a layer-3 device because its primary forwarding decision is based on the information in the layer-3 IP packet, specifically the destination IP address. When a router receives a packet, it searches its routing table to find the best match between the destination IP address of the packet and one of the addresses in the routing table. Once a match is found, the packet is encapsulated in the layer-2 data link frame for the outgoing interface indicated in the table entry. A router typically does not look into the packet payload, but only at the layer-3 addresses to make a forwarding decision, plus optionally other information in the header for hints on, for example, quality of service (QoS). For pure IP forwarding, a router is designed to minimize the state information associated with individual packets. Once a packet is forwarded, the router does not retain any historical information about the packet.The routing table itself can contain information derived from a variety of sources, such as a default or static routes that are configured manually, or dynamic entries from routing protocols where the router learns routes from other routers.  A default route is one that is used to route all traffic whose destination does not otherwise appear in the routing table; it is common \u2013  even necessary \u2013  in small networks, such as a home or small business where the default route simply sends all non-local traffic to the Internet service provider. The default route can be manually configured (as a static route); learned by dynamic routing protocols; or be obtained by DHCP.A router can run more than one routing protocol at a time, particularly if it serves as an autonomous system border router between parts of a network that run different routing protocols; if it does so, then redistribution may be used (usually selectively) to share information between the different protocols running on the same router.Besides deciding to which interface a packet is forwarded, which is handled primarily via the routing table, a router also has to manage congestion when packets arrive at a rate higher than the router can process. Three policies commonly used are tail drop, random early detection (RED), and weighted random early detection (WRED). Tail drop is the simplest and most easily implemented: the router simply drops new incoming packets once buffer space in the router is exhausted. RED probabilistically drops datagrams early when the queue exceeds a pre-configured portion of the buffer, until reaching a pre-determined maximum, when it drops all incoming packets, thus reverting to tail drop. WRED can be configured to drop packets more readily dependent on the type of traffic. 
### Another function a router performs is traffic classification and deciding which packet should be processed first. This is managed through QoS, which is critical when Voice over IP is deployed, so as not to introduce excessive latency.Yet another function a router performs is called policy-based routing where special rules are constructed to override the rules derived from the routing table when a packet forwarding decision is made.Some of the functions may be performed through an application-specific integrated circuit (ASIC) to avoid overhead of scheduling CPU time to process the packets. Others may have to be performed through the CPU as these packets need special attention that cannot be handled by an ASIC.
## See also  
### Mobile broadband modem 
### Modem 
### Residential gateway 
### Switch virtual interface 
### Wireless router
## Notes 
## References 
## External links "
## Links
### ADSL
### ARPANET
### Access servers
### Alcatel-Lucent
### AlliedWare Plus
### American English
### Application-specific integrated circuit
### Australian English
### Autonomous system (Internet)
### B.A.T.M.A.N.
### BBN Technologies
### Babel (protocol)
### Bird Internet routing daemon
### Border Gateway Protocol
### British English
### CYCLADES
### Captive portal
### Cisco CRS-1
### Cisco IOS
### Cisco NX-OS
### Cisco Press
### Closed source
### Collapsed backbone
### Comparison of firewalls
### Computer network
### Connectionless
### Control plane
### Core router
### DARPA
### DD-WRT
### DHCP
### DSL router
### Data link layer
### Data packet
### Default-free zone
### Default route
### Doi (identifier)
### Donald Davies
### Dynamic DNS
### Dynamic routing
### Email
### End-to-end principle
### Endian Firewall
### Ethernet
### Exterior Border Gateway Protocol
### ExtremeXOS
### Extreme Networks
### FRRouting
### Firewall (computing)
### Floppyfw
### Forwarding information base
### Forwarding plane
### FreeBSD
### Free and open-source software
### Fritz!Box
### GNU Zebra
### Gateway (telecommunications)
### Gateway router
### Ginny Strazisar
### Hardware acceleration
### Header (computing)
### Hierarchical internetworking model
### Hierarchical routing
### Host (network)
### Huawei
### IPFire
### IP network
### IP packet (disambiguation)
### IP routing
### IPsec
### ISBN (identifier)
### Interface Message Processor
### International Federation for Information Processing
### International Networking Working Group
### Internet
### Internet Protocol
### Internet backbone
### Internet service provider
### Internetwork
### Intranet
### Juniper Networks
### Junos
### Junos OS
### LEDE
### Latency (audio)
### Layer-3
### LibreCMC
### Linux
### Linux kernel
### List of router and firewall distributions
### List of router firmware projects
### Load balancing (computing)
### Local area network
### M0n0wall
### Massachusetts Institute of Technology
### MikroTik
### Minicomputer
### Mobile broadband modem
### Modem
### Multi-Protocol Label Switching
### Multilayer switch
### Mumble (software)
### NPL network
### NX-OS
### National Security Agency
### Neighbornode
### Network address
### Network address translation
### Network layer
### Network operating system
### Network prefix
### Network processor
### Network switch
### Networking device
### Node (networking)
### Noel Chiappa
### OPNsense
### Open-source software
### OpenBGPD
### OpenOSPFD
### OpenWrt
### Operating system
### Optical fiber
### Oxford English Dictionary
### Oxford University Press
### PARC Universal Packet
### PDP-11
### Packet forwarding
### Packet switching
### PfSense
### Physical layer
### Policy-based routing
### Port forwarding
### Proprietary software
### Quagga (software)
### Quality of service
### RFC (identifier)
### Random early detection
### Residential gateway
### Router (woodworking)
### Routing
### Routing policy
### Routing protocol
### Routing table
### Serial line
### Small office/home office
### SmoothWall
### Stanford University
### State (computer science)
### Static route
### Subnetwork
### Switch virtual interface
### TCP/IP
### Tail drop
### Telephone socket
### Tomato (firmware)
### Tor (network)
### Traffic classification
### Ubiquiti Networks
### Unix
### VOIP
### Virtual private network
### Voice over IP
### VyOS
### Vyatta
### Wayback Machine
### Web page
### Weighted random early detection
### Wesley A. Clark
### Wide area network
### William Yeager
### Wireless
### Wireless router
### XORP
### Xerox PARC
### Zeroshell
## References
### [Reference](http://www.packet.cc/files/FlowPaper/NextGenerationofIP-FlowRouting.htm) - http://www.packet.cc/files/FlowPaper/NextGenerationofIP-FlowRouting.htm
### [Reference](http://www.packet.cc/files/arpanet-computernet.html) - http://www.packet.cc/files/arpanet-computernet.html
### [Reference](http://www.businesswire.com/news/home/20151014005564/en) - http://www.businesswire.com/news/home/20151014005564/en
### [Reference](http://www.ciscopress.com/articles/article.asp?p=2180210&seqNum=4) - http://www.ciscopress.com/articles/article.asp?p=2180210&seqNum=4
### [Reference](http://social.technet.microsoft.com/wiki/contents/articles/windows-home-server-router-setup.aspx) - http://social.technet.microsoft.com/wiki/contents/articles/windows-home-server-router-setup.aspx
### [Reference](http://my-technet.com/index.php/cisco/setting-up-netflow-on-cisco-routers/) - http://my-technet.com/index.php/cisco/setting-up-netflow-on-cisco-routers/
### [Reference](http://www.networkworld.com/supp/2006/anniversary/032706-routerman.html?t5) - http://www.networkworld.com/supp/2006/anniversary/032706-routerman.html?t5
### [Reference](http://www.tcpipguide.com/free/t_OverviewOfKeyRoutingProtocolConceptsArchitecturesP.htm) - http://www.tcpipguide.com/free/t_OverviewOfKeyRoutingProtocolConceptsArchitecturesP.htm
### [Reference](http://www.techrepublic.com/article/cisco-administration-101-what-you-need-to-know-about-default-routes) - http://www.techrepublic.com/article/cisco-administration-101-what-you-need-to-know-about-default-routes
### [Reference](http://www.telecomsportal.com/Assets_papers/Routers_&_Netman/Ironbridge_Virt_Bbone_Route.pdf) - http://www.telecomsportal.com/Assets_papers/Routers_&_Netman/Ironbridge_Virt_Bbone_Route.pdf
### [Reference](http://www.safecomputing.umich.edu/protect-personal/download/nat_security.pdf) - http://www.safecomputing.umich.edu/protect-personal/download/nat_security.pdf
### [Reference](http://www.juniper.net/techpubs/qrc/m160-qrc.pdf) - http://www.juniper.net/techpubs/qrc/m160-qrc.pdf
### [Reference](http://doi.org/10.17487%2FRFC3654) - http://doi.org/10.17487%2FRFC3654
### [Reference](http://doi.org/10.17487%2FRFC4098) - http://doi.org/10.17487%2FRFC4098
### [Reference](http://ieeexplore.ieee.org/iel5/8159/23818/01092259.pdf) - http://ieeexplore.ieee.org/iel5/8159/23818/01092259.pdf
### [Reference](http://ieeexplore.ieee.org/iel5/8159/23925/01094684.pdf) - http://ieeexplore.ieee.org/iel5/8159/23925/01094684.pdf
### [Reference](http://ieeexplore.ieee.org/iel5/85/33687/01603444.pdf) - http://ieeexplore.ieee.org/iel5/85/33687/01603444.pdf
### [Reference](http://www.ithistory.org/honor-roll/ms-ginny-strazisar) - http://www.ithistory.org/honor-roll/ms-ginny-strazisar
### [Reference](https://www.ciscopress.com/articles/article.asp?p=2202410&seqNum=4) - https://www.ciscopress.com/articles/article.asp?p=2202410&seqNum=4
### [Reference](https://www.examcollection.com/certification-training/network-plus-soho-network-requirements-planning-and-implementation.html) - https://www.examcollection.com/certification-training/network-plus-soho-network-requirements-planning-and-implementation.html
### [Reference](https://ispfamily.com/how-do-wifi-extenders-work/) - https://ispfamily.com/how-do-wifi-extenders-work/
### [Reference](https://oed.com/search?searchType=dictionary&q=router) - https://oed.com/search?searchType=dictionary&q=router
### [Reference](https://www.oed.com/public/login/loggingin#withyourlibrary) - https://www.oed.com/public/login/loggingin#withyourlibrary
### [Reference](https://docs.oracle.com/cd/E23823_01/html/816-4554/gcvjj.html) - https://docs.oracle.com/cd/E23823_01/html/816-4554/gcvjj.html
### [Reference](https://catalogue.bnf.fr/ark:/12148/cb135602665) - https://catalogue.bnf.fr/ark:/12148/cb135602665
### [Reference](https://data.bnf.fr/ark:/12148/cb135602665) - https://data.bnf.fr/ark:/12148/cb135602665
### [Reference](https://id.loc.gov/authorities/subjects/sh99004539) - https://id.loc.gov/authorities/subjects/sh99004539
### [Reference](https://d-nb.info/gnd/4298524-9) - https://d-nb.info/gnd/4298524-9
### [Reference](https://web.archive.org/web/20080911135408/http://ieeexplore.ieee.org/iel5/8159/23925/01094684.pdf) - https://web.archive.org/web/20080911135408/http://ieeexplore.ieee.org/iel5/8159/23925/01094684.pdf
### [Reference](https://web.archive.org/web/20101220111345/http://tcpipguide.com/free/t_OverviewOfKeyRoutingProtocolConceptsArchitecturesP.htm) - https://web.archive.org/web/20101220111345/http://tcpipguide.com/free/t_OverviewOfKeyRoutingProtocolConceptsArchitecturesP.htm
### [Reference](https://web.archive.org/web/20101222175405/http://social.technet.microsoft.com/wiki/contents/articles/windows-home-server-router-setup.aspx) - https://web.archive.org/web/20101222175405/http://social.technet.microsoft.com/wiki/contents/articles/windows-home-server-router-setup.aspx
### [Reference](https://web.archive.org/web/20110714141500/http://my-technet.com/index.php/cisco/setting-up-netflow-on-cisco-routers/) - https://web.archive.org/web/20110714141500/http://my-technet.com/index.php/cisco/setting-up-netflow-on-cisco-routers/
### [Reference](https://web.archive.org/web/20110716203325/http://www.telecomsportal.com/Assets_papers/Routers_&_Netman/Ironbridge_Virt_Bbone_Route.pdf) - https://web.archive.org/web/20110716203325/http://www.telecomsportal.com/Assets_papers/Routers_&_Netman/Ironbridge_Virt_Bbone_Route.pdf
### [Reference](https://web.archive.org/web/20110920213215/http://www.juniper.net/techpubs/qrc/m160-qrc.pdf) - https://web.archive.org/web/20110920213215/http://www.juniper.net/techpubs/qrc/m160-qrc.pdf
### [Reference](https://web.archive.org/web/20130605195255/http://www.networkworld.com/supp/2006/anniversary/032706-routerman.html?t5) - https://web.archive.org/web/20130605195255/http://www.networkworld.com/supp/2006/anniversary/032706-routerman.html?t5
### [Reference](https://web.archive.org/web/20131617133200/http://www.techrepublic.com/article/cisco-administration-101-what-you-need-to-know-about-default-routes/) - https://web.archive.org/web/20131617133200/http://www.techrepublic.com/article/cisco-administration-101-what-you-need-to-know-about-default-routes/
### [Reference](https://web.archive.org/web/20141018184244/http://www.safecomputing.umich.edu/protect-personal/download/nat_security.pdf) - https://web.archive.org/web/20141018184244/http://www.safecomputing.umich.edu/protect-personal/download/nat_security.pdf
### [Reference](https://web.archive.org/web/20150404030549/http://www.packet.cc/files/FlowPaper/NextGenerationofIP-FlowRouting.htm) - https://web.archive.org/web/20150404030549/http://www.packet.cc/files/FlowPaper/NextGenerationofIP-FlowRouting.htm
### [Reference](https://web.archive.org/web/20151020003515/http://www.businesswire.com/news/home/20151014005564/en) - https://web.archive.org/web/20151020003515/http://www.businesswire.com/news/home/20151014005564/en
### [Reference](https://web.archive.org/web/20151027133937/http://www.ciscopress.com/articles/article.asp?p=2180210&seqNum=4) - https://web.archive.org/web/20151027133937/http://www.ciscopress.com/articles/article.asp?p=2180210&seqNum=4
### [Reference](https://web.archive.org/web/20160303172753/http://www.pbs.org/cringely/pulpit/1998/pulpit_19981210_000593.html) - https://web.archive.org/web/20160303172753/http://www.pbs.org/cringely/pulpit/1998/pulpit_19981210_000593.html
### [Reference](https://web.archive.org/web/20160324032800/http://www.packet.cc/files/arpanet-computernet.html) - https://web.archive.org/web/20160324032800/http://www.packet.cc/files/arpanet-computernet.html
### [Reference](https://web.archive.org/web/20171201034131/http://www.ithistory.org/honor-roll/ms-ginny-strazisar) - https://web.archive.org/web/20171201034131/http://www.ithistory.org/honor-roll/ms-ginny-strazisar
### [Reference](https://datatracker.ietf.org/doc/html/rfc3654) - https://datatracker.ietf.org/doc/html/rfc3654
### [Reference](https://datatracker.ietf.org/doc/html/rfc4098) - https://datatracker.ietf.org/doc/html/rfc4098
### [Reference](https://www.pbs.org/cringely/pulpit/1998/pulpit_19981210_000593.html) - https://www.pbs.org/cringely/pulpit/1998/pulpit_19981210_000593.html
### [Reference](https://www.wikidata.org/wiki/Q5318#identifiers) - https://www.wikidata.org/wiki/Q5318#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/1/18/ARPANET_first_router_2.jpg) - https://upload.wikimedia.org/wikipedia/commons/1/18/ARPANET_first_router_2.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/8/85/ASR9006.jpg) - https://upload.wikimedia.org/wikipedia/commons/8/85/ASR9006.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/2/21/Adsl_connections.jpg) - https://upload.wikimedia.org/wikipedia/commons/2/21/Adsl_connections.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/9/93/Modem-and-router-units.jpg) - https://upload.wikimedia.org/wikipedia/commons/9/93/Modem-and-router-units.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/a/ad/OpenWRT_8.09.1_LuCI_screenshot.png) - https://upload.wikimedia.org/wikipedia/commons/a/ad/OpenWRT_8.09.1_LuCI_screenshot.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/df/Wikibooks-logo-en-noslogan.svg) - https://upload.wikimedia.org/wikipedia/commons/d/df/Wikibooks-logo-en-noslogan.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/9/99/Wiktionary-logo-en-v2.svg) - https://upload.wikimedia.org/wikipedia/commons/9/99/Wiktionary-logo-en-v2.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg) - https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg