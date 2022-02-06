# Ethernet physical layer
## [URL](https://en.wikipedia.org/wiki/Ethernet_physical_layer) - https://en.wikipedia.org/wiki/Ethernet_physical_layer
## Catagories
### All Wikipedia articles written in American English
### All articles containing potentially dated statements
### All articles with failed verification
### Articles containing potentially dated statements from 2009
### Articles containing potentially dated statements from 2018
### Articles containing potentially dated statements from April 2020
### Articles with failed verification from December 2010
### Articles with short description
### CS1 errors: generic name
### Ethernet
### Physical layer protocols
### Short description matches Wikidata
### Use American English from March 2019
### "The Ethernet physical layer is the physical layer functionality of the Ethernet family of computer network standards published by the Institute of Electrical and Electronics Engineers (IEEE). The physical layer defines the electrical or optical properties and the transfer speed of the physical connection between a device and the network or between network devices. It is complemented by the MAC layer and the logical link layer. 
### The Ethernet physical layer has evolved over its existence starting in 1980 and encompasses multiple physical media interfaces and several orders of magnitude of speed from 1 Mbit/s to 400 Gbit/s. The physical medium ranges from bulky coaxial cable to twisted pair and optical fiber with a standardized reach of up to 80 km. In general, network protocol stack software will work similarly on all physical layers. 
### Many Ethernet adapters and switch ports support multiple speeds by using autonegotiation to set the speed and duplex for the best values supported by both connected devices. If autonegotiation fails, some multiple-speed devices sense the speed used by their partner, but this may result in a duplex mismatch. With rare exceptions, a 100BASE-TX port (10/100) also supports 10BASE-T while a 1000BASE-T port (10/100/1000) also supports 10BASE-T and 100BASE-TX. Most 10GBASE-T ports also support 1000BASE-T, some even 100BASE-TX or 10BASE-T. While autonegotiation can practically be relied on for Ethernet over twisted pair, few optical-fiber ports support multiple speeds. In any case, even multi-rate fiber interfaces only support a single wavelength (e.g. 850 nm for 1000BASE-SX or 10GBASE-SR). 
### 10 Gigabit Ethernet was already used in both enterprise and carrier networks by 2007, with 40 Gbit/s and 100 Gigabit Ethernet ratified. In 2017, the fastest additions to the Ethernet family were 200 and 400 Gbit/s. Development of 800 Gbit/s and 1.6 Tbit/s Ethernet standards started in 2021.
## Naming conventions  
### Generally, layers are named by their specifications: 
### 10, 100, 1000, 10G, ... \u2013 the nominal, usable speed at the top of the physical layer (no suffix  megabit/s, G  gigabit/s), excluding line codes but including other physical layer overhead (preamble, SFD, IPG); some WAN PHYs (W) run at slightly reduced bitrates for compatibility reasons; encoded PHY sublayers usually run at higher bitrates 
### BASE, BROAD, PASS \u2013 indicates baseband, broadband, or passband signaling respectively 
### -T, -T1, -S, -L, -E, -Z, -C, -K, -H ... \u2013 medium (PMD): T  twisted pair, -T1  single-pair twisted pair, S  850 nm short wavelength (multi-mode fiber), L  1300 nm long wavelength (mostly single-mode fiber), E or Z  1500 nm extra long wavelength (single-mode), B  bidirectional fiber (mostly single-mode) using WDM, P  passive optical (PON), C  copper/twinax, K  backplane, 2 or 5 or 36  coax with 185/500/3600 m reach (obsolete), F  fiber, various wavelengths, H  plastic optical fiber 
### X, R \u2013 PCS encoding method (varying with the generation): X for 8b/10b block encoding (4B5B for Fast Ethernet), R for large block encoding (64b/66b) 
### 1, 2, 4, 10 \u2013 for LAN PHYs indicates number of lanes used per link; for WAN PHYs indicates reach in kilometersFor 10 Mbit/s, no encoding is indicated as all variants use Manchester code. Most twisted pair layers use unique encoding, so most often just -T is used. 
### The reach, especially for optical connections, is defined as the maximum achievable link length that is guaranteed to work when all channel parameters are met (modal bandwidth, attenuation, insertion losses etc.). With better channel parameters, often a longer, stable link length can be achieved. Vice versa, a link with worse channel parameters can also work but only over a shorter distance. Reach and maximum distance have the same meaning.
## Physical layers  
### The following sections provide a brief summary of official Ethernet media types. In addition to these official standards, many vendors have implemented proprietary media types for various reasons\u2014often to support longer distances over fiber optic cabling.
## Early implementations and 10 Mbit/s  

### Early Ethernet standards used Manchester coding so that the signal was self-clocking and not adversely affected by high-pass filters.
## Fast Ethernet  

### All Fast Ethernet variants use a star topology and generally use 4B5B line coding.
## 1 Gbit/s  

### All Gigabit Ethernet variants use a star topology. 1000BASE-X variants use 8b/10b PCS encoding. Initially, half-duplex mode was included in the standard but has since been abandoned. Very few devices support gigabit speed in half-duplex.
## 2.5 and 5 Gbit/s  

### 2.5GBASE-T and 5GBASE-T are scaled-down variants of 10GBASE-T and provide longer reach over pre-Cat 6A cabling. These physical layers support twisted pair copper cabling only.
## 10 Gbit/s  

### 10 Gigabit Ethernet is a version of Ethernet with a nominal data rate of 10 Gbit/s, ten times as fast as Gigabit Ethernet. The first 10 Gigabit Ethernet standard, IEEE Std 802.3ae-2002, was published in 2002. Subsequent standards encompass media types for single-mode fiber (long haul), multi-mode fiber (up to 400 m), copper backplane (up to 1 m) and copper twisted pair (up to 100 m). All 10-gigabit standards were consolidated into IEEE Std 802.3-2008. Most 10-gigabit variants use 64b/66b PCS code (-R). 10 Gigabit Ethernet, specifically 10GBASE-LR and 10GBASE-ER, enjoys significant market shares in carrier networks.
## 25 Gbit/s  

### Single-lane 25-gigabit Ethernet is based on one 25.78125 GBd lane of the four from the 100 Gigabit Ethernet standard developed by the P802.3by task force. 25GBASE-T over twisted pair was approved alongside 40GBASE-T within IEEE 802.3bq.
## 40 Gbit/s  

### This class of Ethernet was standardized in June 2010 as IEEE 802.3ba. The work also included the first 100 Gbit/s generation, published in March 2011 as IEEE 802.3bg. A 40 Gbit/s twisted-pair standard was published in 2016 as IEEE 802.3bq-2016.
## 50 Gbit/s  
### The IEEE 802.3cd task force developed 50 Gbit/s along with next-generation 100 and 200 Gbit/s standards using 50 Gbit/s lanes.
## 100 Gbit/s  

### The first generation of 100 Gigabit Ethernet using 10 and 25 Gbit/s lanes was standardized in June 2010 as IEEE 802.3ba alongside 40 Gigabit Ethernet. The second generation using 50 Gbit/s lanes was developed by the IEEE 802.3cd task force along with 50 and 200 Gbit/s standards. The third generation using a single 100 Gbit/s lane is currently being developed by the IEEE 802.3ck task force along with 200 and 400 Gbit/s Ethernet.
## 200 Gbit/s  
### First generation 200 Gbit/s have been defined by the IEEE 802.3bs task force and standardized in 802.3bs-2017. The IEEE 802.3cd task force has developed 50 and next-generation 100 and 200 Gbit/s standards using one, two, or four 50 Gbit/s lanes respectively. The next generation using 100 Gbit/s lanes is currently being developed by the IEEE 802.3ck task force along with 100 and 400 Gbit/s PHYs and attachment unit interfaces (AUI) using 100 Gbit/s lanes.
## 400 Gbit/s  

### An Ethernet standard capable of 200 and 400 Gbit/s is defined in IEEE 802.3bs-2017. 1 Tbit/s may be a further goal.In May 2018, IEEE 802.3 started the 802.3ck task force to develop standards for 100, 200, and 400 Gbit/s PHYs and attachment unit interfaces (AUI) using 100 Gbit/s lanes.In 2008, Robert Metcalfe, one of the co-inventors of Ethernet, said he believed commercial applications using Terabit Ethernet may occur by 2015, though it might require new Ethernet standards. It was predicted this would be followed rapidly by a scaling to 100 Terabit, possibly as early as 2020. These were theoretical predictions of technological ability, rather than estimates of when such speeds would actually become available at a practical price point.
## 800 Gbit/s  
### The Ethernet Technology Consortium (former 25 Gigabit Ethernet Consortium) proposed an 800 Gbit/s Ethernet PCS variant based on tightly bundled 400GBASE-R in April 2020.In December 2021, IEEE started the P802.3df Task Force to define variants for 800 and 1600 Gbit/s over twinaxial copper, electrical backplanes, single-mode and multi-mode optical fiber along with new 200 and 400 Gbit/s variants using 100 and 200 Gbit/s lanes.
## 1.6 Tbit/s  
### In December 2021, IEEE started the P802.3df Task Force to define variants for 800 and 1600 Gbit/s over twinaxial copper, electrical backplanes, single-mode and multi-mode optical fiber along with new 200 and 400 Gbit/s variants using 100 and 200 Gbit/s lanes.
## First mile  

### For providing Internet access service directly from providers to homes and small businesses:
## Sublayers  
### Starting with Fast Ethernet, the physical layer specifications are divided into three sublayers in order to simplify design and interoperability: 
### PCS (Physical Coding Sublayer) - This sublayer performs auto-negotiation and basic encoding such as 8b/10b, lane separation and recombination. For Ethernet, the bit rate at the top of the PCS is the nominal bit rate, e.g. 10 Mbit/s for classic Ethernet or 1000 Mbit/s for Gigabit Ethernet. 
### PMA (Physical Medium Attachment sublayer) - This sublayer performs PMA framing, octet synchronization/detection, and polynomial scrambling/descrambling. 
### PMD (Physical Medium Dependent sublayer) - This sublayer consists of a transceiver for the physical medium.
## Twisted-pair cable  

### Several varieties of Ethernet were specifically designed to run over 4-pair copper structured cabling already installed in many locations. 
### In a departure from both 10BASE-T and 100BASE-TX, 1000BASE-T and above use all four cable pairs for simultaneous transmission in both directions through the use of echo cancellation. 
### Using point-to-point copper cabling provides the opportunity to transmit low electrical power along with the data. This is called Power over Ethernet and there are several, incremental IEEE 802.3 standards. Combining 10BASE-T (or 100BASE-TX) with Mode A allows a hub or a switch to transmit both power and data over only two pairs. This was designed to leave the other two pairs free for analog telephone signals. The pins used in Mode B supply power over the spare pairs not used by 10BASE-T and 100BASE-TX. 4PPoE defined in IEEE 802.3bt can use all four pairs to supply up to 100 W. 

### The cable requirements depend on the transmission speed and the employed encoding method. Generally, faster speeds require both higher-grade cables and more sophisticated encoding.
## Minimum cable lengths  
### Fiber connections have minimum cable lengths due to level requirements on received signals. Fiber ports designed for long-haul wavelengths require a signal attenuator if used within a building. 
### 10BASE2 installations, running on RG-58 coaxial cable, require a minimum of 0.5 m between stations tapped into the network cable to minimize reflections.10BASE-T, 100BASE-T, and 1000BASE-T installations running on twisted pair cable use a star topology. No minimum cable length is required for these networks.
## Related standards  
### Some networking standards are not part of the IEEE 802.3 Ethernet standard, but support the Ethernet frame format, and are capable of interoperating with it. 

### LattisNet\u2014A SynOptics pre-standard twisted-pair 10 Mbit/s variant. 
### 100BaseVG\u2014An early contender for 100 Mbit/s Ethernet. It runs over Category 3 cabling. Uses four pairs. Commercial failure. 
### TIA 100BASE-SX\u2014Promoted by the Telecommunications Industry Association. 100BASE-SX is an alternative implementation of 100 Mbit/s Ethernet over fiber; it is incompatible with the official 100BASE-FX standard. Its main feature is interoperability with 10BASE-FL, supporting autonegotiation between 10 Mbit/s and 100 Mbit/s operation \u2013 a feature lacking in the official standards due to the use of differing LED wavelengths. It is targeted at the installed base of 10 Mbit/s fiber network installations. 
### TIA 1000BASE-TX\u2014Promoted by the Telecommunications Industry Association, it was a commercial failure, and no products exist. 1000BASE-TX uses a simpler protocol than the official 1000BASE-T standard so the electronics can be cheaper, but requires Category 6 cabling. 
### G.hn\u2014A standard developed by ITU-T and promoted by HomeGrid Forum for high-speed (up to 1 Gbit/s) local area networks over existing home wiring (coaxial cables, power lines and phone lines). G.hn defines an Application Protocol Convergence (APC) layer that accepts Ethernet frames and encapsulates them into G.hn MSDUs.Other networking standards do not use the Ethernet frame format but can still be connected to Ethernet using MAC-based bridging. 

### 802.11\u2014Standards for wireless local area networks (LANs), sold with brand name Wi-Fi 
### 802.16\u2014Standards for wireless metropolitan area networks (MANs), sold with brand name WiMAXOther special-purpose physical layers include Avionics Full-Duplex Switched Ethernet and TTEthernet \u2014 Time-Triggered Ethernet for embedded systems.
## References 
## External links  
### IEEE GET Program GET 802(R) Standards 
### IEEE 802.3 
### How to make an Ethernet cable"
## References
### [Reference](http://web.cs.dal.ca/~yongzhen/course/6704/report.pdf) - http://web.cs.dal.ca/~yongzhen/course/6704/report.pdf
### [Reference](http://www.cisco.com/c/en/us/support/docs/interfaces-modules/port-adapters/12768-eth-collisions.html) - http://www.cisco.com/c/en/us/support/docs/interfaces-modules/port-adapters/12768-eth-collisions.html
### [Reference](http://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) - http://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html
### [Reference](http://www.cisco.com/en/US/products/hw/modules/ps2033/products_data_sheet09186a0080091ce7.html) - http://www.cisco.com/en/US/products/hw/modules/ps2033/products_data_sheet09186a0080091ce7.html
### [Reference](http://www.cisco.com/en/US/products/hw/modules/ps5455/products_data_sheet0900aecd801ba88e.html) - http://www.cisco.com/en/US/products/hw/modules/ps5455/products_data_sheet0900aecd801ba88e.html
### [Reference](http://www.electronista.com/articles/12/08/20/aging.standard.is.still.ahead.of.most.core.networking/) - http://www.electronista.com/articles/12/08/20/aging.standard.is.still.ahead.of.most.core.networking/
### [Reference](http://www.fiber-optical-networking.com/characteristics-of-10gbase-t-technology.html) - http://www.fiber-optical-networking.com/characteristics-of-10gbase-t-technology.html
### [Reference](http://www.infineon.com/cms/en/corporate/press/news/releases/2001/130817.html) - http://www.infineon.com/cms/en/corporate/press/news/releases/2001/130817.html
### [Reference](http://www.infineon.com/news/press/101_031e.htm) - http://www.infineon.com/news/press/101_031e.htm
### [Reference](http://www.lightreading.com/video.asp?section_id=154&doc_id=703860) - http://www.lightreading.com/video.asp?section_id=154&doc_id=703860
### [Reference](http://www.proavbiz-europe.com/index.php?option=com_content&view=article&id=6151:ieee-begins-work-on-new-ethernet-standard&catid=15&Itemid=401979) - http://www.proavbiz-europe.com/index.php?option=com_content&view=article&id=6151:ieee-begins-work-on-new-ethernet-standard&catid=15&Itemid=401979
### [Reference](http://proquest.safaribooksonline.com/book/networking/9781449362980/8dot-10-mb-s-ethernet/_10base_fl_fiber_optic_characteristics_html?uicode=vatech) - http://proquest.safaribooksonline.com/book/networking/9781449362980/8dot-10-mb-s-ethernet/_10base_fl_fiber_optic_characteristics_html?uicode=vatech
### [Reference](http://ethernethistory.typepad.com/papers/EthernetEvolution.pdf) - http://ethernethistory.typepad.com/papers/EthernetEvolution.pdf
### [Reference](http://www.virtual-strategy.com/2012/06/11/l-com-introduces-commercial-grade-thinnet-10base-2-and-thicknet-10base-5-converters-legac) - http://www.virtual-strategy.com/2012/06/11/l-com-introduces-commercial-grade-thinnet-10base-2-and-thicknet-10base-5-converters-legac
### [Reference](http://www.wikihow.com/Make-a-Network-Cable) - http://www.wikihow.com/Make-a-Network-Cable
### [Reference](http://www.zytrax.com/tech/layer_1/cables/mixed.html) - http://www.zytrax.com/tech/layer_1/cables/mixed.html
### [Reference](http://www.trincoll.edu/Academics/MajorsAndMinors/Engineering/Documents/IEEE%20Standard%20for%20Ethernet.pdf) - http://www.trincoll.edu/Academics/MajorsAndMinors/Engineering/Documents/IEEE%20Standard%20for%20Ethernet.pdf
### [Reference](http://www.hecto.eu/) - http://www.hecto.eu/
### [Reference](http://doi.org/10.1109%2FIEEESTD.2017.8207825) - http://doi.org/10.1109%2FIEEESTD.2017.8207825
### [Reference](http://doi.org/10.1109%2FMC.1982.1654107) - http://doi.org/10.1109%2FMC.1982.1654107
### [Reference](http://www.homegridforum.org/) - http://www.homegridforum.org/
### [Reference](http://grouper.ieee.org/groups/802/3/hssg/public/may07/duelk_01_0507.pdf) - http://grouper.ieee.org/groups/802/3/hssg/public/may07/duelk_01_0507.pdf
### [Reference](http://grouper.ieee.org/groups/802/3/hssg/public/may07/kipp_01_0507.pdf) - http://grouper.ieee.org/groups/802/3/hssg/public/may07/kipp_01_0507.pdf
### [Reference](http://www.ieee802.org/3/) - http://www.ieee802.org/3/
### [Reference](http://www.ieee802.org/3/400GSG/email/msg01519.html) - http://www.ieee802.org/3/400GSG/email/msg01519.html
### [Reference](http://www.ieee802.org/3/NGBASET/email/msg00972.html) - http://www.ieee802.org/3/NGBASET/email/msg00972.html
### [Reference](http://www.ieee802.org/3/ba/) - http://www.ieee802.org/3/ba/
### [Reference](http://www.ieee802.org/3/ba/public/may08/ganga_02_0508.pdf) - http://www.ieee802.org/3/ba/public/may08/ganga_02_0508.pdf
### [Reference](http://www.ieee802.org/3/bg/) - http://www.ieee802.org/3/bg/
### [Reference](http://www.ieee802.org/3/bq/index.html) - http://www.ieee802.org/3/bq/index.html
### [Reference](http://www.ieee802.org/3/by/index.html) - http://www.ieee802.org/3/by/index.html
### [Reference](http://www.ieee802.org/3/cd/) - http://www.ieee802.org/3/cd/
### [Reference](http://www.ieee802.org/3/ck/) - http://www.ieee802.org/3/ck/
### [Reference](https://arstechnica.com/hardware/news/2007/07/new-ethernet-standard-not-40-gbps-not-100-but-both.ars) - https://arstechnica.com/hardware/news/2007/07/new-ethernet-standard-not-40-gbps-not-100-but-both.ars
### [Reference](https://web.archive.org/web/20010413234628/http://www.infineon.com/news/press/101_031e.htm) - https://web.archive.org/web/20010413234628/http://www.infineon.com/news/press/101_031e.htm
### [Reference](https://web.archive.org/web/20071013023543/http://www.cisco.com/en/US/products/hw/modules/ps5455/products_data_sheet0900aecd801ba88e.html) - https://web.archive.org/web/20071013023543/http://www.cisco.com/en/US/products/hw/modules/ps5455/products_data_sheet0900aecd801ba88e.html
### [Reference](https://web.archive.org/web/20131219024707/http://www.virtual-strategy.com/2012/06/11/l-com-introduces-commercial-grade-thinnet-10base-2-and-thicknet-10base-5-converters-legac) - https://web.archive.org/web/20131219024707/http://www.virtual-strategy.com/2012/06/11/l-com-introduces-commercial-grade-thinnet-10base-2-and-thicknet-10base-5-converters-legac
### [Reference](https://ethernettechnologyconsortium.org/press-room/press-releases/25-gigabit-ethernet-consortium-rebrands-to-ethernet-technology-consortium-announces-800-gigabit-ethernet-gbe-specification-152/) - https://ethernettechnologyconsortium.org/press-room/press-releases/25-gigabit-ethernet-consortium-rebrands-to-ethernet-technology-consortium-announces-800-gigabit-ethernet-gbe-specification-152/
### [Reference](https://ethernettechnologyconsortium.org/wp-content/uploads/2020/03/800G-Specification_r1.0.pdf) - https://ethernettechnologyconsortium.org/wp-content/uploads/2020/03/800G-Specification_r1.0.pdf
### [Reference](https://ieeexplore.ieee.org/browse/standards/get-program/page/series?id=68) - https://ieeexplore.ieee.org/browse/standards/get-program/page/series?id=68
### [Reference](https://www.ieee802.org/3/df/proj_doc/objectives_P802d3df_211118.pdf) - https://www.ieee802.org/3/df/proj_doc/objectives_P802d3df_211118.pdf
### [Reference](https://www.ieee802.org/3/df/public/index.html) - https://www.ieee802.org/3/df/public/index.html
### [Reference](https://api.semanticscholar.org/CorpusID:14546631) - https://api.semanticscholar.org/CorpusID:14546631
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/f/fa/EthernetCableYellow3.jpg) - https://upload.wikimedia.org/wikipedia/commons/f/fa/EthernetCableYellow3.jpg
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