# Simple Network Management Protocol
## [URL](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol) - https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol
## Catagories
### All Wikipedia articles written in American English
### All articles containing potentially dated statements
### All articles with failed verification
### All articles with unsourced statements
### All pages needing cleanup
### Application layer protocols
### Articles containing potentially dated statements from 2004
### Articles needing cleanup from September 2016
### Articles with Curlie links
### Articles with LCCN identifiers
### Articles with failed verification from January 2022
### Articles with failed verification from November 2010
### Articles with sections that need to be turned into prose from September 2016
### Articles with short description
### Articles with unsourced statements from April 2017
### Articles with unsourced statements from June 2020
### CS1 errors: missing periodical
### CS1 maint: uses authors parameter
### Internet Standards
### Internet protocols
### Multi-agent systems
### Network management
### Short description is different from Wikidata
### System administration
### Use American English from September 2020
### Webarchive template wayback links
### "Simple Network Management Protocol (SNMP) is an Internet Standard protocol for collecting and organizing information about managed devices on IP networks and for modifying that information to change device behaviour.  Devices that typically support SNMP include cable modems, routers, switches, servers, workstations, printers, and more.SNMP is widely used in network management for network monitoring.  SNMP exposes management data in the form of variables on the managed systems organized in a management information base (MIB) which describe the system status and configuration. These variables can then be remotely queried (and, in some circumstances, manipulated) by managing applications. 
### Three significant versions of SNMP have been developed and deployed. SNMPv1 is the original version of the protocol. More recent versions, SNMPv2c and SNMPv3, feature improvements in performance, flexibility and security. 
### SNMP is a component of the Internet Protocol Suite as defined by the Internet Engineering Task Force (IETF). It consists of a set of standards for network management, including an application layer protocol, a database schema, and a set of data objects.
## Overview and basic concepts  

### In typical uses of SNMP, one or more administrative computers called managers have the task of monitoring or managing a group of hosts or devices on a computer network. Each managed system executes a software component called an agent which reports information via SNMP to the manager. 
### An SNMP-managed network consists of three key components: 

### Managed devices 
### Agent \u2013 software which runs on managed devices 
### Network management station (NMS) \u2013 software which runs on the managerA managed device is a network node that implements an SNMP interface that allows unidirectional (read-only) or bidirectional (read and write) access to node-specific information. Managed devices exchange node-specific information with the NMSs. Sometimes called network elements, the managed devices can be any type of device, including, but not limited to, routers, access servers, switches, cable modems, bridges, hubs, IP telephones, IP video cameras, computer hosts, and printers. 
### An agent is a network-management software module that resides on a managed device. An agent has local knowledge of management information and translates that information to or from an SNMP-specific form. 
### A network management station executes applications that monitor and control managed devices. NMSs provide the bulk of the processing and memory resources required for network management. One or more NMSs may exist on any managed network.
## Management information base  

### SNMP agents expose management data on the managed systems as variables. The protocol also permits active management tasks, such as configuration changes, through remote modification of these variables. The variables accessible via SNMP are organized in hierarchies. SNMP itself does not define which variables a managed system should offer. Rather, SNMP uses an extensible design that allows applications to define their own hierarchies. These hierarchies are described as a management information base (MIB). MIBs describe the structure of the management data of a device subsystem; they use a hierarchical namespace containing object identifiers (OID). Each OID identifies a variable that can be read or set via SNMP. MIBs use the notation defined by Structure of Management Information Version 2.0 (SMIv2, RFC 2578), a subset of ASN.1.
## Protocol details  
### SNMP operates in the application layer of the Internet protocol suite. All SNMP messages are transported via User Datagram Protocol (UDP). The SNMP agent receives requests on UDP port 161. The manager may send requests from any available source port to port 161 in the agent. The agent response is sent back to the source port on the manager. The manager receives notifications (Traps and InformRequests) on port 162. The agent may generate notifications from any available port. When used with Transport Layer Security or Datagram Transport Layer Security, requests are received on port 10161 and notifications are sent to port 10162.SNMPv1 specifies five core protocol data units (PDUs). Two other PDUs, GetBulkRequest and InformRequest were added in SNMPv2 and the Report PDU was added in SNMPv3. All SNMP PDUs are constructed as follows: 

### The seven SNMP PDU types as identified by the PDU-type field are as follows: 

### GetRequest 
### A manager-to-agent request to retrieve the value of a variable or list of variables. Desired variables are specified in variable bindings (the value field is not used). Retrieval of the specified variable values is to be done as an atomic operation by the agent. A Response with current values is returned. 
### SetRequest 
### A manager-to-agent request to change the value of a variable or list of variables. Variable bindings are specified in the body of the request. Changes to all specified variables are to be made as an atomic operation by the agent. A Response with (current) new values for the variables is returned. 
### GetNextRequest 
### A manager-to-agent request to discover available variables and their values. Returns a Response with variable binding for the lexicographically next variable in the MIB. The entire MIB of an agent can be walked by iterative application of GetNextRequest starting at OID 0. Rows of a table can be read by specifying column OIDs in the variable bindings of the request. 
### GetBulkRequest 
### A manager-to-agent request for multiple iterations of GetNextRequest. An optimized version of GetNextRequest. Returns a Response with multiple variable bindings walked from the variable binding or bindings in the request. PDU specific non-repeaters and max-repetitions fields are used to control response behavior. GetBulkRequest was introduced in SNMPv2. 
### Response 
### Returns variable bindings and acknowledgement from agent to manager for GetRequest, SetRequest, GetNextRequest, GetBulkRequest and InformRequest. Error reporting is provided by error-status and error-index fields. Although it was used as a response to both gets and sets, this PDU was called GetResponse in SNMPv1. 
### Trap 
### Asynchronous notification from agent to manager. While in other SNMP communication, the manager actively requests information from the agent, these are PDUs that are sent from the agent to the manager without being explicitly requested. SNMP traps enable an agent to notify the management station of significant events by way of an unsolicited SNMP message. Trap PDUs include current sysUpTime value, an OID identifying the type of trap and optional variable bindings. Destination addressing for traps is determined in an application-specific manner typically through trap configuration variables in the MIB. The format of the trap message was changed in SNMPv2 and the PDU was renamed SNMPv2-Trap. 
### InformRequest 
### Acknowledged asynchronous notification. This PDU was introduced in SNMPv2 and was originally defined as manager to manager communication. Later implementations have loosened the original definition to allow agent to manager communications. Manager-to-manager notifications were already possible in SNMPv1 using a Trap, but as SNMP commonly runs over UDP where delivery is not assured and dropped packets are not reported, delivery of a Trap was not guaranteed. InformRequest fixes this as an acknowledgement is returned on receipt.RFC 1157 specifies that an SNMP implementation must accept a message of at least 484 bytes in length. In practice, SNMP implementations accept longer messages.:\u200a1870\u200a If implemented correctly, an SNMP message is discarded if the decoding of the message fails and thus malformed SNMP requests are ignored. A successfully decoded SNMP request is then authenticated using the community string. If the authentication fails, a trap is generated indicating an authentication failure and the message is dropped.:\u200a1871\u200aSNMPv1 and SNMPv2 use communities to establish trust between managers and agents. Most agents support three community names, one each for read-only, read-write and trap. These three community strings control different types of activities. The read-only community applies to get requests. The read-write community string applies to set requests. The trap community string applies to receipt of traps. SNMPv3 also uses community strings, but allows for secure authentication and communication between SNMP manager and agent.
## Protocol versions  
### In practice, SNMP implementations often support multiple versions: typically SNMPv1, SNMPv2c, and SNMPv3.
## Version 1  
### SNMP version 1 (SNMPv1) is the initial implementation of the SNMP protocol. The design of SNMPv1 was done in the 1980s by a group of collaborators who viewed the officially sponsored OSI/IETF/NSF (National Science Foundation) effort (HEMS/CMIS/CMIP) as both unimplementable in the computing platforms of the time as well as potentially unworkable. SNMP was approved based on a belief that it was an interim protocol needed for taking steps towards large-scale deployment of the Internet and its commercialization. 
### The first Request for Comments (RFCs) for SNMP, now known as SNMPv1, appeared in 1988: 

### RFC 1065 \u2014 Structure and identification of management information for TCP/IP-based internets 
### RFC 1066 \u2014 Management information base for network management of TCP/IP-based internets 
### RFC 1067 \u2014 A simple network management protocolIn 1990, these documents were superseded by: 

### RFC 1155 \u2014 Structure and identification of management information for TCP/IP-based internets 
### RFC 1156 \u2014 Management information base for network management of TCP/IP-based internets 
### RFC 1157 \u2014 A simple network management protocolIn 1991, RFC 1156 (MIB-1) was replaced by the more often used: 

### RFC 1213 \u2014 Version 2 of management information base (MIB-2) for network management of TCP/IP-based internetsSNMPv1 is widely used and is the de facto network management protocol in the Internet community.SNMPv1 may be carried by transport layer protocols such as User Datagram Protocol (UDP), Internet Protocol (IP), OSI Connectionless-mode Network Service (CLNS), AppleTalk Datagram Delivery Protocol (DDP), and Novell Internetwork Packet Exchange (IPX). 
### Version 1 has been criticized for its poor security. The specification does, in fact, allow room for custom authentication to be used, but widely used implementations \"support only a trivial authentication service that identifies all SNMP messages as authentic SNMP messages.\". The security of the messages, therefore, becomes dependent on the security of the channels over which the messages are sent. For example, an organization may consider their internal network to be sufficiently secure that no encryption is necessary for its SNMP messages. In such cases, the \"community name\", which is transmitted in cleartext, tends to be viewed as a de facto password, in spite of the original specification.
## Version 2  
### SNMPv2, defined by RFC 1441 and RFC 1452, revises version 1 and includes improvements in the areas of performance, security and manager-to-manager communications. It introduced GetBulkRequest, an alternative to iterative GetNextRequests for retrieving large amounts of management data in a single request. The new party-based security system introduced in SNMPv2, viewed by many as overly complex, was not widely adopted.  This version of SNMP reached the Proposed Standard level of maturity, but was deemed obsolete by later versions.Community-Based Simple Network Management Protocol version 2, or SNMPv2c, is defined in RFC 1901\u2013RFC 1908.  SNMPv2c comprises SNMPv2 without the controversial new SNMP v2 security model, using instead the simple community-based security scheme of SNMPv1. This version is one of relatively few standards to meet the IETF's Draft Standard maturity level, and was widely considered the de facto SNMPv2 standard.  It was later restated as part of SNMPv3.User-Based Simple Network Management Protocol version 2, or SNMPv2u, is defined in RFC 1909\u2013RFC 1910. This is a compromise that attempts to offer greater security than SNMPv1, but without incurring the high complexity of SNMPv2. A variant of this was commercialized as SNMP v2*, and the mechanism was eventually adopted as one of two security frameworks in SNMP v3.
## 64-bit counters  
### SNMP version 2 introduces the option for 64-bit data counters. Version 1 was designed only with 32-bit counters which can store integer values from zero to 4.29 billion (precisely 4,294,967,295). A 32-bit version 1 counter cannot store the maximum speed of a 10 gigabit or larger interface, expressed in bits per second. Similarly, a 32-bit counter tracking statistics for a 10 gigabit or larger interface can roll over back to zero again in less than one minute, which may be a shorter time interval than a counter is polled to read its current state. This would result in lost or invalid data due to the undetected value rollover, and corruption of trend-tracking data. 
### The 64-bit version 2 counter can store values from zero to 18.4 quintillion (precisely 18,446,744,073,709,551,615) and so is currently unlikely to experience a counter rollover between polling events. For example, 1.6 terabit Ethernet is predicted to become available by 2025. A 64-bit counter incrementing at a rate of 1.6 trillion bits per second would be able to retain information for such an interface without rolling over for 133 days.
## SNMPv1 & SNMPv2c interoperability  
### SNMPv2c is incompatible with SNMPv1 in two key areas: message formats and protocol operations. SNMPv2c messages use different header and protocol data unit (PDU) formats than SNMPv1 messages. SNMPv2c also uses two protocol operations that are not specified in SNMPv1. To overcome incompatibility, RFC 3584 defines two SNMPv1/v2c coexistence strategies: proxy agents and bilingual network-management systems.
## Proxy agents  
### An SNMPv2 agent can act as a proxy agent on behalf of SNMPv1 managed devices. When an SNMPv2 NMS issues a command intended for an SNMPv1 agent it sends it to the SNMPv2 proxy agent instead. The proxy agent forwards Get, GetNext, and Set messages to the SNMPv1 agent unchanged. GetBulk messages are converted by the proxy agent to GetNext messages and then are forwarded to the SNMPv1 agent. Additionally, the proxy agent receives and maps SNMPv1 trap messages to SNMPv2 trap messages and then forwards them to the NMS.
## Bilingual network-management system  
### Bilingual SNMPv2 network-management systems support both SNMPv1 and SNMPv2. To support this dual-management environment, a management application examines information stored in a local database to determine whether the agent supports SNMPv1 or SNMPv2. Based on the information in the database, the NMS communicates with the agent using the appropriate version of SNMP.
## Version 3  
### Although SNMPv3 makes no changes to the protocol aside from the addition of cryptographic security, it looks very different due to new textual conventions, concepts, and terminology. The most visible change was to define a secure version of SNMP, by adding security and remote configuration enhancements to SNMP. The security aspect is addressed by offering both strong authentication and data encryption for privacy. For the administration aspect, SNMPv3 focuses on two parts, namely notification originators and proxy forwarders. The changes also facilitate remote configuration and administration of the SNMP entities, as well as addressing issues related to the large-scale deployment, accounting, and fault management. 
### Features and enhancements included: 

### Identification of SNMP entities to facilitate communication only between known SNMP entities \u2013 Each SNMP entity has an identifier called the SNMPEngineID, and SNMP communication is possible only if an SNMP entity knows the identity of its peer. Traps and Notifications are exceptions to this rule. 
### Support for security models \u2013 A security model may define the security policy within an administrative domain or an intranet. SNMPv3 contains the specifications for a user-based security model (USM). 
### Definition of security goals where the goals of message authentication service include protection against the following: 
### Modification of Information \u2013 Protection against some unauthorized SNMP entity altering in-transit messages generated by an authorized principal. 
### Masquerade \u2013 Protection against attempting management operations not authorized for some principal by assuming the identity of another principal that has the appropriate authorizations. 
### Message stream modification \u2013 Protection against messages getting maliciously re-ordered, delayed, or replayed to affect unauthorized management operations. 
### Disclosure \u2013 Protection against eavesdropping on the exchanges between SNMP engines. 
### Specification for USM \u2013 USM consists of the general definition of the following communication mechanisms available: 
### Communication without authentication and privacy (NoAuthNoPriv). 
### Communication with authentication and without privacy (AuthNoPriv). 
### Communication with authentication and privacy (AuthPriv). 
### Definition of different authentication and privacy protocols \u2013 MD5, SHA and HMAC-SHA-2 authentication protocols and the CBC_DES and CFB_AES_128 privacy protocols are supported in the USM. 
### Definition of a discovery procedure \u2013 To find the SNMPEngineID of an SNMP entity for a given transport address and transport endpoint address. 
### Definition of the time synchronization procedure \u2013 To facilitate authenticated communication between the SNMP entities. 
### Definition of the SNMP framework MIB \u2013 To facilitate remote configuration and administration of the SNMP entity. 
### Definition of the USM MIBs \u2013 To facilitate remote configuration and administration of the security module. 
### Definition of the view-based access control model (VACM) MIBs \u2013 To facilitate remote configuration and administration of the access control module.Security was one of the biggest weakness of SNMP until v3. Authentication in SNMP Versions 1 and 2 amounts to nothing more than a password (community string) sent in clear text between a manager and agent. Each SNMPv3 message contains security parameters which are encoded as an octet string. The meaning of these security parameters depends on the security model being used. The security approach in v3 targets: 
### Confidentiality \u2013 Encryption of packets to prevent snooping by an unauthorized source. 
### Integrity \u2013 Message integrity to ensure that a packet has not been tampered while in transit including an optional packet replay protection mechanism. 
### Authentication \u2013 to verify that the message is from a valid source.v3 also defines the USM and VACM, which were later followed by a transport security model (TSM) that provided support for SNMPv3 over SSH and SNMPv3 over TLS and DTLS. 

### USM (User-based Security Model) provides authentication and privacy (encryption) functions and operates at the message level. 
### VACM (View-based Access Control Model) determines whether a given principal is allowed access to a particular MIB object to perform specific functions and operates at the PDU level. 
### TSM (Transport Security Model) provides a method for authenticating and encrypting messages over external security channels.  Two transports, SSH and TLS/DTLS, have been defined that make use of the TSM specification.As of 2004 the IETF recognizes Simple Network Management Protocol version 3 as defined by RFC 3411\u2013RFC 3418 (also known as STD0062) as the current standard version of SNMP. The IETF has designated SNMPv3 a full Internet standard, the highest maturity level for an RFC. It considers earlier versions to be obsolete (designating them variously \"Historic\" or \"Obsolete\").
## Implementation issues  
### SNMP's powerful write capabilities, which would allow the configuration of network devices, are not being fully utilized by many vendors, partly because of a lack of security in SNMP versions before SNMPv3, and partly because many devices simply are not capable of being configured via individual MIB object changes. 
### Some SNMP values (especially tabular values) require specific knowledge of table indexing schemes, and these index values are not necessarily consistent across platforms. This can cause correlation issues when fetching information from multiple devices that may not employ the same table indexing scheme (for example fetching disk utilization metrics, where a specific disk identifier is different across platforms.)Some major equipment vendors tend to over-extend their proprietary command line interface (CLI) centric configuration and control systems.In February 2002 the Carnegie Mellon Software Engineering Institute (CM-SEI) Computer Emergency Response Team Coordination Center (CERT-CC) issued an Advisory on SNMPv1, after the Oulu University Secure Programming Group conducted a thorough analysis of SNMP message handling. Most SNMP implementations, regardless of which version of the protocol they support, use the same program code for decoding protocol data units (PDU) and problems were identified in this code. Other problems were found with decoding SNMP trap messages received by the SNMP management station or requests received by the SNMP agent on the network device. Many vendors had to issue patches for their SNMP implementations.:\u200a1875\u200a
## Security implications 
## Using SNMP to attack a network  
### Because SNMP is designed to allow administrators to monitor and configure network devices remotely it can also be used to penetrate a network. A significant number of software tools can scan the entire network using SNMP, therefore mistakes in the configuration of the read-write mode can make a network susceptible to attacks.:\u200a52\u200aIn 2001, Cisco released information that indicated that, even in read-only mode, the SNMP implementation of Cisco IOS is vulnerable to certain denial of service attacks. These security issues can be fixed through an IOS upgrade.If SNMP is not used in a network it should be disabled in network devices. When configuring SNMP read-only mode, close attention should be paid to the configuration of the access control and from which IP addresses SNMP messages are accepted. If the SNMP servers are identified by their IP, SNMP is only allowed to respond to these IPs and SNMP messages from other IP addresses would be denied. However, IP address spoofing remains a security concern.:\u200a54\u200a
## Authentication  
### SNMP is available in different versions, each has its own security issues. SNMP v1 sends passwords in clear-text over the network. Therefore, passwords can be read with packet sniffing. SNMP v2 allows password hashing with MD5, but this has to be configured. Virtually all network management software support SNMP v1, but not necessarily SNMP v2 or v3. SNMP v2 was specifically developed to provide data security, that is authentication, privacy and authorization, but only SNMP version 2c gained the endorsement of the Internet Engineering Task Force (IETF), while versions 2u and 2* failed to gain IETF approval due to security issues. SNMP v3 uses MD5, Secure Hash Algorithm (SHA) and keyed algorithms to offer protection against unauthorized data modification and spoofing attacks. If a higher level of security is needed the Data Encryption Standard (DES) can be optionally used in the cipher block chaining mode. SNMP v3 is implemented on Cisco IOS since release 12.0(3)T.:\u200a52\u200aSNMPv3 may be subject to brute force and dictionary attacks for guessing the authentication keys, or encryption keys, if these keys are generated from short (weak) passwords or passwords that can be found in a dictionary. SNMPv3 allows both providing random uniformly distributed cryptographic keys and generating cryptographic keys from a password supplied by the user. The risk of guessing authentication strings from hash values transmitted over the network depends on the cryptographic hash function used and the length of the hash value. SNMPv3 uses the HMAC-SHA-2 authentication protocol for the User-based Security Model (USM). SNMP does not use a more secure challenge-handshake authentication protocol. SNMPv3 (like other SNMP protocol versions) is a stateless protocol, and it has been designed with a minimal amount of interactions between the agent and the manager. Thus introducing a challenge-response handshake for each command would impose a burden on the agent (and possibly on the network itself) that the protocol designers deemed excessive and unacceptable.The security deficiencies of all SNMP versions can be mitigated by IPsec authentication and confidentiality mechanisms. SNMP also may be carried securely over Datagram Transport Layer Security (DTLS).Many SNMP implementations include a type of automatic discovery where a new network component, such as a switch or router, is discovered and polled automatically. In SNMPv1 and SNMPv2c this is done through a community string that is transmitted in clear-text to other devices. Clear-text passwords are a significant security risk. Once the community string is known outside the organization it could become the target for an attack. To alert administrators of other attempts to glean community strings, SNMP can be configured to pass community-name authentication failure traps.:\u200a54\u200a If SNMPv2 is used, the issue can be avoided by enabling password encryption on the SNMP agents of network devices.  
### The common default configuration for community strings are \"public\" for read-only access and \"private\" for read-write.:\u200a1874\u200a Because of the well-known defaults, SNMP topped the list of the SANS Institute's Common Default Configuration Issues and was number ten on the SANS Top 10 Most Critical Internet Security Threats for the year 2000. System and network administrators frequently do not change these configurations.:\u200a1874\u200aWhether it runs over TCP or UDP, SNMPv1 and v2 are vulnerable to IP spoofing attacks. With spoofing, attackers may bypass device access lists in agents that are implemented to restrict SNMP access. SNMPv3 security mechanisms such as USM or TSM prevent a successful spoofing attack.
## RFC references  
### RFC 1155 (STD 16) \u2014 Structure and Identification of Management Information for the TCP/IP-based Internets 
### RFC 1156 (Historic) \u2014 Management Information Base for Network Management of TCP/IP-based internets 
### RFC 1157 (Historic) \u2014 A Simple Network Management Protocol (SNMP) 
### RFC 1213 (STD 17) \u2014 Management Information Base for Network Management of TCP/IP-based internets: MIB-II 
### RFC 1452 (Informational) \u2014 Coexistence between version 1 and version 2 of the Internet-standard Network Management Framework (Obsoleted by RFC 1908) 
### RFC 1901 (Experimental) \u2014 Introduction to Community-based SNMPv2 
### RFC 1902 (Draft Standard) \u2014 Structure of Management Information for SNMPv2 (Obsoleted by RFC 2578) 
### RFC 1908 (Standards Track) \u2014 Coexistence between Version 1 and Version 2 of the Internet-standard Network Management Framework 
### RFC 2570 (Informational) \u2014 Introduction to Version 3 of the Internet-standard Network Management Framework  (Obsoleted by RFC 3410) 
### RFC 2578 (STD 58) \u2014 Structure of Management Information Version 2 (SMIv2) 
### RFC 3410 (Informational) \u2014 Introduction and Applicability Statements for Internet Standard Management Framework 
### STD 62 contains the following RFCs: 
### RFC 3411 \u2014 An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks 
### RFC 3412 \u2014 Message Processing and Dispatching for the Simple Network Management Protocol (SNMP) 
### RFC 3413 \u2014 Simple Network Management Protocol (SNMP) Applications 
### RFC 3414 \u2014 User-based Security Model (USM) for version 3 of the Simple Network Management Protocol (SNMPv3) 
### RFC 3415 \u2014 View-based Access Control Model (VACM) for the Simple Network Management Protocol (SNMP) 
### RFC 3416 \u2014 Version 2 of the Protocol Operations for the Simple Network Management Protocol (SNMP) 
### RFC 3417 \u2014 Transport Mappings for the Simple Network Management Protocol (SNMP) 
### RFC 3418 \u2014 Management Information Base (MIB) for the Simple Network Management Protocol (SNMP) 
### RFC 3430 (Experimental) \u2014 Simple Network Management Protocol (SNMP) over Transmission Control Protocol (TCP) Transport Mapping 
### RFC 3584 (BCP 74) \u2014 Coexistence between Version 1, Version 2, and Version 3 of the Internet-standard Network Management Framework 
### RFC 3826 (Proposed) \u2014 The Advanced Encryption Standard (AES) Cipher Algorithm in the SNMP User-based Security Model 
### RFC 4789 (Proposed) \u2014 Simple Network Management Protocol (SNMP) over IEEE 802 Networks 
### RFC 5343 (STD 78) \u2014 Simple Network Management Protocol (SNMP) Context EngineID Discovery 
### RFC 5590 (STD 78) \u2014 Transport Subsystem for the Simple Network Management Protocol (SNMP) 
### RFC 5591 (STD 78) \u2014 Transport Security Model for the Simple Network Management Protocol (SNMP) 
### RFC 5592 (Proposed) \u2014 Secure Shell Transport Model for the Simple Network Management Protocol (SNMP) 
### RFC 5608 (Proposed) \u2014  Remote Authentication Dial-In User Service (RADIUS) Usage for Simple Network Management Protocol (SNMP) Transport Models. 
### RFC 6353 (STD 78) \u2014 Transport Layer Security (TLS) Transport Model for the Simple Network Management Protocol (SNMP) 
### RFC 7630 (Proposed) \u2014 HMAC-SHA-2 Authentication Protocols in the User-based Security Model (USM) for SNMPv3
## See also  
### Agent Extensibility Protocol (AgentX) \u2013 Subagent protocol for SNMP 
### Common Management Information Protocol (CMIP) \u2013 Management protocol by ISO/OSI used by telecommunications devices 
### Common Management Information Service (CMIS) 
### Comparison of network monitoring systems 
### IEC 62379 \u2013 Control protocol based on Simple Network Management Protocol 
### Net-SNMP \u2013 Open source reference implementation of SNMP 
### NETCONF \u2013 Protocol which is an XML-based configuration protocol for network equipment 
### Remote Network Monitoring (RMON) 
### Simple Gateway Monitoring Protocol (SGMP) \u2013 Obsolete protocol replaced by SNMP 
### SNMP simulator \u2013 Software that siimulates devices supporting SNMP
## References 
## Further reading  
### Douglas Mauro; Kevin Schmidt (2005). Essential SNMP (Second ed.). O'Reilly Media. ISBN 978-0596008406. 
### William Stallings (1999). SNMP, SNMPv2, SNMPv3, and RMON 1 and 2. Addison Wesley Longman, Inc. ISBN 978-0201485349. 
### Marshall T. Rose (1996). The Simple Book. Prentice Hall. ISBN 0-13-451659-1.
## External links  
### Simple Network Management Protocol at Curlie"
## References
### [Reference](http://www.aethis.com/solutions/snmp_research/snmpv3_vs_wp.pdf) - http://www.aethis.com/solutions/snmp_research/snmpv3_vs_wp.pdf
### [Reference](http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/40700-snmp-ifIndex40700.html) - http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/40700-snmp-ifIndex40700.html
### [Reference](http://www.cisco.com/en/US/docs/ios/11_3/feature/guide/snmpinfm.html) - http://www.cisco.com/en/US/docs/ios/11_3/feature/guide/snmpinfm.html
### [Reference](http://www.cisco.com/en/US/docs/ios/12_0t/12_0t3/feature/guide/Snmp3.html) - http://www.cisco.com/en/US/docs/ios/12_0t/12_0t3/feature/guide/Snmp3.html
### [Reference](http://www.drdobbs.com/snmpv3-user-security-model/199100972) - http://www.drdobbs.com/snmpv3-user-security-model/199100972
### [Reference](http://www.snmp.com/conferences/) - http://www.snmp.com/conferences/
### [Reference](http://www.ibr.cs.tu-bs.de/projects/snmpv3/) - http://www.ibr.cs.tu-bs.de/projects/snmpv3/
### [Reference](http://lwn.net/2002/0214/a/cert-snmp.php3) - http://lwn.net/2002/0214/a/cert-snmp.php3
### [Reference](http://doi.org/10.17487%2FRFC3411) - http://doi.org/10.17487%2FRFC3411
### [Reference](http://tools.ietf.org/html/rfc7630) - http://tools.ietf.org/html/rfc7630
### [Reference](http://www.rfc-editor.org/categories/rfc-standard.html) - http://www.rfc-editor.org/categories/rfc-standard.html
### [Reference](http://www.rfc-editor.org/search/rfc_search_detail.php?pubstatus%5B%5D=Standards+Track&std_trk=Any&pub_date_type=any&wg_acronym=snmpv2) - http://www.rfc-editor.org/search/rfc_search_detail.php?pubstatus%5B%5D=Standards+Track&std_trk=Any&pub_date_type=any&wg_acronym=snmpv2
### [Reference](http://www.sans.org/top20/2000/) - http://www.sans.org/top20/2000/
### [Reference](http://www.simple-times.org/) - http://www.simple-times.org/
### [Reference](http://www.simple-times.org/pub/simple-times/issues/5-1.html) - http://www.simple-times.org/pub/simple-times/issues/5-1.html
### [Reference](https://books.google.com/books?id=6i1cCwAAQBAJ&q=snmpv1+is+obsolete&pg=PA366) - https://books.google.com/books?id=6i1cCwAAQBAJ&q=snmpv1+is+obsolete&pg=PA366
### [Reference](https://id.loc.gov/authorities/subjects/sh93003801) - https://id.loc.gov/authorities/subjects/sh93003801
### [Reference](https://www.juniper.net/techpubs/software/junos-security/junos-security10.2/mib-srx5600-srx5800-service-gateway/topic-21511.html) - https://www.juniper.net/techpubs/software/junos-security/junos-security10.2/mib-srx5600-srx5800-service-gateway/topic-21511.html
### [Reference](https://archive.org/details/ciscosecureinter00maso) - https://archive.org/details/ciscosecureinter00maso
### [Reference](https://archive.org/details/ciscosecureinter00maso/page/n51) - https://archive.org/details/ciscosecureinter00maso/page/n51
### [Reference](https://archive.org/details/snmpsnmpv2snmpv30000stal/page/619) - https://archive.org/details/snmpsnmpv2snmpv30000stal/page/619
### [Reference](https://web.archive.org/web/20071029103140/http://www.rfc-editor.org/categories/rfc-standard.html) - https://web.archive.org/web/20071029103140/http://www.rfc-editor.org/categories/rfc-standard.html
### [Reference](https://web.archive.org/web/20110719232546/http://www.cisco.com/en/US/docs/ios/12_0t/12_0t3/feature/guide/Snmp3.html) - https://web.archive.org/web/20110719232546/http://www.cisco.com/en/US/docs/ios/12_0t/12_0t3/feature/guide/Snmp3.html
### [Reference](https://web.archive.org/web/20130429201847/http://www.aethis.com/solutions/snmp_research/snmpv3_vs_wp.pdf) - https://web.archive.org/web/20130429201847/http://www.aethis.com/solutions/snmp_research/snmpv3_vs_wp.pdf
### [Reference](https://curlie.org/Computers/Internet/Protocols/SNMP) - https://curlie.org/Computers/Internet/Protocols/SNMP
### [Reference](https://datatracker.ietf.org/doc/html/rfc1065) - https://datatracker.ietf.org/doc/html/rfc1065
### [Reference](https://datatracker.ietf.org/doc/html/rfc1066) - https://datatracker.ietf.org/doc/html/rfc1066
### [Reference](https://datatracker.ietf.org/doc/html/rfc1067) - https://datatracker.ietf.org/doc/html/rfc1067
### [Reference](https://datatracker.ietf.org/doc/html/rfc1155) - https://datatracker.ietf.org/doc/html/rfc1155
### [Reference](https://datatracker.ietf.org/doc/html/rfc1156) - https://datatracker.ietf.org/doc/html/rfc1156
### [Reference](https://datatracker.ietf.org/doc/html/rfc1157) - https://datatracker.ietf.org/doc/html/rfc1157
### [Reference](https://datatracker.ietf.org/doc/html/rfc1213) - https://datatracker.ietf.org/doc/html/rfc1213
### [Reference](https://datatracker.ietf.org/doc/html/rfc1441) - https://datatracker.ietf.org/doc/html/rfc1441
### [Reference](https://datatracker.ietf.org/doc/html/rfc1452) - https://datatracker.ietf.org/doc/html/rfc1452
### [Reference](https://datatracker.ietf.org/doc/html/rfc1901) - https://datatracker.ietf.org/doc/html/rfc1901
### [Reference](https://datatracker.ietf.org/doc/html/rfc1902) - https://datatracker.ietf.org/doc/html/rfc1902
### [Reference](https://datatracker.ietf.org/doc/html/rfc1908) - https://datatracker.ietf.org/doc/html/rfc1908
### [Reference](https://datatracker.ietf.org/doc/html/rfc1909) - https://datatracker.ietf.org/doc/html/rfc1909
### [Reference](https://datatracker.ietf.org/doc/html/rfc1910) - https://datatracker.ietf.org/doc/html/rfc1910
### [Reference](https://datatracker.ietf.org/doc/html/rfc2570) - https://datatracker.ietf.org/doc/html/rfc2570
### [Reference](https://datatracker.ietf.org/doc/html/rfc2578) - https://datatracker.ietf.org/doc/html/rfc2578
### [Reference](https://datatracker.ietf.org/doc/html/rfc3410) - https://datatracker.ietf.org/doc/html/rfc3410
### [Reference](https://datatracker.ietf.org/doc/html/rfc3411) - https://datatracker.ietf.org/doc/html/rfc3411
### [Reference](https://datatracker.ietf.org/doc/html/rfc3412) - https://datatracker.ietf.org/doc/html/rfc3412
### [Reference](https://datatracker.ietf.org/doc/html/rfc3413) - https://datatracker.ietf.org/doc/html/rfc3413
### [Reference](https://datatracker.ietf.org/doc/html/rfc3414) - https://datatracker.ietf.org/doc/html/rfc3414
### [Reference](https://datatracker.ietf.org/doc/html/rfc3415) - https://datatracker.ietf.org/doc/html/rfc3415
### [Reference](https://datatracker.ietf.org/doc/html/rfc3416) - https://datatracker.ietf.org/doc/html/rfc3416
### [Reference](https://datatracker.ietf.org/doc/html/rfc3417) - https://datatracker.ietf.org/doc/html/rfc3417
### [Reference](https://datatracker.ietf.org/doc/html/rfc3418) - https://datatracker.ietf.org/doc/html/rfc3418
### [Reference](https://datatracker.ietf.org/doc/html/rfc3430) - https://datatracker.ietf.org/doc/html/rfc3430
### [Reference](https://datatracker.ietf.org/doc/html/rfc3584) - https://datatracker.ietf.org/doc/html/rfc3584
### [Reference](https://datatracker.ietf.org/doc/html/rfc3826) - https://datatracker.ietf.org/doc/html/rfc3826
### [Reference](https://datatracker.ietf.org/doc/html/rfc4789) - https://datatracker.ietf.org/doc/html/rfc4789
### [Reference](https://datatracker.ietf.org/doc/html/rfc5343) - https://datatracker.ietf.org/doc/html/rfc5343
### [Reference](https://datatracker.ietf.org/doc/html/rfc5590) - https://datatracker.ietf.org/doc/html/rfc5590
### [Reference](https://datatracker.ietf.org/doc/html/rfc5591) - https://datatracker.ietf.org/doc/html/rfc5591
### [Reference](https://datatracker.ietf.org/doc/html/rfc5592) - https://datatracker.ietf.org/doc/html/rfc5592
### [Reference](https://datatracker.ietf.org/doc/html/rfc5608) - https://datatracker.ietf.org/doc/html/rfc5608
### [Reference](https://datatracker.ietf.org/doc/html/rfc6353) - https://datatracker.ietf.org/doc/html/rfc6353
### [Reference](https://datatracker.ietf.org/doc/html/rfc7630) - https://datatracker.ietf.org/doc/html/rfc7630
### [Reference](https://tools.ietf.org/html/rfc1448#page-27) - https://tools.ietf.org/html/rfc1448#page-27
### [Reference](https://tools.ietf.org/html/rfc2573#section-3.3) - https://tools.ietf.org/html/rfc2573#section-3.3
### [Reference](https://www.rfc-editor.org/info/std62) - https://www.rfc-editor.org/info/std62
### [Reference](https://www.wikidata.org/wiki/Q184230#identifiers) - https://www.wikidata.org/wiki/Q184230#identifiers
### [Reference](https://www.worldcat.org/search?fq=x0:jrnl&q=n2:1060-6084) - https://www.worldcat.org/search?fq=x0:jrnl&q=n2:1060-6084
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/2/26/SNMP_communication_principles_diagram.PNG) - https://upload.wikimedia.org/wikipedia/commons/2/26/SNMP_communication_principles_diagram.PNG
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg) - https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/f/f2/Edit-clear.svg) - https://upload.wikimedia.org/wikipedia/en/f/f2/Edit-clear.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg