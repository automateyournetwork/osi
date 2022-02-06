# Network switch
## [URL](https://en.wikipedia.org/wiki/Network_switch) - https://en.wikipedia.org/wiki/Network_switch
## Catagories
### All Wikipedia articles written in American English
### Articles with short description
### CS1 maint: bot: original URL status unknown
### Commons category link is on Wikidata
### Ethernet
### Networking hardware
### Short description is different from Wikidata
### Use American English from March 2019
### "A network switch (also called switching hub, bridging hub, and, by the IEEE, MAC bridge) is networking hardware that connects devices on a computer network by using packet switching to receive and forward data to the destination device. 
### A network switch is a multiport network bridge that uses MAC addresses to forward data at the data link layer (layer 2) of the OSI model. Some switches can also forward data at the network layer (layer 3) by additionally incorporating routing functionality. Such switches are commonly known as layer-3 switches or multilayer switches.Switches for Ethernet are the most common form of network switch. The first MAC Bridge was invented in 1983 by Mark Kempf, an engineer in the Networking Advanced Development group of Digital Equipment Corporation. The first 2 port Bridge product (LANBridge 100) was introduced by that company shortly after.  The company subsequently produced multi-port switches for both Ethernet and FDDI such as GigaSwitch.  Digital decided to license its MAC Bridge patent in a royalty-free, non-discriminatory basis that allowed IEEE standardization.  This permitted a number of other companies to produce multi-port switches, including Kalpana. Ethernet was initially a shared-access medium, but the introduction of the MAC bridge began its transformation into its most-common point-to-point form without a collision domain.  Switches also exist for other types of networks including Fibre Channel, Asynchronous Transfer Mode, and InfiniBand. 
### Unlike repeater hubs, which broadcast the same data out of each port and let the devices pick out the data addressed to them, a network switch learns the identities of connected devices and then only forwards data to the port connected to the device to which it is addressed.
## Overview  

### A switch is a device in a computer network that connects other devices together. Multiple data cables are plugged into a switch to enable communication between different networked devices. Switches manage the flow of data across a network by transmitting a received network packet only to the one or more devices for which the packet is intended. Each networked device connected to a switch can be identified by its network address, allowing the switch to direct the flow of traffic maximizing the security and efficiency of the network. 
### A switch is more intelligent than an Ethernet hub, which simply retransmits packets out of every port of the hub except the port on which the packet was received, unable to distinguish different recipients, and achieving an overall lower network efficiency. 
### An Ethernet switch operates at the data link layer (layer 2) of the OSI model to create a separate collision domain for each switch port. Each device connected to a switch port can transfer data to any of the other ports at any time and the transmissions will not interfere. Because broadcasts are still being forwarded to all connected devices by the switch, the newly formed network segment continues to be a broadcast domain. Switches may also operate at higher layers of the OSI model, including the network layer and above. A device that also operates at these higher layers is known as a multilayer switch. 
### Segmentation involves the use of a switch to split a larger collision domain into smaller ones in order to reduce collision probability and to improve overall network throughput. In the extreme case (i.e. micro-segmentation), each device is located on a dedicated switch port. In contrast to an Ethernet hub, there is a separate collision domain on each of the switch ports. This allows computers to have dedicated bandwidth on point-to-point connections to the network and also to run in full-duplex mode. Full-duplex mode has only one transmitter and one receiver per collision domain, making collisions impossible. 
### The network switch plays an integral role in most modern Ethernet local area networks (LANs). Mid-to-large sized LANs contain a number of linked managed switches. Small office/home office (SOHO) applications typically use a single switch, or an all-purpose device such as a residential gateway to access small office/home broadband services such as DSL or cable Internet. In most of these cases, the end-user device contains a router and components that interface to the particular physical broadband technology. User devices may also include a telephone interface for Voice over IP (VoIP).
## Role in a network  
### Switches are most commonly used as the network connection point for hosts at the edge of a network. In the hierarchical internetworking model and similar network architectures, switches are also used deeper in the network to provide connections between the switches at the edge. 
### In switches intended for commercial use, built-in or modular interfaces make it possible to  connect different types  of  networks, including Ethernet, Fibre Channel, RapidIO, ATM, ITU-T G.hn and 802.11. This connectivity can be at any of the layers mentioned. While the layer-2 functionality is adequate for bandwidth-shifting within one technology, interconnecting technologies such as Ethernet and Token Ring is performed more easily at layer 3 or via routing. Devices that interconnect at the layer 3 are traditionally called routers.Where there is a need for a great deal of analysis of network performance and security, switches may be connected between WAN routers as places for analytic modules. Some vendors provide firewall, network intrusion detection, and performance analysis modules that can plug into switch ports. Some of these functions may be on combined modules.Through port mirroring, a switch can create a mirror image of data that can go to an external device such as intrusion detection systems and packet sniffers. 
### A modern switch may implement power over Ethernet (PoE), which avoids the need for attached devices, such as a VoIP phone or wireless access point, to have a separate power supply. Since switches can have redundant power circuits connected to uninterruptible power supplies, the connected device can continue operating even when regular office power fails.
## Bridging  

