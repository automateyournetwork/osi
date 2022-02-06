# IS-IS
## [URL](https://en.wikipedia.org/wiki/IS-IS) - https://en.wikipedia.org/wiki/IS-IS
## Catagories
### All articles with unsourced statements
### Articles with LCCN identifiers
### Articles with short description
### Articles with unsourced statements from February 2013
### ISO standards
### Internet Standards
### Internet protocols
### OSI protocols
### Routing protocols
### Short description is different from Wikidata
### "Intermediate System to Intermediate System  (IS-IS, also written ISIS) is a routing protocol designed to move information efficiently within a computer network, a group of physically connected computers or similar devices. It accomplishes this by determining the best route for data through a packet switching network. 
### The IS-IS protocol is defined in ISO/IEC 10589:2002 as an international standard within the Open Systems Interconnection (OSI) reference design.  The Internet Engineering Task Force (IETF) republished IS-IS in RFC 1142, but that RFC was later marked as historic by RFC 7142 because it republished a draft rather than a final version of the ISO standard, causing confusion. 
### IS-IS has been called \"the de facto standard for large service provider network backbones.\"
## Description  
### IS-IS is an interior gateway protocol, designed for use within an administrative domain or network.  This is in contrast to exterior gateway protocols, primarily Border Gateway Protocol (BGP), which is used for routing between autonomous systems (RFC 1930). 
### IS-IS is a link-state routing protocol, operating by reliably flooding link state information throughout a network of routers. Each IS-IS router independently builds a database of the network's topology, aggregating the flooded network information.  Like the OSPF protocol, IS-IS uses Dijkstra's algorithm for computing the best path through the network.  Packets (datagrams) are then forwarded, based on the computed ideal path, through the network to the destination.
## History  
### The IS-IS protocol was developed by a team of people working at Digital Equipment Corporation as part of DECnet Phase V. It was standardized by the ISO in 1992 as ISO 10589 for communication between network devices that are termed Intermediate Systems (as opposed to end systems or hosts) by the ISO. The purpose of IS-IS was to make possible the routing of datagrams using the ISO-developed OSI protocol stack called CLNS. 
### IS-IS was developed at roughly the same time that the Internet Engineering Task Force IETF was developing a similar protocol called OSPF. IS-IS was later extended to support routing of datagrams in the Internet Protocol (IP), the Network Layer protocol of the global Internet. This version of the IS-IS routing protocol was then called Integrated IS-IS (RFC 1195)
## Packet types  
### IS-IS adjacency can be either broadcast or point-to-point. 

### Hello Packet 
### The IS-IS hello packets needs to be exchanged periodically between 2 routers to establish adjacency. Based on the negotiation, one of them will be selected as DIS (Designated IS). This hello packet will be sent separately for Level-1 or Level-2. 
### LSP 
### This contains the actual route information. This LSP can contain many type\u2013length\u2013values (TLVs). 
### CSNP 
### This packet will be sent only by the DIS. By default for every 10 seconds, CSNP packet will be transmitted by DIS. This will contain the list of LSP IDs along with sequence number and checksum. 
### PSNP 
### If the router which receives CSNP packet finds some discrepancy in its own database, it will send an PSNP request asking the DIS to send specific LSP back to it.
## Comparison with OSPF  
### Both IS-IS and Open Shortest Path First (OSPF) are link-state protocols, and both use the same Dijkstra algorithm for computing the best path through the network. As a result, they are conceptually similar. Both support Classless Inter-Domain Routing, can use multicast to discover neighboring routers using hello packets, and can support authentication of routing updates. 
### OSPF was natively built to route IP and is itself a protocol that runs on top of IP, and OSPFv2 is only able to build IPv4 routing tables. IS-IS is an OSI Layer 3 protocol initially defined for routing CLNP. However, IS-IS is neutral regarding the type of network addresses for which it can route, and was easily extended to support IPv4 routing, using mechanisms described in RFC 1195, and later IPv6 as specified in RFC 5308.  To operate with IPv6 networks, the OSPF protocol was rewritten in OSPF v3 (as specified in RFC 5340). 
### Both OSPF and IS-IS routers build a topological representation of the network. This map indicates the subnets which each IS-IS router can reach, and the lowest-cost (shortest) path to a subnet is used to forward traffic. 
### IS-IS differs from OSPF in the way that \"areas\" are defined and routed between. IS-IS routers are designated as being: Level 1 (intra-area); Level 2 (inter area); or Level 1\u20132 (both). Routing information is exchanged between Level 1 routers and other Level 1 routers of the same area, and Level 2 routers can only form relationships and exchange information with other Level 2 routers. Level 1\u20132 routers exchange information with both levels and are used to connect the inter area routers with the intra area routers. 
### In OSPF, areas are delineated on the interface such that an area border router (ABR) is actually in two or more areas at once, effectively creating the borders between areas inside the ABR, whereas in IS-IS area borders are in between routers, designated as Level 2 or Level 1\u20132. The result is that an IS-IS router is only ever a part of a single area. 
### IS-IS also does not require Area 0 (Area Zero) to be the backbone area through which all inter-area traffic must pass. The logical view is that OSPF creates something of a spider web or star topology of many areas all attached directly to Area Zero and IS-IS, by contrast, creates a logical topology of a backbone of Level 2 routers with branches of Level 1\u20132 and Level 1 routers forming the individual areas. 
### IS-IS also differs from OSPF in the methods by which it reliably floods topology and topology change information through the network. However, the basic concepts are similar.OSPF has a larger set of extensions and optional features specified in the protocol standards. However, IS-IS is easier to expand: its use of TLV data allows engineers to implement support for new techniques without redesigning the protocol. For example, in order to support IPv6, the IS-IS protocol was extended to support a few additional TLVs, whereas OSPF required a new protocol draft (OSPFv3). In addition to that, IS-IS is less \"chatty\" and can scale to support larger networks. Given the same set of resources, IS-IS can support more routers in an area than OSPF. This has contributed to IS-IS as an ISP-scale protocol.The TCP/IP implementation, known as \"Integrated IS-IS\" or \"Dual IS-IS\", is described in RFC 1195.
## Other uses  
### IS-IS is also used as the control plane for IEEE 802.1aq Shortest Path Bridging (SPB).  SPB allows for shortest-path forwarding in an Ethernet mesh network context utilizing multiple equal cost paths.  This permits SPB to support large Layer 2 topologies, with fast convergence, and improved use of the mesh topology.  Combined with this is single point provisioning for logical connectivity membership.  IS-IS is therefore augmented with a small number of TLVs and sub-TLVs, and supports two Ethernet encapsulating data paths, 802.1ad Provider Bridges and 802.1ah Provider Backbone Bridges.  SPB requires no state machine or other substantive changes to IS-IS, and simply requires a new Network Layer Protocol Identifier (NLPID) and set of TLVs.  This extension to IS-IS is defined in the IETF proposed standard RFC 6329.
## Related protocols  
### Fabric Shortest Path First (FSPF) 
### Transparent Interconnect of Lots of Links (TRILL)
## References 
## External links  
### IS-IS standard (ISO/IEC 10589:2002, Second Edition) \u2013 free-of-charge PDF version 
### RFC 1195 \u2013 Use of OSI IS-IS for Routing in TCP/IP and Dual Environments 
### OSPF and IS-IS: A Comparative Anatomy by Dave Katz, Juniper 
### Collection of RFCs pertaining to IS-IS 
### IS-IS and OSPF difference discussion (Vishwas Manral, Manav Bhatia and Yasuhiro Ohara) 
### Google Quagga IS-IS implementation 
### Sample isisd.conf file: used with Quagga"
## References
### [Reference](http://code.google.com/p/google-quagga/source/list?name=is-is) - http://code.google.com/p/google-quagga/source/list?name=is-is
### [Reference](http://www.networksorcery.com/enp/protocol/is-is.htm) - http://www.networksorcery.com/enp/protocol/is-is.htm
### [Reference](http://www.ietf.org/rfc/rfc1195.txt) - http://www.ietf.org/rfc/rfc1195.txt
### [Reference](http://standards.iso.org/ittf/PubliclyAvailableStandards/c030932_ISO_IEC_10589_2002(E).zip) - http://standards.iso.org/ittf/PubliclyAvailableStandards/c030932_ISO_IEC_10589_2002(E).zip
### [Reference](http://www.nada.kth.se/kurser/kth/2D1490/06/hemuppgifter/bhatia-manral-diff-isis-ospf-01.txt.html) - http://www.nada.kth.se/kurser/kth/2D1490/06/hemuppgifter/bhatia-manral-diff-isis-ospf-01.txt.html
### [Reference](https://id.loc.gov/authorities/subjects/sh2002000572) - https://id.loc.gov/authorities/subjects/sh2002000572
### [Reference](https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://www.itu.int/rec/T-REC-X.225-199511-I/en
### [Reference](https://web.archive.org/web/20070928004122/http://svn.dd-wrt.com:8000/dd-wrt/browser/src/router/quagga/isisd/isisd.conf.sample?rev=7215) - https://web.archive.org/web/20070928004122/http://svn.dd-wrt.com:8000/dd-wrt/browser/src/router/quagga/isisd/isisd.conf.sample?rev=7215
### [Reference](https://web.archive.org/web/20140907054246/http://www.nanog.org/meetings/nanog19/presentations/katz.ppt) - https://web.archive.org/web/20140907054246/http://www.nanog.org/meetings/nanog19/presentations/katz.ppt
### [Reference](https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en
### [Reference](https://datatracker.ietf.org/doc/html/rfc1142) - https://datatracker.ietf.org/doc/html/rfc1142
### [Reference](https://datatracker.ietf.org/doc/html/rfc1195) - https://datatracker.ietf.org/doc/html/rfc1195
### [Reference](https://datatracker.ietf.org/doc/html/rfc5308) - https://datatracker.ietf.org/doc/html/rfc5308
### [Reference](https://datatracker.ietf.org/doc/html/rfc5340) - https://datatracker.ietf.org/doc/html/rfc5340
### [Reference](https://datatracker.ietf.org/doc/html/rfc7142) - https://datatracker.ietf.org/doc/html/rfc7142
### [Reference](https://tools.ietf.org/html/rfc6329) - https://tools.ietf.org/html/rfc6329
### [Reference](https://www.iso.org/standard/30932.html) - https://www.iso.org/standard/30932.html
### [Reference](https://www.wikidata.org/wiki/Q1165964#identifiers) - https://www.wikidata.org/wiki/Q1165964#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg) - https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg