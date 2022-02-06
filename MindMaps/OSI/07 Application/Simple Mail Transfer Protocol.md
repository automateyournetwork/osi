# Simple Mail Transfer Protocol
## [URL](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) - https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol
## Catagories
### All articles with failed verification
### All articles with unsourced statements
### Articles with failed verification from January 2022
### Articles with short description
### Articles with unsourced statements from April 2021
### Articles with unsourced statements from March 2021
### Articles with unsourced statements from October 2019
### Internet mail protocols
### Short description matches Wikidata
### Use mdy dates from October 2013
### Webarchive template wayback links
### "The Simple Mail Transfer Protocol (SMTP) is an internet standard communication protocol for electronic mail transmission. Mail servers and other message transfer agents use SMTP to send and receive mail messages. User-level email clients typically use SMTP only for sending messages to a mail server for relaying, and typically submit outgoing email to the mail server on port 587 or 465 per RFC 8314. For retrieving messages, IMAP (which replaced the older POP3) is standard, but proprietary servers also often implement proprietary protocols, e.g., Exchange ActiveSync. 
### Since SMTP's introduction in 1981, it has been updated, modified and extended multiple times. The protocol version in common use today has extensible structure with various extensions for authentication, encryption, binary data transfer, and internationalized email addresses. SMTP servers commonly use the Transmission Control Protocol on port number 25 (for plaintext) and 587 (for encrypted communications).
## History 
## Predecessors to SMTP  
### Various forms of one-to-one electronic messaging were used in the 1960s. Users communicated using systems developed for specific mainframe computers. As more computers were interconnected, especially in the U.S. Government's ARPANET, standards were developed to permit exchange of messages between different operating systems. SMTP grew out of these standards developed during the 1970s. 
### SMTP traces its roots to two implementations described in 1971: the Mail Box Protocol, whose implementation has been disputed, but is discussed in RFC 196 and other RFCs, and the SNDMSG program, which, according to RFC 2235, Ray Tomlinson of BBN invented for TENEX computers to send mail messages across the ARPANET. Fewer than 50 hosts were connected to the ARPANET at this time.Further implementations include FTP Mail and Mail Protocol, both from 1973. Development work continued throughout the 1970s, until the ARPANET transitioned into the modern Internet around 1980.
## Original SMTP  
### In 1980, Jon Postel published RFC 772 which proposed the Mail Transfer Protocol as a replacement of the use of the File Transfer Protocol (FTP) for mail. RFC 780 of May 1981 removed all references to FTP and allocated port 57 for TCP and UDP, an allocation that has since been removed by IANA. In November 1981, Postel published RFC 788 \"Simple Mail Transfer Protocol\". 
### The SMTP standard was developed around the same time as Usenet, a one-to-many communication network with some similarities.SMTP became widely used in the early 1980s. At the time, it was a complement to the Unix to Unix Copy Program (UUCP), which was better suited for handling email transfers between machines that were intermittently connected. SMTP, on the other hand, works best when both the sending and receiving machines are connected to the network all the time. Both used a store and forward mechanism and are examples of push technology. Though Usenet's newsgroups were still propagated with UUCP between servers, UUCP as a mail transport has virtually disappeared along with the \"bang paths\" it used as message routing headers.Sendmail, released with 4.1cBSD in 1982, soon after RFC 788 was published in November 1981, was one of the first mail transfer agents to implement SMTP. Over time, as BSD Unix became the most popular operating system on the Internet, Sendmail became the most common MTA (mail transfer agent).The original SMTP protocol supported only unauthenticated unencrypted 7-bit ASCII text communications, susceptible to trivial man-in-the-middle attack, spoofing, and spamming, and requiring any binary data to be encoded to readable text before transmission. Due to absence of a proper authentication mechanism, by design every SMTP server was an open mail relay. The Internet Mail Consortium (IMC) reported that 55% of mail servers were open relays in 1998, but less than 1% in 2002. Because of spam concerns most email providers blocklist open relays, making original SMTP essentially impractical for general use on the Internet.
## Modern SMTP  
### In November 1995, RFC 1869 defined Extended Simple Mail Transfer Protocol (ESMTP), which established a general structure for all existing and future extensions which aimed to add-in the features missing from the original SMTP. ESMTP defines consistent and manageable means by which ESMTP clients and servers can be identified and servers can indicate supported extensions.  
### Message submission (RFC 2476) and SMTP-AUTH (RFC 2554) were introduced in 1998 and 1999, both describing new trends in email delivery. Originally, SMTP servers were typically internal to an organization, receiving mail for the organization from the outside, and relaying messages from the organization to the outside. But as time went on, SMTP servers (mail transfer agents), in practice, were expanding their roles to become message submission agents for Mail user agents, some of which were now relaying mail from the outside of an organization. (e.g. a company executive wishes to send email while on a trip using the corporate SMTP server.) This issue, a consequence of the rapid expansion and popularity of the World Wide Web, meant that SMTP had to include specific rules and methods for relaying mail and authenticating users to prevent abuses such as relaying of unsolicited email (spam). Work on message submission (RFC 2476) was originally started because popular mail servers would often rewrite mail in an attempt to fix problems in it, for example, adding a domain name to an unqualified address. This behavior is helpful when the message being fixed is an initial submission, but dangerous and harmful when the message originated elsewhere and is being relayed. Cleanly separating mail into submission and relay was seen as a way to permit and encourage rewriting submissions while prohibiting rewriting relay. As spam became more prevalent, it was also seen as a way to provide authorization for mail being sent out from an organization, as well as traceability. This separation of relay and submission quickly became a foundation for modern email security practices. 
### As this protocol started out purely ASCII text-based, it did not deal well with binary files, or characters in many non-English languages. Standards such as Multipurpose Internet Mail Extensions (MIME) were developed to encode binary files for transfer through SMTP. Mail transfer agents (MTAs) developed after Sendmail also tended to be implemented 8-bit-clean, so that the alternate \"just send eight\" strategy could be used to transmit arbitrary text data (in any 8-bit ASCII-like character encoding) via SMTP. Mojibake was still a problem due to differing character set mappings between vendors, although the email addresses themselves still allowed only ASCII. 8-bit-clean MTAs today tend to support the 8BITMIME extension, permitting some binary files to be transmitted almost as easily as plain text (limits on line length and permitted octet values still apply, so that MIME encoding is needed for most non-text data and some text formats). In 2012, the SMTPUTF8 extension was created to support UTF-8 text, allowing international content and addresses in non-Latin scripts like Cyrillic or Chinese. 
### Many people contributed to the core SMTP specifications, among them Jon Postel, Eric Allman, Dave Crocker, Ned Freed, Randall Gellens, John Klensin, and Keith Moore.
## Mail processing model  

### Email is submitted by a mail client (mail user agent, MUA) to a mail server (mail submission agent, MSA) using SMTP on TCP port 587. Most mailbox providers still allow submission on traditional port 25. The MSA delivers the mail to its mail transfer agent (mail transfer agent, MTA). Often, these two agents are instances of the same software launched with different options on the same machine. Local processing can be done either on a single machine, or split among multiple machines; mail agent processes on one machine can share files, but if processing is on multiple machines, they transfer messages between each other using SMTP, where each machine is configured to use the next machine as a smart host. Each process is an MTA (an SMTP server) in its own right. 
### The boundary MTA uses DNS to look up the MX (mail exchanger) record for the recipient's domain (the part of the email address on the right of @). The MX record contains the name of the target MTA. Based on the target host and other factors, the sending MTA selects a recipient server and connects to it to complete the mail exchange. 
### Message transfer can occur in a single connection between two MTAs, or in a series of hops through intermediary systems. A receiving SMTP server may be the ultimate destination, an intermediate \"relay\" (that is, it stores and forwards the message) or a \"gateway\" (that is, it may forward the message using some protocol other than SMTP). Per RFC 5321 section 2.1, each hop is a formal handoff of responsibility for the message, whereby the receiving server must either deliver the message or properly report the failure to do so. 
### Once the final hop accepts the incoming message, it hands it to a mail delivery agent (MDA) for local delivery. An MDA saves messages in the relevant mailbox format. As with sending, this reception can be done using one or multiple computers, but in the diagram above the MDA is depicted as one box near the mail exchanger box. An MDA may deliver messages directly to storage, or forward them over a network using SMTP or other protocol such as Local Mail Transfer Protocol (LMTP), a derivative of SMTP designed for this purpose. 
### Once delivered to the local mail server, the mail is stored for batch retrieval by authenticated mail clients (MUAs). Mail is retrieved by end-user applications, called email clients, using Internet Message Access Protocol (IMAP), a protocol that both facilitates access to mail and manages stored mail, or the Post Office Protocol (POP) which typically uses the traditional mbox mail file format or a proprietary system such as Microsoft Exchange/Outlook or Lotus Notes/Domino. Webmail clients may use either method, but the retrieval protocol is often not a formal standard. 
### SMTP defines message transport, not the message content. Thus, it defines the mail envelope and its parameters, such as the envelope sender, but not the header (except trace information) nor the body of the message itself. STD 10 and RFC 5321 define SMTP (the envelope), while STD 11 and RFC 5322 define the message (header and body), formally referred to as the Internet Message Format.
## Protocol overview  
### SMTP is a connection-oriented, text-based protocol in which a mail sender communicates with a mail receiver by issuing command strings and supplying necessary data over a reliable ordered data stream channel, typically a Transmission Control Protocol (TCP) connection. An SMTP session consists of commands originated by an SMTP client (the initiating agent, sender, or transmitter) and corresponding responses from the SMTP server (the listening agent, or receiver) so that the session is opened, and session parameters are exchanged. A session may include zero or more SMTP transactions. An SMTP transaction consists of three command/reply sequences: 

### MAIL command, to establish the return address, also called return-path, reverse-path, bounce address, mfrom, or envelope sender. 
### RCPT command, to establish a recipient of the message. This command can be issued multiple times, one for each recipient. These addresses are also part of the envelope. 
### DATA to signal the beginning of the message text; the content of the message, as opposed to its envelope. It consists of a message header and a message body separated by an empty line. DATA is actually a group of commands, and the server replies twice: once to the DATA command itself, to acknowledge that it is ready to receive the text, and the second time after the end-of-data sequence, to either accept or reject the entire message.Besides the intermediate reply for DATA, each server's reply can be either positive (2xx reply codes) or negative. Negative replies can be permanent (5xx codes) or transient (4xx codes). A reject is a permanent failure and the client should send a bounce message to the server it received it from. A drop is a positive response followed by message discard rather than delivery. 
### The initiating host, the SMTP client, can be either an end-user's email client, functionally identified as a mail user agent (MUA), or a relay server's mail transfer agent (MTA), that is an SMTP server acting as an SMTP client, in the relevant session, in order to relay mail. Fully capable SMTP servers maintain queues of messages for retrying message transmissions that resulted in transient failures. 
### A MUA knows the outgoing mail SMTP server from its configuration. A relay server typically determines which server to connect to by looking up the MX (Mail eXchange) DNS resource record for each recipient's domain name. If no MX record is found, a conformant relaying server (not all are) instead looks up the A record. Relay servers can also be configured to use a smart host. A relay server initiates a TCP connection to the server on the \"well-known port\" for SMTP: port 25, or for connecting to an MSA, port 587. The main difference between an MTA and an MSA is that connecting to an MSA requires SMTP Authentication.
## SMTP vs mail retrieval  
### SMTP is a delivery protocol only. In normal use, mail is \"pushed\" to a destination mail server (or next-hop mail server) as it arrives. Mail is routed based on the destination server, not the individual user(s) to which it is addressed. Other protocols, such as the Post Office Protocol (POP) and the Internet Message Access Protocol (IMAP) are specifically designed for use by individual users retrieving messages and managing mail boxes. To permit an intermittently-connected mail server to pull messages from a remote server on demand, SMTP has a feature to initiate mail queue processing on a remote server (see Remote Message Queue Starting below). POP and IMAP are unsuitable protocols for relaying mail by intermittently-connected machines; they are designed to operate after final delivery, when information critical to the correct operation of mail relay (the \"mail envelope\") has been removed.
## Remote Message Queue Starting  
### Remote Message Queue Starting enables a remote host to start processing of the mail queue on a server so it may receive messages destined to it by sending a corresponding command. The original TURN command was deemed insecure and was extended in RFC 1985 with the ETRN command which operates more securely using an authentication method based on Domain Name System information.
## Outgoing mail SMTP server  
### An email client needs to know the IP address of its initial SMTP server and this has to be given as part of its configuration (usually given as a DNS name). This server will deliver outgoing messages on behalf of the user.
## Outgoing mail server access restrictions  
### Server administrators need to impose some control on which clients can use the server. This enables them to deal with abuse, for example spam. Two solutions have been in common use: 

### In the past, many systems imposed usage restrictions by the location of the client, only permitting usage by clients whose IP address is one that the server administrators control. Usage from any other client IP address is disallowed. 
### Modern SMTP servers typically offer an alternative system that requires authentication of clients by credentials before allowing access.
## Restricting access by location  
### Under this system, an ISP's SMTP server will not allow access by users who are outside the ISP's network. More precisely, the server may only allow access to users with an IP address provided by the ISP, which is equivalent to requiring that they are connected to the Internet using that same ISP. A mobile user may often be on a network other than that of their normal ISP, and will then find that sending email fails because the configured SMTP server choice is no longer accessible. 
### This system has several variations. For example, an organisation's SMTP server may only provide service to users on the same network, enforcing this by firewalling to block access by users on the wider Internet. Or the server may perform range checks on the client's IP address. These methods were typically used by corporations and institutions such as universities which provided an SMTP server for outbound mail only for use internally within the organisation. However, most of these bodies now use client authentication methods, as described below. 
### Where a user is mobile, and may use different ISPs to connect to the internet, this kind of usage restriction is onerous, and altering the configured outbound email SMTP server address is impractical. It is highly desirable to be able to use email client configuration information that does not need to change.
## Client authentication  
### Modern SMTP servers typically require authentication of clients by credentials before allowing access, rather than restricting access by location as described earlier. This more flexible system is friendly to mobile users and allows them to have a fixed choice of configured outbound SMTP server. SMTP Authentication, often abbreviated SMTP AUTH, is an extension of the SMTP in order to log in using an authentication mechanism.
## Ports  
### Communication between mail servers generally uses the standard TCP port 25 designated for SMTP. 
### Mail clients however generally don't use this, instead using specific \"submission\" ports. Mail services generally accept email submission from clients on one of: 

### 587 (Submission), as formalized in RFC 6409 (previously RFC 2476) 
### 465 This port was deprecated after RFC 2487, until the issue of RFC 8314.Port 2525 and others may be used by some individual providers, but have never been officially supported. 
### Many Internet service providers now block all outgoing port 25 traffic from their customers. Mainly as an anti-spam measure, but also to cure for the higher cost they have when leaving it open, perhaps by charging more from the few customers that require it open.
## SMTP transport example  
### A typical example of sending a message via SMTP to two mailboxes (alice and theboss) located in the same mail domain (example.com) is reproduced in the following session exchange. (In this example, the conversation parts are prefixed with S: and C:, for server and client, respectively; these labels are not part of the exchange.) 
### After the message sender (SMTP client) establishes a reliable communications channel to the message receiver (SMTP server), the session is opened with a greeting by the server, usually containing its fully qualified domain name (FQDN), in this case smtp.example.com. The client initiates its dialog by responding with a HELO command identifying itself in the command's parameter with its FQDN (or an address literal if none is available). 
### S: 220 smtp.example.com ESMTP Postfix 
### C: HELO relay.example.org 
### S: 250 Hello relay.example.org, I am glad to meet you 
### C: MAIL FROM:<bob@example.org> 
### S: 250 Ok 
### C: RCPT TO:<alice@example.com> 
### S: 250 Ok 
### C: RCPT TO:<theboss@example.com> 
### S: 250 Ok 
### C: DATA 
### S: 354 End data with <CR><LF>.<CR><LF> 
### C: From: \"Bob Example\" <bob@example.org> 
### C: To: \"Alice Example\" <alice@example.com> 
### C: Cc: theboss@example.com 
### C: Date: Tue, 15 Jan 2008 16:02:43 -0500 
### C: Subject: Test message 
### C: 
### C: Hello Alice. 
### C: This is a test message with 5 header fields and 4 lines in the message body. 
### C: Your friend, 
### C: Bob 
### C: . 
### S: 250 Ok: queued as 12345 
### C: QUIT 
### S: 221 Bye 
### {The server closes the connection} 

### The client notifies the receiver of the originating email address of the message in a MAIL FROM command. This is also the return or bounce address in case the message cannot be delivered. In this example the email message is sent to two mailboxes on the same SMTP server: one for each recipient listed in the To: and Cc: header fields. The corresponding SMTP command is RCPT TO. Each successful reception and execution of a command is acknowledged by the server with a result code and response message (e.g., 250 Ok). 
### The transmission of the body of the mail message is initiated with a DATA command after which it is transmitted verbatim line by line and is terminated with an end-of-data sequence. This sequence consists of a new-line (<CR><LF>), a single full stop (.), followed by another new-line (<CR><LF>). Since a message body can contain a line with just a period as part of the text, the client sends two periods every time a line starts with a period; correspondingly, the server replaces every sequence of two periods at the beginning of a line with a single one. Such escaping method is called dot-stuffing. 
### The server's positive reply to the end-of-data, as exemplified, implies that the server has taken the responsibility of delivering the message. A message can be doubled if there is a communication failure at this time, e.g. due to a power shortage: Until the sender has received that 250 Ok reply, it must assume the message was not delivered. On the other hand, after the receiver has decided to accept the message, it must assume the message has been delivered to it. Thus, during this time span, both agents have active copies of the message that they will try to deliver. The probability that a communication failure occurs exactly at this step is directly proportional to the amount of filtering that the server performs on the message body, most often for anti-spam purposes. The limiting timeout is specified to be 10 minutes.The QUIT command ends the session. If the email has other recipients located elsewhere, the client would QUIT and connect to an appropriate SMTP server for subsequent recipients after the current destination(s) had been queued. The information that the client sends in the HELO and MAIL FROM commands are added (not seen in example code) as additional header fields to the message by the receiving server. It adds a Received and Return-Path header field, respectively. 
### Some clients are implemented to close the connection after the message is accepted (250 Ok: queued as 12345), so the last two lines may actually be omitted. This causes an error on the server when trying to send the 221 Bye reply.
## SMTP Extensions 
## Extension discovery mechanism  
### Clients learn a server's supported options by using the EHLO greeting, as exemplified below, instead of the original HELO. Clients fall back to HELO only if the server does not support EHLO greeting.Modern clients may use the ESMTP extension keyword SIZE to query the server for the maximum message size that will be accepted. Older clients and servers may try to transfer excessively sized messages that will be rejected after consuming network resources, including connect time to network links that is paid by the minute.Users can manually determine in advance the maximum size accepted by ESMTP servers. The client replaces the HELO command with the EHLO command. 

### S: 220 smtp2.example.com ESMTP Postfix 
### C: EHLO bob.example.org 
### S: 250-smtp2.example.com Hello bob.example.org [192.0.2.201] 
### S: 250-SIZE 14680064 
### S: 250-PIPELINING 
### S: 250 HELP 

### Thus smtp2.example.com declares that it can accept a fixed maximum message size no larger than 14,680,064 octets (8-bit bytes). 
### In the simplest case, an ESMTP server declares a maximum SIZE immediately after receiving an EHLO. According to RFC 1870, however, the numeric parameter to the SIZE extension in the EHLO response is optional. Clients may instead, when issuing a MAIL FROM command, include a numeric estimate of the size of the message they are transferring, so that the server can refuse receipt of overly-large messages.
## Binary data transfer  
### Original SMTP supports only a single body of ASCII text, therefore any binary data needs to be encoded as text into that body of the message before transfer, and then decoded by the recipient. Binary-to-text encodings, such as uuencode and BinHex were typically used. 
### The 8BITMIME command was developed to address this. It was standardized in 1994 as RFC 1652 It facilitates the transparent exchange of e-mail messages containing octets outside the seven-bit ASCII character set by encoding them as MIME content parts, typically encoded with Base64.
## Mail delivery mechanism extensions 
## On-Demand Mail Relay  

### On-Demand Mail Relay (ODMR) is an SMTP extension standardized in RFC 2645 that allows an intermittently-connected SMTP server to receive email queued for it when it is connected.
## Internationalization extension  

### Original SMTP supports email addresses composed of ASCII characters only, which is inconvenient for users whose native script is not Latin based, or who use diacritic not in the ASCII character set. This limitation was alleviated via extensions enabling UTF-8 in address names. RFC 5336 introduced experimental UTF8SMTP command and later was superseded by RFC 6531 that introduced SMTPUTF8 command. These extensions provide support for multi-byte and non-ASCII characters in email addresses, such as those with diacritics and other language characters such as Greek and Chinese.Current support is limited, but there is strong interest in broad adoption of RFC 6531 and the related RFCs in countries like China that have a large user base where Latin (ASCII) is a foreign script.
## Extensions  
### Like SMTP, ESMTP is a protocol used to transport Internet mail. It is used as both an inter-server transport protocol and (with restricted behavior enforced) a mail submission protocol. 
### The main identification feature for ESMTP clients is to open a transmission with the command EHLO (Extended HELLO), rather than HELO (Hello, the original RFC 821 standard). A server will respond with success (code 250), failure (code 550) or error (code 500, 501, 502, 504, or 421), depending on its configuration. An ESMTP server returns the code 250 OK in a multi-line reply with its domain and a list of keywords to indicate supported extensions. A RFC 821 compliant server returns error code 500, allowing ESMTP clients to try either HELO or QUIT. 
### Each service extension is defined in an approved format in subsequent RFCs and registered with the Internet Assigned Numbers Authority (IANA). The first definitions were the RFC 821 optional services: SEND, SOML (Send or Mail), SAML (Send and Mail), EXPN, HELP, and TURN. The format of additional SMTP verbs was set and for new parameters in MAIL and RCPT. 
### Some relatively common keywords (not all of them corresponding to commands) used today are: 

### 8BITMIME \u2013 8 bit data transmission, RFC 6152 
### ATRN \u2013 Authenticated TURN for On-Demand Mail Relay, RFC 2645 
### AUTH \u2013 Authenticated SMTP, RFC 4954 
### CHUNKING \u2013 Chunking, RFC 3030 
### DSN \u2013 Delivery status notification, RFC 3461 (See Variable envelope return path) 
### ETRN \u2013 Extended version of remote message queue starting command TURN, RFC 1985 
### HELP \u2013 Supply helpful information, RFC 821 
### PIPELINING \u2013 Command pipelining, RFC 2920 
### SIZE \u2013 Message size declaration, RFC 1870 
### STARTTLS \u2013 Transport Layer Security, RFC 3207 (2002) 
### SMTPUTF8 \u2013 Allow UTF-8 encoding in mailbox names and header fields, RFC 6531 
### UTF8SMTP \u2013 Allow UTF-8 encoding in mailbox names and header fields, RFC 5336 (deprecated)The ESMTP format was restated in RFC 2821 (superseding RFC 821) and updated to the latest definition in RFC 5321 in 2008. Support for the EHLO command in servers became mandatory, and HELO designated a required fallback. 
### Non-standard, unregistered, service extensions can be used by bilateral agreement, these services are indicated by an EHLO message keyword starting with \"X\", and with any additional parameters or verbs similarly marked. 
### SMTP commands are case-insensitive. They are presented here in capitalized form for emphasis only. An SMTP server that requires a specific capitalization method is a violation of the standard.
## 8BITMIME  
### At least the following servers advertise the 8BITMIME extension: 

### Apache James (since 2.3.0a1) 
### Citadel (since 7.30) 
### Courier Mail Server 
### Gmail 
### IceWarp 
### IIS SMTP Service 
### Kerio Connect 
### Lotus Domino 
### Microsoft Exchange Server (as of Exchange Server 2000) 
### Novell GroupWise 
### OpenSMTPD 
### Oracle Communications Messaging Server 
### Postfix 
### Sendmail (since 6.57)The following servers can be configured to advertise 8BITMIME, but do not perform conversion of 8-bit data to 7-bit when connecting to non-8BITMIME relays: 

### Exim and qmail do not translate eight-bit messages to seven-bit when making an attempt to relay 8-bit data to non-8BITMIME peers, as is required by the RFC. This does not cause problems in practice, since virtually all modern mail relays are 8-bit clean. 
### Microsoft Exchange Server 2003 advertises 8BITMIME by default, but relaying to a non-8BITMIME peer results in a bounce. This is allowed by RFC 6152 section 3.
## SMTP-AUTH  

### The SMTP-AUTH extension provides an access control mechanism. It consists of an authentication step through which the client effectively logs into the mail server during the process of sending mail. Servers that support SMTP-AUTH can usually be configured to require clients to use this extension, ensuring the true identity of the sender is known. The SMTP-AUTH extension is defined in RFC 4954. 
### SMTP-AUTH can be used to allow legitimate users to relay mail while denying relay service to unauthorized users, such as spammers. It does not necessarily guarantee the authenticity of either the SMTP envelope sender or the RFC 2822 \"From:\" header. For example, spoofing, in which one sender masquerades as someone else, is still possible with SMTP-AUTH unless the server is configured to limit message from-addresses to addresses this AUTHed user is authorized for. 
### The SMTP-AUTH extension also allows one mail server to indicate to another that the sender has been authenticated when relaying mail. In general this requires the recipient server to trust the sending server, meaning that this aspect of SMTP-AUTH is rarely used on the Internet.
## SMTPUTF8  
### Supporting servers include: 

### Postfix (version 3.0 and later) 
### Momentum (versions 4.1 and 3.6.5, and later) 
### Sendmail (under development) 
### Exim (experimental as of the 4.86 release) 
### CommuniGate Pro as of version 6.2.2 
### Courier-MTA as of version 1.0 
### Halon as of version 4.0 
### Microsoft Exchange Server as of protocol revision 14.0 
### Haraka and other servers. 
### Oracle Communications Messaging Server as of release 8.0.2.
## Security extensions  
### Mail delivery can occur both over plain text and encrypted connections, however the communicating parties might not know in advance of other party's ability to use secure channel.
## STARTTLS or \"Opportunistic TLS\"  

### The STARTTLS extensions enables supporting SMTP servers to notify connecting clients that it supports TLS encrypted communication and offers the opportunity for clients to upgrade their connection by sending the STARTTLS command. Servers supporting the extension do not inherently gain any security benefits from its implementation on its own, as upgrading to a TLS encrypted session is dependent on the connecting client deciding to exercise this option, hence the term opportunistic TLS. 
### STARTTLS is effective only against passive observation attacks, since the STARTTLS negotiation happens in plain text and an active attacker can trivially remove STARTTLS commands. This type of man-in-the-middle attack is sometimes referred to as STRIPTLS, where the encryption negotiation information sent from one end never reaches the other. In this scenario both parties take the invalid or unexpected responses as indication that the other does not properly support STARTTLS, defaulting to traditional plain-text mail transfer. Note that STARTTLS is also defined for IMAP and POP3 in other RFCs, but these protocols serve different purposes: SMTP is used for communication between message transfer agents, while IMAP and POP3 are for end clients and message transfer agents. 
### In 2014 the Electronic Frontier Foundation began \"STARTTLS Everywhere\" project that, similarly to \"HTTPS Everywhere\" list, allowed relying parties to discover others supporting secure communication without prior communication. The project stopped accepting submissions on 29 April 2021, and EFF recommended switching to DANE and MTA-STS for discovering information on peers' TLS support.RFC 8314 officially declared plain text obsolete and recommend always using TLS, adding ports with implicit TLS.
## SMTP MTA Strict Transport Security  
### A newer 2018 RFC 8461 called \"SMTP MTA Strict Transport Security (MTA-STS)\" aims to address the problem of active adversary by defining a protocol for mail servers to declare their ability to use secure channels in specific files on the server and specific DNS TXT records. The relying party would regularly check existence of such record, and cache it for the amount of time specified in the record and never communicate over insecure channels until record expires. Note that MTA-STS records apply only to SMTP traffic between mail servers while communications between a user's client and the mail server are protected by Transport Layer Security with SMTP/MSA, IMAP, POP3, or HTTPS in combination with an organizational or technical policy. Essentially, MTA-STS is a means to extend such a policy to third parties. 
### In April 2019 Google Mail announced support for MTA-STS.
## SMTP TLS Reporting  
### A number of protocols allows secure delivery of messages, but they can fail due to misconfigurations or deliberate active interference, leading to undelivered messages or delivery over unencrypted or unauthenticated channels. RFC 8460 \"SMTP TLS Reporting\" describes a reporting mechanism and format for sharing statistics and specific information about potential failures with recipient domains. Recipient domains can then use this information to both detect potential attacks and diagnose unintentional misconfigurations. 
### In April 2019 Google Mail announced support for SMTP TLS Reporting.
## Spoofing and spamming  

### The original design of SMTP had no facility to authenticate senders, or check that servers were authorized to send on their behalf, with the result that email spoofing is possible, and commonly used in email spam and phishing. 
### Occasional proposals are made to modify SMTP extensively or replace it completely. One example of this is Internet Mail 2000, but neither it, nor any other has made much headway in the face of the network effect of the huge installed base of classic SMTP.  
### Instead, mail servers now use a range of techniques, such as stricter enforcement of standards such as RFC 5322, DomainKeys Identified Mail, Sender Policy Framework and DMARC, DNSBLs and greylisting to reject or quarantine suspicious emails.
## Implementations  
### There is also SMTP proxy implementation as for example nginx.
## Related requests for comments  
### RFC 1123 \u2013 Requirements for Internet Hosts\u2014Application and Support (STD 3) 
### RFC 1870 \u2013 SMTP Service Extension for Message Size Declaration (\u043ebsoletes: RFC 1653) 
### RFC 2505 \u2013 Anti-Spam Recommendations for SMTP MTAs (BCP 30) 
### RFC 2821 \u2013 Simple Mail Transfer Protocol 
### RFC 2920 \u2013 SMTP Service Extension for Command Pipelining (STD 60) 
### RFC 3030 \u2013 SMTP Service Extensions for Transmission of Large and Binary MIME Messages 
### RFC 3207 \u2013 SMTP Service Extension for Secure SMTP over Transport Layer Security (obsoletes RFC 2487) 
### RFC 3461 \u2013 SMTP Service Extension for Delivery Status Notifications (obsoletes RFC 1891) 
### RFC 3463 \u2013 Enhanced Status Codes for SMTP (obsoletes RFC 1893, updated by RFC 5248) 
### RFC 3464 \u2013 An Extensible Message Format for Delivery Status Notifications (obsoletes RFC 1894) 
### RFC 3798 \u2013 Message Disposition Notification (updates RFC 3461) 
### RFC 3834 \u2013 Recommendations for Automatic Responses to Electronic Mail 
### RFC 3974 \u2013 SMTP Operational Experience in Mixed IPv4/v6 Environments 
### RFC 4952 \u2013 Overview and Framework for Internationalized Email (updated by RFC 5336) 
### RFC 4954 \u2013 SMTP Service Extension for Authentication (obsoletes RFC 2554, updates RFC 3463, updated by RFC 5248) 
### RFC 5068 \u2013 Email Submission Operations: Access and Accountability Requirements (BCP 134) 
### RFC 5248 \u2013 A Registry for SMTP Enhanced Mail System Status Codes (BCP 138) (updates RFC 3463) 
### RFC 5321 \u2013 The Simple Mail Transfer Protocol (obsoletes RFC 821 aka STD 10, RFC 974, RFC 1869, RFC 2821, updates RFC 1123) 
### RFC 5322 \u2013 Internet Message Format (obsoletes RFC 822 aka STD 11, and RFC 2822) 
### RFC 5504 \u2013 Downgrading Mechanism for Email Address Internationalization 
### RFC 6409 \u2013 Message Submission for Mail (STD 72) (obsoletes RFC 4409, RFC 2476) 
### RFC 6522 \u2013 The Multipart/Report Content Type for the Reporting of Mail System Administrative Messages (obsoletes RFC 3462, and in turn RFC 1892) 
### RFC 6531 \u2013 SMTP Extension for Internationalized Email Addresses (updates RFC 2821, RFC 2822, RFC 4952, and RFC 5336) 
### RFC 8314 \u2013 Cleartext Considered Obsolete: Use of Transport Layer Security (TLS) for Email Submission and Access
## See also  
### Bounce address 
### CRAM-MD5 (a SASL mechanism for ESMTPA) RFC 2195 
### Email 
### Email encryption 
### DKIM 
### Ident 
### List of mail server software 
### List of SMTP server return codes 
### POP before SMTP / SMTP after POP 
### Internet Message Access Protocol Binary Content Extension RFC 3516 
### Sender Policy Framework (SPF) 
### Simple Authentication and Security Layer (SASL) RFC 4422 
### SMTP Authentication 
### Variable envelope return path 
### Comparison of email clients for information about SMTP support
## Notes 
## References  
### Hughes, L (1998). Internet E-mail: Protocols, Standards and Implementation. Artech House Publishers. ISBN 978-0-89006-939-4. 
### Hunt, C (2003). sendmail Cookbook. O'Reilly Media. ISBN 978-0-596-00471-2. 
### Johnson, K (2000). Internet Email Protocols: A Developer's Guide. Addison-Wesley Professional. ISBN 978-0-201-43288-6. 
### Loshin, P (1999). Essential Email Standards: RFCs and Protocols Made Practical. John Wiley & Sons. ISBN 978-0-471-34597-8. 
### Rhoton, J (1999). Programmer's Guide to Internet Mail: SMTP, POP, IMAP, and LDAP. Elsevier. ISBN 978-1-55558-212-8. 
### Wood, D (1999). Programming Internet Mail. O'Reilly. ISBN 978-1-56592-479-6.
## External links  
### RFC 1869 SMTP Service Extensions 
### RFC 5321 Simple Mail Transfer Protocol 
### RFC 4954 SMTP Service Extension for Authentication (obsoletes RFC 2554) 
### RFC 3848 SMTP and LMTP Transmission Types Registration (with ESMTPA) 
### RFC 6409 Message Submission for Mail (obsoletes RFC 4409, which obsoletes RFC 2476)"
## References
### [Reference](http://www.ir.bbn.com/~craig/email.pdf) - http://www.ir.bbn.com/~craig/email.pdf
### [Reference](http://openmap.bbn.com/~tomlinso/ray/firstemailframe.html) - http://openmap.bbn.com/~tomlinso/ray/firstemailframe.html
### [Reference](http://openmap.bbn.com/~tomlinso/ray/ka10.html) - http://openmap.bbn.com/~tomlinso/ray/ka10.html
### [Reference](http://www.opost.com/dlm/tenex/) - http://www.opost.com/dlm/tenex/
### [Reference](http://www.pcworld.com/article/116843/article.html) - http://www.pcworld.com/article/116843/article.html
### [Reference](http://www.prnewswire.com/news-releases/message-systems-introduces-latest-version-of-momentum-with-new-api-driven-capabilities-277568381.html) - http://www.prnewswire.com/news-releases/message-systems-introduces-latest-version-of-momentum-with-new-api-driven-capabilities-277568381.html
### [Reference](http://kb.iu.edu/data/aivh.html) - http://kb.iu.edu/data/aivh.html
### [Reference](http://james.apache.org/server/2.3.0/changelog.html) - http://james.apache.org/server/2.3.0/changelog.html
### [Reference](http://doi.org/10.1109%2FMAHC.2008.32) - http://doi.org/10.1109%2FMAHC.2008.32
### [Reference](http://doi.org/10.17487%2FRFC1869) - http://doi.org/10.17487%2FRFC1869
### [Reference](http://tools.ietf.org/html/draft-barber-uucp-project-conclusion-05) - http://tools.ietf.org/html/draft-barber-uucp-project-conclusion-05
### [Reference](http://tools.ietf.org/html/rfc5321#section-4.5.3.2.6) - http://tools.ietf.org/html/rfc5321#section-4.5.3.2.6
### [Reference](http://tools.ietf.org/html/rfc6152#section-3) - http://tools.ietf.org/html/rfc6152#section-3
### [Reference](http://www.ietf.org/mail-archive/web/ima/current/msg05395.html) - http://www.ietf.org/mail-archive/web/ima/current/msg05395.html
### [Reference](http://www.imc.org/imcr-006.html) - http://www.imc.org/imcr-006.html
### [Reference](http://www.imc.org/ube-relay.html) - http://www.imc.org/ube-relay.html
### [Reference](http://www.multicians.org/thvv/mail-history.html) - http://www.multicians.org/thvv/mail-history.html
### [Reference](http://www.postfix.org/SMTPUTF8_README.html) - http://www.postfix.org/SMTPUTF8_README.html
### [Reference](http://tldp.org/HOWTO/Usenet-News-HOWTO/x64.html) - http://tldp.org/HOWTO/Usenet-News-HOWTO/x64.html
### [Reference](http://cr.yp.to/smtp/8bitmime.html) - http://cr.yp.to/smtp/8bitmime.html
### [Reference](http://cr.yp.to/smtp/mail.html) - http://cr.yp.to/smtp/mail.html
### [Reference](https://communigate.com/Communigatepro/History62.html#6.2.2) - https://communigate.com/Communigatepro/History62.html#6.2.2
### [Reference](https://github.com/halon/changelog) - https://github.com/halon/changelog
### [Reference](https://support.google.com/mail/?p=RfcMessageNonCompliant) - https://support.google.com/mail/?p=RfcMessageNonCompliant
### [Reference](https://www.hardenize.com/blog/mta-sts) - https://www.hardenize.com/blog/mta-sts
### [Reference](https://answers.microsoft.com/en-us/outlook_com/forum/oemail-osend/why-are-the-emails-sent-to-microsoft-account/b64e3e4a-0d93-40c8-8e28-4be849012f9c) - https://answers.microsoft.com/en-us/outlook_com/forum/oemail-osend/why-are-the-emails-sent-to-microsoft-account/b64e3e4a-0d93-40c8-8e28-4be849012f9c
### [Reference](https://answers.microsoft.com/en-us/outlook_com/forum/oemail-ocompose/message-could-not-be-delivered-please-ensure-the/87a52762-7d08-467e-85a2-120721c2dd8e?auth=1) - https://answers.microsoft.com/en-us/outlook_com/forum/oemail-ocompose/message-could-not-be-delivered-please-ensure-the/87a52762-7d08-467e-85a2-120721c2dd8e?auth=1
### [Reference](https://docs.nginx.com/nginx/admin-guide/mail-proxy/mail-proxy/) - https://docs.nginx.com/nginx/admin-guide/mail-proxy/mail-proxy/
### [Reference](https://docs.oracle.com/communications/E72263_01/doc.802/e72267/msvrn.htm#BAJGIBHB) - https://docs.oracle.com/communications/E72263_01/doc.802/e72267/msvrn.htm#BAJGIBHB
### [Reference](https://www.prnewswire.com/news-releases/message-systems-introduces-latest-version-of-momentum-with-new-api-driven-capabilities-277568381.html) - https://www.prnewswire.com/news-releases/message-systems-introduces-latest-version-of-momentum-with-new-api-driven-capabilities-277568381.html
### [Reference](https://www.zdnet.com/article/gmail-becomes-first-major-email-provider-to-support-mta-sts-and-tls-reporting/) - https://www.zdnet.com/article/gmail-becomes-first-major-email-provider-to-support-mta-sts-and-tls-reporting/
### [Reference](https://sourceforge.net/p/courier/mailman/message/36417878/) - https://sourceforge.net/p/courier/mailman/message/36417878/
### [Reference](https://interoperability.blob.core.windows.net/files/MS-OXSMTP/%5BMS-OXSMTP%5D-180724.docx) - https://interoperability.blob.core.windows.net/files/MS-OXSMTP/%5BMS-OXSMTP%5D-180724.docx
### [Reference](https://archive.org/details/livesofcaptivere00petz) - https://archive.org/details/livesofcaptivere00petz
### [Reference](https://web.archive.org/web/20070118121843/http://www.imc.org/ube-relay.html) - https://web.archive.org/web/20070118121843/http://www.imc.org/ube-relay.html
### [Reference](https://web.archive.org/web/20070617083024/http://kb.iu.edu/data/aivh.html) - https://web.archive.org/web/20070617083024/http://kb.iu.edu/data/aivh.html
### [Reference](https://web.archive.org/web/20071118204016/http://www.opost.com/dlm/tenex/) - https://web.archive.org/web/20071118204016/http://www.opost.com/dlm/tenex/
### [Reference](https://web.archive.org/web/20110512165437/http://www.ir.bbn.com/~craig/email.pdf) - https://web.archive.org/web/20110512165437/http://www.ir.bbn.com/~craig/email.pdf
### [Reference](https://docs.freebsd.org/44doc/smm/09.sendmail/paper.pdf) - https://docs.freebsd.org/44doc/smm/09.sendmail/paper.pdf
### [Reference](https://www.iana.org/assignments/mail-parameters/mail-parameters.txt) - https://www.iana.org/assignments/mail-parameters/mail-parameters.txt
### [Reference](https://datatracker.ietf.org/doc/html/rfc1047) - https://datatracker.ietf.org/doc/html/rfc1047
### [Reference](https://datatracker.ietf.org/doc/html/rfc1123) - https://datatracker.ietf.org/doc/html/rfc1123
### [Reference](https://datatracker.ietf.org/doc/html/rfc1652) - https://datatracker.ietf.org/doc/html/rfc1652
### [Reference](https://datatracker.ietf.org/doc/html/rfc1653) - https://datatracker.ietf.org/doc/html/rfc1653
### [Reference](https://datatracker.ietf.org/doc/html/rfc1869) - https://datatracker.ietf.org/doc/html/rfc1869
### [Reference](https://datatracker.ietf.org/doc/html/rfc1870) - https://datatracker.ietf.org/doc/html/rfc1870
### [Reference](https://datatracker.ietf.org/doc/html/rfc1891) - https://datatracker.ietf.org/doc/html/rfc1891
### [Reference](https://datatracker.ietf.org/doc/html/rfc1892) - https://datatracker.ietf.org/doc/html/rfc1892
### [Reference](https://datatracker.ietf.org/doc/html/rfc1893) - https://datatracker.ietf.org/doc/html/rfc1893
### [Reference](https://datatracker.ietf.org/doc/html/rfc1894) - https://datatracker.ietf.org/doc/html/rfc1894
### [Reference](https://datatracker.ietf.org/doc/html/rfc196) - https://datatracker.ietf.org/doc/html/rfc196
### [Reference](https://datatracker.ietf.org/doc/html/rfc1985) - https://datatracker.ietf.org/doc/html/rfc1985
### [Reference](https://datatracker.ietf.org/doc/html/rfc2195) - https://datatracker.ietf.org/doc/html/rfc2195
### [Reference](https://datatracker.ietf.org/doc/html/rfc2235) - https://datatracker.ietf.org/doc/html/rfc2235
### [Reference](https://datatracker.ietf.org/doc/html/rfc2476) - https://datatracker.ietf.org/doc/html/rfc2476
### [Reference](https://datatracker.ietf.org/doc/html/rfc2487) - https://datatracker.ietf.org/doc/html/rfc2487
### [Reference](https://datatracker.ietf.org/doc/html/rfc2505) - https://datatracker.ietf.org/doc/html/rfc2505
### [Reference](https://datatracker.ietf.org/doc/html/rfc2554) - https://datatracker.ietf.org/doc/html/rfc2554
### [Reference](https://datatracker.ietf.org/doc/html/rfc2645) - https://datatracker.ietf.org/doc/html/rfc2645
### [Reference](https://datatracker.ietf.org/doc/html/rfc2821) - https://datatracker.ietf.org/doc/html/rfc2821
### [Reference](https://datatracker.ietf.org/doc/html/rfc2822) - https://datatracker.ietf.org/doc/html/rfc2822
### [Reference](https://datatracker.ietf.org/doc/html/rfc2920) - https://datatracker.ietf.org/doc/html/rfc2920
### [Reference](https://datatracker.ietf.org/doc/html/rfc3030) - https://datatracker.ietf.org/doc/html/rfc3030
### [Reference](https://datatracker.ietf.org/doc/html/rfc3207) - https://datatracker.ietf.org/doc/html/rfc3207
### [Reference](https://datatracker.ietf.org/doc/html/rfc3461) - https://datatracker.ietf.org/doc/html/rfc3461
### [Reference](https://datatracker.ietf.org/doc/html/rfc3462) - https://datatracker.ietf.org/doc/html/rfc3462
### [Reference](https://datatracker.ietf.org/doc/html/rfc3463) - https://datatracker.ietf.org/doc/html/rfc3463
### [Reference](https://datatracker.ietf.org/doc/html/rfc3464) - https://datatracker.ietf.org/doc/html/rfc3464
### [Reference](https://datatracker.ietf.org/doc/html/rfc3516) - https://datatracker.ietf.org/doc/html/rfc3516
### [Reference](https://datatracker.ietf.org/doc/html/rfc3798) - https://datatracker.ietf.org/doc/html/rfc3798
### [Reference](https://datatracker.ietf.org/doc/html/rfc3834) - https://datatracker.ietf.org/doc/html/rfc3834
### [Reference](https://datatracker.ietf.org/doc/html/rfc3848) - https://datatracker.ietf.org/doc/html/rfc3848
### [Reference](https://datatracker.ietf.org/doc/html/rfc3974) - https://datatracker.ietf.org/doc/html/rfc3974
### [Reference](https://datatracker.ietf.org/doc/html/rfc4409) - https://datatracker.ietf.org/doc/html/rfc4409
### [Reference](https://datatracker.ietf.org/doc/html/rfc4422) - https://datatracker.ietf.org/doc/html/rfc4422
### [Reference](https://datatracker.ietf.org/doc/html/rfc469) - https://datatracker.ietf.org/doc/html/rfc469
### [Reference](https://datatracker.ietf.org/doc/html/rfc4952) - https://datatracker.ietf.org/doc/html/rfc4952
### [Reference](https://datatracker.ietf.org/doc/html/rfc4954) - https://datatracker.ietf.org/doc/html/rfc4954
### [Reference](https://datatracker.ietf.org/doc/html/rfc5068) - https://datatracker.ietf.org/doc/html/rfc5068
### [Reference](https://datatracker.ietf.org/doc/html/rfc524) - https://datatracker.ietf.org/doc/html/rfc524
### [Reference](https://datatracker.ietf.org/doc/html/rfc5248) - https://datatracker.ietf.org/doc/html/rfc5248
### [Reference](https://datatracker.ietf.org/doc/html/rfc5321) - https://datatracker.ietf.org/doc/html/rfc5321
### [Reference](https://datatracker.ietf.org/doc/html/rfc5322) - https://datatracker.ietf.org/doc/html/rfc5322
### [Reference](https://datatracker.ietf.org/doc/html/rfc5336) - https://datatracker.ietf.org/doc/html/rfc5336
### [Reference](https://datatracker.ietf.org/doc/html/rfc5504) - https://datatracker.ietf.org/doc/html/rfc5504
### [Reference](https://datatracker.ietf.org/doc/html/rfc6152) - https://datatracker.ietf.org/doc/html/rfc6152
### [Reference](https://datatracker.ietf.org/doc/html/rfc6409) - https://datatracker.ietf.org/doc/html/rfc6409
### [Reference](https://datatracker.ietf.org/doc/html/rfc6522) - https://datatracker.ietf.org/doc/html/rfc6522
### [Reference](https://datatracker.ietf.org/doc/html/rfc6531) - https://datatracker.ietf.org/doc/html/rfc6531
### [Reference](https://datatracker.ietf.org/doc/html/rfc772) - https://datatracker.ietf.org/doc/html/rfc772
### [Reference](https://datatracker.ietf.org/doc/html/rfc780) - https://datatracker.ietf.org/doc/html/rfc780
### [Reference](https://datatracker.ietf.org/doc/html/rfc788) - https://datatracker.ietf.org/doc/html/rfc788
### [Reference](https://datatracker.ietf.org/doc/html/rfc821) - https://datatracker.ietf.org/doc/html/rfc821
### [Reference](https://datatracker.ietf.org/doc/html/rfc822) - https://datatracker.ietf.org/doc/html/rfc822
### [Reference](https://datatracker.ietf.org/doc/html/rfc8314) - https://datatracker.ietf.org/doc/html/rfc8314
### [Reference](https://datatracker.ietf.org/doc/html/rfc8460) - https://datatracker.ietf.org/doc/html/rfc8460
### [Reference](https://datatracker.ietf.org/doc/html/rfc8461) - https://datatracker.ietf.org/doc/html/rfc8461
### [Reference](https://datatracker.ietf.org/doc/html/rfc974) - https://datatracker.ietf.org/doc/html/rfc974
### [Reference](https://api.semanticscholar.org/CorpusID:206442868) - https://api.semanticscholar.org/CorpusID:206442868
### [Reference](https://starttls-everywhere.org/) - https://starttls-everywhere.org/
### [Reference](https://uasg.tech/wp-content/uploads/2019/02/UASG021D-EN-EAI-Readiness-in-TLDs.pdf) - https://uasg.tech/wp-content/uploads/2019/02/UASG021D-EN-EAI-Readiness-in-TLDs.pdf
### [Reference](https://archive.today/20120630212728/http://home.pages.de/~mandree/qmail-bugs.html) - https://archive.today/20120630212728/http://home.pages.de/~mandree/qmail-bugs.html
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/6/69/SMTP-transfer-model.svg) - https://upload.wikimedia.org/wikipedia/commons/6/69/SMTP-transfer-model.svg