### Modern commercial switches primarily use Ethernet interfaces. The core function of an Ethernet switch is to provide multiple ports of layer-2 bridging. Layer-1 functionality is required in all switches in support of the higher layers. Many switches also perform operations at other layers. A device capable of more than bridging is known as a multilayer switch. 
### A layer 2 network device is a multiport device that uses hardware addresses (MAC addresses) to process and forward data at the data link layer (layer 2). 
### A switch operating as a network bridge may interconnect otherwise separate layer 2 networks. The bridge learns the MAC address of each connected device. Bridges also buffer an incoming packet and adapt the transmission speed to that of the outgoing port. While there are specialized applications, such as storage area networks, where the input and output interfaces are the same bandwidth, this is not always the case in general LAN applications. In LANs, a switch used for end-user access typically concentrates lower bandwidth and uplinks into a higher bandwidth. 
### Interconnects between switches may be regulated using the spanning tree protocol (STP) that disables links so that the resulting local area network is a tree without switching loops. In contrast to routers, spanning tree bridges must have topologies with only one active path between two points. Shortest path bridging and TRILL (TRansparent Interconnection of Lots of Links) are layer 2 alternatives to STP which allow all paths to be active with multiple equal cost paths.
## Types 
## Form factors  
### Switches are available in many form factors, including stand-alone, desktop units which are typically intended to be used in a home or office environment outside a wiring closet; rack-mounted switches for use in an equipment rack or an enclosure; DIN rail mounted for use in industrial environments; and small installation switches, mounted into a cable duct, floor box or communications tower, as found, for example, in fiber to the office infrastructures. 
### Rack-mounted switches may be standalone units, stackable switches or large chassis units with swappable line cards.
## Configuration options  
### Unmanaged switches have no configuration interface or options. They are plug and play. They are typically the least expensive switches, and therefore often used in a small office/home office environment. Unmanaged switches can be desktop or rack mounted. 
### Managed switches have one or more methods to modify the operation of the switch. Common management methods include: a command-line interface (CLI) accessed via serial console, telnet or Secure Shell, an embedded Simple Network Management Protocol (SNMP) agent allowing management from a remote console or management station, or a web interface for management from a web browser. Examples of configuration changes that one can do from a managed switch include: enabling features such as Spanning Tree Protocol or port mirroring, setting port bandwidth, creating or modifying virtual LANs (VLANs), etc. Two sub-classes of managed switches are smart and enterprise managed switches. 
### Smart switches (aka intelligent switches) are managed switches with a limited set of management features. Likewise, \"web-managed\" switches are switches that fall into a market niche between unmanaged and managed. For a price much lower than a fully managed switch they provide a web interface (and usually no CLI access) and allow configuration of basic settings, such as VLANs, port-bandwidth and duplex. 
### Enterprise managed switches (aka managed switches) have a full set of management features, including CLI, SNMP agent, and web interface. They may have additional features to manipulate configurations, such as the ability to display, modify, backup and restore configurations. Compared with smart switches, enterprise switches have more features that can be customized or optimized and are generally more expensive than smart switches. Enterprise switches are typically found in networks with a larger number of switches and connections, where centralized management is a significant savings in administrative time and effort. A stackable switch is a type of an enterprise-managed switch.
## Typical management features  

### Enable and disable ports 
### Link bandwidth and duplex settings 
### Quality of service configuration and monitoring 
### MAC filtering and other access control list features 
### Configuration of Spanning Tree Protocol (STP) and Shortest Path Bridging (SPB) features 
### Simple Network Management Protocol (SNMP) monitoring of device and link health 
### Port mirroring for monitoring traffic and troubleshooting 
### Link aggregation configuration to set up multiple ports for the same connection to achieve higher data transfer rates and reliability 
### VLAN configuration and port assignments including IEEE 802.1Q tagging 
### Network Access Control features such as IEEE 802.1X 
### IGMP snooping for control of multicast traffic
## Traffic monitoring  
### It is difficult to monitor traffic that is bridged using a switch because only the sending and receiving ports can see the traffic. 
### Methods that are specifically designed to allow a network analyst to monitor traffic include: 

### Port mirroring \u2013  the switch sends a copy of network packets to a monitoring network connection. 
### SMON \u2013  \"Switch Monitoring\" is described by RFC 2613 and is a protocol for controlling facilities such as port mirroring. 
### RMON 
### sFlowThese monitoring features are rarely present on consumer-grade switches. Other monitoring methods include connecting a layer-1 hub or network tap between the monitored device and its switch port.
## See also 
## Notes 
## References 
## External links  
### What to consider when buying an Ethernet Switch"
## Links
### 19-inch rack
### 3Com
### 802.11
### Access control list
### Asynchronous Transfer Mode
### Avaya
### Bit rate
### Broadband
### Broadcast domain
### Broadcasting (networking)
### Cable Internet
### Category 6 cable
### Cisco Systems
### Cisco small business
### Collision domain
### Command-line interface
### Computer network
### Console server
### D-Link
### DIN rail
### Data link layer
### Digital Equipment Corporation
### Digital subscriber line
### Duplex (telecommunications)
### ERS 3500 and ERS 2500 series
### Enclosure (electrical)
### Energy-Efficient Ethernet
### Ethernet
### Ethernet hub
### Fiber Distributed Data Interface
### Fiber to the office
### Fibre Channel
### Fibre Channel switch
### Firewall (computing)
### Full duplex
### Fully switched network
### G.hn
### Gigabit Ethernet
### Half duplex
### Hierarchical internetworking model
### IBM
### IEEE
### IEEE 802.1Q
### IEEE 802.1X
### IGMP snooping
### ISBN (identifier)
### ITU-T
### Industrial Ethernet
### InfiniBand
### Intrusion detection
### Intrusion detection system
### Kalpana (company)
### Link aggregation
### Load-balanced switch
### Local area network
### MAC address
### MAC filtering
### Modular computer network switch
### Multilayer switch
### Network Access Control
### Network address
### Network bridge
### Network layer
### Network packet
### Network segment
### Network tap
### Networking hardware
### OSI model
### Packet sniffer
### Packet switch
### Packet switching
### Patch cable
### Patch panel
### Plug and play
### Port mirroring
### Power over Ethernet
### Quality of service
### RMON
### RapidIO
### Repeater hub
### Residential gateway
### Router (computing)
### Routing
### SFlow
### SOHO network
### Secure Shell
### Serial console
### Shared medium
### Shortest Path Bridging
### Shortest path bridging
### Simple Network Management Protocol
### Small office/home office
### Spanning Tree Protocol
### Spanning tree protocol
### Stackable switch
### Switching loop
### TRILL
### Telephone exchange
### Telnet
### Token Ring
### Tree (graph theory)
### Turing switch
### Uninterruptible power supply
### Uplink
### Virtual LAN
### VoIP phone
### Voice over IP
### Web browser
### Wide area network
### Wireless access point
### Wiring closet
## References
### [Reference](http://www.3com.com/products/en_US/detail.jsp?tab=features&sku=3C17546&pathtype=purchase3Com) - http://www.3com.com/products/en_US/detail.jsp?tab=features&sku=3C17546&pathtype=purchase3Com
### [Reference](http://www.ccontrols.com/pdf/Extv3n3.pdf) - http://www.ccontrols.com/pdf/Extv3n3.pdf
### [Reference](http://cisco.com/en/US/products/hw/modules/ps2706/ps4452/index.html) - http://cisco.com/en/US/products/hw/modules/ps2706/ps4452/index.html
### [Reference](http://cisco.com/en/US/products/hw/modules/ps2706/ps5058/index.html) - http://cisco.com/en/US/products/hw/modules/ps2706/ps5058/index.html
### [Reference](http://blogs.cisco.com/smallbusiness/understanding-the-different-types-of-ethernet-switches/) - http://blogs.cisco.com/smallbusiness/understanding-the-different-types-of-ethernet-switches/
### [Reference](http://www.cisco.com/web/about/ac123/ac147/archived_issues/ipj_1-2/switch_evolution.html) - http://www.cisco.com/web/about/ac123/ac147/archived_issues/ipj_1-2/switch_evolution.html
### [Reference](http://www.ciscopress.com/articles/article.asp?p=2181836&seqNum=5) - http://www.ciscopress.com/articles/article.asp?p=2181836&seqNum=5
### [Reference](http://www.redbooks.ibm.com/redpapers/pdfs/redp0168.pdf#page=23) - http://www.redbooks.ibm.com/redpapers/pdfs/redp0168.pdf#page=23
### [Reference](http://www.networkcomputing.com/1119/1119f1products_5.html) - http://www.networkcomputing.com/1119/1119f1products_5.html
### [Reference](http://www.techpowerup.com/165594/IEEE-Approves-New-IEEE-802.1aq-Shortest-Path-Bridging-Standard.html) - http://www.techpowerup.com/165594/IEEE-Approves-New-IEEE-802.1aq-Shortest-Path-Bridging-Standard.html
### [Reference](http://meetings.apnic.net/__data/assets/pdf_file/0012/32007/APRICOT_SPB_Overview.pdf) - http://meetings.apnic.net/__data/assets/pdf_file/0012/32007/APRICOT_SPB_Overview.pdf
### [Reference](http://www.ietf.org/rfc/rfc2819.txt) - http://www.ietf.org/rfc/rfc2819.txt
### [Reference](https://logrhythm.com/blog/how-to-build-a-miniature-network-monitor-device/) - https://logrhythm.com/blog/how-to-build-a-miniature-network-monitor-device/
### [Reference](https://mergie.com/computers/hardware/network/buying-a-network-ethernet-switch/) - https://mergie.com/computers/hardware/network/buying-a-network-ethernet-switch/
### [Reference](https://web.archive.org/web/20031007183603/http://www.checkpoint.com/support/technical/online_ug/firewall-14.0/config.htm) - https://web.archive.org/web/20031007183603/http://www.checkpoint.com/support/technical/online_ug/firewall-14.0/config.htm
### [Reference](https://web.archive.org/web/20071213185114/http://www.hp.com/rnd/products/switches/ProCurve_Switch_1800_Series/specs.htm) - https://web.archive.org/web/20071213185114/http://www.hp.com/rnd/products/switches/ProCurve_Switch_1800_Series/specs.htm
### [Reference](https://web.archive.org/web/20100105152318/http://www.networkcomputing.com/1119/1119f1products_5.html) - https://web.archive.org/web/20100105152318/http://www.networkcomputing.com/1119/1119f1products_5.html
### [Reference](https://web.archive.org/web/20130515115628/http://meetings.apnic.net/__data/assets/pdf_file/0012/32007/APRICOT_SPB_Overview.pdf) - https://web.archive.org/web/20130515115628/http://meetings.apnic.net/__data/assets/pdf_file/0012/32007/APRICOT_SPB_Overview.pdf
### [Reference](https://web.archive.org/web/20150924111914/http://www.redbooks.ibm.com/redpapers/pdfs/redp0168.pdf#page=23) - https://web.archive.org/web/20150924111914/http://www.redbooks.ibm.com/redpapers/pdfs/redp0168.pdf#page=23
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/b/bc/19-inch_rackmount_Ethernet_switches_and_patch_panels.jpg) - https://upload.wikimedia.org/wikipedia/commons/b/bc/19-inch_rackmount_Ethernet_switches_and_patch_panels.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/e/e4/24-port_3Com_switch.JPG) - https://upload.wikimedia.org/wikipedia/commons/e/e4/24-port_3Com_switch.JPG
### [Image](https://upload.wikimedia.org/wikipedia/commons/b/b9/2550T-PWR-Front.jpg) - https://upload.wikimedia.org/wikipedia/commons/b/b9/2550T-PWR-Front.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/7/74/5_Port_Gigabit_Netzwerk-Switch_TL-SG1005D_01.jpg) - https://upload.wikimedia.org/wikipedia/commons/7/74/5_Port_Gigabit_Netzwerk-Switch_TL-SG1005D_01.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/7/7f/Cisco_small_business_SG300-28_28-port_Gigabit_Ethernet_rackmount_switch.jpg) - https://upload.wikimedia.org/wikipedia/commons/7/7f/Cisco_small_business_SG300-28_28-port_Gigabit_Ethernet_rackmount_switch.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/2/21/Internals_of_a_Cisco_small_business_SG300-28_28-port_Gigabit_Ethernet_rackmount_switch.jpg) - https://upload.wikimedia.org/wikipedia/commons/2/21/Internals_of_a_Cisco_small_business_SG300-28_28-port_Gigabit_Ethernet_rackmount_switch.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/d5/Smartswitch6000.jpg) - https://upload.wikimedia.org/wikipedia/commons/d/d5/Smartswitch6000.jpg
### [Image](https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg) - https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg