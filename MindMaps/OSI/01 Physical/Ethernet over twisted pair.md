# Ethernet over twisted pair
## [URL](https://en.wikipedia.org/wiki/Ethernet_over_twisted_pair) - https://en.wikipedia.org/wiki/Ethernet_over_twisted_pair
## Catagories
### All Wikipedia articles written in American English
### All articles with unsourced statements
### Articles with short description
### Articles with unsourced statements from August 2011
### Articles with unsourced statements from February 2011
### Ethernet cables
### Local loop
### Physical layer protocols
### Short description matches Wikidata
### Use American English from March 2019
### "Ethernet over twisted-pair technologies use twisted-pair cables for the physical layer of an Ethernet computer network. They are a subset of all Ethernet physical layers. 
### Early Ethernet used various grades of coaxial cable, but in 1984, StarLAN showed the potential of simple unshielded twisted pair. This led to the development of 10BASE-T and its successors 100BASE-TX, 1000BASE-T and 10GBASE-T, supporting speeds of 10 and 100 megabit per second, then 1 and 10 gigabit per second respectively.Two new variants of 10 megabit per second Ethernet over a single twisted pair, known as 10BASE-T1S and 10BASE-T1L, were standardized in IEEE Std 802.3cg-2019.    10BASE-T1S has its origins in the automotive industry and may be useful in other short-distance applications where substantial electrical noise is present.  10BASE-T1L is a long-distance Ethernet, supporting connections up to 1 km in length.   Both of these standards are finding applications implementing the Internet of things. 
### The earlier standards use 8P8C modular connectors, and supported cable standards range from Category 3 to Category 8. These cables typically have four pairs of wires for each connection, although early Ethernet used only two of the pairs.   Unlike the earlier -T standards, the -T1 interfaces were designed to operate over a single pair of conductors and introduce the use of two new connectors referred to as IEC 63171-1 and IEC 63171-6.
## History  
### The first two early designs of twisted-pair networking were StarLAN, standardized by the IEEE Standards Association as IEEE 802.3e in 1986, at one megabit per second, and LattisNet, developed in January 1987, at 10 megabit per second. Both were developed before the 10BASE-T standard (published in 1990 as IEEE 802.3i) and used different signalling, so they were not directly compatible with it.In 1988, AT&T released StarLAN 10, named for working at 10 Mbit/s.  The StarLAN 10 signalling was used as the basis of 10BASE-T, with the addition of link beat to quickly indicate connection status.Using twisted-pair cabling in a star topology addressed several weaknesses of the previous Ethernet standards: 

### Twisted-pair cables were already in use for telephone service and were already present in many office buildings, lowering the overall cost of deployment 
### The centralized star topology was also already often in use for telephone service cabling, as opposed to the bus topology required by earlier Ethernet standards 
### Using point-to-point links was less prone to failure and greatly simplified troubleshooting compared to a shared bus 
### Exchanging cheap repeater hubs for more advanced switching hubs provided a viable upgrade path 
### Mixing different speeds in a single network became possible with the arrival of Fast Ethernet 
### Depending on cable grades, subsequent upgrading to Gigabit Ethernet or faster could be accomplished by replacing the network switchesAlthough 10BASE-T is rarely used as a normal-operation signaling rate today, it is still in wide use with network interface controllers in Wake-on-LAN power-down mode and for special, low-power, low-bandwidth applications. 10BASE-T is still supported on most twisted-pair Ethernet ports with up to Gigabit Ethernet speed.
## Naming  

### The common names for the standards derive from aspects of the physical media. The leading number (10 in 10BASE-T) refers to the transmission speed in Mbit/s. BASE denotes that baseband transmission is used. The T designates twisted-pair cable. Where there are several standards for the same transmission speed, they are distinguished by a letter or digit following the T, such as TX or T4, referring to the encoding method and number of lanes.
## Cabling  

### Most Ethernet cables are wired \"straight-through\" (pin 1 to pin 1, pin 2 to pin 2, and so on). In some instances the \"crossover\" form (receive to transmit and transmit to receive) may still be required. 
### Cables for Ethernet may be wired to either the T568A or T568B termination standards at both ends of the cable. Since these standards differ only in that they swap the positions of the two pairs used for transmitting and receiving, a cable with T568A wiring at one end and T568B wiring at the other results in a crossover cable. 
### A 10BASE-T or 100BASE-TX host uses a connector wiring called medium dependent interfaces (MDI), transmitting on pins 1 and 2 and receiving on pins 3 and 6 to a network device. An infrastructure node (a hub or a switch) accordingly uses a connector wiring called MDI-X, transmitting on pins 3 and 6 and receiving on pins 1 and 2. These ports are connected using a straight-through cable so each transmitter talks to the receiver on the other end of the cable. 
### Nodes can have two types of ports: MDI (uplink port) or MDI-X (regular port, 'X' for internal crossover). Hubs and switches have regular ports. Routers, servers and end hosts (e.g. personal computers) have uplink ports. When two nodes having the same type of ports need to be connected, a crossover cable may be required, especially for older equipment. Connecting nodes having different types of ports (i.e., MDI to MDI-X and vice versa) requires a straight-through cable. Thus connecting an end host to a hub or switch requires a straight-through cable. Some older switches and hubs provided a button to allow a port to act as either a normal (regular) or an uplink port, i.e. using MDI-X or MDI pinout, respectively. 
### Many modern Ethernet host adapters can automatically detect another computer connected with a straight-through cable and then automatically introduce the required crossover if needed; if neither of the adapters has this capability, then a crossover cable is required. Most newer switches have auto MDI-X on all ports allowing all connections to be made with straight-through cables.  If both devices being connected support 1000BASE-T according to the standards, they will connect regardless of whether a straight-through or crossover cable is used.A 10BASE-T transmitter sends two differential voltages, +2.5 V or \u22122.5 V. A 100BASE-TX transmitter sends three differential voltages, +1 V, 0 V, or \u22121 V. Unlike earlier Ethernet standards using broadband and coaxial cable, such as 10BASE5 (thicknet) and 10BASE2 (thinnet), 10BASE-T does not specify the exact type of wiring to be used but instead specifies certain characteristics that a cable must meet.  This was done in anticipation of using 10BASE-T in existing twisted-pair wiring systems that did not conform to any specified wiring standard.  Some of the specified characteristics are attenuation, characteristic impedance, propagation delay, and several types of crosstalk.  Cable testers are widely available to check these parameters to determine if a cable can be used with 10BASE-T.  These characteristics are expected to be met by 100 meters of 24-gauge unshielded twisted-pair cable.  However, with high-quality cabling, reliable cable runs of 150 meters or longer are often achievable and are considered viable by technicians familiar with the 10BASE-T specification.100BASE-TX follows the same wiring patterns as 10BASE-T, but is more sensitive to wire quality and length, due to the higher bit rates. 
### 1000BASE-T uses all four pairs bi-directionally using hybrid circuits and cancellers. Data is encoded using 4D-PAM5; four dimensions using pulse-amplitude modulation (PAM) with five voltages, \u22122 V, \u22121 V, 0 V, +1 V, and +2 V.  While +2 V to \u22122 V may appear at the pins of the line driver, the voltage on the cable is nominally +1 V, +0.5 V, 0 V, \u22120.5 V and \u22121 V.100BASE-TX and 1000BASE-T were both designed to require a minimum of category 5 cable and also specify a maximum cable length of 100 metres (330 ft). Category 5 cable has since been deprecated and new installations use Category 5e.
## Shared cable  

### 10BASE-T and 100BASE-TX require only two pairs (pins 1\u20132, 3\u20136) to operate.  Since common Category 5 cable has four pairs, it is possible to use the spare pairs (pins 4\u20135, 7\u20138) in 10- and 100-Mbit/s configurations for other purposes. The spare pairs may be used for power over Ethernet (PoE), for two plain old telephone service (POTS) lines, or for a second 10BASE-T or 100BASE-TX connection. In practice, great care must be taken to separate these pairs as 10/100-Mbit/s Ethernet equipment electrically terminates the unused pins. Shared cable is not an option for Gigabit Ethernet as 1000BASE-T requires all four pairs to operate.
## Single-pair  
### In addition to the more computer-oriented two and four-pair variants, the 10BASE-T1, 100BASE-T1 and 1000BASE-T1 single-pair Ethernet physical layers are intended for industrial and automotive applications or as optional data channels in other interconnect applications. The single pair operates at full duplex and has a maximum reach of 15 m or 49 ft (100BASE-T1, 1000BASE-T1 link segment type A) or up to 40 m or 130 ft (1000BASE-T1 link segment type B) with up to four in-line connectors. Both physical layers require a balanced twisted pair with an impedance of 100 \u03a9. The cable must be capable of transmitting 600 MHz for 1000BASE-T1 and 66 MHz for 100BASE-T1. 2.5 Gb/s, 5 Gb/s, and 10 Gb/s over a 15 m single pair is standardized in 802.3ch-2020. As of 2021, the P802.3cy Task Force is examining having 25, 50, 100 Gb/s speeds at lengths up to 11 m.Similar to PoE, Power over Data Lines (PoDL) can provide up to 50 W to a device.
## Connectors  

### 8P8C modular connector: For stationary uses in controlled environments, from homes to datacenters, this is the dominant connector. Its fragile locking tab otherwise limits its suitability and durability. Bandwidths supporting up to Cat 8 cabling are defined for this connector format. 
### M12X: This is the M12 connector designated for Ethernet, standardized as IEC 61076-2-109. It is a 12mm metal screw that houses 4 shielded pairs of pins. Nominal bandwidth is 500MHz (Cat 6A). The connector family is used in chemically and mechanically harsh environments such as factory automation and transportation. Its size is similar to the modular connector. 
### ix Industrial: This connector is designed to be small yet strong. It has 10 pins and a different locking mechanism than the modular connector. Standardized as IEC 61076-3-124, its nominal bandwidth is 500MHz (Cat 6A). 
### Single-pair Ethernet defines its own connectors: 
### IEC 63171-1 \u201cLC\u201d: This is a 2-pin connector with a similar locking tab to the modular connector, if thicker. 
### IEC 63171-6 \u201cindustrial\u201d: This standard defines 5 2-pin connectors that differ in their locking mechanisms and one 4-pin connector with dedicated pins for power. The locking mechanisms range from a metal locking tab to M8 and M12 connectors with screw or push-pull locking. The 4-pin connector is only defined with M8 screw locking.
## Autonegotiation and duplex  
### Ethernet over twisted-pair standards up through Gigabit Ethernet define both full-duplex and half-duplex communication. However, half-duplex operation for gigabit speed is not supported by any existing hardware. Higher speed standards, 2.5GBASE-T up to 40GBASE-T running at 2.5 to 40 Gbit/s, consequently define only full-duplex point-to-point links which are generally connected by network switches, and do not support the traditional shared-medium CSMA/CD operation.Many different modes of operations (10BASE-T half-duplex, 10BASE-T full-duplex, 100BASE-TX half-duplex, etc.) exist for Ethernet over twisted pair, and most network adapters are capable of different modes of operation. Autonegotiation is required in order to make a working 1000BASE-T connection. 
### When two linked interfaces are set to different duplex modes, the effect of this duplex mismatch is a network that functions much more slowly than its nominal speed. Duplex mismatch may be inadvertently caused when an administrator configures an interface to a fixed mode (e.g. 100 Mbit/s full-duplex) and fails to configure the remote interface, leaving it set to autonegotiate. Then, when the auto-negotiation process fails, half-duplex is assumed by the autonegotiating side of the link.
## Variants 
## See also  
### Classic Ethernet 
### 25-pair color code 
### Copper cable certification 
### Ethernet extender 
### Network isolator
## Notes 
## References 
## External links  
### How to Make a Network Cable, a how-to article from wikiHow 
### How to create your own Ethernet Cables"
## References
### [Reference](http://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html#gb) - http://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html#gb
### [Reference](http://www.eetimes.com/document.asp?doc_id=1271142) - http://www.eetimes.com/document.asp?doc_id=1271142
### [Reference](http://www.walshcomptech.com/ohlandl/NIC/3com_523.html) - http://www.walshcomptech.com/ohlandl/NIC/3com_523.html
### [Reference](http://www.ertyu.org/steven_nikkel/ethernetcables.html) - http://www.ertyu.org/steven_nikkel/ethernetcables.html
### [Reference](http://grouper.ieee.org/groups/802/3/minutes/july98/E2_0798.pdf) - http://grouper.ieee.org/groups/802/3/minutes/july98/E2_0798.pdf
### [Reference](http://www.ieee802.org/3/bp/) - http://www.ieee802.org/3/bp/
### [Reference](http://www.ieee802.org/3/bq/) - http://www.ieee802.org/3/bq/
### [Reference](https://www.ccontrols.com/pdf/ExtV2N6.pdf) - https://www.ccontrols.com/pdf/ExtV2N6.pdf
### [Reference](https://books.google.com/books?id=-QELAAAAQBAJ&pg=PA180) - https://books.google.com/books?id=-QELAAAAQBAJ&pg=PA180
### [Reference](https://books.google.com/books?id=392CdZHdUDEC&pg=PA240) - https://books.google.com/books?id=392CdZHdUDEC&pg=PA240
### [Reference](https://books.google.com/books?id=4QQAAAAAMBAJ&pg=PA13) - https://books.google.com/books?id=4QQAAAAAMBAJ&pg=PA13
### [Reference](https://books.google.com/books?id=AtBeNTDGfhEC&q=starLAN+vs+LattisNet&pg=SL2-PA4) - https://books.google.com/books?id=AtBeNTDGfhEC&q=starLAN+vs+LattisNet&pg=SL2-PA4
### [Reference](https://books.google.com/books?id=MRChaUQr0Q0C&pg=PA123) - https://books.google.com/books?id=MRChaUQr0Q0C&pg=PA123
### [Reference](https://books.google.com/books?id=hBwEAAAAMBAJ&pg=PA2) - https://books.google.com/books?id=hBwEAAAAMBAJ&pg=PA2
### [Reference](https://books.google.com/books?id=ooBqdIXIqbwC&pg=PA175) - https://books.google.com/books?id=ooBqdIXIqbwC&pg=PA175
### [Reference](https://books.google.com/books?id=wvsgBQAAQBAJ) - https://books.google.com/books?id=wvsgBQAAQBAJ
### [Reference](https://www.harting.com/DE/en-gb/ix-Industrial) - https://www.harting.com/DE/en-gb/ix-Industrial
### [Reference](https://planetechusa.com/blog/ieee-standardizes-802-3bw-ethernet-adopts-automobile-application/) - https://planetechusa.com/blog/ieee-standardizes-802-3bw-ethernet-adopts-automobile-application/
### [Reference](https://blog.siemon.com/standards/ieee-p802-3ch-multi-gig-automotive-ethernet-phy) - https://blog.siemon.com/standards/ieee-p802-3ch-multi-gig-automotive-ethernet-phy
### [Reference](https://standards.ieee.org/standard/802_3cg-2019.html) - https://standards.ieee.org/standard/802_3cg-2019.html
### [Reference](https://www.ieee802.org/3/cy/) - https://www.ieee802.org/3/cy/
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/2/28/10baseT_cable.jpeg) - https://upload.wikimedia.org/wikipedia/commons/2/28/10baseT_cable.jpeg
### [Image](https://upload.wikimedia.org/wikipedia/commons/5/5f/10baseT_jack.png) - https://upload.wikimedia.org/wikipedia/commons/5/5f/10baseT_jack.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/8/86/M12X_vs_8P8C_ethernet_connectors.webp) - https://upload.wikimedia.org/wikipedia/commons/8/86/M12X_vs_8P8C_ethernet_connectors.webp
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/36/Rj45plug-8p8c.png) - https://upload.wikimedia.org/wikipedia/commons/3/36/Rj45plug-8p8c.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/6/6b/Twisted_pair_based_ethernet.svg) - https://upload.wikimedia.org/wikipedia/commons/6/6b/Twisted_pair_based_ethernet.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/de/Wire_blue.svg) - https://upload.wikimedia.org/wikipedia/commons/d/de/Wire_blue.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/d0/Wire_brown.svg) - https://upload.wikimedia.org/wikipedia/commons/d/d0/Wire_brown.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/d9/Wire_green.svg) - https://upload.wikimedia.org/wikipedia/commons/d/d9/Wire_green.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/c/c7/Wire_orange.svg) - https://upload.wikimedia.org/wikipedia/commons/c/c7/Wire_orange.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/2/29/Wire_white_blue_stripe.svg) - https://upload.wikimedia.org/wikipedia/commons/2/29/Wire_white_blue_stripe.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/3b/Wire_white_brown_stripe.svg) - https://upload.wikimedia.org/wikipedia/commons/3/3b/Wire_white_brown_stripe.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/c/c4/Wire_white_green_stripe.svg) - https://upload.wikimedia.org/wikipedia/commons/c/c4/Wire_white_green_stripe.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/dd/Wire_white_orange_stripe.svg) - https://upload.wikimedia.org/wikipedia/commons/d/dd/Wire_white_orange_stripe.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg) - https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg) - https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg