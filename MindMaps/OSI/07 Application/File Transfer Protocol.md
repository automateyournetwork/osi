# File Transfer Protocol
## [URL](https://en.wikipedia.org/wiki/File_Transfer_Protocol) - https://en.wikipedia.org/wiki/File_Transfer_Protocol
## Catagories
### All articles with failed verification
### Application layer protocols
### Articles with GND identifiers
### Articles with LCCN identifiers
### Articles with failed verification from January 2022
### Articles with short description
### CS1 maint: bot: original URL status unknown
### CS1 maint: url-status
### Clear text protocols
### Computer-related introductions in 1971
### File Transfer Protocol
### File sharing
### History of the Internet
### Internet Standards
### Network file transfer protocols
### OS/2 commands
### Short description matches Wikidata
### Unix network-related software
### Use dmy dates from August 2016
### "The File Transfer Protocol (FTP) is a standard communication protocol used for the transfer of computer files from a server to a client on a computer network. FTP is built on a client\u2013server model architecture using separate control and data connections between the client and the server. FTP users may authenticate themselves with a clear-text sign-in protocol, normally in the form of a username and password, but can connect anonymously if the server is configured to allow it. For secure transmission that protects the username and password, and encrypts the content, FTP is often secured with SSL/TLS (FTPS) or replaced with SSH File Transfer Protocol (SFTP). 
### The first FTP client applications were command-line programs developed before operating systems had graphical user interfaces, and are still shipped with most Windows, Unix, and Linux operating systems. Many FTP clients and automation utilities have since been developed for desktops, servers, mobile devices, and hardware, and FTP has been incorporated into productivity applications, such as HTML editors. 
### In January 2021, support for the FTP protocol was disabled in Google Chrome 88, and disabled in Firefox 88.0. In July 2021, Firefox 90 dropped FTP entirely, and Google followed suit in October 2021, removing FTP entirely in Google Chrome 95.
## History of FTP servers  
### The original specification for the File Transfer Protocol was written by Abhay Bhushan and published as RFC 114 on 16 April 1971. Until 1980, FTP ran on NCP, the predecessor of TCP/IP. The protocol was later replaced by a TCP/IP version, RFC 765 (June 1980) and RFC 959 (October 1985), the current specification. Several proposed standards amend RFC 959, for example RFC 1579 (February 1994) enables Firewall-Friendly FTP (passive mode), RFC 2228 (June 1997) proposes security extensions, RFC 2428 (September 1998) adds support for IPv6 and defines a new type of passive mode.
## Protocol overview 
## Communication and data transfer  

### FTP may run in active or passive mode, which determines how the data connection is established. (This sense of \"mode\" is different from that of the MODE command in the FTP protocol, and corresponds to the PORT/PASV/EPSV/etc commands instead.) In both cases, the client creates a TCP control connection from a random, usually an unprivileged, port N to the FTP server command port 21. 

### In active mode, the client starts listening for incoming data connections from the server on port M. It sends the FTP command PORT M to inform the server on which port it is listening. The server then initiates a data channel to the client from its port 20, the FTP server data port. 
### In situations where the client is behind a firewall and unable to accept incoming TCP connections, passive mode may be used. In this mode, the client uses the control connection to send a PASV command to the server and then receives a server IP address and server port number from the server, which the client then uses to open a data connection from an arbitrary client port to the server IP address and server port number received.Both modes were updated in September 1998 to support IPv6. Further changes were introduced to the passive mode at that time, updating it to extended passive mode.The server responds over the control connection with three-digit status codes in ASCII with an optional text message. For example, \"200\" (or \"200 OK\") means that the last command was successful. The numbers represent the code for the response and the optional text represents a human-readable explanation or request (e.g. <Need account for storing file>). An ongoing transfer of file data over the data connection can be aborted using an interrupt message sent over the control connection. 
### FTP needs two ports (one for sending and one for receiving) because it was originally designed to operate on Network Control Program (NCP), which was a simplex protocol that utilized two port addresses, establishing two connections, for two-way communications. An odd and an even port were reserved for each application layer application or protocol. The standardization of TCP and UDP reduced the need for the use of two simplex ports for each application down to one duplex port,:\u200a15\u200a but the FTP protocol was never altered to only use one port, and continued using two for backwards compatibility.
## NAT and firewall traversal  
### FTP normally transfers data by having the server connect back to the client, after the PORT command is sent by the client. This is problematic for both NATs and firewalls, which do not allow connections from the Internet towards internal hosts. For NATs, an additional complication is that the representation of the IP addresses and port number in the PORT command refer to the internal host's IP address and port, rather than the public IP address and port of the NAT. 
### There are two approaches to solve this problem. One is that the FTP client and FTP server use the PASV command, which causes the data connection to be established from the FTP client to the server. This is widely used by modern FTP clients. Another approach is for the NAT to alter the values of the PORT command, using an application-level gateway for this purpose.
## Data types  
### While transferring data over the network, four data types are defined: 
### ASCII (TYPE A): Used for text. Data is converted, if needed, from the sending host's character representation to \"8-bit ASCII\" before transmission, and (again, if necessary) to the receiving host's character representation. As a consequence, this mode is inappropriate for files that contain data other than plain text. 
### Image (TYPE I, commonly called Binary mode): The sending machine sends each file byte by byte, and the recipient stores the bytestream as it receives it. (Image mode support has been recommended for all implementations of FTP). 
### EBCDIC (TYPE E): Used for plain text between hosts using the EBCDIC character set. 
### Local (TYPE L n): Designed to support file transfer between machines which do not use 8-bit bytes, e.g. 36-bit systems such as DEC PDP-10s. For example, \"TYPE L 9\" would be used to transfer data in 9-bit bytes, or \"TYPE L 36\" to transfer 36-bit words. Most contemporary FTP clients/servers only support L 8, which is equivalent to I.An expired Internet Draft defined a TYPE U for transferring Unicode text files using UTF-8; although the draft never became an RFC, it has been implemented by several FTP clients/servers. 
### Note these data types are commonly called \"modes\", although ambiguously that word is also used to refer to active-vs-passive communication mode (see above), and the modes set by the FTP protocol MODE command (see below). 
### For text files (TYPE A and TYPE E), three different format control options are provided, to control how the file would be printed: 

### Non-print (TYPE A N and TYPE E N) \u2013 the file does not contain any carriage control characters intended for a printer 
### Telnet (TYPE A T and TYPE E T) \u2013 the file contains Telnet (or in other words, ASCII C0) carriage control characters (CR, LF, etc) 
### ASA (TYPE A A and TYPE E A) \u2013 the file contains ASA carriage control charactersThese formats were mainly relevant to line printers; most contemporary FTP clients/servers only support the default format control of N.
## File structures  
### File organization is specified using the STRU command. The following file structures are defined in section 3.1.1 of RFC959: 

### F or FILE structure (stream-oriented). Files are viewed as an arbitrary sequence of bytes, characters or words. This is the usual file structure on Unix systems and other systems such as CP/M, MS-DOS and Microsoft Windows. (Section 3.1.1.1) 
### R or RECORD structure (record-oriented). Files are viewed as divided into records, which may be fixed or variable length. This file organization is common on mainframe and midrange systems, such as MVS, VM/CMS, OS/400 and VMS, which support record-oriented filesystems. 
### P or PAGE structure (page-oriented). Files are divided into pages, which may either contain data or metadata; each page may also have a header giving various attributes. This file structure was specifically designed for TENEX systems, and is generally not supported on other platforms. RFC1123 section 4.1.2.3 recommends that this structure not be implemented.Most contemporary FTP clients and servers only support STRU F. STRU R is still in use in mainframe and minicomputer file transfer applications.
## Data transfer modes  
### Data transfer can be done in any of three modes: 
### Stream mode (MODE S): Data is sent as a continuous stream, relieving FTP from doing any processing. Rather, all processing is left up to TCP. No End-of-file indicator is needed, unless the data is divided into records. 
### Block mode (MODE B): Designed primarily for transferring record-oriented files (STRU R), although can also be used to transfer stream-oriented (STRU F) text files. FTP puts each record (or line) of data into several blocks (block header, byte count, and data field) and then passes it on to TCP. 
### Compressed mode (MODE C): Extends MODE B with data compression using run-length encoding.Most contemporary FTP clients and servers do not implement MODE B or MODE C; FTP clients and servers for mainframe and minicomputer operating systems are the exception to that. 
### Some FTP software also implements a DEFLATE-based compressed mode, sometimes called \"Mode Z\" after the command that enables it. This mode was described in an Internet Draft, but not standardized.GridFTP defines additional modes, MODE E and MODE X, as extensions of MODE B.
## Additional commands  
### More recent implementations of FTP support the Modify Fact: Modification Time (MFMT) command, which allows a client to adjust that file attribute remotely, enabling the preservation of that attribute when uploading files.To retrieve a remote file timestamp, there's MDTM command. Some servers (and clients) support nonstandard syntax of the MDTM command with two arguments, that works the same way as MFMT
## Login  
### FTP login uses normal username and password scheme for granting access. The username is sent to the server using the USER command, and the password is sent using the PASS command. This sequence is unencrypted \"on the wire\", so may be vulnerable to a network sniffing attack. If the information provided by the client is accepted by the server, the server will send a greeting to the client and the session will commence. If the server supports it, users may log in without providing login credentials, but the same server may authorize only limited access for such sessions.
## Anonymous FTP  
### A host that provides an FTP service may provide anonymous FTP access. Users typically log into the service with an 'anonymous' (lower-case and case-sensitive in some FTP servers) account when prompted for user name. Although users are commonly asked to send their email address instead of a password, no verification is actually performed on the supplied data. Many FTP hosts whose purpose is to provide software updates will allow anonymous logins.
## Differences from HTTP  
### HTTP essentially fixes the bugs in FTP that made it inconvenient to use for many small ephemeral transfers as are typical in web pages. 
### FTP has a stateful control connection which maintains a current working directory and other flags, and each transfer requires a secondary connection through which the data are transferred. In \"passive\" mode this secondary connection is from client to server, whereas in the default \"active\" mode this connection is from server to client. This apparent role reversal when in active mode, and random port numbers for all transfers, is why firewalls and NAT gateways have such a hard time with FTP. HTTP is stateless and multiplexes control and data over a single connection from client to server on well-known port numbers, which trivially passes through NAT gateways and is simple for firewalls to manage. 
### Setting up an FTP control connection is quite slow due to the round-trip delays of sending all of the required commands and awaiting responses, so it is customary to bring up a control connection and hold it open for multiple file transfers rather than drop and re-establish the session afresh each time. In contrast, HTTP originally dropped the connection after each transfer because doing so was so cheap. While HTTP has subsequently gained the ability to reuse the TCP connection for multiple transfers, the conceptual model is still of independent requests rather than a session. 
### When FTP is transferring over the data connection, the control connection is idle. If the transfer takes too long, the firewall or NAT may decide that the control connection is dead and stop tracking it, effectively breaking the connection and confusing the download. The single HTTP connection is only idle  between requests and it is normal and expected for such connections to be dropped after a time-out.
## Software support 
## Web browser  
### Most common web browsers can retrieve files hosted on FTP servers, although they may not support protocol extensions such as FTPS. When an FTP\u2014rather than an HTTP\u2014URL is supplied, the accessible contents on the remote server are presented in a manner that is similar to that used for other web content. FireFTP is an browser extension designed as a full-featured FTP client, it could be run within Firefox in the past, but it's now recommend working with Waterfox. 
### Google Chrome removed FTP support entirely in Chrome 88. As of 2019, Mozilla was discussing proposals, including only removing support for old FTP implementations that are no longer in use to simplify their code. In April, 2021, Mozilla released Firefox 88.0 which disabled FTP support by default. In July 2021, Firefox 90 dropped FTP support entirely.
## Syntax  
### FTP URL syntax is described in RFC 1738, taking the form: ftp://[user[:password]@]host[:port]/url-path (the bracketed parts are optional). 
### For example, the URL ftp://public.ftp-servers.example.com/mydirectory/myfile.txt represents the file myfile.txt from the directory mydirectory on the server public.ftp-servers.example.com as an FTP resource. The URL ftp://user001:secretpassword@private.ftp-servers.example.com/mydirectory/myfile.txt adds a specification of the username and password that must be used to access this resource. 
### More details on specifying a username and password may be found in the browsers' documentation (e.g., Firefox and Internet Explorer). By default, most web browsers use passive (PASV) mode, which more easily traverses end-user firewalls. 
### Some variation has existed in how different browsers treat path resolution in cases where there is a non-root home directory for a user.
## Download manager  
### Most common download managers can receive files hosted on FTP servers, while some of them also give the interface to retrieve the files hosted on FTP servers. DownloadStudio and Internet Download Accelerator allows not only download a file from FTP server but also view the list of files on a FTP server.
## Security  
### FTP was not designed to be a secure protocol, and has many security weaknesses. In May 1999, the authors of RFC 2577 listed a vulnerability to the following problems: 

### Brute-force attack 
### FTP bounce attack 
### Packet capture 
### Port stealing (guessing the next open port and usurping a legitimate connection) 
### Spoofing attack 
### Username enumeration 
### DoS or DDoSFTP does not encrypt its traffic; all transmissions are in clear text, and usernames, passwords, commands and data can be read by anyone able to perform packet capture (sniffing) on the network. This problem is common to many of the Internet Protocol specifications (such as SMTP, Telnet, POP and IMAP) that were designed prior to the creation of encryption mechanisms such as TLS or SSL.Common solutions to this problem include: 

### Using the secure versions of the insecure protocols, e.g., FTPS instead of FTP and TelnetS instead of Telnet. 
### Using a different, more secure protocol that can handle the job, e.g. SSH File Transfer Protocol or Secure Copy Protocol. 
### Using a secure tunnel such as Secure Shell (SSH) or virtual private network (VPN).
## FTP over SSH  
### FTP over SSH is the practice of tunneling a normal FTP session over a Secure Shell connection. Because FTP uses multiple TCP connections (unusual for a TCP/IP protocol that is still in use), it is particularly difficult to tunnel over SSH. With many SSH clients, attempting to set up a tunnel for the control channel (the initial client-to-server connection on port 21) will protect only that channel; when data is transferred, the FTP software at either end sets up new TCP connections (data channels) and thus have no confidentiality or integrity protection. 
### Otherwise, it is necessary for the SSH client software to have specific knowledge of the FTP protocol, to monitor and rewrite FTP control channel messages and autonomously open new packet forwardings for FTP data channels. Software packages that support this mode include: 

### Tectia ConnectSecure (Win/Linux/Unix) of SSH Communications Security's software suite
## Derivatives 
## FTPS  

### Explicit FTPS is an extension to the FTP standard that allows clients to request FTP sessions to be encrypted. This is done by sending the \"AUTH TLS\" command. The server has the option of allowing or denying connections that do not request TLS. This protocol extension is defined in RFC 4217. Implicit FTPS is an outdated standard for FTP that required the use of a SSL or TLS connection. It was specified to use different ports than plain FTP.
## SSH File Transfer Protocol  

### The SSH file transfer protocol (chronologically the second of the two protocols abbreviated SFTP) transfers files and has a similar command set for users, but uses the Secure Shell protocol (SSH) to transfer files. Unlike FTP, it encrypts both commands and data, preventing passwords and sensitive information from being transmitted openly over the network. It cannot interoperate with FTP software.
## Trivial File Transfer Protocol  

### Trivial File Transfer Protocol (TFTP) is a simple, lock-step FTP that allows a client to get a file from or put a file onto a remote host. One of its primary uses is in the early stages of booting from a local area network, because TFTP is very simple to implement. TFTP lacks security and most of the advanced features offered by more robust file transfer protocols such as File Transfer Protocol. TFTP was first standardized in 1981 and the current specification for the protocol can be found in RFC 1350.
## Simple File Transfer Protocol  
### Simple File Transfer Protocol (the first protocol abbreviated SFTP), as defined by RFC 913, was proposed as an (unsecured) file transfer protocol with a level of complexity intermediate between TFTP and FTP. It was never widely accepted on the Internet, and is now assigned Historic status by the IETF. It runs through port 115, and often receives the initialism of SFTP. It has a command set of 11 commands and support three types of data transmission: ASCII, binary and continuous. For systems with a word size that is a multiple of 8 bits, the implementation of binary and continuous is the same. The protocol also supports login with user ID and password, hierarchical folders and file management (including rename, delete, upload, download, download with overwrite, and download with append).
## FTP commands 
## FTP reply codes  

### Below is a summary of FTP reply codes that may be returned by an FTP server. These codes have been standardized in RFC 959 by the IETF. The reply code is a three-digit value. The first digit is used to indicate one of three possible outcomes \u2014 success, failure, or to indicate an error or incomplete reply: 

### 2yz \u2013 Success reply 
### 4yz or 5yz \u2013 Failure reply 
### 1yz or 3yz \u2013 Error or Incomplete replyThe second digit defines the kind of error: 

### x0z \u2013 Syntax. These replies refer to syntax errors. 
### x1z \u2013 Information. Replies to requests for information. 
### x2z \u2013 Connections. Replies referring to the control and data connections. 
### x3z \u2013 Authentication and accounting. Replies for the login process and accounting procedures. 
### x4z \u2013 Not defined. 
### x5z \u2013 File system. These replies relay status codes from the server file system.The third digit of the reply code is used to provide additional detail for each of the categories defined by the second digit.
## See also 
## References 
## Further reading  
### RFC 697 \u2013 CWD Command of FTP. July 1975. 
### RFC 959 \u2013 (Standard) File Transfer Protocol (FTP). J. Postel, J. Reynolds. October 1985. 
### RFC 1579 \u2013 (Informational) Firewall-Friendly FTP. February 1994. 
### RFC 1635 \u2013 (Informational) How to Use Anonymous FTP. May 1994. 
### RFC 1639 \u2013 FTP Operation Over Big Address Records (FOOBAR). June 1994. 
### RFC 1738 \u2013 Uniform Resource Locators (URL). December 1994. 
### RFC 2228 \u2013 (Proposed Standard) FTP Security Extensions. October 1997. 
### RFC 2389 \u2013 (Proposed Standard) Feature negotiation mechanism for the File Transfer Protocol. August 1998. 
### RFC 2428 \u2013 (Proposed Standard) Extensions for IPv6, NAT, and Extended passive mode. September 1998. 
### RFC 2577 \u2013 (Informational) FTP Security Considerations. May 1999. 
### RFC 2640 \u2013 (Proposed Standard) Internationalization of the File Transfer Protocol. July 1999. 
### RFC 3659 \u2013 (Proposed Standard) Extensions to FTP. P. Hethmon. March 2007. 
### RFC 5797 \u2013 (Proposed Standard) FTP Command and Extension Registry. March 2010. 
### RFC 7151 \u2013 (Proposed Standard) File Transfer Protocol HOST Command for Virtual Hosts.  March 2014. 
### IANA FTP Commands and Extensions registry \u2013 The official registry of FTP Commands and Extensions
## External links  
Communication Networks/File Transfer Protocol at Wikibooks 
### FTP Server Online Tester Authentication, encryption, mode and connectivity. 
### Anonymous FTP Servers by Country Code TLD (2012): \"Offbeat Internet - Public Access - FTP\". www.jumpjet.info. 2012. Retrieved 16 January 2020."
## References
### [Reference](http://www.conceiva.com/products/downloadstudio/features.asp) - http://www.conceiva.com/products/downloadstudio/features.asp
### [Reference](http://slacksite.com/other/ftp.html) - http://slacksite.com/other/ftp.html
### [Reference](http://www.tcpipguide.com/free/t_FTPOverviewHistoryandStandards.htm) - http://www.tcpipguide.com/free/t_FTPOverviewHistoryandStandards.htm
### [Reference](http://servertest.online/ftp) - http://servertest.online/ftp
### [Reference](https://www.androidpolice.com/2021/07/14/firefox-90-fully-removes-ftp-support-and-reorganizes-some-settings-apk-download/) - https://www.androidpolice.com/2021/07/14/firefox-90-fully-removes-ftp-support-and-reorganizes-some-settings-apk-download/
### [Reference](https://www.chromestatus.com/feature/6246151319715840) - https://www.chromestatus.com/feature/6246151319715840
### [Reference](https://developers.google.com/web/updates/2020/10/chrome-87-deps-rems) - https://developers.google.com/web/updates/2020/10/chrome-87-deps-rems
### [Reference](https://www.ncftp.com/ncftpd/doc/misc/ftp_and_firewalls.html) - https://www.ncftp.com/ncftpd/doc/misc/ftp_and_firewalls.html
### [Reference](https://nurdletech.com/linux-notes/ftp/ssh.html) - https://nurdletech.com/linux-notes/ftp/ssh.html
### [Reference](https://www.securityweek.com/should-organizations-retire-ftp-security) - https://www.securityweek.com/should-organizations-retire-ftp-security
### [Reference](https://www.serv-u.com/resource/tutorial/dsiz-mfct-mfmt-avbl-pass-xpwd-xmkd-ftp-command) - https://www.serv-u.com/resource/tutorial/dsiz-mfct-mfmt-avbl-pass-xpwd-xmkd-ftp-command
### [Reference](https://support.solarwinds.com/SuccessCenter/s/article/MDTM-FTP-command) - https://support.solarwinds.com/SuccessCenter/s/article/MDTM-FTP-command
### [Reference](https://support.solarwinds.com/SuccessCenter/s/article/MFMT-FTP-command) - https://support.solarwinds.com/SuccessCenter/s/article/MFMT-FTP-command
### [Reference](https://www.ssh.com/manuals/mft-events-product/63/ssh-solutions-your-business-components.html) - https://www.ssh.com/manuals/mft-events-product/63/ssh-solutions-your-business-components.html
### [Reference](https://www.westbyte.com/ida/index.phtml?page=features&tmp=1&lng=English) - https://www.westbyte.com/ida/index.phtml?page=features&tmp=1&lng=English
### [Reference](https://jkorpela.fi/ftpurl.html) - https://jkorpela.fi/ftpurl.html
### [Reference](https://id.loc.gov/authorities/subjects/sh95000465) - https://id.loc.gov/authorities/subjects/sh95000465
### [Reference](https://d-nb.info/gnd/4268371-3) - https://d-nb.info/gnd/4268371-3
### [Reference](https://www.jumpjet.info/Offbeat-Internet/Public/FTP/url.htm) - https://www.jumpjet.info/Offbeat-Internet/Public/FTP/url.htm
### [Reference](https://web.archive.org/web/20150702005840/https://support.microsoft.com/en-us/kb/135975) - https://web.archive.org/web/20150702005840/https://support.microsoft.com/en-us/kb/135975
### [Reference](https://web.archive.org/web/20200731160323/https://www.ssh.com/manuals/mft-events-product/63/ssh-solutions-your-business-components.html) - https://web.archive.org/web/20200731160323/https://www.ssh.com/manuals/mft-events-product/63/ssh-solutions-your-business-components.html
### [Reference](https://www.iana.org/assignments/ftp-commands-extensions/ftp-commands-extensions.xhtml) - https://www.iana.org/assignments/ftp-commands-extensions/ftp-commands-extensions.xhtml
### [Reference](https://datatracker.ietf.org/doc/html/draft-klensin-ftpext-typeu-00) - https://datatracker.ietf.org/doc/html/draft-klensin-ftpext-typeu-00
### [Reference](https://datatracker.ietf.org/doc/html/draft-preston-ftpext-deflate-03) - https://datatracker.ietf.org/doc/html/draft-preston-ftpext-deflate-03
### [Reference](https://datatracker.ietf.org/doc/html/rfc114) - https://datatracker.ietf.org/doc/html/rfc114
### [Reference](https://datatracker.ietf.org/doc/html/rfc1350) - https://datatracker.ietf.org/doc/html/rfc1350
### [Reference](https://datatracker.ietf.org/doc/html/rfc1579) - https://datatracker.ietf.org/doc/html/rfc1579
### [Reference](https://datatracker.ietf.org/doc/html/rfc1635) - https://datatracker.ietf.org/doc/html/rfc1635
### [Reference](https://datatracker.ietf.org/doc/html/rfc1639) - https://datatracker.ietf.org/doc/html/rfc1639
### [Reference](https://datatracker.ietf.org/doc/html/rfc1738) - https://datatracker.ietf.org/doc/html/rfc1738
### [Reference](https://datatracker.ietf.org/doc/html/rfc2228) - https://datatracker.ietf.org/doc/html/rfc2228
### [Reference](https://datatracker.ietf.org/doc/html/rfc2389) - https://datatracker.ietf.org/doc/html/rfc2389
### [Reference](https://datatracker.ietf.org/doc/html/rfc2428) - https://datatracker.ietf.org/doc/html/rfc2428
### [Reference](https://datatracker.ietf.org/doc/html/rfc2577) - https://datatracker.ietf.org/doc/html/rfc2577
### [Reference](https://datatracker.ietf.org/doc/html/rfc2640) - https://datatracker.ietf.org/doc/html/rfc2640
### [Reference](https://datatracker.ietf.org/doc/html/rfc3659) - https://datatracker.ietf.org/doc/html/rfc3659
### [Reference](https://datatracker.ietf.org/doc/html/rfc4217) - https://datatracker.ietf.org/doc/html/rfc4217
### [Reference](https://datatracker.ietf.org/doc/html/rfc5797) - https://datatracker.ietf.org/doc/html/rfc5797
### [Reference](https://datatracker.ietf.org/doc/html/rfc697) - https://datatracker.ietf.org/doc/html/rfc697
### [Reference](https://datatracker.ietf.org/doc/html/rfc7151) - https://datatracker.ietf.org/doc/html/rfc7151
### [Reference](https://datatracker.ietf.org/doc/html/rfc765) - https://datatracker.ietf.org/doc/html/rfc765
### [Reference](https://datatracker.ietf.org/doc/html/rfc913) - https://datatracker.ietf.org/doc/html/rfc913
### [Reference](https://datatracker.ietf.org/doc/html/rfc959) - https://datatracker.ietf.org/doc/html/rfc959
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=1574475) - https://bugzilla.mozilla.org/show_bug.cgi?id=1574475
### [Reference](https://support.mozilla.org/en-US/kb/Accessing%20FTP%20servers#w_ftp-servers-that-require-a-username-and-password) - https://support.mozilla.org/en-US/kb/Accessing%20FTP%20servers#w_ftp-servers-that-require-a-username-and-password
### [Reference](https://www.mozilla.org/en-US/firefox/88.0/releasenotes/) - https://www.mozilla.org/en-US/firefox/88.0/releasenotes/
### [Reference](https://www.ogf.org/documents/GFD.20.pdf) - https://www.ogf.org/documents/GFD.20.pdf
### [Reference](https://www.ogf.org/documents/GFD.47.pdf) - https://www.ogf.org/documents/GFD.47.pdf
### [Reference](https://www.wikidata.org/wiki/Q42283#identifiers) - https://www.wikidata.org/wiki/Q42283#identifiers
### [Reference](https://www.omgubuntu.co.uk/2021/01/linux-release-roundup-chrome-lightworks-more) - https://www.omgubuntu.co.uk/2021/01/linux-release-roundup-chrome-lightworks-more
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/8/84/Passive_FTP_Verbindung.svg) - https://upload.wikimedia.org/wikipedia/commons/8/84/Passive_FTP_Verbindung.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/df/Wikibooks-logo-en-noslogan.svg) - https://upload.wikimedia.org/wikipedia/commons/d/df/Wikibooks-logo-en-noslogan.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg