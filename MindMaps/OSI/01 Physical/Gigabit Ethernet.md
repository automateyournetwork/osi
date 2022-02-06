# Gigabit Ethernet
## [URL](https://en.wikipedia.org/wiki/Gigabit_Ethernet) - https://en.wikipedia.org/wiki/Gigabit_Ethernet
## Catagories
### All Wikipedia articles written in American English
### All articles needing additional references
### All articles with self-published sources
### All articles with unsourced statements
### Articles needing additional references from March 2017
### Articles with self-published sources from May 2020
### Articles with short description
### Articles with unsourced statements from January 2021
### Articles with unsourced statements from June 2012
### Articles with unsourced statements from March 2019
### Computer-related introductions in 1999
### Ethernet
### Short description matches Wikidata
### Use American English from January 2021
### Use mdy dates from December 2021
### "In computer networking, Gigabit Ethernet (GbE or 1 GigE) is the term applied to transmitting Ethernet frames at a rate of a gigabit per second. The most popular variant 1000BASE-T is defined by the IEEE 802.3ab standard. It came into use in 1999, and has replaced Fast Ethernet in wired local networks due to its considerable speed improvement over Fast Ethernet, as well as its use of cables and equipment that are widely available, economical, and similar to previous standards.
## History  
### Ethernet was the result of research conducted at Xerox PARC in the early 1970s, and later evolved into a widely implemented physical and link layer protocol. Fast Ethernet increased the speed from 10 to 100 megabits per second (Mbit/s). Gigabit Ethernet was the next iteration, increasing the speed to 1000 Mbit/s. 

### The initial standard for Gigabit Ethernet was produced by the IEEE in June 1998 as IEEE 802.3z, and required optical fiber. 802.3z is commonly referred to as 1000BASE-X, where -X refers to either -CX, -SX, -LX, or (non-standard) -ZX. (For the history behind the \"X\" see Fast Ethernet \u00a7 Nomenclature.) 
### IEEE 802.3ab, ratified in 1999, defines Gigabit Ethernet transmission over unshielded twisted pair (UTP) category 5, 5e or 6 cabling, and became known as 1000BASE-T. With the ratification of 802.3ab, Gigabit Ethernet became a desktop technology as organizations could use their existing copper cabling infrastructure. 
### IEEE 802.3ah, ratified in 2004, added two more gigabit fiber standards: 1000BASE-LX10 (which was already widely implemented as vendor-specific extension) and 1000BASE-BX10. This was part of a larger group of protocols known as Ethernet in the First Mile.Initially, Gigabit Ethernet was deployed in high-capacity backbone network links (for instance, on a high-capacity campus network). In 2000, Apple's Power Mac G4 and PowerBook G4 were the first mass-produced personal computers to feature the 1000BASE-T connection. It quickly became a built-in feature in many other computers. 
### Half-duplex gigabit links connected through repeater hubs were part of the IEEE specification, but the specification is not updated anymore and full-duplex operation with switches is used exclusively.
## Varieties  

### There are five physical layer standards for Gigabit Ethernet using optical fiber (1000BASE-X), twisted pair cable (1000BASE-T), or shielded balanced copper cable (1000BASE-CX). 
### The IEEE 802.3z standard includes 1000BASE-SX for transmission over multi-mode fiber, 1000BASE-LX for transmission over single-mode fiber, and the nearly obsolete 1000BASE-CX for transmission over shielded balanced copper cabling. These standards use 8b/10b encoding, which inflates the line rate by 25%, from 1000 Mbit/s to 1250 Mbit/s, to ensure a DC balanced signal, and allow for clock recovery. The symbols are then sent using NRZ. 
### Optical fiber transceivers are most often implemented as user-swappable modules in SFP form or GBIC on older devices. 
### IEEE 802.3ab, which defines the widely used 1000BASE-T interface type, uses a different encoding scheme in order to keep the symbol rate as low as possible, allowing transmission over twisted pair. 
### IEEE 802.3ap defines Ethernet Operation over Electrical Backplanes at different speeds. 
### Ethernet in the First Mile later added 1000BASE-LX10 and -BX10.
## Copper 
## 1000BASE-T  

### 1000BASE-T (also known as IEEE 802.3ab) is a standard for Gigabit Ethernet over copper wiring. 
### Each 1000BASE-T network segment is recommended to be a maximum length of 100 meters (330 feet), and must use Category 5 cable or better (including Cat 5e and Cat 6). 
### Autonegotiation is a requirement for using 1000BASE-T according to Section 28D.5 Extensions required for Clause40 (1000BASE-T).  At least the clock source has to be negotiated, as one endpoint must be master and the other endpoint must be slave. 
### In a departure from both 10BASE-T and 100BASE-TX, 1000BASE-T uses four lanes over all four cable pairs for simultaneous transmission in both directions through the use of echo cancellation with adaptive equalization called hybrid circuits (this is like telephone hybrid) and five-level pulse-amplitude modulation (PAM-5). The symbol rate is identical to that of 100BASE-TX (125 megabaud) and the noise immunity of the five-level signaling is also identical to that of the three-level signaling in 100BASE-TX, since 1000BASE-T uses four-dimensional trellis coded modulation (TCM) to achieve a 6 dB coding gain across the four pairs. 
### Since negotiation takes place on only two pairs, if two gigabit interfaces are connected through a cable with only two pairs, the interfaces will successfully choose 'gigabit' as the highest common denominator (HCD), but the link will never come up. Most gigabit physical devices have a specific register to diagnose this behavior. Some drivers offer an \"Ethernet@Wirespeed\" option where this situation leads to a slower yet functional connection.The data is transmitted over four copper pairs, eight bits at a time. First, eight bits of data are expanded into four three-bit symbols through a non-trivial scrambling procedure based on a linear-feedback shift register; this is similar to what is done in 100BASE-T2, but uses different parameters. The three-bit symbols are then mapped to voltage levels which vary continuously during transmission. An example mapping is as follows: 

### Automatic MDI/MDI-X Configuration is specified as an optional feature in the 1000BASE-T standard, meaning that straight-through cables will often work between gigabit-capable interfaces. This feature eliminates the need for crossover cables, making obsolete the uplink/normal ports and manual selector switches found on many older hubs and switches and greatly reduces installation errors. 
### In order to extend and maximize the use of existing Cat-5e and Cat-6 cabling, additional next-generation standards 2.5GBASE-T and 5GBASE-T will operate at 2.5 and 5.0 Gbit/s, respectively, on existing copper infrastructure designed for use with 1000BASE-T. It is based on 10GBASE-T but uses lower signaling frequencies.
## 1000BASE-T1  

### IEEE 802.3 standardized 1000BASE-T1 in IEEE Std 802.3bp-2016. It defines Gigabit Ethernet over a single twisted pair for automotive and industrial applications. It includes cable specifications for 15 meters (type A) or 40 meters (type B) reach. The transmission is done using PAM-3 at 750 MBd.
## 1000BASE-TX  
### The Telecommunications Industry Association (TIA) created and promoted a standard similar to 1000BASE-T that was simpler to implement, calling it 1000BASE-TX (TIA/EIA-854). The simplified design would have, in theory, reduced the cost of the required electronics by only using four unidirectional pairs (two pairs TX and two pairs RX) instead of four bidirectional pairs. However, this solution has been a commercial failure, likely due to the required Category 6 cabling and the rapidly falling cost of 1000BASE-T products.
## 1000BASE-CX  
### 802.3z-1998 CL39 standardized 1000BASE-CX is an initial standard for Gigabit Ethernet connections with maximum distances of 25 meters using balanced shielded twisted pair and either DE-9 or 8P8C connector (with a pinout different from 1000BASE-T). The short segment length is due to a very high signal transmission rate. Although it is still used for specific applications where cabling is done by IT professionals, for instance, the IBM BladeCenter uses 1000BASE-CX for the Ethernet connections between the blade servers and the switch modules, 1000BASE-T has succeeded it for general copper wiring use.
## 1000BASE-KX  
### 802.3ap-2007 CL70 standardized 1000BASE-KX is part of the IEEE 802.3ap standard for Ethernet Operation over Electrical Backplanes. This standard defines one to four lanes of backplane links, one RX and one TX differential pair per lane, at link bandwidth ranging from 100Mbit to 10Gbit per second (from 100BASE-KX to 10GBASE-KX4). The 1000BASE-KX variant uses 1.25 GBd electrical (not optical) signalling speed.
## Fiber optics  
### 1000BASE-X is used in industry to refer to Gigabit Ethernet transmission over fiber, where options include 1000BASE-SX, 1000BASE-LX, 1000BASE-LX10, 1000BASE-BX10 or the non-standard -EX and -ZX implementations. Included are copper variants using the same 8b/10b line code. 1000BASE-X is based on the physical-layer standards developed for Fibre Channel.
## 1000BASE-SX  
### 1000BASE-SX is an optical fiber Gigabit Ethernet standard for operation over multi-mode fiber using a 770 to 860 nanometer, near infrared (NIR) light wavelength. 
### The standard specifies a maximum length of 220 meters for 62.5 \u03bcm/160 MHz\u00d7km multi-mode fiber, 275 m for 62.5 \u03bcm/200 MHz\u00d7km, 500 m for 50 \u03bcm/400 MHz\u00d7km, and 550 m for 50 \u03bcm/500 MHz\u00d7km multi-mode fiber. In practice, with good quality fiber, optics, and terminations, 1000BASE-SX will usually work over significantly longer distances.This standard is highly popular for intra-building links in large office buildings, co-location facilities and carrier-neutral Internet exchanges. 
### Optical power specifications of SX interface: Minimum output power  \u22129.5 dBm. Minimum receive sensitivity  \u221217 dBm.
## 1000BASE-LSX  
### 1000BASE-LSX is a non-standard but industry accepted 
### term to refer to Gigabit Ethernet transmission. It is very similar to 1000BASE-SX but achieves longer distances up to 2 km over a pair of multi-mode fibers due to higher quality optics than a SX, running on 1310 nm wavelength lasers. It  is easily confused with 1000BASE-SX or 1000BASE-LX because the use of -LX, -LX10 and -SX is ambiguous between vendors.  
### The range is achieved with use of Fabry Perot laser transmitter.
## 1000BASE-LX  
### 1000BASE-LX is an optical fiber Gigabit Ethernet standard specified in IEEE 802.3 Clause 38 which uses a long wavelength laser (1,270\u20131,355 nm), and a maximum RMS spectral width of 4 nm. 
### 1000BASE-LX is specified to work over a distance of up to 5 km over 10 \u03bcm single-mode fiber. 
### 1000BASE-LX can also run over all common types of multi-mode fiber with a maximum segment length of 550 m. For link distances greater than 300 m, the use of a special launch conditioning patch cord may be required. This launches the laser at a precise offset from the center of the fiber which causes it to spread across the diameter of the fiber core, reducing the effect known as differential mode delay which occurs when the laser couples onto only a small number of available modes in multi-mode fiber.
## 1000BASE-LX10  
### 1000BASE-LX10 was standardized six years after the initial gigabit fiber versions as part of the Ethernet in the First Mile task group. It is practically identical to 1000BASE-LX, but achieves longer distances up to 10 km over a pair of single-mode fiber due to higher quality optics. Before it was standardized, 1000BASE-LX10 was essentially already in widespread use by many vendors as a proprietary extension called either 1000BASE-LX/LH or 1000BASE-LH.
## 1000BASE-EX  
### 1000BASE-EX is a non-standard but industry accepted term to refer to Gigabit Ethernet transmission. It is very similar to 1000BASE-LX10 but achieves longer distances up to 40 km over a pair of single-mode fibers due to higher quality optics than a LX10, running on 1310 nm wavelength lasers. It is sometimes referred to as LH (Long Haul), and is easily confused with 1000BASE-LX10 or 1000BASE-ZX because the use of -LX(10), -LH, -EX, and -ZX is ambiguous between vendors. 1000BASE-ZX is a very similar non-standard longer-reach variant that uses 1550 nm wavelength optics.
## 1000BASE-BX10  
### 1000BASE-BX10 is capable of up to 10 km over a single strand of single-mode fiber, with a different wavelength going in each direction. The terminals on each side of the fiber are not equal, as the one transmitting downstream (from the center of the network to the outside) uses the 1490 nm wavelength, and the one transmitting upstream uses the 1310 nm wavelength. This is accomplished using a passive splitter prism inside each transceiver. 
### Other, non-standard higher-powered single-strand optics commonly known as \"BiDi\" (bi-directional) utilize wavelength pairs in the 1490/1550 nm range, and are capable of reaching distances of 20, 40 and 80 km, or greater depending on module cost, fiber path loss, splices, connectors and patch panels. Very long reach BiDi optics may use 1510/1590 nm wavelength pairs.
## 1000BASE-ZX  
### 1000BASE-ZX is a non-standard but multi-vendor term to refer to Gigabit Ethernet transmission using 1,550 nm wavelength to achieve distances of at least 70 kilometres (43 miles) over single-mode fiber. Some vendors specify distances up to 120 kilometres (75 miles) over single-mode fiber, sometimes called 1000BASE-EZX. Ranges beyond 80 km are highly dependent upon the path loss of the fiber in use, specifically the attenuation figure in dB per km, the number and quality of connectors/patch panels and splices located between transceivers.
## 1000BASE\u2011CWDM  
### 1000BASE-CWDM is a non-standard but industry accepted term to refer to Gigabit Ethernet transmission. It is very similar to 1000BASE-LX10 but achieves longer distances up 40\u2013120 km, and up to 18 parallel channels over a pair of single-mode fibers due to higher quality optics than LX10 and use of CWDM, running on 1270-1610 nm wavelength lasers. 
### To use CWDM you need a Mux/Demux unit on both ends of the fiber link, a CWDM MUX/DEMUX with corresponding wavelengths, and SFP with corresponding wavelengths. is it also possible to DWDM in serie to increase number of channels. 
### Most uses Wavelengths:  1270 nm, 1290 nm, 1310 nm, 1330 nm, 1350 nm, 1370 nm, 1390 nm, 1410 nm, 1430 nm, 1450 nm, 1470 nm, 1490 nm, 1510 nm, 1530 nm, 1550 nm, 1570 nm, 1590 nm and 1610 nm 
### CWDM is cheaper to use than DWDM, about 1/5-1/3 of the cost. CWDM is about 5-10 times more expensive the if you have the fiber available, then traditional  -LX/-LZ transceivers.
## 1000BASE\u2011DWDM  
### 1000BASE-DWDM is a non-standard but industry accepted term to refer to Gigabit Ethernet transmission. It is very similar to 1000BASE-LX10 but achieves longer distances up 40\u2013120 km, and up to 64 to 160 parallel channels over a pair of single-mode fibers due to higher quality optics than LX10 and use of DWDM, running on 1528-1565 nm wavelength lasers. 
### The most used channels are  CH17-61 on Wavelength 1528.77-1563-86 nm. 
### To use DWDM you need a Mux/Demux unit on both ends of the fiber link, a DWDM MUX/DEMUX with corresponding wavelengths, and SFP with corresponding wavelengths. is it also possible to use CWDM in series to increase the number of channels.
## 1000BASE-RHx  
### IEEE 802.3bv-2017 defines standardizes Gigabit Ethernet over step-index plastic optical fiber (POF) using -R 64b/65b large block encoding with red light (600\u2013700 nm). 1000BASE-RHA is intended for home and consumer use (just clamping the bare POF), 1000BASE-RHB for industrial, and 1000BASE-RHC for automotive applications.
## Optical interoperability  
### There may be optical interoperability with respective 1000BASE-X Ethernet interfaces on the same link. It is also possible with certain types of optics to have a mismatch in wavelength.To achieve interoperability some criteria have to be met: 
### Line encoding 
### Wavelength 
### Duplex mode 
### Media count 
### Media type and dimension1000BASE-X Ethernet is not backward compatible with 100BASE-X and is not forward compatible with 10GBASE-X.
## See also  
### List of device bandwidths 
### Physical Coding Sublayer
## Notes 
## References 
## Further reading  
### Norris, Mark, Gigabit Ethernet Technology and Applications, Artech House, 2002. ISBN 1-58053-505-4
## External links  
### Get IEEE 802.3 
### IEEE 802.3 
### IEEE and Gigabit Ethernet Alliance Announce Formal Ratification of gigabit Ethernet Over Copper Standard - Announcement from IEEE June 28, 1999 
### IEEE P802.3ab 1000BASE-T Task Force (historical information) 
### IEEE 802.3 CSMA/CD (ETHERNET) 
### 1000BASE-T Whitepaper from 10GEA 
### Gigabit Ethernet Auto-Negotiation"
## References
### [Reference](http://www.apple-history.com/frames/body.php?page=gallery&model=g4giga) - http://www.apple-history.com/frames/body.php?page=gallery&model=g4giga
### [Reference](http://www.cisco.com/c/en/us/td/docs/interfaces_modules/transceiver_modules/installation/note/OL_19329.html) - http://www.cisco.com/c/en/us/td/docs/interfaces_modules/transceiver_modules/installation/note/OL_19329.html
### [Reference](http://www.cisco.com/en/US/prod/collateral/modules/ps5455/ps6577/product_data_sheet0900aecd8033f885.html) - http://www.cisco.com/en/US/prod/collateral/modules/ps5455/ps6577/product_data_sheet0900aecd8033f885.html
### [Reference](http://scholar.google.com/scholar?q=%22Gigabit+Ethernet%22) - http://scholar.google.com/scholar?q=%22Gigabit+Ethernet%22
### [Reference](http://www.google.com/search?&q=%22Gigabit+Ethernet%22&tbs=bkt:s&tbm=bks) - http://www.google.com/search?&q=%22Gigabit+Ethernet%22&tbs=bkt:s&tbm=bks
### [Reference](http://www.google.com/search?as_eq=wikipedia&q=%22Gigabit+Ethernet%22) - http://www.google.com/search?as_eq=wikipedia&q=%22Gigabit+Ethernet%22
### [Reference](http://www.google.com/search?tbm=nws&q=%22Gigabit+Ethernet%22+-wikipedia&tbs=ar:1) - http://www.google.com/search?tbm=nws&q=%22Gigabit+Ethernet%22+-wikipedia&tbs=ar:1
### [Reference](http://www.google.com/search?tbs=bks:1&q=%22Gigabit+Ethernet%22+-wikipedia) - http://www.google.com/search?tbs=bks:1&q=%22Gigabit+Ethernet%22+-wikipedia
### [Reference](http://menaranet.com/download/datasheets/SFP/187-0A031-00%20SFP%201550nm%20EZX%201GbE%20-%20Product%20Datasheet-%202%20page.pdf) - http://menaranet.com/download/datasheets/SFP/187-0A031-00%20SFP%201550nm%20EZX%201GbE%20-%20Product%20Datasheet-%202%20page.pdf
### [Reference](http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7F1654843%7F1103%7Fpdf%7FEnglish%7FENG_DS_1654843_1103.pdf) - http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7F1654843%7F1103%7Fpdf%7FEnglish%7FENG_DS_1654843_1103.pdf
### [Reference](http://www.thenetworkencyclopedia.com/entry/1000basecx/) - http://www.thenetworkencyclopedia.com/entry/1000basecx/
### [Reference](http://www.respice-sme.eu/fileadmin/cms/downloads/KDPOF-07_Presentation_Optical_Ethernet_Automotive.pdf) - http://www.respice-sme.eu/fileadmin/cms/downloads/KDPOF-07_Presentation_Optical_Ethernet_Automotive.pdf
### [Reference](http://www.10gea.org/1000base-t/) - http://www.10gea.org/1000base-t/
### [Reference](http://grouper.ieee.org/groups/802/3/) - http://grouper.ieee.org/groups/802/3/
### [Reference](http://grouper.ieee.org/groups/802/3/ab/) - http://grouper.ieee.org/groups/802/3/ab/
### [Reference](http://standards.ieee.org/announcements/802.3ab.html) - http://standards.ieee.org/announcements/802.3ab.html
### [Reference](http://standards.ieee.org/getieee802/802.3.html) - http://standards.ieee.org/getieee802/802.3.html
### [Reference](http://standards.ieee.org/getieee802/download/802.3-2008_section1.pdf) - http://standards.ieee.org/getieee802/download/802.3-2008_section1.pdf
### [Reference](http://standards.ieee.org/reading/ieee/interp/IEEE802.3af-2003interp-6.pdf) - http://standards.ieee.org/reading/ieee/interp/IEEE802.3af-2003interp-6.pdf
### [Reference](http://www.ieee802.org/3/) - http://www.ieee802.org/3/
### [Reference](http://www.ieee802.org/3/bp/) - http://www.ieee802.org/3/bp/
### [Reference](http://www.ieee802.org/3/bv/public/Sep_2015/perezaranda_3bv_1_0915.pdf) - http://www.ieee802.org/3/bv/public/Sep_2015/perezaranda_3bv_1_0915.pdf
### [Reference](http://www.nbaset.org/technology/) - http://www.nbaset.org/technology/
### [Reference](http://www.tiaonline.org/news_events/press_room/press_releases/legacy.cfm?parelease=01-87) - http://www.tiaonline.org/news_events/press_room/press_releases/legacy.cfm?parelease=01-87
### [Reference](https://arstechnica.com/civis/viewtopic.php?p=6647265&sid=1207bc662946d0bf8ff15eac6753a819#p6647265) - https://arstechnica.com/civis/viewtopic.php?p=6647265&sid=1207bc662946d0bf8ff15eac6753a819#p6647265
### [Reference](https://www.broadcom.com/application/ethernet_nic.php) - https://www.broadcom.com/application/ethernet_nic.php
### [Reference](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/dwdm-transceiver-modules/product_data_sheet0900aecd80582763.html) - https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/dwdm-transceiver-modules/product_data_sheet0900aecd80582763.html
### [Reference](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/cwdm-transceiver-modules/product_data_sheet09186a00801a557c.html) - https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/cwdm-transceiver-modules/product_data_sheet09186a00801a557c.html
### [Reference](https://www02.cp-static.com/objects/pdf/2/227/1347766271_1_network-media-converters-cisco-100base-zx-for-fast-ethernet-sfp-ports-glc-fe-100zx253d.pdf) - https://www02.cp-static.com/objects/pdf/2/227/1347766271_1_network-media-converters-cisco-100base-zx-for-fast-ethernet-sfp-ports-glc-fe-100zx253d.pdf
### [Reference](https://community.fs.com/blog/complete-analysis-on-dwdm-technology.html) - https://community.fs.com/blog/complete-analysis-on-dwdm-technology.html
### [Reference](https://community.fs.com/blog/cwdm-cost-effective-alternative-to-expand-network-capacity.html) - https://community.fs.com/blog/cwdm-cost-effective-alternative-to-expand-network-capacity.html
### [Reference](https://www.fs.com/de-en/products/11776.html) - https://www.fs.com/de-en/products/11776.html
### [Reference](https://www.fs.com/de-en/products/49943.html) - https://www.fs.com/de-en/products/49943.html
### [Reference](https://www.fs.com/products/75795.html) - https://www.fs.com/products/75795.html
### [Reference](https://medium.com/@opticalfibersolutions/cwdm-vs-dwdm-what-are-the-differences-67c1c8adeccc) - https://medium.com/@opticalfibersolutions/cwdm-vs-dwdm-what-are-the-differences-67c1c8adeccc
### [Reference](https://www.moxa.com/getmedia/ea25d5b9-e1dd-4c78-9196-75888e1df95f/moxa-sfp-1g-series-datasheet-v1.0.pdf) - https://www.moxa.com/getmedia/ea25d5b9-e1dd-4c78-9196-75888e1df95f/moxa-sfp-1g-series-datasheet-v1.0.pdf
### [Reference](https://www.youtube.com/watch?v=kNa_IdfivKs) - https://www.youtube.com/watch?v=kNa_IdfivKs
### [Reference](https://kb.wisc.edu/ns/page.php?id=7829) - https://kb.wisc.edu/ns/page.php?id=7829
### [Reference](https://web.archive.org/web/20101206030247/http://standards.ieee.org/getieee802/download/802.3-2008_section1.pdf) - https://web.archive.org/web/20101206030247/http://standards.ieee.org/getieee802/download/802.3-2008_section1.pdf
### [Reference](https://web.archive.org/web/20110927060633/http://www.tiaonline.org/news_events/press_room/press_releases/legacy.cfm?parelease=01-87) - https://web.archive.org/web/20110927060633/http://www.tiaonline.org/news_events/press_room/press_releases/legacy.cfm?parelease=01-87
### [Reference](https://web.archive.org/web/20120205143649/http://www.dell.com/content/topics/global.aspx/power/en/ps1q01_hernan?c=us&l=en&cs=555) - https://web.archive.org/web/20120205143649/http://www.dell.com/content/topics/global.aspx/power/en/ps1q01_hernan?c=us&l=en&cs=555
### [Reference](https://ghostarchive.org/varchive/youtube/20211117/kNa_IdfivKs) - https://ghostarchive.org/varchive/youtube/20211117/kNa_IdfivKs
### [Reference](https://standards.ieee.org/content/dam/ieee-standards/standards/web/download/802.3-2008_downloads.zip) - https://standards.ieee.org/content/dam/ieee-standards/standards/web/download/802.3-2008_downloads.zip
### [Reference](https://www.jstor.org/action/doBasicSearch?Query=%22Gigabit+Ethernet%22&acc=on&wc=on) - https://www.jstor.org/action/doBasicSearch?Query=%22Gigabit+Ethernet%22&acc=on&wc=on
### [Reference](https://archive.nanog.org/sites/default/files/Steenbergen.Everything_You_Need.pdf) - https://archive.nanog.org/sites/default/files/Steenbergen.Everything_You_Need.pdf
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/b/be/Intel_PRO-1000_GT_PCI_NIC.jpg) - https://upload.wikimedia.org/wikipedia/commons/b/be/Intel_PRO-1000_GT_PCI_NIC.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/c/c5/Intelpromtserverpcixadapter1000mta342.jpg) - https://upload.wikimedia.org/wikipedia/commons/c/c5/Intelpromtserverpcixadapter1000mta342.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/3b/Supermicro_AOC-SGP-I2_Gigabit_Ethernet_NIC%2C_PCI-Express_x4_card.jpg) - https://upload.wikimedia.org/wikipedia/commons/3/3b/Supermicro_AOC-SGP-I2_Gigabit_Ethernet_NIC%2C_PCI-Express_x4_card.jpg
### [Image](https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg) - https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg) - https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg