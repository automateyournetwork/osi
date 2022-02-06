# Firewall (computing)
## [URL](https://en.wikipedia.org/wiki/Firewall_(computing)) - https://en.wikipedia.org/wiki/Firewall_(computing)
## Catagories
### All articles with unsourced statements
### American inventions
### Articles with GND identifiers
### Articles with LCCN identifiers
### Articles with short description
### Articles with unsourced statements from August 2020
### Commons category link is on Wikidata
### Cyberwarfare
### Data security
### Firewall software
### Network management
### Packets (information technology)
### Short description is different from Wikidata
### "In computing, a firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. A firewall typically establishes a barrier between a trusted network and an untrusted network, such as the Internet.
## History  
### The term firewall originally referred to a wall intended to confine a fire within a line of adjacent buildings. Later uses refer to similar structures, such as the metal sheet separating the engine compartment of a vehicle or aircraft from the passenger compartment. The term was applied in the late 1980s to network technology  that emerged when the Internet was fairly new in terms of its global use and connectivity. The predecessors to firewalls for network security were routers used in the late 1980s. Because they already segregated networks, routers could apply filtering to packets crossing them.Before it was used in real-life computing, the term appeared in the 1983 computer-hacking movie WarGames, and possibly inspired its later use.
## Types  

### Firewalls are categorized as a network-based or a host-based system. Network-based firewalls can be positioned anywhere within a LAN or WAN. They are either a software appliance running on general-purpose hardware, a hardware appliance running on special-purpose hardware, or a virtual appliance running on a virtual host controlled by a hypervisor. Firewall appliances may also offer non firewall functionality, such as DHCP or VPN services. Host-based firewalls are deployed directly on the host itself to control network traffic or other computing resources. This can be a daemon or service as a part of the operating system or an agent application for protection.
## Packet filter  
### The first reported type of network firewall is called a packet filter, which inspect packets transferred between computers. The firewall maintains an access control list which dictates what packets will be looked at and what action should be applied, if any, with the default action set to silent discard. Three basic actions regarding the packet consist of a silent discard, discard with Internet Control Message Protocol or TCP reset response to the sender, and forward to the next hop. Packets may be filtered by source and destination IP addresses, protocol, source and destination ports. The bulk of Internet communication in 20th and early 21st century used either Transmission Control Protocol (TCP) or User Datagram Protocol (UDP) in conjunction with well-known ports, enabling firewalls of that era to distinguish between specific types of traffic such as web browsing, remote printing, email transmission, and file transfers.The first paper published on firewall technology was in 1987 when engineers from Digital Equipment Corporation (DEC) developed filter systems known as packet filter firewalls. At AT&T Bell Labs, Bill Cheswick and Steve Bellovin continued their research in packet filtering and developed a working model for their own company based on their original first-generation architecture.
## Connection tracking  

### From 1989\u20131990, three colleagues from AT&T Bell Laboratories, Dave Presotto, Janardan Sharma, and Kshitij Nigam, developed the second generation of firewalls, calling them circuit-level gateways.Second-generation firewalls perform the work of their first-generation predecessors but also maintain knowledge of specific conversations between endpoints by remembering which port number the two IP addresses are using at layer 4 (transport layer) of the OSI model for their conversation, allowing examination of the overall exchange between the nodes.
## Application layer  

### Marcus Ranum, Wei Xu, and Peter Churchyard released an application firewall known as Firewall Toolkit (FWTK) in October 1993. This became the basis for Gauntlet firewall at Trusted Information Systems.The key benefit of application layer filtering is that it can understand certain applications and protocols such as File Transfer Protocol (FTP), Domain Name System (DNS), or Hypertext Transfer Protocol (HTTP). This allows it to identify unwanted applications or services using a non standard port, or detect if an allowed protocol is being abused. It can also provide unified security management including enforced encrypted DNS and virtual private networking.As of 2012, the next-generation firewall provides a wider range of inspection at the application layer, extending deep packet inspection functionality to include, but is not limited to: 

### Web filtering 
### Intrusion prevention systems 
### User identity management 
### Web application firewall
## Endpoint specific  
### Endpoint based application firewalls function by determining whether a process should accept any given connection. Application firewalls filter connections by examining the process ID of data packets against a rule set for the local process involved in the data transmission. Application firewalls accomplish their function by hooking into socket calls to filter the connections between the application layer and the lower layers. Application firewalls that hook into socket calls are also referred to as socket filters.
## Configuration  
### Setting up a firewall is a complex and error-prone task. A network may face security issues due to configuration errors.
## See also 
## References 
## External links  
### Evolution of the Firewall Industry \u2013 discusses different architectures, how packets are processed, and provides a timeline of the evolution. 
### A History and Survey of Network Firewalls \u2013 provides an overview of firewalls at various ISO levels, with references to original papers where early firewall work was reported."
## References
### [Reference](http://www.avolio.com/papers/FWTKv1.0Announcement.html) - http://www.avolio.com/papers/FWTKv1.0Announcement.html
### [Reference](http://www.avolio.com/papers/fwtk-history.html) - http://www.avolio.com/papers/fwtk-history.html
### [Reference](http://www.tech-faq.com/firewall.html) - http://www.tech-faq.com/firewall.html
### [Reference](http://www.cs.unm.edu/~treport/tr/02-12/firewall.pdf) - http://www.cs.unm.edu/~treport/tr/02-12/firewall.pdf
### [Reference](http://www.shorewall.net/dhcp.htm) - http://www.shorewall.net/dhcp.htm
### [Reference](http://www.skullbox.net/tcpudp.php) - http://www.skullbox.net/tcpudp.php
### [Reference](http://doi.org/10.1145%2F253769.253802) - http://doi.org/10.1145%2F253769.253802
### [Reference](http://doi.org/10.1145%2F3130876) - http://doi.org/10.1145%2F3130876
### [Reference](http://dx.doi.org/10.1145/3130876) - http://dx.doi.org/10.1145/3130876
### [Reference](http://www.worldcat.org/issn/0360-0300) - http://www.worldcat.org/issn/0360-0300
### [Reference](http://docstore.mik.ua/univercd/cc/td/doc/product/iaabu/centri4/user/scf4ch3.htm) - http://docstore.mik.ua/univercd/cc/td/doc/product/iaabu/centri4/user/scf4ch3.htm
### [Reference](https://www.checkpoint.com/cyber-hub/network-security/what-is-firewall/5-firewall-features-you-must-have/) - https://www.checkpoint.com/cyber-hub/network-security/what-is-firewall/5-firewall-features-you-must-have/
### [Reference](https://www.cloudflare.com/learning/ddos/what-is-layer-7/) - https://www.cloudflare.com/learning/ddos/what-is-layer-7/
### [Reference](https://personalfirewall.comodo.com/what-is-firewall.html) - https://personalfirewall.comodo.com/what-is-firewall.html
### [Reference](https://blogs.gartner.com/john_pescatore/2008/10/02/this-week-in-network-security-history-the-firewall-toolkit/) - https://blogs.gartner.com/john_pescatore/2008/10/02/this-week-in-network-security-history-the-firewall-toolkit/
### [Reference](https://books.google.com/books?id=TnJk09xmdFsC&pg=PA513) - https://books.google.com/books?id=TnJk09xmdFsC&pg=PA513
### [Reference](https://paloaltonetworks.com/documentation/70/pan-os/pan-os/networking/firewall-as-a-dhcp-server-and-client.html) - https://paloaltonetworks.com/documentation/70/pan-os/pan-os/networking/firewall-as-a-dhcp-server-and-client.html
### [Reference](https://www.paloaltonetworks.com/documentation/glossary/what-is-a-firewall) - https://www.paloaltonetworks.com/documentation/glossary/what-is-a-firewall
### [Reference](https://screenrant.com/80s-sci-fi-movies-predicted-the-future/) - https://screenrant.com/80s-sci-fi-movies-predicted-the-future/
### [Reference](https://www.stanfieldit.com/11-firewall-features/) - https://www.stanfieldit.com/11-firewall-features/
### [Reference](https://www.techopedia.com/definition/30753/vpn-firewall) - https://www.techopedia.com/definition/30753/vpn-firewall
### [Reference](https://id.loc.gov/authorities/subjects/sh00006011) - https://id.loc.gov/authorities/subjects/sh00006011
### [Reference](https://d-nb.info/gnd/4386332-2) - https://d-nb.info/gnd/4386332-2
### [Reference](https://safing.io/portmaster/) - https://safing.io/portmaster/
### [Reference](https://archive.org/details/securitymobileco00boud) - https://archive.org/details/securitymobileco00boud
### [Reference](https://archive.org/details/securitymobileco00boud/page/n66) - https://archive.org/details/securitymobileco00boud/page/n66
### [Reference](https://web.archive.org/web/20160429131516/http://blogs.gartner.com/john_pescatore/2008/10/02/this-week-in-network-security-history-the-firewall-toolkit/) - https://web.archive.org/web/20160429131516/http://blogs.gartner.com/john_pescatore/2008/10/02/this-week-in-network-security-history-the-firewall-toolkit/
### [Reference](https://api.semanticscholar.org/CorpusID:15271915) - https://api.semanticscholar.org/CorpusID:15271915
### [Reference](https://api.semanticscholar.org/CorpusID:6570517) - https://api.semanticscholar.org/CorpusID:6570517
### [Reference](https://www.wikidata.org/wiki/Q80998#identifiers) - https://www.wikidata.org/wiki/Q80998#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/c/c5/CIAJMK1209-en.svg) - https://upload.wikimedia.org/wikipedia/commons/c/c5/CIAJMK1209-en.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/5/5b/Firewall.png) - https://upload.wikimedia.org/wikipedia/commons/5/5b/Firewall.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/37/Netfilter-packet-flow.svg) - https://upload.wikimedia.org/wikipedia/commons/3/37/Netfilter-packet-flow.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/df/Wikibooks-logo-en-noslogan.svg) - https://upload.wikimedia.org/wikipedia/commons/d/df/Wikibooks-logo-en-noslogan.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg) - https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg