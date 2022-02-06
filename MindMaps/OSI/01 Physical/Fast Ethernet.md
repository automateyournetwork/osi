# Fast Ethernet
## [URL](https://en.wikipedia.org/wiki/Fast_Ethernet) - https://en.wikipedia.org/wiki/Fast_Ethernet
## Catagories
### All accuracy disputes
### All articles lacking reliable references
### All articles with self-published sources
### Articles lacking reliable references from February 2021
### Articles with disputed statements from October 2021
### Articles with self-published sources from May 2020
### Articles with short description
### Ethernet
### Short description matches Wikidata
### "In computer networking, Fast Ethernet physical layers carry traffic at the nominal rate of 100 Mbit/s. The prior Ethernet speed was 10 Mbit/s. Of the Fast Ethernet physical layers, 100BASE-TX is by far the most common. 
### Fast Ethernet was introduced in 1995 as the IEEE 802.3u standard and remained the fastest version of Ethernet for three years before the introduction of Gigabit Ethernet. The acronym GE/FE is sometimes used for devices supporting both standards.
## Nomenclature  
### The \"100\" in the media type designation refers to the transmission speed of 100 Mbit/s, while the \"BASE\" refers to baseband signalling. The letter following the dash (\"T\" or \"F\") refers to the physical medium that carries the signal (twisted pair or fiber, respectively), while the last character (\"X\", \"4\", etc.) refers to the line code method used. Fast Ethernet is sometimes referred to as 100BASE-X, where \"X\" is a placeholder for the FX and TX variants.
## General design  
### Fast Ethernet is an extension of the 10 megabit Ethernet standard. It runs on twisted pair or optical fiber cable in a star wired bus topology, similar to the IEEE standard 802.3i called 10BASE-T, itself an evolution of 10BASE5 (802.3) and 10BASE2 (802.3a). Fast Ethernet devices are generally backward compatible with existing 10BASE-T systems, enabling plug-and-play upgrades from 10BASE-T. Most switches and other networking devices with ports capable of Fast Ethernet can perform autonegotiation, sensing a piece of 10BASE-T equipment and setting the port to 10BASE-T half duplex if the 10BASE-T equipment cannot perform auto negotiation itself. The standard specifies the use of CSMA/CD for media access control. A full-duplex mode is also specified and in practice all modern networks use Ethernet switches and operate in full-duplex mode, even as legacy devices that use half duplex still exist. 
### A Fast Ethernet adapter can be logically divided into a media access controller (MAC), which deals with the higher-level issues of medium availability, and a physical layer interface (PHY). The MAC is typically linked to the PHY by a four-bit 25 MHz synchronous parallel interface known as a media-independent interface (MII), or by a two-bit 50 MHz variant called reduced media independent interface (RMII). In rare cases the MII may be an external connection but is usually a connection between ICs in a network adapter or even two sections within a single IC. The specs are written based on the assumption that the interface between MAC and PHY will be an MII but they do not require it. Fast Ethernet or Ethernet hubs may use the MII to connect to multiple PHYs for their different interfaces. 
### The MII fixes the theoretical maximum data bit rate for all versions of Fast Ethernet to 100 Mbit/s. The information rate actually observed on real networks is less than the theoretical maximum, due to the necessary header and trailer (addressing and error-detection bits) on every Ethernet frame, and the required interpacket gap between transmissions.
## Copper  
### 100BASE-T is any of several Fast Ethernet standards for twisted pair cables, including: 100BASE-TX (100 Mbit/s over two-pair Cat5 or better cable), 100BASE-T4 (100 Mbit/s over four-pair Cat3 or better cable, defunct), 100BASE-T2 (100 Mbit/s over two-pair Cat3 or better cable, also defunct). The segment length for a 100BASE-T cable is limited to 100 metres (328 ft) (the same limit as 10BASE-T and gigabit Ethernet). All are or were standards under IEEE 802.3 (approved 1995). Almost all 100BASE-T installations are 100BASE-TX.
## 100BASE-TX  

### 100BASE-TX is the predominant form of Fast Ethernet, and runs over two wire-pairs inside a category 5 or above cable. Each network segment can have a maximum cabling distance of 100 metres (328 ft). One pair is used for each direction, providing full-duplex operation with 100 Mbit/s of throughput in each direction. 
### Like 10BASE-T, the active pairs in a standard connection are terminated on pins 1, 2, 3 and 6. Since a typical category 5 cable contains 4 pairs, it can support two 100BASE-TX links with a wiring adaptor. Cabling is conventional wired to ANSI/TIA-568's termination standards, T568A or T568B. This places the active pairs on the orange and green pairs (canonical second and third pairs). 
### The configuration of 100BASE-TX networks is very similar to 10BASE-T. When used to build a local area network, the devices on the network (computers, printers etc.) are typically connected to a hub or switch, creating a star network. Alternatively it is possible to connect two devices directly using a crossover cable. With today's equipment, crossover cables are generally not needed as most equipment support auto-negotiation along with auto MDI-X to select and match speed, duplex and pairing. 
### With 100BASE-TX hardware, the raw bits, presented 4 bits wide clocked at 25 MHz at the MII, go through 4B5B binary encoding to generate a series of 0 and 1 symbols clocked at a 125 MHz symbol rate. The 4B5B encoding provides DC equalization and spectrum shaping. Just as in the 100BASE-FX case, the bits are then transferred to the physical medium attachment layer using NRZI encoding. However, 100BASE-TX introduces an additional, medium dependent sublayer, which employs MLT-3 as a final encoding of the data stream before transmission, resulting in a maximum fundamental frequency of 31.25 MHz. The procedure is borrowed from the ANSI X3.263 FDDI specifications, with minor changes.
## 100BASE-T1  

### In 100BASE-T1 the data is transmitted over a single copper pair, 3 bits per symbol, each transmitted as code pair using PAM3. It supports only full-duplex, transmitting in both directions simultaneously. The twisted-pair cable is required to support 66 MHz, with a maximum length of 15 m. No specific connector is defined. The standard is intended for automotive applications or when Fast Ethernet is to be integrated into another application. It was developed as BroadR-Reach before IEEE standardization.
## 100BASE-T2  
### In 100BASE-T2, standardized in IEEE 802.3y, the data is transmitted over two copper pairs, but these pairs are only required to be category 3 rather than the category 5 required by 100BASE-TX. Data is transmitted and received on both pairs simultaneously thus allowing full-duplex operation. Transmission uses 4 bits per symbol. The 4-bit symbol is expanded into two 3-bit symbols through a non-trivial scrambling procedure based on a linear-feedback shift register. This is needed to flatten the bandwidth and emission spectrum of the signal, as well as to match transmission line properties. The mapping of the original bits to the symbol codes is not constant in time and has a fairly large period (appearing as a pseudo-random sequence). The final mapping from symbols to PAM-5 line modulation levels obeys the table on the right. 100BASE-T2 was not widely adopted but the technology developed for it is used in 1000BASE-T.
## 100BASE-T4  
### 100BASE-T4 was an early implementation of Fast Ethernet.  It requires four twisted copper pairs of voice grade twisted pair, a lower performing cable compared to category 5 cable used by 100BASE-TX. Maximum distance is limited to 100 meters. One pair is reserved for transmit, one for receive, and the remaining two switch direction. The fact that 3 pairs are used to transmit in each direction makes 100BASE-T4 inherently half-duplex. 
### A very unusual 8B6T code is used to convert 8 data bits into 6 base-3 digits (the signal shaping is possible as there are nearly three times as many 6-digit base-3 numbers as there are 8-digit base-2 numbers). The two resulting 3-digit base-3 symbols are sent in parallel over 3 pairs using 3-level pulse-amplitude modulation (PAM-3). 
### 100BASE-T4 was not widely adopted but some of the technology developed for it is used in 1000BASE-T.
## 100BaseVG  

### Proposed and marketed by Hewlett Packard, 100BaseVG was an alternative design using category 3 cabling and a token concept instead of CSMA/CD. It was slated for standardization as IEEE 802.12 but it quickly vanished when switched 100BASE-TX became popular.
## Fiber optics 
## Fast Ethernet SFP ports  
### Fast Ethernet speed is not available on all SFP ports, but supported by some devices. An SFP port for Gigabit Ethernet should not be assumed to be backwards compatible with Fast Ethernet.
## Optical interoperability  
### To have interoperable there is some criteria that have to be meet: 
### Line encoding 
### Wavelength 
### Duplex mode 
### Media count 
### Media type and dimension100BASE-X Ethernet is not backward compatible with 10BASE-F and is not forward compatible with 1000BASE-X.
## 100BASE-FX  
### 100BASE-FX is a version of Fast Ethernet over optical fiber. The 100BASE-FX Physical Medium Dependent (PMD) sublayer is defined by FDDI's PMD, so 100BASE-FX is not compatible with 10BASE-FL, the 10 Mbit/s version over optical fiber. 
### 100BASE-FX is still used for existing installation of multimode fiber where more speed is not required, like industrial automation plants.
## 100BASE-LFX  
### 100BASE-LFX is a non-standard term to refer to Fast Ethernet transmission. It is very similar to 100BASE-FX but achieves longer distances up to 4-5 km over a pair of multi-mode fibers through the use of Fabry\u2013P\u00e9rot laser transmitter running on 1310 nm wavelength. The signal attenuation per km at 1300 nm is about half the loss of 850nm.
## 100BASE-SX  
### 100BASE-SX is a version of Fast Ethernet over optical fiber standardized in TIA/EIA-785-1-2002. It is a lower-cost, shorter-distance alternative to 100BASE-FX. Because of the shorter wavelength used (850 nm) and the shorter distance supported, 100BASE-SX uses less expensive optical components (LEDs instead of lasers). 
### Because it uses the same wavelength as 10BASE-FL, the 10 Mbit/s version of Ethernet over optical fiber, 100BASE-SX can be backward-compatible with 10BASE-FL. Cost and compatibility makes 100BASE-SX an attractive option for those upgrading from 10BASE-FL and those who do not require long distances.
## 100BASE-LX10  
### 100BASE-LX10 is a version of Fast Ethernet over optical fiber standardized in 802.3ah-2004 clause 58. It has a 10 km reach over a pair of single-mode fibers.
## 100BASE-BX10  
### 100BASE-BX10 is a version of Fast Ethernet over optical fiber standardized in 802.3ah-2004 clause 58. It uses an optical multiplexer to split TX and RX signals into different wavelengths on the same fiber. It has a 10 km reach over a single strand of single-mode fiber.
## 100BASE-EX  
### 100BASE-EX is very similar to 100BASE-LX10 but achieves longer distances up to 40 km over a pair of single-mode fibers due to higher quality optics than a LX10, running on 1310 nm wavelength lasers. 100BASE-EX is not a formal standard but industry-accepted term. It is sometimes referred to as 100BASE-LH (long haul), and is easily confused with 100BASE-LX10 or 100BASE-ZX because the use of -LX(10), -LH, -EX, and -ZX is ambiguous between vendors.
## 100BASE-ZX  
### 100BASE-ZX is a non-standard but multi-vendor term to refer to Fast Ethernet transmission using 1,550 nm wavelength to achieve distances of at least 70 km over single-mode fiber. Some vendors specify distances up to 160 km over single-mode fiber, sometimes called 100BASE-EZX. Ranges beyond 80 km are highly dependent upon the path loss of the fiber in use, specifically the attenuation figure in dB per km, the number and quality of connectors/patch panels and splices located between transceivers.
## See also  
### List of device bandwidths
## Notes 
## References 
## External links  
### Common 100 Mbit/s Hardware Variations 
### Origins and History of Ethernet 
### IEEE802.3 standards free download 
### ProCurve Networking 100BASE-FX Technical Brief"
## References
### [Reference](http://www.cisco.com/c/en/us/products/collateral/interfaces-modules/fast-ethernet-sfp-modules/product_data_sheet0900aecd801f931c.html) - http://www.cisco.com/c/en/us/products/collateral/interfaces-modules/fast-ethernet-sfp-modules/product_data_sheet0900aecd801f931c.html
### [Reference](http://www.eetimes.com/document.asp?doc_id=1328371) - http://www.eetimes.com/document.asp?doc_id=1328371
### [Reference](http://www.inetdaemon.com/tutorials/networking/lan/ethernet/origins.shtml) - http://www.inetdaemon.com/tutorials/networking/lan/ethernet/origins.shtml
### [Reference](http://www.trinetusa.com/images/catalog/pages31-40.pdf) - http://www.trinetusa.com/images/catalog/pages31-40.pdf
### [Reference](http://doi.org/10.1109%2F65.690946) - http://doi.org/10.1109%2F65.690946
### [Reference](http://doi.org/10.1109%2FIEEESTD.1995.7974916) - http://doi.org/10.1109%2FIEEESTD.1995.7974916
### [Reference](https://arstechnica.com/civis/viewtopic.php?p=6647265&sid=1207bc662946d0bf8ff15eac6753a819#p6647265) - https://arstechnica.com/civis/viewtopic.php?p=6647265&sid=1207bc662946d0bf8ff15eac6753a819#p6647265
### [Reference](https://www.ccontrols.com/pdf/ExtV2N6.pdf) - https://www.ccontrols.com/pdf/ExtV2N6.pdf
### [Reference](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/fast-ethernet-sfp-modules/product_data_sheet0900aecd801f931c.html) - https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/fast-ethernet-sfp-modules/product_data_sheet0900aecd801f931c.html
### [Reference](https://www.cisco.com/c/en_in/products/collateral/switches/small-business-smart-switches/data-sheet-c78-737359.html) - https://www.cisco.com/c/en_in/products/collateral/switches/small-business-smart-switches/data-sheet-c78-737359.html
### [Reference](https://www.flukenetworks.com/knowledge-base/copper-testing/om1-om2-om3-om4-om5-and-os1-os2-fiber) - https://www.flukenetworks.com/knowledge-base/copper-testing/om1-om2-om3-om4-om5-and-os1-os2-fiber
### [Reference](https://www.fs.com/de-en/products/12678.html) - https://www.fs.com/de-en/products/12678.html
### [Reference](https://www.fs.com/products/12672.html) - https://www.fs.com/products/12672.html
### [Reference](https://www.fs.com/products/12679.html) - https://www.fs.com/products/12679.html
### [Reference](https://www.fs.com/products/37324.html) - https://www.fs.com/products/37324.html
### [Reference](https://www.moxa.com/en/products/industrial-network-infrastructure/ethernet-switches/layer-2-managed-switches/eds-408a-series/eds-408a-mm-st) - https://www.moxa.com/en/products/industrial-network-infrastructure/ethernet-switches/layer-2-managed-switches/eds-408a-series/eds-408a-mm-st
### [Reference](https://www.moxa.com/getmedia/97d0d84d-3574-4456-a8b1-ee24aeaf04fc/moxa-sfp-1fe-series-datasheet-v1.0.pdf) - https://www.moxa.com/getmedia/97d0d84d-3574-4456-a8b1-ee24aeaf04fc/moxa-sfp-1fe-series-datasheet-v1.0.pdf
### [Reference](https://www.skylaneoptics.com/en/product/sfp15160fe0b-sfp-100base-ezx/) - https://www.skylaneoptics.com/en/product/sfp15160fe0b-sfp-100base-ezx/
### [Reference](https://www.juniper.net/techpubs/hardware/erx/junose103/hw-erx-module/oc3-ge-fe-w-aps.html) - https://www.juniper.net/techpubs/hardware/erx/junose103/hw-erx-module/oc3-ge-fe-w-aps.html
### [Reference](https://web.archive.org/web/20080916221133/http://www.cs.bsu.edu/homepages/peb/cs637/ethernet/100mbps.htm) - https://web.archive.org/web/20080916221133/http://www.cs.bsu.edu/homepages/peb/cs637/ethernet/100mbps.htm
### [Reference](https://web.archive.org/web/20121009212203/http://www.hp.com/rnd/pdfs/100FXtechbrief.pdf) - https://web.archive.org/web/20121009212203/http://www.hp.com/rnd/pdfs/100FXtechbrief.pdf
### [Reference](https://web.archive.org/web/20140707221928/http://www.trinetusa.com/images/catalog/pages31-40.pdf) - https://web.archive.org/web/20140707221928/http://www.trinetusa.com/images/catalog/pages31-40.pdf
### [Reference](https://web.archive.org/web/20200819045024/https://www.skylaneoptics.com/en/product/sfp15160fe0b-sfp-100base-ezx/) - https://web.archive.org/web/20200819045024/https://www.skylaneoptics.com/en/product/sfp15160fe0b-sfp-100base-ezx/
### [Reference](https://ieeexplore.ieee.org/browse/standards/get-program/page/series?id=68) - https://ieeexplore.ieee.org/browse/standards/get-program/page/series?id=68
### [Reference](https://archive.nanog.org/sites/default/files/Steenbergen.Everything_You_Need.pdf) - https://archive.nanog.org/sites/default/files/Steenbergen.Everything_You_Need.pdf
### [Reference](https://www.stl.tech/connectivity-solution/optical-fibre/pdf/Differences_between_OM1__OM2__OM3__OM4_.pdf) - https://www.stl.tech/connectivity-solution/optical-fibre/pdf/Differences_between_OM1__OM2__OM3__OM4_.pdf
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/f/f2/3Com_3C905B.jpg) - https://upload.wikimedia.org/wikipedia/commons/f/f2/3Com_3C905B.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/8/89/Intel_Pro-100_82558_PCI_NIC.jpg) - https://upload.wikimedia.org/wikipedia/commons/8/89/Intel_Pro-100_82558_PCI_NIC.jpg
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