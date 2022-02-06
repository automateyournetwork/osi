# Autonomous system (Internet)
## [URL](https://en.wikipedia.org/wiki/Autonomous_system_(Internet)) - https://en.wikipedia.org/wiki/Autonomous_system_(Internet)
## Catagories
### AC with 0 elements
### Articles with short description
### Internet architecture
### Short description is different from Wikidata
### Wikipedia articles needing clarification from January 2016
### Wikipedia articles needing clarification from November 2015
### Wikipedia pending changes protected pages
### "An autonomous system (AS) is a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain, that presents a common and clearly defined routing policy to the Internet. Each AS is assigned an autonomous system number (ASN), for use in Border Gateway Protocol (BGP) routing. Autonomous System Numbers are assigned to Local Internet Registries (LIRs) and end user organizations by their respective Regional Internet Registries (RIRs), which in turn receive blocks of ASNs for reassignment from the Internet Assigned Numbers Authority (IANA). The IANA also maintains a registry of ASNs which are reserved for private use (and should therefore not be announced to the global Internet). 
### Originally, the definition required control by a single entity, typically an Internet service provider (ISP) or a very large organization with independent connections to multiple networks, that adhered to a single and clearly defined routing policy. In March 1996, the newer definition came into use because multiple organizations can run BGP using private AS numbers to an ISP that connects all those organizations to the Internet. Even though there may be multiple autonomous systems supported by the ISP, the Internet only sees the routing policy of the ISP. That ISP must have an officially registered ASN. 
### Until 2007, AS numbers were defined as 16-bit integers, which allowed for a maximum of 65,536 assignments. Since then, the IANA has begun to also assign 32-bit AS numbers to regional Internet registry (RIRs). These numbers are written preferably as simple integers, in a notation referred to as \"asplain\", ranging from 0 to 4,294,967,295 (hexadecimal 0xFFFF FFFF). Or, alternatively, in the form called \"asdot\" which looks like x.y, where x and y are 16-bit numbers. Numbers of the form 0.y are exactly the old 16-bit AS numbers. The special 16-bit ASN 23456 (\"AS_TRANS\") was assigned by IANA as a placeholder for 32-bit ASN values for the case when 32-bit-ASN capable routers (\"new BGP speakers\") send BGP messages to routers with older BGP software (\"old BGP speakers\") which do not understand the new 32-bit ASNs.The first and last ASNs of the original 16-bit integers (0 and 65,535) and the last ASN of the 32-bit numbers (4,294,967,295) are reserved and should not be used by operators; AS0 is used by all five RIRs to invalidate unallocated space. ASNs 64,496 to 64,511 of the original 16-bit range and 65,536 to 65,551 of the 32-bit range are reserved for use in documentation. ASNs 64,512 to 65,534 of the original 16-bit AS range, and 4,200,000,000 to 4,294,967,294 of the 32-bit range are reserved for Private Use.The number of unique autonomous networks in the routing system of the Internet exceeded 5,000 in 1999, 30,000 in late 2008, 35,000 in mid-2010, 42,000 in late 2012, 54,000 in mid-2016 and 60,000 in early 2018. 
### The number of allocated ASNs exceeded 100,000 as of March 2021.
## Assignment  
### AS numbers are assigned in blocks by Internet Assigned Numbers Authority (IANA) to regional Internet registries (RIRs). The appropriate RIR then assigns ASNs to entities within its designated area from the block assigned by IANA. Entities wishing to receive an ASN must complete the application process of their RIR, LIR or upstream service provider and be approved before being assigned an ASN. Current IANA ASN assignments to RIRs can be found on the IANA website. RIRs, as part of NRO, can revoke AS numbers as part of their Internet governance abilities.There are other sources for more specific data: 

### APNIC: https://ftp.apnic.net/stats/apnic/ 
### RIPE NCC: https://ftp.ripe.net/ripe/stats/ 
### AFRINIC: https://ftp.afrinic.net/pub/stats/afrinic/ 
### ARIN: https://ftp.arin.net/pub/stats/arin/ 
### LACNIC: https://ftp.lacnic.net/pub/stats/lacnic/
## ASN Table  
### A complete table of 16-bits and 32-bits ASN available:
## Types  
### Autonomous systems (AS) can be grouped into four categories, depending on their connectivity and operating policy. 

### multihomed: An AS that maintains connections to more than one other AS. This allows the AS to remain connected to the Internet in the event of a complete failure of one of their connections. However, unlike a transit AS, this type of AS would not allow traffic from one AS to pass through on its way to another AS. 
### stub: An AS that is connected to only one other AS. This may be an apparent waste of an AS number if the network's routing policy is the same as its upstream AS's. However, the stub AS may have peering with other autonomous systems that is not reflected in public route-view servers. Specific examples include private interconnections in the financial and transportation sectors. 
### transit: An AS that provides connections through itself to other networks. That is, network A can use network B, the transit AS, to connect to network C. If one AS is an ISP for another, then it is considered a transit AS. 
### Internet Exchange Point (IX or IXP): A physical infrastructure through which ISPs or content delivery networks (CDNs) exchange Internet traffic between their networks (autonomous systems). These are often groups of local ISPs that band together to exchange data by splitting the costs of a local networking hub, avoiding the higher costs (and bandwidth charges) of a Transit AS. IXP ASNs are usually transparent.
## AS-SET  
### Autonomous systems can be included in one or more AS-SETs, for example AS-SET of RIPE NCC \"AS-12655\" has AS1, AS2 and AS3 as its members, but AS1 is also included in other sets in ARIN (AS-INCAPSULA) and APNIC (AS-IMCL). Another AS-SET sources can be RADB, LEVEL3 (tier 1 network now called Lumen Technologies) and also ARIN has ARIN-NONAUTH source of AS-SETs. AS-SETs can be included in other AS-SETs and even form cycles.
## See also  
### Administrative distance 
### INOC-DBA \u2014 a hotline communications system between the network operations centers of major Autonomous Systems 
### Internet Routing Registry 
### PeeringDB \u2014 a freely available web-based database of networks that are interested in peering 
### Routing Assets Database (RADB)
## References 
## External links  
### RIPEstat \u2014 Internet Measurements and Analysis 
### Merit RADb 
### Hurricane Electric BGP Toolkit 
### PeeringDB https://www.peeringdb.com/ 
### Robtex: Various kinds of research of IP numbers, Domain names, ASN, etc 
### astraceroute, an AS traceroute utility (part of netsniff-ng) 
### ASN FAQ 
### CIDR and ASN assignment report 
### Partial List of Autonomous system numbers 
### Lookin'STAT Graph: number of Autonomous systems online"
## Links
### AFRINIC
### APNIC
### ARIN
### Administrative distance
### Border Gateway Protocol
### Content delivery network
### Doi (identifier)
### Hexadecimal
### IETF
### INOC-DBA
### ISP
### ISSN (identifier)
### Internet Assigned Numbers Authority
### Internet Engineering Task Force
### Internet Exchange Point
### Internet Routing Registry
### Internet governance
### Internet protocol address
### Internet service provider
### Internet transit
### LACNIC
### Looking Glass server
### Lumen Technologies
### Multihoming
### Number Resource Organization
### Peering
### PeeringDB
### RFC (identifier)
### RIPE NCC
### Regional Internet registry
### Resource Public Key Infrastructure
### Routing
### Routing Assets Database
### Stub network
### Tier 1 network
## References
### [Reference](http://www.bgplookingglass.com/list-of-autonomous-system-numbers) - http://www.bgplookingglass.com/list-of-autonomous-system-numbers
### [Reference](http://icons.apnic.net/display/ASN/Using+AS+23456) - http://icons.apnic.net/display/ASN/Using+AS+23456
### [Reference](http://doi.org/10.17487%2FRFC1771) - http://doi.org/10.17487%2FRFC1771
### [Reference](http://doi.org/10.17487%2FRFC1930) - http://doi.org/10.17487%2FRFC1930
### [Reference](http://doi.org/10.17487%2FRFC4893) - http://doi.org/10.17487%2FRFC4893
### [Reference](http://doi.org/10.17487%2FRFC5396) - http://doi.org/10.17487%2FRFC5396
### [Reference](http://doi.org/10.17487%2FRFC5398) - http://doi.org/10.17487%2FRFC5398
### [Reference](http://doi.org/10.17487%2FRFC6483) - http://doi.org/10.17487%2FRFC6483
### [Reference](http://doi.org/10.17487%2FRFC6793) - http://doi.org/10.17487%2FRFC6793
### [Reference](http://doi.org/10.17487%2FRFC6996) - http://doi.org/10.17487%2FRFC6996
### [Reference](http://doi.org/10.17487%2FRFC7300) - http://doi.org/10.17487%2FRFC7300
### [Reference](http://doi.org/10.17487%2FRFC7607) - http://doi.org/10.17487%2FRFC7607
### [Reference](http://www.netsniff-ng.org/) - http://www.netsniff-ng.org/
### [Reference](http://www.worldcat.org/issn/2070-1721) - http://www.worldcat.org/issn/2070-1721
### [Reference](https://www.peeringdb.com/) - https://www.peeringdb.com/
### [Reference](https://www.robtex.com/) - https://www.robtex.com/
### [Reference](https://www-public.imtbs-tsp.eu/~maigron/RIR_Stats/RIR_Delegations/World/ASN-ByNb.html) - https://www-public.imtbs-tsp.eu/~maigron/RIR_Stats/RIR_Delegations/World/ASN-ByNb.html
### [Reference](https://ftp.afrinic.net/pub/stats/afrinic/) - https://ftp.afrinic.net/pub/stats/afrinic/
### [Reference](https://www.afrinic.net/library/198-how-to-setup-a-lir-) - https://www.afrinic.net/library/198-how-to-setup-a-lir-
### [Reference](https://blog.apnic.net/2020/09/02/policy-prop-132-as0-for-unallocated-space-deployed-in-service/) - https://blog.apnic.net/2020/09/02/policy-prop-132-as0-for-unallocated-space-deployed-in-service/
### [Reference](https://ftp.apnic.net/stats/apnic/) - https://ftp.apnic.net/stats/apnic/
### [Reference](https://www.apnic.net/get-ip/faqs/asn/) - https://www.apnic.net/get-ip/faqs/asn/
### [Reference](https://ftp.arin.net/pub/stats/arin/) - https://ftp.arin.net/pub/stats/arin/
### [Reference](https://bgp.he.net) - https://bgp.he.net
### [Reference](https://bgp.he.net/irr/as-set/AS-12655) - https://bgp.he.net/irr/as-set/AS-12655
### [Reference](https://ftp.lacnic.net/pub/stats/lacnic/) - https://ftp.lacnic.net/pub/stats/lacnic/
### [Reference](https://www.lacnic.net/en/web/lacnic/revocacion-de-recursos) - https://www.lacnic.net/en/web/lacnic/revocacion-de-recursos
### [Reference](https://irrexplorer.nlnog.net/as-set/AS-ROSTELECOM) - https://irrexplorer.nlnog.net/as-set/AS-ROSTELECOM
### [Reference](https://irrexplorer.nlnog.net/asn/AS1) - https://irrexplorer.nlnog.net/asn/AS1
### [Reference](https://www.radb.net/) - https://www.radb.net/
### [Reference](https://ftp.ripe.net/ripe/stats/) - https://ftp.ripe.net/ripe/stats/
### [Reference](https://stat.ripe.net/) - https://stat.ripe.net/
### [Reference](https://www.ripe.net/publications/docs/ripe-679) - https://www.ripe.net/publications/docs/ripe-679
### [Reference](https://irrexplorer.dashcare.nl/asn/AS0) - https://irrexplorer.dashcare.nl/asn/AS0
### [Reference](https://web.archive.org/web/20161029182359/http://icons.apnic.net/display/ASN/Using+AS+23456) - https://web.archive.org/web/20161029182359/http://icons.apnic.net/display/ASN/Using+AS+23456
### [Reference](https://www.cidr-report.org/as2.0/) - https://www.cidr-report.org/as2.0/
### [Reference](https://www.iana.org/assignments/as-numbers/as-numbers.xhtml) - https://www.iana.org/assignments/as-numbers/as-numbers.xhtml
### [Reference](https://datatracker.ietf.org/doc/html/rfc1771) - https://datatracker.ietf.org/doc/html/rfc1771
### [Reference](https://datatracker.ietf.org/doc/html/rfc1930) - https://datatracker.ietf.org/doc/html/rfc1930
### [Reference](https://datatracker.ietf.org/doc/html/rfc1930#section-3) - https://datatracker.ietf.org/doc/html/rfc1930#section-3
### [Reference](https://datatracker.ietf.org/doc/html/rfc4271) - https://datatracker.ietf.org/doc/html/rfc4271
### [Reference](https://datatracker.ietf.org/doc/html/rfc4893) - https://datatracker.ietf.org/doc/html/rfc4893
### [Reference](https://datatracker.ietf.org/doc/html/rfc5396) - https://datatracker.ietf.org/doc/html/rfc5396
### [Reference](https://datatracker.ietf.org/doc/html/rfc5398) - https://datatracker.ietf.org/doc/html/rfc5398
### [Reference](https://datatracker.ietf.org/doc/html/rfc6483) - https://datatracker.ietf.org/doc/html/rfc6483
### [Reference](https://datatracker.ietf.org/doc/html/rfc6793) - https://datatracker.ietf.org/doc/html/rfc6793
### [Reference](https://datatracker.ietf.org/doc/html/rfc6996) - https://datatracker.ietf.org/doc/html/rfc6996
### [Reference](https://datatracker.ietf.org/doc/html/rfc7300) - https://datatracker.ietf.org/doc/html/rfc7300
### [Reference](https://datatracker.ietf.org/doc/html/rfc7607) - https://datatracker.ietf.org/doc/html/rfc7607
### [Reference](https://stat.lookinglass.org) - https://stat.lookinglass.org
### [Reference](https://www.ididb.ru/asset/#AS-ROSTELECOM) - https://www.ididb.ru/asset/#AS-ROSTELECOM
## Images
### [Image](https://upload.wikimedia.org/wikipedia/en/b/b7/Pending-protection-shackle.svg) - https://upload.wikimedia.org/wikipedia/en/b/b7/Pending-protection-shackle.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/b/b7/20190717132309%21Pending-protection-shackle.svg) - https://upload.wikimedia.org/wikipedia/en/archive/b/b7/20190717132309%21Pending-protection-shackle.svg