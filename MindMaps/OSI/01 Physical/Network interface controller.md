# Network interface controller
## [URL](https://en.wikipedia.org/wiki/Network_interface_controller) - https://en.wikipedia.org/wiki/Network_interface_controller
## Catagories
### All articles containing potentially dated statements
### Articles containing potentially dated statements from November 2014
### Articles with short description
### Ethernet
### Networking hardware
### Short description is different from Wikidata
### "A network interface controller (NIC, also known as a network interface card, network adapter, LAN adapter or physical network interface, and by similar terms) is a computer hardware component that connects a computer to a computer network.Early network interface controllers were commonly implemented on expansion cards that plugged into a computer bus. The low cost and ubiquity of the Ethernet standard means that most newer computers have a network interface built into the motherboard, or is contained into a USB-connected dongle. 
### Modern network interface controllers offer advanced features such as interrupt and DMA interfaces to the host processors, support for multiple receive and transmit queues, partitioning into multiple logical interfaces, and on-controller network traffic processing such as the TCP offload engine.
## Purpose  
### The network controller implements the electronic circuitry required to communicate using a specific physical layer and data link layer standard such as Ethernet or Wi-Fi. This provides a base for a full network protocol stack, allowing communication among computers on the same local area network (LAN) and large-scale network communications through routable protocols, such as Internet Protocol (IP). 
### The NIC allows computers to communicate over a computer network, either by using cables or wirelessly. The NIC is both a physical layer and data link layer device, as it provides physical access to a networking medium and, for IEEE 802 and similar networks, provides a low-level addressing system through the use of MAC addresses that are uniquely assigned to network interfaces.
## Implementation  

### Network controllers were originally implemented as expansion cards that plugged into a computer bus. The low cost and ubiquity of the Ethernet standard means that most new computers have a network interface controller built into the motherboard. Newer server motherboards may have multiple network interfaces built-in. The Ethernet capabilities are either integrated into the motherboard chipset or implemented via a low-cost dedicated Ethernet chip. A separate network card is typically no longer required unless additional independent network connections are needed or some non-Ethernet type of network is used. A general trend in computer hardware is towards integrating the various components of systems on a chip, and this is also applied to network interface cards. 
### An Ethernet network controller typically has an 8P8C socket where the network cable is connected. Older NICs also supplied BNC, or AUI connections. Ethernet network controllers typically support 10 Mbit/s Ethernet, 100 Mbit/s Ethernet, and 1000 Mbit/s Ethernet varieties. Such controllers are designated as 10/100/1000, meaning that they can support data rates of 10, 100 or 1000 Mbit/s. 10 Gigabit Ethernet NICs are also available, and, as of November 2014, are beginning to be available on computer motherboards. 

### Modular designs like SFP and SFP+ are highly popular, especially for fiber-optic communication. These define a standard receptacle for media-dependent transceivers, so users can easily adapt the network interface to their needs. 
### LEDs adjacent to or integrated into the network connector inform the user of whether the network is connected, and when data activity occurs. 
### The NIC may use one or more of the following techniques to indicate the availability of packets to transfer: 

### Polling is where the CPU examines the status of the peripheral under program control. 
### Interrupt-driven I/O is where the peripheral alerts the CPU that it is ready to transfer data.NICs may use one or more of the following techniques to transfer packet data: 

### Programmed input/output, where the CPU moves the data to or from the NIC to memory. 
### Direct memory access (DMA), where a device other than the CPU assumes control of the system bus to move data to or from the NIC to memory. This removes load from the CPU but requires more logic on the card. In addition, a packet buffer on the NIC may not be required and latency can be reduced.
## Performance and advanced functionality  

### Multiqueue NICs provide multiple transmit and receive queues, allowing packets received by the NIC to be assigned to one of its receive queues. The NIC may distribute incoming traffic between the receive queues using a hash function. Each receive queue is assigned to a separate interrupt; by routing each of those interrupts to different CPUs or CPU cores, processing of the interrupt requests triggered by the network traffic received by a single NIC can be distributed improving performance.The hardware-based distribution of the interrupts, described above, is referred to as receive-side scaling (RSS).:\u200a82\u200a Purely software implementations also exist, such as the receive packet steering (RPS) and receive flow steering (RFS). Further performance improvements can be achieved by routing the interrupt requests to the CPUs or cores executing the applications that are the ultimate destinations for network packets that generated the interrupts. This technique improves Locality of reference and results in higher overall performance, reduced latency and better hardware utilization because of the higher utilization of CPU caches and fewer required context switches. Examples of such implementations are the RFS and Intel Flow Director.:\u200a98,\u200a99\u200aWith multi-queue NICs, additional performance improvements can be achieved by distributing outgoing traffic among different transmit queues. By assigning different transmit queues to different CPUs or CPU cores, internal operating system contentions can be avoided. This approach is usually referred to as transmit packet steering (XPS).Some products feature NIC partitioning (NPAR, also known as port partitioning) that uses SR-IOV virtualization to divide a single 10 Gigabit Ethernet NIC into multiple discrete virtual NICs with dedicated bandwidth, which are presented to the firmware and operating system as separate PCI device functions.TCP offload engine is a technology used in some NICs to offload processing of the entire TCP/IP stack to the network controller. It is primarily used with high-speed network interfaces, such as Gigabit Ethernet and 10 Gigabit Ethernet, for which the processing overhead of the network stack becomes significant. 
### Some NICs offer integrated field-programmable gate arrays (FPGAs) for user-programmable processing of network traffic before it reaches the host computer, allowing for significantly reduced latencies in time-sensitive workloads. Moreover, some NICs offer complete low-latency TCP/IP stacks running on integrated FPGAs in combination with userspace libraries that intercept networking operations usually performed by the operating system kernel; Solarflare's open-source OpenOnload network stack that runs on Linux is an example. This kind of functionality is usually referred to as user-level networking.
## See also  
### Converged network adapter (CNA) 
### Host adapter 
### Intel Data Direct I/O (DDIO) 
### Loopback interface 
### Network monitoring interface card (NMIC) 
### Virtual network interface (VIF) 
### Wireless network interface controller (WNIC)
## Notes 
## References 
## External links  
### \"Physical Network Interface\". Microsoft. 
### \"Predictable Network Interface Names\". Freedesktop.org. 
### Multi-queue network interfaces with SMP on Linux"
## Links
### 10/100/1000
### 10BASE-T
### 10BASE2
### 10 Gigabit Ethernet
### 8P8C
### ARCNET
### Asynchronous Transfer Mode
### Attachment Unit Interface
### Avago
### BNC connector
### Blu-ray
### Broadcom
### CPU
### CPU cache
### Cavium
### Central processing unit
### Chelsio
### Chipset
### Compact disc
### Computer
### Computer bus
### Computer case
### Computer data storage
### Computer hardware
### Computer keyboard
### Computer memory
### Computer monitor
### Computer motherboard
### Computer mouse
### Computer network
### Computer port (hardware)
### Computer speakers
### Context switch
### Converged network adapter
### DVD
### Data link layer
### Dell
### Digital Visual Interface
### Direct memory access
### Disk pack
### DisplayPort
### Dongle
### Electronic visual display
### Emulex
### Ethernet
### Expansion card
### Fast Ethernet
### Fax modem
### Fiber-optic communication
### Fiber Distributed Data Interface
### Fibre Channel
### Field-programmable gate array
### FireWire
### Flash memory
### Floppy disk
### Freedesktop.org
### Full-duplex
### Game controller
### Gigabit Ethernet
### Graphics card
### Graphics processing unit
### Graphics tablet
### HDMI
### Half-duplex
### Hard disk drive
### Hash function
### Host adapter
### IEEE 1394
### IEEE 802
### IEEE 802.11
### IEEE 802.3
### ISA bus
### Image scanner
### Industry Standard Architecture
### Input device
### Integrated circuit
### Intel
### Intel Data Direct I/O
### Internet Protocol
### Interrupt
### Interrupt request
### Kernel.org
### LWN.net
### Latency (engineering)
### Light-emitting diode
### Light pen
### Linux
### Local area network
### Locality of reference
### Loopback interface
### M.2
### MAC address
### MOSFET
### Marvell Technology Group
### Megabit per second
### Mellanox
### Memory card
### Microphone
### Microprocessor
### Microsoft
### Mini PCIe
### Modem
### Motherboard
### Multi-core processor
### NVM Express
### Network Railcard
### Network card
### Network monitoring interface card
### Network packet
### Nonvolatile BIOS memory
### Operating system kernel
### Optical disc
### Optical mouse
### Optical trackpad
### Output device
### PCI device function
### PCIe
### PS/2 port
### Parallel port
### Peripheral
### Peripheral Component Interconnect
### Phone connector (audio)
### Physical layer
### Plotter
### Pointing device
### Pointing stick
### Polling (computer science)
### Power MOSFET
### Power supply unit (computer)
### Printer (computing)
### Programmed input/output
### Protocol stack
### QLogic
### Qlogic
### Queue (abstract data type)
### Random-access memory
### Realtek
### Receive flow steering
### Receive packet steering
### Refreshable braille display
### Removable media
### SATA
### SR-IOV
### Serial ATA
### Serial port
### Server (computing)
### Small form-factor pluggable transceiver
### Softcam
### Solid-state drive
### Solid-state hybrid drive
### Sound card
### Sound chip
### Switched-mode power supply
### System bus
### System on a chip
### TCP/IP
### TCP/IP stack
### TCP offload engine
### The Register
### Thunderbolt (interface)
### Token Ring
### Touchpad
### Touchscreen
### Trackball
### USB
### USB flash drive
### Userspace
### VGA connector
### Virtual network interface
### Voltage regulator module
### Webcam
### Wi-Fi
### Wireless network interface controller
## References
### [Reference](http://www.asrock.com/news/index.asp?id=2517) - http://www.asrock.com/news/index.asp?id=2517
### [Reference](http://www.dell.com/downloads/global/products/pedge/en/Dell-Broadcom-NPAR-White-Paper.pdf) - http://www.dell.com/downloads/global/products/pedge/en/Dell-Broadcom-NPAR-White-Paper.pdf
### [Reference](http://www.intel.com/content/dam/doc/datasheet/82574l-gbe-controller-datasheet.pdf) - http://www.intel.com/content/dam/doc/datasheet/82574l-gbe-controller-datasheet.pdf
### [Reference](http://www.intel.com/content/dam/technology-provider/secure/us/en/documents/product-marketing-information/tst-grantley-launch-presentation-2014.pdf) - http://www.intel.com/content/dam/technology-provider/secure/us/en/documents/product-marketing-information/tst-grantley-launch-presentation-2014.pdf
### [Reference](http://www.intel.com/content/dam/www/public/us/en/documents/white-papers/intel-ethernet-flow-director.pdf) - http://www.intel.com/content/dam/www/public/us/en/documents/white-papers/intel-ethernet-flow-director.pdf
### [Reference](http://www.intel.com/content/dam/www/public/us/en/documents/solution-briefs/10-gbe-ethernet-flexible-port-partitioning-brief.pdf) - http://www.intel.com/content/dam/www/public/us/en/documents/solution-briefs/10-gbe-ethernet-flexible-port-partitioning-brief.pdf
### [Reference](http://www.intel.com/content/www/us/en/ethernet-controllers/ethernet-flow-director-video.html) - http://www.intel.com/content/www/us/en/ethernet-controllers/ethernet-flow-director-video.html
### [Reference](http://www.mouser.com/pdfdocs/i210brief.pdf) - http://www.mouser.com/pdfdocs/i210brief.pdf
### [Reference](http://www.networkcomputing.com/networking/will-2014-be-the--year-of-10-gigabit-ethernet/a/d-id/1234640?) - http://www.networkcomputing.com/networking/will-2014-be-the--year-of-10-gigabit-ethernet/a/d-id/1234640?
### [Reference](http://newwavedv.com/markets/defense/cyber-security/) - http://newwavedv.com/markets/defense/cyber-security/
### [Reference](http://docs.ruckuswireless.com/fastiron/08.0.70/fastiron-08070-managementguide/GUID-EDD7D44C-A627-4B76-A9FE-D7657FFF62D3.html) - http://docs.ruckuswireless.com/fastiron/08.0.70/fastiron-08070-managementguide/GUID-EDD7D44C-A627-4B76-A9FE-D7657FFF62D3.html
### [Reference](http://www.windowsnetworking.com/articles_tutorials/networking-basics-part1.html) - http://www.windowsnetworking.com/articles_tutorials/networking-basics-part1.html
### [Reference](http://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames/) - http://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames/
### [Reference](http://www.openonload.org/) - http://www.openonload.org/
### [Reference](http://www.openonload.org/openonload-google-talk.pdf) - http://www.openonload.org/openonload-google-talk.pdf
### [Reference](https://www.arista.com/en/um-eos/eos-section-11-2-ethernet-standards) - https://www.arista.com/en/um-eos/eos-section-11-2-ethernet-standards
### [Reference](https://technet.microsoft.com/en-us/library/dd392944(v=ws.10).aspx) - https://technet.microsoft.com/en-us/library/dd392944(v=ws.10).aspx
### [Reference](https://lwn.net/Articles/243949/) - https://lwn.net/Articles/243949/
### [Reference](https://greenhost.nl/2013/04/10/multi-queue-network-interfaces-with-smp-on-linux/) - https://greenhost.nl/2013/04/10/multi-queue-network-interfaces-with-smp-on-linux/
### [Reference](https://web.archive.org/web/20150326095816/http://www.intel.com/content/dam/technology-provider/secure/us/en/documents/product-marketing-information/tst-grantley-launch-presentation-2014.pdf) - https://web.archive.org/web/20150326095816/http://www.intel.com/content/dam/technology-provider/secure/us/en/documents/product-marketing-information/tst-grantley-launch-presentation-2014.pdf
### [Reference](https://www.kernel.org/doc/Documentation/networking/ixgbe.txt) - https://www.kernel.org/doc/Documentation/networking/ixgbe.txt
### [Reference](https://www.kernel.org/doc/Documentation/networking/scaling.txt) - https://www.kernel.org/doc/Documentation/networking/scaling.txt
### [Reference](https://www.theregister.co.uk/2012/02/08/solarflare_application_onload_engine/) - https://www.theregister.co.uk/2012/02/08/solarflare_application_onload_engine/
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/a/aa/12_early_PC_network_cards.jpg) - https://upload.wikimedia.org/wikipedia/commons/a/aa/12_early_PC_network_cards.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/2/24/An_Intel_82574L_Gigabit_Ethernet_NIC%2C_PCI_Express_x1_card.jpg) - https://upload.wikimedia.org/wikipedia/commons/2/24/An_Intel_82574L_Gigabit_Ethernet_NIC%2C_PCI_Express_x1_card.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/6/6c/ForeRunnerLE_25_ATM_Network_Interface_%281%29.jpg) - https://upload.wikimedia.org/wikipedia/commons/6/6c/ForeRunnerLE_25_ATM_Network_Interface_%281%29.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/9/9e/Network_card.jpg) - https://upload.wikimedia.org/wikipedia/commons/9/9e/Network_card.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/4/4a/Qle3442-cu_10gbe_nic.jpg) - https://upload.wikimedia.org/wikipedia/commons/4/4a/Qle3442-cu_10gbe_nic.jpg