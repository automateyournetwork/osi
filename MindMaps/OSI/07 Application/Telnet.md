# Telnet
## [URL](https://en.wikipedia.org/wiki/Telnet) - https://en.wikipedia.org/wiki/Telnet
## Catagories
### All articles needing additional references
### All articles with failed verification
### Application layer protocols
### Articles needing additional references from April 2010
### Articles needing additional references from April 2014
### Articles with failed verification from January 2022
### Articles with short description
### CS1 maint: others
### History of the Internet
### Internet Protocol based network software
### Internet Standards
### Internet protocols
### Remote administration software
### Short description matches Wikidata
### Telnet
### URI schemes
### Unix network-related software
### Webarchive template wayback links
### "Telnet is an application protocol used on the Internet or local area network to provide a bidirectional interactive text-oriented communication facility using a virtual terminal connection. User data is interspersed in-band with Telnet control information in an 8-bit byte oriented data connection over the  Transmission Control Protocol (TCP). 
### Telnet was developed in 1969 beginning with RFC 15, extended in RFC 855, and standardized as Internet Engineering Task Force (IETF) Internet Standard STD 8, one of the first Internet standards. The name stands for \"teletype network\".Historically, Telnet provided access to a command-line interface on a remote host. However, because of serious security concerns when using Telnet over an open network such as the Internet, its use for this purpose has waned significantly in favor of SSH.The term telnet is also used to refer to the software that implements the client part of the protocol. Telnet client applications are available for virtually all computer platforms. Telnet is also used as a verb. To telnet means to establish a connection using the Telnet protocol, either with a command line client or with a graphical interface. For example, a common directive might be: \"To change your password, telnet into the server, log in and run the passwd command.\" In most cases, a user would be telnetting into a Unix-like server system or a network device (such as a router).
## History and standards  
### Telnet is a  client-server protocol, based on a reliable connection-oriented transport.  Typically, this protocol is used to establish a connection to Transmission Control Protocol (TCP) port number 23, where a Telnet server application (telnetd) is listening. Telnet, however, predates TCP/IP and was originally run over Network Control Program (NCP) protocols. 
### Even though Telnet was an ad hoc protocol with no official definition until March 5, 1973, the name actually referred to Teletype Over Network Protocol as the RFC 206 (NIC 7176) on Telnet makes the connection clear: 
### The TELNET protocol is based upon the notion of a virtual teletype, employing a 7-bit ASCII character set.  The primary function of a User TELNET, then, is to provide the means by which its users can 'hit' all the keys on that virtual teletype. Essentially, it used an 8-bit channel to exchange 7-bit ASCII data. Any byte with the high bit set was a special Telnet character. On March 5, 1973, a Telnet protocol standard was defined at UCLA with the publication of two NIC documents: Telnet Protocol Specification, NIC 15372, and Telnet Option Specifications, NIC 15373. 
### Many extensions were made for Telnet because of its negotiable options protocol architecture. Some of these extensions have been adopted as Internet standards, IETF documents STD 27 through STD 32. Some extensions have been widely implemented and others are proposed standards on the IETF standards track (see below) 
### Telnet is best understood in the context of a user with a simple terminal using the local Telnet program (known as the client program) to run a logon session on a remote computer where the user's communications needs are handled by a Telnet server program.
## Security  
### When Telnet was initially developed in 1969, most users of networked computers were in the computer departments of academic institutions, or at large private and government research facilities. In this environment, security was not nearly as much a concern as it became after the bandwidth explosion of the 1990s. The rise in the number of people with access to the Internet, and by extension the number of people attempting to hack other people's servers, made encrypted alternatives necessary. 
### Experts in computer security, such as SANS Institute, recommend that the use of Telnet for remote logins should be discontinued under all normal circumstances, for the following reasons: 

### Telnet, by default, does not encrypt any data sent over the connection (including passwords), and so it is often feasible to eavesdrop on the communications and use the password later for malicious purposes; anybody who has access to a router, switch, hub or gateway located on the network between the two hosts where Telnet is being used can intercept the packets passing by and obtain login, password and whatever else is typed with a packet analyzer. 
### Most implementations of Telnet have no authentication that would ensure communication is carried out between the two desired hosts and not intercepted in the middle. 
### Several vulnerabilities have been discovered over the years in commonly used Telnet daemons.These security-related shortcomings have seen the usage of the Telnet protocol drop rapidly, especially on the public Internet, in favor of the Secure Shell (SSH) protocol, first released in 1995. SSH has practically replaced Telnet, and the older protocol is used these days only in rare cases to access decades-old legacy equipment that does not support more modern protocols. SSH provides much of the functionality of telnet, with the addition of strong encryption to prevent sensitive data such as passwords from being intercepted, and public key authentication, to ensure that the remote computer is actually who it claims to be. As has happened with other early Internet protocols, extensions to the Telnet protocol provide Transport Layer Security (TLS) security and Simple Authentication and Security Layer (SASL) authentication that address the above concerns.  However, most Telnet implementations do not support these extensions; and there has been relatively little interest in implementing these as SSH is adequate for most purposes. 
### It is of note that there are a large number of industrial and scientific devices which have only Telnet available as a communication option.  Some are built with only a standard RS-232 port and use a serial server hardware appliance to provide the translation between the TCP/Telnet data and the RS-232 serial data.  In such cases, SSH is not an option unless the interface appliance can be configured for SSH (or is replaced with one supporting SSH). 
### Telnet is still used by hobbyists, especially among amateur radio operators. The Winlink protocol supports packet radio via a Telnet connection.
## Telnet 5250  
### IBM 5250 or 3270 workstation emulation is supported via custom telnet clients, TN5250/TN3270, and IBM i systems. Clients and servers designed to pass IBM 5250 data streams over Telnet generally do support SSL encryption, as SSH does not include 5250 emulation. Under IBM i (also known as OS/400), port 992 is the default port for secured telnet.
## Telnet data  
### All data octets except 0xff are transmitted over Telnet as is. 
### (0xff, or 255 in decimal, is the IAC byte (Interpret As Command) which signals that the next byte is a telnet command. The command to insert 0xff into the stream is 0xff, so 0xff must be escaped by doubling it when sending data over the telnet protocol.) 
### Telnet client applications can establish an interactive TCP session to a port other than the Telnet server port. Connections to such ports do not use IAC and all octets are sent to the server without interpretation. For example, a command line telnet client could make an HTTP request to a web server on TCP port 80 as follows: 

### There are other TCP terminal clients, such as netcat or socat on UNIX and PuTTY on Windows, which handle such requirements. Nevertheless, Telnet may still be used in debugging network services such as SMTP, IRC, HTTP, FTP or POP3, to issue commands to a server and examine the responses. 
### Another difference between Telnet and other TCP terminal clients is that Telnet is not 8-bit clean by default. 8-bit mode may be negotiated, but octets with the high bit set may be garbled until this mode is requested, as 7-bit is the default mode. The 8-bit mode (so named binary option) is intended to transmit binary data, not ASCII characters. The standard suggests the interpretation of codes 0000\u20130176 as ASCII, but does not offer any meaning for high-bit-set data octets. There was an attempt to introduce a switchable character encoding support like HTTP has, but nothing is known about its actual software support.
## Related RFCs 
## Internet Standards  
### RFC 854, Telnet Protocol Specification 
### RFC 855, Telnet Option Specifications 
### RFC 856, Telnet Binary Transmission 
### RFC 857, Telnet Echo Option 
### RFC 858, Telnet Suppress Go Ahead Option 
### RFC 859, Telnet Status Option 
### RFC 860, Telnet Timing Mark Option 
### RFC 861, Telnet Extended Options: List Option
## Proposed Standards  
### RFC 885, Telnet End of Record Option 
### RFC 1073, Telnet Window Size Option 
### RFC 1079, Telnet Terminal Speed Option 
### RFC 1091, Telnet Terminal-Type Option 
### RFC 1096, Telnet X Display Location Option 
### RFC 1123, Requirements for Internet Hosts - Application and Support 
### RFC 1184, Telnet Linemode Option 
### RFC 1372, Telnet Remote Flow Control Option 
### RFC 1572, Telnet Environment Option 
### RFC 2941, Telnet Authentication Option 
### RFC 2942, Telnet Authentication: Kerberos Version 5 
### RFC 2943, TELNET Authentication Using DSA 
### RFC 2944, Telnet Authentication: SRP 
### RFC 2946, Telnet Data Encryption Option 
### RFC 4248, The telnet URI Scheme
## Informational/experimental  
### RFC 1143, The Q Method of Implementing TELNET Option Negotiation 
### RFC 1571, Telnet Environment Option Interoperability Issues
## Other RFCs  
### RFC 1041, Telnet 3270 Regime Option 
### RFC 1205, 5250 Telnet Interface 
### RFC 2217, Telnet Com Port Control Option 
### RFC 4777, IBM's iSeries Telnet Enhancements
## Telnet clients  
### PuTTY and plink command line are a free, open-source SSH, Telnet, rlogin, and raw TCP client for Windows, Linux, and Unix. 
### AbsoluteTelnet is a telnet client for Windows.  It also supports SSH and SFTP, 
### RUMBA (Terminal Emulator) 
### Line Mode Browser, a command line web browser 
### NCSA Telnet 
### TeraTerm 
### SecureCRT from Van Dyke Software 
### ZOC Terminal 
### SyncTERM BBS terminal program supporting Telnet, SSHv2, RLogin, Serial, Windows, *nix, and Mac OS X platforms, X/Y/ZMODEM and various BBS terminal emulations 
### Rtelnet is a SOCKS client version of Telnet, providing similar functionality of telnet to those hosts which are behind firewall and NAT. 
### Inetutils includes a telnet client and server and is installed by default on many Linux distributions. 
### telnet.exe command line utility included in default installation of many versions of Microsoft Windows.
## See also  
### List of terminal emulators 
### Banner grabbing 
### Virtual terminal 
### Reverse telnet 
### HyTelnet 
### Kermit 
### SSH
## References  
### 57.9654
## External links  
### Telnet Options \u2014 the official list of assigned option numbers at iana.org 
### Telnet Interactions Described as a Sequence Diagram 
### Telnet configuration 
### Telnet protocol description, with NVT reference 
### Microsoft TechNet:Telnet commands 
### TELNET: The Mother of All (Application) Protocols 
### Troubleshoot Telnet Errors in Windows Operating System 
### \"telnet.org - information about telnet\". telnet.org. Retrieved 2020-01-07. Contains a list of telnet addresses and list of telnet clients"
## References
### [Reference](http://www.eventhelix.com/RealtimeMantra/Networking/Telnet.pdf) - http://www.eventhelix.com/RealtimeMantra/Networking/Telnet.pdf
### [Reference](http://scholar.google.com/scholar?q=%22Telnet%22) - http://scholar.google.com/scholar?q=%22Telnet%22
### [Reference](http://www.google.com/search?&q=%22Telnet%22&tbs=bkt:s&tbm=bks) - http://www.google.com/search?&q=%22Telnet%22&tbs=bkt:s&tbm=bks
### [Reference](http://www.google.com/search?as_eq=wikipedia&q=%22Telnet%22) - http://www.google.com/search?as_eq=wikipedia&q=%22Telnet%22
### [Reference](http://www.google.com/search?tbm=nws&q=%22Telnet%22+-wikipedia&tbs=ar:1) - http://www.google.com/search?tbm=nws&q=%22Telnet%22+-wikipedia&tbs=ar:1
### [Reference](http://www.google.com/search?tbs=bks:1&q=%22Telnet%22+-wikipedia) - http://www.google.com/search?tbs=bks:1&q=%22Telnet%22+-wikipedia
### [Reference](http://www-01.ibm.com/support/docview.wss?uid=nas8N1019667) - http://www-01.ibm.com/support/docview.wss?uid=nas8N1019667
### [Reference](http://www.pcmicro.com/netfoss/telnet.html) - http://www.pcmicro.com/netfoss/telnet.html
### [Reference](http://www.technig.com/troubleshoot-telnet-errors/) - http://www.technig.com/troubleshoot-telnet-errors/
### [Reference](http://www2.sims.berkeley.edu/courses/is250/s99/articles/w3088.pdf) - http://www2.sims.berkeley.edu/courses/is250/s99/articles/w3088.pdf
### [Reference](http://ietf.org/rfc/rfc0206.txt) - http://ietf.org/rfc/rfc0206.txt
### [Reference](http://telnet.org/) - http://telnet.org/
### [Reference](http://www.worldcat.org/oclc/263353270) - http://www.worldcat.org/oclc/263353270
### [Reference](https://technet.microsoft.com/en-us/library/bb491013.aspx) - https://technet.microsoft.com/en-us/library/bb491013.aspx
### [Reference](https://www.ssh.com/ssh/telnet) - https://www.ssh.com/ssh/telnet
### [Reference](https://www.wired.com/2007/04/telnet_dead_at_/) - https://www.wired.com/2007/04/telnet_dead_at_/
### [Reference](https://web.archive.org/web/20160918095706/http://www-01.ibm.com/support/docview.wss?uid=nas8N1019667) - https://web.archive.org/web/20160918095706/http://www-01.ibm.com/support/docview.wss?uid=nas8N1019667
### [Reference](https://web.archive.org/web/20161221012744/https://www.wired.com/2007/04/telnet_dead_at_/) - https://web.archive.org/web/20161221012744/https://www.wired.com/2007/04/telnet_dead_at_/
### [Reference](https://web.archive.org/web/20170315080607/http://ietf.org/rfc/rfc0206.txt) - https://web.archive.org/web/20170315080607/http://ietf.org/rfc/rfc0206.txt
### [Reference](https://web.archive.org/web/20180702181236/http://telecomacadmey.com/configure-telnet/) - https://web.archive.org/web/20180702181236/http://telecomacadmey.com/configure-telnet/
### [Reference](https://web.archive.org/web/20180725073549/https://www.ssh.com/ssh/telnet) - https://web.archive.org/web/20180725073549/https://www.ssh.com/ssh/telnet
### [Reference](https://www.iana.org/assignments/telnet-options) - https://www.iana.org/assignments/telnet-options
### [Reference](https://datatracker.ietf.org/doc/html/rfc1041) - https://datatracker.ietf.org/doc/html/rfc1041
### [Reference](https://datatracker.ietf.org/doc/html/rfc1073) - https://datatracker.ietf.org/doc/html/rfc1073
### [Reference](https://datatracker.ietf.org/doc/html/rfc1079) - https://datatracker.ietf.org/doc/html/rfc1079
### [Reference](https://datatracker.ietf.org/doc/html/rfc1091) - https://datatracker.ietf.org/doc/html/rfc1091
### [Reference](https://datatracker.ietf.org/doc/html/rfc1096) - https://datatracker.ietf.org/doc/html/rfc1096
### [Reference](https://datatracker.ietf.org/doc/html/rfc1123) - https://datatracker.ietf.org/doc/html/rfc1123
### [Reference](https://datatracker.ietf.org/doc/html/rfc1143) - https://datatracker.ietf.org/doc/html/rfc1143
### [Reference](https://datatracker.ietf.org/doc/html/rfc1184) - https://datatracker.ietf.org/doc/html/rfc1184
### [Reference](https://datatracker.ietf.org/doc/html/rfc1205) - https://datatracker.ietf.org/doc/html/rfc1205
### [Reference](https://datatracker.ietf.org/doc/html/rfc1372) - https://datatracker.ietf.org/doc/html/rfc1372
### [Reference](https://datatracker.ietf.org/doc/html/rfc15) - https://datatracker.ietf.org/doc/html/rfc15
### [Reference](https://datatracker.ietf.org/doc/html/rfc1571) - https://datatracker.ietf.org/doc/html/rfc1571
### [Reference](https://datatracker.ietf.org/doc/html/rfc1572) - https://datatracker.ietf.org/doc/html/rfc1572
### [Reference](https://datatracker.ietf.org/doc/html/rfc2217) - https://datatracker.ietf.org/doc/html/rfc2217
### [Reference](https://datatracker.ietf.org/doc/html/rfc2941) - https://datatracker.ietf.org/doc/html/rfc2941
### [Reference](https://datatracker.ietf.org/doc/html/rfc2942) - https://datatracker.ietf.org/doc/html/rfc2942
### [Reference](https://datatracker.ietf.org/doc/html/rfc2943) - https://datatracker.ietf.org/doc/html/rfc2943
### [Reference](https://datatracker.ietf.org/doc/html/rfc2944) - https://datatracker.ietf.org/doc/html/rfc2944
### [Reference](https://datatracker.ietf.org/doc/html/rfc2946) - https://datatracker.ietf.org/doc/html/rfc2946
### [Reference](https://datatracker.ietf.org/doc/html/rfc4248) - https://datatracker.ietf.org/doc/html/rfc4248
### [Reference](https://datatracker.ietf.org/doc/html/rfc4777) - https://datatracker.ietf.org/doc/html/rfc4777
### [Reference](https://datatracker.ietf.org/doc/html/rfc854) - https://datatracker.ietf.org/doc/html/rfc854
### [Reference](https://datatracker.ietf.org/doc/html/rfc855) - https://datatracker.ietf.org/doc/html/rfc855
### [Reference](https://datatracker.ietf.org/doc/html/rfc856) - https://datatracker.ietf.org/doc/html/rfc856
### [Reference](https://datatracker.ietf.org/doc/html/rfc857) - https://datatracker.ietf.org/doc/html/rfc857
### [Reference](https://datatracker.ietf.org/doc/html/rfc858) - https://datatracker.ietf.org/doc/html/rfc858
### [Reference](https://datatracker.ietf.org/doc/html/rfc859) - https://datatracker.ietf.org/doc/html/rfc859
### [Reference](https://datatracker.ietf.org/doc/html/rfc860) - https://datatracker.ietf.org/doc/html/rfc860
### [Reference](https://datatracker.ietf.org/doc/html/rfc861) - https://datatracker.ietf.org/doc/html/rfc861
### [Reference](https://datatracker.ietf.org/doc/html/rfc885) - https://datatracker.ietf.org/doc/html/rfc885
### [Reference](https://www.jstor.org/action/doBasicSearch?Query=%22Telnet%22&acc=on&wc=on) - https://www.jstor.org/action/doBasicSearch?Query=%22Telnet%22&acc=on&wc=on
### [Reference](https://www.worldcat.org/oclc/263353270) - https://www.worldcat.org/oclc/263353270
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/6/6d/Busybox_DG834Gt.PNG) - https://upload.wikimedia.org/wikipedia/commons/6/6d/Busybox_DG834Gt.PNG
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg