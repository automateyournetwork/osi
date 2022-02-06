# NetBIOS
## [URL](https://en.wikipedia.org/wiki/NetBIOS) - https://en.wikipedia.org/wiki/NetBIOS
## Catagories
### All articles lacking in-text citations
### All articles that are too technical
### All articles with unsourced statements
### Articles lacking in-text citations from August 2012
### Articles with NKC identifiers
### Articles with multiple maintenance issues
### Articles with short description
### Articles with unsourced statements from December 2017
### Network protocols
### Short description matches Wikidata
### Use dmy dates from July 2020
### Wikipedia articles needing clarification from June 2012
### Wikipedia articles needing clarification from October 2021
### Wikipedia articles that are too technical from September 2010
### "NetBIOS () is an acronym for Network Basic Input/Output System. It provides services related to the session layer of the OSI model allowing applications on separate computers to communicate over a local area network. As strictly an API, NetBIOS is not a networking protocol. Older operating systems ran NetBIOS over IEEE 802.2 and IPX/SPX using the NetBIOS Frames (NBF) and NetBIOS over IPX/SPX (NBX) protocols, respectively. In modern networks, NetBIOS normally runs over TCP/IP via the NetBIOS over TCP/IP (NBT) protocol. This results in each computer in the network having both an IP address and a NetBIOS name corresponding to a (possibly different) host name. NetBIOS is also used for identifying system names in TCP/IP(Windows). Simply saying, it is a protocol that allows communication of files and printers through the Session Layer of the OSI Model in a LAN.
## History and terminology  
### NetBIOS is a non-routable OSI Session Layer 5 Protocol and a service that allows applications on computers to communicate with one another over a local area network (LAN). NetBIOS was developed in 1983 by Sytek Inc. as an API for software communication over IBM PC Network LAN technology. On IBM PC Network, as an API alone, NetBIOS relied on proprietary Sytek networking protocols for communication over the wire. Despite supporting a maximum of 80 PCs in a LAN, NetBIOS became an industry standard.In 1985, IBM went forward with the Token Ring network scheme and a NetBIOS emulator was produced to allow NetBIOS-aware applications from the PC-Network era to work over this new design. This emulator, named NetBIOS Extended User Interface (NetBEUI), expanded the base NetBIOS API with, among other things, the ability to deal with the greater node capacity of Token Ring. A new networking protocol, NBF, was simultaneously produced to allow NetBEUI (NetBIOS) to provide its services over Token Ring \u2013 specifically, at the IEEE 802.2 Logical Link Control layer. 
### In 1985, Microsoft created a NetBIOS implementation for its MS-Net networking technology. As in the case of IBM's Token Ring, the services of Microsoft's NetBIOS implementation were provided over the IEEE 802.2 Logical Link Control layer by the NBF protocol. Until Microsoft adopted Domain Name System (DNS) resolution of hostnames, Microsoft operating systems used NetBIOS to resolve names in Windows client-server networks.In 1986, Novell released Advanced Novell NetWare 2.0 featuring the company's own NetBIOS emulator. Its services were encapsulated within NetWare's IPX/SPX protocol using the NetBIOS over IPX/SPX (NBX) protocol. 
### In 1987, a method of encapsulating NetBIOS in TCP and UDP packets, NetBIOS over TCP/IP (NBT), was published. It was described in RFC 1001 (\"Protocol Standard for a NetBIOS Service on a TCP/UDP Transport: Concepts and Methods\") and RFC 1002 (\"Protocol Standard for a NetBIOS Service on a TCP/UDP Transport: Detailed Specifications\"). The NBT protocol was developed in order to \"allow an implementation [of NetBIOS applications] to be built on virtually any type of system where the TCP/IP protocol suite is available,\" and to \"allow NetBIOS interoperation in the Internet.\" 
### After the PS/2 computer hit the market in 1987, IBM released the PC LAN Support Program, which included a driver for NetBIOS. 
### There is some confusion between the names NetBIOS and NetBEUI. NetBEUI originated strictly as the moniker for IBM's enhanced 1985 NetBIOS emulator for Token Ring. The name NetBEUI should have died there, considering that at the time, the NetBIOS implementations by other companies were known simply as NetBIOS regardless of whether they incorporated the API extensions found in that emulator. For MS-Net, however, Microsoft elected to name its implementation of the NBF protocol \"NetBEUI\" \u2013 naming its implementation of the transport protocol after IBM's second version of the API. Consequently Microsoft file and printer sharing over Ethernet continues to be called NetBEUI, with the name NetBIOS commonly used only in for file and printer sharing over TCP/IP. More accurately, the former is NetBIOS Frames (NBF), and the latter is NetBIOS over TCP/IP (NBT). 
### Since its original publishing in a technical reference book from IBM, the NetBIOS API specification has become a de facto standard.
## Services  
### NetBIOS provides three distinct services: 

### Name service (NetBIOS-NS) for name registration and resolution. 
### Datagram distribution service (NetBIOS-DGM) for connectionless communication. 
### Session service (NetBIOS-SSN) for connection-oriented communication.(Note: SMB, an upper layer, is a service that runs on top of the Session Service and the Datagram service, and is not to be confused as a necessary and integral part of NetBIOS itself. It can now run atop TCP with a small adaptation layer that adds a packet length to each SMB message; this is necessary because TCP only provides a byte-stream service with no notion of packet boundaries.)
## Name service  
### In order to start sessions or distribute datagrams, an application must register its NetBIOS name using the name service. NetBIOS names are 16 octets in length and vary based on the particular implementation. Frequently, the 16th octet, called the NetBIOS Suffix, designates the type of resource, and can be used to tell other applications what type of services the system offers. In NBT, the name service operates on UDP port 137 (TCP port 137 can also be used, but rarely is). 
### The name service primitives offered by NetBIOS are: 

### Add name \u2013 registers a NetBIOS name. 
### Add group name \u2013 registers a NetBIOS \"group\" name. 
### Delete name \u2013 un-registers a NetBIOS name or group name. 
### Find name \u2013 looks up a NetBIOS name on the network.NetBIOS name resolution is not supported by Microsoft for Internet Protocol Version 6 (IPv6).
## Datagram distribution service  
### Datagram mode is connectionless; the application is responsible for error detection and recovery. In NBT, the datagram service runs on UDP port 138. 
### The datagram service primitives offered by NetBIOS are: 

### Send Datagram \u2013 send a datagram to a remote NetBIOS name. 
### Send Broadcast Datagram \u2013 send a datagram to all NetBIOS names on the network. 
### Receive Datagram \u2013 wait for a packet to arrive from a Send Datagram operation. 
### Receive Broadcast Datagram \u2013 wait for a packet to arrive from a Send Broadcast Datagram operation.
## Session service  
### Session mode lets two computers establish a connection, allows messages to span multiple packets, and provides error detection and recovery. In NBT, the session service runs on TCP port 139. 
### The session service primitives offered by NetBIOS are: 

### Call \u2013 opens a session to a remote NetBIOS name. 
### Listen \u2013 listen for attempts to open a session to a NetBIOS name. 
### Hang Up \u2013 close a session. 
### Send \u2013 sends a packet to the computer on the other end of a session. 
### Send No Ack \u2013 like Send, but doesn't require an acknowledgment. 
### Receive \u2013 wait for a packet to arrive from a Send on the other end of a session.In the original protocol used to implement NetworkBIOS services on PC-Network, to establish a session, the initiating computer sends an Open request which is answered by an Open acknowledgment. The computer that started the session will then send a Session Request packet which will prompt either a Session Accept or Session Reject packet. 
### During an established session, each transmitted packet is answered by either a positive-acknowledgment (ACK) or negative-acknowledgment (NAK) response. A NAK will prompt retransmission of the data. Sessions are closed by the non-initiating computer by sending a close request. The computer that started the session will reply with a close response which prompts the final session closed packet.
## NetBIOS name vs Internet host name  
### When NetBIOS is run in conjunction with Internet protocols (e.g., NBT), each computer may have multiple names: one or more NetBIOS name service names and one or more Internet host names.
## NetBIOS name  
### The NetBIOS name is 16 ASCII characters, however Microsoft limits the host name to 15 characters and reserves the 16th character as a NetBIOS Suffix. This suffix describes the service or name record type such as host record, master browser record, or domain controller record or other services. The host name (or short host name) is specified when Windows networking is installed/configured, the suffixes registered are determined by the individual services supplied by the host. In order to connect to a computer running TCP/IP via its NetBIOS name, the name must be resolved to a network address. Today this is usually an IP address (the NetBIOS name to IP address resolution is often done by either broadcasts or a WINS Server \u2013 NetBIOS Name Server). A computer's NetBIOS name is often the same as that computer's host name (see below), although truncated to 15 characters, but it may also be completely different. 
### NetBIOS names are a sequence of alphanumeric characters. The following characters are explicitly not permitted: \\/:*?\"<>|. Since Windows 2000, NetBIOS names also had to comply with restrictions on DNS names: they cannot consist entirely of digits, and the hyphen (\"-\") or full-stop (\".\") characters may not appear as the first or last character. Since Windows 2000, Microsoft has advised against including any full-stop (\".\") characters in NetBIOS names, such that applications can use the presence of a full-stop to distinguish domain names from NetBIOS names.The Windows LMHOSTS file provides a NetBIOS name resolution method that can be used for small networks that do not use a WINS server.
## Internet host name  
### A Windows machine's NetBIOS name is not to be confused with the computer's Internet host name (assuming that the computer is also an Internet host in addition to being a NetBIOS node, which need not necessarily be the case). Generally a computer running Internet protocols (whether it is a Windows machine or not) usually has a host name (also sometimes called a machine name). Originally these names were stored in and provided by a hosts file but today most such names are part of the hierarchical Domain Name System (DNS). 
### Generally the host name of a Windows computer is based on the NetBIOS name plus the Primary DNS Suffix, which are both set in the System Properties dialog box. There may also be connection-specific suffixes which can be viewed or changed on the DNS tab in Control Panel \u2192 Network \u2192 TCP/IP \u2192 Advanced Properties. Host names are used by applications such as telnet, ftp, web browsers, etc. To connect to a computer running the TCP/IP protocol using its name, the host name must be resolved into an IP address, typically by a DNS server. (It is also possible to operate many TCP/IP-based applications, including the three listed above, using only IP addresses, but this is not the norm.)
## Node types  
### Under Windows, the node type of a networked computer relates to the way it resolves NetBIOS names to IP addresses. This assumes that there are any IP addresses for the NetBIOS nodes, which is assured only when NetBIOS operates over NBT; thus, node types are not a property of NetBIOS per se but of interaction between NetBIOS and TCP/IP in the Windows OS environment. There are four node types. 

### B-node: 0x01 Broadcast 
### P-node: 0x02 Peer (WINS only) 
### M-node: 0x04 Mixed (broadcast, then WINS) 
### H-node: 0x08 Hybrid (WINS, then broadcast)The node type in use is displayed by opening a command line and typing ipconfig /all. 
### A Windows computer registry may also be configured in such a way as to display \"unknown\" for the node type.
## NetBIOS Suffixes  
### The NetBIOS Suffix, alternately called the NetBIOS End Character (endchar), is the 16th character of a NetBIOS name and indicates service type for the registered name. The number of record types is limited to 255; some commonly used values are: 
### For unique names: 

### 00: Workstation Service (workstation name) 
### 03: Windows Messenger service 
### 06: Remote Access Service 
### 20: File Service (also called Host Record) 
### 21: Remote Access Service client 
### 1B: Domain Master Browser \u2013 Primary Domain Controller for a domain 
### 1D: Master BrowserFor group names: 

### 00: Workstation Service (workgroup/domain name) 
### 1C: Domain Controllers for a domain (group record with up to 25 IP addresses) 
### 1E: Browser Service Elections
## See also  
### NetBIOS over TCP/IP (NBT) 
### NetBIOS Frames (NBF) 
### Server Message Block (SMB)
## References 
## Further reading  
### Haugdahl, J. Scott (1990). Inside NetBIOS. Architecture Technology Corp. ISBN 99914-57-34-8 
### Silberschatz, Abraham; Galvin, Peter Baer; Gagne, Greg (2004). Operating System Concepts. (7th Ed.). John Wiley & Sons. ISBN 0-471-69466-5 
### Meyers, Michael (2004). \"Managing and Troubleshooting Networks\". McGraw-Hill. ISBN 978-0-07-225665-9 
### Tamara Dean. Network+ Guide to Networks, pg. 206 (NetBEUI)
## External links  
### LAN Technical Reference: 802.2 and NetBIOS APIs 
### Implementing CIFS (from the Samba team, published under the Open Publication License) 
### NetBIOS, NetBEUI, NBF, SMB, CIFS Networking 
### LMHOSTS File 
### NETBIOS End Characters / Suffixes \u2013 Microsoft Knowledge Base article describing list of NetBIOS Suffixes. 
### [1] \u2013 Visual Basic 2010 NetBIOS API source code. 
### Richard Sharpe (8 October 2002). \"Just what is SMB?\". Archived from the original on 2 December 2009. Retrieved 1 January 2012."
## References
### [Reference](http://samba.anu.edu.au/cifs/docs/what-is-smb.html) - http://samba.anu.edu.au/cifs/docs/what-is-smb.html
### [Reference](http://publib.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/BK8P7001/CCONTENTS) - http://publib.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/BK8P7001/CCONTENTS
### [Reference](http://support.microsoft.com/kb/163409) - http://support.microsoft.com/kb/163409
### [Reference](http://www.microsoft.com/technet/prodtechnol/windows2000serv/reskit/cnet/cnfd_lmh_qxqq.mspx?mfr=true) - http://www.microsoft.com/technet/prodtechnol/windows2000serv/reskit/cnet/cnfd_lmh_qxqq.mspx?mfr=true
### [Reference](http://ubiqx.org/cifs) - http://ubiqx.org/cifs
### [Reference](http://timothydevans.me.uk/n2c.html) - http://timothydevans.me.uk/n2c.html
### [Reference](https://support.microsoft.com/en-us/help/909264/naming-conventions-in-active-directory-for-computers-domains-sites-and) - https://support.microsoft.com/en-us/help/909264/naming-conventions-in-active-directory-for-computers-domains-sites-and
### [Reference](https://aleph.nkp.cz/F/?func=find-c&local_base=aut&ccl_term=ica=ph508942&CON_LNG=ENG) - https://aleph.nkp.cz/F/?func=find-c&local_base=aut&ccl_term=ica=ph508942&CON_LNG=ENG
### [Reference](https://archive.org/details/networkingbible00sosi) - https://archive.org/details/networkingbible00sosi
### [Reference](https://archive.org/details/networkingbible00sosi/page/n552) - https://archive.org/details/networkingbible00sosi/page/n552
### [Reference](https://web.archive.org/web/20091202045224/http://samba.anu.edu.au/cifs/docs/what-is-smb.html) - https://web.archive.org/web/20091202045224/http://samba.anu.edu.au/cifs/docs/what-is-smb.html
### [Reference](https://web.archive.org/web/20141025202805/http://www.coderbliss.com/2014/10/24/windows-7-netbios-library-in-visual-basic/) - https://web.archive.org/web/20141025202805/http://www.coderbliss.com/2014/10/24/windows-7-netbios-library-in-visual-basic/
### [Reference](https://www.wikidata.org/wiki/Q742650#identifiers) - https://www.wikidata.org/wiki/Q742650#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/a/a4/Text_document_with_red_question_mark.svg) - https://upload.wikimedia.org/wikipedia/commons/a/a4/Text_document_with_red_question_mark.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/b/b4/Ambox_important.svg) - https://upload.wikimedia.org/wikipedia/en/b/b4/Ambox_important.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/f/f2/Edit-clear.svg) - https://upload.wikimedia.org/wikipedia/en/f/f2/Edit-clear.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg