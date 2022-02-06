# Dynamic Host Configuration Protocol
## [URL](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) - https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol
## Catagories
### All articles containing potentially dated statements
### All articles needing additional references
### All articles with failed verification
### Application layer protocols
### Articles containing potentially dated statements from 2021
### Articles needing additional references from September 2020
### Articles with GND identifiers
### Articles with failed verification from January 2022
### Articles with short description
### CS1 maint: archived copy as title
### Commons category link is on Wikidata
### Internet Standards
### Network service
### Short description matches Wikidata
### "The Dynamic Host Configuration Protocol (DHCP) is a network management protocol used on Internet Protocol (IP) networks for automatically assigning IP addresses and other communication parameters to devices connected to the network using a client\u2013server architecture.The technology eliminates the need for individually configuring network devices manually, and consists of two network components, a centrally installed network DHCP server and client instances of the protocol stack on each computer or device. When connected to the network, and periodically thereafter, a client requests a set of parameters from the DHCP server using the DHCP protocol. 
### DHCP can be implemented on networks ranging in size from residential networks to large campus networks and regional ISP networks. Many routers and residential gateways have DHCP server capability. Most residential network routers receive a unique IP address within the ISP network. Within a local network, a DHCP server assigns a local IP address to each device. 
### DHCP services exist for networks running Internet Protocol version 4 (IPv4), as well as version 6 (IPv6). The IPv6 version of the DHCP protocol is commonly called DHCPv6.
## History  
### The Reverse Address Resolution Protocol (RARP) was defined in RFC 903 in 1984 for the configuration of simple devices, such as diskless workstations, with a suitable IP address. Acting in the data link layer it made implementation difficult in many server platforms. It required that a server be present on each individual network link. RARP was superseded by the Bootstrap Protocol (BOOTP) defined in RFC 951 in September 1985. This introduced the concept of a relay agent, which allowed the forwarding of BOOTP packets across networks, allowing one central BOOTP server to serve hosts on many IP subnets.DHCP is based on BOOTP, but can dynamically allocate IP addresses from a pool and reclaim them when they are no longer in use. It can also be used to deliver a wide range of extra configuration parameters to IP clients, including platform-specific parameters. DHCP was first defined in RFC 1531 in October 1993, but due to errors in the editorial process was almost immediately reissued as RFC 1541. 
### Four years later the DHCPINFORM message type and other small changes were added by RFC 2131, which as of 2021 remains the core of the standard for IPv4 networks, with updates in RFC 3396, RFC 4361, RFC 5494, and RFC 6842.DHCPv6 was initially described by RFC 3315 in 2003, but this has been updated by many subsequent RFCs. RFC 3633 added a DHCPv6 mechanism for prefix delegation, and stateless address autoconfiguration was added by RFC 3736.
## Overview  
### Internet Protocol (IP) defines how devices communicate within and across local networks on the Internet.  A DHCP server can manage IP settings for devices on its local network, e.g., by assigning IP addresses to those devices automatically and dynamically. 
### DHCP operates based on the client\u2013server model. When a computer or other device connects to a network, the DHCP client software sends a DHCP broadcast query requesting the necessary information. Any DHCP server on the network may service the request. The DHCP server manages a pool of IP addresses and information about client configuration parameters such as default gateway, domain name, the name servers, and time servers. On receiving a DHCP request, the DHCP server may respond with specific information for each client, as previously configured by an administrator, or with a specific address and any other information valid for the entire network and for the time period for which the allocation (lease) is valid. A DHCP client typically queries for this information immediately after booting, and periodically thereafter before the expiration of the information. When a DHCP client refreshes an assignment, it initially requests the same parameter values, but the DHCP server may assign a new address based on the assignment policies set by administrators. 
### On large networks that consist of multiple links, a single DHCP server may service the entire network when aided by DHCP relay agents located on the interconnecting routers. Such agents relay messages between DHCP clients and DHCP servers located on different subnets. 
### Depending on implementation, the DHCP server may have three methods of allocating IP addresses: 

### Dynamic allocation 
### A network administrator reserves a range of IP addresses for DHCP, and each DHCP client on the LAN is configured to request an IP address from the DHCP server during network initialization. The request-and-grant process uses a lease concept with a controllable time period, allowing the DHCP server to reclaim and then reallocate IP addresses that are not renewed.Automatic allocation 
### The DHCP server permanently assigns an IP address to a requesting client from a range defined by an administrator. This is like dynamic allocation, but the DHCP server keeps a table of past IP address assignments, so that it can preferentially assign to a client the same IP address that the client previously had.Manual allocation 
### This method is also variously called static DHCP allocation, fixed address allocation, reservation, and MAC/IP address binding. An administrator maps a unique identifier (a client id or MAC address) for each client to an IP address, which is offered to the requesting client. DHCP servers may be configured to fall back to other methods if this fails.DHCP services are used for Internet Protocol version 4 (IPv4) and IPv6. The details of the protocol for IPv4 and IPv6 differ sufficiently that they may be considered separate protocols. For the IPv6 operation, devices may alternatively use stateless address autoconfiguration. IPv6 hosts may also use link-local addressing to achieve operations restricted to the local network link.
## Operation  

### The DHCP employs a connectionless service model, using the User Datagram Protocol (UDP). It is implemented with two UDP port numbers for its operations which are the same as for the bootstrap protocol (BOOTP). UDP port number 67 is the destination port of a server, and UDP port number 68 is used by the client. 
### DHCP operations fall into four phases: server discovery, IP lease offer, IP lease request, and IP lease acknowledgement. These stages are often abbreviated as DORA for discovery, offer, request, and acknowledgement. 
### The DHCP operation begins with clients broadcasting a request. If the client and server are in different Broadcast Domains, a DHCP Helper or DHCP Relay Agent may be used. Clients requesting renewal of an existing lease may communicate directly via UDP unicast, since the client already has an established IP address at that point. Additionally, there is a BROADCAST flag (1 bit in 2 byte flags field, where all other bits are reserved and so are set to 0) the client can use to indicate in which way (broadcast or unicast) it can receive the DHCPOFFER: 0x8000 for broadcast, 0x0000 for unicast. Usually, the DHCPOFFER is sent through unicast. For those hosts which cannot accept unicast packets before IP addresses are configured, this flag can be used to work around this issue.
## Discovery  
### The DHCP client broadcasts a DHCPDISCOVER message on the network subnet using the destination address 255.255.255.255 (limited broadcast) or the specific subnet broadcast address (directed broadcast). A DHCP client may also request its last known IP address. If the client remains connected to the same network, the server may grant the request. Otherwise, it depends whether the server is set up as authoritative or not. An authoritative server denies the request, causing the client to issue a new request. A non-authoritative server simply ignores the request, leading to an implementation-dependent timeout for the client to expire the request and ask for a new IP address. 
### For example, if HTYPE is set to 1, to specify that the medium used is Ethernet, HLEN is set to 6 because an Ethernet address (MAC address) is 6 octets long. The CHADDR is set to the MAC address used by the client. Some options are set as well.
## Offer  
### When a DHCP server receives a DHCPDISCOVER message from a client, which is an IP address lease request, the DHCP server reserves an IP address for the client and makes a lease offer by sending a DHCPOFFER message to the client. This message contains the client's client id (traditionally a MAC address), the IP address that the server is offering, the subnet mask, the lease duration, and the IP address of the DHCP server making the offer. The DHCP server may also take notice of the hardware-level MAC address in the underlying transport layer: according to current RFCs the transport layer MAC address may be used if no client ID is provided in the DHCP packet. 
### The DHCP server determines the configuration based on the client's hardware address as specified in the CHADDR (client hardware address) field. Here the server, 192.168.1.1, specifies the client's IP address in the YIADDR (your IP address) field.
## Request  
### In response to the DHCP offer, the client replies with a DHCPREQUEST message, broadcast to the server, requesting the offered address. A client can receive DHCP offers from multiple servers, but it will accept only one DHCP offer. The client will produce a gratuitous ARP in order to find if there is any other host present in the network with the same IP address. If there is no reply by other host, then there is no host with same IP configuration in the network and the message is broadcast to server showing the acceptance of IP address. The client must send the server identification option in the request message indicating the server whose offer the client has selected.:\u200aSection 3.1,\u200aItem 3\u200a When other DHCP servers receive this message, they withdraw any offers that they have made to the client and return the offered IP address to the pool of available addresses.
## Acknowledgement  
### When the DHCP server receives the DHCPREQUEST message from the client, the configuration process enters its final phase. The acknowledgement phase involves sending a DHCPACK packet to the client. This packet includes the lease duration and any other configuration information that the client might have requested. At this point, the IP configuration process is completed. 
### The protocol expects the DHCP client to configure its network interface with the negotiated parameters. 
### After the client obtains an IP address, it should probe the newly received address (e.g. with ARP Address Resolution Protocol) to prevent address conflicts caused by overlapping address pools of DHCP servers. If this probe finds another computer using that address, the computer should send DHCPDECLINE, broadcast, to the server.
## Information  
### A DHCP client may request more information than the server sent with the original DHCPOFFER. The client may also request repeat data for a particular application. For example, browsers use DHCP Inform to obtain web proxy settings via WPAD.
## Releasing  
### The client sends a request to the DHCP server to release the DHCP information and the client deactivates its IP address. As client devices usually do not know when users may unplug them from the network, the protocol does not mandate the sending of DHCP Release.
## Client configuration parameters  
### A DHCP server can provide optional configuration parameters to the client. RFC 2132 describes the available DHCP options defined by Internet Assigned Numbers Authority (IANA) -  DHCP and BOOTP PARAMETERS.A DHCP client can select, manipulate and overwrite parameters provided by a DHCP server. In Unix-like systems this client-level refinement typically takes place according to the values in the configuration file /etc/dhclient.conf.
## Options  
### Options are octet strings of varying length. This is called Type\u2013length\u2013value encoding. The first octet is the option code, the second octet is the number of following octets and the remaining octets are code dependent. 
### For example, the DHCP message-type option for an offer would appear as 0x35, 0x01, 0x02, where 0x35 is code 53 for \"DHCP message type\", 0x01 means one octet follows and 0x02 is the value of \"offer\". 
### The following tables list the available DHCP options, as listed in RFC 2132 and IANA registry.
## DHCP Message Types  
### This table lists the DHCP message types, documented in RFC 2132, RFC 3203, RFC 4388, RFC 6926 and RFC 7724.  These codes are the value in the DHCP extension 53, shown in the 
### table above.
## Client vendor identification  
### An option exists to identify the vendor and functionality of a DHCP client. The information is a variable-length string of characters or octets which has a meaning specified by the vendor of the DHCP client. One method  by which a DHCP client can communicate to the server that it is using a certain type of hardware or firmware is to set a value in its DHCP requests called the Vendor Class Identifier (VCI) (Option 60). This method allows a DHCP server to differentiate between the two kinds of client machines and process the requests from the two types of modems appropriately. Some types of set-top boxes also set the VCI (Option 60) to inform the DHCP server about the hardware type and functionality of the device. The value to which this option is set gives the DHCP server a hint about any required extra information that this client needs in a DHCP response.
## Other extensions 
## Relay agent information sub-options  
### The relay agent information option (option 82) specifies container for attaching sub-options to DHCP requests transmitted between a DHCP relay and a DHCP server.
## Relaying  
### In small networks, where only one IP subnet is being managed, DHCP clients communicate directly with DHCP servers. However, DHCP servers can also provide IP addresses for multiple subnets. In this case, a DHCP client that has not yet acquired an IP address cannot communicate directly with a DHCP server not on the same subnet, as the client's broadcast can only be received on its own subnet. 
### In order to allow DHCP clients on subnets not directly served by DHCP servers to communicate with DHCP servers, DHCP relay agents can be installed on these subnets. The DHCP client broadcasts on the local link; the relay agent receives the broadcast and transmits it to one or more DHCP servers using unicast. The relay agent stores its own IP address in field GIADDR field of the DHCP packet. The DHCP server uses the GIADDR-value to determine the subnet on which the relay agent received the broadcast, and allocates an IP address on that subnet. When the DHCP server replies to the client, it sends the reply to the GIADDR-address, again using unicast. The relay agent then retransmits the response on the local network. 
### In this situation, the communication between the relay agent and the DHCP server typically uses both a source and destination UDP port of 67.
## Client states  

### As described in RFC 2131,:\u200aSection 4.4\u200a a DHCP client can receive these messages from a server: 

### DHCPOFFER 
### DHCPACK 
### DHCPNAKThe client moves through DHCP states depending on how the server responds to the messages that the client sends.
## Reliability  
### The DHCP ensures reliability in several ways: periodic renewal, rebinding,:\u200aSection 4.4.5\u200a and failover. DHCP clients are allocated leases that last for some period of time. Clients begin to attempt to renew their leases once half the lease interval has expired.:\u200aSection 4.4.5 Paragraph 3\u200a   They do this by sending a unicast DHCPREQUEST message to the DHCP server that granted the original lease. If that server is down or unreachable, it will fail to respond to the DHCPREQUEST. However, in that case the client repeats the DHCPREQUEST from time to time,:\u200aSection 4.4.5 Paragraph 8\u200a so if the DHCP server comes back up or becomes reachable again, the DHCP client will succeed in contacting it and renew the lease. 
### If the DHCP server is unreachable for an extended period of time,:\u200aSection 4.4.5 Paragraph 5\u200a the DHCP client will attempt to rebind, by broadcasting its DHCPREQUEST rather than unicasting it. Because it is broadcast, the DHCPREQUEST message will reach all available DHCP servers. If some other DHCP server is able to renew the lease, it will do so at this time. 
### In order for rebinding to work, when the client successfully contacts a backup DHCP server, that server must have accurate information about the client's binding. Maintaining accurate binding information between two servers is a complicated problem; if both servers are able to update the same lease database, there must be a mechanism to avoid conflicts between updates on the independent servers. A proposal for implementing fault-tolerant DHCP servers was submitted to the Internet Engineering Task Force, but never formalized.If rebinding fails, the lease will eventually expire. When the lease expires, the client must stop using the IP address granted to it in its lease.:\u200aSection 4.4.5 Paragraph 9\u200a   At that time it will restart the DHCP process from the beginning by broadcasting a DHCPDISCOVER message. Since its lease has expired, it will accept any IP address offered to it. Once it has a new IP address (presumably from a different DHCP server) it will once again be able to use the network. However, since its IP address has changed, any ongoing connections will be broken.
## IPv6 networks  
### The basic methodology of DHCP was developed for networks based on Internet Protocol version 4 (IPv4). Since the development and deployment of IPv6 networks, DHCP has also been used for assigning parameters in such networks, despite the inherent features of IPv6 for stateless address autoconfiguration. The IPv6 version of the protocol is designated as DHCPv6.
## Security  

### The base DHCP does not include any mechanism for authentication.  Because of this, it is vulnerable to a variety of attacks. These attacks fall into three main categories: 

### Unauthorized DHCP servers providing false information to clients. 
### Unauthorized clients gaining access to resources. 
### Resource exhaustion attacks from malicious DHCP clients.Because the client has no way to validate the identity of a DHCP server, unauthorized DHCP servers (commonly called \"rogue DHCP\") can be operated on networks, providing incorrect information to DHCP clients.  This can serve either as a denial-of-service attack, preventing the client from gaining access to network connectivity, or as a man-in-the-middle attack.  Because the DHCP server provides the DHCP client with server IP addresses, such as the IP address of one or more DNS servers, an attacker can convince a DHCP client to do its DNS lookups through its own DNS server, and can therefore provide its own answers to DNS queries from the client. This in turn allows the attacker to redirect network traffic through itself, allowing it to eavesdrop on connections between the client and network servers it contacts, or to simply replace those network servers with its own.Because the DHCP server has no secure mechanism for authenticating the client, clients can gain unauthorized access to IP addresses by presenting credentials, such as client identifiers, that belong to other DHCP clients. This also allows DHCP clients to exhaust the DHCP server's store of IP addresses\u2014by presenting new credentials each time it asks for an address, the client can consume all the available IP addresses on a particular network link, preventing other DHCP clients from getting service.DHCP does provide some mechanisms for mitigating these problems. The Relay Agent Information Option protocol extension (RFC 3046, usually referred to in the industry by its actual number as Option 82) allows network operators to attach tags to DHCP messages as these messages arrive on the network operator's trusted network. This tag is then used as an authorization token to control the client's access to network resources. Because the client has no access to the network upstream of the relay agent, the lack of authentication does not prevent the DHCP server operator from relying on the authorization token. 
### Another extension, Authentication for DHCP Messages (RFC 3118), provides a mechanism for authenticating DHCP messages. As of 2002, RFC 3118 had not seen widespread adoption because of the problems of managing keys for large numbers of DHCP clients. A 2007 book about DSL technologies remarked that:there were numerous security vulnerabilities identified against the security measures proposed by RFC 3118. This fact, combined with the introduction of 802.1x, slowed the deployment and take-rate of authenticated DHCP, and it has never been widely deployed. A 2010 book notes that:[t]here have been very few implementations of DHCP Authentication. The challenges of key management and processing delays due to hash computation have been deemed too heavy a price to pay for the perceived benefits. 
### Architectural proposals from 2008 involve authenticating DHCP requests using 802.1x or PANA (both of which transport EAP). An IETF proposal was made for including EAP in DHCP itself, the so-called EAPoDHCP; this does not appear to have progressed beyond IETF draft level, the last of which dates to 2010.
## IETF standards documents  
### RFC 2131, Dynamic Host Configuration Protocol 
### RFC 2132, DHCP Options and BOOTP Vendor Extensions 
### RFC 3046, DHCP Relay Agent Information Option 
### RFC 3397, Dynamic Host Configuration Protocol (DHCP) Domain Search Option 
### RFC 3942, Reclassifying Dynamic Host Configuration Protocol Version Four (DHCPv4) Options 
### RFC 4242, Information Refresh Time Option for Dynamic Host Configuration Protocol for IPv6 
### RFC 4361, Node-specific Client Identifiers for Dynamic Host Configuration Protocol Version Four (DHCPv4) 
### RFC 4436, Detecting Network Attachment in IPv4 (DNAv4) 
### RFC 3442, Classless Static Route Option for Dynamic Host Configuration Protocol (DHCP) version 4 
### RFC 3203, DHCP reconfigure extension 
### RFC 4388, Dynamic Host Configuration Protocol (DHCP) Leasequery 
### RFC 6926, DHCPv4 Bulk Leasequery 
### RFC 7724, Active DHCPv4 Lease Query
## See also 
## Notes 
## References 
## External links  
Media related to Dynamic Host Configuration Protocol (DHCP) at Wikimedia Commons"
## References
### [Reference](http://greyhatsspeak.blogspot.com/2015/11/dhcp-protocol-and-its-vulnerabilities.html) - http://greyhatsspeak.blogspot.com/2015/11/dhcp-protocol-and-its-vulnerabilities.html
### [Reference](http://www.securelist.com/en/blog/208188095/TDSS_loader_now_got_legs) - http://www.securelist.com/en/blog/208188095/TDSS_loader_now_got_legs
### [Reference](http://doi.org/10.17487%2FRFC2131) - http://doi.org/10.17487%2FRFC2131
### [Reference](http://doi.org/10.17487%2FRFC2132) - http://doi.org/10.17487%2FRFC2132
### [Reference](http://doi.org/10.17487%2FRFC3046) - http://doi.org/10.17487%2FRFC3046
### [Reference](http://doi.org/10.17487%2FRFC3203) - http://doi.org/10.17487%2FRFC3203
### [Reference](http://doi.org/10.17487%2FRFC3256) - http://doi.org/10.17487%2FRFC3256
### [Reference](http://doi.org/10.17487%2FRFC3397) - http://doi.org/10.17487%2FRFC3397
### [Reference](http://doi.org/10.17487%2FRFC4388) - http://doi.org/10.17487%2FRFC4388
### [Reference](http://doi.org/10.17487%2FRFC6926) - http://doi.org/10.17487%2FRFC6926
### [Reference](http://doi.org/10.17487%2FRFC7724) - http://doi.org/10.17487%2FRFC7724
### [Reference](http://tools.ietf.org/html/rfc2131#section-2.2) - http://tools.ietf.org/html/rfc2131#section-2.2
### [Reference](http://tools.ietf.org/html/rfc2131#section-7) - http://tools.ietf.org/html/rfc2131#section-7
### [Reference](http://tools.ietf.org/html/rfc3046#section-7) - http://tools.ietf.org/html/rfc3046#section-7
### [Reference](http://tools.ietf.org/html/rfc951#section-6) - http://tools.ietf.org/html/rfc951#section-6
### [Reference](http://tools.ietf.org/search/draft-pruss-dhcp-auth-dsl-07) - http://tools.ietf.org/search/draft-pruss-dhcp-auth-dsl-07
### [Reference](http://www.ietf.org/mail-archive/web/dhcwg/current/msg00876.html) - http://www.ietf.org/mail-archive/web/dhcwg/current/msg00876.html
### [Reference](https://books.google.com/books?id=70tr_hSDULwC&pg=PA55) - https://books.google.com/books?id=70tr_hSDULwC&pg=PA55
### [Reference](https://books.google.com/books?id=BvaFreun1W8C&pg=PA372) - https://books.google.com/books?id=BvaFreun1W8C&pg=PA372
### [Reference](https://books.google.com/books?id=Jjkd74jY47oC&pg=PA484) - https://books.google.com/books?id=Jjkd74jY47oC&pg=PA484
### [Reference](https://books.google.com/books?id=Mly55VntuYMC&pg=PA39) - https://books.google.com/books?id=Mly55VntuYMC&pg=PA39
### [Reference](https://books.google.com/books?id=NFzou_d4MGUC&pg=SA2-PA13) - https://books.google.com/books?id=NFzou_d4MGUC&pg=SA2-PA13
### [Reference](https://books.google.com/books?id=QgRDxkuI1MkC&pg=PA180) - https://books.google.com/books?id=QgRDxkuI1MkC&pg=PA180
### [Reference](https://books.google.com/books?id=QgRDxkuI1MkC&pg=PA181) - https://books.google.com/books?id=QgRDxkuI1MkC&pg=PA181
### [Reference](https://books.google.com/books?id=aS1ZngveBIkC&pg=PA239) - https://books.google.com/books?id=aS1ZngveBIkC&pg=PA239
### [Reference](https://books.google.com/books?id=ruWv8RGkBGgC&pg=PA142) - https://books.google.com/books?id=ruWv8RGkBGgC&pg=PA142
### [Reference](https://books.google.com/books?id=w9bEwBwd33MC&pg=PA339) - https://books.google.com/books?id=w9bEwBwd33MC&pg=PA339
### [Reference](https://www.networkworld.com/article/3297800/why-dhcps-days-might-be-numbered.html) - https://www.networkworld.com/article/3297800/why-dhcps-days-might-be-numbered.html
### [Reference](https://searchnetworking.techtarget.com/definition/DHCP) - https://searchnetworking.techtarget.com/definition/DHCP
### [Reference](https://d-nb.info/gnd/4608416-2) - https://d-nb.info/gnd/4608416-2
### [Reference](https://web.archive.org/web/20150403091552/http://tools.ietf.org/search/draft-pruss-dhcp-auth-dsl-07) - https://web.archive.org/web/20150403091552/http://tools.ietf.org/search/draft-pruss-dhcp-auth-dsl-07
### [Reference](https://www.iana.org/assignments/bootp-dhcp-parameters/bootp-dhcp-parameters.xhtml) - https://www.iana.org/assignments/bootp-dhcp-parameters/bootp-dhcp-parameters.xhtml
### [Reference](https://datatracker.ietf.org/doc/html/draft-ietf-dhc-failover-12) - https://datatracker.ietf.org/doc/html/draft-ietf-dhc-failover-12
### [Reference](https://datatracker.ietf.org/doc/html/rfc2131) - https://datatracker.ietf.org/doc/html/rfc2131
### [Reference](https://datatracker.ietf.org/doc/html/rfc2132) - https://datatracker.ietf.org/doc/html/rfc2132
### [Reference](https://datatracker.ietf.org/doc/html/rfc3046) - https://datatracker.ietf.org/doc/html/rfc3046
### [Reference](https://datatracker.ietf.org/doc/html/rfc3203) - https://datatracker.ietf.org/doc/html/rfc3203
### [Reference](https://datatracker.ietf.org/doc/html/rfc3397) - https://datatracker.ietf.org/doc/html/rfc3397
### [Reference](https://datatracker.ietf.org/doc/html/rfc3442) - https://datatracker.ietf.org/doc/html/rfc3442
### [Reference](https://datatracker.ietf.org/doc/html/rfc3942) - https://datatracker.ietf.org/doc/html/rfc3942
### [Reference](https://datatracker.ietf.org/doc/html/rfc4242) - https://datatracker.ietf.org/doc/html/rfc4242
### [Reference](https://datatracker.ietf.org/doc/html/rfc4361) - https://datatracker.ietf.org/doc/html/rfc4361
### [Reference](https://datatracker.ietf.org/doc/html/rfc4388) - https://datatracker.ietf.org/doc/html/rfc4388
### [Reference](https://datatracker.ietf.org/doc/html/rfc4436) - https://datatracker.ietf.org/doc/html/rfc4436
### [Reference](https://datatracker.ietf.org/doc/html/rfc6926) - https://datatracker.ietf.org/doc/html/rfc6926
### [Reference](https://datatracker.ietf.org/doc/html/rfc7724) - https://datatracker.ietf.org/doc/html/rfc7724
### [Reference](https://tools.ietf.org/html/rfc2131#section-4.1) - https://tools.ietf.org/html/rfc2131#section-4.1
### [Reference](https://tools.ietf.org/html/rfc2131#section-4.4.4) - https://tools.ietf.org/html/rfc2131#section-4.4.4
### [Reference](https://tools.ietf.org/html/rfc2241) - https://tools.ietf.org/html/rfc2241
### [Reference](https://tools.ietf.org/html/rfc3046) - https://tools.ietf.org/html/rfc3046
### [Reference](https://tools.ietf.org/html/rfc3118) - https://tools.ietf.org/html/rfc3118
### [Reference](https://tools.ietf.org/html/rfc3256) - https://tools.ietf.org/html/rfc3256
### [Reference](https://tools.ietf.org/html/rfc3397) - https://tools.ietf.org/html/rfc3397
### [Reference](https://tools.ietf.org/html/rfc3442) - https://tools.ietf.org/html/rfc3442
### [Reference](https://tools.ietf.org/html/rfc4833) - https://tools.ietf.org/html/rfc4833
### [Reference](https://tools.ietf.org/html/rfc5071) - https://tools.ietf.org/html/rfc5071
### [Reference](https://tools.ietf.org/html/rfc8910) - https://tools.ietf.org/html/rfc8910
### [Reference](https://www.rfc-editor.org/info/rfc2131) - https://www.rfc-editor.org/info/rfc2131
### [Reference](https://www.wikidata.org/wiki/Q11166#identifiers) - https://www.wikidata.org/wiki/Q11166#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/e/e4/DHCP_session.svg) - https://upload.wikimedia.org/wikipedia/commons/e/e4/DHCP_session.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/a/af/Dhcp-client-state-diagram.svg) - https://upload.wikimedia.org/wikipedia/commons/a/af/Dhcp-client-state-diagram.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg) - https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg